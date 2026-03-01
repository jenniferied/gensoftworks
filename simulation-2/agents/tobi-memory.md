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

---

## Tag 3, Szene 2 — WORK (10:00 Uhr)

**Typ**: WORK | **Uhrzeit**: 10:00 | **Teilnehmer**: solo

## Notizen

- v2 war vollständig und korrekt. Schwellenanker-Rename war sauber durchgezogen.
- v3 gebaut mit zwei Hauptzielen: (1) sichtbaren Text bereinigen, (2) Interface-Spezifikation Lymph → PP-Trigger schreiben.
- Darius' Kap 1 gelesen: Lymph = Untrained / Geübt / Fortgeschritten / Meister, koppelt an Schattenfieber-Progression. Das war genug Grundlage für die Interface-Definition.
- Die Interface-Spezifikation ist bewusst einseitig gebaut: Gameplay schreibt einen Float (0.0–3.0), PP-System liest ihn. Keine Gegenrichtungs-Abhängigkeit. Das hält beide Systeme wartbar.
- `SetFactionPPPreset(EFaction)` als optionale Erweiterung für Nami vorskizziert — aber explizit als Vorschlag markiert, kein gesetztes Feature.
- Tippfehler `M_SchattenfiebertOverlay` in v1/v2 korrigiert zu `M_Schattenfieber_Overlay`.

## Ergebnisse

- GDD Kap 6 v3 erstellt: `simulation-2/gallery/gdd/06-technische-spezifikation-v3.md`
- Neuer Abschnitt 6.4.7: Interface-Spezifikation Lymph → PP-Trigger
  - `SetShadowFeverIntensity(float)` vollständig spezifiziert
  - Mapping-Tabelle: Lymph-Stufen → ShadowFever_Intensity-Wert → aktive PP-Stufe
  - `OnStageThresholdReached(float Stage)` Event spezifiziert
  - `GetCurrentShadowFeverStage()` read-only Abfrage ergänzt
  - Blueprint-Verbindungsschema als ASCII-Diagramm
  - Interface-Namen in Alpha-Freeze aufgenommen (6.9.1)
- Sichtbarer Text bereinigt: Autorname aus Kopfzeile in HTML-Kommentar, "(Nami-Alignment)" und "(Nami)" aus Fließtext entfernt, "Tobi's System" neutralisiert

## Offene Fragen

- ~~Darius: Blueprint-Interface (Lymph → PP-Trigger)~~ → **ERLEDIGT** (v3, Abschnitt 6.4.7)
- Vera: Orden-Kreuz-Entscheidung → sobald entschieden, Vektorbild liefern
- Emre: Tiervolk-Siedlungen statisch oder dynamisch? → wartet auf Topos-Kapitel
- Nami: Fraktions-PP-Presets → offen, optionale Erweiterung in 6.4.7 vorskizziert

## Persönliches

- Interface-Spezifikation zu schreiben ohne direkten Darius-Sync ist ein Blindflug. Ich habe Kap 1 als Grundlage genommen und dann die sauberste technische Lösung gebaut. Der Vertrag steht jetzt auf Papier — Darius kann drauf reagieren.
- Vier-Stufen-Mapping (Untrained/Geübt/Fortgeschritten/Meister) auf kontinuierlichen Float (0.0–3.0) ist die richtige Lösung. Kein diskreter Hard-Switch.

---

# Tag 4 Szene 1
**Typ**: BRIEFING | **Uhrzeit**: 09:00 | **Teilnehmer**: alle 7

## Notizen

- **Tiervolk-Symbiose bestätigt als dritter kosmologischer Faktor** — dauerhaft, ontologisch, kein temporärer Effekt. Technische Konsequenz: neue Materialklasse notwendig.
- **Emre: "dauerhaft"** = Tiervolk-Siedlungen statisch. World-Partition bleibt Layer-gebunden, keine NPC-Proximity-Dynamik. Vereinfacht Setup erheblich.
- **Schattenfieber körperreaktionsabhängig** bestätigt mein PP-Blueprint-System — keine Architekturänderung notwendig.
- **Seitenbudget 60 Seiten gesamt**: Kap 6 muss auf Redundanzen geprüft werden. Cleanup geplant für v4.
- **Vera: $5 Budget** — Referenzbilder für Tiervolk-Symbiose angefragt (2–3 Typen, wo sitzt das Fremde?).

