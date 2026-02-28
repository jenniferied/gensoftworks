#!/usr/bin/env python3
"""Migrate per-scene logbook JSONs to single dayDD.json index files.

Merges dayDD-sceneS.json + dayDD-summary.json → dayDD.json per day.
Only keeps metadata + summaries — dialogue lives in transcript.md files.

Usage:
    python scripts/migrate-to-day-index.py --sim-dir simulation-2-test
    python scripts/migrate-to-day-index.py --sim-dir simulation-2-test --dry-run
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SCENE_FIELDS = ("scene", "type", "time", "location", "participants",
                "summary", "artifacts", "cd_feedback")


def migrate(sim_dir: Path, dry_run: bool = False):
    logbook_dir = sim_dir / "logbook"
    if not logbook_dir.exists():
        print(f"Error: {logbook_dir} not found", file=sys.stderr)
        sys.exit(1)

    # Discover days from per-scene files
    scene_re = re.compile(r"day(\d+)-scene(\d+)\.json$")
    scenes_by_day: dict[int, list[tuple[int, Path]]] = {}
    for f in sorted(logbook_dir.glob("day*-scene*.json")):
        m = scene_re.match(f.name)
        if not m:
            continue
        day_num = int(m.group(1))
        scene_num = int(m.group(2))
        scenes_by_day.setdefault(day_num, []).append((scene_num, f))

    if not scenes_by_day:
        print("No per-scene JSON files found.", file=sys.stderr)
        sys.exit(1)

    files_to_delete = []

    for day_num in sorted(scenes_by_day.keys()):
        scene_files = sorted(scenes_by_day[day_num])

        # Build scenes array (metadata only)
        scenes = []
        for scene_num, f in scene_files:
            raw = json.loads(f.read_text())
            scene = {k: raw[k] for k in SCENE_FIELDS if k in raw}
            scenes.append(scene)
            files_to_delete.append(f)

        # Load day summary
        summary_file = logbook_dir / f"day{day_num:02d}-summary.json"
        day_index = {"day": day_num, "scenes": scenes}

        if summary_file.exists():
            summary = json.loads(summary_file.read_text())
            for k in ("weekday", "phase", "title", "summary",
                       "cd_decisions", "key_moments", "artifacts"):
                if k in summary:
                    day_index[k] = summary[k]
            files_to_delete.append(summary_file)

        # Write merged file
        out_file = logbook_dir / f"day{day_num:02d}.json"
        if dry_run:
            print(f"[dry-run] Would write {out_file} ({len(scenes)} scenes)")
        else:
            out_file.write_text(json.dumps(day_index, ensure_ascii=False, indent=2))
            print(f"Wrote {out_file} ({len(scenes)} scenes)")

    # Delete old files
    for f in files_to_delete:
        if dry_run:
            print(f"[dry-run] Would delete {f.name}")
        else:
            f.unlink()
            print(f"Deleted {f.name}")

    print(f"\nMigrated {len(scenes_by_day)} days, "
          f"{'would delete' if dry_run else 'deleted'} {len(files_to_delete)} files.")


def main():
    parser = argparse.ArgumentParser(description="Migrate logbook to day-index format")
    parser.add_argument("--sim-dir", required=True, help="Simulation directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    sim_dir = ROOT / args.sim_dir
    if not sim_dir.exists():
        print(f"Error: {sim_dir} not found", file=sys.stderr)
        sys.exit(1)

    migrate(sim_dir, args.dry_run)


if __name__ == "__main__":
    main()
