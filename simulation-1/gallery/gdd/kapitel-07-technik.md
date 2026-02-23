# Kapitel 7 — Technik

---

## 7.1 Engine & Ziel-Hardware

**Engine**: Unreal Engine 5.4+ (Nanite, Lumen, World Partition, Enhanced Input)

**Zielplattform**: PC (Steam) — Konsole als Stretch Goal, nicht für V1 geplant.

**Ziel-Framerate**: 60 fps @ 1440p auf Mid-Range-Hardware (RTX 4060 / RX 7600 Äquivalent).

---

## 7.2 Kamera-System

### Konzept

Skyrim-Style nahtloses Umschalten zwischen First Person (FP) und Third Person (TP). Keine harte Trennung — ein fließender Übergang über Kamera-Boom und FOV-Interpolation.

### Technische Umsetzung

**Ein Skelett, eine Mesh-Instanz.** Kein Dual-Character-Setup.

| Kamera-State | Verhalten |
|---|---|
| FP | Runtime-Visibility-Maske blendet Kopf + Torso aus. FP-Arms-Override aktiv. |
| TP | Volle Mesh-Sichtbarkeit. FP-Arms-Override inaktiv. |
| Transition | Interpolation über 0.3s — Visibility-Maske morpht, Kamera-Boom fährt zurück. |

**Visibility-Maske**: Per-Bone-Visibility über `SetBoneVisibility()` im Skeletal Mesh Component. Steuert zur Laufzeit, welche Körperteile gerendert werden. Vorteil: Ein Skelett, eine Animation-Instanz, kein doppelter Speicher.

**FP-Arms-Override**: LOD-Override für Hände und Unterarme mit eigenem Mesh-Segment (8–10k Tris). Wird nur in FP gerendert — höhere Detaildichte für die Nahansicht, eigene Materialinstanz mit feinerem Normal-Detail.

**Fallback**: Falls die Visibility-Maske Clip-Artefakte an Schulter-/Halspartie produziert (bekanntes Problem bei breiten FOVs), Wechsel auf Bethesda-Style Dual-Mesh: separates FP-Body-Mesh mit eigenem Skeleton, synchronisiert über `CopyPoseFromMesh`. Aufwand: ca. 2 Tage Implementierung, kostet ~15 MB RAM pro geladenen Charakter zusätzlich.

---

## 7.3 Character-Pipeline (MetaHuman-Hybrid)

### Shared Base Skeleton

Alle spielbaren und wichtigen NPCs teilen ein gemeinsames Skelett:

| Bereich | Joints | Anmerkung |
|---|---|---|
| Body | ~70 | Standard-Humanoid. Genug für IK-Chains + Twist-Bones. |
| Face | ~300 | MetaHuman-kompatibel. Für Lippensync + Emotionen. |
| **Gesamt** | **~370** | Einheitlich für Retargeting und Animation-Sharing. |

### Attachment-Sockets (7 Stück)

Fest definierte Sockets am Skelett für modulare Ausrüstung:

| Socket | Parent Bone | Zweck |
|---|---|---|
| `socket_shoulder_L` | `clavicle_l` | Schulterpanzer links |
| `socket_shoulder_R` | `clavicle_r` | Schulterpanzer rechts |
| `socket_back` | `spine_03` | Rucksack, Waffe (verstaut) |
| `socket_hip_L` | `pelvis` (Offset) | Schwert, Trank |
| `socket_hip_R` | `pelvis` (Offset) | Dolch, Beutel |
| `socket_helm` | `head` | Helm, Kopfschmuck |
| `socket_cloak` | `spine_03` (Offset) | Umhang-Attachment (Cloth-Sim-Root) |

### Fellträger-Erweiterung

Für nicht-menschliche Rassen (Fellträger) wird das Base Skeleton um Extension-Chains erweitert:

- **Ohren**: 3 Joints pro Seite (`ear_L_01/02/03`, `ear_R_01/02/03`) — genug für Sekundäranimation (Ohr-Zucken, Windreaktion)
- **Schnauze**: 2 Joints (`muzzle_01/02`) — für Lippensync-Erweiterung und Snarl-Expressions

