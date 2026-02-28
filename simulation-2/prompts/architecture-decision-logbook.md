# Architecture Decision: Logbook vs. Transcripts

## Status Quo

Der GM schreibt nach jeder Szene ein `logbook/dayDD-sceneS.json` mit:
- `scene`, `type`, `time`, `location`, `participants` (Metadaten)
- `dialogue` (1:1 kopiert aus Agent-Output)
- `summary` (GM-Zusammenfassung)
- `artifacts` (was produziert wurde)
- `cd_feedback` (CD-Kommentar)

## Problem

Seit dem Transkript-System ist das Logbook zu 90% redundant:
- Dialogue → steht 1:1 im Agent-Transkript
- Metadaten → stehen im GM-Prompt an den Agent
- Artifacts → erkennbar an Write-Calls im Transkript
- CD-Feedback → steht im Start-Prompt

Einzige GM-Eigenleistung: `summary` (2-3 Sätze).

## Option A: Logbook komplett raus

**Pro:**
- GM-Overhead massiv reduziert (keine Dialogue-Kopiererei, kein JSON-Schema)
- Keine Fehlerquelle (GM kürzt/verfälscht Dialogue nicht mehr)
- Transkripte = einzige Quelle der Wahrheit
- Simulation läuft schneller (weniger Tool-Calls)

**Contra:**
- Phaser Viewer braucht strukturierte Daten (Scene-Typ, Dialogue-Array)
- PDF Export braucht strukturierte Daten
- Müsste post-hoc Parsing-Script schreiben (Transkript → strukturierte Daten)
- Summary geht verloren (oder muss woanders hin)

## Option B: Minimales Index-File (empfohlen)

Der GM schreibt nur eine `logbook/dayDD.json` pro TAG (nicht pro Szene):

```json
{
  "day": 1,
  "weekday": "Montag",
  "phase": "Recherche & Konzeption",
  "scenes": [
    {"scene": 1, "type": "BRIEFING", "time": "09:00", "participants": ["all"]},
    {"scene": 2, "type": "WORK", "time": "10:00", "participants": ["darius", "emre", ...]},
    ...
  ],
  "summary": "Tag 1 stand im Zeichen der Recherche...",
  "cd_feedback": "Mehr Futurismus, weniger heruntergekommen.",
  "artifacts": ["01-spieluebersicht-v1.md", "01-mythos-v1.md"]
}
```

**Pro:**
- GM schreibt 1 File pro Tag statt 6
- Kein Dialogue-Kopieren mehr (lebt in Transkripten)
- Viewer bekommt Scene-Index für Navigation
- Summary bleibt als GM-Eigenleistung erhalten
- Deutlich weniger Overhead

**Contra:**
- Viewer/PDF müssen Dialogue aus Transkripten ziehen (braucht Anpassung)
- Mehr Logik in build-viewer-data.py / export-logbook.py

## Option C: Logbook bleibt, aber ohne Dialogue

Wie heute, aber `dialogue: []` für alle Szenen. Dialogue kommt aus Transkripten.

**Pro:** Minimale Änderung an bestehenden Scripts
**Contra:** Immer noch 6 JSONs pro Tag, immer noch Overhead
