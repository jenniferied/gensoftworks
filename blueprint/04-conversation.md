# 04 — Conversation System

> How agents talk to each other. Based on the dual-agent dialogue pattern from Park et al. 2023.

## Conversation Trigger

A conversation starts when:
1. Two agents are within proximity range AND
2. At least one agent's cognitive module decides to engage (see `03-simulation-loop.md`)

The deciding agent becomes the **initiator**. The other is the **respondent**.

## Conversation Flow

```
1. Initiator retrieves relevant memories about the respondent + current topic
2. Initiator generates opening line
3. Respondent retrieves relevant memories, generates response
4. Loop: each turn, both agents retrieve + respond
5. Either agent can signal end: "[END CONVERSATION]"
6. Max turns: 8 (configurable, prevents runaway dialogues)
7. Both agents store the full conversation in their memory streams
```

## Prompt Structure (per turn)

```
You are {agent_name}. {persona_summary}

You are having a conversation with {other_agent_name} in the {room_name}.
You are currently working on: {current_task}

Your relevant memories:
{top_10_retrieved_memories}

Conversation so far:
{conversation_history}

What do you say next? Stay in character. If you feel the conversation
has reached a natural end, include [END CONVERSATION] after your line.

{agent_name}:
```

**Model**: Sonnet (conversations need personality and coherence)

## Conversation Types

### Casual (water cooler, kitchen)
Low stakes. Agents share what they're working on, complain about deadlines, reference D&D, mention games they've been playing. These build relationship memories.

### Work-Related (at desks, nearby workstations)
One agent notices the other's work and comments. "That texture reminds me of..." or "Have you considered how this affects the quest structure?"

### Meetings (conference room, scheduled)
All agents in the meeting room. Turn-based discussion with an agenda topic. More structured: one agent presents, others react.

### D&D Night (special mode)
Agents switch to their D&D characters. Conversations are in-character. This is pure relationship building — no direct work output, but the shared experience creates strong memory bonds.

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
