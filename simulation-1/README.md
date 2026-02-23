# Simulation 1 — Archive

**Dates**: 2026-02-19 to 2026-02-21 (5 simulated days)
**Scenes**: 25 total (8 → 9 → 4 → 3 → 3 per day)
**Schema**: v1 (3 variants across 5 days — see notes below)

## Deliverables

- GDD v0.3 — `gallery/gdd/RELICS-GDD-v03.md` (225 KB, 1830 lines)
- WBB v0.3 — `gallery/wbb/RELICS-WBB-v03-export.md` (49 MB PDF, landscape multi-column, 26 concept arts)
- 35 concept art pieces across 4 rounds ($8 total)
- Logbook PDF — `export/logbook-tag-001.pdf`

## Schema Note

The log schema drifted three times during simulation 1:

1. **Day 1**: `scene_number`, `scene_type`, `dialogue[].agent`, `memories_added[].agent`
2. **Day 2–3**: Added `agent_details` (mood_before, mood_after, key_reaction), renamed some fields
3. **Day 4–5**: Inconsistent `time_of_day` values, compound types (`WORK+REFLECTION`)

Simulation 2 uses a fixed v2 schema. See `blueprint/07-logging.md`.

## Directory Structure

```
simulation-1/
├── state/           # Final agent states + memories after day 5
├── logbook/         # day-001.jsonl through day-005.jsonl
├── gallery/         # GDD, WBB, concept art, writing
├── pinwall/         # ROADMAP.md + COMPLETED.md from sim 1
├── export/          # LaTeX export output
└── viewer-data/     # simulation.json for Phaser viewer
```
