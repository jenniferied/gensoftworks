# GDD Kapitel 6: Technische Spezifikation & Produktion

**RELICS: Schwellenanker**
**Version**: 4.0 — Tag 4, Donnerstag, 10:00 Uhr
**Status**: Arbeitsdokument — v4 (Tiervolk-Symbiose-Shader neu, Cleanup, Seitenbudget-Pass)

<!-- Tobi: v4-Änderungen gegenüber v3: (1) Neuer Abschnitt 6.7 — Tiervolk-Symbiose-Shader (Dual-Layer: Tier-Biologie + Fremdes, Blend-Maske). Alter 6.7 (Houdini) wird zu 6.8, 6.8 (Color Science) zu 6.9, 6.9 (Release-Pipeline) zu 6.10, 6.10 (Risiko-Register) zu 6.11, 6.11 (Offene Fragen) zu 6.12. (2) 6.4.6 Kommentar aktualisiert — Tiervolk-Siedlungen-Frage erledigt (statisch, Layer-gebunden). (3) Risiko-Register: Tiervolk-Shader-Eintrag ergänzt. (4) Offene Fragen: Tiervolk-Zeile als erledigt. (5) Autorenerwähnung im v3-Kommentar lag bereits in HTML-Kommentar — belassen. -->

<!-- Tobi: Verfasser Kap. 6: Tobias Richter, Technical Artist. v1: Tag 2. v2: Tag 3 Briefing. v3: Tag 3 WORK. v4: Tag 4 WORK. -->

---

> **Anmerkung zur Dokumentstruktur**
> Dieses Kapitel ist die technische Antwort auf das kreative Briefing. Jede Entscheidung hier hat einen Grund — und den schreibe ich dazu. Wenn eine Entscheidung keine Begründung hat, gehört sie nicht ins Dokument.

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

*Anmerkung*: Die Minimum-Konfiguration nutzt Lumen im Software-RT-Modus. Das degeneriert GI-Qualität in den Slum-Unterebenen merklich. Akzeptabel — die Unterebenen sind dunkel per Design.

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

Lumen ist das wichtigste und gleichzeitig riskanteste System im Projekt. Die Begründung ist direkt: eine lebendige, biolumineszente Stadt mit phosphoreszierenden Mineralien, Alchemie-Lampen und Schattenfieber-Mutationen braucht echte dynamische GI. Statisches Baked Lighting würde jeden Runtime-Zustandswechsel — das Aktivieren des Schwellenankens, eine Schattenfieber-Eskalation, die Biolumineszenz-Klasse-A-Emitter — optisch inkonsistent machen.

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
| **Layer 0** | Untergrund, Kanal-System, Slum-Keller | Phosphoreszierendes Blau-Grün, vereinzelt Feuerschein | Hoch — subtile PP-Basis-Ambience aktiv |
| **Layer 1** | Straßenebene, Handwerkerviertel, Marktplätze | Warmes Kerzenlicht, Buntglas-Farbflecken aus Obergeschossen | Mittel |
| **Layer 2** | Brücken, Arkaden, niederer Gilden-Bereich | Diffuses Tageslicht durch Bergkristall-Linsen-Streuung | Niedrig |
| **Layer 3** | Türme, Gildenhochbau, Ordensanlagen, Kronenpalast | Klares Tageslicht, Bergkristall-Linsen direkt, Metallic-Reflektionen | Minimal |

*Technische Implementierung:*
- Jeder Data Layer ist eine eigenständige Streaming-Einheit mit eigenem Post-Process-Volume-Stack
- Manuelle Occlusion-Volumes an allen Schicht-Übergängen — Layer 3 cullt aggressiv Layer 0 und 1 wenn Sichtlinien getrennt
- Ebenen-Übergänge (Treppen, Lifte, Schächte) sind als "Transition Zones" definiert — beide angrenzenden Layer gleichzeitig geladen für 60m Radius um den Übergang
- **Schichtgrenzen-Entscheidung (Vera, Tag 2)**: oben fließend, unten diskret. Obere Ebenen (Layer 2–3) nutzen Blend-Volumes; untere Ebenen (Layer 0–1) haben harte Data-Layer-Cuts.
- **Tiervolk-Siedlungen (Emre, Tag 4)**: statisch, an festen kosmologisch dünnen Orten. Ambient-Werte bleiben Layer-gebunden — kein NPC-Proximity-System notwendig.

<!-- Tobi: Vera-Abstimmung zu Schichtgrenzen erledigt (Tag 2). Emre-Abstimmung zu Tiervolk-Siedlungen erledigt (Tag 4): statisch → World Partition bleibt Layer-gebunden, keine Dynamik-Komplexität. -->

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

Für Cutscenes, Dialoge und Schwellenanker-Aktivierungs-Sequenzen nutzen wir **UE5 Sequencer** mit eigenem Kamerasystem.

- Cinematic-Kameras sind separate Kamera-Akteure — sie übernehmen temporär die Kontrolle, blenden zurück auf Spieler-Camera
- DOF: echtes Bokeh-DOF im Cinematic-Modus (Performance-Kosten akzeptiert für Kino-Qualität)
- **Kamera-Führungsprinzip**: Statische Langzeiteinstellungen, langsame Zooms, keine handheld-Simulation. Die Kamera ruht — die Welt bewegt sich in ihr. Das gilt für alle Haupt-Cutscenes.

<!-- Tobi: Tarkowski als Einfluss für Kamerastil, nach Nami-Input Tag 2. Im Fließtext kein Autorname. -->

---

## 6.3 Rendering-Pipeline: Materialien & Biolumineszenz

### 6.3.1 Material-Philosophie

