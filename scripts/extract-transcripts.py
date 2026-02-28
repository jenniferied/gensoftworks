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
    """Extract agent ID from the initial prompt text."""
    m = re.search(r"Du bist (\w+ \w+)", prompt_text)
    if m:
        name = m.group(1).lower()
        if name in _NAME_TO_ID:
            return _NAME_TO_ID[name]
    m = re.search(r"Du bist (\w+)", prompt_text)
    if m:
        name = m.group(1).lower()
        if name in _NAME_TO_ID:
            return _NAME_TO_ID[name]
    return None


def identify_trace_dir(entries, sim_dir):
    """Find the trace directory this agent writes to.

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

    if not trace_dir_name:
        return None, None

    # Extract agent ID from initial prompt
    agent_id = None
    if entries:
        first_msg = entries[0].get("message", {})
        first_content = first_msg.get("content", "")
        if isinstance(first_content, str):
            agent_id = _extract_agent_from_prompt(first_content)

    # Fallback: extract from trace dir name
    if not agent_id:
        last = trace_dir_name.split("-")[-1]
        if last in AGENT_NAMES:
            agent_id = last

    return trace_dir_name, agent_id or "unknown"


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
    pattern = re.compile(rf"{re.escape(sim_dir)}/logbook/day(\d+)-scene\d+\.json")
    for entry in entries:
        msg = entry.get("message", {})
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use" and block.get("name") == "Write":
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

    # --- Extract agent transcripts ---
    for session_id, jsonl_files in sorted(sessions):
        for jsonl_path in sorted(jsonl_files):
            if "compact" in jsonl_path.name:
                continue

            entries = parse_jsonl(jsonl_path)
            if not entries:
                continue

            trace_dir_name, agent_id = identify_trace_dir(entries, sim_dir)
            if not trace_dir_name:
                continue

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

    print(f"\nDone. Agents: {total_found} found, {total_written} written. GM: {gm_written} written.")


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
