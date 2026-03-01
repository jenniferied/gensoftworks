#!/usr/bin/env python3
"""Build simulation.json for the Phaser logbook viewer.

Reads logbook data → frontend/public/data/simulation.json

Supports four logbook formats:
  - v1 (simulation 1): day-NNN.jsonl files with agent_details
  - v2 (simulation 2): day-NNN.jsonl files with mood dict
  - v4 (simulation 2 test): individual dayDD-sceneS.json files
  - v5 (simulation 2 test+): dayDD.json index files with transcript refs

Use --sim-dir to point at a simulation directory.
"""

import argparse
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent

# --- Agent desk positions (tile coords, matching StudioScene.js) ---
AGENT_DESKS = {
    "emre":   {"x": 4,  "y": 3},
    "vera":   {"x": 12, "y": 3},
    "tobi":   {"x": 20, "y": 3},
    "darius": {"x": 4,  "y": 16},
    "nami":   {"x": 12, "y": 16},
    "leo":    {"x": 20, "y": 16},
    "finn":   {"x": 8,  "y": 23},
}

ALL_AGENTS = list(AGENT_DESKS.keys())

# --- Location → Phaser room mapping ---
LOCATION_ROOM = {
    "gemeinschaftsraum": "conference",
    "besprechungsraum":  "conference",
    "lore-ecke":         "7a",
    "art-station":       "7b",
    "bibliothek":        "lounge",
    "küche":             "kitchen",
    "kueche":            "kitchen",
    "flur":              "hallway",
    # v4 locations (sim-2-test)
    "alle-stationen":    None,  # distributed, agents at desks
    "alle-arbeitsplätze": None,  # legacy alias
    "game-design-corner": "7d",
    "qa-ecke":           "7f",
    "tech-ecke":         "7c",
}

# --- Logical seat/spot positions per shared room ---
ROOM_SPOTS = {
    "conference": [
        {"x": 26, "y": 3},
        {"x": 32, "y": 3},
        {"x": 25, "y": 3},
        {"x": 32, "y": 2},
        {"x": 27, "y": 5},
        {"x": 29, "y": 5},
        {"x": 31, "y": 5},
    ],
    "kitchen": [
        {"x": 37, "y": 2},
        {"x": 39, "y": 2},
        {"x": 36, "y": 2},
        {"x": 42, "y": 3},
        {"x": 37, "y": 6},
        {"x": 39, "y": 6},
        {"x": 41, "y": 6},
    ],
    "lounge": [
        {"x": 25, "y": 16},
        {"x": 33, "y": 16},
        {"x": 27, "y": 18},
        {"x": 31, "y": 18},
        {"x": 27, "y": 21},
        {"x": 32, "y": 21},
        {"x": 25, "y": 26},
    ],
    "hallway": [
        {"x": 5,  "y": 10},
        {"x": 12, "y": 10},
        {"x": 18, "y": 11},
        {"x": 24, "y": 10},
        {"x": 30, "y": 11},
        {"x": 36, "y": 10},
        {"x": 40, "y": 11},
    ],
    "7": [
        {"x": 8,  "y": 23},
        {"x": 10, "y": 23},
        {"x": 9,  "y": 21},
        {"x": 12, "y": 21},
        {"x": 5,  "y": 21},
        {"x": 7,  "y": 25},
        {"x": 11, "y": 25},
    ],
}

ROOM_GUEST_SPOTS = {
    "7a": [{"x": 4, "y": 5}, {"x": 6, "y": 5}, {"x": 6, "y": 4}, {"x": 2, "y": 4}, {"x": 5, "y": 4}, {"x": 7, "y": 3}],
    "7b": [{"x": 12, "y": 5}, {"x": 14, "y": 5}, {"x": 14, "y": 4}, {"x": 10, "y": 4}, {"x": 13, "y": 4}, {"x": 15, "y": 3}],
    "7c": [{"x": 20, "y": 5}, {"x": 22, "y": 5}, {"x": 22, "y": 4}, {"x": 18, "y": 4}, {"x": 21, "y": 4}, {"x": 23, "y": 3}],
    "7d": [{"x": 3, "y": 17}, {"x": 5, "y": 17}, {"x": 2, "y": 16}, {"x": 1, "y": 17}, {"x": 4, "y": 18}, {"x": 3, "y": 15}],
    "7e": [{"x": 11, "y": 17}, {"x": 13, "y": 17}, {"x": 10, "y": 16}, {"x": 9, "y": 17}, {"x": 12, "y": 18}, {"x": 11, "y": 15}],
    "7f": [{"x": 19, "y": 17}, {"x": 21, "y": 17}, {"x": 18, "y": 16}, {"x": 17, "y": 17}, {"x": 19, "y": 18}, {"x": 19, "y": 15}],
}

