#!/usr/bin/env python3
"""
Export GenSoftworks logbook as readable PDF.

Reads logbook JSONL + agent memory streams, weaves them into a
chronological Markdown narrative, then compiles via Pandoc + LuaLaTeX.

Supports both v1 (simulation 1) and v2 (simulation 2+) log schemas.
Exhaustive mode (default): shows ALL data including agent_details,
narrative transcripts, full memory streams with evidence chains.

Usage:
    python scripts/export-logbook.py                          # All days
    python scripts/export-logbook.py --day 1                  # Single day
    python scripts/export-logbook.py --md-only                # Markdown only (no PDF)
    python scripts/export-logbook.py --tex-only               # Generate .tex (no PDF)
    python scripts/export-logbook.py --sim-dir simulation-1   # Archived simulation
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

PROJECT_ROOT = Path(__file__).parent.parent

# Agent display names
AGENT_NAMES = {
    "emre": "Emre Yilmaz",
    "vera": "Vera Kowalski",
    "darius": "Darius Engel",
    "nami": "Nami Okafor",
    "tobi": "Tobi Richter",
    "leo": "Leo Fischer",
    "finn": "Finn Bergmann",
}

# Scene type labels (German)
SCENE_LABELS = {
    "ARRIVAL": "Ankunft",
    "ENCOUNTER": "Begegnung",
    "WORK": "Arbeit",
    "MEETING": "Meeting",
    "EVENT": "Ereignis",
    "REFLECTION": "Reflexion",
    "WORK+REFLECTION": "Arbeit & Reflexion",
    "BRIEF": "Briefing",
    "BRIEF+REACTION": "Briefing & Reaktion",
    "DELIVERY": "Lieferung",
    "RETROSPECTIVE": "Retrospektive",
    "SOCIAL": "Sozial",
    # v4 scene types (sim-2-test daily schedule)
    "BRIEFING": "Briefing",
    "PAUSE": "Pause",
    "DND": "D\\&D",
}

TIME_LABELS = {
    "morning": "Morgen",
    "late-morning": "Vormittag",
    "midday": "Mittag",
    "afternoon": "Nachmittag",
    "late-afternoon": "Spätnachmittag",
    "evening": "Abend",
    "morning-to-evening": "Ganztags",
}

POST_TYPE_LABELS = {
    "brief": "Creative Director — Brief",
    "feedback": "Creative Director — Feedback",
    "course-correction": "Creative Director — Kurskorrektur",
    "note": "Creative Director — Notiz",
    "answers-to-team": "Creative Director — Antworten",
    "feedback+deadlines": "Creative Director — Feedback \\& Deadlines",
    "feedback+budget": "Creative Director — Feedback \\& Budget",
    "feedback+direction": "Creative Director — Feedback \\& Richtung",
    "feedback+final-direction": "Creative Director — Abschluss-Feedback",
    "vision-update": "Creative Director — Vision-Update",
}

MEMORY_TYPE_LABELS = {
    "observation": "Beobachtung",
    "reflection": "Reflexion",
    "plan": "Plan",
    "artifact": "Artefakt",
    "conversation": "Gespräch",
}

DEPTH_LABELS = {
    0: "",
    1: "Synthese",
    2: "Tiefe Reflexion",
}


def detect_schema(entry):
    """Detect whether entry uses v1 or v2 schema."""
    if "mood" in entry and isinstance(entry["mood"], dict):
        return "v2"
    return "v1"


def load_bulletin(bulletin_path) -> dict[tuple[int, int], list[dict]]:
    """Load CD posts from bulletin board, indexed by (day, scene)."""
    posts_by_scene: dict[tuple[int, int], list[dict]] = {}
    if not bulletin_path.exists():
        return posts_by_scene
    data = json.loads(bulletin_path.read_text())
    for post in data.get("posts", []):
        key = (post.get("day", 0), post.get("scene", 0))
        posts_by_scene.setdefault(key, []).append(post)
    return posts_by_scene


def load_bulletin_notes(bulletin_path) -> str:
    """Load the initial CD note from bulletin."""
    if not bulletin_path.exists():
        return ""
    data = json.loads(bulletin_path.read_text())
    return data.get("creative_director_notes", "")


def load_all_memories(memories_dir) -> dict[str, dict]:
    """Load all memory entries from all agents, keyed by memory ID."""
    memories = {}
    if not memories_dir.exists():
        return memories
    for mem_file in memories_dir.glob("*.jsonl"):
        for line in mem_file.read_text().strip().splitlines():
            if not line.strip():
                continue
            entry = json.loads(line)
            memories[entry["id"]] = entry
    return memories


def load_logbook_day(logbook_dir, day: int) -> list[dict]:
    """Load all scenes for a given day.

    Supports both JSONL format (day-NNN.jsonl) and individual JSON files
    (dayDD-sceneS.json) used by sim-2-test+.
    """
    # Try JSONL first
    path = logbook_dir / f"day-{day:03d}.jsonl"
    if path.exists():
        scenes = []
        for line in path.read_text().strip().splitlines():
            if not line.strip():
                continue
            scenes.append(json.loads(line))
        return scenes

    # Try individual JSON files (v4 format)
    import re
    pattern = re.compile(rf"day{day:02d}-scene(\d+)\.json$")
    scene_files = []
    for f in sorted(logbook_dir.glob(f"day{day:02d}-scene*.json")):
        m = pattern.match(f.name)
        if m:
            scene_files.append((int(m.group(1)), f))
    if scene_files:
        return [json.loads(f.read_text()) for _, f in sorted(scene_files)]

    return []


def get_available_days(logbook_dir) -> list[int]:
    """Find all day numbers that have logbook files.

    Supports both JSONL (day-NNN.jsonl) and individual JSON (dayDD-sceneS.json).
    """
    import re
    days = set()
    # JSONL format
    for path in sorted(logbook_dir.glob("day-*.jsonl")):
        try:
            num = int(path.stem.split("-")[1])
            days.add(num)
        except (IndexError, ValueError):
            continue
    # v4 individual JSON format
    pattern = re.compile(r"day(\d+)-scene\d+\.json$")
    for path in sorted(logbook_dir.glob("day*-scene*.json")):
        m = pattern.match(path.name)
        if m:
            days.add(int(m.group(1)))
    return sorted(days)


def agent_name(agent_id: str) -> str:
    return AGENT_NAMES.get(agent_id, agent_id.title())


def format_participants(participants: list[str]) -> str:
    names = [agent_name(p) for p in participants if p != "creative-director"]
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} und {names[1]}"
    return ", ".join(names[:-1]) + f" und {names[-1]}"


def format_participant_icons(participants: list[str]) -> str:
    icons = []
    for p in participants:
        if p in AGENT_NAMES:
            icons.append(f"\\agenticon{{{p}}}")
    return "".join(icons)


def get_memory_text(mem):
    """Get text from memory (handles both 'description' and 'content' field names)."""
    return mem.get("description", mem.get("content", ""))


def esc(text):
    """Escape special chars for LaTeX via Pandoc markdown."""
    if not text:
        return ""
    return str(text).replace("→", "$\\rightarrow$")


# ---------------------------------------------------------------------------
# Screenshot Cropping
# ---------------------------------------------------------------------------

def crop_screenshot(src_path: Path, dst_dir: Path) -> Path:
    """Copy screenshot to dst_dir (no cropping — capture-scenes.mjs handles sizing)."""
    import shutil
    dst_path = dst_dir / src_path.name
    shutil.copy2(src_path, dst_path)
    return dst_path


# ---------------------------------------------------------------------------
# Rendering: Agent Details
# ---------------------------------------------------------------------------

def render_agent_details(agent_details):
    """Render per-agent emotional arc data as markdown."""
    if not agent_details:
        return ""
    lines = []
    for agent_id, details in agent_details.items():
        name = agent_name(agent_id)
        icon = f"\\agenticon{{{agent_id}}}" if agent_id in AGENT_NAMES else ""

        lines.append("::: {.agentdetail}")
        lines.append(f"{icon} \\textbf{{{name}}}")
        lines.append("")

        mood_b = details.get("mood_before", "")
        mood_a = details.get("mood_after", "")
        if mood_b and mood_a:
            lines.append(f"- *Stimmung:* {esc(mood_b)} $\\rightarrow$ {esc(mood_a)}")

        influences = details.get("influences", [])
        if influences:
            for inf in influences:
                lines.append(f"- *Einfluss:* {esc(inf)}")

        reaction = details.get("key_reaction", "")
        if reaction:
            lines.append(f"- *Reaktion:* {esc(reaction)}")

        arc = details.get("emotional_arc", "")
        if arc:
            lines.append(f"- *Bogen:* {esc(arc)}")

        frustration = details.get("frustration_level", "")
        if frustration:
            lines.append(f"- *Frustration:* {esc(frustration)}")

        lines.append(":::")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Rendering: All Memories (no filtering)
# ---------------------------------------------------------------------------

def render_all_memories(memory_ids, all_memories):
    """Render ALL memories for a scene, grouped by agent, with full metadata."""
    if not memory_ids:
        return ""

    # Group by agent
    by_agent: dict[str, list[tuple[str, dict]]] = {}
    for mid in memory_ids:
        mem = all_memories.get(mid)
        if not mem:
            continue
        agent_id = mid.rsplit("-", 1)[0]
        by_agent.setdefault(agent_id, []).append((mid, mem))

    if not by_agent:
        return ""

    lines = []
    for agent_id in sorted(by_agent.keys()):
        entries = by_agent[agent_id]
        for mid, mem in entries:
            mem_type = mem.get("type", "observation")
            depth = mem.get("depth", 0)
            importance = mem.get("importance", 5)
            text = get_memory_text(mem)
            evidence = mem.get("evidence", [])

            type_label = MEMORY_TYPE_LABELS.get(mem_type, mem_type)
            depth_label = DEPTH_LABELS.get(depth, "")

            # Choose div class based on type
            if mem_type == "reflection":
                div_class = "reflection"
            elif mem_type == "artifact":
                div_class = "artifact"
            elif mem_type == "plan":
                div_class = "thought"
            elif mem_type == "conversation":
                div_class = "thought"
            else:
                div_class = "thought"

            # Build header
            header_parts = [type_label]
            if depth_label:
                header_parts.append(depth_label)
            header = " · ".join(header_parts)
            stars = importance

            name = agent_name(agent_id)
            icon = f"\\agenticon{{{agent_id}}}" if agent_id in AGENT_NAMES else ""

            # Type-specific bubble icon
            if mem_type == "reflection":
                bubble = "\\reflectionbubble"
            elif mem_type == "plan":
                bubble = "\\planbubble"
            elif mem_type == "artifact":
                bubble = "\\artifactbubble"
            elif mem_type == "conversation":
                bubble = "\\speechbubble"
            else:
                bubble = "\\thoughtbubble"

            lines.append(f"::: {{.{div_class}}}")
            lines.append(
                f"{icon}{bubble} \\textbf{{{name} — {header}"
                f" (\\stmark{{{stars}}}):}} {esc(text)}"
            )

            # Evidence chain
            if evidence:
                lines.append("")
                evidence_str = ", ".join(f"`{e}`" for e in evidence)
                lines.append(f"*Basiert auf: {evidence_str}*")

            # Artifact path
            if mem_type == "artifact":
                path = mem.get("metadata", {}).get("artifact_path", "")
                if path:
                    lines.append("")
                    lines.append(f"`{path}`")

            lines.append(":::")
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Scene Rendering: v1 (exhaustive)
# ---------------------------------------------------------------------------

def render_scene_v1(scene, all_memories, cd_posts, day, screenshot_dir=None, crop_dir=None):
    """Render a v1 scene with ALL available data."""
    lines = []
    scene_num = scene.get("scene", 0)
    scene_type = SCENE_LABELS.get(scene.get("type", ""), scene.get("type", ""))
    lines.append(f"## Szene {scene_num} · {scene_type}")
    lines.append("")

    # Scene metadata
    time = TIME_LABELS.get(scene.get("time_of_day", ""), scene.get("time_of_day", ""))
    location = scene.get("location", "").replace("-", " ").title()
    participant_list = scene.get("participants", [])
    participants = format_participants(participant_list)
    icons = format_participant_icons(participant_list)

    lines.append("::: {.scenemeta}")
    lines.append(f"{time} — {location}\\")
    lines.append(f"{icons} {participants}")
    lines.append(":::")
    lines.append("")

    # Screenshot embedding
    if screenshot_dir:
        pattern = f"day-{day:03d}-scene-{scene_num:03d}-*.png"
        matches = list(screenshot_dir.glob(pattern))
        if matches:
            img_path = matches[0]
            if crop_dir:
                img_path = crop_screenshot(img_path, crop_dir)
            lines.append("```{=latex}")
            lines.append("\\begin{wrapfigure}{l}{0.4\\textwidth}")
            lines.append("  \\vspace{-4mm}")
            lines.append(f"  \\includegraphics[width=0.38\\textwidth]{{{img_path}}}")
            lines.append("  \\vspace{-4mm}")
            lines.append("\\end{wrapfigure}")
            lines.append("```")
            lines.append("")

    # Trigger
    trigger = scene.get("trigger")
    if trigger:
        lines.append(f"*Auslöser: {esc(trigger)}*")
        lines.append("")

    # CD posts from bulletin board
    scene_posts = cd_posts.get((day, scene_num), [])
    for post in scene_posts:
        label = POST_TYPE_LABELS.get(post.get("type", ""), "Creative Director")
        content = esc(post.get("content", ""))
        lines.append("::: {.directive}")
        lines.append(f"\\textbf{{{label}}}")
        lines.append("")
        lines.append(content)
        lines.append(":::")
        lines.append("")

    # Summary
    summary = esc(scene.get("summary", ""))
    lines.append(summary)
    lines.append("")

    # Narrative transcript (full screenplay dialogue)
    transcript = scene.get("narrative_transcript")
    if transcript:
        lines.append("### Szenenprotokoll")
        lines.append("")
        lines.append("::: {.transcript}")
        lines.append(transcript)
        lines.append(":::")
        lines.append("")

    # Agent details (emotional arcs per agent)
    agent_details = scene.get("agent_details", {})
    if agent_details:
        lines.append("### Agenten-Reaktionen")
        lines.append("")
        lines.append(render_agent_details(agent_details))

    # ALL memories (no filtering)
    memory_ids = scene.get("memories_created", [])
    if memory_ids:
        lines.append("### Erinnerungen")
        lines.append("")
        lines.append(render_all_memories(memory_ids, all_memories))

    # Artifacts
    artifacts = scene.get("artifacts", [])
    if artifacts:
        for art in artifacts:
            if isinstance(art, dict):
                art_name = art.get("name", art.get("path", str(art)))
                art_desc = art.get("description", "")
                if art_desc:
                    lines.append(f"*Artefakt: `{art_name}` — {esc(art_desc)}*")
                else:
                    lines.append(f"*Artefakt: `{art_name}`*")
            else:
                filename = Path(art).name
                lines.append(f"*Artefakt: `{filename}`*")
            lines.append("")

    # Key moment
    key_moment = scene.get("key_moment")
    if key_moment:
        lines.append(f"\\textbf{{Schlüsselmoment:}} *{esc(key_moment)}*")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Scene Rendering: v2 (exhaustive)
# ---------------------------------------------------------------------------

def render_scene_v2(scene, cd_posts, day, screenshot_dir=None, crop_dir=None, traces_dir=None):
    """Render a v2 scene with ALL available data."""
    lines = []
    scene_num = scene.get("scene", 0)
    scene_type = SCENE_LABELS.get(scene.get("type", ""), scene.get("type", ""))
    lines.append(f"## Szene {scene_num} · {scene_type}")
    lines.append("")

    time = TIME_LABELS.get(scene.get("time", ""), scene.get("time", ""))
    location = scene.get("location", "").replace("-", " ").title()
    participant_list = scene.get("participants", [])
    participants = format_participants(participant_list)
    icons = format_participant_icons(participant_list)

    lines.append("::: {.scenemeta}")
    lines.append(f"{time} — {location}\\")
    lines.append(f"{icons} {participants}")
    lines.append(":::")
    lines.append("")

    # Screenshot embedding (wrapfigure: image left, text wraps right)
    if screenshot_dir:
        pattern = f"day-{day:03d}-scene-{scene_num:03d}-*.png"
        matches = list(screenshot_dir.glob(pattern))
        if matches:
            img_path = matches[0]
            if crop_dir:
                img_path = crop_screenshot(img_path, crop_dir)
            lines.append("```{=latex}")
            lines.append("\\begin{wrapfigure}{l}{0.4\\textwidth}")
            lines.append("  \\vspace{-4mm}")
            lines.append(f"  \\includegraphics[width=0.38\\textwidth]{{{img_path}}}")
            lines.append("  \\vspace{-4mm}")
            lines.append("\\end{wrapfigure}")
            lines.append("```")
            lines.append("")

    # Trigger
    trigger = scene.get("trigger")
    if trigger:
        lines.append(f"*Auslöser: {esc(trigger)}*")
        lines.append("")

    # CD directives from bulletin
    scene_posts = cd_posts.get((day, scene_num), [])
    for post in scene_posts:
        label = POST_TYPE_LABELS.get(post.get("type", ""), "Creative Director")
        content = esc(post.get("content", ""))
        lines.append("::: {.directive}")
        lines.append(f"\\textbf{{{label}}}")
        lines.append("")
        lines.append(content)
        lines.append(":::")
        lines.append("")

    # CD feedback inline
    cd_fb = scene.get("cd_feedback")
    if cd_fb:
        lines.append("::: {.directive}")
        lines.append("\\textbf{Creative Director --- Feedback}")
        lines.append("")
        lines.append(esc(cd_fb))
        lines.append(":::")
        lines.append("")

    # Summary
    summary = esc(scene.get("summary", ""))
    lines.append(summary)
    lines.append("")

    # Narrative transcript
    transcript = scene.get("narrative_transcript")
    if transcript:
        lines.append("### Szenenprotokoll")
        lines.append("")
        lines.append("::: {.transcript}")
        lines.append(transcript)
        lines.append(":::")
        lines.append("")

    # Dialogue
    dialogue = scene.get("dialogue", [])
    if dialogue:
        for line_d in dialogue:
            who = agent_name(line_d["who"])
            icon = (
                f"\\agenticon{{{line_d['who']}}}"
                if line_d["who"] in AGENT_NAMES
                else ""
            )
            says = esc(line_d["says"])
            lines.append(f"{icon}\\speechbubble \\textbf{{{who}:}} \"{says}\"")
            lines.append("")

    # Thoughts
    thoughts = scene.get("thoughts", [])
    if thoughts:
        for t in thoughts:
            who = agent_name(t["who"])
            icon = (
                f"\\agenticon{{{t['who']}}}"
                if t["who"] in AGENT_NAMES
                else ""
            )
            thinks = esc(t["thinks"])
            lines.append("::: {.thought}")
            lines.append(f"{icon}\\thoughtbubble \\textbf{{{who} denkt:}} {thinks}")
            lines.append(":::")
            lines.append("")

    # Feedback
    feedback = scene.get("feedback", [])
    if feedback:
        for fb in feedback:
            from_name = agent_name(fb["from"])
            to_name = agent_name(fb["to"])
            icon = (
                f"\\agenticon{{{fb['from']}}}"
                if fb["from"] in AGENT_NAMES
                else ""
            )
            text = esc(fb["text"])
            lines.append("::: {.feedback}")
            lines.append(
                f"{icon}\\feedbackbubble \\textbf{{{from_name}"
                f" $\\rightarrow$ {to_name}:}} {text}"
            )
            lines.append(":::")
            lines.append("")

    # Agent details (if present in v2 data)
    agent_details = scene.get("agent_details", {})
    if agent_details:
        lines.append("### Agenten-Reaktionen")
        lines.append("")
        lines.append(render_agent_details(agent_details))

    # Mood (v2 compact format)
    mood = scene.get("mood", {})
    if mood:
        mood_parts = []
        for agent_id, m in mood.items():
            name = agent_name(agent_id)
            mood_parts.append(
                f"{name} ({m.get('before', '?')}"
                f" $\\rightarrow$ {m.get('after', '?')})"
            )
        lines.append(f"*Stimmung: {', '.join(mood_parts)}*")
        lines.append("")

    # Memories (v2 inline format)
    memories = scene.get("memories", [])
    if memories:
        lines.append("### Erinnerungen")
        lines.append("")
        for mem in memories:
            who = agent_name(mem["who"])
            icon = (
                f"\\agenticon{{{mem['who']}}}"
                if mem["who"] in AGENT_NAMES
                else ""
            )
            text = esc(mem.get("text", ""))
            imp = mem.get("importance", 5)
            lines.append(
                f"{icon} *{who} [{mem['id']}]"
                f" (\\stmark{{{imp}}}):* {text}"
            )
        lines.append("")

    # Artifacts
    artifacts = scene.get("artifacts", [])
    if artifacts:
        for art in artifacts:
            if isinstance(art, dict):
                art_name = art.get("name", art.get("path", str(art)))
                art_desc = art.get("description", "")
                if art_desc:
                    lines.append(f"*Artefakt: `{art_name}` — {esc(art_desc)}*")
                else:
                    lines.append(f"*Artefakt: `{art_name}`*")
            else:
                filename = Path(art).name
                lines.append(f"*Artefakt: `{filename}`*")
            lines.append("")

    # Full trace contents (very small font)
    trace_dir_names = scene.get("trace_dirs", [])
    if trace_dir_names and traces_dir and traces_dir.exists():
        for td_name in trace_dir_names:
            td_path = traces_dir / td_name
            if not td_path.is_dir():
                continue
            for trace_file in sorted(td_path.glob("*.md")):
                label = trace_file.stem  # e.g. "0-prompt", "1-reasoning", "2-output"
                content = trace_file.read_text().strip()
                if not content:
                    continue
                lines.append(f"**{td_name}/{label}**")
                lines.append("")
                lines.append("```{=latex}")
                lines.append("\\begingroup\\scriptsize")
                lines.append("```")
                lines.append("")
                lines.append(content)
                lines.append("")
                lines.append("```{=latex}")
                lines.append("\\endgroup")
                lines.append("```")
                lines.append("")

    # Key moment
    key_moment = scene.get("key_moment")
    if key_moment:
        lines.append(f"\\textbf{{Schlüsselmoment:}} *{esc(key_moment)}*")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Routing + Day/Document Rendering
# ---------------------------------------------------------------------------

def render_scene(scene, all_memories, cd_posts, day, screenshot_dir=None, crop_dir=None, traces_dir=None):
    """Route to v1 or v2 renderer based on schema."""
    schema = detect_schema(scene)
    if schema == "v2":
        return render_scene_v2(scene, cd_posts, day, screenshot_dir, crop_dir, traces_dir)
    return render_scene_v1(scene, all_memories, cd_posts, day, screenshot_dir, crop_dir)


DAY_NAMES = {1: "Montag", 2: "Dienstag", 3: "Mittwoch", 4: "Donnerstag", 5: "Freitag"}


def render_day(day, scenes, all_memories, cd_posts, world_path, bulletin_path,
               screenshot_dir=None, crop_dir=None, traces_dir=None):
    """Render a full day as Markdown."""
    day_of_week = DAY_NAMES.get(day, "")
    if world_path.exists() and not day_of_week:
        world = json.loads(world_path.read_text())
        if world.get("day") == day:
            day_of_week = world.get("day_of_week", "")

    lines = []
    lines.append(f"# Tag {day} — {day_of_week}")
    lines.append("")

    # Initial CD note (day 1 only)
    if day == 1:
        cd_note = load_bulletin_notes(bulletin_path)
        if cd_note:
            lines.append("::: {.directive}")
            lines.append("\\textbf{Creative Director --- Auftrag}")
            lines.append("")
            lines.append(f"*{cd_note}*")
            lines.append(":::")
            lines.append("")

    # Day-level CD posts (scene: 0) — show before any scenes
    day_start_posts = cd_posts.get((day, 0), [])
    for post in day_start_posts:
        label = POST_TYPE_LABELS.get(post.get("type", ""), "Creative Director")
        content = esc(post.get("content", ""))
        lines.append("::: {.directive}")
        lines.append(f"\\textbf{{{label}}}")
        lines.append("")
        lines.append(content)
        lines.append(":::")
        lines.append("")

    for scene in scenes:
        lines.append(render_scene(scene, all_memories, cd_posts, day, screenshot_dir, crop_dir, traces_dir))
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def build_markdown(logbook_dir, memories_dir, world_path, bulletin_path,
                   days_filter=None, screenshot_dir=None, crop_dir=None,
                   traces_dir=None):
    """Build the full Markdown document."""
    all_memories = load_all_memories(memories_dir)
    cd_posts = load_bulletin(bulletin_path)
    available = get_available_days(logbook_dir)

    if not available:
        print("No logbook files found.")
        sys.exit(1)

    if days_filter:
        available = [d for d in available if d in days_filter]

    if not available:
        print("No matching days found.")
        sys.exit(1)

    if len(available) == 1:
        subtitle = f"Tag {available[0]}"
    else:
        subtitle = f"Tag {available[0]}–{available[-1]}"

    lines = []
    lines.append("---")
    lines.append('title: "GenSoftworks — Logbuch"')
    lines.append(f'subtitle: "{subtitle}"')
    lines.append('author: "GenSoftworks Studio Simulation"')
    lines.append('date: "2026"')
    lines.append("lang: german")
    lines.append("toc: true")
    lines.append("---")
    lines.append("")

    for day in available:
        scenes = load_logbook_day(logbook_dir, day)
        if scenes:
            lines.append(render_day(day, scenes, all_memories, cd_posts,
                                    world_path, bulletin_path, screenshot_dir,
                                    crop_dir, traces_dir))

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Lua filter for Pandoc fenced-div -> LaTeX environments
# ---------------------------------------------------------------------------

LUA_FILTER = r"""
function Div(el)
  local classes = el.classes

  if classes:includes("scenemeta") then
    return {
      pandoc.RawBlock("latex", "\\begin{scenemeta}"),
      el,
      pandoc.RawBlock("latex", "\\end{scenemeta}")
    }
  end

  if classes:includes("thought") then
    return {
      pandoc.RawBlock("latex", "\\begin{thought}"),
      el,
      pandoc.RawBlock("latex", "\\end{thought}")
    }
  end

  if classes:includes("reflection") then
    return {
      pandoc.RawBlock("latex", "\\begin{reflection}"),
      el,
      pandoc.RawBlock("latex", "\\end{reflection}")
    }
  end

  if classes:includes("artifact") then
    return {
      pandoc.RawBlock("latex", "\\begin{artifact}"),
      el,
      pandoc.RawBlock("latex", "\\end{artifact}")
    }
  end

  if classes:includes("directive") then
    return {
      pandoc.RawBlock("latex", "\\begin{directive}"),
      el,
      pandoc.RawBlock("latex", "\\end{directive}")
    }
  end

  if classes:includes("feedback") then
    return {
      pandoc.RawBlock("latex", "\\begin{feedbackbox}"),
      el,
      pandoc.RawBlock("latex", "\\end{feedbackbox}")
    }
  end

  if classes:includes("agentdetail") then
    return {
      pandoc.RawBlock("latex", "\\begin{agentdetail}"),
      el,
      pandoc.RawBlock("latex", "\\end{agentdetail}")
    }
  end

  if classes:includes("transcript") then
    return {
      pandoc.RawBlock("latex", "\\begin{transcript}"),
      el,
      pandoc.RawBlock("latex", "\\end{transcript}")
    }
  end

  return el
