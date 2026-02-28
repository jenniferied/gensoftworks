#!/usr/bin/env python3
"""
Export GenSoftworks GDD chapters as a single PDF.

Scans gallery/gdd/ for versioned chapter files (KK-titel-vN.md),
picks the highest version per chapter, concatenates into one Markdown
document, and compiles via Pandoc + LuaLaTeX.

Usage:
    python scripts/export-gdd.py --sim-dir simulation-2-test
    python scripts/export-gdd.py --sim-dir simulation-2-test --md-only
"""

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

# Chapter order (canonical GDD structure)
GDD_CHAPTERS = [
    "01-spieluebersicht",
    "02-kernmechaniken",
    "03-erzaehlkonzept",
    "04-schluesselfiguren",
    "05-designsprache",
    "06-technik-produktion",
]


def find_chapters(gallery_dir: Path) -> list[tuple[str, Path]]:
    """Find highest-version file for each chapter number.

    Supports both versioned (KK-titel-vN.md) and unversioned (KK-titel.md) names.
    Returns list of (chapter_id, path) sorted by chapter number.
    """
    pattern = re.compile(r"^(\d{2}-.+?)(?:-v(\d+))?\.md$")
    chapters: dict[str, list[tuple[int, Path]]] = {}

    for f in sorted(gallery_dir.glob("*.md")):
        m = pattern.match(f.name)
        if not m:
            continue
        chapter_id = m.group(1)
        version = int(m.group(2)) if m.group(2) else 0
        chapters.setdefault(chapter_id, []).append((version, f))

    result = []
    for chapter_id in sorted(chapters.keys()):
        versions = chapters[chapter_id]
        best = max(versions, key=lambda x: x[0])
        result.append((chapter_id, best[1]))

    return result


