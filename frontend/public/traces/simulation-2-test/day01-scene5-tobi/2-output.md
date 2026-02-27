# RELICS — Technische Pipeline-Architektur V0.1

**Autor:** Tobi Richter, Technical Artist
**Stand:** Tag 1, Montag — Recherche-Phase
**Status:** Entwurf, nicht abgestimmt

---

## 1. Asset-Pipeline

### 1.1 Geometrie — Nanite

Alle statischen Hard-Surface-Meshes laufen über Nanite. Das betrifft Architektur, Props, Waffen, Rüstungen, Terrain-Deko (Felsen, Ruinen).

**Einschränkungen, die ich jetzt schon dokumentiere:**
- Nanite unterstützt kein Vertex-Animation (relevant für organische Biotech-Elemente, die pulsieren oder sich bewegen sollen)
- Nanite unterstützt kein Masked Material / Alpha-Testing (relevant für Vegetation)
- Skeletal Meshes (Charaktere, NPCs, Kreaturen) laufen nicht über Nanite

**Konsequenz:** Hybrides Setup. Bäume könnten als Nanite-Stämme mit traditionellen Blatt-Karten funktionieren. Gras und Unterholz über ISM (Instanced Static Mesh) oder Nanite Foliage (Ü 5.3+ experimentell). Muss im Prototyp getestet werden.

### 1.2 Modulare Architektur

Bei einem Team dieser Grösse ist ein modulares Kit-System Pflicht. Die Gothic-Architektur-Referenz eignet sich dafür hervorragend.

**Kit-Kategorien:**
- Mauern (gerade, Ecke, T-Stück, Bogen)
- Böden (Stein, Holz, Erde)
- Dächer (Giebel, Walm, Turmspitzen)
- Vertikale Elemente (Säulen, Stützen, Treppen, Leitern)
- Dekorationen (Fenster, Türen, Beschläge, Laternen)

**Fraktions-Differenzierung über Material-Layer:**
Die drei Biotech-Sprachen (Krone=eleganter Zerfall, Gilden=industrielle Eleganz, Orden=monolithisch verbergend) werden nicht als separate Mesh-Sets gebaut. Stattdessen: gleiche Basis-Geometrie, unterschiedliche Material-Instanzen mit fraktionsspezifischen Detail-Layern. Das spart enorm Produktionszeit.

**Texel Density:** Einheitlich 10.24 px/cm für Hero-Assets, 5.12 px/cm für Hintergrund. Virtual Texturing für grosse einzigartige Oberflächen (Wandmalereien, Karten).

**Naming Convention:** `SM_[Kategorie]_[Name]_[Variante]` (z.B. `SM_Wall_Stone_01`), Material-Instanzen: `MI_[Fraktion]_[Material]` (z.B. `MI_Gilden_Bronze_Patina`).

### 1.3 Houdini-Terrain

Houdini Engine for Unreal als Bridge. Terrain-Generation als HDA (Houdini Digital Asset).

**Pipeline:**
1. Heightfield-Generation in Houdini (Erosion, Terracing, Pfade)
2. Scatter-Layer für Vegetation, Felsen, Detail-Meshes
3. Export als Ü5 Landscape über Houdini Engine Plugin
4. Manuelle Verfeinerung in Ü5 (Landschaft-Splines für Wege, handplatzierte Hero-Props)

**Scope:** Bei 4-6 km² reicht ein einzelnes Landscape-Setup. World Partition für Streaming-Zellen (vermutlich 256m x 256m), aber kein OFPA (One File Per Actor) nötig bei dieser Grösse.

**Offene Frage:** Vera hat vermutlich keine Houdini-Erfahrung. Ich würde die HDAs bauen und ihr eine vereinfachte Oberfläche geben, über die sie Parameter anpassen kann (Biom-Typ, Dichte, Höhe). Das ist realistischer, als sie in Houdini einzuarbeiten, während sie gleichzeitig Assets produziert.

### 1.4 PCG-Vegetation

