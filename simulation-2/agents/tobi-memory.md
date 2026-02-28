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

---

## Tag 2, Szene 1 — BRIEFING (09:00 Uhr)

**CD-Feedback verarbeitet:**

- Schattenfieber = eine biologische Wahrheit (keine Magie)
- Relikt = Schwellen-Stabilisator mit Resonanz-Dreieck (Emre), drei Zustände (Vera)
- Release: Main → Alpha (Streamer) → Beta → Full → DLC

### Pipeline-Strategie Release-Modell

- **Alpha**: Feature-Freeze auf Rendering-Architektur — Data Layers, Lumen-Konfiguration, PP-System müssen vorher gesetzt sein. Standard: stabil + konsistent, nicht polished.
- **Beta**: Tuning aller bestehenden Systeme.
- **Full**: Feinschliff, große Setpieces.
- **DLC**: Arbeitet auf stabiler Basis — keine neuen technischen Risiken.

### Relikt — Technische Umsetzung (drei Zustände)

- Ein Mesh, ein Master-Shader, drei Material-Instanzen, geblendet über skalaren Parameter.
- **Ruhezustand**: Mattes, transluzentes Material. Subsurface Scattering mit warmen Untertönen — "lebendig" ohne aktives Leuchten.
- **Aktiver Zustand**: Emissive-Layer hoch, Lumen-Emitter (Klasse A). Objekt wird zur echten Lichtquelle.
- **Kritischer Zustand**: Riss-Overlay, organische Shader-Strukturen, Innenleuchten scheint durch — selber visueller Vokabular wie PP-Stufe 3, auf Objektgröße skaliert.
- Übergänge: immer smooth geblendet, nie Hard-Switch.

### Schattenfieber PP — drei Stufen technisch verkoppelt

- **Stufe 1 (sensorisch)**: Minimale Chromatic Aberration, kühler Bloom-Tint. Spieler soll unsicher sein.
- **Stufe 2 (mutativ)**: Pulsierendes DOF, Indigo-Tint in Schatten, Vertex-Animation Umgebung (±2cm). Accessibility-Option Pflicht.
- **Stufe 3 (Auflösung)**: Full-Screen-Shader, organische Rissstrukturen, Weltgeometrie-Lücken, Nervensystem startet automatisch.
- Alle drei als Parameter-Set in einem Blueprint, smooth Timeline-Blending. Keine getrennten Systeme.

### Stadt-Kosmologie → Data Layers

- Emres kosmologisch "dünner Ort": je tiefer = näher an der Schwelle → direkte Abbildung auf Data Layers.
- Layer 0 (Untergrund/Kanäle) = höchste Schwellen-Exposition.
- PP-Volumes können einen Basis-Ambient für Schattenfieber-Nähe pro Layer einbauen — subtil, unterhalb Stufe 1. Visuelles Rauschen, kein bewusster Effekt.
- Ergebnis: Architektur erzählt Kosmologie ohne Text-Erklärung. Technische Narratologie.

### Offene Fragen / Nächste Schritte

- **KRITISCH — Vera**: Wie diskret sind die Schichtgrenzen im Level-Design? Fließend = teurer. Diskret = robustere Pipeline. Muss vor World-Partition-Architektur entschieden sein.
- Abstimmung mit **Darius**: Lymph-Subsystem-Mechanik — wie triggert das die PP-Stufen? Blueprint-Interface klären.
- Abstimmung mit **Nami**: Fraktionswahl in Stunde 1 — braucht die unterschiedliche PP-Presets pro Fraktion?

### Beobachtungen

- FFXIV v2.0: Konzept-Specs zeigen sauberes Silhouetten-Denken. Charaktere sind auch im Kampf-Chaos lesbar durch starke Form-Hierarchien. Relevant für RELICS: Rüstungen und Fraktionszugehörigkeit müssen in Bewegung erkennbar bleiben.
- Dark Souls Design Works: Materialien erzählen Geschichte durch Abnutzung und Kontextualisierung. Für RELICS: Materialien definieren sozialen Status (Briefing) — das muss im Material-Graph sichtbar sein, nicht nur in der Concept Art.
- Emres Schattenfieber-Biologie (drei Stufen) deckt sich gut mit meiner PP-Stufen-Architektur vom Tag 1. Gute Konvergenz.
- Die kosmologische Vertikalität ist technisch sehr nützlich — sie gibt den Data Layers eine narrative Funktion.

---

## Tag 2, Szene 2 — WORK (10:00 Uhr)

