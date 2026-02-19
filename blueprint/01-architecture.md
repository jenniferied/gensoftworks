# 01 — Architecture

## System Overview

```
                    ┌────────────────────┐
                    │   CREATIVE DIRECTOR │
                    │   (Human — You)     │
                    └─────────┬──────────┘
                              │ Briefings, Feedback, Intervention
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     GAME MASTER                              │
│              (Main Claude Code Session)                       │
│                                                              │
│  Reads world state → Determines next scene →                 │
│  Spawns agent subagents → Reconciles results →               │
│  Updates state → Writes logbook → Asks CD for input          │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                     AGENT SUBAGENTS                           │
│              (Spawned per scene via Task tool)                │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ PERSONA      │  │ MEMORY       │  │ SCENE        │      │
│  │              │  │ STREAM       │  │ RESPONSE     │      │
│  │ .claude/     │  │              │  │              │      │
│  │ agents/      │  │ memories/    │  │ Action       │      │
│  │ {name}.md    │  │ {name}.jsonl │  │ Dialogue     │      │
│  │              │  │              │  │ Thoughts     │      │
│  │ Identity     │  │ Observations │  │ Artifacts    │      │
│  │ Traits       │  │ Reflections  │  │ New memories │      │
│  │ Preferences  │  │ Artifacts    │  │ Position     │      │
│  │ Relationships│  │ Plans        │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                     STATE LAYER (Files)                       │
│                                                              │
│  state/world.json  ·  state/agents/*.json  ·                 │
│  state/memories/*.jsonl  ·  state/bulletin.json              │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                     OUTPUT LAYER                             │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐ │
│  │ GALLERY  │  │ LOGBOOK  │  │ PHASER   │  │ EXPORT     │ │
│  │          │  │          │  │ VIZ      │  │            │ │
│  │ lore/    │  │ scene    │  │          │  │ PDF/HTML   │ │
│  │ concepts/│  │ logs per │  │ Reads    │  │ via Jinja2 │ │
│  │ designs/ │  │ day      │  │ state/   │  │ + Weasy    │ │
│  │ writing/ │  │          │  │ renders  │  │            │ │
│  └──────────┘  └──────────┘  └──────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Key Design Decision: Claude Code IS the Engine

There is no separate Python simulation server. The Claude Code session (on subscription) acts as both the **Game Master** and the **runtime**:

- The Game Master reads state files, decides what scene happens next, spawns agent subagents (up to 7 in parallel via the Task tool), reconciles their outputs, and updates state.
- Each agent is a **custom subagent** defined in `.claude/agents/{name}.md` with personality, role, memory access, and restricted tools.
- The simulation advances when the Creative Director triggers it (`/scene`, `/day`) or Claude suggests the next beat.
- All state lives in JSON/JSONL files — no database, no embedding service, no API keys.

This means the simulation runs on a **Claude Pro/Max subscription** with zero additional cost.

## Component Breakdown

### Game Master (Main Session)

The orchestrator. Responsible for:

1. **Scene selection** — What happens next? (See `03-simulation-loop.md`)
2. **Agent dispatch** — Spawn relevant subagents for the scene
3. **Reconciliation** — If two agents are in the same scene, merge their outputs into coherent interaction
4. **State updates** — Write new positions, memories, artifacts to state files
5. **Logging** — Append scene to `logbook/`
6. **Creative Director interface** — Present results, ask for input, accept feedback

### Agent Subagents

Each of the 7 agents is defined as a `.claude/agents/{name}.md` file with YAML frontmatter:

```yaml
---
name: emre-worldbuilder
description: "Emre Yilmaz — Worldbuilder at GenSoftworks"
tools:
  - Read      # read own memories, world state, library references
  - Write     # write artifacts to gallery/
  - Glob      # find relevant files
---
```

When spawned for a scene, a subagent receives:
- Its persona (from the agent definition + `roster/{name}.md`)
- Its recent memories (last ~50 entries from `state/memories/{name}.jsonl`)
- The scene context (who's present, where, what's happening)
- The bulletin board (Creative Director feedback, shared decisions)

The subagent returns a structured response: what they do, say, think, and create.

### State Layer

```
state/
├── world.json              # Day counter, time of day, scene log, scheduled events
├── agents/
│   ├── emre.json           # Position, current task, today's plan, mood
│   ├── vera.json
│   ├── darius.json
│   ├── nami.json
│   ├── tobi.json
│   ├── leo.json
│   └── finn.json
├── memories/
│   ├── emre.jsonl          # Chronological memory stream
│   ├── vera.jsonl
│   └── ...
└── bulletin.json           # Creative Director posts, team decisions, deadlines
```

### Output Layer

**Gallery** — Real artifacts in `gallery/`, same structure as `05-creative-pipeline.md`.

**Logbook** — One JSONL file per simulated day (`logbook/day-001.jsonl`), one entry per scene.

**Phaser.js Visualization** — Browser-based, reads `state/` files, renders the Tiled map with agent sprites. Independent layer — the viz doesn't need Claude to run. See `06-visualization.md`.

**Export** — PDF/HTML from logbook data via Jinja2 + WeasyPrint.

## Data Flow (One Scene)

```
1. Game Master reads state/world.json → decides scene type and participants
2. Game Master reads relevant agent states + recent memories
3. Spawn involved agents as subagents (parallel via Task tool)
   Each subagent:
   a. Reads its persona + memories + scene context
   b. Decides: what do I do/say/think in this scene?
   c. Returns: actions, dialogue, thoughts, new memories, artifacts (if any)
4. Game Master reconciles outputs:
   - If two agents interact → weave their dialogue together
   - If an agent creates an artifact → save to gallery/
   - Update all agent positions and states
5. Append new memories to state/memories/*.jsonl
6. Write scene to logbook/day-XXX.jsonl
7. Update state/world.json (advance time, increment scene counter)
8. Present scene summary to Creative Director
9. Creative Director: continue? intervene? skip to next day?
```

## Integration Points

### With master-thesis repo
- `gallery/` artifacts flow into `master-thesis/project/`
- The simulation methodology is documented in the thesis
- Logbook exports become thesis appendix material

### With Phaser.js visualization
- Viz reads `state/` directory (polling or file-watch)
- Completely decoupled — can run without viz, or viz can replay past days
- WebSocket bridge optional for live updates (Phase 3+)

### With Claude Code ecosystem
- **Subagents**: 7 agent definitions in `.claude/agents/`
- **Skills**: `/scene`, `/day`, `/brief` for Creative Director commands
- **Hooks**: Validate artifacts, enforce German language, auto-log
- **MCP**: Optional — could expose world state as MCP tools for richer agent interaction

## Cost

**Zero additional cost.** Everything runs on the Claude Pro/Max subscription. Token usage comes from the subscription allowance. Scene-based simulation minimizes token usage: 3–6 scenes per day instead of 36–96 ticks.
