# Tobi — Memory

<!-- Nur der Agent selbst schreibt in diese Datei. GM fasst Memories NICHT an. -->

## Tag 1, Szene 2 — WORK (10:00 Uhr)

**Recherche abgeschlossen.** Artbooks gelesen: FFXIV 2.0 Concept Specs (Pipeline-Denken, Materiallesbarkeit durch Kontrast-Hierarchien), Dark Souls Design Works (tonale Dichte, Hell-Dunkel-Kontraste für Zonen-Lesbarkeit).

**Notat erstellt**: `simulation-2/gallery/gdd/00-recherche-notizen-tobi.md`

### Technische Kernentscheidungen (vorläufig)

- **Nanite**: Gesetzt. Fallback für dünne Geometrien (Ketten, Pflanzen) notwendig.
- **Lumen**: Hardware-RT für obere Stadtebenen. Hybrid-Baking für Slum-Kanäle/Untergrund. Lumen degeneriert bei starker Überdachung — das ist das zentrale Problem der vertikalen Stadt.
- **Biolumineszenz**: Drei Klassen (A: echte Lumen-Emitter, B: visuell ohne GI, C: Niagara-Partikel). Kontrast-Hierarchie nach FFXIV-Vorbild.
- **Schattenfieber PP**: Drei Stufen, Blueprint-gesteuert, smooth geblendet. Stufe 2/3 brauchen Accessibility-Option (Motion Sickness).
- **Vertikale Stadt**: World Partition mit manuellen Data Layers (4 Vertikalschichten). Manuelle Occlusion Volumes für Ebenen-Übergänge. UE5 World Partition ist primär horizontal — das muss früh adressiert werden.
- **Kamera**: Blend-System, kein Swap. Nervensystem-Visualisierung im First-Person-Modus erfordert separates Arm-Mesh-Set.

### Offene Fragen / Nächste Schritte

- Abstimmung mit **Vera**: Wie diskret sind die Stadtebenen im Level-Design? Das bestimmt die gesamte Culling-Strategie.
- Abstimmung mit **Nami**: Post-Process-Parameter für Schattenfieber-Stufen — was ist narrativ gewollt, was ist technisch umsetzbar?
- **Kritischste frühe Entscheidung**: Vertikalstruktur der Stadt muss als Level-Design-Constraint definiert sein, bevor ich die World-Partition-Architektur aufsetze.

### Beobachtungen

- FFXIV v2.0: Konzept-Specs zeigen sauberes Silhouetten-Denken. Charaktere sind auch im Kampf-Chaos lesbar durch starke Form-Hierarchien. Relevant für RELICS: Rustungen und Fraktionszugehörigkeit müssen in Bewegung erkennbar bleiben.
- Dark Souls Design Works: Materialien erzählen Geschichte durch Abnutzung und Kontextualisierung. Für RELICS: Materialien definieren sozialen Status (Briefing) — das muss im Material-Graph sichtbar sein, nicht nur in der Concept Art.
