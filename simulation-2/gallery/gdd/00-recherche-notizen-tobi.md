# Technische Recherche-Notizen — RELICS
**Autor**: Tobias Richter, Technical Artist
**Datum**: Tag 1, Montag, 10:00 Uhr
**Status**: Arbeitsdokument — nicht final

---

## 1. Rendering-Pipeline: Lumen + Nanite

**Nanite** ist für RELICS gesetzt. Die vertikale Stadt mit ihren Schichtungen aus poliertem Stein, Metall-Intarsien und Fachwerk-Strukturen braucht extreme Geometriedichte ohne manuelles LOD-Authoring. Risiko: Nanite hat bekannte Schwächen bei dünnen Geometrien (Ketten, Zaunstäbe, Pflanzen) — die müssen weiterhin als traditionelle Meshes mit handgestellten LODs gehandhabt werden. Knochen-Schnitzereien der Unterschicht und Zunftzeichen-Reliefs sind gute Nanite-Kandidaten.

**Lumen** für Global Illumination ist der richtige Ansatz, aber die vertikale Stadtstruktur stellt ein ernstes Problem: Lumen arbeitet mit Screen-Space-Fallbacks und Software-Raytracing in einem fixen Radius. Tiefe Kanäle, überhängende Arkaden, Slum-Bereiche unter Brücken — überall dort, wo der Himmel nicht sichtbar ist, degeneriert Lumen-GI. **Lösung**: Hardware-Raytracing aktivieren wo Budget es erlaubt, kombiniert mit manuell platzierten Lumen-Importance-Volumes für kritische Innenräume (Gildenhallen, Ordenskorridore). Für die Slum-Kanäle: statisches Baked Lighting als Fallback definieren.

**Fazit Rendering**: Machbar. Kein Experiment, sondern Handwerk. Die Kombination aus Lumen-Hardware-RT für obere Stadtebenen und Hybrid-Baking für untere Ebenen ist ein etabliertes Muster. Zeitaufwand für Setup-Phase: realistisch 3–4 Wochen für eine stabile Basis-Pipeline.

---

## 2. Biolumineszenz — Emissive in Lumen

Das Briefing setzt auf Biolumineszenz als Neon-Äquivalent: phosphoreszierende Mineralien, Alchemie-Leuchtstoffe. Das ist technisch der interessanteste Teil.

In UE5 funktioniert Emissive mit Lumen gut — Emissive-Flächen werden als Lichtquellen behandelt, wenn der Mesh als "Emissive Light Source" flagged ist. **Problem**: Bei vielen kleinen Emissive-Quellen (hunderte Pilze, Alchemie-Phiolen, Buntglasfenster) explodiert der Performance-Overhead. **Lösung**: Emissive-Quellen in drei Klassen einteilen:

- **Klasse A** (hero lights): Echte Lumen-Emitter. Wenige, sorgfältig platzierte Stücke pro Szene — die Bergkristall-Linsen der Oberschicht, die großen Alchemie-Lampen der Gilden.
- **Klasse B** (ambient glow): Emissive-Material ohne Lumen-Light-Source-Flag. Leuchten visuell, strahlen aber kein GI ab. Für Füllmaterial in Slum-Bereichen.
- **Klasse C** (VFX): Particle-basierte Biolumineszenz für organische Leuchtelemente (Pilze, Schimmel). Niagara-System, skalierbar über Qualitätsstufen.

**FFXIV-Referenz**: Die v2.0-Specs zeigen, dass Square Enix Materiallesbarkeit durch starke Kontrast-Hierarchien sicherte — helle, klar definierte Emissive-Stellen auf dunklen Basismaterialien. Das ist für RELICS direkt anwendbar: die Biolumineszenz muss lesbar sein, nicht überwältigend.

---

## 3. Schattenfieber — VFX-Stufen (Post-Processing)

Das Schattenfieber ist das einzige Übernatürliche im Spiel. Die visuelle Eskalation muss in der Pipeline klar definiert sein, damit Nami und Vera konsistent arbeiten können.

**Drei Stufen, Post-Process Volume gesteuert:**

**Stufe 1 — Frühinfektion (subtil):** Leichte Chromatic Aberration an Bildrändern (+/- 0.3 Pixel max). Gelegentliches Film Grain-Aufflackern. Farbtemperatur minimal kühler (Bloom-Tint Richtung Cyan). Der Spieler soll unsicher sein, ob er etwas sieht.

**Stufe 2 — Fortgeschritten (eindeutig):** Vignetierung verstärkt. Pulsierendes Depth of Field im Nahbereich (simuliert veränderte Wahrnehmung). Schatten-Bereiche des Bildes erhalten einen Indigo-Tint durch Color Grading Curve. Geometrie "atmet" leicht — vertex-animierte Umgebungsobjekte im sichtbaren Radius (±2cm Oszillation). Risiko: das kann Spieler mit Motion-Sickness-Empfindlichkeit treffen. Accessibility-Option muss her.