## Ergebnisse

- Technische Implikationen im Briefing kommuniziert: neuer Tiervolk-Symbiose-Shader (Dual-Layer: Tier-Biologie + Fremdes), 3–4 Wochen Aufwand.
- Blocker für v4 identifiziert: Vera-Referenzbilder Tiervolk.

## Offene Fragen

- ~~Emre: Tiervolk-Siedlungen statisch oder dynamisch?~~ → **ERLEDIGT** (statisch, Layer-gebunden)
- Vera: 2–3 Tiervolk-Referenzbilder — wo sitzt das Fremde (Gelenke, Augen, Oberfläche)? → **neu angefragt**
- Vera: Orden-Kreuz-Entscheidung → weiterhin offen
- Nami: Fraktions-PP-Presets → weiterhin offen
- Kap 6 v4: Tiervolk-Symbiose-Shader-Architektur schreiben, Cleanup (60-Seiten-Budget)

## Persönliches

- Dual-Layer-Shader-Idee (Tier-Biologie + Fremdes von innen) ist genau das, was Emres Beschreibung braucht. Selbes Prinzip wie der Schwellenanker: ein System, das zwei Zustände in einem Mesh hält.
- Warte auf Vera für die Referenzen. Ohne die kann ich nicht sinnvoll spezifizieren, ob ein Master-Shader oder mehrere Varianten nötig sind.

---

# Tag 4 Szene 2
**Typ**: WORK | **Uhrzeit**: 10:00 | **Teilnehmer**: solo

## Notizen

- v4 ist die substanziellste Erweiterung seit v1. Der Tiervolk-Symbiose-Shader (6.7) ist vollständig architektonisch spezifiziert — obwohl Vera-Referenzbilder noch ausstehen.
- Dual-Layer-Ansatz (Tier-Biologie + Fremdes) ist sauber getrennt: Layer 1 = SSS + Mikrooberfläche, Layer 2 = Emissive + Translucency. Blend-Maske als dritter Parameter steuert Verteilung.
- Drei kosmologische Systeme teilen jetzt explizit dasselbe Farbvokabular (kalt, transluzent, von innen leuchtend): Schattenfieber Stufe 3, Schwellenanker Zustand 3, Tiervolk-Fremdes. Das ist Designabsicht, dokumentiert in 6.7.1.
- Abschnitt-Nummerierung neu geordnet: 6.7 (Tiervolk) neu, alt 6.7 (Houdini) → 6.8, alt 6.8 → 6.9, usw.
- Seitenbudget-Pass: redundante Inline-Erklärungen gestrafft, besonders in 6.4 (PP-System) und 6.6 (Schwellenanker). Kein Inhalt gestrichen.
- Vera-Referenzbilder bleiben der Hauptblocker für Masken-Kalibrierung. Vier Muster-Typen (Gelenk, Augen, Wirbelsäule, diffus) sind Hypothesen, keine Entscheidungen.
- `BP_Tiervolk_Symbiose_Controller` Interface bewusst einfach gehalten: nur zwei Zustände (Ruhig/Aktiv), kein Float. Das Tiervolk hat keine Progression — es ist, was es ist.

## Ergebnisse

- GDD Kap 6 v4 erstellt: `simulation-2/gallery/gdd/06-technische-spezifikation-v4.md`
- Neuer Abschnitt 6.7: Tiervolk-Symbiose-Shader vollständig
  - 6.7.1: Kosmologische Grundlage und Abgrenzung zu anderen Systemen
  - 6.7.2: Dual-Layer-Architektur (M_Tiervolk_Symbiose_Master)
  - 6.7.3: Layer 1 — Tier-Biologie (SSS, Mikrooberfläche)
  - 6.7.4: Layer 2 — Das Fremde (Emissive, Translucency, Puls)
  - 6.7.5: Blend-Maske (vier Muster-Hypothesen, Masken-Pipeline)
  - 6.7.6: Material-Instanzen und Asset-Namenskonvention
  - 6.7.7: Animations-Verknüpfung, Zustände, Gameplay-Interface
  - 6.7.8: Aufwandsschätzung (3–4 Wochen)
