# 07 — Logging & Export System (v2)

> Single source of truth. Every field in every scene, no exceptions.

## v2 Scene Schema

Each simulated day produces one log file: `logbook/day-XXX.jsonl`. Each line is one scene:

```json
{
  "scene": 3,
  "type": "ENCOUNTER",
  "time": "morning",
  "location": "kueche",
  "participants": ["emre", "vera"],
  "summary": "Narrative summary of what happens in this scene.",
  "dialogue": [
    {"who": "vera", "says": "Schau mal, die neue Version..."},
    {"who": "emre", "says": "Die sehen aus als wären sie gewachsen!"}
  ],
  "thoughts": [
    {"who": "emre", "thinks": "Das verbindet Geologie und Biologie."}
  ],
  "mood": {
    "emre": {"before": "nachdenklich", "after": "aufgeregt"},
    "vera": {"before": "neugierig", "after": "inspiriert"}
  },
  "feedback": [
    {"from": "vera", "to": "emre", "type": "honest", "text": "Die organische Idee ist stark, aber die Skalierung stimmt noch nicht."}
  ],
  "memories": [
    {"who": "emre", "id": "emre-043", "importance": 7, "text": "Vera findet die organische Turm-Idee stark, will aber Skalierung überarbeiten."}
  ],
  "artifacts": [],
  "cd_feedback": null,
  "key_moment": "Emres spontane Idee der organischen Türme öffnet eine neue Designrichtung."
}
```

### Rules

- **ALL fields in EVERY scene** — empty = `[]` or `null`, never omitted
- **No compound types** (`WORK+REFLECTION`) — one type per scene
- `dialogue` replaces both `narrative_transcript` and summary-only approaches
- `memories` includes `text` inline (no cross-referencing memory files)
- `feedback` required in ENCOUNTER and MEETING scenes (may be empty `[]` in others)
- `mood` keyed by participant agent ID, always has `before` and `after`

### Valid Scene Types

| Type | Description |
|------|-------------|
| `ARRIVAL` | Agents arrive, declare daily plans |
| `ENCOUNTER` | Two or more agents cross paths |
| `WORK` | Agent produces artifact or makes progress (max 3 participants) |
| `MEETING` | Scheduled or spontaneous group discussion |
| `REFLECTION` | Agent synthesizes accumulated experience |
| `EVENT` | External trigger changes the day |

### Field Reference

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `scene` | int | yes | Sequential scene number within the day |
| `type` | string | yes | One of the valid types above |
| `time` | string | yes | `morning`, `late-morning`, `afternoon`, `late-afternoon`, `evening` |
| `location` | string | yes | Room key (e.g. `kueche`, `gemeinschaftsraum`, `studio-weit`) |
| `participants` | string[] | yes | Agent IDs. Never includes `creative-director`. |
| `summary` | string | yes | Narrative summary in German |
| `dialogue` | object[] | yes | `{who, says}` — empty `[]` if no dialogue |
| `thoughts` | object[] | yes | `{who, thinks}` — empty `[]` if none |
| `mood` | object | yes | `{agent_id: {before, after}}` for each participant |
| `feedback` | object[] | yes | `{from, to, type, text}` — required in ENCOUNTER/MEETING |
| `memories` | object[] | yes | `{who, id, importance, text}` — text inline |
| `artifacts` | string[] | yes | File paths, or `[]` |
| `cd_feedback` | string\|null | yes | Creative Director feedback text, or `null` |
| `key_moment` | string\|null | yes | Highlight of the scene, or `null` |

## Terminal Display

Rendered from the same v2 fields. This is what the Game Master outputs in Claude Code:

```
━━━ Tag X, Szene Y: TYPE (Location) ━━━

[summary]

💬 VERA: "dialogue.says"
💬 EMRE: "dialogue.says"

💭 EMRE denkt: thoughts.thinks

🗣️ VERA → EMRE: feedback.text

📊 Stimmung: EMRE (before → after)
📝 Erinnerungen: id (★importance)
⭐ key_moment
```

## PDF Export

Via `scripts/export-logbook.py` → Pandoc + XeLaTeX. Reads the same v2 fields. Uses `templates/logbook-header.tex` for styling with tcolorbox environments for thoughts, reflections, artifacts, feedback, and directives.

## Backward Compatibility

`scripts/build-viewer-data.py` detects schema version:
- **v1** (simulation 1): `agent_details` field present → old rendering path
- **v2** (simulation 2+): `mood` field present → new rendering path

Use `--sim-dir simulation-1` to point scripts at the archived data.