**Stufe 3 — Kritisch (Grenze zur anderen Seite):** Full-Screen-Shader-Overlay mit organischen Riss-Strukturen (inspiriert von den planes of existence beyond known reality aus dem Briefing). Welt-Geometrie zeigt temporäre "Lücken" — schwarze Flächen, durch die Dunkelheit scheint. Nervensystem-Visualisierung startet automatisch. Das ist der gefährlichste State — Spieler kann Fähigkeiten nutzen, aber die Wahrnehmung ist kompromittiert.

**Implementierung**: Alle drei Stufen als Parameter-Set in einem Blueprint-System. Smooth Blending zwischen Stufen über Timeline-Nodes. Kein Hard-Cut.

---

## 4. Vertikale Stadt — Occlusion, LOD, Sichtlinien

Die größte technische Herausforderung des Projekts. Die Stadt ist vertikal geschichtet wie eine Cyberpunk-Metropole — Macht oben, Slums unten. Das bedeutet:

**Occlusion**: Massive Überhänge und Brückenstrukturen blockieren natürliche Sichtlinien. UE5-Occlusion-Culling funktioniert horizontal gut, hat aber Schwächen bei starker Vertikalität. **Empfehlung**: Manuelle Occlusion Volumes für die Hauptebenen-Übergänge. Jede Stadtebene bekommt einen eigenen "Sichtbereich" — was von oben nicht sichtbar ist, wird aggressiv gecult. Das setzt voraus, dass das Level-Design Ebenen als diskrete Zonen behandelt.

**Streaming**: World Partition in UE5 ist Pflicht. Vertikale Achse muss in der Partitionierung berücksichtigt werden — UE5 World Partition ist primär horizontal konzipiert. Lösung: Manuelle Data Layers für Vertikalschichten (Layer 0: Untergrund/Kanäle, Layer 1: Straßenebene, Layer 2: Brücken/Arkaden, Layer 3: Türme/Gilden).

**Dark Souls-Referenz**: FromSoftware verwaltet Materiallesbarkeit durch starke Hell-Dunkel-Kontraste und begrenzte Farbpaletten pro Zone. Das ist für RELICS nützlich: jede Vertikalebene bekommt eine dominante Lichtstimmung (Oben: kaltes Tageslicht durch Bergkristall-Linsen; Mitte: warmes Kerzenlicht, Buntglas-Farbflecken; Unten: phosphoreszierendes Blau-Grün, Feuerschein). Lesbarkeit durch Licht, nicht durch Komplexitätsreduktion.

---

## 5. Kamerasystem — Third/First Person nahtlos

Skyrim-Referenz ist explizit im Briefing. Umsetzung in UE5:

**Ansatz**: Eine Camera-Komponente, zwei Modi. Kein Kamera-Swap, sondern Blend zwischen Offset-Position (Third-Person: 200cm hinter, 80cm über Schulter) und Eye-Position (First-Person: exakte Head-Socket-Koordinate). Blend-Zeit: 0.3 Sekunden, Ease-In/Out-Kurve.

**Herausforderung**: Das Nervensystem-Leveling-System zeigt halbtransparente Körper-Overlays (Cardio, Muskel, Lymph). Im Third-Person-Modus ist das trivial — Overlay auf Character Mesh. Im First-Person-Modus brauchen wir einen separaten "Arm Mesh", der das eigene Körper-Nervensystem in der Kamera-Perspektive zeigt. Das ist ein separates Mesh-Set, das synchron animiert werden muss. **Aufwand: mittel-hoch.**

**FOV**: Third Person: 90° empfohlen für das Gefühl von Raum in der vertikalen Stadt. First Person: 95–100° für Immersion in engen Gängen (Slums, Ordenskorridore). Beide als Spieler-Option exposiert.

---

## 6. Risiko-Übersicht

| System | Machbarkeit | Hauptrisiko |
|---|---|---|
| Nanite Geometrie | Hoch | Dünne Geometrien, erfordern Fallback |
| Lumen GI vertikal | Mittel | Degeneriert in tiefen Kanälen — Hybrid-Baking nötig |
| Biolumineszenz-Skala | Mittel | Performance bei vielen Emittern — Klassifizierung nötig |
| Schattenfieber PP | Hoch | Accessibility-Risiko bei Stufe 2/3 |
| Vertikales Culling | Mittel-Hoch | UE5 World Partition primär horizontal |
| Kamera-Blend | Hoch | Nervensystem-Arm-Mesh erhöht Aufwand |

**Gesamteinschätzung**: Das Projekt ist technisch machbar mit UE5. Kein System erfordert Custom-Engine-Arbeit. Die kritischste Entscheidung, die früh getroffen werden muss: wie diskret sind die Stadtebenen? Je klarer das Level-Design die Vertikalschichten trennt, desto robuster wird die gesamte technische Pipeline.

---

*Nächster Schritt: Abstimmung mit Vera über Vertikalstruktur. Abstimmung mit Nami über Post-Process-Stufen des Schattenfiebers.*