def strip_meta(content: str) -> str:
    """Strip meta-information blocks from chapter content for clean PDF export.

    Removes: YAML frontmatter, author/version/status headers, changelogs,
    blockquote annotations (V2-Ergänzung etc.), open-questions sections,
    next-steps sections, and trailing author signatures.
    """
    lines = content.split("\n")
    out: list[str] = []

    # 1. Strip YAML frontmatter (--- ... ---)
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        lines = lines[i + 1:] if i < len(lines) else lines[1:]

    # 2. Strip old-style meta header block (bold lines before first ---)
    # Pattern: lines starting with **Autor**, **Version**, **Status**, etc.
    META_PREFIXES = (
        "**Autor", "**Autorin", "**Autoren",
        "**Version", "**Status", "**Stand",
        "**Änderungslog", "**Abhängigkeiten", "**Querverweise",
        "**QA:", "**Narrativ-Sync:", "**Projekt:",
        "**Basis:", "**Prüfung gegen:",
        "**Letzte Aktualisierung:",
        "**Basis**:", "**Basis:",
        "**Prüfung gegen**:", "**Prüfung gegen:",
    )
    cleaned: list[str] = []
    in_changelog = False
    for line in lines:
        stripped = line.strip()
        # Detect start of changelog (multi-line after **Änderungslog**)
        if stripped.startswith("**Änderungslog"):
            in_changelog = True
            continue
        if in_changelog:
            if stripped.startswith("- V") or stripped.startswith("- v"):
                continue
            in_changelog = False
        if any(stripped.startswith(p) for p in META_PREFIXES):
            continue
        cleaned.append(line)
    lines = cleaned

    # 3. Strip blockquote-style status headers (> **Status:** ... lines)
    STATUS_QUOTE_RE = re.compile(
        r"^>\s*\*\*(Status|Autor|Autorin|Version|Stand|Änderungslog|Abhängigkeiten|Letzte Aktualisierung)"
    )
    cleaned = []
    skip_quote_block = False
    for line in lines:
        stripped = line.strip()
        if STATUS_QUOTE_RE.match(stripped):
            skip_quote_block = True
            continue
        if skip_quote_block:
            # Continue skipping continuation lines (> - V1 ..., > - V2 ...)
            if stripped.startswith(">"):
                continue
            skip_quote_block = False
        cleaned.append(line)
    lines = cleaned

    # 4. Strip editorial blockquotes (> V2-Ergänzung, > V2-Schärfung, > QA-Einschätzung, etc.)
    EDITORIAL_RE = re.compile(
        r"^>\s*(V\d+-|QA-|CD-|Neu:|Hinweis:|Anmerkung:)", re.IGNORECASE
    )
    lines = [l for l in lines if not EDITORIAL_RE.match(l.strip())]

    # 5. Strip "Offene Fragen" / "Nächste Schritte" sections (heading + content until next heading)
    DROP_SECTIONS = re.compile(
        r"^#{2,4}\s+(?:[\d.]+\s+|Anhang\s+\w+:\s+)?"
        r"(?:Offene\s+(?:Design-)?(?:Fragen|Punkte)|N(?:ä|ae)chste Schritte"
        r"|Zusammenfassung:\s*N(?:ä|ae)chste)",
        re.IGNORECASE,
    )
    HEADING_RE = re.compile(r"^#{1,4}\s+")
    cleaned = []
    dropping = False
    drop_level = 0
    for line in lines:
        stripped = line.strip()
        m_drop = DROP_SECTIONS.match(stripped)
        if m_drop:
            dropping = True
            drop_level = len(stripped) - len(stripped.lstrip("#"))
            continue
        if dropping:
            m_head = HEADING_RE.match(stripped)
            if m_head:
                level = len(stripped) - len(stripped.lstrip("#"))
                if level <= drop_level:
                    dropping = False
                    cleaned.append(line)
                    continue
            # Still in dropped section
            continue
        cleaned.append(line)
    lines = cleaned

    # 6. Strip inline "Offene Fragen" bold labels + following checkbox lines
    INLINE_OPEN_Q = re.compile(r"^\*\*Offene\s+Fragen", re.IGNORECASE)
    CHECKBOX_RE = re.compile(r"^- \[[ x]\] ")
    cleaned = []
    skip_checkboxes = False
    for line in lines:
        stripped = line.strip()
        if INLINE_OPEN_Q.match(stripped):
            skip_checkboxes = True
            continue
        if skip_checkboxes:
            if CHECKBOX_RE.match(stripped) or not stripped:
                continue
            skip_checkboxes = False
        cleaned.append(line)
    lines = cleaned

    # 7. Strip author signatures anywhere (*Name Surname, ... *)
    SIGNATURE_RE = re.compile(
        r"^\*[A-ZÄÖÜ][a-zäöüß]+ [A-ZÄÖÜ][a-zäöüß]+,\s+.+\*$"
    )
    lines = [l for l in lines if not SIGNATURE_RE.match(l.strip())]

    # 8. Collapse triple+ blank lines to double
    result: list[str] = []
    blank_count = 0
    for line in lines:
        if not line.strip():
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)

    return "\n".join(result).strip()


def build_markdown(gallery_dir: Path, doc_title: str) -> str:
    """Concatenate chapter files into a single Markdown document."""
    chapters = find_chapters(gallery_dir)

    if not chapters:
        print(f"No chapter files found in {gallery_dir}")
        sys.exit(1)

    lines = []
    lines.append("---")
    lines.append(f'title: "{doc_title}"')
    lines.append('author: "GenSoftworks Studio Simulation"')
    lines.append('date: "2026"')
    lines.append("lang: german")
    lines.append("toc: true")
    lines.append("---")
    lines.append("")

    for chapter_id, path in chapters:
        content = path.read_text().strip()
        content = strip_meta(content)
        lines.append(content)
        lines.append("")
        lines.append("\\clearpage")
        lines.append("")

    return "\n".join(lines)