Unreal 5.3+ PCG Framework für regelbasierte Vegetationsplatzierung.

**Ansatz:**
- Biom-Zonen als Spline-Areas definieren
- PCG-Graphen regeln Platzierung nach: Neigung, Höhe, Bodentyp, Distanz zu Wegen/Gebäuden
- Vera liefert 8-12 Vegetations-Assets pro Biom (Bäume, Sträucher, Bodendecker, Gras)
- PCG erzeugt natürlich wirkende Verteilung

**Performance-Überlegung:** Vegetation-LOD aggressiv. Gras-Draw-Distance auf 50-80m begrenzen. Baumkronen ab 200m als Billboards oder Impostor-Baking.

---

## 2. Rendering-Pipeline

### 2.1 Global Illumination — Lumen

Lumen als primäres GI-System. Keine Lightmaps, kein Baking.

**Modus-Empfehlung:**
- **Shipping:** Hardware Ray Tracing (HW RT Lumen) für bestmögliche Qualität
- **Fallback:** Software Lumen für ältere Hardware
- **Minimum Spec:** GTX 1070 / RX 5700 (Software Lumen)
- **Recommended Spec:** RTX 3070 / RX 6800 (HW RT Lumen)

**Warum Lumen hier besonders sinnvoll ist:**
Die Gothic-Architektur mit engen Gängen, hohen Gewölben und dramatischen Lichtschächten lebt von indirektem Licht. Gebackene Lightmaps könnten das statisch, aber wir brauchen dynamische Tageszeiten und Wettereinfluss. Lumen liefert das ohne Bake-Zeit.

Referenz: Control (Remedy) — vergleichbare Raumsituationen, ähnliche Lichtqualität. Alan Wake 2 als Benchmark für atmosphärisches Outdoor-Lumen.

### 2.2 Schatten — Virtual Shadow Maps

VSM ist Standard bei Lumen-Projekten. Vorteile:
- Einheitliches Schattensystem für alle Lichtquellen
- Keine Shadow Map Resolution-Probleme bei grossen Welten
- Automatische Detail-Skalierung nach Kameradistanz

**Performance-Risiko:** VSM kann teuer werden bei vielen kleinen Lichtquellen (Fackeln, Laternen in Gebäuden). Budget: maximal 8-12 dynamische Lichtquellen pro Szene gleichzeitig. Statische Lichter mit begrenztem Radius als Alternative.

### 2.3 Post-Processing

Die Briefing-Tonalität ("düster, geerdet, gotische Grandeur") definiert den Look.

**Basis-Stack:**
- **Color Grading:** Gedämpfte Palette, Veras Hex-Codes als Ausgangspunkt. Kein Entsättigungs-Klischee — die Welt soll düster, aber farbig sein. Eher Deakins als Snyder.
- **Tone Mapping:** ACES oder eigene LUT. Muss im Prototyp getestet werden.
- **Vignette:** Subtil, 0.3-0.4 Intensität.
- **Film Grain:** Optional, als Einstellung. Nicht aufzwingen.
- **DOF:** Cinematische DOF für Gespräche und Cutscenes. Gameplay: nur leichte DOF im Hintergrund.
- **Bloom:** Minimal. Kein JJ-Abrams-Effekt. Nur für praktische Lichtquellen (Fackeln, Feuer).
- **Motion Blur:** Per-Object Motion Blur für Waffen-Swings. Kein Camera Motion Blur.

**Schattenfieber-Layer (Spezial-Post-Processing):**
Eigener Post-Processing-Volume oder Material-basierter Effekt, der sich mit dem Infektionsgrad des Spielers verstärkt. Mögliche Effekte:
- Chromatische Aberration (leicht, steigend)
- Farbverschiebung (Schatten werden kälter, Lichter wärmer)
- Subtile geometrische Verzerrung am Bildrand
- Partikel-Overlay (Schattensporen?)

**Wichtig:** Das muss narrativ mit Emre und mechanisch mit Darius abgestimmt werden. Ich liefere die technische Palette, die müssen den Einsatz definieren.

