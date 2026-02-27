# RELICS — Technische Pipeline-Architektur V0.1

**Autor:** Tobi Richter, Technical Artist
**Stand:** Tag 1, Montag — Recherche-Phase
**Status:** Entwurf, nicht abgestimmt

---

## 1. Asset-Pipeline

### 1.1 Geometrie — Nanite

Alle statischen Hard-Surface-Meshes laufen ueber Nanite. Das betrifft Architektur, Props, Waffen, Ruestungen, Terrain-Deko (Felsen, Ruinen).

**Einschraenkungen, die ich jetzt schon dokumentiere:**
- Nanite unterstuetzt kein Vertex-Animation (relevant fuer organische Biotech-Elemente, die pulsieren oder sich bewegen sollen)
- Nanite unterstuetzt kein Masked Material / Alpha-Testing (relevant fuer Vegetation)
- Skeletal Meshes (Charaktere, NPCs, Kreaturen) laufen nicht ueber Nanite

**Konsequenz:** Hybrides Setup. Baeume koennten als Nanite-Staemme mit traditionellen Blatt-Karten funktionieren. Gras und Unterholz ueber ISM (Instanced Static Mesh) oder Nanite Foliage (UE 5.3+ experimentell). Muss im Prototyp getestet werden.

### 1.2 Modulare Architektur

Bei einem Team dieser Groesse ist ein modulares Kit-System Pflicht. Die Gothic-Architektur-Referenz eignet sich dafuer hervorragend.

**Kit-Kategorien:**
- Mauern (gerade, Ecke, T-Stueck, Bogen)
- Boeden (Stein, Holz, Erde)
- Daecher (Giebel, Walm, Turmspitzen)
- Vertikale Elemente (Saeulen, Stuetzen, Treppen, Leitern)
- Dekorationen (Fenster, Tueren, Beschlaege, Laternen)

**Fraktions-Differenzierung ueber Material-Layer:**
Die drei Biotech-Sprachen (Krone=eleganter Zerfall, Gilden=industrielle Eleganz, Orden=monolithisch verbergend) werden nicht als separate Mesh-Sets gebaut. Stattdessen: gleiche Basis-Geometrie, unterschiedliche Material-Instanzen mit fraktionsspezifischen Detail-Layern. Das spart enorm Produktionszeit.

**Texel Density:** Einheitlich 10.24 px/cm fuer Hero-Assets, 5.12 px/cm fuer Hintergrund. Virtual Texturing fuer grosse einzigartige Oberflaechen (Wandmalereien, Karten).

**Naming Convention:** `SM_[Kategorie]_[Name]_[Variante]` (z.B. `SM_Wall_Stone_01`), Material-Instanzen: `MI_[Fraktion]_[Material]` (z.B. `MI_Gilden_Bronze_Patina`).

### 1.3 Houdini-Terrain

Houdini Engine for Unreal als Bridge. Terrain-Generation als HDA (Houdini Digital Asset).

**Pipeline:**
1. Heightfield-Generation in Houdini (Erosion, Terracing, Pfade)
2. Scatter-Layer fuer Vegetation, Felsen, Detail-Meshes
3. Export als UE5 Landscape ueber Houdini Engine Plugin
4. Manuelle Verfeinerung in UE5 (Landschaft-Splines fuer Wege, handplatzierte Hero-Props)

**Scope:** Bei 4-6 km² reicht ein einzelnes Landscape-Setup. World Partition fuer Streaming-Zellen (vermutlich 256m x 256m), aber kein OFPA (One File Per Actor) noetig bei dieser Groesse.

**Offene Frage:** Vera hat vermutlich keine Houdini-Erfahrung. Ich wuerde die HDAs bauen und ihr eine vereinfachte Oberflaeche geben, ueber die sie Parameter anpassen kann (Biom-Typ, Dichte, Hoehe). Das ist realistischer, als sie in Houdini einzuarbeiten, waehrend sie gleichzeitig Assets produziert.

### 1.4 PCG-Vegetation

Unreal 5.3+ PCG Framework fuer regelbasierte Vegetationsplatzierung.

**Ansatz:**
- Biom-Zonen als Spline-Areas definieren
- PCG-Graphen regeln Platzierung nach: Neigung, Hoehe, Bodentyp, Distanz zu Wegen/Gebaeuden
- Vera liefert 8-12 Vegetations-Assets pro Biom (Baeume, Straeucher, Bodendecker, Gras)
- PCG erzeugt natuerlich wirkende Verteilung

**Performance-Ueberlegung:** Vegetation-LOD aggressiv. Gras-Draw-Distance auf 50-80m begrenzen. Baumkronen ab 200m als Billboards oder Impostor-Baking.

---

## 2. Rendering-Pipeline

### 2.1 Global Illumination — Lumen

Lumen als primaeres GI-System. Keine Lightmaps, kein Baking.

**Modus-Empfehlung:**
- **Shipping:** Hardware Ray Tracing (HW RT Lumen) fuer bestmoegliche Qualitaet
- **Fallback:** Software Lumen fuer aeltere Hardware
- **Minimum Spec:** GTX 1070 / RX 5700 (Software Lumen)
- **Recommended Spec:** RTX 3070 / RX 6800 (HW RT Lumen)

