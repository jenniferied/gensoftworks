# 03 — Simulation Loop

> How time passes in GenSoftworks.

## Time Model

| Unit | Simulated Duration | Real Duration (1x speed) |
|------|-------------------|--------------------------|
| 1 tick | 15 minutes | ~2–5 seconds (LLM latency) |
| 1 hour | 4 ticks | ~10–20 seconds |
| 1 workday (09:00–18:00) | 36 ticks | ~2–3 minutes |
| 1 full day (06:00–22:00) | 64 ticks | ~3–5 minutes |
| 1 week (5 workdays + D&D night) | ~350 ticks | ~20–30 minutes |

The simulation speed is configurable: **observe** (real-time with visualization), **fast** (skip to next interesting event), or **overnight** (batch-run multiple days, review logs later).

## Main Loop (Pseudocode)

```
initialize_world(tiled_map)
initialize_agents(roster/)
load_or_create_memories(data/)

while simulation_running:
    clock.tick()

    # 1. WORLD UPDATE
    check_scheduled_events(clock.current_time)
    check_creative_director_input()

    # 2. AGENT LOOP (per agent, order randomized each tick)
    for agent in shuffle(agents):
        # Perceive
        nearby = world.get_nearby_entities(agent.position, radius=INTERACTION_RANGE)
        observations = agent.perceive(nearby, world.state)

        # Decide
        if agent.should_react_to(observations):
            agent.replan(observations)

        # Act
        action = agent.get_current_action()
        match action:
            case Move(target):
                world.move_agent(agent, target)
            case Work(task):
                output = agent.do_creative_work(task)
                if output:
                    broadcast_artifact(output, agent.room)
            case Talk(other_agent):
                conversation = run_conversation(agent, other_agent)
                log_conversation(conversation)
            case Idle:
                pass

        # Memory maintenance
        if agent.importance_accumulator >= REFLECTION_THRESHOLD:
            agent.reflect()

    # 3. LOG & RENDER
    logbook.record_tick(clock, agents, world)
    if visualization_enabled:
        renderer.draw_frame(world, agents)
```

## Day Structure

```
06:00  Agents "wake up" — load yesterday's summary, generate daily plan
06:30  Morning routine (background, not simulated in detail)
09:00  Arrive at studio — walk to assigned workspace
09:00–12:00  Morning work block
       Interruptions: proximity encounters, Creative Director input
12:00–13:00  Lunch break — high-probability casual encounters in kitchen
13:00–14:00  Potential scheduled meeting (if any)
14:00–17:30  Afternoon work block
17:30–18:00  End of day — agents reflect, save state
18:00  Agents "leave" (simulation can continue for evening events)

THURSDAY 19:00–22:00  D&D Night (all agents, special interaction mode)
SPECIAL EVENTS  GamesBomb (multi-day, changes location and interaction patterns)
```

## Event Types

### Proximity Events
Triggered when two agents are within `INTERACTION_RANGE` (2 tiles). The initiating agent's cognitive module decides whether to engage:

```
{agent_name} notices {other_agent_name} nearby.
{agent_name}'s current task: "{current_task}"
{relevant_memories_about_other_agent}

Does {agent_name} want to start a conversation? Consider:
- Is the current task interruptible?
- Do they have something relevant to discuss?
- What's their relationship like?

Decision (yes/no) and brief reason:
```

### Scheduled Events
Defined in `config/schedule.yaml`:
- Daily standup (optional, togglable)
- Weekly D&D night (Thursday 19:00)
- Monthly GamesBomb preparation
- Milestone deadlines

### External Events
Injected by the Creative Director or by the simulation engine:
- Feedback posts ("The bone-tower concept needs darker colors")
- New reference material ("New artbook added to library")
- Deadline changes ("Publisher demo in 2 weeks")
- Visitor events ("An industry contact wants to see the prototype")

## State Persistence

After each simulated day, a snapshot is saved:

```json
{
    "day": 5,
    "date": "2026-03-15",
    "agents": {
        "kael": {
            "position": [12, 8],
            "current_plan": [...],
            "importance_accumulator": 87,
            "memory_count": 142
        }
    },
    "world_state": {
        "active_artifacts": [...],
        "bulletin_board": [...]
    }
}
```

Resuming loads the snapshot + full memory databases. The simulation can be rewound to any saved day.
