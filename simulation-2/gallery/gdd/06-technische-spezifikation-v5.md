# GDD Kapitel 6: Technische Spezifikation & Produktion

**RELICS: Schwellenanker**
**Version**: 5.0 — Tag 5, Freitag, 10:00 Uhr
**Status**: Finalisierung — v5 (Seitenbudget-Kürzung, Bilder, Siegel-Rename)

<!-- Tobi: v5-Änderungen gegenüber v4: (1) 6.7 Tiervolk-Symbiose-Shader auf ein Drittel gekürzt — nur Dual-Layer-Konzept, Abgrenzungstabelle, Asset-Konvention. Pipeline-Details (Layer-Einzelbeschreibungen, Blend-Maske-Hypothesen, Aufwandsschätzung, Animations-Verknüpfung) in Pipeline-Bibel ausgelagert. (2) 6.4.2–6.4.5 Schattenfieber-PP-Stufen: konkrete Parameter-Werte in HTML-Kommentare verschoben, Stufen-Logik/Konzept bleibt sichtbar. (3) 6.10.2 Pre-Alpha-Timeline komplett entfernt — Produktionsplanung, nicht GDD. (4) Redundante Inline-Erklärungen gestrafft. (5) "Orden-Kreuz" → "Orden-Siegel" in 6.12. (6) Bilder eingebaut: Schwellenanker drei Zustände und Hero-Shot bei 6.6. (7) Keine neuen Inhalte. -->

<!-- Tobi: Verfasser Kap. 6: Tobias Richter, Technical Artist. v1: Tag 2. v2: Tag 3 Briefing. v3: Tag 3 WORK. v4: Tag 4 WORK. v5: Tag 5 WORK (Finalisierung). -->

---

> **Anmerkung zur Dokumentstruktur**
> Dieses Kapitel ist die technische Antwort auf das kreative Briefing. Jede Entscheidung hier hat einen Grund — und den schreibe ich dazu.

---

## 6.1 Engine & Technologiebasis

### 6.1.1 Unreal Engine 5 — Begründung

RELICS wird in **Unreal Engine 5** entwickelt. Das Kernszenario — eine vertikal geschichtete Stadt mit extremer Geometriedichte, biolumineszenten Materialien, dynamischer Globalbeleuchtung und einem Post-Process-System, das die Spielwahrnehmung schrittweise deformiert — erfordert eine Kombination aus Nanite, Lumen und World Partition. Kein anderes aktuell verfügbares System bietet alle drei in Integration.

**Engine-Version**: UE5.4 LTS. Kein Upgrade während der Alpha-Phase.

**Ziel-Plattform (primär)**: Windows PC (DirectX 12)
**Ziel-Plattform (sekundär)**: PlayStation 5, Xbox Series X (nach Full-Release evaluiert)

**Hardware-Mindestanforderungen (PC, Zielzustand):**
| Stufe | GPU | RAM | Einstellung |
|---|---|---|---|
| Minimum | NVIDIA RTX 2070 / AMD RX 6700 XT | 16 GB | Lumen Software RT, mittlere Qualität |
| Empfohlen | NVIDIA RTX 3080 / AMD RX 7900 XT | 32 GB | Lumen Hardware RT, hohe Qualität |
| Ultra | NVIDIA RTX 4080 / AMD RX 7900 XTX | 32 GB | Full Hardware RT, maximale Qualität |

---

### 6.1.2 Kernkomponenten der Engine

**Nanite** — Virtualisierte Geometrie

Nanite ist für die gesamte statische Architekturgeometrie aktiviert. Die Materiallesbarkeit der Welt — Zunftzeichen-Reliefs, Titan-Legierung-Oberflächendetail, Knochen-Schnitzereien der Unterschicht — funktioniert nur mit Nanite-Detailauflösung. Einsparung gegenüber traditioneller Pipeline: 40–60% des Modellierungs-Aufwands.

*Bekannte Schwächen und Kompensation:*
- **Dünne Geometrien** (Ketten, Gitterstäbe, Pflanzenstiele, Stoff-Überhänge): traditionelle LODs und Imposter-Billboards ab Distanzklasse 3.
- **Wasser, Transluzenz**: Nanite unterstützt keine transluzenten Materialien. Alle Wasseroberflächen und Glas-Elemente sind non-Nanite mit eigenem LOD-Setup.
- **Moving Meshes**: Kampf-Props mit Destruction-Proxy als Nanite-Fallback-Mesh.

---

**Lumen** — Dynamische Globalbeleuchtung und Reflexionen

