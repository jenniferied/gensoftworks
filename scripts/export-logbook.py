#!/usr/bin/env python3
"""
Export GenSoftworks logbook as readable PDF.

Reads logbook JSONL + agent memory streams, weaves them into a
chronological Markdown narrative, then compiles via Pandoc + LuaLaTeX.

Usage:
    python scripts/export-logbook.py                  # All days
    python scripts/export-logbook.py --day 1          # Single day
    python scripts/export-logbook.py --md-only        # Markdown only (no PDF)
    python scripts/export-logbook.py --tex-only       # Generate .tex (no PDF)
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
LOGBOOK_DIR = PROJECT_ROOT / "logbook"
MEMORIES_DIR = PROJECT_ROOT / "state" / "memories"
BULLETIN_PATH = PROJECT_ROOT / "state" / "bulletin.json"
WORLD_PATH = PROJECT_ROOT / "state" / "world.json"
EXPORT_DIR = PROJECT_ROOT / "export"
HEADER = PROJECT_ROOT / "templates" / "logbook-header.tex"

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
}

TIME_LABELS = {
    "morning": "Morgen",
    "afternoon": "Nachmittag",
    "evening": "Abend",
}


def load_bulletin() -> dict[tuple[int, int], list[dict]]:
    """Load CD posts from bulletin board, indexed by (day, scene)."""
    posts_by_scene: dict[tuple[int, int], list[dict]] = {}
    if not BULLETIN_PATH.exists():
        return posts_by_scene

    data = json.loads(BULLETIN_PATH.read_text())

    # Index posts by (day, scene)
    for post in data.get("posts", []):
        key = (post.get("day", 0), post.get("scene", 0))
        posts_by_scene.setdefault(key, []).append(post)

    return posts_by_scene


def load_bulletin_notes() -> str:
    """Load the initial CD note from bulletin."""
    if not BULLETIN_PATH.exists():
        return ""
    data = json.loads(BULLETIN_PATH.read_text())
    return data.get("creative_director_notes", "")


# Post type labels
POST_TYPE_LABELS = {
    "brief": "Creative Director — Brief",
    "feedback": "Creative Director — Feedback",
    "course-correction": "Creative Director — Kurskorrektur",
    "note": "Creative Director — Notiz",
}


def load_all_memories() -> dict[str, dict]:
    """Load all memory entries from all agents, keyed by memory ID."""
    memories = {}
    if not MEMORIES_DIR.exists():
        return memories

    for mem_file in MEMORIES_DIR.glob("*.jsonl"):
        for line in mem_file.read_text().strip().splitlines():
            if not line.strip():
                continue
            entry = json.loads(line)
            memories[entry["id"]] = entry

    return memories


def load_logbook_day(day: int) -> list[dict]:
    """Load all scenes for a given day."""
    path = LOGBOOK_DIR / f"day-{day:03d}.jsonl"
    if not path.exists():
        return []

    scenes = []
    for line in path.read_text().strip().splitlines():
        if not line.strip():
            continue
        scenes.append(json.loads(line))

    return scenes


def get_available_days() -> list[int]:
    """Find all day numbers that have logbook files."""
    days = []
    for path in sorted(LOGBOOK_DIR.glob("day-*.jsonl")):
        try:
            num = int(path.stem.split("-")[1])
            days.append(num)
        except (IndexError, ValueError):
            continue
    return days


def agent_name(agent_id: str) -> str:
    """Get display name for an agent."""
    return AGENT_NAMES.get(agent_id, agent_id.title())


def format_participants(participants: list[str]) -> str:
    """Format participant list as readable string."""
    if len(participants) == 1:
        return agent_name(participants[0])
    names = [agent_name(p) for p in participants]
    if len(names) == 2:
        return f"{names[0]} und {names[1]}"
    return ", ".join(names[:-1]) + f" und {names[-1]}"


def format_participant_icons(participants: list[str]) -> str:
    """Generate LaTeX agent icon row for scene participants."""
    icons = []
    for p in participants:
        if p in AGENT_NAMES:
            icons.append(f"\\agenticon{{{p}}}")
    return "".join(icons)


def select_interesting_memories(
    memory_ids: list[str],
    all_memories: dict[str, dict],
) -> list[dict]:
    """Pick the most interesting memories for display.

    Prioritizes: reflections > plans > high-importance observations.
    Skips routine observations (importance <= 4).
    """
    selected = []
    for mid in memory_ids:
        mem = all_memories.get(mid)
        if not mem:
            continue
        # Always include reflections
        if mem["type"] == "reflection":
            selected.append(mem)
        # Include plans (they show intent)
        elif mem["type"] == "plan" and mem.get("importance", 0) >= 6:
            selected.append(mem)
        # Include high-importance observations that add to the scene
        elif mem["type"] == "observation" and mem.get("importance", 0) >= 7:
            selected.append(mem)
        # Include artifact memories
        elif mem["type"] == "artifact":
            selected.append(mem)
        # Include significant conversations
        elif mem["type"] == "conversation" and mem.get("importance", 0) >= 7:
            selected.append(mem)

    return selected


def render_scene(
    scene: dict,
    all_memories: dict[str, dict],
    cd_posts: dict[tuple[int, int], list[dict]],
    day: int,
) -> str:
    """Render a single scene as Markdown."""
    lines = []

    scene_num = scene.get("scene", 0)

    # Scene heading
    scene_type = SCENE_LABELS.get(scene.get("type", ""), scene.get("type", ""))
    lines.append(f"## Szene {scene_num} · {scene_type}")
    lines.append("")

    # Metadata line (as fenced div for LaTeX scenemeta environment)
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

    # CD directives for this scene (shown BEFORE the narrative)
    scene_posts = cd_posts.get((day, scene_num), [])
    for post in scene_posts:
        label = POST_TYPE_LABELS.get(post.get("type", ""), "Creative Director")
        content = post.get("content", "").replace("→", "$\\rightarrow$")
        lines.append("::: {.directive}")
        lines.append(f"**{label}**")
        lines.append("")
        lines.append(content)
        lines.append(":::")
        lines.append("")

    # Scene narrative (replace special chars that Lora doesn't have)
    summary = scene.get("summary", "")
    summary = summary.replace("→", "$\\rightarrow$")
    lines.append(summary)
    lines.append("")

    # Agent inner thoughts and reflections from this scene
    memory_ids = scene.get("memories_created", [])
    interesting = select_interesting_memories(memory_ids, all_memories)

    for mem in interesting:
        # Determine agent ID from memory ID
        agent_id = mem["id"].rsplit("-", 1)[0]
        name = agent_name(agent_id)
        icon = f"\\agenticon{{{agent_id}}}" if agent_id in AGENT_NAMES else ""

        if mem["type"] == "reflection":
            lines.append("::: {.reflection}")
            desc = mem["description"].replace("→", "$\\rightarrow$")
            lines.append(f"{icon}\\reflectionbubble \\textbf{{{name} reflektiert:}} {desc}")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "plan":
            lines.append("::: {.thought}")
            desc = mem["description"].replace("→", "$\\rightarrow$")
            lines.append(f"{icon}\\planbubble \\textbf{{{name} plant:}} {desc}")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "artifact":
            path = mem.get("metadata", {}).get("artifact_path", "")
            lines.append("::: {.artifact}")
            desc = mem["description"].replace("→", "$\\rightarrow$")
            lines.append(f"{icon}\\artifactbubble \\textbf{{{name} erstellt:}} {desc}")
            if path:
                lines.append(f"\n`{path}`")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "conversation" and mem.get("importance", 0) >= 7:
            lines.append("::: {.thought}")
            desc = mem["description"].replace("→", "$\\rightarrow$")
            lines.append(f"{icon}\\speechbubble \\textbf{{{name} erzählt:}} {desc}")
            lines.append(":::")
            lines.append("")
        elif mem["type"] == "observation" and mem.get("importance", 0) >= 8:
            lines.append("::: {.thought}")
            desc = mem["description"].replace("→", "$\\rightarrow$")
            lines.append(f"{icon}\\thoughtbubble \\textbf{{{name}:}} {desc}")
            lines.append(":::")
            lines.append("")

    # Artifacts listing (if any produced this scene)
    artifacts = scene.get("artifacts", [])
    if artifacts:
        for art in artifacts:
            filename = Path(art).name
            lines.append(f"*Artefakt: `{filename}`*")
            lines.append("")

    return "\n".join(lines)


def render_day(
    day: int,
    scenes: list[dict],
    all_memories: dict[str, dict],
    cd_posts: dict[tuple[int, int], list[dict]],
) -> str:
    """Render a full day as Markdown."""
    # Read world state for day-of-week info
    day_of_week = "Montag"
    if WORLD_PATH.exists():
        world = json.loads(WORLD_PATH.read_text())
        if world.get("day") == day:
            day_of_week = world.get("day_of_week", "Montag")

    lines = []
    lines.append(f"# Tag {day} — {day_of_week}")
    lines.append("")

    # Initial CD note at start of day 1
    if day == 1:
        cd_note = load_bulletin_notes()
        if cd_note:
            lines.append("::: {.directive}")
            lines.append("**Creative Director — Auftrag**")
            lines.append("")
            lines.append(f"*{cd_note}*")
            lines.append(":::")
            lines.append("")

    for scene in scenes:
        lines.append(render_scene(scene, all_memories, cd_posts, day))
        # Divider between scenes (Lua filter converts HorizontalRule)
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def build_markdown(days: list[int] | None = None) -> str:
    """Build the full Markdown document."""
    all_memories = load_all_memories()
    cd_posts = load_bulletin()
    available = get_available_days()

    if not available:
        print("No logbook files found.")
        sys.exit(1)

    if days:
        available = [d for d in available if d in days]

    if not available:
        print("No matching days found.")
        sys.exit(1)

    # YAML frontmatter
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
        scenes = load_logbook_day(day)
        if scenes:
            lines.append(render_day(day, scenes, all_memories, cd_posts))

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

  return el
end

function HorizontalRule(el)
  return pandoc.RawBlock("latex", "\\scenedivider")
end
"""


