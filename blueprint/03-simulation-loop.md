# 03 — Simulation Loop

> How time passes in GenSoftworks. Scene-based, not tick-based.

## Design Philosophy

Real creative studios don't run on 15-minute intervals. Days have rhythm: a slow morning, a burst of conversation at lunch, a focused afternoon, an unexpected breakthrough at 4pm. Some days are quiet. Some days everything happens at once.

The simulation advances in **scenes** — narrative beats that the Game Master (main Claude Code session) selects based on what would be interesting, productive, or natural. This is closer to how Concordia (DeepMind) and tabletop RPGs work than to Stanford's clock-based ticks.

**Token efficiency**: 3–6 scenes per day vs. 36–96 ticks. Massive savings on a subscription.

## Scene Types

| Type | What Happens | Who's Involved | Typical Count/Day |
|------|-------------|----------------|-------------------|
| **ARRIVAL** | Agents arrive, declare daily plans | All agents | 1 (morning) |
| **ENCOUNTER** | Two agents cross paths, may talk | 2 agents | 1–3 |
| **WORK** | Agent produces an artifact or makes progress | 1 agent (+ observers) | 1–2 |
| **MEETING** | Scheduled or spontaneous group discussion | 2–7 agents | 0–1 |
| **EVENT** | External trigger changes the day | Varies | 0–1 |
| **REFLECTION** | Agent synthesizes accumulated experience | 1 agent | 0–1 |

A typical day: **3–6 scenes**. A busy day (Creative Director gives a brief, two encounters, an artifact, a meeting): **6–8 scenes**.

## Scene Flow (Pseudocode)

```
load_state("state/")

while simulation_running:
    # 1. GAME MASTER decides next scene
    scene = game_master.select_next_scene(world_state, agent_states)

    # 2. Identify participants
    agents = scene.get_involved_agents()

    # 3. Spawn agent subagents (parallel)
    responses = parallel_spawn(
        for agent in agents:
            agent.respond_to_scene(
                persona=agent.definition,
                memories=agent.recent_memories(limit=50),
                context=scene.description,
                bulletin=shared_bulletin
            )
    )

    # 4. Game Master reconciles
    if scene.has_interaction(responses):
        dialogue = game_master.weave_dialogue(responses)
    artifacts = game_master.collect_artifacts(responses)
    new_memories = game_master.extract_memories(responses)

    # 5. Update state
    for agent, memories in new_memories:
        append_to_memory_stream(agent, memories)
    update_agent_positions(responses)
    update_world_state(scene)
    save_to_logbook(scene, responses)

    # 6. Present to Creative Director
    display_scene_summary()

    # 7. Creative Director input
    match get_cd_input():
        case Continue:    pass
        case Intervene:   inject_event(cd_input)
        case SkipToNext:  advance_to_next_interesting_moment()
        case EndDay:      run_evening_reflections()
```

## Day Structure

```
ARRIVAL (morning)
  All 7 agents declare their plans.
  Game Master notes who wants to work near whom,
  who has unfinished business, who received feedback.
     │
     ▼
MORNING SCENES (1–3 scenes)
  Game Master picks the most interesting beats:
  - An encounter between agents with overlapping concerns
  - A work scene for an agent with a clear task
  - A follow-up on yesterday's cliffhanger
     │
     ▼
LUNCH (optional encounter scene)
  Kitchen proximity. Casual conversation.
  High chance of unexpected cross-pollination.
     │
     ▼
AFTERNOON SCENES (1–3 scenes)
  - Work artifacts most likely here (agents had time to think)
  - Meetings if scheduled
  - Creative Director intervention if desired
     │
     ▼
EVENING (wrap-up)
  - Reflection scenes for agents who crossed importance threshold
  - Brief summary of what happened today
  - Preview of tomorrow's energy (who's excited, who's stuck)

SPECIAL EVENTS
  Thursday 19:00: D&D Night (all agents, special interaction mode)
  GamesBomb week: Location changes, visitor NPCs, deadline pressure
```

## Scene Selection Logic

The Game Master decides the next scene based on:

1. **Unresolved threads** — Did Emre promise Vera feedback yesterday? Did the Creative Director post a brief that hasn't been addressed?
2. **Planned activities** — Agents declared plans in the ARRIVAL scene. Who has the most interesting task?
3. **Proximity and relationships** — Who works near whom? Who hasn't talked in a while? Who has tension?
4. **Importance accumulation** — Is any agent due for a reflection?
5. **Scheduled events** — D&D night, GamesBomb, deadlines
6. **Narrative pacing** — Don't stack three conversations in a row. Alternate between encounter, work, and meeting scenes.

The Game Master doesn't need a rigid algorithm for this — it reads the state and picks what feels right. This is an advantage of running on Claude: the "simulation engine" has narrative judgment.

## Creative Director Interactions

Between scenes, the Creative Director can:

- **Post feedback**: "Die Knochentürme brauchen mehr biologisches Detail" → enters bulletin board, high-importance observation for all agents
- **Call a meeting**: Force a MEETING scene with a topic and attendees
- **Give a brief**: New creative direction that reshapes agent plans
- **Ask an agent**: "Vera, was denkst du über den aktuellen Stil?" → triggers an out-of-scene response
- **Skip ahead**: "Run the rest of the day" → Game Master generates remaining scenes without pausing
- **End the day**: Jump to evening reflections and wrap up

## State Persistence

After each simulated day, the state is complete in `state/`:

```json
// state/world.json
{
    "day": 5,
    "day_of_week": "Wednesday",
    "scenes_today": 5,
    "scenes_total": 23,
    "scheduled_events": [
        {"day": 6, "event": "D&D Night", "time": "evening"}
    ],
    "active_briefs": [
        "Knochentürme: mehr biologisches Detail (CD, day 4)"
    ]
}
```

Resuming the simulation: `claude --continue` or `/scene` in a new session that reads the state directory.

## Speed Modes

| Mode | How It Works | Use Case |
|------|-------------|----------|
| **Interactive** | Game Master presents each scene, waits for CD input | Engaged play, giving feedback |
| **Autopilot** | Game Master runs a full day, presents summary at end | Overnight simulation, batch mode |
| **Focused** | CD picks an agent, only their scenes are expanded | Deep-dive on one character's day |

In **Autopilot**, the Creative Director types `/day` or `/day 3` and gets a narrative summary of what happened, with the option to rewind and intervene at any scene.
