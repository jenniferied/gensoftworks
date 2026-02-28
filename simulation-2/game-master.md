# Game Master — Simulationsregeln

Dieses Dokument beschreibt, wie die Simulation funktioniert. Der GM (Opus 4.6) liest es **aktiv** vor jedem Tag.

## Architektur

Basiert auf Park et al. (2023, Generative Agents — Smallville) für Memory-Streams und szenenbasierte Steuerung, und Qian et al. (2024, ChatDev) für phasenbasierte Aufgabenzerlegung mit klaren Abbruchbedingungen.

- **GM** = Hauptsession (Opus 4.6). Orchestriert Szenen, spawnt Agenten, schreibt Logbuch.
- **7 Agenten** = Subagenten (Sonnet 4.6, `model: "sonnet"`). Werden pro Szene via Task-Tool gespawnt. Jeder Agent hat eine Rollendefinition in `.claude/agents/{name}.md` und ein Persönlichkeitsprofil in `roster/`.
- **CD** / **Creative Director** = Menschlicher Nutzer. Gibt Feedback, trifft kreative Entscheidungen.

Kein separater Server. Die Claude-Code-Session IST die Runtime. Alle Daten leben in Dateien.

## Pfade (relativ zu `simulation-2/`)

| Was | Pfad |
|-----|------|
| Weltzustand | `state/world.json` |
| Agent-Memory | `agents/{name}-memory.md` (finn, darius, emre, nami, vera, tobi, leo) |
| Agent-Roster | `roster/{vorname}-{nachname}.md` (Frontmatter `workspace` → Szenen-Ort) |
| Traces | `traces/dayDD-sceneS-…/` (JSONL automatisch, transcript.md per Script) |
| Logbuch | `logbook/dayDD.json` |
| Logbuch-Schema | `schemas/day-index.json` (**Repo-Root**, nicht in simulation-2/) |
| Briefing | `briefing.md` |

## Tagesablauf (6 Szenen)

| # | Zeit | Typ | Wer | Was |
|---|------|-----|-----|-----|
| 1 | 09:00 | BRIEFING | alle 7 | CD-Feedback + Tagesziele. Finn moderiert. |
| 2 | 10:00 | WORK | alle 7 | Parallel: Mo/Di Recherche+Konzeption, Mi–Fr Produktion |
| 3 | 11:30 | MEETING | alle 7 | Standup: Ergebnisse, Fragen, Abstimmung |
| 4 | 12:30 | PAUSE | 2–3 | Sozial/spontan — keine Deliverables |
| 5 | 14:00 | WORK | alle 7 | Parallel: Mo/Di Recherche+Konzeption, Mi–Fr Produktion |
| 6 | 16:00 | REVIEW | alle 7 | Ergebnisse vorstellen, offene Fragen für CD |

**Donnerstag**: Szene 6 = D&D (Emre ist DM + 2 Spieler). Ort: Bibliothek.

## Szenenausführung

### WORK-Szenen

Alle 7 Agenten **parallel** spawnen (`model: "sonnet"`). Jeder Agent bekommt:
- Eigene Rollendefinition (aus `.claude/agents/{name}.md`)
- Eigene Memory (`agents/{name}-memory.md`)
- Briefing-Kontext + Szenenkontext (Tag, Szenennummer, Aufgabe)
- Anweisung: Am Ende eigene Memory-Datei ergänzen

### Gesprächsszenen (BRIEFING, MEETING, REVIEW, PAUSE, DND)

**Sequenzielle** Subagenten-Turns — jeder Sprecher ist ein separater Sonnet-Task.

1. GM legt Teilnehmer + Reihenfolge fest
2. Pro Turn: Agent spawnen mit Szenenkontext + eigener Memory + **gesamtem bisherigen Dialog**
3. Agent spricht + ergänzt eigene Memory-Datei
4. GM sammelt Output → hängt an Dialog an → spawnt nächsten Agenten
5. Wiederholen bis Gespräch natürlich endet

Umfang:
- BRIEFING/MEETING/REVIEW: Finn eröffnet, 3–5 Agenten reagieren
- PAUSE: 2–3 Agenten, 5–8 Turns gesamt
- DND: 3 Agenten (Emre als DM + 2 Spieler), 6–10 Turns

## Agent-Prompts — Pflichtbestandteile

Jeder Agent-Prompt, den der GM schreibt, MUSS enthalten:
1. "Schreibe echte deutsche Umlaute (ä, ö, ü, ß), NICHT ae, oe, ue, ss."
2. Verweis auf Briefing-Datei und eigene Memory-Datei (exakte Pfade)
3. Szenenkontext: Tag, Szene, Uhrzeit, Ort, Teilnehmer, Aufgabe
4. Anweisung: "Ergänze am Ende deine Memory-Datei mit einer kurzen Erinnerung an diese Szene."

## GM-Checkliste (pro Szene)

1. `state/world.json` lesen → Tag + Szenennummer bestimmen
2. `agents/{name}-memory.md` für jeden Teilnehmer lesen
3. Szene ausführen (parallel oder sequenziell) — jeder Agent ergänzt **selbst** seine Memory-Datei

## Tagesende (nach Szene 6)

4. `logbook/dayDD.json` schreiben gemäß `schemas/day-index.json`
5. `state/world.json` aktualisieren (Tag +1, Szene 0)
6. `python scripts/validate-sim.py --sim-dir simulation-2` — Fehler beheben vor Weiterarbeit
7. `python3 scripts/extract-transcripts.py --sim-dir simulation-2 --overwrite`
8. Outputs generieren:
   - **Immer**: `scripts/export-logbook.py --sim-dir simulation-2`, `scripts/build-viewer-data.py --sim-dir simulation-2`
   - **Wenn GDD/WBB existieren**: `scripts/export-gdd.py --sim-dir simulation-2`, `scripts/export-wbb.py --sim-dir simulation-2`

## Traces

Traces werden **automatisch** von Claude Code als JSONL geloggt. Nach Tagesende extrahiert `scripts/extract-transcripts.py` daraus lesbare `transcript.md`-Dateien. Agenten schreiben **keine** manuellen Trace-Dateien.

| Szenentyp | Verzeichnisname | Beispiel |
|-----------|----------------|----------|
| WORK | `dayDD-sceneS-name/` | `day01-scene2-emre/` |
| Gesprächs-Turn | `dayDD-sceneS-tT-name/` | `day06-scene4-t1-vera/` |

## Logbuch-Format (v5)

Eine Datei pro Tag: `logbook/dayDD.json` gemäß `schemas/day-index.json`. Nur Metadaten + Zusammenfassungen — **kein Dialog** (lebt in Transkripten).

- `weekday`: deutsch, großgeschrieben (Montag, Dienstag, …)
- `artifacts` (NICHT `artifacts_produced`)
- `location`: aus Roster-Frontmatter Feld `workspace` (z.B. "Küche", "Bibliothek")

## Concept Art (Vera)

Vera generiert Bilder über fal.ai in WORK-Szenen. Stilregeln, Modelle und Budget in `.claude/agents/vera-conceptartist.md`. CD-freigegebene Bilder → sofort nach `pinwall/favorites/`.