Jedes Material in RELICS muss auf drei Ebenen funktionieren:
1. **Materiallesbarkeit** — der Spieler erkennt sofort den sozialen Status des Trägers/Besitzers
2. **Physikalische Plausibilität** — kein Material sieht "falsch" aus. PBR-Werte innerhalb physikalischer Grenzen.
3. **Performance-Budget** — jedes Material hat ein definiertes Instruction-Count-Limit

**Material-Hierarchie nach sozialer Schicht:**

| Schicht | Materialklasse | Roughness-Range | Metallic | Besonderheit |
|---|---|---|---|---|
| Oberschicht | High-Fidelity PBR | 0.05 – 0.25 | Ja (Titan, Edelstahl, Gold) | Clearcoat-Layer für Bergkristall-Linsen, Emissive optional |
| Mittelschicht | Standard PBR | 0.3 – 0.6 | Partiell (Bronze, Silber) | Malachit-Einlagen via Masked-Layer |
| Unterschicht | Dirty/Layered PBR | 0.6 – 0.95 | Selten | Wear-Maps, Schmutz-Parameter, gestohlene Akzente |

*Globalregel*: Emissive-Elemente sitzen auf dunklen Basismaterialien — Lesbarkeit vor Sättigung.

---

### 6.3.2 Biolumineszenz — Dreiklassen-System

Biolumineszenz ist das Neon-Äquivalent dieser Welt. Phosphoreszierende Mineralien, Alchemie-Leuchtstoffe, organisches Glühen. Das technische Problem: viele Emitter = Performance-Kollaps. Lösung: striktes Klassifizierungssystem.

**Klasse A — Hero Lights (echte Lumen-GI-Emitter):**
- Mesh-Flag: `Cast Lumen Light = true`
- Budget: max. 8–12 Klasse-A-Emitter gleichzeitig im sichtbaren Bereich
- Beispiele: Bergkristall-Linsen der Gildenmeister, große Alchemie-Lampen in Ordenskorridoren, der aktivierte Schwellenanker (Zustand 2), Tiervolk-Emissive im aktiven Zustand
- Emissive-Intensität: 50–200 cd/m²

**Klasse B — Ambient Glow (visuell emissiv, kein GI-Beitrag):**
- Mesh-Flag: `Cast Lumen Light = false`
- Budget: unbegrenzt — kein GI-Overhead
- Beispiele: phosphoreszierende Schimmel-Patches, Alchemie-Phiolen, Kleinst-Buntglas-Elemente, Tiervolk-Ruhezustand-Emissive
- Emissive-Intensität: 2–15 cd/m²

**Klasse C — Particle Glow (Niagara, organisch):**
- Niagara-System mit Billboard-Sprites und Custom-Depth-Masking
- Skalierbar über GPU-Simulationsstufen (Low/Medium/High)
- Lodded ab 20m Distanz
- Beispiele: Slum-Pilz-Cluster, Kanal-Algen-Glühen, Schattenfieber-Pusteln, Tiervolk-Partikel-Ausstöße

*Dokumentationspflicht*: Jeder platzierte Klasse-A-Emitter wird in einer Scene-Light-Bible dokumentiert. Keine undokumentierten Hero Lights in final gebauten Szenen.

---

## 6.4 Schattenfieber — Post-Processing-System

### 6.4.1 Systemarchitektur

Das Schattenfieber-PP-System ist das komplexeste Single-Feature im Projekt. Es muss drei klar definierte Stufen mit smoothem Übergang abbilden und darf kein hartcodiertes System sein — alle Parameter müssen Blueprint-seitig steuerbar bleiben.

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

**Übergänge**: Immer geblended über die Timeline-Kurve. Kein Hard-Switch zwischen Stufen. Minimum-Blend-Zeit: 2 Sekunden pro Stufe.

---

### 6.4.2 Stufe 0 — Basis (kein Schattenfieber)

Normaler Spielzustand. Der PP_Stage_0-Stack setzt die Color-Grading-Basis.

- **Color Grading**: ACES-Tonemapping, leicht kühle Schattenbereiche (Shadow Gain: RGB 0.95 / 0.95 / 1.02)
- **Film Grain**: 0.2 Intensität, 1.0 Körnung
- **Bloom**: Physikalisch kalibrierter Bloom-Mode, Schwellwert 1.2
- **Schärfe**: Temporal Anti-Aliasing (TAA), Schärfe-Boost 0.2

*Begründung*: Die leicht kühlen Schatten bauen schon im Normalzustand eine latente Kälte auf. Technische Narratologie.

---

### 6.4.3 Stufe 1 — Frühinfiltration (sensorisch, subtil)

Der Spieler soll unsicher sein, ob er etwas sieht.

**Aktive Parameter:**
- **Chromatic Aberration**: Randbereich +0.4 Pixel max, zentral 0
- **Bloom-Tint**: Leicht Richtung Cyan (RGB-Multiplikator: 0.95 / 1.0 / 1.05)
- **Film Grain**: hochgesetzt auf 0.45, Körnung feiner (0.7)
- **Schattenbereich-Kühlung**: Shadow Gain +0.05 auf Blaukanal
- **Vignette**: 0.15 Intensität

*Visuelles Konzept*: Die Chromatic Aberration ist das optische Echo — das Bild "klingt nach" im visuellen Sinne.

---

### 6.4.4 Stufe 2 — Mutative Phase (eindeutig, riskant)

Ab hier ist das Schattenfieber bewusst spürbar.

**Aktive Parameter:**
- **Chromatic Aberration**: 0.8 Pixel, leichte Oszillation (Sinuswelle, 0.5 Hz)
- **Vignette**: 0.35, pulsierend (0.25 Hz Sinuswelle, Amplitude 0.1)
- **Depth of Field**: Nahbereichs-DOF aktiviert, Focal Length 400cm, F-Stop 1.8
- **Color Grading Curves**: Shadow-Midpoint-Offset: RGB -0.03 / -0.03 / +0.08
- **Vertex-Animation** (Umgebungsobjekte): ausgewählte organische Meshes im 15m-Radius oszillieren ±1.5 cm, 0.3–0.8 Hz