Lumen ist das wichtigste und gleichzeitig riskanteste System im Projekt. Eine biolumineszente Stadt mit Runtime-Zustandswechseln — Schwellenanker-Aktivierung, Schattenfieber-Eskalation, Klasse-A-Emitter — braucht echte dynamische GI. Statisches Baked Lighting wäre optisch inkonsistent.

*Lumen-Konfiguration nach Stadtschicht:*

| Schicht | Modus | Begründung |
|---|---|---|
| **Layer 3** (Türme, Gilden-Hochbau) | Hardware Raytracing | Offener Himmel, Bergkristall-Linsen-Reflektionen |
| **Layer 2** (Brücken, Arkaden) | Hardware Raytracing | Buntglas-Farbflecken, Metall-Intarsien-Reflexionen |
| **Layer 1** (Straßenebene) | Software Raytracing (hohe Qualität) | Kerzenlicht-Atmosphäre, Budget-schonend |
| **Layer 0** (Untergrund, Kanäle) | Software RT + Hybrid Baked | Lumen degeneriert ohne Himmelssicht — Baked Irradiance für statische Bereiche |

<!-- Tobi: Lumen-Tuning-Parameter für Pipeline-Bibel: r.Lumen.ScreenProbeGather.ScreenSpaceBentNormal 1, r.Lumen.Reflections.MaxRoughnessToTrace 0.4, r.Lumen.DiffuseIndirect.Allow 1. Lumen-Importance-Volumes manuell in Gildenhallen, Ordenskorridoren, Ratsräumen. -->

*Lumen-Emitter-Klassifizierung* (→ detailliert in 6.3.2):
- Klasse A: echte GI-Emitter (wenige, hero lights)
- Klasse B: visuell emissiv, kein GI-Beitrag
- Klasse C: Niagara-Partikel-Glow

---

**World Partition** — Streaming und vertikale Architektur

UE5 World Partition ist horizontal konzipiert. Die vertikale Stadtstruktur von RELICS (vier Schichten auf der Z-Achse) erfordert manuelle Data Layers als vertikale Strukturierung.

| Layer | Inhalt | Lichtstimmung | Schattenfieber-Ambience |
|---|---|---|---|
| **Layer 0** | Untergrund, Kanal-System, Slum-Keller | Phosphoreszierendes Blau-Grün, vereinzelt Feuerschein | Hoch |
| **Layer 1** | Straßenebene, Handwerkerviertel, Marktplätze | Warmes Kerzenlicht, Buntglas-Farbflecken | Mittel |
| **Layer 2** | Brücken, Arkaden, niederer Gilden-Bereich | Diffuses Tageslicht durch Bergkristall-Linsen | Niedrig |
| **Layer 3** | Türme, Gildenhochbau, Ordensanlagen, Kronenpalast | Klares Tageslicht, Metallic-Reflektionen | Minimal |

*Technische Implementierung:*
- Jeder Data Layer ist eine eigenständige Streaming-Einheit mit eigenem Post-Process-Volume-Stack
- Manuelle Occlusion-Volumes an allen Schicht-Übergängen
- Ebenen-Übergänge (Treppen, Lifte, Schächte): beide angrenzenden Layer gleichzeitig geladen für 60m Radius
- **Schichtgrenzen**: oben fließend (Blend-Volumes), unten diskret (harte Data-Layer-Cuts)
- **Tiervolk-Siedlungen**: statisch, an festen kosmologisch dünnen Orten. Ambient-Werte Layer-gebunden.

<!-- Tobi: Vera-Abstimmung zu Schichtgrenzen erledigt (Tag 2). Emre-Abstimmung zu Tiervolk-Siedlungen erledigt (Tag 4): statisch → World Partition bleibt Layer-gebunden, keine Dynamik-Komplexität. -->

---

## 6.2 Kamerasystem

### 6.2.1 Third/First Person — nahtloser Übergang

Der Übergang zwischen Third und First Person muss nahtlos sein — kein Ladebildschirm, kein sichtbarer Kamera-Swap. Eine einzige Camera-Component, zwei Offset-Zustände, interpoliert.

- **Third-Person-Position**: 200 cm hinter dem Charakter, 80 cm über der Schulter
- **First-Person-Position**: Exakte Head-Socket-Koordinate
- **Blend-Dauer**: 0.3 Sekunden, Ease-In/Out-Kurve
- **Context-Trigger**: Enge Gänge lösen optionalen Auto-Wechsel aus

