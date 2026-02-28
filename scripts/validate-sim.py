#!/usr/bin/env python3
"""Validate a GenSoftworks simulation directory.

Checks the essentials: dialogue in conversation scenes, trace integrity,
summary field names, agent memories, world.json.

Usage:
    python scripts/validate-sim.py --sim-dir simulation-2
    python scripts/validate-sim.py --sim-dir simulation-2-test --day 3
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VALID_TYPES = {"BRIEFING", "WORK", "MEETING", "PAUSE", "REVIEW", "DND"}
VALID_AGENTS = {"finn", "darius", "emre", "nami", "vera", "tobi", "leo"}
CONV_TYPES = {"BRIEFING", "MEETING", "REVIEW", "PAUSE", "DND"}
GERMAN_WEEKDAYS = {"Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag",
                   "Samstag", "Sonntag"}

errors = []


def err(file, msg):
    errors.append((str(file), msg))


def check_logbook(logbook_dir, day_filter=None):
    pattern = re.compile(r"day(\d+)-scene(\d+)\.json$")
    files = sorted(logbook_dir.glob("day*-scene*.json"))
    if not files:
        err(logbook_dir, "No logbook scene files found")
        return

    for f in files:
        m = pattern.match(f.name)
        if not m:
            continue
        day_num = int(m.group(1))
        scene_num = int(m.group(2))
        if day_filter and day_num != day_filter:
            continue

        try:
            entry = json.loads(f.read_text())
        except json.JSONDecodeError as e:
            err(f, f"Invalid JSON: {e}")
            continue

        # Scene number matches filename
        if entry.get("scene") != scene_num:
            err(f, f"scene={entry.get('scene')} doesn't match filename scene{scene_num}")

        # Type valid
        scene_type = entry.get("type", "")
        if scene_type not in VALID_TYPES:
            err(f, f"Invalid type: {scene_type}")

        # Participants not empty
        if not entry.get("participants"):
            err(f, "participants is empty")

        # Dialogue: conversation scenes must have it, WORK must not
        dialogue = entry.get("dialogue", [])
        if scene_type in CONV_TYPES and not dialogue:
            err(f, f"Conversation scene ({scene_type}) has empty dialogue")
        if scene_type == "WORK" and dialogue:
            err(f, "WORK scene should have empty dialogue")


def check_summaries(logbook_dir, day_filter=None):
    pattern = re.compile(r"day(\d+)-summary\.json$")
    for f in sorted(logbook_dir.glob("day*-summary.json")):
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

        # Wrong field name
        if "artifacts_produced" in entry:
            err(f, "Field 'artifacts_produced' should be 'artifacts'")

        # Weekday check
        weekday = entry.get("weekday", "")
        if weekday and weekday not in GERMAN_WEEKDAYS:
            err(f, f"weekday '{weekday}' not a valid German weekday")


def check_traces(sim_dir, logbook_dir, day_filter=None):
    traces_dir = sim_dir / "traces"
    if not traces_dir.exists():
        err(traces_dir, "traces/ directory not found")
        return

    expected_files = {"0-prompt.md", "1-reasoning.md", "2-output.md"}

    # Check trace_dirs referenced from logbook
    pattern = re.compile(r"day(\d+)-scene(\d+)\.json$")
    for f in sorted(logbook_dir.glob("day*-scene*.json")):
        m = pattern.match(f.name)
        if not m:
            continue
        day_num = int(m.group(1))
        if day_filter and day_num != day_filter:
            continue

        try:
            entry = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue

        for td in entry.get("trace_dirs", []):
            td_path = traces_dir / td
            if not td_path.exists():
                err(f, f"trace_dirs entry '{td}' not found on disk")
                continue

            actual_files = {p.name for p in td_path.iterdir() if p.is_file()}
            missing = expected_files - actual_files
            if missing:
                err(td_path, f"Missing trace files: {', '.join(sorted(missing))}")

            for tf in expected_files:
                tf_path = td_path / tf
                if tf_path.exists() and tf_path.stat().st_size == 0:
                    err(tf_path, "Empty trace file")


def check_memories(agents_dir):
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
        check_summaries(logbook_dir, args.day)
        check_traces(sim_dir, logbook_dir, args.day)
    else:
        err(logbook_dir, "logbook/ directory not found")

    check_memories(agents_dir)

    if state_dir.exists():
        check_world(state_dir)
    else:
        err(state_dir, "state/ directory not found")

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
