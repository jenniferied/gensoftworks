# GDD Kapitel 6: Technische Spezifikation & Produktion

**RELICS: [Relikt-Name steht aus]**
**Autor**: Tobias Richter, Technical Artist
**Version**: 1.0 — Tag 2, Dienstag, 10:00 Uhr
**Status**: Arbeitsdokument — erste vollständige Version

---

> **Anmerkung zur Dokumentstruktur**
> Dieses Kapitel ist die technische Antwort auf das kreative Briefing. Jede Entscheidung hier hat einen Grund — und den schreibe ich dazu. Wenn eine Entscheidung keine Begründung hat, gehört sie nicht ins Dokument. Das ist mein Standard.

---

## 6.1 Engine & Technologiebasis

### 6.1.1 Unreal Engine 5 — Begründung

RELICS wird in **Unreal Engine 5** entwickelt. Diese Entscheidung ist gesetzt und nicht diskussionswürdig. Die Begründung:

Das Kernszenario — eine vertikal geschichtete Stadt mit extremer Geometriedichte, biolumineszenten Materialien, dynamischer Globalbeleuchtung und einem Post-Process-System, das die Spielwahrnehmung schrittweise deformiert — erfordert eine Kombination aus Nanite, Lumen und World Partition. Kein anderes aktuell verfügbares System bietet alle drei in Integration. Custom-Engine-Arbeit wäre für ein Studio dieser Größe prohibitiv.

**Engine-Version**: UE5.4 LTS (Long-Term Support Release). Kein Upgrade während der Alpha-Phase. Feature-Patches werden erst nach Beta evaluiert.

**Ziel-Plattform (primär)**: Windows PC (DirectX 12)
**Ziel-Plattform (sekundär)**: PlayStation 5, Xbox Series X (nach Full-Release evaluiert)

**Hardware-Mindestanforderungen (PC, Zielzustand):**
| Stufe | GPU | RAM | Einstellung |
|---|---|---|---|
| Minimum | NVIDIA RTX 2070 / AMD RX 6700 XT | 16 GB | Lumen Software RT, mittlere Qualität |
| Empfohlen | NVIDIA RTX 3080 / AMD RX 7900 XT | 32 GB | Lumen Hardware RT, hohe Qualität |
| Ultra | NVIDIA RTX 4080 / AMD RX 7900 XTX | 32 GB | Full Hardware RT, maximale Qualität |

*Anmerkung*: Die Minimum-Konfiguration nutzt Lumen in Software-RT-Modus. Das degeneriert GI-Qualität in den Slum-Unterebenen merklich. Akzeptabel — die Unterebenen sind dunkel per Design.

---

### 6.1.2 Kernkomponenten der Engine

**Nanite** — Virtualisierte Geometrie
Nanite ist für die gesamte statische Architekturgeometrie aktiviert. Die Materiallesbarkeit der Welt — Zunftzeichen-Reliefs, Titan-Legierung-Oberflächendetail, Knochen-Schnitzereien der Unterschicht — funktioniert nur mit Nanite-Detailauflösung. Ohne LOD-Authoring pro Mesh spart das konservativ geschätzt 40–60% des Modellierungs-Aufwands gegenüber traditioneller Pipeline.

*Bekannte Schwächen und Kompensation:*
- **Dünne Geometrien** (Ketten, Gitterstäbe, Pflanzenstifte, Stoff-Überhänge): Nanite crasht bei Meshes unter ~2px projected-size. Diese Kategorie behält traditionelle LODs und Imposter-Billboards ab Distanzklasse 3.
- **Wasser, Transluzenz**: Nanite unterstützt keine transluzenten Materialien. Alle Wasseroberflächen und Glas-Elemente sind non-Nanite mit eigenem LOD-Setup.
- **Moving Meshes**: Nanite funktioniert für statische und leicht animierte Meshes. Kampf-Props, die zerstört werden können, müssen als Nanite-Fallback-Mesh mit Destruction-Proxy gebaut werden.

---

**Lumen** — Dynamische Globalbeleuchtung und Reflexionen

Lumen ist das wichtigste und gleichzeitig riskanteste System im Projekt. Die Begründung ist direkt: eine lebendige, biolumineszente Stadt mit phosphoreszierenden Mineralien, Alchemie-Lampen und Schattenfieber-Mutationen braucht echte dynamische GI. Statisches Baked Lighting würde jeden Runtime-Zustandswechsel — das Aktivieren eines Relikts, eine Schattenfieber-Eskalation, die Biolumineszenz-Klasse-A-Emitter — optisch inkonsistent machen.

*Lumen-Konfiguration nach Stadtschicht:*

| Schicht | Modus | Begründung |
|---|---|---|
| **Layer 3** (Türme, Gilden-Hochbau) | Hardware Raytracing | Offener Himmel, viele Bergkristall-Linsen-Reflektionen — hier ist Hardware-RT-Qualität sichtbar und rechtfertigbar |
| **Layer 2** (Brücken, Arkaden) | Hardware Raytracing | Starke Buntglas-Farbflecken auf Böden, Reflexionen in Metall-Intarsien — RT sichtbar |
| **Layer 1** (Straßenebene) | Software Raytracing (hohe Qualität) | Kompromiss: genug GI-Bouncing für Kerzenlicht-Atmosphäre, Budget-schonend |
| **Layer 0** (Untergrund, Kanäle) | Software Raytracing + Hybrid Baked | Lumen degeneriert stark ohne Himmelssicht. Baked Irradiance für statische Bereiche, Lumen-Emitter für dynamische Lichtquellen |