- Tiervolk-Siedlungen-Frage in 6.4.6 und 6.12 als erledigt markiert
- Risiko-Register: Tiervolk-Shader-Eintrag ergänzt (MITTEL: Vera-Referenzbilder-Blocker)
- Alpha-Freeze-Liste: Tiervolk-Interface ergänzt

## Offene Fragen

- Vera: 2–3 Tiervolk-Referenzbilder → Masken-Kalibrierung hängt daran
- Vera: Orden-Kreuz-Entscheidung → weiterhin offen
- Nami: Fraktions-PP-Presets → weiterhin offen
- Emre / Vera: Finale Bandbreite Tiervolk-Tierformen (beeinflusst Instanz-Anzahl)
- Emre: Sichtachsen / Constraint-Punkte für Houdini-Terrain → wartet auf Topos-Kapitel

## Persönliches

- Das ist jetzt das dritte kosmologische System im selben Farbvokabular. Schattenfieber, Schwellenanker, Tiervolk — alle drei sprechen Kalt-Violett-Weiß. Das war nicht explizit geplant, aber es ist jetzt dokumentierte Absicht. Das Dokument ist kohärenter als ich erwartet hatte.
- Der Tiervolk-Shader ist der einzige neue Abschnitt in v4, der wirklich von null gebaut werden muss. Der Rest ist Iteration auf Bestehendem. 3–4 Wochen Aufwand ist konservativ realistisch — vorausgesetzt, Vera liefert Referenzen rechtzeitig.

---

# Tag 4 Szene 4
**Typ**: PAUSE | **Uhrzeit**: 14:00 | **Teilnehmer**: Tobi, Leo (vor Ort), Vera (Slack)

## Notizen

- Vera meldet: Nano Banana Pro hat beim Tiervolk-Hero-Sheet selbstständig Detailinsets generiert (Auge, Nacken, Hand) — ohne Prompt-Vorgabe. Sie findet es gruselig.
- Ihre Analogie zu Houdini ist treffend. Habe mit der Erosions-Node-Anekdote geantwortet: unerwartete, trotzdem richtige Geometrie — die Lösung war im Parameterraum, ich hatte sie nur noch nicht gefunden.
- Leo eingebunden via Roguelike/Procgen-Frage: gleicher Effekt auf Spieler-Seite?

## Ergebnisse

- Kein technischer Output. Pausengespräch.

## Offene Fragen

- Gleiche wie nach Szene 2 (unverändert).

## Persönliches

- Vera hat heute schon einiges geliefert (Hero-Sheet mit Detailinsets). Das ist mehr als erwartet. Die KI macht ihr Arbeit leichter und gleichzeitig unheimlicher — das ist eine reale Spannung, keine Übertreibung.
- Leo ist ruhig, geerdet. Gut, sie in dieser Szene dabei zu haben.

---

# Tag 5 Szene 1
**Typ**: BRIEFING | **Uhrzeit**: 09:00 | **Teilnehmer**: alle 7

## Notizen

- **GDD 83 Seiten, Budget 60 — 23 Seiten kürzen.** WBB 41, im Budget. Letzter Tag, Content-Lock 15:00.
- Alle offenen Fragen geschlossen — keine neuen Inhalte, nur kürzen und Bilder einbauen.
- **Orden-Symbol = SIEGEL** (nicht mehr "Kreuz"). Prüfen ob "Kreuz" in meinen Asset-Namen oder Kommentaren vorkommt.
- Finn: Bilder in Dokumente einbauen, alle Kapitel kürzen.
- Darius: Kap 1–3, 5 kürzen. Vera: Pinnwand korrigieren, 18 neue Bilder, Bilder einbauen. Emre: WBB finalisieren. Nami: Kap 4 kürzen, WBB Kap 3.

## Ergebnisse

- Kürzungsplan für Kap 6 v5 identifiziert:
  - **6.7 Tiervolk-Symbiose-Shader**: von 8 Unterabschnitten auf ~3 eindampfen. Layer-Details, Blend-Maske-Hypothesen, Aufwandsschätzung → Pipeline-Bibel, nicht GDD.
  - **6.4.2–6.4.5 Schattenfieber-PP-Stufen**: Einzelne Shader-Parameter-Werte raus, Stufen-Logik bleibt.
  - **6.10.2 Pre-Alpha-Timeline**: Woche-für-Woche-Aufschlüsselung raus, nur Milestone-Tabelle bleibt.
  - Geschätztes Einsparpotenzial: 3–4 PDF-Seiten.