ROOM_OWNERS = {
    "7a": "emre",
    "7b": "vera",
    "7c": "tobi",
    "7d": "darius",
    "7e": "nami",
    "7f": "leo",
    "7":  "finn",
}

TIME_LABELS = {
    "morning": "Morgen",
    "late-morning": "Vormittag",
    "afternoon": "Nachmittag",
    "late-afternoon": "Spätnachmittag",
    "evening": "Abend",
    "morning-to-evening": "Ganztags",
}

TYPE_LABELS = {
    "ARRIVAL": "Ankunft",
    "MEETING": "Meeting",
    "ENCOUNTER": "Begegnung",
    "WORK": "Arbeit",
    "WORK+REFLECTION": "Arbeit",
    "BRIEF+REACTION": "Briefing",
    "REFLECTION": "Reflexion",
    "EVENT": "Ereignis",
    # v3 simplified types
    "TALK": "Gespraech",
    "REVIEW": "Review",
    # v4 scene types (sim-2-test daily schedule)
    "BRIEFING": "Briefing",
    "PAUSE": "Pause",
    "DND": "D&D",
}


def load_chapters(gallery_dir, days):
    """Scan gallery/gdd/ and gallery/wbb/ for versioned markdown chapters.

    Filename pattern: KK-title-vN.md (e.g. 01-spieluebersicht-v2.md)
    Cross-references scene artifacts to determine when each version appeared.
    Returns dict: {"gdd": [...], "wbb": [...]} with all versions per chapter.
    """
    file_pattern = re.compile(r"^(\d{2})-(.+)-v(\d+)\.md$")
    result = {}

    # Build artifact timeline: scan all scenes for gallery/ references
    # Artifact strings like: "gallery/gdd/01-spielübersicht.md (V2)"
    # or plain: "gallery/gdd/01-spielübersicht.md"
    art_gallery_re = re.compile(r"gallery/(gdd|wbb)/(\d{2})-")
    art_version_re = re.compile(r"\((?:.*?V|v)(\d+)\)")
    timeline = {}  # (doc_type, chapter_num, version) -> (day, scene)
    for day_entry in days:
        day_num = day_entry["day"]
        for sc in day_entry["scenes"]:
            scene_num = sc.get("scene", 0)
            for art in sc.get("artifacts", []):
                gm = art_gallery_re.search(art)
                if not gm:
                    continue
                doc_type_match = gm.group(1)
                chapter_num = gm.group(2)
                vm = art_version_re.search(art)
                version = int(vm.group(1)) if vm else 1
                key = (doc_type_match, chapter_num, version)
                if key not in timeline:
                    timeline[key] = {"day": day_num, "scene": scene_num}

    for doc_type in ("gdd", "wbb"):
        doc_dir = gallery_dir / doc_type
        if not doc_dir.exists():
            continue
        chapters = {}
        for f in sorted(doc_dir.glob("*.md")):
            m = file_pattern.match(f.name)
            if not m:
                continue
            chapter_num = m.group(1)
            # Skip 00-* note files — they're inline scene notes, not document chapters
            if chapter_num == "00":
                continue
            chapter_slug = m.group(2)
            version = int(m.group(3))
            chapter_id = f"{chapter_num}-{chapter_slug}"
            content = f.read_text()
            title = chapter_id
            for line in content.splitlines():
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
            if chapter_id not in chapters:
                chapters[chapter_id] = {"id": chapter_id, "title": title, "versions": []}
            ver_entry = {
                "version": version,
                "filename": f.name,
                "content": content,
            }
            # Add appearance time from artifact timeline
            tl_key = (doc_type, chapter_num, version)
            if tl_key in timeline:
                ver_entry["appeared"] = timeline[tl_key]
            chapters[chapter_id]["versions"].append(ver_entry)
        for ch in chapters.values():
            ch["versions"].sort(key=lambda v: v["version"])
            # Compute first_appeared: earliest artifact reference for this chapter
            # across ALL versions (including ones without files on disk)
            chapter_num = ch["id"][:2]
            earliest = None
            for tl_key, tl_val in timeline.items():
                if tl_key[0] == doc_type and tl_key[1] == chapter_num:
                    if earliest is None or (tl_val["day"], tl_val["scene"]) < (earliest["day"], earliest["scene"]):
                        earliest = tl_val
            if earliest:
                ch["first_appeared"] = earliest
        result[doc_type] = sorted(chapters.values(), key=lambda c: c["id"])
    return result


