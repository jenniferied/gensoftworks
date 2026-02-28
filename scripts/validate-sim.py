#!/usr/bin/env python3
"""Validate a GenSoftworks simulation directory against schemas.

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

# --- Constants ---
VALID_TYPES = {"BRIEFING", "WORK", "MEETING", "PAUSE", "REVIEW", "DND"}
VALID_AGENTS = {"finn", "darius", "emre", "nami", "vera", "tobi", "leo"}
LOCATION_BY_TYPE = {
    "WORK": {"alle-stationen"},
    "BRIEFING": {"küche"},
    "MEETING": {"küche"},
    "REVIEW": {"küche"},
    "PAUSE": {"küche"},
    "DND": {"bibliothek"},
}
CONV_TYPES = {"BRIEFING", "MEETING", "REVIEW", "PAUSE", "DND"}
SCENE_FIELDS = {"day", "scene", "type", "time", "location", "participants",
                "summary", "dialogue", "artifacts", "cd_feedback",
                "trace_dirs", "metrics"}
SUMMARY_FIELDS = {"day", "weekday", "phase", "title", "summary",
                  "cd_decisions", "artifacts", "key_moments"}
ARTIFACT_HEADER_FIELDS = {"dokument", "titel", "version", "autor", "status", "datum"}
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

        # Field check
        entry_fields = set(entry.keys())
        missing = SCENE_FIELDS - entry_fields
        extra = entry_fields - SCENE_FIELDS
        if missing:
            err(f, f"Missing fields: {', '.join(sorted(missing))}")
        if extra:
            err(f, f"Extra fields: {', '.join(sorted(extra))}")

        # Day matches filename
        if entry.get("day") != day_num:
            err(f, f"day={entry.get('day')} doesn't match filename day{day_num:02d}")

        # Scene matches filename
        if entry.get("scene") != scene_num:
            err(f, f"scene={entry.get('scene')} doesn't match filename scene{scene_num}")

        # Type valid
        scene_type = entry.get("type", "")
        if scene_type not in VALID_TYPES:
            err(f, f"Invalid type: {scene_type}")

        # Location valid per type
        location = entry.get("location", "")
        allowed_locs = LOCATION_BY_TYPE.get(scene_type, set())
        if allowed_locs and location not in allowed_locs:
            err(f, f"Location '{location}' not allowed for {scene_type} (expected: {allowed_locs})")

        # Time check (scenes 1-3 = morning, 4-6 = afternoon)
        time_val = entry.get("time", "")
        if scene_num <= 3 and time_val != "morning":
            err(f, f"Scene {scene_num} should be 'morning', got '{time_val}'")
        if scene_num >= 4 and time_val != "afternoon":
            err(f, f"Scene {scene_num} should be 'afternoon', got '{time_val}'")

        # Participants not empty
        participants = entry.get("participants", [])
        if not participants:
            err(f, "participants is empty")

        # Dialogue check for conversation scenes
        dialogue = entry.get("dialogue", [])
        if scene_type in CONV_TYPES and not dialogue:
            err(f, f"Conversation scene ({scene_type}) has empty dialogue")
        if scene_type == "WORK" and dialogue:
            err(f, "WORK scene should have empty dialogue")

        # Metrics
        if "metrics" not in entry or not entry.get("metrics"):
            err(f, "metrics missing or empty")


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

        entry_fields = set(entry.keys())
        missing = SUMMARY_FIELDS - entry_fields
        if missing:
            err(f, f"Missing fields: {', '.join(sorted(missing))}")

        # Check for wrong field name
        if "artifacts_produced" in entry_fields:
            err(f, "Field 'artifacts_produced' should be 'artifacts'")

        # Weekday check
        weekday = entry.get("weekday", "")
        if weekday not in GERMAN_WEEKDAYS:
            err(f, f"weekday '{weekday}' not a valid German weekday")


def check_traces(sim_dir, logbook_dir, day_filter=None):
    traces_dir = sim_dir / "traces"
    if not traces_dir.exists():
        err(traces_dir, "traces/ directory not found")
        return

    expected_files = {"0-prompt.md", "1-reasoning.md", "2-output.md"}

    # Collect trace_dirs from logbook
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

        trace_dirs = entry.get("trace_dirs", [])
        for td in trace_dirs:
            td_path = traces_dir / td
            if not td_path.exists():
                err(f, f"trace_dirs entry '{td}' not found on disk")
                continue

            actual_files = {p.name for p in td_path.iterdir() if p.is_file()}
            missing = expected_files - actual_files
            extra = actual_files - expected_files
            if missing:
                err(td_path, f"Missing trace files: {', '.join(sorted(missing))}")
            if extra:
                err(td_path, f"Extra trace files: {', '.join(sorted(extra))}")

            # Check non-empty
            for tf in expected_files:
                tf_path = td_path / tf
                if tf_path.exists() and tf_path.stat().st_size == 0:
                    err(tf_path, "Empty trace file")

            # Check prompt header
            prompt_path = td_path / "0-prompt.md"
            if prompt_path.exists():
                first_line = prompt_path.read_text().split("\n", 1)[0]
                if not first_line.startswith("# "):
                    err(prompt_path, f"Prompt doesn't start with '# ' header")


def check_artifacts(gallery_dir):
    file_pattern = re.compile(r"^(\d{2})-(.+)-v(\d+)\.md$")
    for doc_type in ("gdd", "wbb"):
        doc_dir = gallery_dir / doc_type
        if not doc_dir.exists():
            continue
        for f in sorted(doc_dir.glob("*.md")):
            m = file_pattern.match(f.name)
            if not m:
                err(f, f"Filename doesn't match NN-titel-vN.md pattern")
                continue

            file_version = int(m.group(3))
            text = f.read_text()

            # Check YAML frontmatter
            if not text.startswith("---"):
                err(f, "Missing YAML frontmatter")
                continue

            try:
                end = text.index("---", 3)
            except ValueError:
                err(f, "Unclosed YAML frontmatter")
                continue

            block = text[3:end].strip()
            meta = {}
            for line in block.splitlines():
                if ":" not in line:
                    continue
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")

            missing = ARTIFACT_HEADER_FIELDS - set(meta.keys())
            if missing:
                err(f, f"Frontmatter missing: {', '.join(sorted(missing))}")

            # Version consistency
            fm_version = meta.get("version", "")
            try:
                if int(fm_version) != file_version:
                    err(f, f"Frontmatter version={fm_version} != filename v{file_version}")
            except (ValueError, TypeError):
                err(f, f"Frontmatter version '{fm_version}' is not an integer")


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


def check_world(state_dir, logbook_dir):
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


def check_concept_art(gallery_dir):
    concepts_dir = gallery_dir / "concepts"
    if not concepts_dir.exists():
        return
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        for f in concepts_dir.rglob(ext):
            # Just check files exist and aren't empty
            if f.stat().st_size == 0:
                err(f, "Empty image file")


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
    gallery_dir = sim_dir / "gallery"
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

    if gallery_dir.exists():
        check_artifacts(gallery_dir)
        check_concept_art(gallery_dir)

    check_memories(agents_dir)

    if state_dir.exists():
        check_world(state_dir, logbook_dir)
    else:
        err(state_dir, "state/ directory not found")

    # Report
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
