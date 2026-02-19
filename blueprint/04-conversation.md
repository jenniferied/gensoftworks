# 04 — Conversation System

> How agents talk to each other. Conversations happen inside ENCOUNTER and MEETING scenes.

## Conversation Trigger

Conversations happen when the Game Master selects an **ENCOUNTER** or **MEETING** scene involving two or more agents. The Game Master decides who meets based on proximity, unresolved threads, and narrative pacing (see `03-simulation-loop.md`).

## Conversation Flow

Inside a scene, conversations are generated in one of two ways:

**Option A — Parallel then weave** (default for ENCOUNTER scenes):
1. Both agents are spawned as subagents in parallel
2. Each receives the scene context + their memories + the other agent's recent state
3. Each independently generates what they'd say/do
4. The Game Master weaves the outputs into a coherent dialogue (2–6 turns)

**Option B — Sequential exchange** (for important conversations):
1. Agent A is spawned, generates opening + first turn
2. Agent B is spawned with Agent A's opening, generates response
3. Repeat for 2–4 exchanges (Game Master decides when to end)
4. More token-intensive but produces richer back-and-forth

**Option A** is cheaper (2 subagent spawns + 1 reconciliation). **Option B** is better for pivotal moments. The Game Master picks based on scene importance.

## Scene Context (per agent)

```
You are {agent_name}. {persona_summary}

SCENE: You run into {other_agent_name} in the {room_name}.
You are currently working on: {current_task}

Your relevant memories:
{recent_memories_about_topic_and_person}

What do you say and do? Stay in character. Speak German.
Include your inner thoughts in [brackets].
```

## Conversation Types

### Casual (ENCOUNTER — kitchen, hallway)
Low stakes. Agents share what they're working on, complain about deadlines, reference D&D, mention games they've been playing. These build relationship memories. Use Option A.

### Work-Related (ENCOUNTER — at desks, nearby workstations)
One agent notices the other's work and comments. "That texture reminds me of..." or "Have you considered how this affects the quest structure?" Use Option A.

### Meetings (MEETING scene — conference room)
All agents (or a subset) in the meeting room. Topic-driven discussion. Use Option B for the core exchange, with the Game Master moderating turn order.

### D&D Night (EVENT scene — special mode)
Agents switch to their D&D characters. Conversations are in-character. This is pure relationship building — no direct work output, but the shared experience creates strong memory bonds. Use Option A with a lighter, playful Game Master tone.

## After Conversation

Both agents receive:
1. A **conversation memory** with the full exchange stored in metadata
2. The conversation summary as the `description` field
3. Updated relationship valence (positive/negative/neutral shift)

Other agents in the same room receive an **observation**:
```
"Kael and Vera were discussing bone-tower architecture at the kitchen.
They seemed excited about a new idea."
```

They don't hear the details — just that a conversation happened. This mimics real offices: you see colleagues talking but don't eavesdrop on content.

## Language

Agents speak **German** in simulation (matching the creative output language for WBB/GDD). The logbook can display original German or auto-translated English summaries.