def embed_note_contents(days, gallery_dir):
    """Embed markdown content from note files (00-*.md, non-versioned) into scene data.

    Scans scene artifacts for gallery paths matching 00-*.md (not *-vN.md),
    reads their content, and stores in scene['note_contents'] = {path: content}.
    """
    note_re = re.compile(r"^gallery/.+/00-.+\.md$")

    for day_entry in days:
        for sc in day_entry["scenes"]:
            note_contents = {}
            for art in sc.get("artifacts", []):
                if not note_re.match(art):
                    continue
                full_path = gallery_dir.parent / art
                # If non-versioned file missing, try -v1.md variant
                if not full_path.exists():
                    stem = full_path.stem  # e.g. "00-recherche-notizen-darius"
                    v1_path = full_path.with_name(f"{stem}-v1.md")
                    if v1_path.exists():
                        full_path = v1_path
                if full_path.exists():
                    try:
                        content = full_path.read_text()
                        note_contents[art] = content
                    except Exception:
                        pass
            if note_contents:
                sc["note_contents"] = note_contents


def load_concept_art(gallery_dir, days):
    """Scan gallery/concepts/ for images and build timeline from artifacts.

    Returns list of {filename, category, path, appeared: {day, scene}} sorted by appearance.
    """
    concepts_dir = gallery_dir / "concepts"
    if not concepts_dir.exists():
        return []

    # Collect all image files recursively
    images = {}
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        for f in concepts_dir.rglob(ext):
            rel = f.relative_to(gallery_dir)
            # Category from subdirectory (e.g. concepts/KK-kategorie/name.png)
            parts = f.relative_to(concepts_dir).parts
            category = parts[0] if len(parts) > 1 else "allgemein"
            entry = {
                "filename": f.name,
                "category": category,
                "path": f"gallery/{rel}",
            }
            # Read embedded metadata from PNG
            try:
                img_obj = Image.open(f)
                meta = img_obj.info
                if meta.get("model"):
                    entry["model"] = meta["model"]
                if meta.get("prompt"):
                    entry["prompt"] = meta["prompt"]
                img_obj.close()
            except Exception:
                pass
            images[str(rel)] = entry

    # Build timeline from scene artifacts
    art_img_re = re.compile(r"gallery/concepts/")
    for day_entry in days:
        day_num = day_entry["day"]
        for sc in day_entry["scenes"]:
            scene_num = sc.get("scene", 0)
            for art in sc.get("artifacts", []):
                if not art_img_re.search(art):
                    continue
                # Match against known images by filename
                for key, img in images.items():
                    if img["filename"] in art and "appeared" not in img:
                        img["appeared"] = {"day": day_num, "scene": scene_num}

    # Assign appearance for images that weren't referenced in scene artifacts
    for key, img in images.items():
        if "appeared" not in img:
            cat = img.get("category", "")
            cat_match = re.search(r"day(\d+)", cat)
            if cat_match:
                day_num = int(cat_match.group(1))
                if "supplement" in cat:
                    img["appeared"] = {"day": f"{day_num}-supplement", "scene": 0}
                else:
                    img["appeared"] = {"day": day_num, "scene": 0}

    # Sort by appearance, then filename
    result = sorted(images.values(),
                    key=lambda i: (str(i.get("appeared", {}).get("day", 999)),
                                   i.get("appeared", {}).get("scene", 999),
                                   i["filename"]))
    return result


def load_roster(roster_dir):
    """Parse YAML frontmatter from roster markdown files.

    Simple key: value parser — no pyyaml dependency needed.
    Returns dict: {agent_key: {name, role, age, pronouns, workspace, background, ...}}
    """
    roster = {}
    if not roster_dir.exists():
        return roster
    for f in sorted(roster_dir.glob("*.md")):
        text = f.read_text()
        if not text.startswith("---"):
            continue
        end = text.index("---", 3)
        block = text[3:end].strip()
        meta = {}
        for line in block.splitlines():
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            v = v.strip().strip('"').strip("'")
            meta[k.strip()] = v
        key = meta.get("sprite", f.stem.split("-")[0])
        age = meta.get("age", "")

        # Parse markdown body into sections
        body = text[end + 3:].strip()
        sections = {}
        current_heading = None
        current_lines = []
        for bline in body.splitlines():
            if bline.startswith("## "):
                if current_heading:
                    sections[current_heading] = "\n".join(current_lines).strip()
                current_heading = bline[3:].strip()
                current_lines = []
            elif current_heading is not None:
                current_lines.append(bline)
            # skip lines before first ## (the # Name heading)
        if current_heading:
            sections[current_heading] = "\n".join(current_lines).strip()

        roster[key] = {
            "name": meta.get("name", ""),
            "role": meta.get("role", ""),
            "age": int(age) if age.isdigit() else None,
            "pronouns": meta.get("pronouns", ""),
            "workspace": meta.get("workspace", ""),
            "background": meta.get("background", ""),
            "color": meta.get("color", ""),
            "address": meta.get("address", ""),
            "commute": meta.get("commute", ""),
            "sections": sections,
        }
    return roster