**Warum Lumen hier besonders sinnvoll ist:**
Die Gothic-Architektur mit engen Gaengen, hohen Gewoelben und dramatischen Lichtschaechten lebt von indirektem Licht. Gebackene Lightmaps koennten das statisch, aber wir brauchen dynamische Tageszeiten und Wettereinfluss. Lumen liefert das ohne Bake-Zeit.

Referenz: Control (Remedy) — vergleichbare Raumsituationen, aehnliche Lichtqualitaet. Alan Wake 2 als Benchmark fuer atmosphaerisches Outdoor-Lumen.

### 2.2 Schatten — Virtual Shadow Maps

VSM ist Standard bei Lumen-Projekten. Vorteile:
- Einheitliches Schattensystem fuer alle Lichtquellen
- Keine Shadow Map Resolution-Probleme bei grossen Welten
- Automatische Detail-Skalierung nach Kameradistanz

**Performance-Risiko:** VSM kann teuer werden bei vielen kleinen Lichtquellen (Fackeln, Laternen in Gebaeuden). Budget: maximal 8-12 dynamische Lichtquellen pro Szene gleichzeitig. Statische Lichter mit begrenztem Radius als Alternative.

### 2.3 Post-Processing

Die Briefing-Tonalitaet ("duester, geerdet, gotische Grandeur") definiert den Look.

**Basis-Stack:**
- **Color Grading:** Gedaempfte Palette, Veras Hex-Codes als Ausgangspunkt. Kein Entsaettigungs-Klischee — die Welt soll duester, aber farbig sein. Eher Deakins als Snyder.
- **Tone Mapping:** ACES oder eigene LUT. Muss im Prototyp getestet werden.
- **Vignette:** Subtil, 0.3-0.4 Intensitaet.
- **Film Grain:** Optional, als Einstellung. Nicht aufzwingen.
- **DOF:** Cinematische DOF fuer Gespraeche und Cutscenes. Gameplay: nur leichte DOF im Hintergrund.
- **Bloom:** Minimal. Kein JJ-Abrams-Effekt. Nur fuer praktische Lichtquellen (Fackeln, Feuer).
- **Motion Blur:** Per-Object Motion Blur fuer Waffen-Swings. Kein Camera Motion Blur.

**Schattenfieber-Layer (Spezial-Post-Processing):**
Eigener Post-Processing-Volume oder Material-basierter Effekt, der sich mit dem Infektionsgrad des Spielers verstaerkt. Moegliche Effekte:
- Chromatische Aberration (leicht, steigend)
- Farbverschiebung (Schatten werden kaelter, Lichter waermer)
- Subtile geometrische Verzerrung am Bildrand
- Partikel-Overlay (Schattensporen?)

**Wichtig:** Das muss narrativ mit Emre und mechanisch mit Darius abgestimmt werden. Ich liefere die technische Palette, die muessen den Einsatz definieren.

---

## 3. Kamerasystem

### 3.1 Architektur

UE5 Spring Arm Component als Basis. Kein Custom-Camera von Grund auf.

**Parameter:**
- **Arm Length:** 250-450 cm (Exploration), 150-250 cm (Combat), 80-120 cm (Gespraech)
- **Zoom:** Smooth Interpolation via Timeline oder Curve. Spieler steuert ueber Mausrad oder Stick.
- **FOV:** 75-90 Grad, dynamisch. Engere Raeume leicht erhoehen (80-90), offene Welt Standard (75-80).
- **Camera Lag:** Leicht (Speed 8-10), damit die Kamera dem Charakter geschmeidig folgt statt starr.
- **Pitch Range:** -60 bis +70 Grad. Erweitert gegenueber Standard, um Vertikalitaet (Dishonored-Referenz) zu unterstuetzen.

### 3.2 Collision

Sphere Trace vom Charakter zum Kamera-Ziel. Bei Kollision: Kamera faehrt naeher ran. Kein Clipping durch Waende.

**Sonderfaelle:**
- Enge Gaenge: Kamera faehrt automatisch naeher, bleibt aber ueber Minimum-Distance
- Durchgaenge/Tuerrahmen: Smooth Blend, kein harter Snap
- Vegetation: Wird bei Kamera-Naehe ausgeblendet (Dithering), nicht kollidiert

### 3.3 Kontext-Wechsel

| Kontext | Arm Length | FOV | Offset | Bemerkung |
|---------|-----------|-----|--------|-----------|
| Exploration | 350 cm | 78 | Leicht rechts | Standard-Spielgefuehl |
| Combat | 200 cm | 82 | Ueber Schulter | Naeher, mehr Uebersicht |
| Gespraech | 100 cm | 72 | Schulterblick | Charakter sichtbar, NPC im Fokus |
| Inspect | 400 cm | 70 | Zentriert | Fuer Architektur/Umgebung |

Uebergaenge via Blend-Kurven (0.3-0.5 Sekunden). Kein harter Cut.

### 3.4 FP-Vorbereitung (V2)