def build_pdf(md_path: Path, output_path: Path, tex_only: bool = False) -> int:
    """Convert Markdown to PDF via Pandoc + LuaLaTeX."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        filter_path = tmp_path / "logbook-filter.lua"
        filter_path.write_text(LUA_FILTER)

        tex_path = output_path.with_suffix(".tex")

        # Font path (relative from export/ to master-thesis fonts)
        fontpath = "../../master-thesis/assets/fonts/"

        # Pandoc: Markdown -> PDF (or -> LaTeX if tex_only)
        output = str(tex_path) if tex_only else str(output_path.with_suffix(".pdf"))
        cmd = [
            "pandoc",
            str(md_path),
            "-o", output,
            f"--include-in-header={HEADER}",
            f"--lua-filter={filter_path}",
            "--pdf-engine=lualatex",
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
    args = parser.parse_args()

    days = [args.day] if args.day else None

    print("GenSoftworks Logbook Export")
    print("=" * 40)

    # Generate Markdown
    md_content = build_markdown(days)

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    if args.day:
        base_name = f"logbook-tag-{args.day:03d}"
    else:
        base_name = "logbook"

    md_path = EXPORT_DIR / f"{base_name}.md"
    md_path.write_text(md_content)
    print(f"  Markdown: {md_path}")

    if args.md_only:
        return 0

    # Build PDF
    output_path = EXPORT_DIR / base_name
    return build_pdf(md_path, output_path, tex_only=args.tex_only)


if __name__ == "__main__":
    sys.exit(main())