def load_agent_memories_md(agents_dir):
    """Parse agent memory markdown files into structured data.

    Each file has sections like: ## Tag 1, Szene 2 (WORK)
    Returns dict: {agent_key: [{day, scene, type, text}, ...]}
    """
    agent_mems = {}
    if not agents_dir.exists():
        return agent_mems

    header_re = re.compile(r"^## Tag (\d+),\s*Szene (\d+)\s*\((\w+)\)")
    for f in sorted(agents_dir.glob("*-memory.md")):
        agent_key = f.stem.replace("-memory", "")
        entries = []
        current = None
        for line in f.read_text().splitlines():
            m = header_re.match(line)
            if m:
                if current:
                    current["text"] = current["text"].strip()
                    entries.append(current)
                current = {
                    "day": int(m.group(1)),
                    "scene": int(m.group(2)),
                    "type": m.group(3),
                    "text": "",
                }
            elif current is not None:
                current["text"] += line + "\n"
        if current:
            current["text"] = current["text"].strip()
            entries.append(current)
        agent_mems[agent_key] = entries
    return agent_mems


def detect_schema(entry):
    """Detect whether entry uses v1, v2, or v3 schema."""
    if "mood" in entry and isinstance(entry["mood"], dict):
        return "v2"
    if entry.get("type") in ("TALK", "WORK", "REVIEW") and "agent_details" not in entry:
        return "v3"
    return "v1"


def load_memories(memories_dir):
    """Load all memories indexed by id."""
    memories = {}
    if not memories_dir.exists():
        return memories
    for f in sorted(memories_dir.glob("*.jsonl")):
        for line in f.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            mem = json.loads(line)
            memories[mem["id"]] = mem
    return memories


def resolve_room(location):
    """Map logbook location string to a Phaser room key."""
    loc = location.lower().strip()
    if loc in LOCATION_ROOM:
        return LOCATION_ROOM[loc]
    if loc in ("studio-weit", "studio-verteilt"):
        return None
    if "+" in loc:
        return None
    return LOCATION_ROOM.get(loc)


def compute_positions(participants, location):
    """Compute tile positions for all 7 agents in a scene."""
    positions = {}
    active_agents = [a for a in participants if a != "creative-director"]
    room = resolve_room(location)

    compound_rooms = {}
    if "+" in location:
        parts = [p.strip() for p in location.split("+")]
        for part in parts:
            r = LOCATION_ROOM.get(part)
            if r:
                compound_rooms[part] = r

    for agent in ALL_AGENTS:
        if agent in active_agents:
            if room and room in ROOM_SPOTS:
                spots = ROOM_SPOTS[room]
                idx = active_agents.index(agent)
                spot = spots[idx % len(spots)]
                positions[agent] = {"x": spot["x"], "y": spot["y"], "state": "active"}
            elif room and room in ROOM_GUEST_SPOTS:
                owner = ROOM_OWNERS.get(room)
                if agent == owner:
                    positions[agent] = {**AGENT_DESKS[agent], "state": "active"}
                else:
                    guests = [a for a in active_agents if a != owner]
                    guest_idx = guests.index(agent) if agent in guests else 0
                    guest_spots = ROOM_GUEST_SPOTS[room]
                    spot = guest_spots[guest_idx % len(guest_spots)]
                    positions[agent] = {"x": spot["x"], "y": spot["y"], "state": "active"}
            elif compound_rooms:
                if agent == "emre" and "lore-ecke" in compound_rooms:
                    c = AGENT_DESKS["emre"]
                    positions[agent] = {"x": c["x"], "y": c["y"] + 1, "state": "active"}
                elif "bibliothek" in compound_rooms:
                    r = compound_rooms["bibliothek"]
                    spots = ROOM_SPOTS.get(r, [])
                    if spots:
                        others = [a for a in active_agents if a != "emre" or "lore-ecke" not in compound_rooms]
                        idx = others.index(agent) if agent in others else 0
                        spot = spots[idx % len(spots)]
                        positions[agent] = {"x": spot["x"], "y": spot["y"], "state": "active"}
                    else:
                        positions[agent] = {**AGENT_DESKS[agent], "state": "active"}
                else:
                    positions[agent] = {**AGENT_DESKS[agent], "state": "active"}
            else:
                positions[agent] = {**AGENT_DESKS[agent], "state": "active"}
        else:
            positions[agent] = {**AGENT_DESKS[agent], "state": "dimmed"}

    return positions