---

## 3. Kamerasystem

### 3.1 Architektur

Ü5 Spring Arm Component als Basis. Kein Custom-Camera von Grund auf.

**Parameter:**
- **Arm Length:** 250-450 cm (Exploration), 150-250 cm (Combat), 80-120 cm (Gespräch)
- **Zoom:** Smooth Interpolation via Timeline oder Curve. Spieler steuert über Mausrad oder Stick.
- **FOV:** 75-90 Grad, dynamisch. Engere Räume leicht erhöhen (80-90), offene Welt Standard (75-80).
- **Camera Lag:** Leicht (Speed 8-10), damit die Kamera dem Charakter geschmeidig folgt statt starr.
- **Pitch Range:** -60 bis +70 Grad. Erweitert gegenüber Standard, um Vertikalität (Dishonored-Referenz) zu unterstützen.

### 3.2 Collision

Sphere Trace vom Charakter zum Kamera-Ziel. Bei Kollision: Kamera fährt näher ran. Kein Clipping durch Wände.

**Sonderfälle:**
- Enge Gänge: Kamera fährt automatisch näher, bleibt aber über Minimum-Distance
- Durchgänge/Türrahmen: Smooth Blend, kein harter Snap
- Vegetation: Wird bei Kamera-Nähe ausgeblendet (Dithering), nicht kollidiert

### 3.3 Kontext-Wechsel

| Kontext | Arm Length | FOV | Offset | Bemerkung |
|---------|-----------|-----|--------|-----------|
| Exploration | 350 cm | 78 | Leicht rechts | Standard-Spielgefühl |
| Combat | 200 cm | 82 | Über Schulter | Näher, mehr Übersicht |
| Gespräch | 100 cm | 72 | Schulterblick | Charakter sichtbar, NPC im Fokus |
| Inspect | 400 cm | 70 | Zentriert | Für Architektur/Umgebung |

Übergänge via Blend-Kurven (0.3-0.5 Sekunden). Kein harter Cut.

### 3.4 FP-Vorbereitung (V2)

Auch wenn FP erst V2 ist: Die Kamera-Architektur sollte so gebaut sein, dass der Zoom bis auf 0 cm Arm Length funktioniert. Dann ist der Übergang zu FP nur eine Frage der Animations-Anpassungen, nicht der Kamera-Logik.

---

## 4. Middleware und Plugin-Empfehlungen

### 4.1 Combat — Gameplay Ability System (GAS)

**Empfehlung:** Ü5-natives GAS als Basis für das Combat-System.

**Begründung:**
- Engine-nativ, kein Drittanbieter-Risiko
- Skalierbar von einfachen Angriffen bis komplexen Fähigkeitsketten
- Attribute-System für Schattenfieber-Stats direkt nutzbar
- Lyra und andere Epic-Beispielprojekte als Referenz

**Risiko:** GAS hat eine steile Lernkurve. Ohne Gameplay-Programmer ist das der grösste Blocker im gesamten Projekt. Das ist kein technisches Problem, das ist ein Personalproblem.

**Alternative:** Marketplace-Framework (z.B. AGR Pro, Combat Framework) als Prototyp-Basis, dann Migration auf Custom-System wenn Programmer an Bord.

### 4.2 Animation

**Motion Matching** (Ü 5.4+ experimentell) für natürliches Movement. Das gewichtete Kampfgefühl (Briefing: "Melee-fokussiert, gewichtig") profitiert enorm davon.

**Control Rig** für IK (Fussplatzierung auf unebenem Terrain, Waffenausrichtung).

**Anim-Assets:** Mixamo als Basis für Prototyping, Marketplace-Packs für Produktion, Motion Capture für Hero-Animationen (wenn Budget vorhanden).

### 4.3 Dialog