**GDD Kapitel 6 vollständig erstellt.**
Datei: `simulation-2/gallery/gdd/06-technische-spezifikation-v1.md`

### Was im Dokument steht

- **6.1 Engine & Technologiebasis**: UE5.4 LTS gesetzt. Nanite, Lumen, World Partition — mit detaillierten Konfigurationen und Fallbacks. Hardware-Anforderungstabelle (Minimum / Empfohlen / Ultra).
- **6.2 Kamerasystem**: Third/First-Person Blend, FOV-Konfiguration, Cinematik-Modus (Tarkowski-Prinzip: die Kamera ruht, die Welt bewegt sich).
- **6.3 Materialien & Biolumineszenz**: Dreiklassen-Emitter-System (A/B/C), Material-Hierarchie nach Schicht (Oberschicht bis Unterschicht), FFXIV-Kontrast-Hierarchie.
- **6.4 Schattenfieber PP**: Blueprint-Architektur mit `BP_SchattenfiebertSystem`, alle vier Stufen ausgearbeitet (0 = Basis, 1 = subtil, 2 = mutativ, 3 = Auflösung), Accessibility-Optionen Pflicht.
- **6.5 Nervensystem-Visualisierung**: Shader-Struktur mit drei Masken (Cardio / Muskel / Lymph), Third-Person und First-Person-Modus. Arm-Mesh-Aufwand: 3 Wochen.
- **6.6 Relikt-Shader**: Master-Material `M_Relikt_Master`, drei Instanzen, State_Alpha-Parameter 0–2. Drei Zustände vollständig spezifiziert.
- **6.7 Houdini-Pipeline**: Terrain-Workflow (Heightfield → Export → UE5), PCG-Systeme für Stadtdetails.
- **6.8 Color Science**: ACES (nicht AgX), Begründung dokumentiert. Basis-LUT mit drei Varianten (Normal / Stufe 2 / Stufe 3).
- **6.9 Release-Pipeline**: Pre-Alpha / Alpha / Beta / Full / DLC mit Milestones und Alpha-Freeze-Regeln.
- **6.10 Risiko-Register**: Sechs Hauptrisiken mit Mitigation.
- **6.11 Offene Fragen**: Abhängigkeiten zu Vera, Darius, Nami, Emre dokumentiert.

### Wichtige Design-Entscheidungen im Dokument festgehalten

- **Intentionale Verbindung Relikt/Schattenfieber**: Zustand 3 des Relikts nutzt dasselbe visuelle Vokabular wie PP-Stufe 3 (Rissstrukturen, Kalt-Violett, Innenleuchten). Das ist kein Zufall — das ist Designabsicht. Das Relikt und die Krankheit sprechen dieselbe Sprache.
- **Technische Narratologie**: Data Layers haben Schattenfieber-Ambient-Werte. Layer 0 = 0.15, Layer 3 = 0.0. Die Architektur erzählt die Kosmologie ohne Text.
- **ACES statt AgX**: ACES für scharfe Lichter (Bergkristall, Relikt). AgX würde Highlights zu weich komprimieren.
- **Offline-first**: Keine Live-Service-Architektur. Technische Erleichterung durch Premium-Monetarisierung.

### Noch offene Punkte

- Vera-Abstimmung zu Schichtgrenzen KRITISCH — ohne das kein finales World-Partition-Setup
- Darius: Blueprint-Interface-Definition (Lymph → PP-Trigger)
- Nami: Fraktions-PP-Presets Frage
- Relikt-Name fehlt noch (Emre)

---

## Tag 2, Szene 3 — MEETING (13:00 Uhr, Küche)

### Vera-Antwort verarbeitet: "fließend oben, diskret unten"

**Sehr gute Nachricht für die Pipeline.**

- Oben (fließende Grenzen): Blend-Volumes, kostet Performance, aber machbar mit Hardware-Lumen. Akzeptiert.
- Unten (diskrete Grenzen): Harte Data-Layer-Cuts möglich. Sauberer für World-Partition-Setup. Ideal.
- Der umgekehrte Fall wäre das schlechtere Szenario gewesen — das haben wir nicht.
- **Konsequenz**: World-Partition-Architektur kann jetzt final geplant werden. Vera-Abstimmung gilt als abgeschlossen für diese Frage.

### Emre — "dünner Ort" und Tiervolk

