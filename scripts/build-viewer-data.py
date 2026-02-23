#!/usr/bin/env python3
"""Build simulation.json for the Phaser logbook viewer.

Reads logbook/*.jsonl + state/memories/*.jsonl → frontend/public/data/simulation.json

Supports both v1 (simulation 1) and v2 (simulation 2+) log schemas.
Use --sim-dir to point at an archived simulation directory.
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

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
}


def detect_schema(entry):
    """Detect whether entry uses v1 or v2 schema."""
    if "mood" in entry and isinstance(entry["mood"], dict):
        return "v2"
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


def main():
    parser = argparse.ArgumentParser(description="Build simulation.json for Phaser viewer")
    parser.add_argument("--sim-dir", type=str, default=None,
                        help="Path to simulation archive dir (e.g. simulation-1)")
    args = parser.parse_args()

    if args.sim_dir:
        sim_root = ROOT / args.sim_dir
        logbook_dir = sim_root / "logbook"
        memories_dir = sim_root / "state" / "memories"
        out_file = sim_root / "viewer-data" / "simulation.json"
    else:
        logbook_dir = ROOT / "logbook"
        memories_dir = ROOT / "state" / "memories"
        out_file = ROOT / "frontend" / "public" / "data" / "simulation.json"

    all_memories = load_memories(memories_dir)
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
            if schema == "v2":
                scenes.append(build_scene_v2(entry))
            else:
                scenes.append(build_scene_v1(entry, all_memories))
        days.append({"day": day_num, "scenes": scenes})

    data = {"days": days}

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(data, ensure_ascii=False, indent=2))

    total_scenes = sum(len(d["scenes"]) for d in days)
    print(f"Built simulation.json: {len(days)} Tage, {total_scenes} Szenen")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