**Accessibility-Option (Pflicht)**:
- "Schattenfieber-Bewegungseffekte reduzieren" — deaktiviert Vertex-Animation, DOF-Pulsieren, reduziert Vignette-Pulsieren auf statisch 0.3
- Dokumentation im Spielhandbuch obligatorisch

---

### 6.4.5 Stufe 3 — Auflösung (Grenze zur anderen Seite)

Das ist das einzige Übernatürliche im Spiel — und es muss sich so anfühlen.

**Aktive Parameter:**
- **Full-Screen-Overlay**: `M_Schattenfieber_Overlay` — Custom-Depth-Masking-Shader mit organischen Rissstrukturen
- **Geometrie-Lücken**: Masked-Visibility über Custom Stencil Buffer
- **Indigo-Bloom**: Bloom-Radius 8.0, stark Richtung Indigo/Violett
- **Chromatic Aberration**: 1.5 Pixel, chaotisch (Rauschwert statt Sinuswelle)
- **Nervensystem-Visualisierung**: startet automatisch (→ 6.5)

**Verbindung Schwellenanker**: Der kritische Schwellenanker-Zustand (→ 6.6) nutzt dasselbe visuelle Vokabular — Rissstrukturen, Innen-Leuchten, Indigo-Tönung. Das ist keine Koinzidenz. Intentionale Ambiguität.

*Accessibility-Option*: Geometrie-Lücken deaktiviert, Overlay-Intensität auf 0.6 reduziert.

---

### 6.4.6 Schattenfieber-Ambient (Layer-gebunden)

Unabhängig vom Spieler-Infektionslevel haben die Data Layers eine Baseline Schattenfieber-Ambience:

- Layer 0 (Untergrund): `ShadowFever_Ambient = 0.15` — die Schwelle ist hier dünn
- Layer 1 (Straße): `ShadowFever_Ambient = 0.05`
- Layer 2 (Arkaden): `ShadowFever_Ambient = 0.0`
- Layer 3 (Türme): `ShadowFever_Ambient = 0.0`

Der Ambient-Wert addiert auf den Spieler-Wert. Technische Narratologie: die Architektur erzählt die Kosmologie.

<!-- Tobi: Tiervolk-Siedlungen sind statisch, an festen "dünnen Orten" (Emre, Tag 4 Briefing). Konsequenz: Ambient-Werte bleiben Layer-gebunden, wie hier implementiert. Keine NPC-Proximity-Dynamik nötig. Frage erledigt. -->

---

### 6.4.7 Interface-Spezifikation: Lymph-Subsystem → PP-Trigger

<!-- Tobi: Vollständige Blueprint-Interface-Definition. Wer ShadowFever_Intensity schreibt, wer liest, welche Werte zu welchen PP-Stufen führen. Gesetzt in v3, Tag 3. -->

Das Lymph-Subsystem (Gameplay) und das Schattenfieber-PP-System (Tech-Art) kommunizieren über ein klar definiertes Blueprint-Interface.

#### Überblick: Wer schreibt, wer liest

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

Das Gameplay-System schreibt `ShadowFever_Intensity`. Das PP-System feuert Events zurück. Keine Gegenrichtungs-Abhängigkeit.

#### Interface-Funktion: `SetShadowFeverIntensity(float Value)`

```
Signatur:      void SetShadowFeverIntensity(float Value)
Werte-Range:   0.0 – 3.0
Clamp:         intern geclampt auf [0.0, 3.0]
```

**Mapping Lymph-Stufe → ShadowFever_Intensity:**

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

<!-- Tobi: Exposure_Delta ist ein Vorschlag — Darius entscheidet, ob er das so implementiert. Das PP-System braucht nur den finalen kombinierten Float. -->

#### Interface-Event: `OnStageThresholdReached`

```
Signatur:      Event OnStageThresholdReached(float Stage)
Werte:         1.0 / 2.0 / 3.0 (Aufwärts UND Abwärts)
```

#### Interface-Funktion: `GetCurrentShadowFeverStage()` (read-only)

```
Signatur:      float GetCurrentShadowFeverStage()
Rückgabe:      aktueller ShadowFever_Intensity-Wert (0.0–3.0)
```

#### Fraktions-Presets (optionale Erweiterung)

```
Signatur:      void SetFactionPPPreset(EFaction Faction)
Werte:         EFaction::Krone | EFaction::Gilden | EFaction::Orden
```

<!-- Tobi: Optionaler Vorschlag — Nami muss bestätigen ob Fraktions-PP-Presets narrativ gewünscht sind. Kein gesetztes Feature. -->

#### Zusammenfassung

Das PP-System braucht von Gameplay-Seite genau **einen Float** (0.0–3.0). Wie dieser Float berechnet wird, ist vollständig in Darius' Hand. Keine Abhängigkeit in die andere Richtung. Das PP-System feuert Events zurück. Darius abonniert, was er braucht.

---

## 6.5 Nervensystem-Visualisierung

### 6.5.1 Konzept

Das Leveling-System nutzt eine halbtransparente Nervensystem-Sicht als Visualisierung des Fortschritts. Drei Subsysteme — Cardio, Muskel, Lymph — werden als Overlay auf den Charakter-Körper projiziert.

Modi:
1. **Statistik-Ansicht** (Menü): Vollbild-Overlay, alle drei Systeme sichtbar, interaktiv
2. **Echtzeit-Overlay** (kontextabhängig): schmales Overlay — aktiv in Stufe 3 Schattenfieber, nach schweren Verletzungen, optional permanent im HUD

