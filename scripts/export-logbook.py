#!/usr/bin/env python3
"""
Export GenSoftworks logbook as readable PDF.

Reads logbook JSONL + agent memory streams, weaves them into a
chronological Markdown narrative, then compiles via Pandoc + LuaLaTeX.

Supports both v1 (simulation 1) and v2 (simulation 2+) log schemas.

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
    "WORK+REFLECTION": "Arbeit",
    "BRIEF+REACTION": "Briefing",
}

TIME_LABELS = {
    "morning": "Morgen",
    "late-morning": "Vormittag",
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
    """Load all scenes for a given day."""
    path = logbook_dir / f"day-{day:03d}.jsonl"
    if not path.exists():
        return []
    scenes = []
    for line in path.read_text().strip().splitlines():
        if not line.strip():
            continue
        scenes.append(json.loads(line))
    return scenes


def get_available_days(logbook_dir) -> list[int]:
    """Find all day numbers that have logbook files."""
    days = []
    for path in sorted(logbook_dir.glob("day-*.jsonl")):
        try:
            num = int(path.stem.split("-")[1])
            days.append(num)
        except (IndexError, ValueError):
            continue
    return days


def agent_name(agent_id: str) -> str:
    return AGENT_NAMES.get(agent_id, agent_id.title())


def format_participants(participants: list[str]) -> str:
    if len(participants) == 1:
        return agent_name(participants[0])
    names = [agent_name(p) for p in participants]
    if len(names) == 2:
        return f"{names[0]} und {names[1]}"
    return ", ".join(names[:-1]) + f" und {names[-1]}"


def format_participant_icons(participants: list[str]) -> str:
    icons = []
    for p in participants:
        if p in AGENT_NAMES:
            icons.append(f"\\agenticon{{{p}}}")
    return "".join(icons)


def select_interesting_memories(memory_ids, all_memories):
    """Pick the most interesting memories for display (v1 path)."""
    selected = []
    for mid in memory_ids:
        mem = all_memories.get(mid)
        if not mem:
            continue
        if mem["type"] == "reflection":
            selected.append(mem)
        elif mem["type"] == "plan" and mem.get("importance", 0) >= 6:
            selected.append(mem)
        elif mem["type"] == "observation" and mem.get("importance", 0) >= 7:
            selected.append(mem)
        elif mem["type"] == "artifact":
            selected.append(mem)
        elif mem["type"] == "conversation" and mem.get("importance", 0) >= 7:
            selected.append(mem)
    return selected


def esc(text):
    """Escape special chars for LaTeX via Pandoc markdown."""
    return text.replace("→", "$\\rightarrow$")


def render_scene_v1(scene, all_memories, cd_posts, day):
    """Render a v1 scene as Markdown."""
    lines = []
    scene_num = scene.get("scene", 0)
    scene_type = SCENE_LABELS.get(scene.get("type", ""), scene.get("type", ""))
    lines.append(f"## Szene {scene_num} · {scene_type}")
    lines.append("")

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

    scene_posts = cd_posts.get((day, scene_num), [])
    for post in scene_posts:
        label = POST_TYPE_LABELS.get(post.get("type", ""), "Creative Director")
        content = esc(post.get("content", ""))
        lines.append("::: {.directive}")
        lines.append(f"**{label}**")
        lines.append("")
        lines.append(content)
        lines.append(":::")
        lines.append("")

    summary = esc(scene.get("summary", ""))
    lines.append(summary)
    lines.append("")

    memory_ids = scene.get("memories_created", [])
    interesting = select_interesting_memories(memory_ids, all_memories)
    for mem in interesting:
        agent_id = mem["id"].rsplit("-", 1)[0]
        name = agent_name(agent_id)
        icon = f"\\agenticon{{{agent_id}}}" if agent_id in AGENT_NAMES else ""
        desc = esc(mem["description"])

        if mem["type"] == "reflection":
            lines.append("::: {.reflection}")
            lines.append(f"{icon}\\reflectionbubble \\textbf{{{name} reflektiert:}} {desc}")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "plan":
            lines.append("::: {.thought}")
            lines.append(f"{icon}\\planbubble \\textbf{{{name} plant:}} {desc}")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "artifact":
            path = mem.get("metadata", {}).get("artifact_path", "")
            lines.append("::: {.artifact}")
            lines.append(f"{icon}\\artifactbubble \\textbf{{{name} erstellt:}} {desc}")
            if path:
                lines.append(f"\n`{path}`")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "conversation" and mem.get("importance", 0) >= 7:
            lines.append("::: {.thought}")
            lines.append(f"{icon}\\speechbubble \\textbf{{{name} erzählt:}} {desc}")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "observation" and mem.get("importance", 0) >= 8:
            lines.append("::: {.thought}")
            lines.append(f"{icon}\\thoughtbubble \\textbf{{{name}:}} {desc}")
            lines.append(":::")
            lines.append("")

    artifacts = scene.get("artifacts", [])
    if artifacts:
        for art in artifacts:
            filename = Path(art.get("path", str(art))).name if isinstance(art, dict) else Path(art).name
            lines.append(f"*Artefakt: `{filename}`*")
            lines.append("")

    return "\n".join(lines)


def render_scene_v2(scene, cd_posts, day, screenshot_dir=None):
    """Render a v2 scene as Markdown."""
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

    # Screenshot embedding
    if screenshot_dir:
        pattern = f"day-*-scene-{scene_num:03d}-*.png"
        matches = list(screenshot_dir.glob(pattern))
        if matches:
            img_path = matches[0]
            lines.append(f"![Szene {scene_num}]({img_path}){{ width=100% }}")
            lines.append("")

    # CD directives
    scene_posts = cd_posts.get((day, scene_num), [])
    for post in scene_posts:
        label = POST_TYPE_LABELS.get(post.get("type", ""), "Creative Director")
        content = esc(post.get("content", ""))
        lines.append("::: {.directive}")
        lines.append(f"**{label}**")
        lines.append("")
        lines.append(content)
        lines.append(":::")
        lines.append("")

    # CD feedback inline
    cd_fb = scene.get("cd_feedback")
    if cd_fb:
        lines.append("::: {.directive}")
        lines.append(f"**Creative Director — Feedback**")
        lines.append("")
        lines.append(esc(cd_fb))
        lines.append(":::")
        lines.append("")

    # Summary
    summary = esc(scene.get("summary", ""))
    lines.append(summary)
    lines.append("")

    # Dialogue
    dialogue = scene.get("dialogue", [])
    if dialogue:
        for line_d in dialogue:
            who = agent_name(line_d["who"])
            icon = f"\\agenticon{{{line_d['who']}}}" if line_d["who"] in AGENT_NAMES else ""
            says = esc(line_d["says"])
            lines.append(f"{icon}\\speechbubble **{who}:** \"{says}\"")
            lines.append("")

    # Thoughts
    thoughts = scene.get("thoughts", [])
    if thoughts:
        for t in thoughts:
            who = agent_name(t["who"])
            icon = f"\\agenticon{{{t['who']}}}" if t["who"] in AGENT_NAMES else ""
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
            icon = f"\\agenticon{{{fb['from']}}}" if fb["from"] in AGENT_NAMES else ""
            text = esc(fb["text"])
            lines.append("::: {.feedback}")
            lines.append(f"{icon}\\feedbackbubble \\textbf{{{from_name} $\\rightarrow$ {to_name}:}} {text}")
            lines.append(":::")
            lines.append("")

    # Mood
    mood = scene.get("mood", {})
    if mood:
        mood_parts = []
        for agent_id, m in mood.items():
            name = agent_name(agent_id)
            mood_parts.append(f"{name} ({m.get('before', '?')} $\\rightarrow$ {m.get('after', '?')})")
        lines.append(f"*Stimmung: {', '.join(mood_parts)}*")
        lines.append("")

    # Memories
    memories = scene.get("memories", [])
    if memories:
        for mem in memories:
            who = agent_name(mem["who"])
            icon = f"\\agenticon{{{mem['who']}}}" if mem["who"] in AGENT_NAMES else ""
            text = esc(mem.get("text", ""))
            imp = mem.get("importance", 5)
            lines.append(f"{icon} *{who} [{mem['id']}] (\\stmark{imp}):* {text}")
        lines.append("")

    # Artifacts
    artifacts = scene.get("artifacts", [])
    if artifacts:
        for art in artifacts:
            filename = Path(art.get("path", str(art))).name if isinstance(art, dict) else Path(art).name
            lines.append(f"*Artefakt: `{filename}`*")
            lines.append("")

    # Key moment
    key_moment = scene.get("key_moment")
    if key_moment:
        lines.append(f"**Schlüsselmoment:** *{esc(key_moment)}*")
        lines.append("")

    return "\n".join(lines)


def render_scene(scene, all_memories, cd_posts, day, screenshot_dir=None):
    """Route to v1 or v2 renderer based on schema."""
    schema = detect_schema(scene)
    if schema == "v2":
        return render_scene_v2(scene, cd_posts, day, screenshot_dir)
    return render_scene_v1(scene, all_memories, cd_posts, day)


def render_day(day, scenes, all_memories, cd_posts, world_path, bulletin_path, screenshot_dir=None):
    """Render a full day as Markdown."""
    day_of_week = "Montag"
    if world_path.exists():
        world = json.loads(world_path.read_text())
        if world.get("day") == day:
            day_of_week = world.get("day_of_week", "Montag")

    lines = []
    lines.append(f"# Tag {day} — {day_of_week}")
    lines.append("")

    if day == 1:
        cd_note = load_bulletin_notes(bulletin_path)
        if cd_note:
            lines.append("::: {.directive}")
            lines.append("**Creative Director — Auftrag**")
            lines.append("")
            lines.append(f"*{cd_note}*")
            lines.append(":::")
            lines.append("")

    for scene in scenes:
        lines.append(render_scene(scene, all_memories, cd_posts, day, screenshot_dir))
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def build_markdown(logbook_dir, memories_dir, world_path, bulletin_path,
                   days_filter=None, screenshot_dir=None):
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
                                    world_path, bulletin_path, screenshot_dir))

    return "\n".join(lines)


# Lua filter for converting fenced divs to LaTeX environments
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

  return el
end

function HorizontalRule(el)
  return pandoc.RawBlock("latex", "\\scenedivider")
end
"""