def build_scene_v1(entry, all_memories):
    """Build a scene object from a v1 logbook entry (simulation 1)."""
    participants = [p for p in entry.get("participants", []) if p != "creative-director"]
    location = entry.get("location", "studio-weit")
    scene_type = entry.get("type", "WORK")
    time_key = entry.get("time_of_day", entry.get("time", "morning"))

    scene = {
        "scene": entry.get("scene", entry.get("scene_number", 0)),
        "type": scene_type,
        "type_label": TYPE_LABELS.get(scene_type, scene_type),
        "time_of_day": time_key,
        "time_label": TIME_LABELS.get(time_key, time_key),
        "location": location,
        "location_label": location.replace("-", " ").title(),
        "participants": participants,
        "summary": entry.get("summary", ""),
        "key_moment": entry.get("key_moment", ""),
        "positions": compute_positions(entry.get("participants", []), location),
        "active_room": resolve_room(location),
        "artifacts": entry.get("artifacts", []),
    }

    # v1 agent_details
    if "agent_details" in entry:
        details = {}
        for agent_key, detail in entry["agent_details"].items():
            if agent_key == "creative-director":
                continue
            details[agent_key] = {
                "mood_before": detail.get("mood_before", ""),
                "mood_after": detail.get("mood_after", ""),
                "key_reaction": detail.get("key_reaction", ""),
                "emotional_arc": detail.get("emotional_arc", ""),
                "influences": detail.get("influences", []),
            }
        scene["agent_details"] = details

    # v1 memories (cross-referenced by id)
    mem_ids = entry.get("memories_created", [])
    if mem_ids:
        memories_by_agent = defaultdict(list)
        for mid in mem_ids:
            mem = all_memories.get(mid)
            if mem:
                agent_key = mid.split("-")[0]
                memories_by_agent[agent_key].append({
                    "id": mem["id"],
                    "type": mem.get("type", "observation"),
                    "description": mem["description"],
                    "importance": mem.get("importance", 5),
                })
        scene["memories"] = dict(memories_by_agent)

    return scene


def build_scene_v2(entry):
    """Build a scene object from a v2 logbook entry (simulation 2+)."""
    participants = [p for p in entry.get("participants", []) if p != "creative-director"]
    location = entry.get("location", "studio-weit")
    scene_type = entry.get("type", "WORK")
    time_key = entry.get("time", "morning")

    scene = {
        "scene": entry["scene"],
        "type": scene_type,
        "type_label": TYPE_LABELS.get(scene_type, scene_type),
        "time_of_day": time_key,
        "time_label": TIME_LABELS.get(time_key, time_key),
        "location": location,
        "location_label": location.replace("-", " ").title(),
        "participants": participants,
        "summary": entry.get("summary", ""),
        "key_moment": entry.get("key_moment"),
        "positions": compute_positions(entry.get("participants", []), location),
        "active_room": resolve_room(location),
        "artifacts": entry.get("artifacts", []),
        # v2 structured fields passed through
        "dialogue": entry.get("dialogue", []),
        "thoughts": entry.get("thoughts", []),
        "mood": entry.get("mood", {}),
        "feedback": entry.get("feedback", []),
        "cd_feedback": entry.get("cd_feedback"),
        "trace_dirs": entry.get("trace_dirs", []),
    }

    # v2 memories (inline text)
    memories_raw = entry.get("memories", [])
    if memories_raw:
        memories_by_agent = defaultdict(list)
        for mem in memories_raw:
            memories_by_agent[mem["who"]].append({
                "id": mem["id"],
                "importance": mem.get("importance", 5),
                "description": mem.get("text", ""),
            })
        scene["memories"] = dict(memories_by_agent)

    return scene