---

### 6.5.2 Technische Umsetzung

**Third-Person-Modus:**
- Overlay via Custom-Depth-Pass auf dem Charakter-Mesh
- Drei Materialschichten (Cardio, Muskel, Lymph) mit eigenem Emissive-Kanal
- Farb-Kodierung: Cardio = warmrot, Muskel = bernsteingelb, Lymph = kühles Grün-Weiß
- Opazität: 0.4–0.7 je nach Kontext
- Fortschritt sichtbar als Textur-Dichte und Emissive-Intensität

**First-Person-Modus:**
- Separates Arm-Mesh-Set (`SK_FP_Arms`)
- Synchron animiert mit dem Haupt-Charakter-Mesh via Animation-Blueprint
- **Aufwand-Klassifizierung**: mittel-hoch. Zeitschätzung: 3 Wochen für stabiles System.

**Shader-Struktur (M_Nervensystem_Base):**
```
Inputs:
  - BaseColor: Charakter-Skin
  - NervensystemMask_Cardio (Texture2D, R-Kanal)
  - NervensystemMask_Muskel (Texture2D, G-Kanal)
  - NervensystemMask_Lymph (Texture2D, B-Kanal)
  - Fortschritt_Cardio / _Muskel / _Lymph (Scalar 0–1 je)
  - Overlay_Opacity (Scalar 0–1)

Outputs:
  - Emissive: Farb-kodiertes Nervensystem-Leuchten
  - Custom Depth: für Compositing-Pass
```

---

## 6.6 Schwellenanker-Shader — Master Material System

<!-- Tobi: Asset-Namen: M_Schwellenanker_Master, MI_Schwellenanker_Dormant, MI_Schwellenanker_Resonant, MI_Schwellenanker_Critical, T_Schwellenanker_Riss_01, BP_Schwellenanker. -->

### 6.6.1 Konzept

Der Schwellenanker — das namensgebende Artefakt dieser Spieliteration — existiert als ein einziges Mesh mit einem Master-Material und drei Material-Instanzen. Übergänge sind immer geblended, nie hart. Der Schwellenanker ist kein Gadget; er ist ein kosmologisches Instrument.

**Zur Form**: Vera hat die Geometriebeschreibung auf "folded geological formation, compressed ossified mineral cluster" spezifiziert. Shader-Konsequenz: SSS-Radius und Riss-Topologie sind auf verdichtete, mineralische Form kalibriert.

<!-- Tobi: Vera hat die Form-Beschreibung geändert (Tag 3 Briefing). Kein großer Umbau — Parametertuning. -->

---

### 6.6.2 Drei Zustände

**Zustand 1 — Ruhezustand (dormant):**
- **Subsurface Scattering (SSS)**: aktiv, warme Untertonfarbe (RGB 1.0 / 0.85 / 0.7)
- **SSS-Radius**: 0.5 cm (mineralisch komprimiert)
- **Roughness**: 0.45–0.55
- **Emissive**: 0.0
- *Designabsicht*: Das SSS erzeugt innere Lebendigkeit — etwas ist da, schläft aber.

**Zustand 2 — Aktiver Zustand (resonant):**
- **Emissive-Layer**: warmes Indigo-Weiß (RGB 0.85 / 0.8 / 1.2, überbelichtet bei 3.5)
- **Lumen-Emitter**: aktiviert (Klasse A), Lichtfarbe CCT 7500K mit Indigo-Bias
- **Lichtradius**: 4m direkt, darüber Bloom-Halo (6.0 Radius, Indigo-Tint)
- *Designabsicht*: Sofort als Lichtquelle erkennbar. Wichtigste dynamische Lichtquelle in jeder Szene, in der er aktiv ist.

**Zustand 3 — Kritischer Zustand (überlastet):**
- **Riss-Overlay-Layer**: `T_Schwellenanker_Riss_01` — organische Rissstrukturen öffnen sich stufenlos per Blend-Parameter
- **Innenleuchten**: lokale Emissive-Intensität an Riss-Kanten (8.0+, kalt-violett)
- **SSS**: blau-violett getönt (RGB 0.7 / 0.6 / 1.3)
- **Lumen-Emitter**: flackernd, instabil (2–8 Hz unregelmäßig)
- **Vertex-Animation**: Mesh vibriert ±0.2mm, 12 Hz
- *Designabsicht*: Visuelles Vokabular entspricht PP-Stufe 3. Der Schwellenanker und das Schattenfieber sprechen dieselbe Sprache. Riss-Blend-Parameter erlaubt sequenzielles Aufziehen für Act 3.

<!-- Tobi: Namis "ein Anker kann reißen" (Tag 3 Briefing) ist für Act 3 angelegt. Kein neuer Shader-Aufwand — nur Blueprint-Kurven-Authoring. -->

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

<!-- Tobi: Neuer Abschnitt v4. Kosmologische Grundlage: Tiervolk = dauerhaft fremde Wesen in Symbiose mit Tieren (Emre, Tag 4 Briefing). Das ist keine Mutation, kein Effekt — das ist ontologischer Normalzustand. Konsequenz: eigene Materialklasse, nicht vom Schattenfieber-System abgeleitet. Vera hat Referenzbilder angefragt — 2–3 Typen. -->

### 6.7.1 Kosmologische Grundlage und Shader-Konsequenz

Das Tiervolk ist nicht krank. Es ist nicht mutiert. Es ist, was es ist — dauerhaft, kosmologisch anders. Die Symbiose zwischen tierischem Wirt und dem Fremden ist keine Infektion, sondern ein ontologischer Zustand. Technische Konsequenz: das Tiervolk-Material ist eine eigenständige Materialklasse. Es leitet sich weder vom Schattenfieber-PP-System ab noch vom Schwellenanker-Shader. Es teilt das visuelle Vokabular — Emissive, organisch, fremd — aber hat eine eigene Grammatik.