*Lumen-Tuning-Parameter (global):*
- `r.Lumen.ScreenProbeGather.ScreenSpaceBentNormal 1` — Verbessert GI in Ecken und Nischen, kritisch für Gewölbe-Architektur
- `r.Lumen.Reflections.MaxRoughnessToTrace 0.4` — Beschränkt RT-Reflexionen auf glänzende Materialien (Titan, Glas, Edelstahl)
- `r.Lumen.DiffuseIndirect.Allow 1`
- Lumen-Importance-Volumes: Manuell platziert in allen Gildenhallen, Ordenskorridoren, Ratsräumen — höhere Probe-Dichte wo Materialqualität inszeniert wird

*Lumen-Emitter-Klassifizierung* (→ detailliert in 6.3.2):
- Klasse A: echte GI-Emitter (wenige, hero lights)
- Klasse B: visuell emissiv, kein GI-Beitrag
- Klasse C: Niagara-Partikel-Glow

---

**World Partition** — Streaming und vertikale Architektur

World Partition ist Pflicht für eine offene Welt dieser Größe. Das primäre technische Problem: UE5 World Partition ist horizontal konzipiert — es streamt Grid-Zellen auf einer XY-Ebene. Die vertikale Stadtstruktur von RELICS (vier markante Schichten auf der Z-Achse) ist kein Standardfall.

*Lösung: Manuelle Data Layers als vertikale Strukturierung*

Statt die Vertikale dem automatischen Streaming zu überlassen, strukturieren wir vier manuelle Data Layers:

| Layer | Inhalt | Lichtstimmung | Schattenfieber-Ambience |
|---|---|---|---|
| **Layer 0** | Untergrund, KanalSystem, Slum-Keller | Phosphoreszierendes Blau-Grün, vereinzelt Feuerschein | Hoch — subtile PP-Basis-Ambience aktiv |
| **Layer 1** | Straßenebene, Handwerkerviertel, Marktplätze | Warmes Kerzenlicht, Buntglas-Farbflecken aus Obergeschossen | Mittel |
| **Layer 2** | Brücken, Arkaden, niederer Gilden-Bereich | Diffuses Tageslicht durch Bergkristall-Linsen-Streuung | Niedrig |
| **Layer 3** | Türme, Gildenhochbau, Ordensanlagen, Kronenpalast | Klares Tageslicht, Bergkristall-Linsen direkt, Metallic-Reflektionen | Minimal |

*Technische Implementierung:*
- Jeder Data Layer ist eine eigenständige Streaming-Einheit mit eigenem Post-Process-Volume-Stack
- Manuelle Occlusion-Volumes an allen Schicht-Übergängen — Layer 3 cullt aggressiv Layer 0 und 1 wenn Sichtlinien getrennt
- Ebenen-Übergänge (Treppen, Lifte, Schächte) sind als "Transition Zones" definiert — beide angrenzenden Layer gleichzeitig geladen für 60m Radius um den Übergang
- **Offene Frage an Vera**: Wie diskret sind die Schichtgrenzen im Level-Design? Fließende Übergänge erhöhen die Transition-Zone-Radius-Kosten signifikant. Diskrete Ebenen = robustere Streaming-Pipeline. Das muss vor World-Partition-Setup entschieden sein.

---

## 6.2 Kamerasystem

### 6.2.1 Third/First Person — nahtloser Übergang

Das Briefing nennt explizit Skyrim als Referenz. Der Übergang muss nahtlos sein — kein Ladebildschirm, kein sichtbarer Kamera-Swap.

**Implementierungsansatz:**
Eine einzige Camera-Component, zwei definierte Offset-Zustände, interpoliert:

- **Third-Person-Position**: 200 cm hinter dem Charakter, 80 cm über der Schulter (leichter Schulter-Offset für bessere Sichtbarkeit der Figur in Kämpfen)
- **First-Person-Position**: Exakte Head-Socket-Koordinate, keine Körper-Sichtbarkeit

**Blend-Mechanismus:**
- Blend-Dauer: 0.3 Sekunden
- Kurventyp: Ease-In/Out (keine lineare Interpolation — die fühlt sich mechanisch an)
- Ausgelöst per Tastendruck oder Context-Trigger (enge Gänge lösen optionalen Auto-Wechsel aus)

**FOV-Konfiguration:**
| Modus | Standard-FOV | Spieler-Range |
|---|---|---|
| Third Person | 90° | 75° – 100° |
| First Person | 95° | 80° – 110° |
| Vertikaler Raum (z.B. Turm-Inneres) | +5° automatisch | — |

*Begründung FOV-Spread*: Die vertikale Stadt erfordert mehr vertikalen Sichtraum als ein Standardspiel. 90° Third Person ist Standard; der automatische +5° in hohen Räumen ist eine qualitative Verbesserung ohne Übelkeit-Risiko.

---

### 6.2.2 Cinematik-Modus (Sequencer)