## Offene Fragen

- Orden-Symbol "Kreuz" → "Siegel" — Asset-Namen-Check in Kap 6 nötig (vermutlich betrifft es nur HTML-Kommentare, nicht Shader-Namen).

## Persönliches

- Letzter Tag. Klarer Auftrag: kürzen, nicht denken. Das ist nach vier Tagen Aufbau eine gute Disziplinübung.
- Finns 23-Seiten-Delta ist sportlich, aber jeder muss seinen Teil beitragen. Kap 6 hat das größte Einspar-Potenzial nach den narrativen Kapiteln.

---

# Tag 5 Szene 2
**Typ**: WORK | **Uhrzeit**: 10:00 | **Teilnehmer**: solo

## Notizen

- v5 ist die Kürzungsversion. Kein neuer Inhalt, nur Reduktion. Von 793 Zeilen Markdown auf 508 — Reduktion um 36%.
- **6.7 Tiervolk-Symbiose-Shader**: von 8 Unterabschnitten (6.7.1–6.7.8) auf 3 (Konzept+Abgrenzung, Dual-Layer-Architektur, Asset-Konvention). Alle Pipeline-Details (Layer-Einzelbeschreibungen mit SSS-Werten, Blend-Maske-Hypothesen-Tabelle, Masken-Pipeline-Workflow, Animations-Verknüpfung, Aufwandsschätzung) → Pipeline-Bibel.
- **6.4.2–6.4.5 Schattenfieber-PP-Stufen**: Alle konkreten Parameter-Werte (RGB-Multiplikatoren, px-Werte, Hz-Frequenzen, F-Stop-Werte) in HTML-Kommentare verschoben. Stufen-Logik und Konzeptbeschreibung bleiben sichtbar.
- **6.10.2 Pre-Alpha-Timeline**: Komplett entfernt. Woche-für-Woche-Aufschlüsselung ist Produktionsplanung, nicht GDD.
- **"Kreuz" → "Siegel"**: Einzige Fundstelle war in 6.12 (Offene-Fragen-Tabelle). Korrigiert zu "Orden-Siegel-Vektor".
- **Bilder eingebaut**: Schwellenanker-Drei-Zustände bei 6.6.1, Schwellenanker-Hero bei 6.6.2. Relative Pfade zu `../../pinwall/favorites/`.
- Redundante Inline-Erklärungen gestrafft: "Diese Entscheidung ist gesetzt und nicht diskussionswürdig" → gestrichen. Lumen-Tuning-Parameter (`r.Lumen.*`) → HTML-Kommentar. Emissive-Intensitäts-Werte (cd/m²) in Biolumineszenz-Tabelle belassen (die sind GDD-relevant).

## Ergebnisse

- GDD Kap 6 v5 erstellt: `simulation-2/gallery/gdd/06-technische-spezifikation-v5.md`
- Zeilenreduktion: 793 → 508 (−36%)
- Geschätzte PDF-Seitenreduktion: ~3–4 Seiten (abhängig von Bild-Einbettung)
- Inhaltlich nichts Neues hinzugefügt — reine Kürzung und Umstrukturierung
- Zwei Concept-Art-Bilder eingebettet (Schwellenanker drei Zustände + Hero-Shot)
- "Kreuz" → "Siegel" korrigiert

## Offene Fragen

- Keine neuen. Alle verbleibenden offenen Fragen aus 6.12 sind Status-quo (Houdini-Terrain-Constraints, Tiervolk-Referenzbilder, Fraktions-PP-Presets, Orden-Siegel-Vektor, Tiervolk-Tierformen-Bandbreite).

## Persönliches

- Das Kürzen ist befriedigend. Der Tiervolk-Abschnitt war in v4 für mich geschrieben — jetzt ist er für den Leser geschrieben. Die Pipeline-Bibel fängt die Details auf.
- Fünf Versionen in fünf Tagen. v1 war das Fundament, v2 der Rename, v3 das Interface, v4 der Tiervolk-Shader, v5 die Diät. Jede Version hatte einen klaren Grund.
