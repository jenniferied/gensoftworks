#!/usr/bin/env python3
"""Build simulation.json for the Phaser logbook viewer.

Reads logbook/*.jsonl + state/memories/*.jsonl → frontend/public/data/simulation.json
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGBOOK_DIR = ROOT / "logbook"
MEMORIES_DIR = ROOT / "state" / "memories"
OUT_FILE = ROOT / "frontend" / "public" / "data" / "simulation.json"

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
    "flur":              "hallway",
}

# Room center positions (tile coords) for distributing participants
ROOM_CENTERS = {
    "7a":        {"x": 4,  "y": 4},
    "7b":        {"x": 12, "y": 4},
    "7c":        {"x": 20, "y": 4},
    "conference": {"x": 29, "y": 4},
    "kitchen":   {"x": 38, "y": 4},
    "hallway":   {"x": 21, "y": 10},
    "7d":        {"x": 4,  "y": 16},
    "7e":        {"x": 12, "y": 16},
    "7f":        {"x": 20, "y": 16},
    "lounge":    {"x": 29, "y": 20},
    "7":         {"x": 12, "y": 23},
}

# Time labels
TIME_LABELS = {
    "morning": "Morgen",
    "late-morning": "Vormittag",
    "afternoon": "Nachmittag",
    "late-afternoon": "Spätnachmittag",
    "evening": "Abend",
    "morning-to-evening": "Ganztags",
}

# Type labels
TYPE_LABELS = {
    "ARRIVAL": "Ankunft",
    "MEETING": "Meeting",
    "ENCOUNTER": "Begegnung",
    "WORK": "Arbeit",
    "WORK+REFLECTION": "Arbeit",
    "BRIEF+REACTION": "Briefing",
    "REFLECTION": "Reflexion",
}


def load_memories():
    """Load all memories indexed by id."""
    memories = {}
    if not MEMORIES_DIR.exists():
        return memories
    for f in sorted(MEMORIES_DIR.glob("*.jsonl")):
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
        return None  # agents at own desks
    if "+" in loc:
        return None  # compound location — use heuristic per agent
    return LOCATION_ROOM.get(loc)


def compute_positions(participants, location):
    """Compute tile positions for all 7 agents in a scene."""
    positions = {}
    active_agents = [a for a in participants if a != "creative-director"]
    room = resolve_room(location)

    # Compound locations (e.g. "bibliothek+lore-ecke")
    compound_rooms = {}
    if "+" in location:
        parts = [p.strip() for p in location.split("+")]
        for part in parts:
            r = LOCATION_ROOM.get(part)
            if r:
                compound_rooms[part] = r

    for agent in ALL_AGENTS:
        if agent in active_agents:
            if room:
                # Distribute participants horizontally in the room
                center = ROOM_CENTERS[room]
                idx = active_agents.index(agent)
                count = len(active_agents)
                spread = min(count - 1, 4)
                offset = (idx - (count - 1) / 2) * (spread / max(count - 1, 1) * 2)
                positions[agent] = {
                    "x": round(center["x"] + offset, 1),
                    "y": center["y"],
                    "state": "active",
                }
            elif compound_rooms:
                # Heuristic for compound locations
                if agent == "emre" and "lore-ecke" in compound_rooms:
                    c = ROOM_CENTERS[compound_rooms["lore-ecke"]]
                    positions[agent] = {"x": c["x"], "y": c["y"], "state": "active"}
                elif "bibliothek" in compound_rooms:
                    c = ROOM_CENTERS[compound_rooms["bibliothek"]]
                    idx = [a for a in active_agents if a != "emre"].index(agent) if agent != "emre" else 0
                    count = len(active_agents) - (1 if "emre" in active_agents and "lore-ecke" in compound_rooms else 0)
                    offset = (idx - (count - 1) / 2) * 1.5
                    positions[agent] = {
                        "x": round(c["x"] + offset, 1),
                        "y": c["y"],
                        "state": "active",
                    }
                else:
                    positions[agent] = {**AGENT_DESKS[agent], "state": "active"}
            else:
                # studio-weit: everyone at their own desk
                positions[agent] = {**AGENT_DESKS[agent], "state": "active"}
        else:
            # Non-participant stays at desk, dimmed
            positions[agent] = {**AGENT_DESKS[agent], "state": "dimmed"}

    return positions


def build_scene(entry, all_memories):
    """Build a single scene object from a logbook entry."""
    participants = [p for p in entry.get("participants", []) if p != "creative-director"]
    location = entry.get("location", "studio-weit")
    scene_type = entry.get("type", "WORK")

    scene = {
        "scene": entry["scene"],
        "type": scene_type,
        "type_label": TYPE_LABELS.get(scene_type, scene_type),
        "time_of_day": entry.get("time_of_day", "morning"),
        "time_label": TIME_LABELS.get(entry.get("time_of_day", "morning"), entry.get("time_of_day", "morning")),
        "location": location,
        "location_label": location.replace("-", " ").title(),
        "participants": participants,
        "summary": entry.get("summary", ""),
        "key_moment": entry.get("key_moment", ""),
        "positions": compute_positions(entry.get("participants", []), location),
    }

    # Agent details (mood, reactions) — only present in day 2+ entries
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

    # Memories created in this scene
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


def main():
    all_memories = load_memories()
    logbook_files = sorted(LOGBOOK_DIR.glob("day-*.jsonl"))

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
            scenes.append(build_scene(entry, all_memories))
        days.append({"day": day_num, "scenes": scenes})

    data = {"days": days}

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))

    total_scenes = sum(len(d["scenes"]) for d in days)
    print(f"Built simulation.json: {len(days)} Tage, {total_scenes} Szenen")
    print(f"Output: {OUT_FILE}")


if __name__ == "__main__":
    main()