Für Cutscenes, Dialoge und Relikt-Aktivierungs-Sequenzen nutzen wir **UE5 Sequencer** mit eigenem Kamerasystem.

- Cinematic-Kameras sind separate Kamera-Akteure — sie übernehmen temporär die Kontrolle, blenden zurück auf Spieler-Camera
- DOF: echtes Bokeh-DOF im Cinematic-Modus (Performance-Kosten akzeptiert für Kino-Qualität)
- **Tarkowski-Referenz** (Nami): Statische Langzeiteinstellungen, langsame Zooms, keine handheld-Simulation. Die Kamera ruht — die Welt bewegt sich in ihr. Das soll das Kamera-Führungsprinzip für alle Haupt-Cutscenes sein.

---

## 6.3 Rendering-Pipeline: Materialien & Biolumineszenz

### 6.3.1 Material-Philosophie

Jedes Material in RELICS muss auf drei Ebenen funktionieren:
1. **Materiallesbarkeit** — der Spieler erkennt sofort den sozialen Status des Trägers/Besitzers (Dark Souls Design Works-Prinzip: Abnutzung und Kontext erzählen Geschichte)
2. **Physikalische Plausibilität** — kein Material sieht "falsch" aus. PBR-Werte innerhalb physikalischer Grenzen.
3. **Performance-Budget** — jedes Material hat ein definiertes Instruction-Count-Limit

**Material-Hierarchie nach sozialer Schicht** (technische Entsprechung des Briefings):

| Schicht | Materialklasse | Roughness-Range | Metallic | Besonderheit |
|---|---|---|---|---|
| Oberschicht | High-Fidelity PBR | 0.05 – 0.25 | Ja (Titan, Edelstahl, Gold) | Clearcoat-Layer für Bergkristall-Linsen, Emissive optional |
| Mittelschicht | Standard PBR | 0.3 – 0.6 | Partiell (Bronze, Silber) | Malachit-Einlagen via Masked-Layer |
| Unterschicht | Dirty/Layered PBR | 0.6 – 0.95 | Selten | Wear-Maps, Schmutz-Parameter, gestohlene Akzente |

*Globalregel*: Material-Kontrast-Hierarchie nach FFXIV-v2.0-Vorbild. Emissive-Elemente sitzen auf dunklen Basismaterialien — Lesbarkeit vor Sättigung.

---

### 6.3.2 Biolumineszenz — Dreiklassen-System

Biolumineszenz ist das Neon-Äquivalent dieser Welt. Phosphoreszierende Mineralien, Alchemie-Leuchtstoffe, organisches Glühen. Das technische Problem: viele Emitter = Performance-Kollaps. Lösung: striktes Klassifizierungssystem.

**Klasse A — Hero Lights (echte Lumen-GI-Emitter):**
- Mesh-Flag: `Cast Lumen Light = true`
- Zweck: Setzt die narrative Lichtstimmung einer Szene
- Budget: max. 8–12 Klasse-A-Emitter gleichzeitig im sichtbaren Bereich
- Beispiele: Bergkristall-Linsen der Gildenmeister, große Alchemie-Lampen in Ordenskorridoren, das aktivierte Relikt (Zustand 2)
- Emissive-Intensität: 50–200 cd/m² (physikalisch plausibel für echte Glaslampen-Äquivalente)

**Klasse B — Ambient Glow (visuell emissiv, kein GI-Beitrag):**
- Mesh-Flag: `Cast Lumen Light = false`
- Zweck: Atmosphärische Dichte ohne Performance-Kosten
- Budget: unbegrenzt — kein GI-Overhead
- Beispiele: phosphoreszierende Schimmel-Patches in Untergeschossen, Alchemie-Phiolen im Regal, Kleinst-Buntglas-Elemente
- Emissive-Intensität: 2–15 cd/m² — leuchten visuell, strahlen aber nicht in die Szene

**Klasse C — Particle Glow (Niagara, organisch):**
- Niagara-System mit Billboard-Sprites und Custom-Depth-Masking
- Zweck: organische Biolumineszenz-Cluster (Pilze, Schimmel-Kolonie, Schattenfieber-Wucherungen)
- Skalierbar über GPU-Simulationsstufen (Low/Medium/High)
- Lodded ab 20m Distanz — Particle Count halbiert sich pro Distanzklasse
- Beispiele: Slum-Pilz-Cluster, Kanal-Algen-Glühen, Schattenfieber-Pusteln an Infizierten

*Dokumentationspflicht*: Jeder platzierte Klasse-A-Emitter wird in einer Scene-Light-Bible dokumentiert. Keine undokumentierten Hero Lights in final gebauten Szenen.

---

## 6.4 Schattenfieber — Post-Processing-System

### 6.4.1 Systemarchitektur

Das Schattenfieber-PP-System ist das komplexeste Single-Feature im Projekt. Es muss drei klar definierte Stufen mit smoothem Übergang abbilden und darf kein hartcodiertes System sein — alle Parameter müssen Blueprint-seitig steuerbar bleiben, damit Darius und Nami Inhalte ohne Tobi-Beteiligung implementieren können.

**Blueprint-Architektur:**

