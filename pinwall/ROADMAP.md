# Roadmap

> Source of truth for GenSoftworks development. Updated as work progresses.

## Phase 0 — Blueprint ✓

> Design everything before building anything.

- [x] Repository + physicalized folder structure
- [x] Vision document (`blueprint/00-vision.md`)
- [x] Architecture overview (`blueprint/01-architecture.md`)
- [x] Memory system design (`blueprint/02-memory-system.md`)
- [x] Simulation loop design (`blueprint/03-simulation-loop.md`)
- [x] Conversation system design (`blueprint/04-conversation.md`)
- [x] Creative pipeline design (`blueprint/05-creative-pipeline.md`)
- [x] Visualization design (`blueprint/06-visualization.md`)
- [x] Logging & export design (`blueprint/07-logging.md`)
- [x] Research foundations (`blueprint/08-research-foundations.md`)
- [x] Character roster (7 agents in `roster/`)
- [x] CLAUDE.md, ROADMAP.md, COMPLETED.md
- [ ] Migrate papers from `master-thesis/literature-review/papers/` to `library/papers/`
- [ ] Review all blueprints for completeness

## Technical Decisions (2026-02-20)

> Resolved during architecture research session.

- **LLM access**: Claude Agent SDK (`claude-agent-sdk`) — runs on Claude Code subscription, no per-token API billing
- **Model routing**: Sonnet 4.6 for agent cognition, Opus 4.6 for synthesis/world events
- **Parallelism**: `asyncio.gather()` — all 7 agents run concurrently per tick
- **Visualization**: Phaser.js in browser (adapted from Stanford Generative Agents repo, Apache 2.0)
- **Tileset**: 16x16 px, purchased pack (LimeZu Modern Interiors or similar)
- **Map creation**: Generated with code from `blueprint/06-visualization.md` floorplan
- **Agent Teams / Mailbox / Shards**: Not applicable — these are CLI features, not SDK APIs
- **Workspace safety**: asyncio.Lock on SQLite + agent-namespaced gallery directories

## Phase 1 — Foundation (current)

> Core simulation without visualization.

- [ ] Python project scaffold (`workshop/`, uv, src layout)
- [ ] Agent SDK integration (`claude-agent-sdk`, async query wrapper)
- [ ] Model dispatch layer (Sonnet for agents, Opus for synthesis)
- [ ] Memory stream implementation (SQLite + ChromaDB)
- [ ] Retrieval scoring function (recency + importance + relevance)
- [ ] Importance scoring via Haiku
- [ ] Embedding pipeline (OpenAI text-embedding-3-small)
- [ ] Agent persona loading from `roster/*.md` YAML frontmatter
- [ ] Reflection mechanism
- [ ] Planning mechanism (daily + hourly)
- [ ] Unit tests for memory, retrieval, reflection

## Phase 2 — Simulation Engine

> Agents that move, perceive, and decide.

- [ ] Clock system (tick-based, variable speed)
- [ ] World grid from Tiled map JSON
- [ ] Agent pathfinding (A* on collision layer)
- [ ] Proximity detection
- [ ] Event bus (proximity, scheduled, external events)
- [ ] Conversation system (multi-turn dialogue, German)
- [ ] Cross-agent observation (memory stream broadcast)
- [ ] Daily simulation loop (64 ticks = 1 day)
- [ ] State snapshots for resumability
- [ ] Integration test: run 1 simulated day, inspect logs

## Phase 3 — Visualization (parallel with Phase 1–2)

> See the studio come alive. Browser-based, adapted from Stanford Generative Agents.

- [ ] Acquire tileset (16x16, modern interior)
- [ ] Acquire/create character sprites (7 agents)
- [ ] Generate studio map JSON from floorplan design
- [ ] Phaser.js frontend setup (renders map + agents in browser)
- [ ] Python web server bridging simulation → Phaser (WebSocket)
- [ ] Agent sprites + walking animation
- [ ] Speech bubbles for conversations
- [ ] Thought bubbles for reflections
- [ ] UI overlay (clock, agent status, speed controls)
- [ ] Creative Director input panel (post feedback, give briefings)

## Phase 4 — Creative Pipeline

> Agents produce real artifacts.

- [ ] Emre (Worldbuilder) → Markdown lore entries
- [ ] Vera (Concept Artist) → Fal.ai image generation
- [ ] Darius (Game Director) → GDD section drafts
- [ ] Nami (Narrative Designer) → dialogue/quest text
- [ ] Artifact display in `gallery/` and in-sim
- [ ] Cross-agent artifact observation system
- [ ] Style guide emergence tracking

## Phase 5 — Logging & Export

> Make every thought observable.

- [ ] JSON log per tick (all agent states, actions, conversations)
- [ ] Daily summary generation (Opus synthesis)
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

## Phase 7 — Polish & Integration

> Connect to thesis, refine the experience.

- [ ] Export to master-thesis repo pipeline
- [ ] Claude Code hooks for agent output validation
- [ ] MCP server for shared studio state
- [ ] Performance tuning (subscription rate limits, batch agents if needed)

## Stretch Goals

- [ ] Voice synthesis for agent dialogue
- [ ] Agent portraits (generated, consistent across sessions)
- [ ] Visitor agents (external characters at GamesBomb)
- [ ] Multiple studio layouts (crunch mode, relaxed mode)
- [ ] Emotional model (mood affects creative output quality)
