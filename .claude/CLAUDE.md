# GenSoftworks

AI Creative Studio Simulator — multi-agent generative system inspired by Stanford's Generative Agents (Park et al. 2023). Seven agents live and work in a virtual 2D game studio, building a dark fantasy CRPG's worldbuilding bible and game design document through organic interaction. The human user is the Creative Director.

## Architecture

- **Design docs**: `blueprint/` (00–08, numbered)
- **Characters**: `roster/` (one `.md` per agent with YAML frontmatter)
- **Simulation code**: `workshop/` (Python, Pygame + Claude API)
- **Reference shelf**: `library/` (papers, artbooks, GDDs, WBBs)
- **Tracking**: `pinwall/ROADMAP.md` + `pinwall/COMPLETED.md`
- **Logs**: `logbook/` (daily simulation logs, exportable)
- **Output**: `gallery/` (generated lore, concepts, designs)

## Build & Run

```bash
uv run studio          # Launch simulation
uv run studio --day 5  # Resume from day 5
uv run export-log      # Export logbook as PDF/HTML
```

## Tech Stack

| Component | Tool |
|-----------|------|
| Language | Python 3.12+ |
| Viz | Pygame + PyTMX + Tiled |
| LLM | Claude API (Haiku routine, Sonnet reflection) |
| Embeddings | OpenAI text-embedding-3-small |
| Memory DB | SQLite + ChromaDB |
| Images | Fal.ai API |
| Map editor | Tiled |

## Guardrails

- **Design-first**: All architecture in `blueprint/` before code in `workshop/`
- **Research-grounded**: Every system must cite its academic basis
- **Log everything**: Every agent thought, observation, reflection → `logbook/`
- **Never invent citations** — same rule as master-thesis
- **German content, English code** — agents speak German in-sim