def build_pdf(md_path: Path, output_path: Path, header_path: Path,
              tex_only: bool = False) -> int:
    """Convert Markdown to PDF via Pandoc + LuaLaTeX."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        fontpath = str((PROJECT_ROOT / "assets" / "fonts").resolve()) + "/"

        # Patch header template with absolute font/icon paths
        icons_dir = str((PROJECT_ROOT / "assets" / "icons").resolve()) + "/"
        header_text = header_path.read_text()
        header_text = header_text.replace(
            "Path = ../assets/fonts/,",
            f"Path = {fontpath},",
        )
        header_text = header_text.replace(
            "{icons/",
            "{" + icons_dir,
        )
        patched_header = tmp_path / "header.tex"
        patched_header.write_text(header_text)

        output = str(output_path.with_suffix(".tex") if tex_only
                     else output_path.with_suffix(".pdf"))
        cmd = [
            "pandoc",
            str(md_path),
            "-o", output,
            f"--include-in-header={patched_header}",
            "--pdf-engine=xelatex",
            "--toc",
            "--toc-depth=3",
            "-V", "mainfont=OpenSans",
            "-V", (f"mainfontoptions=Path={fontpath},"
                   "UprightFont=OpenSans-Variable.ttf,"
                   "ItalicFont=OpenSans-Italic-Variable.ttf,"
                   "BoldFont=OpenSans-Variable.ttf,"
                   "BoldItalicFont=OpenSans-Italic-Variable.ttf,"
                   "BoldFeatures={Weight=700}"),
            "-V", "sansfont=OpenSans",
            "-V", (f"sansfontoptions=Path={fontpath},"
                   "UprightFont=OpenSans-Variable.ttf,"
                   "ItalicFont=OpenSans-Italic-Variable.ttf,"
                   "BoldFont=OpenSans-Variable.ttf,"
                   "BoldItalicFont=OpenSans-Italic-Variable.ttf,"
                   "BoldFeatures={Weight=700}"),
            "-V", "monofont=JetBrainsMono",
            "-V", (f"monofontoptions=Path={fontpath},"
                   "UprightFont=JetBrainsMono-Variable.ttf,"
                   "Scale=0.85"),
            "-V", "fontsize=9pt",
            "-V", "geometry:margin=25mm",
        ]

        print(f"  Building: {md_path.name} -> {Path(output).name}")
        result = subprocess.run(cmd, capture_output=True, text=True,
                                cwd=md_path.parent)
        if result.returncode != 0:
            print(f"  Error:\n{result.stderr}")
            return 1

        out_path = Path(output)
        if out_path.exists():
            size_kb = out_path.stat().st_size / 1024
            print(f"  Output: {out_path} ({size_kb:.0f} KB)")
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export GenSoftworks GDD as PDF")
    parser.add_argument("--sim-dir", type=str, required=True,
                        help="Simulation directory (e.g. simulation-2-test)")
    parser.add_argument("--md-only", action="store_true",
                        help="Generate Markdown only")
    parser.add_argument("--tex-only", action="store_true",
                        help="Generate TeX only")
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Override output directory")
    parser.add_argument("--output-name", type=str, default=None,
                        help="Override output filename (without extension)")
    args = parser.parse_args()

    sim_root = PROJECT_ROOT / args.sim_dir
    gallery_dir = sim_root / "gallery" / "gdd"
    export_dir = sim_root / "export"
    header_path = PROJECT_ROOT / "templates" / "logbook-header.tex"

    if not gallery_dir.exists():
        print(f"Gallery directory not found: {gallery_dir}")
        return 1

    print("GenSoftworks GDD Export")
    print("=" * 40)

    chapters = find_chapters(gallery_dir)
    print(f"  Found {len(chapters)} chapters:")
    for chapter_id, path in chapters:
        print(f"    {path.name}")

    doc_title = "RELICS — Game Design Document"
    md_content = build_markdown(gallery_dir, doc_title)

    export_dir.mkdir(parents=True, exist_ok=True)
    base_name = args.output_name or "Meier_KIComputerRollenspiele_Sim2Test_GDD_2026"
    md_path = export_dir / f"{base_name}.md"
    md_path.write_text(md_content)
    print(f"  Markdown: {md_path}")

    if args.md_only:
        return 0

    if args.output_dir:
        pdf_dir = Path(args.output_dir).resolve()
        pdf_dir.mkdir(parents=True, exist_ok=True)
    else:
        pdf_dir = export_dir

    output_path = pdf_dir / base_name
    return build_pdf(md_path, output_path, header_path, tex_only=args.tex_only)


if __name__ == "__main__":
    sys.exit(main())
