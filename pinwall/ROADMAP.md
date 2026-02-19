# Roadmap

> Source of truth for GenSoftworks development. Updated as work progresses.

## Phase 0 — Blueprint (current)

> Design everything before building anything.

- [x] Repository + physicalized folder structure
- [x] Vision document (`blueprint/00-vision.md`)
- [x] Architecture overview (`blueprint/01-architecture.md`)
- [x] Memory system design (`blueprint/02-memory-system.md`)
- [x] Character roster (6 agents in `roster/`)
- [x] Research foundations (`blueprint/08-research-foundations.md`)
- [x] CLAUDE.md, ROADMAP.md, COMPLETED.md
- [ ] Migrate papers from `master-thesis/literature-review/papers/` (180 files, 12 categories) to `library/papers/`
- [ ] Simulation loop design (`blueprint/03-simulation-loop.md`)
- [ ] Conversation system design (`blueprint/04-conversation.md`)
- [ ] Creative pipeline design (`blueprint/05-creative-pipeline.md`)
- [ ] Visualization design (`blueprint/06-visualization.md`)
- [ ] Logging & export design (`blueprint/07-logging.md`)
- [ ] Review all blueprints for completeness

## Phase 1 — Foundation

> Core simulation without visualization.

- [ ] Python project scaffold (uv, src layout, tests)
- [ ] Memory stream implementation (SQLite + ChromaDB)
- [ ] Retrieval scoring function (recency + importance + relevance)
- [ ] Importance scoring via Claude Haiku
- [ ] Embedding pipeline (OpenAI text-embedding-3-small)
- [ ] Basic agent persona loading from YAML
- [ ] Reflection mechanism
- [ ] Planning mechanism (daily + hourly)
- [ ] Unit tests for memory, retrieval, reflection

## Phase 2 — Simulation Engine

> Agents that move, perceive, and decide.

- [ ] Clock system (tick-based, variable speed)
- [ ] World grid from Tiled `.tmx` file
- [ ] Agent pathfinding (A* on collision layer)
- [ ] Proximity detection
- [ ] Event system (proximity, scheduled, external)
- [ ] Conversation system (multi-turn dialogue)
- [ ] Daily simulation loop (96 ticks = 1 day)
- [ ] State snapshots for resumability
- [ ] Integration test: run 1 simulated day, inspect logs

## Phase 3 — Visualization

> See the studio come alive.

- [ ] Pygame window + main render loop
- [ ] Tiled map rendering (PyTMX)
- [ ] Agent sprites + walking animation
- [ ] Speech bubbles for conversations
- [ ] Thought bubbles for reflections
- [ ] UI overlay (clock, agent status, current activity)
- [ ] Creative Director input panel (post feedback, give briefings)
- [ ] Camera controls (pan, zoom)

## Phase 4 — Creative Pipeline

> Agents produce real artifacts.

- [ ] Worldbuilder → Markdown lore entries
- [ ] Concept Artist → Fal.ai image generation
- [ ] Game Director → GDD section drafts
- [ ] Narrative Designer → dialogue/quest text
- [ ] Artifact display in gallery/ and in-sim
- [ ] Cross-agent artifact observation system
- [ ] Style guide emergence tracking

## Phase 5 — Logging & Export

> Make every thought observable.

- [ ] JSON log per tick (all agent states, actions, conversations)
- [ ] Daily summary generation
- [ ] PDF export (WeasyPrint + Jinja2 templates)
- [ ] HTML export (browsable web page)
- [ ] Memory stream visualization (timeline view)
- [ ] Relationship graph visualization

## Phase 6 — Events & Enrichment

> The studio becomes a living world.

- [ ] Weekly D&D night (agents play together, build rapport)
- [ ] GamesBomb event (Cologne, visitor feedback, industry contacts)
- [ ] Deadline pressure mechanics (affects agent mood/focus)
- [ ] Relationship evolution (friendships deepen, tensions arise)
- [ ] Library integration (agents reference papers, artbooks)
- [ ] Creative Director presence mechanics (agents react to your visits)

## Phase 7 — Claude Code Integration

> Leverage the development environment.

- [ ] Hooks for agent output validation
- [ ] MCP server for shared studio state
- [ ] Skills for quick agent interactions
- [ ] Export to master-thesis repo pipeline
- [ ] Evaluate: Agent Teams for parallel simulation?

## Stretch Goals

- [ ] Phaser.js web frontend (shareable URL, browser-based)
- [ ] Voice synthesis for agent dialogue
- [ ] Agent portraits (generated, consistent across sessions)
- [ ] Visitor agents (external characters at GamesBomb)
- [ ] Multiple studio layouts (crunch mode, relaxed mode)
- [ ] Emotional model (mood affects creative output quality)