**Fellträger-Kopf-Swap**: Der MetaHuman-Kopf wird durch ein Custom Mesh ersetzt, das auf dasselbe Rig gebunden ist. Face-Joints werden manuell auf die neue Topologie gewichtet.

**Aufwand**: 2–3 Tage pro Kopf-Typ (Modellierung, Retopologie, Skinning, Blendshape-Anpassung). Bei ~4 geplanten Fellträger-Varianten = ca. 2 Wochen Gesamtaufwand.

---

## 7.4 Slot-System (Modulare Rüstung)

### Slot-Übersicht

| Slot | Mesh-Typ | Anmerkung |
|---|---|---|
| Helm | Attached Mesh | Auf `socket_helm`, ersetzt Haar-Sichtbarkeit |
| Schulter | Attached Mesh (L/R) | Auf `socket_shoulder_L/R` |
| Brust | Modular Mesh | Body-Section-Override, Skeletal Mesh Merge |
| Rücken | Attached Mesh | Auf `socket_back` |
| Hüfte | Attached Mesh (L/R) | Auf `socket_hip_L/R` |
| Umhang | Cloth-Sim Mesh | Auf `socket_cloak`, Chaos Cloth |

### FFXIV-Prinzip: Fit-Varianten statt separater Assets

Keine separaten Rüstungsmodelle pro Rasse. Stattdessen: **Rüstungs-Fit-Varianten** als Morph Targets auf dem Basis-Rüstungsmesh.

- Mensch → Basis-Fit
- Fellträger → Morph Target für breitere Schultern, Kopföffnung, Schwanz-Cutout
- Weitere Rassen → weitere Morph Targets

**Vorteil**: Ein Asset, ein Material, ein LOD-Set. Nur die Morph-Target-Daten kommen pro Rasse dazu (~5–15% Speicher-Overhead statt 100% Duplikation).

### Layered Armor

Modulare Slots stacken visuell. Brust + Schulter + Umhang = sichtbares Komplett-Set. Clipping wird über Mesh-Masking und manuelle Anpassung der inneren Lagen minimiert — kein perfektes System, aber produktionsrealistisch.

---

## 7.5 LOD-System

### LOD-Stufen pro Charakter

| LOD | Tris | Distanz | Detail-Anmerkung |
|---|---|---|---|
| LOD0 | 65.000 | 0–5m | Volle Detailstufe. Alle Anatomie-Overlays aktiv. |
| LOD1 | 32.000 | 5–15m | Reduzierte Geometrie, aber genug UV-Dichte für Nervensystem-Adern als Textur. |
| LOD2 | 16.000 | 15–40m | Nervensystem nur noch als Emissive-Glow (kein Geometrie-Detail). Silhouette bleibt erhalten. |
| LOD3 | Billboard | 40m+ | Impostor-Sprite. Für Crowd-Shots und Fernansicht. |

### Constraints

- **Silhouetten-Erhalt bis LOD2**: Die Charaktersilhouette (Helm-Form, Schulterbreite, Umhang-Kontur) muss bis LOD2 lesbar bleiben. Das ist essenziell für Gameplay-Klarheit — der Spieler muss auf 40m erkennen können, ob er einem Krieger oder Magier gegenübersteht.
- **LOD-Transitions**: Dithered Transition über 2 Frames, kein harter Pop.
- **Nanite**: Wird für Umgebungsgeometrie genutzt, **nicht** für Charaktere (Nanite unterstützt kein Skeletal Mesh, Stand UE 5.4).

---

## 7.6 Master-Material-System

### Philosophie

**Ein parametrisches Master-Material für alle Charaktere und Rüstungen.** Inspiriert vom FFXIV-Materialansatz: maximale visuelle Vielfalt bei minimalem Asset-Aufwand. Jede Rüstung, jede Haut, jedes Gewebe ist eine Material-Instanz mit geänderten Parametern — kein eigenes Material.

### Basis-Layer

| Parameter | Typ | Funktion |
|---|---|---|
| `BaseColor` | Texture2D | Albedo |
| `Normal` | Texture2D | Oberflächen-Detail |
| `ORM` | Texture2D (Packed) | Occlusion (R), Roughness (G), Metallic (B) |
| `EmissiveColor` | LinearColor | Basis-Emissive-Farbe |
| `EmissiveIntensity` | Scalar | Emissive-Stärke |

