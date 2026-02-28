# Day 02, Scene 2 — Output (Tobi)

## Ergebnis

**GDD Kapitel 06 — Technische Spezifikation & Produktion, v1** fertiggestellt.

Datei: `simulation-2/gallery/gdd/06-technik-produktion-v1.md`

### Inhalt (12 Abschnitte)

1. **Engine & Zielplattformen** — UE5, PC primär, PS5/XSX sekundär, Mindestanforderungen
2. **Rendering-Pipeline** — Nanite (Asset-Eignungstabelle), Lumen (Hybrid-Lighting nach Vertikalebene), Biolumineszenz (3-Klassen-System)
3. **Schwellenanker-System** — Vollständige MPC-Spec: 7 Parameter, 3 Distanz-Zonen, Material-Graph-Integration, Schattenfieber-Interaktionsformel
4. **Schattenfieber VFX-Pipeline** — 3 Stufen mit Float-Bereichen, Post-Process-Parameter-Tabelle, Accessibility-Optionen (3 Stufen)
5. **Kamerasystem** — Third/First-Person-Blend, Nervensystem-Arm-Mesh, FOV-Optionen
6. **World Partition & Vertikale Stadt** — 4 Data Layers, Streaming-Regeln, Occlusion-Strategie
7. **Audio-Pipeline** — Grundriss/Platzhalter, vertikale Akustik
8. **Release-Modell & Monetarisierung** — Premium, Streamer-Alpha, Beta, 2 DLCs, Preispunkte
9. **Team-Sizing** — 7 Kern + Skalierung auf 20-30 für Produktion, Outsourcing-Bereiche
10. **Produktions-Roadmap** — 6 Phasen, 30-42 Monate Gesamtdauer, kritischer Pfad
11. **Risikomatrix** — 9 identifizierte Risiken mit Wahrscheinlichkeit, Impact und Mitigation
12. **Pipeline-Standards** — ACES-Farbraum, Asset-Naming, Dokumentationsprinzip

### Kernentscheidung: Schwellenanker-MPC

Die MPC-Spec ist das technisch Neue. Sieben Parameter in einer Material Parameter Collection steuern die gesamte visuelle Transformation um den Schwellenanker. Das System ist additiv mit dem Schattenfieber kompatibel — beide lesen aus derselben Collection, der kombinierte Effekt verstärkt sich bei infizierten Spielern.

### Offene Punkte

- Audio-Pipeline ist nur ein Grundriss, muss mit einem Sound-Lead ausgearbeitet werden
- Vertikalstruktur als Level-Design-Constraint muss mit Vera/Darius formalisiert werden
- Rendering-Prototyp (Testszene) als nächster praktischer Schritt
- Budget-Zahlen liegen bei Finn
