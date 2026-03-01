#!/usr/bin/env python3
"""Extract subagent JSONL transcripts into trace directories.

Two outputs per agent per scene:
  1. transcript.jsonl  — raw JSONL, 1:1 copy from Claude Code (objective source of truth)
  2. transcript.md     — human-readable markdown conversion

For shared scenes (BRIEFING, MEETING, REVIEW, PAUSE, DND) where multiple agents
share one trace dir, files are named transcript-{agent}.jsonl / .md.

Usage:
    # Extract from Claude Code's internal storage → trace dirs
    python3 scripts/extract-transcripts.py --sim-dir simulation-2-test

    # Convert already-copied JSONL files in trace dirs to readable markdown
    python3 scripts/extract-transcripts.py --sim-dir simulation-2-test --local

    # Preview without writing
    python3 scripts/extract-transcripts.py --sim-dir simulation-2-test --dry-run
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime

PROJECT_DIR = Path("/Users/jennifer/.claude/projects/-Users-jennifer-Documents-GitHub-gensoftworks")
REPO_ROOT = Path(__file__).resolve().parent.parent

AGENT_NAMES = {
    "darius": "Darius Engel",
    "emre": "Emre Yilmaz",
    "finn": "Finn Bergmann",
    "leo": "Leonie Fischer",
    "nami": "Nami Okafor",
    "tobi": "Tobias Richter",
    "vera": "Vera Kowalski",
}

# Map full names / first names to agent IDs
_NAME_TO_ID = {}
for _id, _full in AGENT_NAMES.items():
    _NAME_TO_ID[_full.lower()] = _id
    _NAME_TO_ID[_full.split()[0].lower()] = _id
    _NAME_TO_ID[_id] = _id


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_jsonl(path):
    """Parse a JSONL file into a list of entries."""
    entries = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return entries


def _extract_agent_from_prompt(prompt_text):
    """Extract agent ID from the initial prompt text.

    Supports two prompt formats:
      - Legacy: "Du bist Darius Engel — ..."
      - New:    "Du bist in einer Szene ... Reagiere als Emre ..."
    Also checks memory file paths: agents/{name}-memory.md
    """
    # 1. Legacy: "Du bist {Full Name}" — try ALL matches, not just first
    for m in re.finditer(r"Du bist (\w+ \w+)", prompt_text):
        name = m.group(1).lower()
        if name in _NAME_TO_ID:
            return _NAME_TO_ID[name]
    for m in re.finditer(r"Du bist (\w+)", prompt_text):
        name = m.group(1).lower()
        if name in _NAME_TO_ID:
            return _NAME_TO_ID[name]

    # 2. New format: "Reagiere als {Name}" or "arbeite als {Name}"
    m = re.search(r"[Rr]eagiere als (\w+)", prompt_text)
    if m:
        name = m.group(1).lower()
        if name in _NAME_TO_ID:
            return _NAME_TO_ID[name]
    m = re.search(r"arbeite.*?als (\w+)", prompt_text)
    if m:
        name = m.group(1).lower()
        if name in _NAME_TO_ID:
            return _NAME_TO_ID[name]

    # 3. Memory file path: agents/{name}-memory.md
    m = re.search(r"agents/(\w+)-memory\.md", prompt_text)
    if m:
        name = m.group(1).lower()
        if name in _NAME_TO_ID:
            return _NAME_TO_ID[name]

    # 4. Check for unique identifiers: "als {Name}" patterns
    for agent_id, full_name in AGENT_NAMES.items():
        first = full_name.split()[0]
        if re.search(rf"als {first}\b", prompt_text, re.IGNORECASE):
            return agent_id

    # 5. "{Name} (du)" pattern — agent addressed in second person
    for agent_id, full_name in AGENT_NAMES.items():
        first = full_name.split()[0]
        if re.search(rf"{first}\s*\(du\)", prompt_text, re.IGNORECASE):
            return agent_id
        # Also check short ID (e.g., "Leo (du)" for agent_id "leo")
        if re.search(rf"{agent_id}\s*\(du\)", prompt_text, re.IGNORECASE):
            return agent_id

    # 6. D&D character → agent mapping
    dnd_chars = {"kess": "nami", "kordt": "darius"}
    for char, agent in dnd_chars.items():
        if re.search(rf"du spielst {char}\b", prompt_text, re.IGNORECASE):
            return agent

    return None


def _extract_agent_from_entries(entries):
    """Extract agent ID by scanning all entries for memory file access patterns.

    Checks Read/Write tool calls for agents/{name}-memory.md paths.
    """
    memory_pattern = re.compile(r"agents/(\w+)-memory")
    for entry in entries:
        msg = entry.get("message", {})
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use" and block.get("name") in ("Read", "Write", "Edit"):
                fp = block.get("input", {}).get("file_path", "")
                m = memory_pattern.search(fp)
                if m:
                    name = m.group(1).lower()
                    if name in _NAME_TO_ID:
                        return _NAME_TO_ID[name]
    return None


def identify_trace_dir(entries, sim_dir):
    """Find the trace directory this agent writes to.

    Strategy:
      1. Look for Write tool calls targeting sim_dir/traces/
      2. Fallback: parse the initial prompt for agent name + scene context

    Returns (trace_dir_name, agent_id) or (None, None).
    """
    trace_pattern = re.compile(
        rf"{re.escape(sim_dir)}/traces/(day\d+-scene\d+-[\w-]+)/"
    )

    trace_dir_name = None
    for entry in entries:
        msg = entry.get("message", {})
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use" and block.get("name") == "Write":
                file_path = block.get("input", {}).get("file_path", "")
                m = trace_pattern.search(file_path)
                if m:
                    trace_dir_name = m.group(1)
                    break
        if trace_dir_name:
            break

    # Extract agent ID from initial prompt
    agent_id = None
    first_text = ""
    if entries:
        first_msg = entries[0].get("message", {})
        first_content = first_msg.get("content", "")
        if isinstance(first_content, str):
            first_text = first_content
            agent_id = _extract_agent_from_prompt(first_content)

    if trace_dir_name:
        # Fallback: extract agent from trace dir name
        if not agent_id:
            last = trace_dir_name.split("-")[-1]
            if last in AGENT_NAMES:
                agent_id = last
        return trace_dir_name, agent_id or "unknown"

    # --- Fallback: derive trace dir from prompt context ---
    if not agent_id:
        agent_id = _extract_agent_from_entries(entries)
    if not agent_id or not first_text:
        return None, None

    # Look for "Tag N" + "Szene M: TYPE" in prompt (with fallbacks)
    day_m = re.search(r"Tag\s+(\d+)", first_text)
    if not day_m:
        weekday_map = {"Montag": 1, "Dienstag": 2, "Mittwoch": 3, "Donnerstag": 4, "Freitag": 5}
        for wd, num in weekday_map.items():
            if wd in first_text:
                day_m = type("M", (), {"group": lambda self, n, _v=num: str(_v)})()
                break
    scene_m = re.search(r"Szene\s+(\d+)(?::\s*([\w&]+))?", first_text)
    if not scene_m and day_m:
        type_m = re.search(r"\b(BRIEFING|WORK|MEETING|PAUSE|REVIEW|DND|D&D|Meeting|Pause|Review)\b", first_text)
        if type_m:
            sn = _infer_scene_num(int(day_m.group(1)), type_m.group(1).upper())
            if sn:
                scene_m = type("M", (), {
                    "group": lambda self, n, _s=sn, _t=type_m.group(1).upper(): str(_s) if n == 1 else _t
                })()
    if not day_m or not scene_m:
        return None, None

    day_num = int(day_m.group(1))
    scene_num = int(scene_m.group(1))
    scene_type = (scene_m.group(2) or "").upper()

    # For shared scenes, we can't assign turn numbers here — caller must handle
    trace_dir_name = f"day{day_num:02d}-scene{scene_num}-{agent_id}"
    return trace_dir_name, agent_id


# Scene types where multiple agents share a directory (conversation rounds)
SHARED_SCENE_TYPES = {"BRIEFING", "MEETING", "PAUSE", "REVIEW", "DND"}


# Scene type → scene number mapping per day (from logbook)
_DAY_SCENE_MAP = {
    1: {"BRIEFING": 1, "WORK": 2, "MEETING": 3, "PAUSE": 4, "REVIEW": 5},
    2: {"BRIEFING": 1, "WORK": 2, "MEETING": 3, "PAUSE": 4, "REVIEW": 5},
    3: {"BRIEFING": 1, "WORK": 2, "MEETING": 3, "PAUSE": 4, "REVIEW": 5},
    4: {"BRIEFING": 1, "WORK": 2, "MEETING": 3, "PAUSE": 4, "DND": 5},
    5: {"BRIEFING": 1, "WORK": 2, "MEETING": 3, "PAUSE": 4, "REVIEW": 5},
}


def _infer_scene_num(day, scene_type):
    """Infer scene number from day + scene type using logbook structure."""
    # Normalize D&D → DND
    if scene_type == "D&D":
        scene_type = "DND"
    day_map = _DAY_SCENE_MAP.get(day, {})
    return day_map.get(scene_type)


def _parse_scene_from_prompt(entries):
    """Extract (day, scene_num, scene_type, agent_id) from the first entry's prompt.

    Supports both legacy and new prompt formats:
      - Legacy: "Tag 1, Szene 2: WORK"
      - New:    "Tag 2 (Dienstag), Szene 3: MEETING"

    Returns (day, scene, type, agent_id) or (None, None, None, None).
    """
    if not entries:
        return None, None, None, None

    first_msg = entries[0].get("message", {})
    prompt = first_msg.get("content", "")
    if not isinstance(prompt, str):
        return None, None, None, None

    # Match various prompt formats:
    #   "Tag 1, Szene 2: WORK"
    #   "Tag 2 (Dienstag), Szene 3: MEETING"
    #   "**Tag:** 2 ... **Szene:** 5 — REVIEW"
    day_m = re.search(r"Tag[:\s*]*\*?\*?\s*(\d+)", prompt)
    if not day_m:
        # Fallback: weekday → day number
        weekday_map = {"Montag": 1, "Dienstag": 2, "Mittwoch": 3, "Donnerstag": 4, "Freitag": 5}
        for wd, num in weekday_map.items():
            if wd in prompt:
                day_m = type("M", (), {"group": lambda self, n: str(num)})()
                break
    scene_m = re.search(r"Szene[:\s*]*\*?\*?\s*(\d+)\s*(?::\s*|—\s*|\s+)([\w&]+)", prompt)
    if not scene_m:
        # Fallback: infer scene number from scene type when explicit "Szene N" is missing
        type_m = re.search(r"\b(BRIEFING|WORK|MEETING|PAUSE|REVIEW|DND)\b", prompt)
        if type_m and day_m:
            scene_type = type_m.group(1)
            scene_num = _infer_scene_num(int(day_m.group(1)), scene_type)
            if scene_num:
                scene_m = type("M", (), {
                    "group": lambda self, n, _s=scene_num, _t=scene_type: str(_s) if n == 1 else _t
                })()
    if not day_m or not scene_m:
        return None, None, None, None

    day = int(day_m.group(1))
    scene_num = int(scene_m.group(1))
    scene_type = scene_m.group(2).upper()
    agent_id = _extract_agent_from_prompt(prompt)

    # Fallback: scan all entries for memory file access
    if not agent_id:
        agent_id = _extract_agent_from_entries(entries)

    return day, scene_num, scene_type, agent_id


def identify_trace_dir_from_prompt(entries, turn_number=None):
    """Fallback: derive trace dir name from the agent's initial prompt.

    For WORK scenes: day01-scene2-emre
    For shared scenes: day01-scene1-t1-finn (with turn number)

    Returns (trace_dir_name, agent_id) or (None, None).
    """
    day, scene_num, scene_type, agent_id = _parse_scene_from_prompt(entries)
    if day is None or agent_id is None:
        return None, None

    prefix = f"day{day:02d}-scene{scene_num}"

    if scene_type in SHARED_SCENE_TYPES:
        if turn_number is None:
            return None, None
        trace_dir_name = f"{prefix}-t{turn_number}-{agent_id}"
    else:
        # WORK or other individual scenes
        trace_dir_name = f"{prefix}-{agent_id}"

    return trace_dir_name, agent_id


def _stem_name(trace_dir_name, agent_id):
    """Return the file stem: 'transcript' or 'transcript-{agent}'."""
    last_part = trace_dir_name.split("-")[-1]
    is_shared = last_part not in AGENT_NAMES
    if is_shared and agent_id != "unknown":
        return f"transcript-{agent_id}"
    return "transcript"


# ---------------------------------------------------------------------------
# Formatting — JSONL → readable markdown
# ---------------------------------------------------------------------------

def format_transcript(entries):
    """Convert JSONL entries into a readable markdown transcript."""
    lines = []

    for entry in entries:
        entry_type = entry.get("type", "")
        msg = entry.get("message", {})
        role = msg.get("role", "")
        content = msg.get("content", "")
        timestamp = entry.get("timestamp", "")

        if entry_type == "progress":
            continue

        ts_str = ""
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                ts_str = f" [{dt.strftime('%H:%M:%S')}]"
            except (ValueError, TypeError):
                pass

        if role == "user" and entry_type == "user":
            if isinstance(content, str):
                if content.startswith("This session is being continued from a previous conversation"):
                    lines.append(f"---\n### CONTEXT COMPACTION{ts_str}\n")
                else:
                    lines.append(f"---\n### USER PROMPT{ts_str}\n")
                lines.append(content)
                lines.append("")
            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_result":
                        result = block.get("content", "")
                        is_error = block.get("is_error", False)
                        if isinstance(result, str) and len(result) > 2000:
                            result = result[:2000] + "\n... [truncated]"
                        prefix = "ERROR" if is_error else "RESULT"
                        lines.append(f"\n**{prefix}**{ts_str}:\n```\n{result}\n```\n")

        elif role == "assistant":
            if isinstance(content, list):
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") == "text":
                        text = block.get("text", "").strip()
                        if text:
                            lines.append(f"\n**ASSISTANT**{ts_str}:\n{text}\n")
                    elif block.get("type") == "tool_use":
                        tool_name = block.get("name", "")
                        tool_input = block.get("input", {})
                        if tool_name == "Write":
                            fp = tool_input.get("file_path", "")
                            preview = tool_input.get("content", "")
                            if len(preview) > 500:
                                preview = preview[:500] + "\n... [truncated]"
                            lines.append(f"\n**TOOL: Write**{ts_str} → `{fp}`\n```\n{preview}\n```\n")
                        elif tool_name == "Read":
                            fp = tool_input.get("file_path", "")
                            lines.append(f"\n**TOOL: Read**{ts_str} → `{fp}`\n")
                        elif tool_name in ("Glob", "Grep"):
                            pat = tool_input.get("pattern", "")
                            lines.append(f"\n**TOOL: {tool_name}**{ts_str} → `{pat}`\n")
                        elif tool_name == "Edit":
                            fp = tool_input.get("file_path", "")
                            old = tool_input.get("old_string", "")[:100]
                            lines.append(f"\n**TOOL: Edit**{ts_str} → `{fp}` (old: `{old}...`)\n")
                        elif tool_name == "Bash":
                            cmd = tool_input.get("command", "")
                            lines.append(f"\n**TOOL: Bash**{ts_str} → `{cmd[:200]}`\n")
                        else:
                            lines.append(f"\n**TOOL: {tool_name}**{ts_str}\n```json\n{json.dumps(tool_input, ensure_ascii=False)[:500]}\n```\n")
            elif isinstance(content, str) and content.strip():
                lines.append(f"\n**ASSISTANT**{ts_str}:\n{content}\n")

    return "\n".join(lines)


def _make_header(trace_dir_name, entries, source_info=""):
    """Build the markdown header block."""
    header = f"# Transcript: {trace_dir_name}\n\n"
    if source_info:
        header += f"{source_info}\n"
    header += f"Entries: {len(entries)}\n"
    if entries:
        ts = entries[0].get("timestamp", "")
        if ts:
            header += f"Start: {ts}\n"
        ts_end = entries[-1].get("timestamp", "")
        if ts_end:
            header += f"End: {ts_end}\n"
    header += "\n---\n\n"
    return header


# ---------------------------------------------------------------------------
# Mode 1: Extract from Claude Code internal storage
# ---------------------------------------------------------------------------

def find_sessions():
    """Find all session directories with subagent JSONL files."""
    sessions = []
    if not PROJECT_DIR.exists():
        return sessions
    for d in PROJECT_DIR.iterdir():
        if d.is_dir() and (d / "subagents").is_dir():
            jsonl_files = list((d / "subagents").glob("agent-*.jsonl"))
            if jsonl_files:
                sessions.append((d.name, jsonl_files))
    return sessions


def _identify_gm_day(entries, sim_dir):
    """Identify which simulation day a GM session covers by scanning logbook writes.

    Returns a set of day numbers (e.g. {6}) or empty set.
    """
    days = set()
    pattern = re.compile(rf"{re.escape(sim_dir)}/logbook/day(\d+)(?:-scene\d+)?\.json")
    for entry in entries:
        msg = entry.get("message", {})
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use" and block.get("name") in ("Write", "Edit"):
                fp = block.get("input", {}).get("file_path", "")
                m = pattern.search(fp)
                if m:
                    days.add(int(m.group(1)))
    return days


def extract_from_storage(args):
    """Scan Claude Code's JSONL storage, copy raw + generate markdown."""
    sim_dir = args.sim_dir
    traces_root = REPO_ROOT / sim_dir / "traces"

    if not traces_root.exists():
        print(f"Traces directory not found: {traces_root}")
        sys.exit(1)

    if not args.session:
        print("Error: --session is required for extract mode (prevents scanning wrong sessions).")
        sys.exit(1)

    sessions = find_sessions()
    if not sessions:
        print("No subagent JSONL files found.")
        sys.exit(1)

    if args.session:
        sessions = [(sid, files) for sid, files in sessions if sid.startswith(args.session)]
        if not sessions:
            print(f"No sessions matching prefix '{args.session}'")
            sys.exit(1)

    total_found = 0
    total_written = 0
    total_skipped = 0

    # --- Phase 1: Pre-scan all JONLs to assign turn numbers for shared scenes ---
    # Structure: {(session_id, scene_key): [(timestamp, agent_id, jsonl_path, entries), ...]}
    scene_groups = {}
    all_agent_data = []

    for session_id, jsonl_files in sorted(sessions):
        for jsonl_path in sorted(jsonl_files):
            if "compact" in jsonl_path.name:
                continue

            entries = parse_jsonl(jsonl_path)
            if not entries:
                continue

            # Try Write-based identification first
            trace_dir_name, agent_id = identify_trace_dir(entries, sim_dir)
            if trace_dir_name:
                all_agent_data.append((session_id, jsonl_path, entries, trace_dir_name, agent_id, None))
                continue

            # Fallback: parse scene info from prompt
            day, scene_num, scene_type, agent_id = _parse_scene_from_prompt(entries)
            if day is None or agent_id is None:
                total_skipped += 1
                print(f"  SKIP {jsonl_path.name} (cannot identify trace dir or scene)")
                continue

            # Get timestamp for ordering
            ts = entries[0].get("timestamp", "")

            if scene_type in SHARED_SCENE_TYPES:
                scene_key = (day, scene_num, scene_type)
                scene_groups.setdefault(scene_key, []).append(
                    (ts, agent_id, jsonl_path, entries, session_id)
                )
            else:
                prefix = f"day{day:02d}-scene{scene_num}"
                trace_dir_name = f"{prefix}-{agent_id}"
                all_agent_data.append((session_id, jsonl_path, entries, trace_dir_name, agent_id, None))

    # Assign shared scene agents to individual dirs (day{N}-scene{M}-{agent}).
    # When multiple JONLs exist for the same agent+scene, keep the one with the
    # most entries (= the most complete transcript).
    for scene_key, agents in scene_groups.items():
        day, scene_num, scene_type = scene_key
        prefix = f"day{day:02d}-scene{scene_num}"
        # Group by agent_id, keep longest
        by_agent = {}
        for ts, agent_id, jsonl_path, entries, session_id in agents:
            key = agent_id
            if key not in by_agent or len(entries) > len(by_agent[key][2]):
                by_agent[key] = (session_id, jsonl_path, entries)
        for agent_id, (session_id, jsonl_path, entries) in by_agent.items():
            trace_dir_name = f"{prefix}-{agent_id}"
            all_agent_data.append((session_id, jsonl_path, entries, trace_dir_name, agent_id, None))

    # --- Phase 1b: Deduplicate — when multiple JONLs map to the same trace dir,
    # keep the one with the most entries (most complete transcript).
    deduped = {}
    for item in all_agent_data:
        session_id, jsonl_path, entries, trace_dir_name, agent_id, turn_num = item
        if trace_dir_name not in deduped or len(entries) > len(deduped[trace_dir_name][2]):
            deduped[trace_dir_name] = item
    all_agent_data = list(deduped.values())

    # --- Phase 2: Write all transcripts ---
    for session_id, jsonl_path, entries, trace_dir_name, agent_id, turn_num in all_agent_data:
        total_found += 1
        target_dir = traces_root / trace_dir_name
        stem = _stem_name(trace_dir_name, agent_id)
        raw_file = target_dir / f"{stem}.jsonl"
        md_file = target_dir / f"{stem}.md"

        if args.dry_run:
            print(f"  {jsonl_path.name} → {trace_dir_name}/{stem}.jsonl + .md ({len(entries)} entries)")
            continue

        if raw_file.exists() and not args.overwrite:
            print(f"  SKIP {trace_dir_name}/{stem} (exists, use --overwrite)")
            continue

        target_dir.mkdir(parents=True, exist_ok=True)

        # 1. Copy raw JSONL
        shutil.copy2(jsonl_path, raw_file)

        # 2. Generate readable markdown
        source_info = f"Session: `{session_id}`\nSource: `{jsonl_path.name}`"
        header = _make_header(trace_dir_name, entries, source_info)
        transcript = format_transcript(entries)
        md_file.write_text(header + transcript, encoding="utf-8")

        raw_kb = raw_file.stat().st_size / 1024
        md_kb = md_file.stat().st_size / 1024
        total_written += 1
        print(f"  {trace_dir_name}/{stem} — jsonl: {raw_kb:.0f} KB, md: {md_kb:.0f} KB ({len(entries)} entries)")

    # --- Extract GM session transcripts ---
    gm_written = 0
    session_ids_with_agents = {sid for sid, _ in sessions}
    for session_id in sorted(session_ids_with_agents):
        gm_jsonl = PROJECT_DIR / f"{session_id}.jsonl"
        if not gm_jsonl.exists():
            continue

        entries = parse_jsonl(gm_jsonl)
        if not entries:
            continue

        days = _identify_gm_day(entries, sim_dir)
        if not days:
            continue

        for day_num in sorted(days):
            trace_dir_name = f"day{day_num:02d}-gm"
            target_dir = traces_root / trace_dir_name
            raw_file = target_dir / "transcript.jsonl"
            md_file = target_dir / "transcript.md"

            if args.dry_run:
                size_mb = gm_jsonl.stat().st_size / (1024 * 1024)
                print(f"  {session_id}.jsonl → {trace_dir_name}/transcript.jsonl + .md ({size_mb:.1f} MB, {len(entries)} entries)")
                continue

            if raw_file.exists() and not args.overwrite:
                print(f"  SKIP {trace_dir_name}/transcript (exists, use --overwrite)")
                continue

            target_dir.mkdir(parents=True, exist_ok=True)

            # 1. Copy raw JSONL
            shutil.copy2(gm_jsonl, raw_file)

            # 2. Generate readable markdown
            source_info = f"Session: `{session_id}`\nRole: Game Master (Opus 4.6)"
            header = _make_header(trace_dir_name, entries, source_info)
            transcript = format_transcript(entries)
            md_file.write_text(header + transcript, encoding="utf-8")

            raw_kb = raw_file.stat().st_size / 1024
            md_kb = md_file.stat().st_size / 1024
            gm_written += 1
            print(f"  {trace_dir_name}/transcript — jsonl: {raw_kb:.0f} KB, md: {md_kb:.0f} KB ({len(entries)} entries)")

    skipped_info = f", {total_skipped} unidentified" if total_skipped else ""
    print(f"\nDone. Agents: {total_found} found, {total_written} written{skipped_info}. GM: {gm_written} written.")


