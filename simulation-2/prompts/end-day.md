# Simulation Tag abschließen

Führe folgende Schritte aus:

1. Prüfe: Alle 6 Logbook-Einträge geschrieben? (`logbook/dayDD-scene1.json` bis `scene6.json`)
2. Schreibe `logbook/dayDD-summary.json` (Tageszusammenfassung)
3. Update `state/world.json` (Tag inkrementieren, Szene auf 0)
4. Validierung: `python3 scripts/validate-sim.py --sim-dir simulation-2`
5. Transkripte extrahieren (Agent + GM): `python3 scripts/extract-transcripts.py --sim-dir simulation-2 --overwrite`
6. Viewer aktualisieren: `python3 scripts/build-viewer-data.py --sim-dir simulation-2`
