# 02 — Memory System

> Based on Park et al. 2023, "Generative Agents: Interactive Simulacra of Human Behavior" (UIST 2023). Adapted for creative production agents.

## Overview

Each agent maintains a **Memory Stream** — a chronological database of every observation, reflection, plan, and created artifact. This is the single most important component: an agent's memory IS their personality over time.

## Memory Node Schema

```sql
CREATE TABLE memories (
    id            TEXT PRIMARY KEY,
    agent_id      TEXT NOT NULL,
    created       TIMESTAMP NOT NULL,
    last_accessed TIMESTAMP NOT NULL,
    type          TEXT NOT NULL,     -- observation | reflection | plan | artifact | conversation
    depth         INTEGER DEFAULT 0, -- 0=observation, 1+=reflection layers
    description   TEXT NOT NULL,     -- natural language
    subject       TEXT,              -- triplet: who/what
    predicate     TEXT,              -- triplet: did what
    object        TEXT,              -- triplet: to whom/what
    importance    INTEGER NOT NULL,  -- 1-10 (LLM-scored)
    keywords      TEXT,              -- JSON array
    evidence_ids  TEXT,              -- JSON array (for reflections: source node IDs)
    metadata      TEXT,              -- JSON blob (artifact_path, style_tags, etc.)
    embedding_key TEXT               -- reference into ChromaDB
);

CREATE INDEX idx_agent_time ON memories(agent_id, created DESC);
CREATE INDEX idx_agent_type ON memories(agent_id, type);
CREATE INDEX idx_importance ON memories(agent_id, importance DESC);
```

## Retrieval: The Scoring Function

When an agent needs to recall relevant memories (for conversation, planning, or creative work), the retrieval function scores every memory against the current query:

```
score(memory, query) = 0.5 * recency + 3.0 * relevance + 2.0 * importance
```

All three components are min-max normalized to [0, 1] before combination.

### Recency (exponential decay)

```python
decay_rate = 0.995  # per simulated hour
hours_since = (now - memory.last_accessed).total_seconds() / 3600
recency = decay_rate ** hours_since
```

Source: Park et al. use 0.995 decay per sandbox game hour. Memories accessed recently score higher. Accessing a memory during retrieval updates `last_accessed`, creating a "the rich get richer" effect — frequently recalled memories stay accessible.

### Importance (LLM-scored, 1–10)

Scored once at creation time. Prompt adapted for creative context:

```
On the scale of 1 to 10, where 1 is purely routine
(e.g., refilling coffee, opening a file) and 10 is a
breakthrough creative moment (e.g., discovering a unifying
visual motif, a lore revelation that recontextualizes the
entire world), rate the creative significance of:

"{memory_description}"

Rating:
```

**Model**: Haiku (cheap, fast — this runs for every observation)

### Relevance (cosine similarity of embeddings)

```python
query_embedding = embed(query_text)       # text-embedding-3-small
memory_embedding = chromadb.get(memory.embedding_key)
relevance = cosine_similarity(query_embedding, memory_embedding)
```

Every memory's `description` is embedded at creation time and stored in ChromaDB. Retrieval embeds the current query and computes cosine similarity against all memories.

### Weight Rationale

The weights (recency=0.5, relevance=3.0, importance=2.0) come from the Stanford implementation's actual code (`retrieve.py`), where they apply multipliers of 0.5x, 3x, and 2x on top of the base alphas. This strongly favors **relevance** (what's topically related) and **importance** (what mattered), with recency as a tiebreaker.

For creative agents, this is correct: a breakthrough insight from two weeks ago should still surface when relevant, not be buried by recent trivia.

## Reflection

### Trigger

Each agent tracks an `importance_accumulator` (starts at 0). Every new observation adds its importance score. When the accumulator exceeds `REFLECTION_THRESHOLD = 150`, reflection fires and the accumulator resets.

With an average importance of ~5, this means reflection triggers roughly every 30 observations — about once per simulated day.

### Process

**Step 1 — Generate focal points** (what to reflect on):

```
Given these recent experiences:
{numbered list of last 100 observations/thoughts}

What are 3 salient high-level questions or themes
emerging from these experiences?
1)
```

**Step 2 — Retrieve evidence** per focal point:

Each focal point question goes through the standard retrieval function, pulling the top 20 most relevant memories.

**Step 3 — Synthesize insights**:

```
{numbered list of retrieved memories}

What 5 high-level creative insights or principles can you
infer from the above? Format each as:
insight (because of 1, 5, 3)
```

The parenthetical references link to evidence node IDs.

**Step 4 — Store reflections**:

Each insight becomes a new memory node with:
- `type = "reflection"`
- `depth = max(evidence_depths) + 1`
- `evidence_ids = [referenced node IDs]`
- Own importance score and embedding

**Model**: Sonnet (reflections require reasoning quality)

### Reflection Hierarchy

Reflections can reference other reflections, creating a hierarchy:

```
Depth 0: "Vera showed me her bone-tower concept art"
Depth 0: "Darius wants a dungeon in the Ashen Wastes"
Depth 1: "The Ashen Wastes are becoming central — Vera's organic
          aesthetic + Darius' dungeon → living structures" (from 0, 0)
Depth 0: "Creative Director said living towers need biology"
Depth 2: "The towers could grow from a dead titan's nervous system —
          this connects geology and mythology" (from 1, 0)
```

## Planning

### Daily Plan Generation (morning)

```
{agent_persona_summary}
{yesterday's summary — 5 most important reflections}
{current date, day of week, weather, any scheduled events}

What is {agent_name}'s plan for today? List 5-7 broad
activities with approximate times.
```

Output: `["Review lore notes (09:00)", "Work on Ashen Wastes geography (10:00)", ...]`

### Hourly Decomposition

Each broad activity is decomposed into 15-minute tasks:

```
{agent_name} plans to "{broad_activity}" from {start} to {end}.
Break this into specific 15-minute tasks:
```

### Reactive Re-Planning

When an agent perceives something unexpected (another agent initiating conversation, Creative Director feedback, a new artifact from a colleague), the planner evaluates:

```
{agent_name} is currently doing: "{current_task}"
They just noticed: "{new_observation}"
Should they: (a) continue current task, (b) briefly respond then continue,
(c) abandon current task to engage with this?
```

If (c), the remaining schedule is regenerated from the current time.

## Creative Memory Adaptations

### Artifact Memories

When an agent creates something (lore text, concept image, design doc), the artifact itself enters the memory stream:

```python
memory_stream.add(
    type="artifact",
    description="Created concept sketch: Ashen Wastes bone-towers, "
                "organic architecture, dark palette, 3 variations",
    metadata={
        "artifact_type": "concept_art",
        "artifact_path": "gallery/concepts/day03_bone_towers_v1.png",
        "style_tags": ["organic", "dark_fantasy", "architectural"],
        "project_context": "wbb/ashen_wastes",
        "fal_prompt": "the actual prompt used",
    }
)
```

### Cross-Agent Observation

When Agent A creates an artifact, all agents in the same room receive an observation:

```
"Vera just finished a concept sketch of bone-towers for the Ashen Wastes.
The style is organic and dark, with structures that look grown rather
than built."
```

This is how creative ideas spread organically — not through direct assignment, but through observation and memory.

### Shared Aesthetic Memory

Over time, agents accumulate overlapping memories about style decisions. Reflections on these shared experiences create an emergent **studio aesthetic** — not programmed, but grown from repeated reinforcement:

```
Day 1:  "Vera used a dark palette for the first concept"
Day 3:  "Kael described the world as 'drained of color'"
Day 5:  REFLECTION: "The team gravitates toward desaturated,
         dark palettes — this could be the visual signature"
Day 8:  "Darius suggested UI should match the world's palette"
Day 12: REFLECTION: "Desaturation is now a design principle,
         not just a preference — it extends from art to UI"
```

## Storage Architecture

```
data/
├── studio.db           # SQLite — all agent memories
├── embeddings/         # ChromaDB persistent storage
│   ├── kael/
│   ├── vera/
│   ├── darius/
│   ├── mira/
│   ├── tobi/
│   └── leo/
└── snapshots/          # Daily state dumps for resumability
    ├── day_001.json
    ├── day_002.json
    └── ...
```

## Performance Considerations

| Operation | Frequency | Model | Estimated Cost |
|-----------|-----------|-------|----------------|
| Importance scoring | ~30/agent/day | Haiku | ~$0.50/day total |
| Embedding | ~30/agent/day | text-embedding-3-small | ~$0.001/day |
| Retrieval (similarity search) | ~50/agent/day | ChromaDB (local) | Free |
| Reflection (3 focal points + synthesis) | ~1/agent/day | Sonnet | ~$3.00/day total |
| Planning (daily + hourly) | 1/agent/day | Haiku | ~$0.30/day total |
| Conversation (multi-turn) | ~3/agent/day | Sonnet | ~$9.00/day total |
| Creative output | ~2/agent/day | Sonnet | ~$4.00/day total |

**Estimated total: ~$17–25 per simulated day with 6 agents.**

With prompt caching (persona descriptions, system prompts): **~$12–18/day**.
