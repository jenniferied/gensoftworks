# 01 — Architecture

## System Overview

```
                    ┌────────────────────┐
                    │   CREATIVE DIRECTOR │
                    │   (Human — You)     │
                    └─────────┬──────────┘
                              │ Briefings, Feedback, Observation
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     SIMULATION ENGINE                        │
│                                                              │
│  ┌──────────┐  ┌──────────────┐  ┌────────────────────────┐│
│  │ CLOCK    │  │ WORLD        │  │ EVENT SYSTEM           ││
│  │          │  │              │  │                        ││
│  │ Tick     │  │ Rooms        │  │ Proximity triggers     ││
│  │ Day/Night│  │ Positions    │  │ Scheduled meetings     ││
│  │ Seasons  │  │ Pathfinding  │  │ External events        ││
│  │          │  │ Collision    │  │ (GamesBomb, deadlines) ││
│  └──────────┘  └──────────────┘  └────────────────────────┘│
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                     AGENT LAYER                              │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ PERSONA      │  │ MEMORY       │  │ COGNITIVE     │      │
│  │              │  │ STREAM       │  │ MODULES       │      │
│  │ Identity     │  │              │  │               │      │
│  │ Traits       │  │ Observations │  │ Perceive      │      │
│  │ Preferences  │  │ Reflections  │  │ Retrieve      │      │
│  │ Relationships│  │ Plans        │  │ Reflect       │      │
│  │ Skills       │  │ Artifacts    │  │ Plan          │      │
│  └──────────────┘  └──────────────┘  │ Act           │      │
│                                       │ Converse      │      │
│                                       └──────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                     OUTPUT LAYER                             │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐ │
│  │ CREATIVE │  │ IMAGE    │  │ LOGBOOK  │  │ VISUALIZER │ │
│  │ PIPELINE │  │ GEN      │  │          │  │            │ │
│  │          │  │          │  │ JSON per │  │ Pygame     │ │
│  │ WBB text │  │ Fal.ai   │  │ tick     │  │ + Tiled    │ │
│  │ GDD text │  │ concepts │  │ PDF/HTML │  │ 2D top-    │ │
│  │ Design   │  │ moods    │  │ export   │  │ down view  │ │
│  │ decisions│  │ refs     │  │          │  │            │ │
│  └──────────┘  └──────────┘  └──────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                     STORAGE LAYER                            │
│                                                              │
│  SQLite (memories)  ·  ChromaDB (embeddings)  ·  Filesystem │
└─────────────────────────────────────────────────────────────┘
```

## Component Breakdown

### Simulation Engine

**Clock** — Manages simulated time. One "tick" = 15 simulated minutes. A full day = 96 ticks. The simulation can run at variable speed: real-time observation or fast-forward.

**World** — The physical 2D space. Loaded from a Tiled `.tmx` file. Contains rooms with named zones (desks, meeting areas, kitchen). Agents have positions (x, y) and move between locations using A* pathfinding on the collision layer.

**Event System** — Three event types:
1. **Proximity events** — Two agents within interaction radius. Memory-based decision: talk or not?
2. **Scheduled events** — Weekly D&D night, daily standup, monthly GamesBomb visit
3. **External events** — Creative Director posts feedback, deadline pressure increases, new reference material arrives

### Agent Layer

**Persona** — Static identity (name, background, personality traits, favorite games, relationships) loaded from `roster/*.md` YAML frontmatter. Does not change during simulation.

**Memory Stream** — The core innovation from Park et al. 2023. Chronological database of every observation, reflection, and plan. Retrieved via weighted scoring: `0.5 * recency + 3.0 * relevance + 2.0 * importance`. See `02-memory-system.md`.

**Cognitive Modules** — Five functions that mirror the Generative Agents architecture:

| Module | Input | Output | LLM Model |
|--------|-------|--------|-----------|
| **Perceive** | World state, nearby agents/objects | New observations added to memory | — (no LLM, just sensing) |
| **Retrieve** | Current situation/query | Top-K relevant memories | Embeddings only |
| **Reflect** | Accumulated importance > threshold | Higher-order insights | Sonnet |
| **Plan** | Morning context + recent reflections | Daily schedule, hourly tasks | Haiku |
| **Act** | Current plan + perceived situation | Movement, creation, conversation | Haiku (routine) / Sonnet (creative) |
| **Converse** | Proximity trigger + retrieved memories | Multi-turn dialogue with other agent | Sonnet |

### Output Layer

**Creative Pipeline** — Transforms agent work into actual artifacts:
- Worldbuilder writes lore → saved as Markdown in `gallery/lore/`
- Concept Artist generates prompts → Fal.ai → images in `gallery/concepts/`
- Game Director writes mechanics → saved in `gallery/designs/`
- All artifacts enter the agents' memory streams as shared observations

**Logbook** — Every tick produces a JSON log entry: agent positions, observations, conversations, reflections, artifacts created. Exportable to PDF (via WeasyPrint + Jinja2 templates) or HTML for web viewing.

**Visualizer** — Pygame renders the studio in real-time: agent sprites walking, speech bubbles for conversations, thought bubbles for reflections, artifact thumbnails when created.

## Data Flow (One Tick)

```
1. Clock advances (+15 min)
2. For each agent (parallel where possible):
   a. PERCEIVE: What's nearby? Who's here? What changed?
   b. RETRIEVE: What memories are relevant to current situation?
   c. DECIDE: Follow plan? React to something? Start conversation?
   d. ACT: Move, work, talk, create
   e. OBSERVE: Log what happened to memory stream
   f. CHECK REFLECTION: Has importance accumulated past threshold?
      → If yes: REFLECT, store insights
3. Log tick state to logbook
4. Render frame to visualization
5. Check for Creative Director input
```

## Integration Points

### With master-thesis repo
- `gallery/` artifacts can be copied/linked into `master-thesis/project/`
- The simulation itself is documented in the thesis (methodology chapter)

### With Claude Code
- The simulation calls Claude API directly (not Claude Code CLI)
- But development happens IN Claude Code with agents, skills, hooks
- Hooks could validate agent outputs, enforce style guides
- MCP servers provide access to Semantic Scholar, Fal.ai

### Cost Control
- **Haiku** ($1/$5 per 1M in/out): Perceive, Plan, routine Act
- **Sonnet** ($3/$15 per 1M in/out): Reflect, Converse, creative Act
- **Prompt caching**: Agent personas cached (90% discount on repeated input)
- **Embedding**: text-embedding-3-small at $0.02/1M (negligible)
- **Target**: ~$20–30 per simulated day with 6 agents