**Abgrenzung zu verwandten Systemen:**

| System | Zustand | Natur | Shader-Basis |
|---|---|---|---|
| Schattenfieber | Infektion, prozessual | pathologisch | PP-Blueprint + Overlay |
| Schwellenanker | Instrument, drei Zustände | kosmologisch | M_Schwellenanker_Master |
| Tiervolk-Symbiose | Dauerhafter Normalzustand | ontologisch fremd | M_Tiervolk_Symbiose_Master (neu) |

Diese drei Systeme teilen das gleiche visuelle Vokabular — weil sie alle denselben kosmologischen Ursprung haben. Aber sie sind technisch getrennte Systeme. Das ist Absicht.

---

### 6.7.2 Dual-Layer-Architektur

Der Tiervolk-Symbiose-Shader ist ein **Dual-Layer-System** in einem einzigen Master-Material:

- **Layer 1 — Tier-Biologie**: das tierische Substrat. SSS, Mikrooberfläche, organische Textur-Variation. Das ist das Fleisch, das Fell, die Schuppe, der Knochen.
- **Layer 2 — Das Fremde**: die kosmologische Präsenz, die von innen durch die Tier-Biologie hindurchscheint. Emissive-Maske, transluzentes Durchleuchten, eine andere Art von Licht.
- **Blend-Maske**: bestimmt, wo sich das Fremde angesammelt hat — Gelenke, Augen, Maulwinkel, Wirbelsäulen-Verlauf, Membranzwischenräume. Die Maske ist pro Charakter individuell; das Master-Material parametrisiert sie.

```
M_Tiervolk_Symbiose_Master
├── Layer 1: Tier-Biologie
│   ├── BaseColor (Texture2D — Fell/Schuppe/Haut)
│   ├── Roughness (Texture2D — Mikro-Oberfläche)
│   ├── Normal (Texture2D — Oberflächendetail)
│   ├── SSS_Color (Vector — Wärme des lebenden Gewebes)
│   ├── SSS_Radius (Scalar — je nach Gewebedichte)
│   └── SSS_Intensity (Scalar)
│
├── Layer 2: Das Fremde
│   ├── Fremd_EmissiveColor (Vector — Farbe des Fremden)
│   ├── Fremd_EmissiveIntensity (Scalar — Helligkeit, 0.0–15.0 cd/m²)
│   ├── Fremd_Translucency (Scalar — wie tief scheint es durch)
│   ├── Fremd_PulseFrequency (Scalar — langsames Atmen, Hz)
│   └── Fremd_PulseAmplitude (Scalar — Intensitätsschwankung)
│
└── Blend-Kontrolle
    ├── Symbiose_Mask (Texture2D — R-Kanal: wo sitzt das Fremde?)
    ├── Symbiose_Intensity (Scalar 0.0–1.0 — Stärke der Symbiose)
    └── Symbiose_EdgeSoftness (Scalar — Übergangsschärfe der Maske)
```

---

### 6.7.3 Layer 1 — Tier-Biologie im Detail

Das tierische Substrat muss organisch und physikalisch plausibel sein. PBR-Standardwerte, aber mit SSS — weil Gewebe Licht streut.

**SSS-Konfiguration:**
- **SSS-Farbe**: warm, je nach Tier-Typ leicht variiert (Säugetier-Ton: RGB 1.0 / 0.75 / 0.6; Reptil-Ton: RGB 0.8 / 0.85 / 0.65)
- **SSS-Radius**: 0.6–1.2 cm je nach Gewebedicke und Fell-/Schuppenbedeckung
- **SSS-Intensität**: 0.4–0.8 — lebendig, aber nicht übertrieben

**Mikrooberfläche:**
- Roughness variiert stark über die Fläche (Fell = hoch, 0.7–0.9; Schleimhäute = niedrig, 0.1–0.25; Knochen-Exposition = mittel, 0.4–0.6)
- Normal-Map-Schichtung: Basis-Normal (Fellstruktur/Schuppenstruktur) + Detail-Normal (Porendetail, Narben, Kampfspuren)

**Wichtig**: Layer 1 alleine muss ein überzeugendes Tier-Material sein. Das Fremde ist Ergänzung, kein Ersatz.

---

### 6.7.4 Layer 2 — Das Fremde im Detail

Das Fremde scheint von innen durch. Es ist kein Aufkleber auf der Oberfläche — es ist ein Leuchten aus dem Inneren, das durch das Gewebe bricht.

**Visuelle Charakterisierung:**
- Farbe: kühl, nicht warm. Leicht ins Violett-Weiße oder Blau-Weiße verschoben — dieselbe kosmologische Farbtemperatur wie der Schwellenanker-Resonanz-Zustand. Das ist kein Zufall. Alle drei kosmologischen Entitäten (Schwellenanker, Schattenfieber-Stufe 3, Tiervolk-Symbiose) sprechen dieselbe Farbsprache: kalt, transluzent, von innen leuchtend.
- Emissive-Intensität im Ruhezustand: 2–8 cd/m² (Klasse B — kein GI-Beitrag im Normalfall). In aktiven Momenten (Bedrohung, ritueller Kontext): bis 40–80 cd/m² (Klasse A, echter GI-Emitter).
- **Pulsieren**: Das Fremde atmet. Langsam. 0.1–0.3 Hz, sehr niedrige Amplitude (±15% der Basisintensität). Das ist kein Flackern — das ist ein Herzschlag, der nicht der eigene ist.