**FOV-Konfiguration:**
| Modus | Standard-FOV | Spieler-Range |
|---|---|---|
| Third Person | 90° | 75° – 100° |
| First Person | 95° | 80° – 110° |
| Vertikaler Raum (z.B. Turm-Inneres) | +5° automatisch | — |

---

### 6.2.2 Cinematik-Modus (Sequencer)

Für Cutscenes, Dialoge und Schwellenanker-Aktivierungs-Sequenzen: **UE5 Sequencer** mit separaten Kamera-Akteuren.

- DOF: echtes Bokeh-DOF im Cinematic-Modus
- **Kamera-Führungsprinzip**: Statische Langzeiteinstellungen, langsame Zooms. Die Kamera ruht — die Welt bewegt sich in ihr.

<!-- Tobi: Tarkowski als Einfluss für Kamerastil. Im Fließtext kein Autorname. -->

---

## 6.3 Rendering-Pipeline: Materialien & Biolumineszenz

### 6.3.1 Material-Philosophie

Jedes Material in RELICS muss auf drei Ebenen funktionieren:
1. **Materiallesbarkeit** — sozialer Status des Trägers/Besitzers erkennbar
2. **Physikalische Plausibilität** — PBR-Werte innerhalb physikalischer Grenzen
3. **Performance-Budget** — definiertes Instruction-Count-Limit pro Material

**Material-Hierarchie nach sozialer Schicht:**

| Schicht | Materialklasse | Roughness-Range | Metallic | Besonderheit |
|---|---|---|---|---|
| Oberschicht | High-Fidelity PBR | 0.05 – 0.25 | Ja (Titan, Edelstahl, Gold) | Clearcoat-Layer, Emissive optional |
| Mittelschicht | Standard PBR | 0.3 – 0.6 | Partiell (Bronze, Silber) | Malachit-Einlagen via Masked-Layer |
| Unterschicht | Dirty/Layered PBR | 0.6 – 0.95 | Selten | Wear-Maps, Schmutz-Parameter |

---

### 6.3.2 Biolumineszenz — Dreiklassen-System

Biolumineszenz ist das Neon-Äquivalent dieser Welt. Technisches Problem: viele Emitter = Performance-Kollaps. Lösung: striktes Klassifizierungssystem.

| Klasse | Funktion | Lumen-GI | Budget | Beispiele |
|---|---|---|---|---|
| **A — Hero Lights** | Echte GI-Emitter | Ja | Max. 8–12 gleichzeitig sichtbar | Bergkristall-Linsen, Schwellenanker (aktiv), Tiervolk-Emissive (aktiv) |
| **B — Ambient Glow** | Visuell emissiv | Nein | Unbegrenzt | Phosphoreszierende Patches, Alchemie-Phiolen, Tiervolk-Ruhezustand |
| **C — Particle Glow** | Niagara-Partikel | Nein | GPU-skalierbar | Pilz-Cluster, Kanal-Algen, Schattenfieber-Pusteln |

*Dokumentationspflicht*: Jeder Klasse-A-Emitter wird in einer Scene-Light-Bible dokumentiert.

---

## 6.4 Schattenfieber — Post-Processing-System

### 6.4.1 Systemarchitektur

Das Schattenfieber-PP-System bildet drei Stufen mit smoothem Übergang ab. Alle Parameter sind Blueprint-seitig steuerbar.

**Blueprint-Architektur:**

```
BP_Schattenfieber
├── Timeline-Komponente (Float-Kurve, 0.0 – 3.0 = Stufe-Werte)
├── PostProcessComponent (Stack)
│   ├── PP_Stage_0 (Base — immer aktiv)
│   ├── PP_Stage_1 (Blend-Weight 0→1 bei 0.0–1.0)
│   ├── PP_Stage_2 (Blend-Weight 0→1 bei 1.0–2.0)
│   └── PP_Stage_3 (Blend-Weight 0→1 bei 2.0–3.0)
├── ScalarParameter: "ShadowFever_Intensity" (0.0 – 3.0)
├── Event: OnStageThresholdReached (1.0 / 2.0 / 3.0)
└── Accessibility-Override: "DisableVertexAnimation" (Bool)
```

**Übergänge**: Immer geblended über die Timeline-Kurve. Kein Hard-Switch. Minimum-Blend-Zeit: 2 Sekunden pro Stufe.

---

### 6.4.2 Stufe 0 — Basis (kein Schattenfieber)

Normaler Spielzustand. ACES-Tonemapping mit leicht kühlen Schattenbereichen — latente Kälte schon im Normalzustand. Technische Narratologie.

