# Simulation Tag abschließen

Führe folgende Schritte aus:

1. Prüfe: Alle 6 Szenen gespielt, Memories für alle Teilnehmer geschrieben?
2. Schreibe `logbook/dayDD.json` (Tagesindex per `schemas/day-index.json`)
3. Update `state/world.json` (Tag inkrementieren, Szene auf 0)
4. Validierung: `python3 scripts/validate-sim.py --sim-dir simulation-2`
5. Transkripte extrahieren: `python3 scripts/extract-transcripts.py --sim-dir simulation-2 --overwrite`