# ---------------------------------------------------------------------------
# Mode 2: Convert local JSONL files already in trace dirs
# ---------------------------------------------------------------------------

def convert_local(args):
    """Find transcript*.jsonl files in trace dirs and generate .md from them."""
    traces_root = REPO_ROOT / args.sim_dir / "traces"

    if not traces_root.exists():
        print(f"Traces directory not found: {traces_root}")
        sys.exit(1)

    jsonl_files = sorted(traces_root.rglob("transcript*.jsonl"))
    if not jsonl_files:
        print("No transcript JSONL files found in trace dirs.")
        sys.exit(1)

    total = 0
    for jsonl_path in jsonl_files:
        md_path = jsonl_path.with_suffix(".md")
        trace_dir_name = jsonl_path.parent.name

        if md_path.exists() and not args.overwrite:
            print(f"  SKIP {trace_dir_name}/{md_path.name} (exists)")
            continue

        entries = parse_jsonl(jsonl_path)
        if not entries:
            print(f"  SKIP {trace_dir_name}/{jsonl_path.name} (empty)")
            continue

        if args.dry_run:
            print(f"  {trace_dir_name}/{jsonl_path.name} → {md_path.name} ({len(entries)} entries)")
            continue

        header = _make_header(trace_dir_name, entries, f"Source: `{jsonl_path.name}`")
        transcript = format_transcript(entries)
        md_path.write_text(header + transcript, encoding="utf-8")

        md_kb = md_path.stat().st_size / 1024
        total += 1
        print(f"  {trace_dir_name}/{md_path.name} ({md_kb:.0f} KB, {len(entries)} entries)")

    print(f"\nDone. Converted {total} JSONL files to markdown.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract & convert subagent JSONL transcripts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Workflow:
  1. After simulation: run without --local to copy raw JONLs + generate markdown
  2. To regenerate markdown from existing JONLs: run with --local
        """,
    )
    parser.add_argument("--sim-dir", required=True, help="Simulation directory name (e.g. simulation-2-test)")
    parser.add_argument("--session", help="Filter by session ID prefix (extract mode only)")
    parser.add_argument("--local", action="store_true", help="Convert local JSONL files instead of extracting from Claude storage")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    if args.local:
        convert_local(args)
    else:
        extract_from_storage(args)


if __name__ == "__main__":
    main()
