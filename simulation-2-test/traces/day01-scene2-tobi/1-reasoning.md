# Reasoning — Tobi, Tag 1, Szene 2 (WORK)

## Erste Reaktion

Das Briefing ist ambitioniert. Ich sortiere das mal nach dem, was UE5 uns "geschenkt" gibt, und dem, was wir selbst bauen muessen.

## Gedankengang

### Was UE5 mitbringt (geschenkt)

- **Nanite**: Virtualisierte Geometrie. Fuer uns enorm wichtig — wir koennen hochaufgeloeste Meshes direkt verwenden, ohne manuelles LOD-Authoring. Das spart einem kleinen Team Wochen. Aber: Nanite unterstuetzt keine Skeletal Meshes (Stand UE 5.4). Charaktere, NPCs, Tiere — alles, was sich bewegt — braucht trotzdem klassische LODs.
- **Lumen**: Globale Beleuchtung und Reflektionen in Echtzeit. Fuer die "gotische Grandeur" im Briefing ist das ein Geschenk. Kein Baken von Lightmaps noetig. Aber: Lumen ist teuer. Offene Welten mit vielen Lichtquellen bringen es an die Grenzen. Hardware-Raytracing (HWRT) vs. Software-Raytracing — wir muessen frueh entscheiden, was unsere Mindest-Spec ist.
- **World Partition**: UE5 kann grosse Welten in Zellen aufteilen und streamen. Das ist die Grundlage fuer Open-World. Funktioniert, ist aber nicht trivial zu debuggen.
- **PCG Framework**: Procedural Content Generation. Fuer Vegetation, Platzierung von Steinen, etc. Kann einem kleinen Team enorm helfen, wenn man es richtig aufsetzt.

### Was wir selbst bauen muessen

- **Kamerasystem FP/TP**: Das ist kein Checkbox-Feature. Skyrim hat das, aber Skyrim hatte ein 100+ Team und Jahre. Das Problem: Animationen muessen fuer beide Perspektiven funktionieren. FP-Arme vs. Vollkoerpermodel. UI/HUD muss sich anpassen. Das ist architektonisch ein fruehes Commitment — wenn wir es falsch aufsetzen, kostet es uns spaeter Monate. Mein Vorschlag: Mit TP anfangen, FP als Stretch Goal behandeln. Oder: Einen smarten Zoom-Ansatz waehlen, aehnlich wie TES, aber mit festem TP als Primaermodus.
- **Combat-System**: Real-time Melee ist eines der schwersten Systeme in Spielen. Hit Detection, Animation Blending, Stagger, Blocking, Stamina, Waffengewicht — das ist ein dedizierter Gameplay Programmer fuer Monate. Wir haben keinen. Darius ist Game Designer, kein Programmer. Ich kann Blueprint-Prototypen bauen, aber C++-Combat-Code ist nicht mein Kern. Entweder brauchen wir Middleware, oder wir muessen den Scope radikal vereinfachen.
- **NPC-AI**: Offene Welt mit lebendigen NPCs braucht Verhaltensbaeume, Scheduling, Pathfinding. UE5 hat Grundlagen, aber fuer Gothic-artige "lebendige" NPCs braucht es viel Custom-Arbeit.
- **Quest-System**: Nicht mein Bereich, aber technisch ein eigenes Framework. Dialogbaeume, Zustandsmaschinen, Trigger-Systeme.

### Asset-Pipeline — der eigentliche Engpass

Wir sind 7 Leute. Davon kann genau eine Person (Vera) Assets produzieren. Ich kann prozedurale Systeme in Houdini bauen — Terrain, Felsen, Vegetation-Platzierung — aber kein Character Art, keine Architektur im Detail, keine Requisiten. Vera muss Concept Art UND 3D-Produktion machen. Das ist bei einem Spiel dieser Ambition nicht machbar ohne:

1. **Aggressive prozedurale Generierung** (mein Job — Houdini-Terrain, PCG in UE5)
2. **Asset Store / Marketplace** als Basis (kontrovers, aber realistisch)
3. **Photogrammetrie** fuer Umgebungs-Assets (wenn wir die Pipeline aufsetzen)
4. **KI-gestuetzte Asset-Erstellung** (Mesh-Generierung ist noch nicht produktionsreif, aber Texturen sind machbar)

### Scope-Empfehlung

Das Briefing sagt "Open-World/Semi-Open-World". Ich wuerde stark zu Semi-Open-World raten — mehrere zusammenhaengende Zonen, Gothic-Stil, nicht Skyrim-Stil. Gruende:

- Weniger Terrain, weniger Assets, weniger Streaming-Komplexitaet
- Dichtere Erfahrung passt zum "Gothic"-Referenz im Briefing ("Dichte statt Breite")
- Einfacher zu testen fuer Leo mit begrenzter QA-Kapazitaet
- Lumen funktioniert besser in kontrollierteren Umgebungen

### Mindest-Spec und Performance

Muessen wir frueh definieren. Mein Vorschlag:
- PC-only (erst mal kein Konsolen-Port)
- RTX 3060 / RX 6700 XT als Minimum (fuer Software Lumen)
- DLSS/FSR als Pflicht (ohne Upscaling laueft UE5 auf Mittelklasse-Hardware nicht)
- 30 FPS Minimum, 60 FPS Target

### Was ich heute anfange

1. Dieses Dokument hier — Machbarkeitsanalyse
2. Erste Struktur fuer die Pipeline-Bibel
3. Notizen fuer das Standup um 11:30 — das Team muss frueh verstehen, wo die technischen Grenzen liegen

## Offene Fragen (fuer CD / Team)

- Primaere Perspektive: Wollen wir wirklich beides (FP+TP) oder koennen wir mit TP + Zoom-in leben?
- Zielplattform: Nur PC oder auch Konsolen?
- Budget fuer Marketplace-Assets?
- Vertical Slice Scope: Eine Region, eine Stadt, ein Dungeon?
