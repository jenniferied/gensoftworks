#!/usr/bin/env python3
"""
Export GenSoftworks WBB chapters as a single PDF.

Scans gallery/wbb/ for versioned chapter files (KK-titel-vN.md),
picks the highest version per chapter, concatenates into one Markdown
document, and compiles via Pandoc + LuaLaTeX.

Usage:
    python scripts/export-wbb.py --sim-dir simulation-2-test
    python scripts/export-wbb.py --sim-dir simulation-2-test --md-only
"""

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

# Chapter order (canonical WBB structure)
WBB_CHAPTERS = [
    "01-mythos",
    "02-topos",
    "03-ethos",
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
            "-V", "mainfont=Lora",
            "-V", (f"mainfontoptions=Path={fontpath},"
                   "UprightFont=Lora-Variable.ttf,"
                   "ItalicFont=Lora-Italic-Variable.ttf,"
                   "BoldFont=Lora-Variable.ttf,"
                   "BoldItalicFont=Lora-Italic-Variable.ttf,"
                   "BoldFeatures={Weight=700},"
                   "BoldItalicFeatures={Weight=700}"),
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
            "-V", "fontsize=10pt",
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
        description="Export GenSoftworks WBB as PDF")
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
    gallery_dir = sim_root / "gallery" / "wbb"
    export_dir = sim_root / "export"
    header_path = PROJECT_ROOT / "templates" / "logbook-header.tex"

    if not gallery_dir.exists():
        print(f"Gallery directory not found: {gallery_dir}")
        return 1

    print("GenSoftworks WBB Export")
    print("=" * 40)

    chapters = find_chapters(gallery_dir)
    print(f"  Found {len(chapters)} chapters:")
    for chapter_id, path in chapters:
        print(f"    {path.name}")

    doc_title = "RELICS — Worldbuilding Bible"
    md_content = build_markdown(gallery_dir, doc_title)

    export_dir.mkdir(parents=True, exist_ok=True)
    base_name = args.output_name or "wbb"
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