<!-- Tobi: Parameter Stufe 0 — Color Grading: Shadow Gain RGB 0.95/0.95/1.02. Film Grain: 0.2 Intensität, 1.0 Körnung. Bloom: Schwellwert 1.2. TAA-Schärfe-Boost 0.2. -->

---

### 6.4.3 Stufe 1 — Frühinfiltration (sensorisch, subtil)

Der Spieler soll unsicher sein, ob er etwas sieht. Minimale Chromatic Aberration am Rand, leichter Cyan-Bloom-Tint, feineres Film Grain, Vignette. Optisches Echo — das Bild "klingt nach".

<!-- Tobi: Parameter Stufe 1 — Chromatic Aberration: Rand +0.4px, zentral 0. Bloom-Tint RGB-Multiplikator: 0.95/1.0/1.05. Film Grain: 0.45, Körnung 0.7. Shadow Gain +0.05 Blaukanal. Vignette: 0.15. -->

---

### 6.4.4 Stufe 2 — Mutative Phase (eindeutig, riskant)

Ab hier ist das Schattenfieber bewusst spürbar. Pulsierende Chromatic Aberration, Nahbereichs-DOF, Indigo-Verschiebung in Schattenbereichen, Vertex-Animation an organischen Umgebungsobjekten (±1.5 cm, 15m Radius).

**Accessibility-Option (Pflicht)**: "Schattenfieber-Bewegungseffekte reduzieren" — deaktiviert Vertex-Animation und DOF-Pulsieren, reduziert Vignette auf statisch. Dokumentation im Spielhandbuch obligatorisch.

<!-- Tobi: Parameter Stufe 2 — Chromatic Aberration: 0.8px, Oszillation 0.5 Hz Sinus. Vignette: 0.35, pulsierend 0.25 Hz, Amplitude 0.1. DOF Focal Length 400cm, F-Stop 1.8. Color Grading: Shadow-Midpoint RGB -0.03/-0.03/+0.08. Vertex-Animation: 0.3–0.8 Hz. -->

---

### 6.4.5 Stufe 3 — Auflösung (Grenze zur anderen Seite)

Das einzige Übernatürliche im Spiel. Full-Screen-Overlay (`M_Schattenfieber_Overlay`) mit organischen Rissstrukturen, Geometrie-Lücken via Custom Stencil Buffer, starker Indigo-Bloom, chaotische Chromatic Aberration. Nervensystem-Visualisierung startet automatisch (→ 6.5).

**Verbindung Schwellenanker**: Der kritische Schwellenanker-Zustand (→ 6.6) nutzt dasselbe visuelle Vokabular — Rissstrukturen, Innen-Leuchten, Indigo-Tönung. Intentionale Ambiguität.

*Accessibility-Option*: Geometrie-Lücken deaktivierbar, Overlay-Intensität reduzierbar.

<!-- Tobi: Parameter Stufe 3 — Bloom-Radius 8.0, Indigo/Violett. Chromatic Aberration: 1.5px, Rauschwert statt Sinus. Overlay-Reduktionswert: 0.6. -->

---

### 6.4.6 Schattenfieber-Ambient (Layer-gebunden)

Unabhängig vom Spieler-Infektionslevel haben die Data Layers eine Baseline Schattenfieber-Ambience:

| Layer | Ambient-Wert | Begründung |
|---|---|---|
| Layer 0 (Untergrund) | 0.15 | Die Schwelle ist hier dünn |
| Layer 1 (Straße) | 0.05 | Schwach spürbar |
| Layer 2 (Arkaden) | 0.0 | — |
| Layer 3 (Türme) | 0.0 | — |

Der Ambient-Wert addiert auf den Spieler-Wert. Die Architektur erzählt die Kosmologie.

---

### 6.4.7 Interface-Spezifikation: Lymph-Subsystem → PP-Trigger

<!-- Tobi: Vollständige Blueprint-Interface-Definition. Gesetzt in v3, Tag 3. -->

Das Lymph-Subsystem (Gameplay) und das Schattenfieber-PP-System (Tech-Art) kommunizieren über ein klar definiertes Blueprint-Interface. Das Gameplay-System schreibt `ShadowFever_Intensity`. Das PP-System feuert Events zurück. Keine Gegenrichtungs-Abhängigkeit.