**Technisches Rendering:**
- Das Durchscheinen wird über `Fremd_Translucency` gesteuert: bei hohem Wert scheint das Emissive durch mehrere Gewebe-Lagen hindurch (wie Licht durch eine Hand)
- Custom Depth: das Fremde wird in einem separaten Compositing-Pass hinzugefügt, damit es nicht mit umgebenden Materialien blendet
- `Fremd_PulseFrequency` und `Fremd_PulseAmplitude` werden via Blueprint gesteuert — kein hartcodiertes Pulsieren im Shader selbst

---

### 6.7.5 Blend-Maske — Wo sitzt das Fremde?

Die `Symbiose_Mask` ist der entscheidende Freiheitsgrad. Sie bestimmt die Physiognomie jedes Tiervolk-Charakters: wo hat sich das Fremde angesammelt, wo ist die Tier-Biologie noch rein?

**Erwartete Muster (basierend auf Emres Weltbeschreibung, zu verifizieren durch Vera-Referenzbilder):**

| Muster-Typ | Beschreibung | Shader-Konsequenz |
|---|---|---|
| Gelenk-Konzentration | Das Fremde sammelt sich an Gelenkflächen — Knie, Ellbogen, Hüfte | Maske: runde Blobs an Gelenkpositionen, weiche Kanten |
| Augen/Sensorik | Augen und Sinnesorgane als Hotspot — "sehen durch die Schwelle" | Maske: präzise Kreise, harte Kanten, höhere Emissive-Intensität |
| Wirbelsäulen-Verlauf | Das Fremde folgt der Nervenbahn | Maske: lineare Struktur entlang Rückgrat, medium-weiche Kanten |
| Diffuse Verteilung | Das Fremde ist gleichmäßig verteilt, nirgendwo konzentriert | Maske: gleichmäßiges Low-Intensity-Rauschen über gesamte Oberfläche |

<!-- Tobi: Vera-Referenzbilder (2–3 Typen) sind der Schlüssel für die finalen Masken-Muster. Ohne Referenz schreibe ich Shader-Parameter ins Blaue. Sobald Vera liefert, kalibriere ich SSS-Radius und Masken-Topologie pro Typ. Die vier Muster-Typen hier sind Hypothesen — keine finalen Entscheidungen. -->

**Masken-Erstellung in der Pipeline:**
1. Character-Art erstellt UV-Layout pro Tiervolk-Charakter
2. Masken-Textur wird in Substance Designer auf Basis des UV-Layouts gemalt (R-Kanal: Symbiose-Stärke, 0–1)
3. Optional: prozedurale Variation über PCG für Crowd-Varianten (Hintergrund-NPCs)

---

### 6.7.6 Material-Instanzen und Varianten

**Master-Material**: `M_Tiervolk_Symbiose_Master`

**Geplante Instanz-Typen** (vorläufig — abhängig von Vera-Referenzbildern):

| Instanz | Tier-Basis | Fremd-Farbe | Muster-Typ | Lumen-Klasse |
|---|---|---|---|---|
| `MI_TV_Saeugetier_Ruhig` | Fell, warm | Violett-Weiß | Gelenke | Klasse B |
| `MI_TV_Saeugetier_Aktiv` | Fell, warm | Violett-Weiß, intensiver | Gelenke + Augen | Klasse A (aktiv) |
| `MI_TV_Reptil_Ruhig` | Schuppe, kühl | Blau-Weiß | Diffus | Klasse B |
| `MI_TV_Reptil_Aktiv` | Schuppe, kühl | Blau-Weiß, intensiver | Diffus + Wirbel | Klasse A (aktiv) |

<!-- Tobi: Instanz-Anzahl und Tier-Typen sind nicht bestätigt. Das hier sind Platzhalter für die Pipeline-Planung. Emre und Vera müssen die finale Bandbreite der Tiervolk-Tierformen definieren. -->

**Namens-Konvention Asset-Pipeline:**
- Master: `M_Tiervolk_Symbiose_Master`
- Instanzen: `MI_TV_{TierTyp}_{Zustand}` (Beispiele: `MI_TV_Wolf_Ruhig`, `MI_TV_Rabe_Aktiv`)
- Masken: `T_TV_{CharName}_Symbiose_Mask` (per Charakter)
- Blueprint: `BP_Tiervolk_Symbiose_Controller` (steuert Puls, Aktivierungs-Übergänge)

---

### 6.7.7 Animations-Verknüpfung und aktive Zustände

Das Fremde reagiert auf den Kontext. Es hat zwei Zustände:

**Ruhezustand (Standard):**
- Pulsiert langsam (0.1–0.2 Hz)
- Klasse B — kein GI-Overhead
- `Symbiose_Intensity` = 0.4–0.7 je nach Charakter-Lore

**Aktiver Zustand (Bedrohung, Ritual, Willenssetzung):**
- `BP_Tiervolk_Symbiose_Controller` erhöht `Fremd_EmissiveIntensity` via Timeline
- Lumen-Emitter-Flag wechselt zu Klasse A
- Pulsfrequenz erhöht auf 0.6–1.2 Hz
- Übergang: smooth geblended, mindestens 0.5 Sekunden
- Trigger kommt aus dem Gameplay-Blueprint (AI-Zustandsmaschine oder Script-Event)

**Interface zu Gameplay:**
```
Signatur:      void SetTiervolkSymbioseState(ETiervolkState State)
Werte:         ETiervolkState::Ruhig | ETiervolkState::Aktiv
```

<!-- Tobi: Einfaches Interface — nur zwei Zustände, kein Float. Das Tiervolk hat keine Progression. Es ist, was es ist. -->

---

### 6.7.8 Aufwandsschätzung

