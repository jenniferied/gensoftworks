# 07 — Logging & Export System

> Every thought, every conversation, every creative decision — observable and exportable.

## Philosophy

The simulation is only as valuable as its observability. A Creative Director (or thesis author) needs to:
1. **Watch in real-time** — see what's happening as it happens
2. **Review afterward** — browse daily summaries, search for moments
3. **Export for publication** — PDF or HTML for thesis appendix or demo

## Log Levels

| Level | Content | Storage |
|-------|---------|---------|
| **tick** | Agent positions, current actions | `logbook/daily/dayXXX.jsonl` |
| **observation** | What each agent perceives | Memory DB (SQLite) |
| **conversation** | Full dialogue transcripts | `logbook/daily/dayXXX_conversations.jsonl` |
| **reflection** | Agent insights + evidence chain | Memory DB + logbook |
| **artifact** | Created works + metadata | `gallery/` + Memory DB |
| **decision** | Why an agent chose an action | `logbook/daily/dayXXX_decisions.jsonl` |
| **system** | LLM calls, costs, latency | `logbook/system.jsonl` |

## Daily Log Structure

```json
{
    "day": 5,
    "date_simulated": "2026-03-15",
    "date_real": "2026-02-20T14:32:00",
    "summary": "Kael and Vera's collaboration on the bone-towers deepened...",
    "highlights": [
        {"time": "10:30", "type": "conversation", "agents": ["kael", "vera"], "topic": "bone-tower biology"},
        {"time": "14:00", "type": "artifact", "agent": "vera", "artifact": "gallery/concepts/day05_towers_v2.png"},
        {"time": "17:00", "type": "reflection", "agent": "kael", "insight": "Towers as titan nervous system"}
    ],
    "stats": {
        "observations": 187,
        "conversations": 12,
        "reflections": 8,
        "artifacts_created": 3,
        "total_tokens": 2100000,
        "cost_usd": 18.50
    }
}
```

## Terminal Output (Rich)

During simulation, the terminal shows a live feed using the `rich` library:

```
╭─ GenSoftworks — Day 5, Wednesday 14:30 ─────────────────╮
│                                                            │
│  🔵 Kael    [Lore Corner]  Writing: Ashen Wastes geology  │
│  🟣 Vera    [Art Station]  Generating: bone-tower v2      │
│  🟢 Darius  [Conference]   Meeting with Mira              │
│  🟡 Mira    [Conference]   Meeting with Darius            │
│  🔴 Tobi    [Tech Corner]  Testing: UE5 lighting rig      │
│  🟠 Leo     [QA Station]   Browsing: r/crpg feedback      │
│                                                            │
│  14:15  Vera → Kael: "Die Knochen-Textur erinnert mich   │
│         an Gaudís Sagrada Família — organisch gewachsen"   │
│  14:20  Kael → Vera: "Genau! Was wenn die Türme           │
│         tatsächlich GEWACHSEN sind, nicht gebaut?"          │
│  14:25  💡 Kael REFLECTION: "Living architecture could     │
│         be the Ashen Wastes' defining characteristic"      │
│                                                            │
╰────────────────────────────── Tokens: 1.2M · Cost: $12.30 ╯
```

## PDF Export

Using Jinja2 templates + WeasyPrint:

### Daily Report Template
- Header: Day number, simulated date, weather/mood
- Timeline: Chronological events with agent avatars
- Conversations: Full transcripts in speech-bubble styling
- Reflections: Highlighted insight boxes with evidence chains
- Artifacts: Thumbnail images with creation context
- Stats: Token usage, cost, memory growth

### Week Summary Template
- Overview of all 5 workdays + D&D night
- Relationship changes (who talked to whom, how often)
- Creative progress (artifacts produced, style evolution)
- Key reflections and emerging themes
- Memory stream growth visualization

## HTML Export

Interactive web page using a Jinja2 template:
- Day picker (navigate between days)
- Agent filter (show only one agent's perspective)
- Searchable (find specific topics/keywords in conversations)
- Memory timeline (scrollable, color-coded by type)
- Embedded images for concept art artifacts

## Cost Tracking

Every LLM call is logged with:
```json
{
    "timestamp": "2026-02-20T14:32:15",
    "agent": "kael",
    "module": "reflect",
    "model": "claude-sonnet-4-6",
    "input_tokens": 3200,
    "output_tokens": 450,
    "cached_tokens": 2800,
    "cost_usd": 0.0089,
    "latency_ms": 1230
}
```

Running totals displayed in terminal footer and in export headers.