```
BP_SchattenfiebertSystem
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

Der `ShadowFever_Intensity`-Wert wird vom Gameplay-Blueprint geschrieben (Darius' Lymph-Subsystem → Interface). Tobi's System liest den Wert und reagiert.

**Übergänge**: Immer geblended über die Timeline-Kurve. Kein Hard-Switch zwischen Stufen. Minimum-Blend-Zeit: 2 Sekunden pro Stufe.

---

### 6.4.2 Stufe 0 — Basis (kein Schattenfieber)

Normaler Spielzustand. Der PP_Stage_0-Stack ist trotzdem aktiv — er setzt die Color-Grading-Basis für RELICS.

- **Color Grading**: ACES-Tonemapping, leicht kühle Schattenbereich (Shadow Gain: RGB 0.95 / 0.95 / 1.02)
- **Film Grain**: 0.2 Intensität, 1.0 Körnung — minimal, nicht bewusst wahrnehmbar
- **Bloom**: Physikalisch kalibrierter Bloom-Mode, Schwellwert 1.2 — nur echte überbelichtete Stellen leuchten
- **Schärfe**: Temporal Anti-Aliasing (TAA), Schärfe-Boost 0.2

*Begründung*: Die leicht kühlen Schatten bauen schon im Normalzustand eine latente Kälte auf — der Spieler fühlt sie nicht bewusst, aber sie ist da. Technische Narratologie.

---

### 6.4.3 Stufe 1 — Frühinfiltration (sensorisch, subtil)

Der Spieler soll unsicher sein, ob er etwas sieht. Die Stufe ist so designt, dass erfahrene Spieler sie aktiv suchen müssen.

**Aktive Parameter:**
- **Chromatic Aberration**: Randbereich +0.4 Pixel max, zentral 0 — nur die Peripherie ist betroffen
- **Bloom-Tint**: Leicht Richtung Cyan verschoben (RGB-Multiplikator: 0.95 / 1.0 / 1.05)
- **Film Grain**: hochgesetzt auf 0.45, Körnung feiner (0.7) — das "Rauschen" aus Namis Stufe-1-Beschreibung
- **Schattenbereich-Kühlung**: Shadow Gain +0.05 auf Blaukanal — Schatten werden kälter
- **Vignette**: 0.15 Intensität — kaum bemerkbar, rahmt aber den Blick

**Was nicht aktiv ist**: kein DOF, keine Vertex-Animation, keine Geometrie-Eingriffe. Das kommt in Stufe 2.

*Spielerfahrung (Nami-Alignment)*: Geräusche klingen nach — das ist Sound-Design-Territorium, kein PP-System. Aber die Bild-Entsprechung ist die Chromatic Aberration: das Bild "klingt nach" im optischen Sinne. Eine winzige Farb-Verschiebung, die sich wie ein Echo anfühlt.

---

### 6.4.4 Stufe 2 — Mutative Phase (eindeutig, riskant)

Ab hier ist das Schattenfieber bewusst spürbar. Spieler wissen, dass sie infiziert sind. Die Wahrnehmung kompromittiert sich.

**Aktive Parameter:**
- **Chromatic Aberration**: 0.8 Pixel, leichte Oszillation (Sinuswelle, 0.5 Hz)
- **Vignette**: 0.35, pulsierend (0.25 Hz Sinuswelle, Amplitude 0.1)
- **Depth of Field**: Nahbereichs-DOF aktiviert, Focal Length 400cm, F-Stop 1.8 — Objekte näher als 4m werden scharf gestellt, Hintergrund unscharf. Simuliert veränderten Wahrnehmungs-Fokus.
- **Color Grading Curves**: Schattenbereich Indigo-Tint — Shadow-Midpoint-Offset: RGB -0.03 / -0.03 / +0.08
- **Vertex-Animation** (Umgebungsobjekte, separates System): ausgewählte organische Meshes im 15m-Radius um den Spieler oszillieren ±1.5 cm, 0.3–0.8 Hz (variiert pro Mesh). Das ist das "Atmen" der Welt.

**Accessibility-Option (Pflicht)**:
- Einstellungsmenü: "Schattenfieber-Bewegungseffekte reduzieren"
- Bei Aktivierung: Vertex-Animation deaktiviert, DOF-Pulsieren deaktiviert, Vignette-Pulsieren → statisch auf 0.3
- Die Stufe bleibt erkennbar, aber Motion-Sickness-Trigger werden eliminiert
- Dokumentation im Spielhandbuch: klarer Hinweis auf diese Option

---

### 6.4.5 Stufe 3 — Auflösung (Grenze zur anderen Seite)

Der kritische Zustand. Spieler befinden sich an der Schwelle zu den "planes of existence beyond known reality". Das ist das einzige Übernatürliche im Spiel — und es muss sich so anfühlen.

**Aktive Parameter:**
- **Full-Screen-Overlay**: `M_SchattenfiebertOverlay` — ein Custom-Depth-Masking-Shader mit organischen Rissstrukturen. Die Risse entstehen an Bildrändern und wandern langsam zur Bildmitte. Bewegungsgeschwindigkeit abhängig von `ShadowFever_Intensity`.
- **Geometrie-Lücken**: Ausgewählte Wand-Meshes zeigen temporäre schwarze Flächenbereiche — als würden Teile der Weltgeometrie nicht mehr existieren. Technisch: ein separater Render-Pass mit Masked-Visibility über Custom Stencil Buffer.
- **Indigo-Bloom**: Emissive-Quellen bekommen starken Indigo-Halo — Bloom-Radius 8.0, Tint stark Richtung Indigo/Violett
- **Chromatic Aberration**: 1.5 Pixel, chaotisch (Rauschwert statt Sinuswelle)
- **Nervensystem-Visualisierung**: startet automatisch (→ 6.5)

**Was diese Stufe mit dem Relikt-Shader verbindet**: Der kritische Relikt-Zustand (→ 6.6) nutzt dasselbe visuelle Vokabular wie Stufe 3 — Rissstrukturen, Innen-Leuchten, Indigo-Tönung. Das ist keine Koinzidenz. Das Relikt und die Krankheit sprechen dieselbe Sprache. Intentionale Ambiguität.

*Accessibility-Option*: Bei aktiviertem Modus werden Geometrie-Lücken deaktiviert, Overlay-Intensität auf 0.6 reduziert. Die Stufe bleibt narrativ funktional.

---

### 6.4.6 Schattenfieber-Ambient (Layer-gebunden)

Unabhängig vom Spieler-Infektionslevel haben die Data Layers eine baseline Schattenfieber-Ambience:

- Layer 0 (Untergrund): `ShadowFever_Ambient = 0.15` — die Schwelle ist hier dünn, das spürt man
- Layer 1 (Straße): `ShadowFever_Ambient = 0.05`
- Layer 2 (Arkaden): `ShadowFever_Ambient = 0.0`
- Layer 3 (Türme): `ShadowFever_Ambient = 0.0`

Der Ambient-Wert addiert auf den Spieler-Wert. Ein Spieler ohne Infektion in Layer 0 läuft bei effektiv 0.15 — im Normalzustand nicht bewusst, aber da. Technische Narratologie: die Architektur erzählt die Kosmologie.

---

## 6.5 Nervensystem-Visualisierung

### 6.5.1 Konzept

Das Leveling-System (→ GDD Kap. 2) nutzt eine halbtransparente Nervensystem-Sicht als Visualisierung des Fortschritts. Drei Subsysteme — Cardio (Ausdauer), Muskel (Stärke), Lymph (Immunresistenz/Schattenfieber-Toleranz) — werden als Overlay auf den Charakter-Körper projiziert.

Dieses System hat zwei Modi:
1. **Statistik-Ansicht** (vom Spieler ausgelöst, Menü): Vollbild-Overlay, alle drei Systeme sichtbar, interaktiv
2. **Echtzeit-Overlay** (kontextabhängig): schmales, halbtransparentes Overlay — aktiviert in Stufe 3 Schattenfieber, nach schweren Verletzungen, und optional permanent im HUD

---

### 6.5.2 Technische Umsetzung

**Third-Person-Modus:**
- Overlay via Custom-Depth-Pass auf dem Charakter-Mesh
- Drei Materialschichten (Cardio, Muskel, Lymph) mit eigenem Emissive-Kanal
- Farb-Kodierung: Cardio = warmrot, Muskel = bernsteingelb, Lymph = kühles Grün-Weiß
- Opazität: 0.4–0.7 je nach Kontext (Menü: 0.7, Echtzeit: 0.4)
- Fortschritt sichtbar als Textur-Dichte und Emissive-Intensität — stärkeres Cardio-Subsystem = dichter gezeichnete rote Linien, die heller leuchten

**First-Person-Modus:**
- Separates Arm-Mesh-Set (eigene Asset-Klasse: `SK_FP_Arms`)
- Synchron animiert mit dem Haupt-Charakter-Mesh via Animation-Blueprint
- Nervensystem-Overlay auf das `SK_FP_Arms`-Mesh — der Spieler sieht seine eigenen Unterarme, Hände, angedeutet die Schultern
- **Aufwand-Klassifizierung**: mittel-hoch. Das Arm-Mesh braucht einen vollständigen eigenen Animations-Set. Synchronisation mit dem Haupt-Mesh ist der technische Hauptaufwand. Zeitschätzung: 3 Wochen für stabiles System.

**Shader-Struktur (M_Nervensystem_Base):**
```
Inputs:
  - BaseColor: Charakter-Skin
  - NervensystemMask_Cardio (Texture2D, R-Kanal)
  - NervensystemMask_Muskel (Texture2D, G-Kanal)
  - NervensystemMask_Lymph (Texture2D, B-Kanal)
  - Fortschritt_Cardio (Scalar 0–1)
  - Fortschritt_Muskel (Scalar 0–1)
  - Fortschritt_Lymph (Scalar 0–1)
  - Overlay_Opacity (Scalar 0–1)

