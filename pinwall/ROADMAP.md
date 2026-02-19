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

> Resolved during architecture research sessions.

- **Engine**: Claude Code itself — the main session is the Game Master, agents are custom subagents
- **LLM access**: Claude Pro/Max subscription only — no API keys, no per-token billing
- **Model**: Whatever Claude Code uses (currently Opus 4.6 / Sonnet 4.6)
- **Parallelism**: Task tool spawns up to 7 subagents in parallel per scene
- **Simulation model**: Scene-based (3–6 scenes/day), not tick-based — inspired by Concordia's Game Master pattern
- **State storage**: JSON/JSONL files in `state/` — no database, no embedding service
- **Memory retrieval**: Claude reads agent memory files directly (no ChromaDB, no cosine similarity)
- **Visualization**: Phaser.js in browser (adapted from Stanford Generative Agents repo, Apache 2.0)
- **Tileset**: 48x48 px (LimeZu Modern Interiors)
- **Map creation**: Tiled editor, exported as TMX/JSON for Phaser.js
- **Agent definitions**: `.claude/agents/{name}.md` with YAML frontmatter
- **Creative Director commands**: Custom skills (`/scene`, `/day`, `/brief`)

## Phase 1 — Foundation (current)

> Agent subagents + state files + first scene.

- [ ] Create `state/` directory structure (world.json, agents/*.json, memories/*.jsonl, bulletin.json)
- [ ] Create 7 agent subagent definitions in `.claude/agents/`
- [ ] Seed initial agent state files from `roster/*.md`
- [ ] Define scene output schema (what a subagent returns)
- [ ] Build `/scene` skill (Game Master orchestration)
- [ ] Test: run one ARRIVAL scene with all 7 agents
- [ ] Test: run one ENCOUNTER scene between 2 agents
- [ ] Test: run one WORK scene producing an artifact in `gallery/`
- [ ] Memory append/read working for all agents
- [ ] Reflection trigger working (importance accumulator)

## Phase 2 — Full Day Loop

> A complete simulated day from arrival to evening.

- [ ] Build `/day` skill (run full day in autopilot or interactive mode)
- [ ] ARRIVAL → ENCOUNTER → WORK → MEETING → REFLECTION flow
- [ ] Scene selection logic (Game Master picks next scene)
- [ ] Creative Director intervention between scenes
- [ ] Cross-agent observation (artifact broadcast)
- [ ] State persistence (resume next day from `state/`)
- [ ] Daily summary generation
- [ ] Logbook writing (one JSONL per day)

## Phase 3 — Visualization (parallel with Phase 1–2)

> See the studio come alive. Browser-based, adapted from Stanford Generative Agents.

- [x] Acquire tileset (48x48, LimeZu Modern Interiors)
- [x] Acquire/create character sprites (7 agents)
- [ ] Build studio map in Tiled from floorplan design
- [ ] Phaser.js frontend setup (renders map + agents in browser)
- [ ] State file reader (polls `state/` for updates)
- [ ] Agent sprites + position rendering
- [ ] Speech bubbles from logbook scene data
- [ ] Thought bubbles for reflections
- [ ] UI overlay (day counter, scene info, agent status)

## Phase 4 — Creative Pipeline

> Agents produce real artifacts.

- [ ] Emre (Worldbuilder) → Markdown lore entries in `gallery/lore/`
- [ ] Vera (Concept Artist) → Fal.ai prompts + concept briefs
- [ ] Darius (Game Director) → GDD section drafts in `gallery/designs/`
- [ ] Nami (Narrative Designer) → dialogue/quest text in `gallery/writing/`
- [ ] Artifact display in Phaser.js viz
- [ ] Cross-agent artifact observation → memory broadcast
- [ ] Style guide emergence tracking

## Phase 5 — Logging & Export

> Make every thought observable and exportable.

- [ ] Scene-based JSONL logs per day
- [ ] Daily summary in logbook
- [ ] PDF export (WeasyPrint + Jinja2 templates)
- [ ] HTML export (browsable web page)
- [ ] Memory stream visualization (timeline view)
- [ ] Relationship graph visualization

## Phase 6 — Events & Enrichment

> The studio becomes a living world.

- [ ] Weekly D&D night (agents play together, special interaction mode)
- [ ] GamesBomb event (Cologne, visitor feedback, industry contacts)
- [ ] Deadline pressure mechanics (affects agent mood/focus)
- [ ] Relationship evolution (friendships deepen, tensions arise)
- [ ] Library integration (agents reference papers, artbooks)
- [ ] Creative Director presence mechanics

## Phase 7 — Polish & Integration

> Connect to thesis, refine the experience.

- [ ] Export to master-thesis repo pipeline
- [ ] Claude Code hooks for agent output validation
- [ ] Optional MCP server for richer world state access
- [ ] Session management (long-running simulation across days)

## Stretch Goals

- [ ] Agent Teams upgrade (when stable — agents message each other directly)
- [ ] Voice synthesis for agent dialogue
- [ ] Agent portraits (generated, consistent across sessions)
- [ ] Visitor agents (external characters at GamesBomb)
- [ ] Multiple studio layouts (crunch mode, relaxed mode)
- [ ] Emotional model (mood affects creative output quality)