def load_logbook_v4(logbook_dir):
    """Load individual dayDD-sceneS.json files (v4 format, sim-2-test).

    Returns list of (day_num, entry) tuples sorted by day+scene.
    """
    entries = []
    pattern = re.compile(r"day(\d+)-scene(\d+)\.json$")
    for f in sorted(logbook_dir.glob("day*-scene*.json")):
        m = pattern.match(f.name)
        if not m:
            continue
        day_num = int(m.group(1))
        entry = json.loads(f.read_text())
        entries.append((day_num, entry))
    return entries


def load_logbook_v5(logbook_dir):
    """Load dayDD.json index files (v5 format).

    Also loads dayDD-supplement.json files as separate day entries.
    Returns list of day dicts with scenes[], or empty list if no v5 files found.
    """
    main_pattern = re.compile(r"day(\d+)\.json$")
    supplement_pattern = re.compile(r"day(\d+)-supplement\.json$")
    days = []
    supplements = []
    for f in sorted(logbook_dir.glob("day*.json")):
        sm = supplement_pattern.match(f.name)
        if sm:
            data = json.loads(f.read_text())
            supplements.append(data)
            continue
        m = main_pattern.match(f.name)
        if not m:
            continue
        data = json.loads(f.read_text())
        days.append(data)
    # Append supplements after main days
    days.extend(supplements)
    return days


def build_scene_v5(entry):
    """Build a scene object from a v5 day-index scene entry."""
    participants = [p for p in entry.get("participants", []) if p != "creative-director"]
    location = entry.get("location", "studio-weit")
    scene_type = entry.get("type", "WORK")
    time_key = entry.get("time", "morning")

    return {
        "scene": entry["scene"],
        "type": scene_type,
        "type_label": TYPE_LABELS.get(scene_type, scene_type),
        "time_of_day": time_key,
        "time_label": TIME_LABELS.get(time_key, time_key),
        "location": location,
        "location_label": location.replace("-", " ").title(),
        "participants": participants,
        "summary": entry.get("summary", ""),
        "positions": compute_positions(entry.get("participants", []), location),
        "active_room": resolve_room(location),
        "artifacts": entry.get("artifacts", []),
        "cd_feedback": entry.get("cd_feedback"),
    }