| Aufgabe | Aufwand | Wer |
|---|---|---|
| M_Tiervolk_Symbiose_Master bauen | 1 Woche | Tech-Art |
| BP_Tiervolk_Symbiose_Controller | 3 Tage | Tech-Art |
| Masken-Textur pro Hero-Charakter (Salva, weitere) | 2–3 Tage je | Character-Art |
| Substance-Designer-Masken-Workflow dokumentieren | 1 Tag | Tech-Art |
| PCG-Varianten für Crowd-NPCs | 1 Woche | Tech-Art + PCG-Artist |
| **Gesamt (konservativ)** | **3–4 Wochen** | — |

*Puffer einplanen*: Vera-Referenzbilder sind Voraussetzung für Masken-Kalibrierung. Ohne die liegen die Hero-Masken in der Luft. Drei bis vier Wochen gilt, sobald Vera liefert.

---

## 6.8 Houdini-Pipeline — Terrain und Prozedurale Systeme

### 6.8.1 Terrain-Generierung

Die vertikale Stadt braucht eine Basis-Topografie: das Flusstal, die Hügelketten, die natürlichen Erhebungen.

**Workflow:**
1. Basis-Terrain in **Houdini** procedural generiert (Houdini Heightfield-System)
2. Export als `.hdr`-Heightmap nach UE5 (16-bit, 4096×4096 für Kernregion)
3. In UE5: Landscape-System mit Nanite-Tessellation für Nahbereich
4. Automatisches Foliage-Placement via PCG

**Houdini-Setup:**
- Basis-Erosion: hydraulische Erosion für naturwirkende Täler und Rinnsale
- Stadtplattform-Sculpting: manuelle Terrassen-Formen als Kontrollkurven in Houdini
- Fluss-System: Heightfield-Vexnet für Flussbettgenerierung
- Output-Auflösungen: 4k für Terrain-Kern (2km Radius), 2k für äußere Bereiche (10km Radius)

<!-- Tobi: Houdini-Terrain wartet auf Emres Topos-Kapitel (Stadtname, Sichtachsen, Gebirgs-Kontext). Sobald Topos verfügbar: erste Constraint-Kurven im Heightfield-Setup. -->

---

### 6.8.2 Prozedurale Stadtdetails (PCG-Systeme)

Für wiederholende Stadtdetails wird ein PCG-System aufgebaut:

- **Pflaster-Variation**: PCG platziert Stein-Typ, Rotation, Abnutzungsgrad basierend auf Nähe zu Fußwegen und Schicht-Tiefe
- **Fassaden-Ageing**: prozedurale Wear-Maps generiert in Houdini, instanziiert via PCG
- **Biolumineszenz-Cluster**: Niagara-Systeme via PCG in Layer-0-Bereichen, Dichte abhängig von Wassernähe
- **Vegetation-Infiltration**: prozedurale Pflanzen-Cluster in Slum-Bereichen aus Rissen

---

## 6.9 Color Science & Display-Pipeline

### 6.9.1 Color-Management

RELICS nutzt **ACES** (Academy Color Encoding System) als Farbraum-Standard.

**Pipeline:**
```
Kreativ-Input → ACEScg Arbeitsraum → ACES Tonemapping → Display-Transform (sRGB/DCI-P3)
```

- Alle Texturen: in sRGB gespeichert, im Shader in lineares Licht konvertiert
- Emissive-Werte: in physikalischen Einheiten (cd/m²) definiert
- LUT: ein Basis-LUT für den RELICS-Look, drei Varianten (Normal / Schattenfieber-Stufe-2 / Schattenfieber-Stufe-3)

**Warum kein AgX?** AgX komprimiert Highlights weicher — für Photography optimal, für RELICS falsch. Die Bergkristall-Linsen und der Schwellenanker müssen leuchten, nicht weich werden. ACES gibt uns das.

---

### 6.9.2 Display-Kalibrierung (internes Studio)

Alle Arbeitsstationen haben kalibrierte Displays (Delta-E < 2.0). Referenz-Display: Samsung Odyssey OLED. Alle Emissive-Werte sind so kalibriert, dass sie auch auf Standard-SDR (sRGB, 200 cd/m² Peak) korrekt wirken. HDR-Displays bekommen automatisch einen separaten Display-Transform.

---

## 6.10 Produktion & Release-Pipeline

### 6.10.1 Milestone-Übersicht

| Milestone | Technischer Status | Schlüssel-Deliverables |
|---|---|---|
| **Pre-Alpha** | Prototyp-Pipeline | Rendering-Architektur steht, Material-Master-Systeme gebaut, World Partition stabil |
| **Alpha** (Streamer) | Feature-Freeze Rendering | Data Layers gesetzt, Lumen-Konfiguration fixiert, PP-System stabil, alle Shader-Master stabil |
| **Beta** | Tuning-Phase | Performance-Optimierung, visuelle Feinheit, Accessibility vollständig |
| **Full Release** | Feinschliff + große Setpieces | Abschließender Lighting-Pass, Cinematic-Sequenzen final |
| **DLC** | Erweiterung auf stabiler Basis | Neue Assets auf bestehenden Systemen — kein neues technisches Risiko |

**Alpha ist der härteste Freeze.** Nach Alpha-Abgabe sind folgende Systeme nicht mehr änderbar:
- Data Layer-Struktur (Schichtanzahl, Naming, Streaming-Logik)
- Lumen-Konfiguration (RT-Modus pro Layer)
- Schattenfieber-PP-System-Architektur (Blueprint-Struktur, Parameter-Namen)
- Schwellenanker-Master-Material-Struktur (Parameter-Gruppen, Slot-Namen)
- Tiervolk-Symbiose-Master-Material-Struktur (Parameter-Gruppen, Slot-Namen)
- Kamerasystem-Grundstruktur
- Interface-Spezifikation Lymph → PP-Trigger (Funktionsnamen, Parameter-Typen, Event-Namen)
- Interface-Spezifikation Tiervolk → Gameplay (Funktionsnamen, Zustandstypen)

