# Reasoning — Tobi, Tag 1, Szene 5 (WORK)

## Denkprozess

### 1. Rahmenbedingungen ordnen

Die drei kritischen Engpaesse aus meiner Machbarkeitsanalyse sind jetzt teilweise entschaerft:
- Scope: Semi-Open-World bestaetigt. 4-6 km² ist realistisch fuer ein kleines Team.
- Kamera: TP Primaermodus bestaetigt. Kein doppelter Animationsaufwand.
- Gameplay-Programmer: Immer noch offen. Brauche Middleware-Empfehlung.
- Asset-Produktion: Immer noch kritisch. Vera allein reicht nicht. Modulares Kit + prozedurale Systeme.

### 2. Asset-Pipeline-Ueberlegungen

Nanite ist gesetzt. Aber Nanite hat Einschraenkungen, die ich dokumentieren muss:
- Kein Vertex-Animation-Support (relevant fuer organische Biotech-Materialien)
- Kein Masked-Material-Support (Alpha-tested Foliage)
- Vegetation muss hybrides Setup bekommen: Baeume als Nanite, Gras/Unterholz als traditionelle ISM

Modulare Architektur ist Pflicht bei einem Team dieser Groesse. Gothic-Stil-Architektur eignet sich gut dafuer: Wiederverwendbare Mauer-, Bogen- und Turm-Module. Die drei fraktionsspezifischen Biotech-Sprachen (Krone=Zerfall, Gilden=industriell, Orden=monolithisch) muessen als Material-Layer funktionieren, nicht als separate Asset-Sets. Sonst explodiert die Produktion.

Houdini-Terrain: World Partition + Houdini Engine for UE liefert prozedurales Heightfield + Scatter. Bei 4-6 km² ist ein einzelnes Landscape ausreichend, kein OFPA noetig. Aber World Partition fuer Streaming trotzdem sinnvoll.

### 3. Rendering-Ueberlegungen

Lumen ist die logische Wahl fuer die angestrebte Beleuchtungsqualitaet. Control und Alan Wake 2 sind meine Referenzen — beides UE-Titel mit starkem atmosphaerischem Lighting.

Lumen-Modus: Hardware Ray Tracing fuer Shipping, Software Lumen als Fallback. Die Gothic-Architektur mit engen Innenraeumen und dramatischen Lichtschaechten profitiert enorm von Lumen GI.

Virtual Shadow Maps sind Standard bei Lumen-Projekten. Kein Grund, davon abzuweichen.

Post-Processing: Hier ist die Briefing-Tonalitaet entscheidend. "Duester, geerdet, politisch. Gotische Grandeur trifft feudale Brutalitaet." Das ist kein Bloom-Festival. Ich denke an:
- Kontrollierte Color Grading (Veras Farbpalette als Basis)
- Subtile Vignette
- Film Grain optional
- Schattenfieber-Post-Processing als eigener Layer (Wahrnehmungsverzerrung bei Infektion)

### 4. Kamerasystem-Ueberlegungen

TP mit Zoom ist technisch ein Spring Arm mit variabler Laenge. Collision-Handling ueber Sphere Trace. Zoom-Stufen: Exploration (weiter), Combat (naeher), Conversation (Schulterblick oder leichter Zoom).

Wichtig: Die Kamera muss die Architektur-Vertikalitaet (Dishonored-Referenz) unterstuetzen. Pitch-Range erweitern, eventuell dynamische FOV-Anpassung bei Hoehenunterschieden.

Kein echtes FP in V1, aber der Zoom sollte nah genug rangehen, dass es sich fast wie FP anfuehlt. Smooth Interpolation zwischen Zoom-Stufen.

### 5. Middleware-Ueberlegungen

Combat: Ohne Gameplay-Programmer brauchen wir ein Framework. Optionen:
- GAS (Gameplay Ability System) — UE5-nativ, maechtig, aber steile Lernkurve
- Marketplace Combat Frameworks — Risiko: Qualitaet, Wartung, Vendor Lock-in
- Custom auf GAS-Basis — meine Empfehlung, aber braucht Programmier-Kompetenz

Animation: UE5 Control Rig + IK ist inzwischen ausgereift. Motion Matching waere ideal fuer das gewichtete Movement-Feel, ist aber aufwaendig.

Dialog: Empfehlung bleibt offen — muss ich recherchieren. Yarn Spinner (Unity-native, UE-Port existiert) oder ein eigenes System auf Data Tables.

### 6. Offene Fragen

- Gameplay-Programmer ist der groesste Blocker. Ohne den bleibt Combat-Middleware theoretisch.
- Art-Pipeline-Standards muessen mit Vera abgestimmt werden (Texel Density, LOD-Stufen, Naming).
- Performance-Budget fuer Schattenfieber-VFX ist unklar. Brauche Emres Beschreibung der visuellen Auswirkungen.
- Netzwerk/Multiplayer: Im Briefing nicht erwaehnt, gehe von Singleplayer aus. Muss bestaetigt werden.

### 7. Was ich NICHT weiss

- Zielplattform(en) jenseits von PC. Konsolen-Support aendert Performance-Budget massiv.
- Audio-Pipeline. Nicht mein Bereich, aber MetaSounds waere der logische UE5-Weg.
- UI-Framework. CommonUI oder eigenes Widget-System?
- Ob Vera bereits mit Houdini-Erfahrung kommt oder ob ich sie einarbeiten muss (vermute Letzteres).