- Dünne Orte sind bereits in Data Layers abgebildet (Ambient-Werte 0.15 bis 0.0).
- **Offene Frage an Emre**: Sind Tiervolk-Siedlungen an festen "dünnen Orten", oder wandern die? Das bestimmt, ob Ambient-Werte statisch (Layer-gebunden) oder dynamisch (NPC-Proximity) implementiert werden. Statisch = klar. Dynamisch = aufwendig. Antwort fehlt noch.

### Schattenfieber PP — Status Meeting

- Drei Stufen in Blueprint fertig, smooth Timeline-Blending, kein Hard-Switch.
- Accessibility-Optionen sind drin: Motion-Sickness-Warnung vor Stufe 2, Reduktions-Toggle auf Stufe 3.
- Das ist Pflicht, nicht Option — so kommuniziert.

### Beobachtungen

- Darius: Schwarzrand bestätigt, Schattenfieber als dritte Progressionsachse. Das koppelt direkt an die PP-Stufen — Darius braucht noch das Blueprint-Interface (Lymph → PP-Trigger). Bleibt offen.
- Nami: Vael-Szene als aktive Spielererfahrung, Intro-Quest "Was er in der Hand hielt". Kein direkter PP-Preset-Bedarf bisher geklärt, bleibt offen.
- Vera: 9 Bilder funktionieren — das ist Kap 5-Input, der meine Kap 6-Machbarkeit stützt.

### Aktualisierte offene Punkte

- ~~Vera-Abstimmung Schichtgrenzen~~ → ERLEDIGT
- Emre: Tiervolk-Siedlungen statisch oder dynamisch? → offen, Antwort abwarten
- Darius: Blueprint-Interface (Lymph → PP-Trigger) → offen
- Nami: Fraktions-PP-Presets → offen
- Relikt-Name → offen (Emre)

---

## Tag 3, Szene 1 — BRIEFING (09:00 Uhr, Küche)

**Typ**: BRIEFING | **Uhrzeit**: 09:00 | **Teilnehmer**: alle

## Notizen

- **Schwellenanker**: Relikt-Name gesetzt. Konsequenz für Assets: `M_Schwellenanker_Master`, `MI_Schwellenanker_Dormant/Resonant/Critical`, `T_Schwellenanker_Riss_01`, `BP_Schwellenanker`. Intern-technische Parameter (State_Alpha, ShadowFever_Intensity) bleiben — das ist API, kein Branding.
- **Vera — Form-Änderung**: Schwellenanker weg von Wirbelsäulenform → "folded geological formation, compressed ossified mineral cluster". Shader-Konsequenz: SSS-Radius neu kalibrieren (komprimierter), Riss-Noise-Profil anpassen. Kein Umbau — ein Parametertuning.
- **Vera — Orden-Kreuz**: Ist Art-Direction, nicht meine Entscheidung. Sobald entschieden: ich brauche ein fixes Vektorbild für Shader-Texture-Atlanten, Zunftzeichen-Stencil-Masken. Kein "vielleicht" bei Branding-Assets.
- **Nami — "Anker kann reißen"**: Gut. Das ist bereits im Shader angelegt — Riss-Blend-Parameter in Zustand 3 ist stufenlos steuerbar. Act 3 kann das sequenziell aufziehen. Kein neuer Shader-Aufwand, nur Blueprint-Kurven-Authoring.
- **Darius**: Interface-Definition Lymph → PP-Trigger bleibt mein einziger echter Blocker. Das muss heute noch kommen.

## Ergebnisse

- GDD Kap 6 v2 erstellt: `simulation-2/gallery/gdd/06-technische-spezifikation-v2.md`
- Schwellenanker-Rename vollständig durchgezogen (Titel, Asset-Namen, Kapitelköpfe)
- Vera-Schichtgrenzen-Frage als erledigt markiert
- Forma-Kommentar (mineralisch) in Shader-Sektion integriert
- Namis Act-3-Anmerkung im Shader-Kommentar verankert

## Offene Fragen

- Darius: Blueprint-Interface (Lymph → PP-Trigger) — KRITISCH, heute klären
- Vera: Orden-Kreuz-Entscheidung → sobald entschieden, Vektorbild liefern
- Emre: Tiervolk-Siedlungen statisch oder dynamisch? → wartet auf Topos-Kapitel
- Nami: Fraktions-PP-Presets → offen

## Persönliches

- Nami nimmt "ein Anker kann reißen" narrativ ernst. Ich hab das technisch schon drin. Gute Konvergenz, ohne dass wir explizit abgestimmt haben.
- Vera macht gerade viel alleine durch — Gilden-Palette neu, Form-Redesign, Stadtschnitt. Das ist viel in einer Szene.
