# Simulation Tag starten

Lies `.claude/CLAUDE.md` und `simulation-2/briefing.md`. Lies `simulation-2/state/world.json` für den aktuellen Tag.

Spiele den nächsten Simulationstag — alle 6 Szenen nacheinander (BRIEFING → WORK → MEETING → PAUSE → WORK → REVIEW). Donnerstag: Szene 6 = D&D.

## CD-Feedback

> [Hier dein Feedback einfügen — was hat gut funktioniert, was soll sich ändern, inhaltliche Entscheidungen, Korrekturen, Prioritäten für heute]

## Regeln

- Lies die Memory-Dateien der Agenten vor jeder Szene
- Schreibe Memories nach jeder Szene (Arbeit UND Zwischenmenschliches)
- Agents mit `model: "sonnet"` spawnen
- Deutsche Umlaute in jedem Agent-Prompt verlangen
- Traces pro Agent: `0-prompt.md`, `1-reasoning.md`, `2-output.md`
- Nach Szene 6: `logbook/dayDD.json` schreiben (1 File pro Tag, Schema: `schemas/day-index.json`)
- Nach Szene 6: `world.json` updaten (Tag +1, Szene 0)
- Nach Szene 6: `python3 scripts/validate-sim.py --sim-dir simulation-2` — Fehler fixen vor Weiterarbeit