*Begründung*: Tuning ist erlaubt. Umstrukturierung bricht abhängige Systeme.

---

### 6.10.2 Pre-Alpha — Technische Prioritäten

**Woche 1–4: Foundation**
- UE5 Projekt-Setup, Engine-Version fixieren
- World Partition aktivieren, vier Data Layers anlegen und testen
- Lumen-Konfiguration pro Layer einrichten
- Erste Prototyp-Materialien: Oberschicht, Unterschicht, Emissive-Klasse-A

**Woche 5–8: Kernsysteme**
- Schattenfieber-Blueprint (alle drei Stufen, smooth geblended)
- Lymph-PP-Interface implementiert und mit Gameplay-Team getestet
- Schwellenanker-Master-Material (alle drei Zustände)
- Tiervolk-Symbiose-Master-Material (Prototyp mit einer Instanz)
- Kamerasystem (Third/First Person Blend)
- Nervensystem-Shader (Third-Person-Modus)

**Woche 9–12: Integration**
- Biolumineszenz-Pipeline (Klasse A/B/C operativ)
- PCG-System für erste Straßen-Füllung
- Houdini-Terrain-Export → UE5 getestet
- Accessibility-Optionen implementiert und getestet
- Interne Alpha-Kandidat: alle Systeme laufen, kein Polishing

---

### 6.10.3 Monetarisierung — Technische Implikation

Das Briefing ist eindeutig: **Klassisch Premium, keine Mikrotransaktionen.**

Kein Live-Service-Backend. Offline-first, Save-Game ist lokal, kein Always-Online-Requirement. DLC-Content wird als Pak-Files geliefert. Kein Platzhalter für DLC im Basis-Spiel.

---

## 6.11 Risiko-Register

| System | Priorität | Risiko | Mitigation |
|---|---|---|---|
| Lumen vertikale GI | HOCH | Degeneriert in tiefen Kanälen | Hybrid Baked für Layer 0, Lumen-Importance-Volumes |
| World Partition vertikal | HOCH | UE5 primär horizontal konzipiert | Manuelle Data Layers, Occlusion Volumes an Ebenen-Übergängen |
| Schattenfieber PP Accessibility | HOCH | Vertex-Animation und DOF-Pulsieren = Motion-Sickness-Risiko | Accessibility-Option Pflicht, intern getestet |
| Nanite dünne Geometrien | MITTEL | Absturz bei dünnen Meshes | Fallback-LOD-Workflow definiert, Asset-Klassifizierung obligatorisch |
| Biolumineszenz Performance | MITTEL | Viele Emitter = GI-Overhead | Dreiklassen-System, Klasse-A-Budget max. 12 gleichzeitig |
| Nervensystem Arm-Mesh | MITTEL | Hoher Animations-Aufwand im FP-Modus | Eigenständiger Task, 3-Wochen-Schätzung |
| Tiervolk-Symbiose-Shader | MITTEL | Masken-Qualität abhängig von Vera-Referenzbildern | Blocker identifiziert — Vera-Referenzen vor Shader-Finalisierung |
| Schwellenanker-Shader-Synchronität | NIEDRIG | State-Alpha-Drift zwischen Blueprint und Material | Interface-Konvention festgelegt, Parameternamen dokumentiert |
| Lymph-PP-Interface-Drift | NIEDRIG | Gameplay ändert Parameternamen nach Alpha-Freeze | Interface-Namen in 6.4.7 festgeschrieben, Alpha-Freeze gilt |

---

## 6.12 Offene Fragen & Abhängigkeiten

| Frage | An wen | Dringlichkeit | Status |
|---|---|---|---|
| ~~Wie diskret sind die Stadtebenen-Übergänge?~~ | Vera | ~~KRITISCH~~ | **ERLEDIGT** (Tag 2): oben fließend, unten diskret |
| ~~Wie triggert das Lymph-Subsystem die PP-Stufen?~~ | Darius | ~~Hoch~~ | **ERLEDIGT** (Tag 3): Interface in 6.4.7 |
| ~~Sind Tiervolk-Siedlungen statisch oder mobil?~~ | Emre | ~~Mittel~~ | **ERLEDIGT** (Tag 4): statisch, Layer-gebunden |
| Welche Sichtachsen / Constraint-Punkte für Houdini-Terrain? | Vera / Emre | Hoch | Offen — wartet auf Topos-Kapitel |
| Vera: 2–3 Tiervolk-Referenzbilder (wo sitzt das Fremde?) | Vera | Hoch | Ausstehend — angefragt Tag 4 |
| Braucht Fraktionswahl unterschiedliche PP-Presets? | Nami | Mittel | Offen — optionale Erweiterung in 6.4.7 vorskizziert |
| Orden-Kreuz-Vektor für Shader-Texture-Atlanten | Vera | Mittel | Offen — wartet auf Art-Direction-Entscheidung |
| Finale Bandbreite Tiervolk-Tierformen (Instanz-Anzahl) | Emre / Vera | Mittel | Offen — beeinflusst MI-Anzahl in 6.7.6 |

---

*Dokument-Status*: Version 4.0. Neuer Abschnitt 6.7 (Tiervolk-Symbiose-Shader) ergänzt — Dual-Layer-Architektur, Blend-Maske, Aufwandsschätzung. Tiervolk-Siedlungen-Frage (6.4.6, 6.12) als erledigt markiert. Risiko-Register um Tiervolk-Shader-Eintrag erweitert. Alpha-Freeze-Liste um Tiervolk-Interface ergänzt. Seitenbudget-Pass: redundante Inline-Erklärungen gestrafft.

*Pipeline-Bibel*: Alle Shader-Parameter und Blueprint-Architekturen aus diesem Dokument werden in die interne Pipeline-Bibel übertragen (separates internes Dokument, nicht GDD).