### Fraktions-Farbmaske

**RGBA-Maske** als separate Textur. Jeder Kanal steuert eine Farbzone:

| Kanal | Zone | Beispiel |
|---|---|---|
| R | Primärfarbe | Wappenfarbe, Hauptstoff |
| G | Sekundärfarbe | Akzente, Bordüren |
| B | Tertiärfarbe | Leder, Metall-Tint |
| A | Sonderzone | Fraktions-Emblem, magische Markierungen |

Fraktionszugehörigkeit wird zur Laufzeit über einen `FactionColorSet`-Parameter (4x LinearColor) gesteuert. Einmal setzen, alle Slots aktualisieren sich.

### Anatomie-Overlay-Layer

Das Kernfeature des visuellen Stils — organische, lebendige Materialien statt totem Metall.

| System | Farbe | Animation | Technik |
|---|---|---|---|
| Herz-Kreislauf | Rot, pulsierend | Flowmap-Animation | UV-Scroll entlang vordefinierter Flowmap. Puls-Frequenz als Material-Parameter (Default: 72 BPM, skaliert mit Gameplay-State). |
| Muskel-Skelett | Blau, statisch | Kontraktions-Animation | Vertex-Color-Maske definiert Muskelgruppen. Kontraktion über World-Position-Offset entlang der Normalen (max. 0.5cm Displacement). |
| Lymphsystem | Grün, fließend | Flowmap-Animation | Ähnlich Herz-Kreislauf, aber langsamere Fließgeschwindigkeit und anderes Flowmap-Pattern. Subtiler — nur bei LOD0/LOD1 sichtbar. |

**Overlay-Blending**: Alle drei Systeme blenden über Masken-Texturen auf den Base-Layer. Jedes System hat einen eigenen `Visibility`-Parameter (0–1), steuerbar durch Gameplay-Systeme.

### Substance-Effect-Gruppe (Biotech-VFX)

Drogen, Gifte und biochemische Zustände als parametrische Material-Effekte:

| Substanz | Visueller Effekt | Technische Umsetzung |
|---|---|---|
| **Gift** | Adern werden grün-schwarz sichtbar, breiten sich vom Eintrittspunkt aus | Animierte Maske expandiert von UV-Koordinate des Treffers. Adern-Textur multipliziert mit Gift-Farbe. Parameter: `PoisonSpread` (0–1), `PoisonOriginUV` (Vector2). |
| **Amphetamine** | Puls-Speed erhöht, Adern leuchten heller | `PulseFrequency` wird von 72 auf 140+ BPM hochgefahren. `EmissiveIntensity` der Herz-Kreislauf-Schicht skaliert mit. |
| **Drogen** | Normal-Map-Verzerrung, leichtes „Atmen" der Oberfläche | Sinuswellen-Offset auf Normal-Map-UV. Frequenz und Amplitude als Parameter. Subtil genug für Unbehagen, nicht genug für Motion Sickness. |

**Alles über Material-Instanzen**: Kein Substanz-Effekt erfordert ein eigenes Material. Ein `SubstanceState`-Struct wird pro Frame an die Material-Instanz übergeben. Die Shader-Logik ist statisch kompiliert — nur die Parameter ändern sich.

---

## 7.7 Biotech-VFX-Philosophie

### Shader-lastig statt Particle-lastig

Bewusste Designentscheidung: Die visuellen Effekte der Welt sind **material-getrieben**, nicht partikelgetrieben.

| Ansatz | Einsatz | Begründung |
|---|---|---|
| Material-Parameter-Drives | 80% der VFX | GPU-seitig, skaliert besser, kein Overdraw-Problem. Pulsende Adern, leuchtende Muster, Oberflächen-Mutationen — alles Shader-Arbeit. |
| Niagara Particle System | 20% der VFX | Nur für physikalisch losgelöste Effekte: Blutspritzer, Sporen, Rauch, Funken. Minimaler Einsatz. |

