#!/usr/bin/env python3
"""
Batch-export all GDD/WBB version PDFs using the compact template.

Re-renders existing .md exports (v0.1, v0.2, v0.3) with document-compact.tex
which has all font sizes reduced by 1pt.

Usage:
    python scripts/export-compact-batch.py
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
EXPORT_DIR = PROJECT_ROOT / "simulation-2" / "export"
TEMPLATE = PROJECT_ROOT / "templates" / "document-compact.tex"
FONTPATH = str((PROJECT_ROOT / "assets" / "fonts").resolve()) + "/"

MAX_IMAGE_WIDTH = 1600
JPEG_QUALITY = 85

# All 6 markdown files to re-export
MD_FILES = [
    "Meier_KIComputerRollenspiele_AnhangB_GDD_v0.1_2026.md",
    "Meier_KIComputerRollenspiele_AnhangB_GDD_v0.2_2026.md",
    "Meier_KIComputerRollenspiele_AnhangB_GDD_v0.3_2026.md",
    "Meier_KIComputerRollenspiele_AnhangB_WBB_v0.1_2026.md",
    "Meier_KIComputerRollenspiele_AnhangB_WBB_v0.2_2026.md",
    "Meier_KIComputerRollenspiele_AnhangB_WBB_v0.3_2026.md",
]


def optimize_images(md_path: Path, img_dir: Path) -> Path:
    """Copy referenced images to img_dir, scaled to MAX_IMAGE_WIDTH."""
    content = md_path.read_text()
    img_re = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    seen: dict[str, Path] = {}

    for m in img_re.finditer(content):
        rel_path = m.group(2)
        src = (md_path.parent / rel_path).resolve()
        if not src.exists() or src.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        if str(src) in seen:
            continue

        dst = img_dir / src.name
        shutil.copy2(src, dst)

        result = subprocess.run(
            ["sips", "-g", "pixelWidth", str(dst)],
            capture_output=True, text=True,
        )
        width_line = [l for l in result.stdout.splitlines() if "pixelWidth" in l]
        if width_line:
            w = int(width_line[0].split()[-1])
            if w > MAX_IMAGE_WIDTH:
                subprocess.run(
                    ["sips", "--resampleWidth", str(MAX_IMAGE_WIDTH), str(dst)],
                    capture_output=True,
                )

        if dst.suffix.lower() == ".png":
            jpg_dst = dst.with_suffix(".jpg")
            subprocess.run(
                ["sips", "-s", "format", "jpeg",
                 "-s", "formatOptions", str(JPEG_QUALITY), str(dst),
                 "--out", str(jpg_dst)],
                capture_output=True,
            )
            if jpg_dst.exists():
                dst.unlink()
                dst = jpg_dst

        seen[str(src)] = dst

    def replace_path(match: re.Match) -> str:
        alt = match.group(1)
        rel = match.group(2)
        src = (md_path.parent / rel).resolve()
        if str(src) in seen:
            return f"![{alt}]({seen[str(src)]})"
        return match.group(0)

    patched = img_re.sub(replace_path, content)
    patched_md = img_dir / md_path.name
    patched_md.write_text(patched)
    return patched_md


def build_pdf(md_path: Path, output_pdf: Path) -> int:
    """Convert Markdown to PDF via Pandoc + XeLaTeX with compact template."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # Patch template with absolute font path
        template_text = TEMPLATE.read_text()
        template_text = template_text.replace(
            "Path = ../assets/fonts/,",
            f"Path = {FONTPATH},",
        )
        template_text = template_text.replace(
            "\\def\\fontpath{../assets/fonts/}",
            f"\\def\\fontpath{{{FONTPATH}}}",
        )
        patched_template = tmp_path / "document-compact.tex"
        patched_template.write_text(template_text)

        # Optimize images
        img_dir = tmp_path / "images"
        img_dir.mkdir()
        build_md = optimize_images(md_path, img_dir)

        cmd = [
            "pandoc",
            str(build_md),
            "-o", str(output_pdf),
            f"--template={patched_template}",
            "--pdf-engine=xelatex",
        ]

        print(f"  pandoc {md_path.name} -> {output_pdf.name}")
        result = subprocess.run(cmd, capture_output=True, text=True,
                                cwd=build_md.parent)
        if result.returncode != 0:
            print(f"  ERROR:\n{result.stderr[:500]}")
            return 1

        if output_pdf.exists():
            size_kb = output_pdf.stat().st_size / 1024
            print(f"  OK ({size_kb:.0f} KB)")
        return 0


def main() -> int:
    print("Compact PDF Batch Export")
    print("=" * 50)

    errors = 0
    for md_name in MD_FILES:
        md_path = EXPORT_DIR / md_name
        if not md_path.exists():
            print(f"  SKIP (not found): {md_name}")
            continue

        pdf_name = md_name.replace(".md", ".pdf")
        output_pdf = EXPORT_DIR / pdf_name
        print(f"\n[{md_name}]")
        errors += build_pdf(md_path, output_pdf)

    print(f"\nDone. Errors: {errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
