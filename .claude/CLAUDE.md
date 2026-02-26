# GenSoftworks

Seven role-based AI agents (ChatDev) interact in scene-based encounters (Park et al. 2023) to produce text and images (fal.ai) for a dark fantasy CRPG's game design document and worldbuilding bible. Open scenes instead of a rigid pipeline allow spontaneous creative ideas. The human user is the Creative Director.

## How a Day Works

1. **Briefing** — CD posts vision/feedback in `simulation-2/briefing.md`
2. **Scenes** — Game Master runs 5+ scenes (TALK, WORK, REVIEW) with agent subprocesses
3. **Feedback** — CD reviews artifacts, gives direction for next day

## Where Things Live

| Path | Content |
|------|---------|
| `roster/` | Character bios (7 agents, YAML frontmatter) |
| `.claude/agents/` | Agent prompt definitions |
| `library/` | Reference material (papers, artbooks, GDDs, WBBs) |
| `simulation-2/` | Active sim: logbook/, gallery/, state/, pinwall/ |
| `ARCHIVE-SIM1.md` | Reference doc for archived simulation 1 |
| `frontend/` | Phaser.js + Tiled browser viewer |
| `assets/` | Icons (bubble/agent PNGs for export + viewer) |
| `scripts/` | build-viewer-data.py, export-logbook.py |
| `templates/` | LaTeX export templates |

## Logbook Schema (v3 — simplified)

```json
{"scene": 1, "type": "TALK|WORK|REVIEW", "time": "morning|afternoon|evening",
 "location": "kueche|lore-ecke|art-station|...", "participants": ["vera","emre"],
 "summary": "...", "dialogue": [{"who":"vera","says":"..."}],
 "artifacts": [], "cd_feedback": null}
```

## Guardrails

- **German content, English code** — agents speak German in-sim
- **Never invent citations** — if unsure, say so
- **Log everything** — every scene → `simulation-2/logbook/`
- **Logbook IS the memory** — no separate memory system, last scenes = agent context