def build_pdf(md_path, output_path, header_path, tex_only=False):
    """Convert Markdown to PDF via Pandoc + LuaLaTeX."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        filter_path = tmp_path / "logbook-filter.lua"
        filter_path.write_text(LUA_FILTER)

        tex_path = output_path.with_suffix(".tex")
        fontpath = str(Path(__file__).resolve().parent.parent.parent / "master-thesis" / "assets" / "fonts") + "/"

        # Patch header template with absolute font/icon paths
        icons_dir = str((PROJECT_ROOT / "export" / "icons").resolve()) + "/"
        header_text = header_path.read_text()
        header_text = header_text.replace(
            "Path = ../../master-thesis/assets/fonts/,",
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
            "-V", f"mainfont=Lora",
            "-V", f"mainfontoptions=Path={fontpath},UprightFont=Lora-Variable.ttf,ItalicFont=Lora-Italic-Variable.ttf,BoldFont=Lora-Variable.ttf,BoldItalicFont=Lora-Italic-Variable.ttf,BoldFeatures={{Weight=700}},BoldItalicFeatures={{Weight=700}}",
            "-V", f"sansfont=OpenSans",
            "-V", f"sansfontoptions=Path={fontpath},UprightFont=OpenSans-Variable.ttf,ItalicFont=OpenSans-Italic-Variable.ttf,BoldFont=OpenSans-Variable.ttf,BoldItalicFont=OpenSans-Italic-Variable.ttf,BoldFeatures={{Weight=700}}",
            "-V", f"monofont=JetBrainsMono",
            "-V", f"monofontoptions=Path={fontpath},UprightFont=JetBrainsMono-Variable.ttf,Scale=0.85",
            "-V", "fontsize=10pt",
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

    print("GenSoftworks Logbook Export")
    print("=" * 40)

    md_content = build_markdown(logbook_dir, memories_dir, world_path, bulletin_path,
                                days, screenshot_dir if screenshot_dir.exists() else None)

    export_dir.mkdir(parents=True, exist_ok=True)

    if args.day:
        base_name = f"logbook-tag-{args.day:03d}"
    else:
        base_name = "logbook"

    md_path = export_dir / f"{base_name}.md"
    md_path.write_text(md_content)
    print(f"  Markdown: {md_path}")

    if args.md_only:
        return 0

    output_path = export_dir / base_name
    return build_pdf(md_path, output_path, header_path, tex_only=args.tex_only)


if __name__ == "__main__":
    sys.exit(main())
