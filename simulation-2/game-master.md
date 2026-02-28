> **STOP — Lies das zuerst.** GM und Agenten schreiben NIEMALS Dateien in `traces/`. Keine output.md, prompt.md, reasoning.md, keine Ordner. Der `traces/`-Ordner wird ausschließlich von Scripts nach Tagesende befüllt.

# Game Master — Simulationsregeln

Dieses Dokument beschreibt, wie die Simulation funktioniert. Der GM (Opus 4.6) liest es **aktiv** vor jedem Tag.

## Architektur

Basiert auf Park et al. (2023, Generative Agents — Smallville) für Memory-Streams und szenenbasierte Steuerung, und Qian et al. (2024, ChatDev) für phasenbasierte Aufgabenzerlegung.

- **GM** = Hauptsession (Opus 4.6). Orchestriert Szenen, spawnt Agenten, schreibt Logbuch.
- **7 Agenten** = Subagenten. Werden pro Szene via Task-Tool gespawnt. Jeder Agent hat eine Rollendefinition in `.claude/agents/{name}.md` und ein Persönlichkeitsprofil in `roster/`.
  Emre: model `"opus"` | Darius, Nami, Vera, Tobi: model `"sonnet"` | Finn, Leo: model `"haiku"`
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

## Tagesablauf (5 Szenen)

| # | Zeit  | Typ      | Modus        | Wer                    | Max Turns |
|---|-------|----------|--------------|------------------------|-----------|
| 1 | 09:00 | BRIEFING | sequenziell  | alle 7                 | 8         |
| 2 | 10:00 | WORK     | parallel     | alle 7                 | —         |
| 3 | 13:00 | MEETING  | sequenziell  | alle 7                 | 8         |
| 4 | 14:00 | PAUSE    | sequenziell  | 2–3 (GM wählt)        | 6         |
| 5 | 15:00 | REVIEW   | sequenziell  | 3–4 relevanteste       | 6         |

**Donnerstag**: Szene 5 = D&D (Emre als DM + 2 Spieler). Sequenziell, max 8 Turns. Ort: Bibliothek.

## Szenenausführung

### Erlaubte Agenten-Typen

Der GM spawnt Agenten **ausschließlich** mit diesen 7 typisierten `subagent_type`-Werten:

- `finn-producer`
- `darius-gamedesigner`
- `emre-worldbuilder`
- `nami-narrativedesigner`
- `vera-conceptartist`
- `tobi-techart`
- `leo-qa`

> **NIEMALS `general-purpose` oder andere Agenten-Typen verwenden.** Jede Szene nutzt ausschließlich die 7 typisierten Agenten.

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

### D&D (Donnerstag, Szene 5)

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
3. `state/world.json` aktualisieren (Szenennummer hochzählen)

**GM schreibt NICHT in**: `agents/*-memory.md` — nur Agenten selbst.

## Tagesende (nach Szene 5)

4. `logbook/dayDD.json` schreiben gemäß `schemas/day-index.json` — NUR Metadaten + Summaries, KEIN Dialog
5. `state/world.json` aktualisieren (Tag +1, Szene 0)
6. Scripts ausführen:
   - `python scripts/validate-sim.py --sim-dir simulation-2` — Fehler beheben vor Weiterarbeit
   - `python3 scripts/extract-transcripts.py --sim-dir simulation-2 --overwrite`
   - **Immer**: `scripts/export-logbook.py --sim-dir simulation-2`, `scripts/build-viewer-data.py --sim-dir simulation-2`
   - **Wenn GDD/WBB existieren**: `scripts/export-gdd.py --sim-dir simulation-2`, `scripts/export-wbb.py --sim-dir simulation-2`
7. Git: Alles commiten und pushen
   ```
   git add -A simulation-2/ && git commit -m "sim2/day{DD}: tag abgeschlossen" && git push
   ```

## Traces

Traces werden **automatisch** von Claude Code als JSONL geloggt. Nach Tagesende extrahiert `scripts/extract-transcripts.py` daraus lesbare `transcript.md`-Dateien. Agenten schreiben **keine** manuellen Trace-Dateien.

> **GM und Agenten schreiben NIEMALS in `traces/`.** Keine output.md, keine prompt.md, keine reasoning.md, keine manuellen Dateien. Der `traces/`-Ordner wird ausschließlich vom Script `extract-transcripts.py` nach Tagesende befüllt.

| Szenentyp | Verzeichnisname | Beispiel |
|-----------|----------------|----------|
| WORK | `dayDD-sceneS-name/` | `day01-scene2-emre/` |
| Gesprächs-Turn | `dayDD-sceneS-tT-name/` | `day06-scene4-t1-vera/` |

## Fehlerbehandlung

Wenn ein Agent keinen verwertbaren Output liefert, eine Szene scheitert, oder etwas Unerwartetes passiert:

1. GM erfindet NICHTS und improvisiert NICHT
2. GM STOPPT die Simulation
3. GM informiert den Creative Director über das Problem
4. GM wartet auf Anweisungen des Creative Directors bevor er fortfährt

## Logbuch-Format (v5)

Eine Datei pro Tag: `logbook/dayDD.json` gemäß `schemas/day-index.json`. Nur Metadaten + Zusammenfassungen — **kein Dialog** (lebt in Transkripten).

- `weekday`: deutsch, großgeschrieben (Montag, Dienstag, …)
- `artifacts` (NICHT `artifacts_produced`)
- `location`: aus Roster-Frontmatter Feld `workspace` (z.B. "Küche", "Bibliothek")

## Artefakte & Produktionszeitplan

Agenten erstellen versionierte Markdown-Dateien in WORK-Szenen:
- GDD: `gallery/gdd/KK-titel-vN.md` (z.B. `01-spieluebersicht-v1.md`)
- WBB: `gallery/wbb/KK-titel-vN.md` (z.B. `01-mythos-v1.md`)
Neue Version → N erhöhen. Alte Versionen bleiben.

PDF-Dokumente sind Gesamt-Snapshots (eigene Nummerierung):

| Tag | Phase | Markdown-Outputs | PDF-Export |
|-----|-------|------------------|------------|
| Mo  | Recherche | Notizen, Konzepte | — |
| Di  | Recherche + erste Produktion | Erste Kapitel-MDs (v1) | — |
| Mi  | Produktion | Weitere Kapitel, Überarbeitungen | GDD v0.1 + WBB v0.1 |
| Do  | Produktion | Alle Sektionen in Arbeit | GDD v0.2 + WBB v0.2 |
| Fr  | Finalisierung | Alle Sektionen vorhanden | GDD v0.3 + WBB v0.3 |

## Concept Art (Vera)

Vera generiert Bilder über fal.ai in WORK-Szenen. Stilregeln, Modelle und Budget in `.claude/agents/vera-conceptartist.md`. CD-freigegebene Bilder → sofort nach `pinwall/favorites/`.

> **ERINNERUNG:** GM und Agenten schreiben NIEMALS in `traces/`. Keine Dateien, keine Ordner, nichts.