**Warum**: Steampunk-Ästhetik lebt von Partikeln (Dampf, Zahnräder, Funken). Biotech-Ästhetik lebt von **Oberflächen-Transformation** — Adern, die pulsieren, Haut, die mutiert, Rüstung, die atmet. Das ist inherent Shader-Arbeit. Wir spielen zur Stärke des Stils.

**Performance-Gewinn**: Material-Parameter-Änderungen sind quasi kostenlos (Uniform-Update). Partikel kosten Simulation + Overdraw + Sortierung. Bei 20+ Charakteren im Bild summiert sich das.

---

## 7.8 Terrain & Welt

### Scope

**Eine Insel.** Keine Open-World-Illusion mit unsichtbaren Wänden. Eine physisch begrenzte, dafür dichte Spielwelt.

### Generierungspipeline

| Bereich | Methode | Tool | Begründung |
|---|---|---|---|
| Großlandschaften | Prozedural | Houdini → UE5 (Houdini Engine Plugin) + PCG Framework | Terrain-Heightmaps, Felsformationen, Vegetationsverteilung. Iteration in Minuten statt Tagen. |
| Siedlungen | Handgebaut | UE5 Level Editor + Modular Kit | Gameplay-Räume brauchen intentionales Design. Jeder Raum hat eine Funktion. |
| Dungeons | Handgebaut | UE5 Level Editor + Modular Kit | Encounter-Design, Sightlines, Pacing — nicht prozedural lösbar. |
| Übergangszonen | Hybrid | Houdini-Basis + manuelle Anpassung | Waldränder, Küstenlinien, Pfade zwischen Siedlungen. |

### World Partition

UE5 World Partition für Streaming. Die Insel wird in Zellen unterteilt (~200m × 200m), On-Demand geladen. Keine manuellen Level-Transitions — der Spieler bewegt sich nahtlos.

### PCG-Regeln (Houdini)

- Vegetations-Density nach Höhe + Neigung + Distanz zu Wasser
- Fels-Placement nach geologischen Schichtregeln (nicht random scatter)
- Pfad-Erosion: Houdini-Sim für natürlich wirkende Trampelpfade
- Export: Heightmap (16-bit), Splatmap (8 Layer), Foliage-Instanzen als CSV → UE5-Import über Custom Python-Bridge

---

## 7.9 Performance-Budget (Zielwerte)

| Ressource | Budget pro Frame | Anmerkung |
|---|---|---|
| Draw Calls | ≤ 2.000 | Nanite reduziert Umgebungs-Draws drastisch |
| Tris on Screen | ≤ 5M | Nanite-managed für Umgebung, LOD-managed für Charaktere |
| VRAM | ≤ 6 GB | Für RTX 4060 Ziel-GPU |
| RAM | ≤ 12 GB | Inkl. Streaming-Budget |
| Charakter-Budget (sichtbar) | ≤ 30 gleichzeitig | LOD3-Billboards darüber hinaus |
| Material-Instanzen (unique, geladen) | ≤ 200 | Durch Master-Material-Ansatz realistisch |

---

## 7.10 Offene Fragen & Risiken

| Risiko | Schwere | Mitigation |
|---|---|---|
| Visibility-Maske-Artefakte bei FP-Kamera | Mittel | Fallback auf Dual-Mesh dokumentiert. Frühzeitig prototypen. |
| MetaHuman Face-Rig-Performance bei 30+ NPCs | Hoch | Face-LOD: Vereinfachtes Rig ab LOD1. Lippensync nur für Sprecher im Fokus. |
| Fellträger-Kopf-Swap bricht MetaHuman-Updates | Mittel | Custom Heads als eigenes Asset, nicht als MetaHuman-Modifikation. Rig-Kompatibilität über Interface-Joints sicherstellen. |
| Substance-Effects + Anatomie-Overlays = Shader-Komplexität | Hoch | Instruction-Count im Master-Material monitoren. Feature-Switches für Low-End. Quality-Presets. |
| Cloth-Sim (Umhang) bei vielen Charakteren | Mittel | Cloth-Sim nur für Spieler + 3 nächste NPCs. Rest: baked Animation. |