**Drei Optionen, noch keine Empfehlung:**
1. **Yarn Spinner (Ü Port)** — Open Source, bewährt in Indie-Titeln, guter Editor
2. **Dialogue Plugin (Marketplace)** — Verschiedene Qualitätsstufen, Vendor-Lock-in-Risiko
3. **Custom auf Data Tables** — Maximale Kontrolle, aber Eigenentwicklung

Muss mit Nami abgestimmt werden — sie definiert die narrativen Anforderungen, ich die technischen Constraints.

### 4.4 Weitere Empfehlungen

- **World Partition** — Ü5-nativ, Pflicht für Semi-Open-World Streaming
- **Mass Entity / StateTree** — Für NPC-Verhalten und KI-Steuerung (leichtgewichtig)
- **MetaSounds** — Audio-Pipeline (nicht mein Kerngebiet, aber der logische Ü5-Weg)
- **CommonUI** — UI-Framework für plattformübergreifende Eingabe (Maus+Tastatur, Controller)

---

## 5. Offene Fragen und Risiken

### Kritisch (blockierend)

| # | Frage | Betrifft | Brauche Antwort von |
|---|-------|----------|---------------------|
| 1 | Gameplay-Programmer: Wann, wie? | Combat, Abilities, KI | Finn / CD |
| 2 | Zielplattformen? Nur PC oder auch Konsolen? | Performance-Budget, gesamte Pipeline | CD |
| 3 | Singleplayer bestätigt? | Architektur-Entscheidungen | CD |

### Wichtig (nicht blockierend, aber bald nötig)

| # | Frage | Betrifft | Brauche Antwort von |
|---|-------|----------|---------------------|
| 4 | Asset-Naming und Texel-Density-Standards | Asset-Pipeline | Vera |
| 5 | Schattenfieber: Visuelle Auswirkungen auf Spieler? | Post-Processing, VFX | Emre / Darius |
| 6 | Dialog-System: Narrative Anforderungen? | Middleware-Wahl | Nami |
| 7 | Terrain-Biome: Wie viele, welche? | Houdini-Pipeline, PCG | Emre (Topos) |
| 8 | Audio-Pipeline: Wer verantwortet das? | MetaSounds-Setup | Finn |

### Risiken

| Risiko | Auswirkung | Gegenmassnahme |
|--------|-----------|----------------|
| Kein Gameplay-Programmer | Combat bleibt Prototyp, kein spielbarer Vertical Slice | Marketplace-Framework als Brücke, Freelancer-Budget einplanen |
| Nanite-Einschränkungen bei Biotech-Assets | Pulsierende organische Elemente brauchen Vertex Animation, die Nanite nicht kann | Hybrides Setup: Nanite für Basis, traditionelle Meshes für animierte Biotech-Elemente |
| Performance-Budget bei Lumen + dichte Gothic-Architektur | Framerate-Einbrüche in Innenräumen mit vielen Lichtquellen | Lichtquellen-Budget pro Szene (8-12), Reflection Capture als Fallback |
| Vera als einzige Asset-Produzentin | Bottleneck bei Produktion | Modulares Kit maximieren, Marketplace-Assets als Basis, prozedurale Systeme wo möglich |

---

## 6. Nächste Schritte

1. **Morgen (Tag 2):** Asset-Pipeline-Standards mit Vera abstimmen. Naming, Texel Density, LOD-Stufen.
2. **Diese Woche:** Houdini-HDA-Prototyp für ein Test-Terrain (1 km² Ausschnitt).
3. **Diese Woche:** Ü5-Projekt-Template aufsetzen (Ordnerstruktur, Rendering-Settings, Kamera-Blueprint V0.1).
4. **Nächste Woche:** Combat-Middleware evaluieren (GAS-Prototyp vs. Marketplace-Framework).
5. **Offene Fragen 1-3** ans Review mitbringen.

---

*Methodische Anmerkung: Das ist eine V0.1-Skizze am ersten Tag. Vieles hier sind begründete Annahmen, keine getesteten Fakten. Jeder einzelne Punkt muss im Prototyp validiert werden. Papier ist geduldig, die Engine nicht.*