end

function HorizontalRule(el)
  return pandoc.RawBlock("latex", "\\scenedivider")
end
"""


# ---------------------------------------------------------------------------
# PDF Build + Main
# ---------------------------------------------------------------------------

def build_pdf(md_path, output_path, header_path, tex_only=False):
    """Convert Markdown to PDF via Pandoc + LuaLaTeX."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        filter_path = tmp_path / "logbook-filter.lua"
        filter_path.write_text(LUA_FILTER)

        tex_path = output_path.with_suffix(".tex")
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
        patched_header = tmp_path / "logbook-header.tex"
        patched_header.write_text(header_text)

        output = str(tex_path) if tex_only else str(output_path.with_suffix(".pdf"))
        cmd = [
            "pandoc",
            str(md_path),
            "-o", output,
            f"--include-in-header={patched_header}",
            f"--lua-filter={filter_path}",
            "--pdf-engine=xelatex",
            "--toc",
            "--toc-depth=2",
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
            "-V", f"monofont=JetBrainsMono",
            "-V", (f"monofontoptions=Path={fontpath},"
                   "UprightFont=JetBrainsMono-Variable.ttf,"
                   "Scale=0.85"),
            "-V", "fontsize=9pt",
            "-V", "geometry:margin=25mm",
        ]

        print(f"  Building: {md_path.name} -> {Path(output).name}")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=md_path.parent)
        if result.returncode != 0:
            print(f"  Error:\n{result.stderr}")
            return 1

        out_path = Path(output)
        if out_path.exists():
            size_kb = out_path.stat().st_size / 1024
            print(f"  Output: {out_path} ({size_kb:.0f} KB)")
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Export GenSoftworks logbook as PDF")
    parser.add_argument("--day", type=int, help="Export a single day")
    parser.add_argument("--md-only", action="store_true", help="Generate Markdown only")
    parser.add_argument("--tex-only", action="store_true", help="Generate TeX only")
    parser.add_argument("--sim-dir", type=str, default=None,
                        help="Path to simulation archive dir (e.g. simulation-1)")
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Override output directory for PDF (e.g. /path/to/_export)")
    parser.add_argument("--output-name", type=str, default=None,
                        help="Override output filename (without extension)")
    args = parser.parse_args()

    days = [args.day] if args.day else None

    if args.sim_dir:
        sim_root = PROJECT_ROOT / args.sim_dir
        logbook_dir = sim_root / "logbook"
        memories_dir = sim_root / "state" / "memories"
        world_path = sim_root / "state" / "world.json"
        bulletin_path = sim_root / "state" / "bulletin.json"
        export_dir = sim_root / "export"
        screenshot_dir = sim_root / "screenshots"
    else:
        logbook_dir = PROJECT_ROOT / "logbook"
        memories_dir = PROJECT_ROOT / "state" / "memories"
        world_path = PROJECT_ROOT / "state" / "world.json"
        bulletin_path = PROJECT_ROOT / "state" / "bulletin.json"
        export_dir = PROJECT_ROOT / "export"
        screenshot_dir = PROJECT_ROOT / "screenshots"

    header_path = PROJECT_ROOT / "templates" / "logbook-header.tex"

    print("GenSoftworks Logbook Export (Vollständig)")
    print("=" * 40)

    # Crop screenshots into a temp dir (originals stay untouched)
    crop_tmpdir = None
    crop_dir = None
    if screenshot_dir.exists():
        crop_tmpdir = tempfile.TemporaryDirectory(prefix="logbook-crop-")
        crop_dir = Path(crop_tmpdir.name)
        print(f"  Cropping screenshots to {crop_dir}")

    traces_dir = sim_root / "traces" if args.sim_dir else PROJECT_ROOT / "traces"
    md_content = build_markdown(logbook_dir, memories_dir, world_path, bulletin_path,
                                days,
                                screenshot_dir if screenshot_dir.exists() else None,
                                crop_dir,
                                traces_dir if traces_dir.exists() else None)

    export_dir.mkdir(parents=True, exist_ok=True)

    if args.day:
        base_name = f"logbook-tag-{args.day:03d}"
    else:
        base_name = "Meier_KIComputerRollenspiele_Sim2Test_Logbuch_2026"

    md_path = export_dir / f"{base_name}.md"
    md_path.write_text(md_content)
    print(f"  Markdown: {md_path}")

    if args.md_only:
        if crop_tmpdir:
            crop_tmpdir.cleanup()
        return 0

    # Allow overriding output location and name
    if args.output_dir:
        pdf_dir = Path(args.output_dir).resolve()
        pdf_dir.mkdir(parents=True, exist_ok=True)
    else:
        pdf_dir = export_dir

    pdf_name = args.output_name if args.output_name else base_name
    output_path = pdf_dir / pdf_name
    result = build_pdf(md_path, output_path, header_path, tex_only=args.tex_only)

    # Clean up cropped screenshots
    if crop_tmpdir:
        crop_tmpdir.cleanup()

    return result


if __name__ == "__main__":
    sys.exit(main())
