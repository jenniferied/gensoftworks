# GenSoftworks

AI Creative Studio Simulator — multi-agent generative system inspired by Stanford's Generative Agents (Park et al. 2023). Seven agents live and work in a virtual 2D game studio, building a dark fantasy CRPG's worldbuilding bible and game design document through organic interaction. The human user is the Creative Director.

## Architecture

- **Design docs**: `blueprint/` (00–08, numbered)
- **Characters**: `roster/` (one `.md` per agent with YAML frontmatter)
- **Agent defs**: `.claude/agents/` (subagent definitions)
- **State**: `state/` (world.json, agents/*.json, memories/*.jsonl)
- **Reference shelf**: `library/` (papers, artbooks, GDDs, WBBs)
- **Tracking**: `pinwall/ROADMAP.md` + `pinwall/COMPLETED.md`
- **Logs**: `logbook/` (scene logs per day, v2 schema)
- **Output**: `gallery/` (gdd/, wbb/, concepts/, writing/)
- **Archive**: `simulation-1/` (completed sim 1 data)
- **Viewer**: `frontend/` (Phaser.js + Tiled browser viewer)
- **Scripts**: `scripts/` (build-viewer-data.py, export-logbook.py, capture-scenes.mjs)

## Run

```
/scene              # Run next scene (interactive)
/day                # Run full day (autopilot)
/brief "message"    # Post Creative Director feedback
```

## Tech Stack

| Component | Tool |
|-----------|------|
| Engine | Claude Code (subscription) |
| Game Master | Main Claude Code session |
| Agents | Custom subagents (`.claude/agents/`) |
| State | JSON/JSONL files |
| Viz | Phaser.js + Tiled (browser) |
| Images | Fal.ai (via prompts from Vera) |
| Map editor | Tiled |
| Export | Pandoc + XeLaTeX |

## Guardrails

- **Design-first**: All architecture in `blueprint/` before code
- **Research-grounded**: Every system must cite its academic basis
- **Log everything**: Every agent thought, observation, reflection → `logbook/`
- **v2 schema**: All fields in every scene, no compound types (see `blueprint/07-logging.md`)
- **Never invent citations** — same rule as master-thesis
- **German content, English code** — agents speak German in-sim