Outputs:
  - Emissive: Farb-kodiertes Nervensystem-Leuchten
  - Custom Depth: für Compositing-Pass
```

---

## 6.6 Relikt-Shader — Master Material System

### 6.6.1 Konzept

Das Relikt — der Schwellen-Stabilisator, der kosmologische Resonanzpunkt — existiert als ein einziges Mesh mit einem Master-Material und drei Material-Instanzen. Die Übergänge zwischen den Zuständen sind immer geblended, nie hart. Das Relikt ist kein Gadget; es ist ein kosmologisches Instrument. Das muss im Material sichtbar sein.

---

### 6.6.2 Drei Zustände

**Zustand 1 — Ruhezustand (dormant):**
Das Relikt ruht. Es ist nicht tot — es ist latent lebendig.

- **Base Material**: transluzentes, mattes Grundmaterial
- **Subsurface Scattering (SSS)**: aktiv, warme Untertonfarbe (RGB 1.0 / 0.85 / 0.7 — leicht goldenes Hautton-Unterlicht)
- **SSS-Radius**: 0.8 cm — das Licht streut tief, wie durch organisches Gewebe
- **Roughness**: 0.55 — nicht spiegelnd, aber nicht stumpf. Polierter Knochen oder Elfenbein-Charakter.
- **Emissive**: 0.0 — kein aktives Leuchten
- **Lumen-Emitter**: deaktiviert

*Designabsicht*: Das Relikt soll schon im Ruhezustand anders aussehen als totes Material. Das SSS erzeugt ein inneres Lebendigkeit — etwas ist da, schläft aber.

---

**Zustand 2 — Aktiver Zustand (resonant):**
Das Relikt ist aktiviert. Es ist zur Lichtquelle geworden.

- **Base Material**: dasselbe Grundmaterial, aber SSS-Intensität um 40% erhöht
- **Emissive-Layer**: hochgefahren, Farbe = warmes Indigo-Weiß (RGB 0.85 / 0.8 / 1.2, überbelichtet bei 3.5)
- **Lumen-Emitter**: aktiviert (Klasse A) — das Relikt wirft echtes GI in die Szene, färbt umliegende Wände und Böden
- **Lichtfarbe Lumen**: leicht violett-weiß (CCT 7500K mit Indigo-Bias) — kühler als natürliches Licht, kalt und klar
- **Lichtradius**: 4m für direkte Lumen-Reichweite, darüber Bloom-Halo
- **Bloom-Halo**: 6.0 Radius, Indigo-Tint — sichtbar auch auf Screenshots, nicht nur in Bewegung

*Designabsicht*: Das aktivierte Relikt soll sofort als Lichtquelle erkennbar sein. Es ist die wichtigste dynamische Lichtquelle in jeder Szene, in der es aktiv ist.

---

**Zustand 3 — Kritischer Zustand (überlastet):**
Das Relikt ist am Limit. Das kosmologische Instrument bricht unter Last.

- **Base Material**: Riss-Overlay-Layer aktiv — ein Masked-Texture-Layer projiziert organische Rissstrukturen auf die Oberfläche
- **Riss-Struktur**: `T_Relikt_Riss_01` (Procedural Noise-basiert, kein symmetrisches Muster) — Risse öffnen sich im Laufe des kritischen Zustands (Blend-Parameter steuert Öffnungsgrad)
- **Innenleuchten**: durch die Risse scheint das Emissive-Innere — lokal höhere Emissive-Intensität an Riss-Kanten (8.0+, kalt-violett)
- **Subsurface Scattering**: jetzt blau-violett getönt (RGB 0.7 / 0.6 / 1.3) — die Wärme ist weg, das SSS-Licht ist kalt
- **Lumen-Emitter**: flackernd, instabil (Blueprint-gesteuerte Intensitätsschwankung, 2–8 Hz unregelmäßig)
- **Lichtfarbe**: hard-violett (CCT >10000K, stark ins Ultraviolett verschoben)
- **Vertex-Animation**: das Mesh selbst vibriert leicht (±0.2mm, 12 Hz) — submillimeter, erzeugt nervöses Shimmern

*Designabsicht*: Visuelles Vokabular entspricht bewusst PP-Stufe 3. Das Relikt und das Schattenfieber sprechen dieselbe Sprache: Rissstrukturen, Kalt-Violett, Innenleuchten, Instabilität. Der Spieler sieht diese Verbindung — ob er sie versteht, ist Erzählung.

---

### 6.6.3 Master-Material-Struktur (M_Relikt_Master)

```
Parameter-Gruppen:
  [Base]
    Roughness (Scalar)
    BaseColor (Vector)

  [SSS]
    SSS_Enabled (StaticBool)
    SSS_Color (Vector)
    SSS_Radius (Scalar)
    SSS_Intensity (Scalar)

  [Emissive]
    Emissive_Enabled (StaticBool)
    Emissive_Color (Vector)
    Emissive_Intensity (Scalar)
    Emissive_Flicker (Bool)
    Emissive_FlickerFrequency (Scalar)

  [Riss]
    Riss_Enabled (StaticBool)
    Riss_Mask (Texture2D)
    Riss_BlendAmount (Scalar 0–1)
    Riss_EmissiveBoost (Scalar)

  [State_Blend]
    State_Alpha (Scalar 0–2.0)
    -- 0.0 = Zustand 1, 1.0 = Zustand 2, 2.0 = Zustand 3
    -- Alle Parameter interpolieren im Blueprint anhand dieses Wertes