```
Gameplay-Seite (Darius):          Tech-Art-Seite:
BP_LymphSubsystem                 BP_Schattenfieber
    │                                     │
    │── schreibt ──►  ShadowFever_Intensity (0.0–3.0)
    │                                     │
    │◄── liest ──────  OnStageThresholdReached(float Stage)
    │
    └── schreibt ──►  ShadowFever_Ambient (addiert, Layer-gebunden, READ ONLY für Gameplay)
```

**Mapping Lymph-Stufe → PP-Stufe:**

| Lymph-Stufe | ShadowFever_Intensity | PP-Stufe | Spielerlebnis |
|---|---|---|---|
| Untrained | 0.0 – 0.2 | Stufe 0 | Kein sichtbares Fieber |
| Geübt | 0.2 – 0.8 | Stufe 0 → 1 (gleitend) | Peripherie-Rauschen |
| Fortgeschritten | 0.8 – 1.8 | Stufe 1 → 2 (gleitend) | Eindeutige Symptome |
| Meister | 1.8 – 3.0 | Stufe 2 → 3 (gleitend) | Auflösung, Schwellen-Erfahrung |

**Wert-Zusammensetzung:**
```
ShadowFever_Intensity = Lymph_BaseValue + Exposure_Delta + ShadowFever_Ambient
```

<!-- Tobi: Exposure_Delta ist ein Vorschlag — Darius entscheidet. Das PP-System braucht nur den finalen kombinierten Float. -->

**Interface-Funktionen:**

| Funktion | Signatur | Richtung |
|---|---|---|
| Intensität setzen | `SetShadowFeverIntensity(float Value)` — geclampt [0.0, 3.0] | Gameplay → PP |
| Stufen-Event | `OnStageThresholdReached(float Stage)` — Werte 1.0 / 2.0 / 3.0 | PP → Gameplay |
| Abfrage | `GetCurrentShadowFeverStage()` — read-only | PP → Gameplay |
| Fraktions-Preset (optional) | `SetFactionPPPreset(EFaction)` — Krone / Gilden / Orden | Gameplay → PP |

<!-- Tobi: Fraktions-PP-Presets sind optionaler Vorschlag — Nami muss bestätigen. Kein gesetztes Feature. -->

---

## 6.5 Nervensystem-Visualisierung

### 6.5.1 Konzept und Umsetzung

Das Leveling-System nutzt eine halbtransparente Nervensystem-Sicht. Drei Subsysteme — Cardio, Muskel, Lymph — werden als Overlay auf den Charakter-Körper projiziert.

**Modi:**
1. **Statistik-Ansicht** (Menü): Vollbild-Overlay, alle drei Systeme sichtbar, interaktiv
2. **Echtzeit-Overlay** (kontextabhängig): aktiv in Stufe 3 Schattenfieber, nach schweren Verletzungen, optional permanent

**Technische Umsetzung:**
- **Third-Person**: Overlay via Custom-Depth-Pass. Drei Materialschichten (Cardio = warmrot, Muskel = bernsteingelb, Lymph = kühles Grün-Weiß) mit Emissive-Kanal. Fortschritt sichtbar als Textur-Dichte und Emissive-Intensität.
- **First-Person**: Separates Arm-Mesh-Set (`SK_FP_Arms`), synchron animiert via Animation-Blueprint. Aufwand: 3 Wochen.

**Shader-Struktur (M_Nervensystem_Base):**
```
Inputs:
  - BaseColor: Charakter-Skin
  - NervensystemMask_Cardio (R), _Muskel (G), _Lymph (B)
  - Fortschritt_Cardio / _Muskel / _Lymph (Scalar 0–1)
  - Overlay_Opacity (Scalar 0–1)
Outputs:
  - Emissive: Farb-kodiertes Nervensystem-Leuchten
  - Custom Depth: für Compositing-Pass
```

---

## 6.6 Schwellenanker-Shader — Master Material System

<!-- Tobi: Asset-Namen: M_Schwellenanker_Master, MI_Schwellenanker_Dormant, MI_Schwellenanker_Resonant, MI_Schwellenanker_Critical, T_Schwellenanker_Riss_01, BP_Schwellenanker. -->

### 6.6.1 Konzept

Der Schwellenanker existiert als ein einziges Mesh mit einem Master-Material und drei Material-Instanzen. Übergänge sind immer geblended, nie hart. **Zur Form**: eine gefaltete, komprimierte, verknöchert-mineralische Formation (Vera, Tag 3).

![Schwellenanker — Drei Zustände: ruhend, resonant, kritisch. Concept Art: Vera Lindström / Nano Banana Pro.](../../pinwall/favorites/relikt-drei-zustaende-v2_nano-banana-pro.png)