Auch wenn FP erst V2 ist: Die Kamera-Architektur sollte so gebaut sein, dass der Zoom bis auf 0 cm Arm Length funktioniert. Dann ist der Uebergang zu FP nur eine Frage der Animations-Anpassungen, nicht der Kamera-Logik.

---

## 4. Middleware und Plugin-Empfehlungen

### 4.1 Combat — Gameplay Ability System (GAS)

**Empfehlung:** UE5-natives GAS als Basis fuer das Combat-System.

**Begruendung:**
- Engine-nativ, kein Drittanbieter-Risiko
- Skalierbar von einfachen Angriffen bis komplexen Faehigkeitsketten
- Attribute-System fuer Schattenfieber-Stats direkt nutzbar
- Lyra und andere Epic-Beispielprojekte als Referenz

**Risiko:** GAS hat eine steile Lernkurve. Ohne Gameplay-Programmer ist das der groesste Blocker im gesamten Projekt. Das ist kein technisches Problem, das ist ein Personalproblem.

**Alternative:** Marketplace-Framework (z.B. AGR Pro, Combat Framework) als Prototyp-Basis, dann Migration auf Custom-System wenn Programmer an Bord.

### 4.2 Animation

**Motion Matching** (UE 5.4+ experimentell) fuer natuerliches Movement. Das gewichtete Kampfgefuehl (Briefing: "Melee-fokussiert, gewichtig") profitiert enorm davon.

**Control Rig** fuer IK (Fussplatzierung auf unebenem Terrain, Waffenausrichtung).

**Anim-Assets:** Mixamo als Basis fuer Prototyping, Marketplace-Packs fuer Produktion, Motion Capture fuer Hero-Animationen (wenn Budget vorhanden).

### 4.3 Dialog

**Drei Optionen, noch keine Empfehlung:**
1. **Yarn Spinner (UE Port)** — Open Source, bewaehrt in Indie-Titeln, guter Editor
2. **Dialogue Plugin (Marketplace)** — Verschiedene Qualitaetsstufen, Vendor-Lock-in-Risiko
3. **Custom auf Data Tables** — Maximale Kontrolle, aber Eigenentwicklung

Muss mit Nami abgestimmt werden — sie definiert die narrativen Anforderungen, ich die technischen Constraints.

### 4.4 Weitere Empfehlungen

- **World Partition** — UE5-nativ, Pflicht fuer Semi-Open-World Streaming
- **Mass Entity / StateTree** — Fuer NPC-Verhalten und KI-Steuerung (leichtgewichtig)
- **MetaSounds** — Audio-Pipeline (nicht mein Kerngebiet, aber der logische UE5-Weg)
- **CommonUI** — UI-Framework fuer plattformuebergreifende Eingabe (Maus+Tastatur, Controller)

---

## 5. Offene Fragen und Risiken

### Kritisch (blockierend)

| # | Frage | Betrifft | Brauche Antwort von |
|---|-------|----------|---------------------|
| 1 | Gameplay-Programmer: Wann, wie? | Combat, Abilities, KI | Finn / CD |
| 2 | Zielplattformen? Nur PC oder auch Konsolen? | Performance-Budget, gesamte Pipeline | CD |
| 3 | Singleplayer bestaetigt? | Architektur-Entscheidungen | CD |

### Wichtig (nicht blockierend, aber bald noetig)

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
| Kein Gameplay-Programmer | Combat bleibt Prototyp, kein spielbarer Vertical Slice | Marketplace-Framework als Bruecke, Freelancer-Budget einplanen |
| Nanite-Einschraenkungen bei Biotech-Assets | Pulsierende organische Elemente brauchen Vertex Animation, die Nanite nicht kann | Hybrides Setup: Nanite fuer Basis, traditionelle Meshes fuer animierte Biotech-Elemente |
| Performance-Budget bei Lumen + dichte Gothic-Architektur | Framerate-Einbrueche in Innenraeumen mit vielen Lichtquellen | Lichtquellen-Budget pro Szene (8-12), Reflection Capture als Fallback |
| Vera als einzige Asset-Produzentin | Bottleneck bei Produktion | Modulares Kit maximieren, Marketplace-Assets als Basis, prozedurale Systeme wo moeglich |

---

## 6. Naechste Schritte

1. **Morgen (Tag 2):** Asset-Pipeline-Standards mit Vera abstimmen. Naming, Texel Density, LOD-Stufen.
2. **Diese Woche:** Houdini-HDA-Prototyp fuer ein Test-Terrain (1 km² Ausschnitt).
3. **Diese Woche:** UE5-Projekt-Template aufsetzen (Ordnerstruktur, Rendering-Settings, Kamera-Blueprint V0.1).
4. **Naechste Woche:** Combat-Middleware evaluieren (GAS-Prototyp vs. Marketplace-Framework).
5. **Offene Fragen 1-3** ans Review mitbringen.

---

*Methodische Anmerkung: Das ist eine V0.1-Skizze am ersten Tag. Vieles hier sind begruendete Annahmen, keine getesteten Fakten. Jeder einzelne Punkt muss im Prototyp validiert werden. Papier ist geduldig, die Engine nicht.*
