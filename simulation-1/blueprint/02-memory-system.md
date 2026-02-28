# 02 — Memory System

> Based on Park et al. 2023, adapted for scene-based simulation running inside Claude Code. No external database or embedding service — Claude itself is the retrieval engine.

## Overview

Each agent maintains a **Memory Stream** — a JSONL file of observations, reflections, plans, conversations, and artifacts. This is the core of the system: an agent's accumulated memory IS their personality over time.

The key simplification from the Stanford architecture: there is no vector database. When an agent needs to recall something, Claude reads their memory file and selects what's relevant. For 7 agents generating ~10–20 memories per simulated day, this scales comfortably for months of simulation.

## Memory Node Schema

Each line in `state/memories/{agent}.jsonl`:

```json
{
    "id": "emre-042",
    "created": "day-003/scene-04",
    "type": "observation",
    "depth": 0,
    "description": "Vera hat ein Konzeptbild der Knochentürme gezeigt — organisch, dunkel, wie gewachsen statt gebaut.",
    "importance": 7,
    "tags": ["ashen-wastes", "bone-towers", "vera", "concept-art"],
    "evidence": [],
    "metadata": {}
}
```

### Fields

| Field | Purpose |
|-------|---------|
| `id` | `{agent}-{sequence_number}` |
| `created` | Scene reference: `day-XXX/scene-YY` |
| `type` | `observation`, `reflection`, `plan`, `artifact`, `conversation` |
| `depth` | 0 = direct experience, 1+ = reflection layers |
| `description` | Natural language, in German |
| `importance` | 1–10, scored by the agent subagent at creation time |
| `tags` | Keywords for quick scanning |
| `evidence` | For reflections: IDs of source memories |
| `metadata` | Extra data (artifact path, conversation partner, etc.) |

## Retrieval: Claude as the Search Engine

When an agent subagent is spawned for a scene, it receives its recent memories as context. The Game Master selects which memories to include:

**Default strategy** — last 50 memories (chronological) + all reflections (depth > 0). This keeps recent context fresh while preserving synthesized insights.

**Focused retrieval** — When a scene has a clear topic (e.g., "meeting about the Ashen Wastes"), the Game Master can grep the memory file for relevant tags and include those memories instead.

**Why this works without embeddings**: With ~10–20 memories per day and a target of weeks-to-months of simulation, an agent accumulates hundreds of memories, not thousands. Claude can read and reason over hundreds of structured entries. The tag system enables fast pre-filtering before Claude even sees the content.

### Comparison to Stanford

| Aspect | Stanford (Park et al.) | GenSoftworks |
|--------|----------------------|--------------|
| Storage | SQLite + ChromaDB | JSONL files |
| Retrieval | Cosine similarity on embeddings | Claude reads + selects |
| Scoring | `0.5*recency + 3.0*relevance + 2.0*importance` | Claude weighs naturally |
| Scale | ~30 memories/agent/day, thousands total | ~10–20/agent/day, hundreds total |
| Cost | Embedding API calls | Zero (included in subscription) |

The tradeoff: Stanford's approach scales to thousands of memories with mathematical precision. Ours is simpler, cheaper, and sufficient for our scale. If memory files grow too large, we can summarize older entries into compressed "era summaries."

## Importance Scoring

When an agent creates a new memory, the subagent scores it 1–10 as part of its scene response. No separate LLM call needed — the agent is already "thinking" about the event.

Scale (adapted for creative context):
- **1–2**: Routine (refilled coffee, opened a file, walked to desk)
- **3–4**: Minor work (continued writing, reviewed notes)
- **5–6**: Notable (received feedback, had a relevant conversation)
- **7–8**: Significant (creative breakthrough, disagreement that produced insight)
- **9–10**: Pivotal (Creative Director brief that reframes the project, artistic epiphany)

## Reflection

### Trigger

Each agent's state (`state/agents/{name}.json`) tracks an `importance_accumulator`. New memories add their importance score. When the accumulator exceeds **100** (lowered from Stanford's 150 to account for fewer observations per day), the Game Master schedules a REFLECTION scene for that agent.

With average importance ~5, this triggers roughly every 2–3 simulated days — appropriate for scene-based pacing.

### Process

The reflection scene works like any other scene, but the agent subagent receives a special prompt:

1. **Input**: Last ~30 memories since previous reflection
2. **Task**: "What 3–5 higher-level insights or creative principles emerge from these experiences?"
3. **Output**: New reflection memories with `depth = max(evidence_depths) + 1` and `evidence` linking to source memory IDs

### Reflection Hierarchy

Reflections can build on other reflections:

```
Depth 0: "Vera hat ein Konzeptbild der Knochentürme gezeigt"
Depth 0: "Darius will einen Dungeon in den Aschen-Einöden"
Depth 1: "Die Aschen-Einöden werden zentral — Veras organische
          Ästhetik + Darius' Dungeon = lebende Strukturen" (from 0, 0)
Depth 0: "Creative Director sagt: lebende Türme brauchen Biologie"
Depth 2: "Die Türme könnten aus dem Nervensystem eines toten Titanen
          wachsen — das verbindet Geologie und Mythologie" (from 1, 0)
```

## Planning

### Daily Plan (ARRIVAL scene)

Each morning's ARRIVAL scene asks agents to declare their plan:

- What they want to work on today
- Who they want to talk to (if anyone)
- Whether they want to consult the library

Plans are stored in `state/agents/{name}.json` as `today_plan` and inform the Game Master's scene selection for the rest of the day.

### Reactive Re-Planning

If something unexpected happens mid-day (Creative Director feedback, a colleague's artifact that changes context), the Game Master can include a re-planning prompt in the next scene: "Given what just happened, does your plan for today change?"

## Creative Memory Adaptations

### Artifact Memories

When an agent creates something, it becomes a memory with rich metadata:

```json
{
    "id": "vera-028",
    "created": "day-003/scene-04",
    "type": "artifact",
    "depth": 0,
    "description": "Konzeptskizze erstellt: Knochentürme der Aschen-Einöden, organische Architektur, dunkle Palette, 3 Varianten.",
    "importance": 8,
    "tags": ["ashen-wastes", "bone-towers", "concept-art", "own-work"],
    "evidence": [],
    "metadata": {
        "artifact_path": "gallery/concepts/day-003_bone-towers_v1.png",
        "style_tags": ["organic", "dark-fantasy", "architectural"]
    }
}
```

### Cross-Agent Observation

When an agent creates an artifact, the Game Master adds an observation to other agents who were present:

```json
{
    "id": "emre-043",
    "type": "observation",
    "description": "Vera hat gerade eine Konzeptskizze der Knochentürme fertiggestellt. Der Stil ist organisch und dunkel — die Strukturen sehen gewachsen aus, nicht gebaut.",
    "importance": 6,
    "tags": ["vera", "bone-towers", "concept-art", "ashen-wastes"]
}
```

This is how ideas spread organically — not through assignment, but through observation and memory.

## State File Structure

```
state/
├── memories/
│   ├── emre.jsonl          # ~10-20 new entries per simulated day
│   ├── vera.jsonl
│   ├── darius.jsonl
│   ├── nami.jsonl
│   ├── tobi.jsonl
│   ├── leo.jsonl
│   └── finn.jsonl
└── agents/
    ├── emre.json           # includes importance_accumulator, today_plan
    └── ...
```
