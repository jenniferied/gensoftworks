# Game Master — Simulationsregeln

Dieses Dokument beschreibt, wie die Simulation funktioniert. Der GM (Opus 4.6) liest es **aktiv** vor jedem Tag.

## Architektur

Basiert auf Park et al. (2023, Generative Agents — Smallville) für Memory-Streams und szenenbasierte Steuerung, und Qian et al. (2024, ChatDev) für phasenbasierte Aufgabenzerlegung.

- **GM** = Hauptsession (Opus 4.6). Orchestriert Szenen, spawnt Agenten, schreibt Logbuch.
- **7 Agenten** = Subagenten (Sonnet 4.6, `model: "sonnet"`). Werden pro Szene via Task-Tool gespawnt. Jeder Agent hat eine Rollendefinition in `.claude/agents/{name}.md` und ein Persönlichkeitsprofil in `roster/`.
- **CD** / **Creative Director** = Menschlicher Nutzer. Gibt Feedback, trifft kreative Entscheidungen beim Start jedes Tages.

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

| # | Zeit | Typ | Modus | Wer | Max Turns |
|---|------|-----|-------|-----|-----------|
| 1 | 09:00 | BRIEFING | sequenziell | alle 7 | 8 |
| 2 | 10:00 | WORK | parallel | alle 7 | — |
| 3 | 11:30 | MEETING | sequenziell | alle 7 | 8 |
| 4 | 12:30 | PAUSE | sequenziell | 2–3 (GM wählt) | 6 |
| 5 | 14:00 | WORK | parallel | alle 7 | — |
| 6 | 16:00 | REVIEW | sequenziell | 3–4 relevanteste (GM wählt) | 6 |

**Donnerstag**: Szene 6 = D&D (Emre als DM + 2 Spieler). Sequenziell, max 8 Turns. Ort: Bibliothek.

## Szenenausführung

### Gesprächsszenen — allgemeiner Ablauf

Für alle sequenziellen Szenen (BRIEFING, MEETING, PAUSE, REVIEW, D&D):

1. GM legt Teilnehmer + Reihenfolge fest
2. Pro Turn: Agent spawnen (`model: "sonnet"`) mit Szenenkontext + bisherigem Dialog
3. GM sammelt Output → hängt an Dialog an → spawnt nächsten Agenten
4. Maximal N Turns (siehe Tabelle), dann beendet der GM die Szene

### WORK

**Modus**: parallel | **Teilnehmer**: alle 7 | **Turn-Cap**: —

Alle 7 Agenten gleichzeitig spawnen (`model: "sonnet"`). Jeder Agent bekommt Szenenkontext + Aufgabe. Mo/Di: Recherche + Konzeption. Mi–Fr: Produktion.

### BRIEFING

**Modus**: sequenziell | **Teilnehmer**: alle 7 | **Turn-Cap**: 8

Finn eröffnet (CD-Feedback + Tagesziele). Alle reagieren reihum.

### MEETING

**Modus**: sequenziell | **Teilnehmer**: alle 7 | **Turn-Cap**: 8

Finn eröffnet. Alle berichten Fortschritt, stellen Fragen, stimmen sich ab.

### PAUSE

**Modus**: sequenziell | **Teilnehmer**: 2–3 (GM wählt) | **Turn-Cap**: 6

Smalltalk, Soziales, Persönliches — keine Deliverables.

### REVIEW

**Modus**: sequenziell | **Teilnehmer**: 3–4 relevanteste (GM wählt nach Tagesarbeit) | **Turn-Cap**: 6

Ergebnisse vorstellen, offene Fragen für den CD sammeln.

### D&D (Donnerstag, Szene 6)

**Modus**: sequenziell | **Teilnehmer**: 3 (Emre als DM + 2 Spieler) | **Turn-Cap**: 8

Emre leitet eine Pen-&-Paper-Session. Ort: Bibliothek.

## Agent-Prompts

Jeder Agent liest seine eigene Definition (`.claude/agents/{name}.md`), die bereits
Umlaute-Regel, Briefing-Verweis und Memory-Anweisungen enthält.

Der GM ergänzt im Prompt nur den **Szenenkontext**:
- Tag, Szene, Uhrzeit, Ort
- Teilnehmer dieser Szene
- Aufgabe / Tagesphase (Recherche, Konzeption, Produktion)
- Bei Gesprächsszenen: bisheriger Dialog

## GM-Checkliste (pro Szene)

1. `state/world.json` lesen → Tag + Szenennummer bestimmen
2. Szene ausführen (parallel oder sequenziell gemäß Szenentyp)

## Tagesende (nach Szene 6)

3. `logbook/dayDD.json` schreiben gemäß `schemas/day-index.json`
4. `state/world.json` aktualisieren (Tag +1, Szene 0)
5. `python scripts/validate-sim.py --sim-dir simulation-2` — Fehler beheben vor Weiterarbeit
6. `python3 scripts/extract-transcripts.py --sim-dir simulation-2 --overwrite`
7. Outputs generieren:
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
