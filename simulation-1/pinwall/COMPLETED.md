# Completed

> What's been done. Newest first.

## 2026-02-21 — Logbook Viewer (Phase 3)

- [x] `build-viewer-data.py` — reads logbook + memories → `simulation.json` (3 Tage, 19 Szenen)
- [x] Sidebar redesign: Tag/Szene-Dropdowns, Vor/Zurück-Buttons, responsive layout
- [x] Agent-Karten pro Szene: Stimmung, Reaktion, Einflüsse, Erinnerungen (auto-expanded)
- [x] Phaser scene loading: Tween-basierte Agentenbewegung, Alpha-Dimming für Nicht-Teilnehmer
- [x] Event-System: `viewer:scene-change`, `viewer:agent-click`, `viewer:data-ready`
- [x] `npm run build:data` Script in package.json
- [x] Roadmap aktualisiert mit weiteren Viewer-Ideen

## 2026-02-20 — Architecture Decisions + Phase 0 Complete

- [x] Researched Claude Agent SDK capabilities vs Agent Teams (CLI-only, not SDK)
- [x] Decided: Agent SDK for subscription billing, asyncio.gather() for parallelism
- [x] Decided: Sonnet 4.6 (agent cognition) + Opus 4.6 (synthesis)
- [x] Decided: Phaser.js browser visualization (adapted from Stanford Generative Agents, Apache 2.0)
- [x] Decided: 48x48 tileset (LimeZu Modern Interiors), map generated with code
- [x] Ruled out: Agent Teams, Mailbox, Shared Task List, Shards, cagent (not SDK APIs)
- [x] Roadmap updated with all technical decisions
- [x] All blueprint documents (00–08) confirmed complete
- [x] Acquired tileset (48x48, LimeZu Modern Interiors)
- [x] Acquired premade character sprites (7 agents)

### Phase 0 — Blueprint (completed)

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

## 2026-02-19 — Project Genesis

- [x] Repository created
- [x] Directory structure with physicalized naming
- [x] Design documents drafted (blueprint/ 00–08)
- [x] Character roster created (7 agents)
- [x] CLAUDE.md, ROADMAP.md, COMPLETED.md
- [x] Research foundations documented
