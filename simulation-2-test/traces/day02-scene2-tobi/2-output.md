# Output — Tobi Richter, Tag 2 Szene 2 (WORK)

## Ergebnis

GDD-06 Outline V0.1 erstellt und abgelegt unter `gallery/gdd/06-technik-produktion.md`.

## Struktur des Dokuments

1. **Engine & Rendering** — UE5, Nanite, Lumen, VSM, ACES-Farbpipeline, Post-Processing Stack
2. **Kamerasystem** — Spring Arm, vier Kontext-Modi (Exploration/Combat/Dialog/Inspect), Kollision, FP-Vorbereitung
3. **Combat-Architektur** — GAS als Basis, Kernkomponenten-Tabelle, Motion Matching, Scope-Steuerung (V1: Schwert + Bogen), Risiken
4. **Asset-Pipeline** — Modulares Kit, Standards (Texel Density, Naming), Houdini-Terrain, PCG-Vegetation, Asset-Quellen
5. **Schattenfieber-Tech** — Post-Processing Layer mit 5 Infektionsstufen, Welt-Effekte, Niagara-Partikel, Abhaengigkeiten
6. **Performance-Ziele** — Drei Hardware-Tiers, DLSS/FSR als Pflicht, konkrete Budgets (Draw Calls, Lichter, NPCs)
7. **Produktions-Pipeline** — Perforce + Git, UE5-Ordnerstruktur, Tool-Chain, Abstimmungsbedarf mit Finn
8. **Meilensteine** — Sechs Phasen (Pre-Production bis Release), kritischer Pfad, Zeitplan-Risiken

## Wesentliche Entscheidungen und Positionen

- **Scope-Steuerung Combat:** V1 nur Schwert + Bogen. Armbrust und Schild sind V2. Lieber zwei Waffentypen mit gutem Gefuehl als vier matschige.
- **Fraktions-Differenzierung ueber Materialien:** Gleiche Basis-Geometrie, unterschiedliche Material-Instanzen. Spart enorm Produktionszeit.
- **DLSS/FSR ist Pflicht, kein Nice-to-have.** Bei Lumen-Rendering auf Minimum-Hardware (GTX 1070) geht es ohne Upscaling nicht.
- **Perforce statt Git fuer Engine-Assets.** Git LFS ist fuer UE5-Projekte nicht sinnvoll. Binaere Assets gehoeren nach Perforce.
- **Schattenfieber als Querschnittssystem:** Eigener Abschnitt, weil es Rendering, VFX, Gameplay und Narrative gleichzeitig betrifft. Abstimmungsmeeting priorisieren.
- **Meilensteine sind vorgeschlagen, nicht beschlossen.** Finn muss die Produktionsseite dazulegen. Ich liefere die technische Einschaetzung, er den realistischen Zeitplan.

## Was als Naechstes passiert

- Abstimmung mit Finn zu Meilensteinen und Produktions-Pipeline (Standup oder nachmittags)
- Abstimmung mit Vera zu Asset-Standards (diese Woche)
- Schattenfieber-Meeting mit Emre und Darius anstossen
- Ab Mittwoch: Outline > V1 ausbauen (Produktionsphase)

## Selbstkritik

Die Outline ist solide, aber sie hat Luecken:
- Audio-Pipeline fehlt fast komplett. Ist nicht mein Gebiet, muss aber ins GDD. Brauche jemanden, der das verantwortet.
- UI/UX-Tech ist nur am Rand erwaehnt (CommonUI). Braucht eigenen Abschnitt in V1.
- Netzwerk/Online-Features: Bewusst weggelassen (Singleplayer bestaetigt). Aber was ist mit Achievements, Cloud Saves, Anti-Cheat? Muss irgendwann geklaert werden.
- Die Meilenstein-Zeitplaene sind optimistisch. Insbesondere der Uebergang von Pre-Production zu Vertical Slice haengt am Gameplay-Programmer-Timing.