```

**Drei Material-Instanzen**: `MI_Relikt_Dormant`, `MI_Relikt_Resonant`, `MI_Relikt_Critical` — alle vom selben Master. Blueprint interpoliert zwischen den Instanz-Parametern über `State_Alpha`.

---

## 6.7 Houdini-Pipeline — Terrain und Prozedurale Systeme

### 6.7.1 Terrain-Generierung

Die vertikale Stadt braucht eine Basis-Topografie: das Flusstal, die Hügelketten der umgebenden Mittelgebirgs-Landschaft, die natürlichen Erhebungen, auf denen die Stadtschichten gebaut sind.

**Workflow:**
1. Basis-Terrain in **Houdini** procedural generiert (Houdini Heightfield-System)
2. Export als `.hdr`-Heightmap nach UE5 (16-bit, 4096×4096 für Kernregion)
3. In UE5: Landscape-System mit Nanite-Tessellation für Nahbereich
4. Automatisches Foliage-Placement via PCG (Procedural Content Generation Graph, UE5 native)

**Houdini-Setup:**
- Basis-Erosion: hydraulische Erosion für naturwirkende Täler und Rinnsale
- Stadtplattform-Sculpting: manuelle Eingaben (Terrassen-Formen für die Stadtebenen) werden in Houdini als Kontrollkurven eingebracht
- Fluss-System: Heightfield-Vexnet für Flussbettgenerierung
- Output-Auflösungen: 4k für Terrain-Kern (2km Radius), 2k für äußere Bereiche (10km Radius)

*Offene Frage an Vera*: Gibt es definierte Punkte für Stadteingang, wichtige Sichtachsen (z.B. von der Stadtmauer auf den Gildenhochbau)? Die brauche ich als Constraint-Kurven für das Houdini-Setup.

---

### 6.7.2 Prozedurale Stadtdetails (PCG-Systeme)

Für wiederholende Stadtdetails (Pflasterstein-Muster, Mauer-Erosion, Fassaden-Ageing, Schimmel-Verteilung im Untergrund) wird ein PCG-System aufgebaut:

- **Pflaster-Variation**: PCG platziert Stein-Typ, Rotation, Abnutzungsgrad basierend auf Nähe zu Fußwegen und Schicht-Tiefe
- **Fassaden-Ageing**: prozedurale Wear-Maps generiert in Houdini, instanziiert via PCG
- **Biolumineszenz-Cluster**: Niagara-Systeme werden via PCG in Layer-0-Bereichen platziert, Dichte abhängig von Nähe zu Wasserquellen (simuliert Feuchtigkeitskorrelation)
- **Vegetation-Infiltration**: in Slum-Bereichen und verlassenen Abschnitten wachsen prozedurale Pflanzen-Cluster aus Rissen

---

## 6.8 Color Science & Display-Pipeline

### 6.8.1 Color-Management

RELICS nutzt **ACES** (Academy Color Encoding System) als Farbraum-Standard.

**Pipeline:**
```
Kreativ-Input → ACEScg Arbeitsraum → ACES Tonemapping → Display-Transform (sRGB/DCI-P3)
```

- Alle Texturen: in sRGB gespeichert, im Shader in lineares Licht konvertiert
- Emissive-Werte: in physikalischen Einheiten (cd/m²) definiert, nicht als 0–1-Werte
- LUT (Look-Up-Table): ein Basis-LUT für den RELICS-Look (kühle Schatten, gedämpfte Mitten, klare Lichter), drei Varianten (Normal / Schattenfieber-Stufe-2 / Schattenfieber-Stufe-3)

**Warum kein AgX?** AgX ist für Photography optimiert und komprimiert Highlights weicher. RELICS braucht scharfe, klare Lichter — die Bergkristall-Linsen, die Relikt-Emitter müssen leuchten, nicht weich werden. ACES gibt uns das.

---

### 6.8.2 Display-Kalibrierung (internes Studio)

Alle Arbeitsstationen im Studio haben kalibrierte Displays (Delta-E < 2.0). Die Referenz-LUT läuft auf einem Samsung Odyssey OLED, der als "Goldstandard"-Display dient. Spieler-seitig gibt es keine Kontrolle — daher sind alle Emissive-Werte so kalibriert, dass sie auch auf einem Standard-SDR-Display (sRGB, 200 cd/m² Peak) korrekt wirken. HDR-Displays bekommen automatisch einen separaten Display-Transform mit erweiterten Highlight-Bereichen.

---

## 6.9 Produktion & Release-Pipeline

### 6.9.1 Milestone-Übersicht

| Milestone | Technischer Status | Schlüssel-Deliverables |
|---|---|---|
| **Pre-Alpha** | Prototyp-Pipeline | Rendering-Architektur steht, Material-Master-Systeme gebaut, World Partition Setup stabil |
| **Alpha** (Streamer) | Feature-Freeze Rendering | Data Layers gesetzt, Lumen-Konfiguration fixiert, PP-System stabil, Relikt-Shader stabil. Standard: stabil + konsistent, NICHT polished |
| **Beta** | Tuning-Phase | Alle bestehenden Systeme werden tuned — Performance-Optimierung, visuelle Feinheit, Accessibility vollständig |
| **Full Release** | Feinschliff + große Setpieces | Abschließende Lighting-Pass für alle Hauptorte, Cinematic-Sequenzen final |
| **DLC** | Erweiterung auf stabiler Basis | Neue Assets auf bestehenden Systemen — kein neues technisches Risiko in DLC-Phase |

**Alpha ist der härteste Freeze**: Nach Alpha-Abgabe sind folgende Systeme nicht mehr änderbar:
- Data Layer-Struktur (Schichtanzahl, Naming, Streaming-Logik)
- Lumen-Konfiguration (RT-Modus pro Layer)
- Schattenfieber-PP-System-Architektur (Blueprint-Struktur, Parameter-Namen)
- Relikt-Master-Material-Struktur (Parameter-Gruppen, Slot-Namen)
- Kamerasystem-Grundstruktur

*Begründung*: Diese Systeme sind die Säulen, auf denen alle anderen Content-Systeme aufbauen. Eine Änderung nach Alpha bricht zuverlässig abhängige Systeme. Tuning ist erlaubt. Umstrukturierung nicht.

---

### 6.9.2 Pre-Alpha — Technische Prioritäten

**Woche 1–4: Foundation**
- UE5 Projekt-Setup, Engine-Version fixieren
- World Partition aktivieren, vier Data Layers anlegen und testen
- Lumen-Konfiguration pro Layer einrichten (Software RT / Hardware RT, Hybrid Baked für Layer 0)
- Erste Prototyp-Materialien: ein Oberschicht-Material, ein Unterschicht-Material, ein Emissive-Klasse-A

**Woche 5–8: Kernsysteme**
- Schattenfieber-Blueprint (alle drei Stufen, smooth geblended)
- Relikt-Master-Material (alle drei Zustände)
- Kamerasystem (Third/First Person Blend)
- Nervensystem-Shader (Third-Person-Modus, First-Person folgt in Woche 10–12)

**Woche 9–12: Integration**
- Biolumineszenz-Pipeline (Klasse A/B/C operativ)
- PCG-System für erste Straßen-Füllung
- Houdini-Terrain-Export → UE5 getestet
- Accessibility-Optionen implementiert und getestet
- Interne Alpha-Kandidat: alle Systeme laufen, kein Polishing

---

### 6.9.3 Monetarisierung — Technische Implikation

Das Briefing ist eindeutig: **Klassisch Premium, keine Mikrotransaktionen.** Das hat eine direkte technische Konsequenz, die ich hier festhalten will:

Kein Live-Service-Backend. Keine Server-seitige Spielstand-Validierung. Keine DRM-Middleware, die Runtime-Overhead erzeugt. Das ist eine technische Erleichterung: die Architektur ist offline-first, save-game ist lokal, kein Always-Online-Requirement.

DLC-Technisch: DLC-Content wird als Pak-Files geliefert (UE5 Standard). Das Basis-Spiel enthält keine Platzhalter für DLC-Content — DLC erweitert auf der stabilen Basis, belegt aber keine Speicherpunkte in der Hauptgame-Dateistruktur.

---

## 6.10 Risiko-Register

| System | Priorität | Risiko | Mitigation |
|---|---|---|---|
| Lumen vertikale GI | HOCH | Degeneriert in tiefen Kanälen | Hybrid Baked für Layer 0, Lumen-Importance-Volumes |
| World Partition vertikal | HOCH | UE5 primär horizontal konzipiert | Manuelle Data Layers, Occlusion Volumes an Ebenen-Übergängen |
| Schattenfieber PP Accessibility | HOCH | Vertex-Animation und DOF-Pulsieren = Motion-Sickness-Risiko | Accessibility-Option Pflicht, intern getestet mit betroffenen Personen |
| Nanite dünne Geometrien | MITTEL | Absturz bei dünnen Meshes | Fallback-LOD-Workflow definiert, Asset-Klassifizierung obligatorisch |
| Biolumineszenz Performance | MITTEL | Viele Emitter = GI-Overhead | Dreiklassen-System, Klasse-A-Budget: max. 12 gleichzeitig |
| Nervensystem Arm-Mesh | MITTEL | Hohes Animations-Aufwand im FP-Modus | Eigenständiger Task, 3-Wochen-Schätzung, eigenständige Asset-Klasse |
| Relikt-Shader-Synchronität | NIEDRIG | State-Alpha-Drift zwischen Blueprint und Material | Interface-Konvention festgelegt, Parameternames dokumentiert |

---

## 6.11 Offene Fragen & Abhängigkeiten

| Frage | An wen | Dringlichkeit |
|---|---|---|
| Wie diskret sind die Stadtebenen-Übergänge im Level-Design? | Vera | KRITISCH vor World-Partition-Setup |
| Welche Sichtachsen / Constraint-Punkte für Houdini-Terrain? | Vera | Hoch |
| Wie triggert das Lymph-Subsystem die PP-Stufen? (Interface-Definition) | Darius | Hoch — vor Alpha-Architektur |
| Braucht Fraktionswahl in Stunde 1 unterschiedliche PP-Presets? | Nami | Mittel — vor Beta |
| Gibt es einen Stadtname / eine definierte Kernregion? | Emre | Mittel — für Terrain-Namensgebung |

---

*Dokument-Status*: Version 1.0, vollständige erste Ausarbeitung. Alle technischen Systeme beschrieben. Offen: Abstimmung mit Vera zu Level-Design-Grenzen (KRITISCH), Abstimmung mit Darius zu Blueprint-Interfaces.

*Pipeline-Bibel*: Alle Shader-Parameter und Blueprint-Architekturen aus diesem Dokument werden in die interne Pipeline-Bibel übertragen (separates internes Dokument, nicht GDD).
