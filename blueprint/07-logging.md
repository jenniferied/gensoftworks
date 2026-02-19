# 07 — Logging & Export System

> Every scene, every conversation, every creative decision — observable and exportable.

## Philosophy

The simulation is only as valuable as its observability. A Creative Director (or thesis author) needs to:
1. **Watch interactively** — see scene results as they happen
2. **Review afterward** — browse daily summaries, search for moments
3. **Export for publication** — PDF or HTML for thesis appendix or demo

## Log Structure

Each simulated day produces one log file: `logbook/day-XXX.jsonl`

Each line is one scene:

```json
{
    "scene_number": 3,
    "scene_type": "ENCOUNTER",
    "time_of_day": "morning",
    "location": "kitchen",
    "participants": ["emre", "vera"],
    "summary": "Emre und Vera treffen sich in der Küche. Vera zeigt ihr neues Konzeptbild der Knochentürme. Emre schlägt vor, die Türme könnten aus einem toten Titanen gewachsen sein.",
    "dialogue": [
        {"agent": "vera", "text": "Schau mal, die neue Version der Türme..."},
        {"agent": "emre", "text": "Die sehen aus als wären sie gewachsen! Was wenn sie tatsächlich organisch sind?"},
        {"agent": "vera", "text": "Du meinst... lebendig? Das würde die Textur erklären."}
    ],
    "thoughts": [
        {"agent": "emre", "thought": "Das verbindet Geologie und Biologie — genau was der Creative Director wollte."}
    ],
    "artifacts_created": [],
    "memories_added": [
        {"agent": "emre", "id": "emre-043", "importance": 7},
        {"agent": "vera", "id": "vera-029", "importance": 6}
    ],
    "cd_feedback": null
}
```

## Terminal Output

During interactive mode, each scene is presented in the Claude Code terminal as a narrative summary:

```
━━━ Day 5, Wednesday — Scene 3: ENCOUNTER (Kitchen) ━━━

Emre und Vera treffen sich in der Küche.

VERA: "Schau mal, die neue Version der Türme..."
EMRE: "Die sehen aus als wären sie gewachsen! Was wenn sie
       tatsächlich organisch sind?"
VERA: "Du meinst... lebendig? Das würde die Textur erklären."

💭 Emre denkt: Das verbindet Geologie und Biologie.
📝 Neue Erinnerungen: emre-043 (★7), vera-029 (★6)

[Continue] [Intervene] [Skip to next day]
```

This is plain text output from Claude Code — no Rich library needed. The formatting IS the presentation.

## Daily Summary

At the end of each simulated day (or when requested), the Game Master produces a summary:

```json
{
    "day": 5,
    "day_of_week": "Wednesday",
    "scenes": 5,
    "summary": "Ein produktiver Tag. Emres Idee der organischen Türme hat Vera inspiriert. Darius und Nami haben den ersten Dungeon-Entwurf besprochen. Leo hat Community-Feedback zu ähnlichen Spielen gesammelt.",
    "highlights": [
        "Emre + Vera: Knochentürme könnten organisch sein (scene 3)",
        "Darius: Erster Dungeon-Entwurf für die Aschen-Einöden (scene 4)",
        "Leo: r/crpg-Analyse zu Dark Fantasy CRPGs (scene 5)"
    ],
    "artifacts_created": [
        "gallery/lore/day-005_organic-towers.md",
        "gallery/designs/day-005_dungeon-draft.md"
    ],
    "reflections": [
        {"agent": "emre", "insight": "Organische Architektur als Leitprinzip der Aschen-Einöden"}
    ],
    "open_threads": [
        "Vera will die organischen Türme als Konzeptbild umsetzen",
        "Creative Director Brief zu Biologie steht noch aus"
    ]
}
```

## PDF Export

Using Jinja2 templates + WeasyPrint:

### Daily Report Template
- Header: Day number, simulated date, day of week
- Scene timeline with dialogue and thought bubbles
- Artifact thumbnails with creation context
- Reflections highlighted as insight boxes
- Open threads for next day

### Week Summary Template
- Overview of all 5 workdays + special events
- Relationship graph (who talked to whom, how often)
- Creative progress (artifacts produced, themes emerging)
- Key reflections and emerging studio aesthetic

## HTML Export

Interactive web page (Jinja2 template):
- Day picker (navigate between days)
- Agent filter (show only one agent's perspective)
- Searchable (find topics in conversations)
- Memory timeline (scrollable, color-coded by type)
- Embedded images for concept art artifacts