def main():
    parser = argparse.ArgumentParser(description="Build simulation.json for Phaser viewer")
    parser.add_argument("--sim-dir", type=str, default=None,
                        help="Path to simulation directory (e.g. simulation-2-test)")
    parser.add_argument("--out", type=str, default=None,
                        help="Output file path override")
    args = parser.parse_args()

    if args.sim_dir:
        sim_root = ROOT / args.sim_dir
        logbook_dir = sim_root / "logbook"
        memories_dir = sim_root / "state" / "memories"
        agents_dir = sim_root / "agents"
        roster_dir = sim_root / "roster"
        gallery_dir = sim_root / "gallery"
        out_file = Path(args.out) if args.out else sim_root / "viewer-data" / "simulation.json"
    else:
        logbook_dir = ROOT / "logbook"
        memories_dir = ROOT / "state" / "memories"
        agents_dir = ROOT / "agents"
        roster_dir = ROOT / "roster"
        gallery_dir = ROOT / "gallery"
        out_file = Path(args.out) if args.out else ROOT / "frontend" / "public" / "data" / "simulation.json"

    all_memories = load_memories(memories_dir)

    # Try v5 format first (dayDD.json index files)
    v5_days = load_logbook_v5(logbook_dir)

    if v5_days:
        days = []
        for day_data in v5_days:
            day_num = day_data["day"]
            is_supplement = isinstance(day_num, str) and "supplement" in day_num

            if is_supplement:
                # Supplement entries have phases instead of scenes
                day_entry = {
                    "day": day_num,
                    "scenes": [],
                    "is_supplement": True,
                    "supplement": {
                        "phases": day_data.get("phases", []),
                        "context": day_data.get("context", {}),
                        "budget_total": day_data.get("budget_total", {}),
                        "image_inventory": day_data.get("image_inventory", {}),
                    },
                }
            else:
                scenes = [build_scene_v5(s) for s in day_data.get("scenes", [])]
                day_entry = {"day": day_num, "scenes": scenes}

            # Day-level summary fields are inline in v5
            for k in ("weekday", "phase", "title", "summary",
                       "cd_decisions", "key_moments", "artifacts"):
                if k in day_data:
                    day_entry.setdefault("summary", {})[k] = day_data[k]
            # Promote day_data summary fields into the summary dict
            if "summary" in day_entry and isinstance(day_entry["summary"], dict):
                day_entry["summary"]["day"] = day_num
            days.append(day_entry)
    else:
        # Try v4 format (individual dayDD-sceneS.json files)
        v4_entries = load_logbook_v4(logbook_dir)

        if v4_entries:
            days_dict = defaultdict(list)
            for day_num, entry in v4_entries:
                days_dict[day_num].append(entry)

            days = []
            for day_num in sorted(days_dict.keys()):
                scenes = []
                for entry in days_dict[day_num]:
                    scenes.append(build_scene_v2(entry))
                days.append({"day": day_num, "scenes": scenes})
        else:
            # Fall back to JSONL format (v1/v2/v3)
            logbook_files = sorted(logbook_dir.glob("day-*.jsonl"))

            if not logbook_files:
                print("No logbook files found!", file=sys.stderr)
                sys.exit(1)

            days = []
            for lf in logbook_files:
                day_num = int(lf.stem.replace("day-", ""))
                scenes = []
                for line in lf.read_text().splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    entry = json.loads(line)
                    schema = detect_schema(entry)
                    if schema in ("v2", "v3"):
                        scenes.append(build_scene_v2(entry))
                    else:
                        scenes.append(build_scene_v1(entry, all_memories))
                days.append({"day": day_num, "scenes": scenes})

        # Load day summaries if available (v4 and older)
        for day_entry in days:
            day_num = day_entry["day"]
            summary_file = logbook_dir / f"day{day_num:02d}-summary.json"
            if summary_file.exists():
                day_entry["summary"] = json.loads(summary_file.read_text())

    # Load agent memory markdown files
    agent_memories = load_agent_memories_md(agents_dir)

    # Load roster profiles
    roster = load_roster(roster_dir)

    # Load GDD/WBB chapters (needs days for artifact timeline)
    chapters = load_chapters(gallery_dir, days)

    # Load concept art
    concept_art = load_concept_art(gallery_dir, days)

    # Embed note contents into scene data
    embed_note_contents(days, gallery_dir)

    # Copy traces and add references to scenes
    if args.sim_dir:
        traces_dir = sim_root / "traces"
        if traces_dir.exists():
            sim_id = args.sim_dir.replace("/", "-")
            traces_dest = ROOT / "frontend" / "public" / "traces" / sim_id
            # Map scene type → trace dir suffix for conversation scenes
            conv_type_suffix = {
                "BRIEFING": "briefing",
                "MEETING": "meeting",
                "PAUSE": "pause",
                "REVIEW": "review",
                "DND": "dnd",
            }
            for day_entry in days:
                day_num = day_entry["day"]

                # Skip supplement entries — they have no traces
                if day_entry.get("is_supplement"):
                    continue

                # Discover GM transcript for this day
                gm_dir = traces_dir / f"day{day_num:02d}-gm"
                gm_tf = gm_dir / "transcript.md"
                gm_url = None
                if gm_tf.exists():
                    dest_dir = traces_dest / gm_dir.name
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest_file = dest_dir / "transcript.md"
                    if not dest_file.exists():
                        shutil.copy2(gm_tf, dest_file)
                    gm_url = f"traces/{sim_id}/{gm_dir.name}/transcript.md"

                for sc in day_entry["scenes"]:
                    scene_num = sc["scene"]
                    prefix = f"day{day_num:02d}-scene{scene_num}"
                    scene_type = sc["type"]
                    traces = {}

                    # Prefer trace_dirs from logbook, fall back to derivation
                    logbook_trace_dirs = sc.get("trace_dirs", [])
                    if logbook_trace_dirs:
                        for td in logbook_trace_dirs:
                            src = traces_dir / td
                            if src.exists():
                                rel = f"traces/{sim_id}/{src.name}/"
                                dest = traces_dest / src.name
                                if not dest.exists():
                                    shutil.copytree(src, dest)
                                # Determine key: shared for conversation, agent name for WORK
                                if scene_type in conv_type_suffix:
                                    traces["_shared"] = rel
                                else:
                                    # Extract agent name from dir suffix
                                    agent_key = td.replace(f"{prefix}-", "")
                                    traces[agent_key] = rel
                    elif scene_type in conv_type_suffix:
                        # Fallback: derive conversation trace dir
                        suffix = conv_type_suffix[scene_type]
                        src = traces_dir / f"{prefix}-{suffix}"
                        if src.exists():
                            rel = f"traces/{sim_id}/{src.name}/"
                            dest = traces_dest / src.name
                            if not dest.exists():
                                shutil.copytree(src, dest)
                            traces["_shared"] = rel
                    else:
                        # Fallback: derive WORK per-agent trace dirs
                        for agent in ALL_AGENTS:
                            src = traces_dir / f"{prefix}-{agent}"
                            if src.exists():
                                rel = f"traces/{sim_id}/{src.name}/"
                                dest = traces_dest / src.name
                                if not dest.exists():
                                    shutil.copytree(src, dest)
                                traces[agent] = rel

                    if traces:
                        sc["traces"] = traces

                    # Discover all transcripts for this scene by scanning trace dirs
                    agent_re = re.compile(rf"^{re.escape(prefix)}-(\w+)$")
                    turn_re = re.compile(rf"^{re.escape(prefix)}-t(\d+)-(\w+)$")
                    ts_re = re.compile(r"^Start:\s*(.+)$", re.MULTILINE)
                    transcripts = {}
                    scene_entries = []  # unified list for timestamp sorting
                    for td in sorted(traces_dir.iterdir()):
                        if not td.is_dir():
                            continue
                        tf = td / "transcript.md"
                        if not tf.exists():
                            continue
                        # Read timestamp from transcript header
                        header = tf.read_text()[:500]
                        ts_match = ts_re.search(header)
                        timestamp = ts_match.group(1).strip() if ts_match else ""

                        # Copy to public traces
                        dest_dir = traces_dest / td.name
                        dest_dir.mkdir(parents=True, exist_ok=True)
                        dest_file = dest_dir / "transcript.md"
                        if not dest_file.exists():
                            shutil.copy2(tf, dest_file)
                        url = f"traces/{sim_id}/{td.name}/transcript.md"

                        # Turn-based trace (e.g. day01-scene1-t1-finn)
                        tm = turn_re.match(td.name)
                        if tm:
                            agent = tm.group(2)
                            scene_entries.append({"agent": agent, "url": url, "ts": timestamp})
                            continue
                        # Agent trace (e.g. day01-scene1-finn)
                        am = agent_re.match(td.name)
                        if am:
                            agent = am.group(1)
                            transcripts[agent] = url
                            scene_entries.append({"agent": agent, "url": url, "ts": timestamp})
                    if transcripts:
                        sc["transcripts"] = transcripts

                    # Build chronological transcript_list sorted by timestamp
                    scene_entries.sort(key=lambda x: x["ts"])
                    tl = []
                    if gm_url:
                        tl.append({"label": "Game Master", "agent": "_gm", "url": gm_url})
                    for i, entry in enumerate(scene_entries):
                        agent = entry["agent"]
                        tl.append({
                            "label": agent.title(),
                            "agent": agent,
                            "order": i + 1,
                            "url": entry["url"],
                        })
                    if tl:
                        sc["transcript_list"] = tl

            copied = sum(1 for d in traces_dest.iterdir() if d.is_dir()) if traces_dest.exists() else 0
            print(f"Traces: {copied} Verzeichnisse kopiert nach {traces_dest}")

    # Copy concept art images to frontend/public/gallery/
    if args.sim_dir:
        src_concepts = gallery_dir / "concepts"
        if src_concepts.exists():
            dest_concepts = ROOT / "frontend" / "public" / "gallery" / "concepts"
            img_count = 0
            for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
                for img_file in src_concepts.rglob(ext):
                    rel = img_file.relative_to(src_concepts)
                    dest_file = dest_concepts / rel
                    if not dest_file.exists():
                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(img_file, dest_file)
                        img_count += 1
            if img_count:
                print(f"Concept Art: {img_count} Bilder kopiert nach {dest_concepts}")

    data = {"days": days}
    if agent_memories:
        data["agent_memories"] = agent_memories
    if roster:
        data["roster"] = roster
    if chapters:
        data["chapters"] = chapters
    if concept_art:
        data["concept_art"] = concept_art

    out_file.parent.mkdir(parents=True, exist_ok=True)
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    out_file.write_text(json_str)

    # Also copy to frontend/public/data/ for the Phaser viewer
    if args.sim_dir:
        sim_id = args.sim_dir.replace("/", "-")
        frontend_copy = ROOT / "frontend" / "public" / "data" / f"{sim_id}.json"
        frontend_copy.parent.mkdir(parents=True, exist_ok=True)
        frontend_copy.write_text(json_str)
        print(f"Viewer copy: {frontend_copy}")

    total_scenes = sum(len(d["scenes"]) for d in days)
    print(f"Built simulation.json: {len(days)} Tage, {total_scenes} Szenen")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