---

### 6.6.2 Drei Zustände

![Schwellenanker im resonanten Zustand in situ. Concept Art: Vera Lindström / Nano Banana Pro.](../../pinwall/favorites/relikt-hero-v2_nano-banana-pro.png)

**Zustand 1 — Ruhezustand (dormant):**
Subsurface Scattering aktiv (warme Untertöne, mineralisch komprimierter Radius). Keine Emission. Das SSS erzeugt innere Lebendigkeit — etwas ist da, schläft aber.

**Zustand 2 — Aktiver Zustand (resonant):**
Emissive-Layer aktiviert (warmes Indigo-Weiß), Lumen-Emitter Klasse A. Sofort als Lichtquelle erkennbar — wichtigste dynamische Lichtquelle in jeder Szene, in der er aktiv ist.

**Zustand 3 — Kritischer Zustand (überlastet):**
Riss-Overlay öffnet sich stufenlos (`T_Schwellenanker_Riss_01`), Innenleuchten an Riss-Kanten (kalt-violett), flackernder Lumen-Emitter. Visuelles Vokabular entspricht PP-Stufe 3 — der Schwellenanker und das Schattenfieber sprechen dieselbe Sprache. Riss-Blend-Parameter erlaubt sequenzielles Aufziehen für Act 3.

<!-- Tobi: Namis "ein Anker kann reißen" (Tag 3) ist angelegt. Kein neuer Shader-Aufwand — nur Blueprint-Kurven-Authoring. -->
<!-- Tobi: Vera hat Form auf "folded geological formation, compressed ossified mineral cluster" spezifiziert (Tag 3). SSS-Radius und Riss-Topologie entsprechend kalibriert. -->
<!-- Tobi: Detaillierte Shader-Parameter (SSS-Farbe, Radius, Emissive-Intensitäten, Flicker-Frequenzen, Vertex-Animation) → Pipeline-Bibel. -->

---

### 6.6.3 Master-Material-Struktur (M_Schwellenanker_Master)

```
Parameter-Gruppen:
  [Base]        Roughness (Scalar), BaseColor (Vector)
  [SSS]         SSS_Enabled, SSS_Color, SSS_Radius, SSS_Intensity
  [Emissive]    Emissive_Enabled, Emissive_Color, Emissive_Intensity,
                Emissive_Flicker, Emissive_FlickerFrequency
  [Riss]        Riss_Enabled, Riss_Mask (Texture2D),
                Riss_BlendAmount (0–1), Riss_EmissiveBoost
  [State_Blend] State_Alpha (0–2.0)
                -- 0.0 = Zustand 1, 1.0 = Zustand 2, 2.0 = Zustand 3
```

**Drei Material-Instanzen**: `MI_Schwellenanker_Dormant`, `MI_Schwellenanker_Resonant`, `MI_Schwellenanker_Critical` — alle vom selben Master. Blueprint interpoliert über `State_Alpha`.

---

## 6.7 Tiervolk-Symbiose-Shader

<!-- Tobi: v5 massiv gekürzt. Layer-Detailbeschreibungen, Blend-Maske-Hypothesen, Aufwandsschätzung, Animations-Details → Pipeline-Bibel. Hier nur Konzept, Abgrenzung, Asset-Konvention. -->

### 6.7.1 Konzept und Abgrenzung

Das Tiervolk ist dauerhaft, kosmologisch anders — keine Infektion, keine Mutation, sondern ontologischer Normalzustand. Die Symbiose zwischen tierischem Wirt und dem Fremden erfordert eine eigenständige Materialklasse.

**Abgrenzung zu verwandten Systemen:**

| System | Zustand | Natur | Shader-Basis |
|---|---|---|---|
| Schattenfieber | Infektion, prozessual | pathologisch | PP-Blueprint + Overlay |
| Schwellenanker | Instrument, drei Zustände | kosmologisch | M_Schwellenanker_Master |
| Tiervolk-Symbiose | Dauerhafter Normalzustand | ontologisch fremd | M_Tiervolk_Symbiose_Master |

Alle drei Systeme teilen dasselbe visuelle Vokabular (kalt, transluzent, von innen leuchtend) — weil sie denselben kosmologischen Ursprung haben. Technisch getrennte Systeme. Das ist Absicht.

### 6.7.2 Dual-Layer-Architektur

Ein **Dual-Layer-System** in einem einzigen Master-Material:

- **Layer 1 — Tier-Biologie**: SSS, Mikrooberfläche, organische Textur-Variation. Das tierische Substrat — Fell, Schuppe, Knochen.
- **Layer 2 — Das Fremde**: Emissive-Maske, transluzentes Durchleuchten von innen. Kühl, leicht violett-weiß — dieselbe kosmologische Farbtemperatur wie Schwellenanker-Resonanz und Schattenfieber Stufe 3.
- **Blend-Maske** (`Symbiose_Mask`): bestimmt pro Charakter, wo sich das Fremde angesammelt hat. Parametrisiert im Master-Material.

**Zwei Zustände** (kein Float — das Tiervolk hat keine Progression):
- **Ruhig**: Pulsiert langsam, Klasse B (kein GI-Overhead)
- **Aktiv** (Bedrohung, Ritual): Emissive-Intensität erhöht, Klasse A, Pulsfrequenz steigt

### 6.7.3 Asset-Konvention

| Typ | Namens-Schema | Beispiel |
|---|---|---|
| Master-Material | `M_Tiervolk_Symbiose_Master` | — |
| Material-Instanz | `MI_TV_{TierTyp}_{Zustand}` | `MI_TV_Wolf_Ruhig` |
| Symbiose-Maske | `T_TV_{CharName}_Symbiose_Mask` | `T_TV_Salva_Symbiose_Mask` |
| Blueprint-Controller | `BP_Tiervolk_Symbiose_Controller` | — |
| Interface | `SetTiervolkSymbioseState(ETiervolkState)` | `Ruhig` / `Aktiv` |

<!-- Tobi: Instanz-Anzahl und Tier-Typen nicht final — abhängig von Emre/Vera. Detaillierte Layer-Parameter, Blend-Maske-Muster, Aufwandsschätzung (3–4 Wochen), PCG-Crowd-Varianten → Pipeline-Bibel. -->

---

## 6.8 Houdini-Pipeline — Terrain und Prozedurale Systeme

### 6.8.1 Terrain-Generierung

**Workflow:**
1. Basis-Terrain in **Houdini** procedural generiert (Heightfield-System)
2. Export als `.hdr`-Heightmap nach UE5 (16-bit, 4096x4096 für Kernregion)
3. In UE5: Landscape-System mit Nanite-Tessellation für Nahbereich
4. Automatisches Foliage-Placement via PCG

**Houdini-Setup**: Hydraulische Erosion, Stadtplattform-Sculpting via Kontrollkurven, Heightfield-Vexnet für Flussbettgenerierung. Auflösungen: 4k Kern (2km Radius), 2k äußere Bereiche (10km Radius).

<!-- Tobi: Houdini-Terrain wartet auf Emres Topos-Kapitel (Stadtname, Sichtachsen, Gebirgs-Kontext). -->

---

### 6.8.2 Prozedurale Stadtdetails (PCG-Systeme)

PCG-Systeme für wiederholende Stadtdetails:

- **Pflaster-Variation**: Stein-Typ, Rotation, Abnutzungsgrad nach Schicht-Tiefe
- **Fassaden-Ageing**: prozedurale Wear-Maps (Houdini → PCG)
- **Biolumineszenz-Cluster**: Niagara via PCG in Layer-0-Bereichen
- **Vegetation-Infiltration**: prozedurale Pflanzen-Cluster in Slum-Bereichen

---

## 6.9 Color Science & Display-Pipeline

### 6.9.1 Color-Management

RELICS nutzt **ACES** (Academy Color Encoding System). Pipeline: ACEScg Arbeitsraum → ACES Tonemapping → Display-Transform (sRGB/DCI-P3).

- Alle Texturen in sRGB gespeichert, im Shader linear konvertiert
- Emissive-Werte in physikalischen Einheiten (cd/m²)
- Basis-LUT für den RELICS-Look, drei Varianten (Normal / Stufe 2 / Stufe 3)

**Warum kein AgX?** AgX komprimiert Highlights zu weich. Bergkristall-Linsen und Schwellenanker müssen leuchten, nicht weich werden. ACES gibt uns das.

### 6.9.2 Display-Kalibrierung

Alle Arbeitsstationen kalibriert (Delta-E < 2.0). Emissive-Werte auf Standard-SDR (sRGB, 200 cd/m² Peak) kalibriert. HDR-Displays: separater Display-Transform.

---

## 6.10 Produktion & Release-Pipeline

### 6.10.1 Milestone-Übersicht

