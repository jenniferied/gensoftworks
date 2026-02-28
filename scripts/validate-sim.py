#!/usr/bin/env python3
"""Validate a GenSoftworks simulation directory.

Checks logbook (dayDD.json), agent memories, world.json, artifact naming,
and warns about stale trace files.

Usage:
    python scripts/validate-sim.py --sim-dir simulation-2
    python scripts/validate-sim.py --sim-dir simulation-2 --day 3
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VALID_TYPES = {"BRIEFING", "WORK", "MEETING", "PAUSE", "REVIEW", "DND"}
VALID_AGENTS = {"finn", "darius", "emre", "nami", "vera", "tobi", "leo"}
GERMAN_WEEKDAYS = {"Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag",
                   "Samstag", "Sonntag"}

errors = []
warnings = []


def err(file, msg):
    errors.append((str(file), msg))


def warn(file, msg):
    warnings.append((str(file), msg))


def check_logbook(logbook_dir, day_filter=None):
    """Check dayDD.json files (one per day)."""
    pattern = re.compile(r"day(\d+)\.json$")
    files = sorted(logbook_dir.glob("day*.json"))
    day_files = [f for f in files if pattern.match(f.name)]

    if not day_files:
        err(logbook_dir, "No logbook day files (dayDD.json) found")
        return

    for f in day_files:
        m = pattern.match(f.name)
        if not m:
            continue
        day_num = int(m.group(1))
        if day_filter and day_num != day_filter:
            continue

        try:
            entry = json.loads(f.read_text())
        except json.JSONDecodeError as e:
            err(f, f"Invalid JSON: {e}")
            continue

        # Required top-level fields
        for field in ("day", "weekday", "phase", "scenes"):
            if field not in entry:
                err(f, f"Missing required field: '{field}'")

        # Weekday check
        weekday = entry.get("weekday", "")
        if weekday and weekday not in GERMAN_WEEKDAYS:
            err(f, f"weekday '{weekday}' not a valid German weekday")

        # Wrong field name
        if "artifacts_produced" in entry:
            err(f, f"Field 'artifacts_produced' should be 'artifacts'")

        # Scenes array
        scenes = entry.get("scenes", [])
        if not isinstance(scenes, list):
            err(f, "scenes is not an array")
            continue

        for i, scene in enumerate(scenes):
            scene_label = f"scenes[{i}]"

            # Required scene fields
            for field in ("scene", "type", "time", "location", "participants", "summary"):
                if field not in scene:
                    err(f, f"{scene_label}: missing required field '{field}'")

            # Type valid
            scene_type = scene.get("type", "")
            if scene_type and scene_type not in VALID_TYPES:
                err(f, f"{scene_label}: invalid type '{scene_type}'")

            # Participants subset of valid agents
            participants = scene.get("participants", [])
            if isinstance(participants, list):
                invalid = set(participants) - VALID_AGENTS
                if invalid:
                    err(f, f"{scene_label}: invalid participants: {', '.join(sorted(invalid))}")

            # Wrong field name in scene
            if "artifacts_produced" in scene:
                err(f, f"{scene_label}: field 'artifacts_produced' should be 'artifacts'")


def check_memories(agents_dir):
    """Check all 7 agent memory files exist and are non-empty."""
    if not agents_dir.exists():
        err(agents_dir, "agents/ directory not found")
        return
    for agent in sorted(VALID_AGENTS):
        mem_file = agents_dir / f"{agent}-memory.md"
        if not mem_file.exists():
            err(mem_file, "Memory file not found")
        elif mem_file.stat().st_size == 0:
            err(mem_file, "Memory file is empty")


def check_world(state_dir):
    """Check world.json has required fields."""
    world_path = state_dir / "world.json"
    if not world_path.exists():
        err(world_path, "world.json not found")
        return
    try:
        world = json.loads(world_path.read_text())
    except json.JSONDecodeError as e:
        err(world_path, f"Invalid JSON: {e}")
        return
    if "day" not in world:
        err(world_path, "Missing 'day' field")
    if "scene" not in world:
        err(world_path, "Missing 'scene' field")


def check_artifacts(sim_dir):
    """Warn about gallery files that don't follow naming convention."""
    naming_re = re.compile(r"^\d{2}-.+-v\d+\.md$")
    for subdir in ("gallery/gdd", "gallery/wbb"):
        d = sim_dir / subdir
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if not naming_re.match(f.name):
                warn(f, f"Filename doesn't follow KK-titel-vN.md convention")


def check_stale_traces(sim_dir):
    """Warn about manual trace files (prompt.md, reasoning.md, output.md) in new trace dirs."""
    traces_dir = sim_dir / "traces"
    if not traces_dir.exists():
        return
    manual_files = {"0-prompt.md", "1-reasoning.md", "2-output.md",
                    "prompt.md", "reasoning.md", "output.md"}
    for d in sorted(traces_dir.iterdir()):
        if not d.is_dir():
            continue
        found = [f.name for f in d.iterdir() if f.name in manual_files]
        if found:
            warn(d, f"Stale manual trace files: {', '.join(sorted(found))}")


def main():
    parser = argparse.ArgumentParser(description="Validate GenSoftworks simulation directory")
    parser.add_argument("--sim-dir", required=True, help="Simulation directory (e.g. simulation-2)")
    parser.add_argument("--day", type=int, default=None, help="Validate only a specific day")
    args = parser.parse_args()

    sim_dir = ROOT / args.sim_dir
    if not sim_dir.exists():
        print(f"\033[31mError: {sim_dir} not found\033[0m")
        sys.exit(1)

    logbook_dir = sim_dir / "logbook"
    agents_dir = sim_dir / "agents"
    state_dir = sim_dir / "state"

    print(f"Validating: {sim_dir}")
    if args.day:
        print(f"  Day filter: {args.day}")
    print()

    if logbook_dir.exists():
        check_logbook(logbook_dir, args.day)
    else:
        err(logbook_dir, "logbook/ directory not found")

    check_memories(agents_dir)

    if state_dir.exists():
        check_world(state_dir)
    else:
        err(state_dir, "state/ directory not found")

    check_artifacts(sim_dir)
    check_stale_traces(sim_dir)

    if warnings:
        print(f"\033[33m{len(warnings)} warning(s):\033[0m\n")
        for filepath, msg in warnings:
            rel = str(filepath).replace(str(ROOT) + "/", "")
            print(f"  \033[33m{rel}\033[0m")
            print(f"    {msg}")
        print()

    if errors:
        print(f"\033[31m{len(errors)} error(s) found:\033[0m\n")
        for filepath, msg in errors:
            rel = str(filepath).replace(str(ROOT) + "/", "")
            print(f"  \033[33m{rel}\033[0m")
            print(f"    {msg}")
        print()
        sys.exit(1)
    else:
        print(f"\033[32mAll checks passed.\033[0m")
        sys.exit(0)


if __name__ == "__main__":
    main()
