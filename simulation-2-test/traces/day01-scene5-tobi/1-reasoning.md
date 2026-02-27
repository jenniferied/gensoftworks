# Reasoning — Tobi, Tag 1, Szene 5 (WORK)

## Denkprozess

### 1. Rahmenbedingungen ordnen

Die drei kritischen Engpässe aus meiner Machbarkeitsanalyse sind jetzt teilweise entschärft:
- Scope: Semi-Open-World bestätigt. 4-6 km² ist realistisch für ein kleines Team.
- Kamera: TP Primärmodus bestätigt. Kein doppelter Animationsaufwand.
- Gameplay-Programmer: Immer noch offen. Brauche Middleware-Empfehlung.
- Asset-Produktion: Immer noch kritisch. Vera allein reicht nicht. Modulares Kit + prozedurale Systeme.

### 2. Asset-Pipeline-Überlegungen

Nanite ist gesetzt. Aber Nanite hat Einschränkungen, die ich dokumentieren muss:
- Kein Vertex-Animation-Support (relevant für organische Biotech-Materialien)
- Kein Masked-Material-Support (Alpha-tested Foliage)
- Vegetation muss hybrides Setup bekommen: Bäume als Nanite, Gras/Unterholz als traditionelle ISM

Modulare Architektur ist Pflicht bei einem Team dieser Grösse. Gothic-Stil-Architektur eignet sich gut dafür: Wiederverwendbare Mauer-, Bogen- und Turm-Module. Die drei fraktionsspezifischen Biotech-Sprachen (Krone=Zerfall, Gilden=industriell, Orden=monolithisch) müssen als Material-Layer funktionieren, nicht als separate Asset-Sets. Sonst explodiert die Produktion.

Houdini-Terrain: World Partition + Houdini Engine for Ü liefert prozedurales Heightfield + Scatter. Bei 4-6 km² ist ein einzelnes Landscape ausreichend, kein OFPA nötig. Aber World Partition für Streaming trotzdem sinnvoll.

### 3. Rendering-Überlegungen

Lumen ist die logische Wahl für die angestrebte Beleuchtungsqualität. Control und Alan Wake 2 sind meine Referenzen — beides Ü-Titel mit starkem atmosphärischem Lighting.

Lumen-Modus: Hardware Ray Tracing für Shipping, Software Lumen als Fallback. Die Gothic-Architektur mit engen Innenräumen und dramatischen Lichtschächten profitiert enorm von Lumen GI.

Virtual Shadow Maps sind Standard bei Lumen-Projekten. Kein Grund, davon abzuweichen.

Post-Processing: Hier ist die Briefing-Tonalität entscheidend. "Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität." Das ist kein Bloom-Festival. Ich denke an:
- Kontrollierte Color Grading (Veras Farbpalette als Basis)
- Subtile Vignette
- Film Grain optional
- Schattenfieber-Post-Processing als eigener Layer (Wahrnehmungsverzerrung bei Infektion)

### 4. Kamerasystem-Überlegungen

TP mit Zoom ist technisch ein Spring Arm mit variabler Länge. Collision-Handling über Sphere Trace. Zoom-Stufen: Exploration (weiter), Combat (näher), Conversation (Schulterblick oder leichter Zoom).

Wichtig: Die Kamera muss die Architektur-Vertikalität (Dishonored-Referenz) unterstützen. Pitch-Range erweitern, eventuell dynamische FOV-Anpassung bei Höhenunterschieden.

Kein echtes FP in V1, aber der Zoom sollte nah genug rangehen, dass es sich fast wie FP anfühlt. Smooth Interpolation zwischen Zoom-Stufen.

### 5. Middleware-Überlegungen

Combat: Ohne Gameplay-Programmer brauchen wir ein Framework. Optionen:
- GAS (Gameplay Ability System) — Ü5-nativ, mächtig, aber steile Lernkurve
- Marketplace Combat Frameworks — Risiko: Qualität, Wartung, Vendor Lock-in
- Custom auf GAS-Basis — meine Empfehlung, aber braucht Programmier-Kompetenz

Animation: Ü5 Control Rig + IK ist inzwischen ausgereift. Motion Matching wäre ideal für das gewichtete Movement-Feel, ist aber aufwändig.

Dialog: Empfehlung bleibt offen — muss ich recherchieren. Yarn Spinner (Unity-native, Ü-Port existiert) oder ein eigenes System auf Data Tables.

### 6. Offene Fragen

- Gameplay-Programmer ist der grösste Blocker. Ohne den bleibt Combat-Middleware theoretisch.
- Art-Pipeline-Standards müssen mit Vera abgestimmt werden (Texel Density, LOD-Stufen, Naming).
- Performance-Budget für Schattenfieber-VFX ist unklar. Brauche Emres Beschreibung der visuellen Auswirkungen.
- Netzwerk/Multiplayer: Im Briefing nicht erwähnt, gehe von Singleplayer aus. Muss bestätigt werden.

### 7. Was ich NICHT weiss

- Zielplattform(en) jenseits von PC. Konsolen-Support ändert Performance-Budget massiv.
- Audio-Pipeline. Nicht mein Bereich, aber MetaSounds wäre der logische Ü5-Weg.
- UI-Framework. CommonUI oder eigenes Widget-System?
- Ob Vera bereits mit Houdini-Erfahrung kommt oder ob ich sie einarbeiten muss (vermute Letzteres).