| Milestone | Technischer Status | Schlüssel-Deliverables |
|---|---|---|
| **Pre-Alpha** | Prototyp-Pipeline | Rendering-Architektur, Material-Master-Systeme, World Partition stabil |
| **Alpha** (Streamer) | Feature-Freeze Rendering | Data Layers gesetzt, Lumen fixiert, PP-System stabil, alle Shader-Master stabil |
| **Beta** | Tuning-Phase | Performance-Optimierung, visuelle Feinheit, Accessibility vollständig |
| **Full Release** | Feinschliff + Setpieces | Abschließender Lighting-Pass, Cinematic-Sequenzen final |
| **DLC** | Erweiterung auf stabiler Basis | Neue Assets auf bestehenden Systemen — kein neues technisches Risiko |

**Alpha ist der härteste Freeze.** Nach Alpha-Abgabe nicht mehr änderbar:
- Data Layer-Struktur (Schichtanzahl, Naming, Streaming-Logik)
- Lumen-Konfiguration (RT-Modus pro Layer)
- Schattenfieber-PP-System-Architektur (Blueprint-Struktur, Parameter-Namen)
- Schwellenanker- und Tiervolk-Symbiose-Master-Material-Strukturen
- Kamerasystem-Grundstruktur
- Interface-Spezifikationen (Lymph → PP-Trigger, Tiervolk → Gameplay)

---

### 6.10.2 Monetarisierung — Technische Implikation

**Klassisch Premium, keine Mikrotransaktionen.** Offline-first, Save-Game lokal, kein Always-Online. DLC als Pak-Files. Kein Platzhalter für DLC im Basis-Spiel.

---

## 6.11 Risiko-Register

| System | Priorität | Risiko | Mitigation |
|---|---|---|---|
| Lumen vertikale GI | HOCH | Degeneriert in tiefen Kanälen | Hybrid Baked für Layer 0, Importance-Volumes |
| World Partition vertikal | HOCH | UE5 primär horizontal | Manuelle Data Layers, Occlusion Volumes |
| Schattenfieber PP Accessibility | HOCH | Vertex-Animation / DOF = Motion-Sickness | Accessibility-Option Pflicht, intern getestet |
| Nanite dünne Geometrien | MITTEL | Absturz bei dünnen Meshes | Fallback-LOD-Workflow, Asset-Klassifizierung |
| Biolumineszenz Performance | MITTEL | Viele Emitter = GI-Overhead | Dreiklassen-System, Klasse-A-Budget |
| Nervensystem Arm-Mesh | MITTEL | Hoher FP-Animations-Aufwand | Eigenständiger Task, 3-Wochen-Schätzung |
| Tiervolk-Symbiose-Shader | MITTEL | Masken-Qualität abhängig von Referenzbildern | Vera-Referenzen vor Shader-Finalisierung |

---

## 6.12 Offene Fragen & Abhängigkeiten

| Frage | An wen | Status |
|---|---|---|
| ~~Stadtebenen-Übergänge?~~ | Vera | **ERLEDIGT** (Tag 2): oben fließend, unten diskret |
| ~~Lymph → PP-Trigger?~~ | Darius | **ERLEDIGT** (Tag 3): Interface in 6.4.7 |
| ~~Tiervolk-Siedlungen statisch/mobil?~~ | Emre | **ERLEDIGT** (Tag 4): statisch, Layer-gebunden |
| Sichtachsen / Constraint-Punkte Houdini-Terrain | Vera / Emre | Offen — wartet auf Topos-Kapitel |
| 2–3 Tiervolk-Referenzbilder | Vera | Ausstehend |
| Fraktionswahl: unterschiedliche PP-Presets? | Nami | Offen — optionale Erweiterung vorskizziert |
| Orden-Siegel-Vektor für Shader-Texture-Atlanten | Vera | Offen — wartet auf Art-Direction |
| Finale Bandbreite Tiervolk-Tierformen | Emre / Vera | Offen — beeinflusst MI-Anzahl |

---

*Dokument-Status*: Version 5.0 — Finalisierung. Seitenbudget-Kürzung: 6.7 auf ein Drittel reduziert, Schattenfieber-PP-Parameter in HTML-Kommentare, Pre-Alpha-Timeline entfernt. Bilder eingebaut. Keine neuen Inhalte.

*Pipeline-Bibel*: Alle detaillierten Shader-Parameter, Tiervolk-Layer-Beschreibungen, Blend-Maske-Hypothesen, Aufwandsschätzungen und Pre-Alpha-Wochenplanung → internes Pipeline-Bibel-Dokument.
