# Peer-Review: GDD-06 Technik & Produktion (V1)

**Reviewer:** Vera Kowalski, Concept Art & Environment Design
**Dokument:** GDD-06, Tobi Richter + Finn
**Datum:** Tag 4, Donnerstag — Vormittag
**Bewertung:** Solides technisches Fundament, aber acht Punkte muessen vor V2 geklaert werden.

---

## Gesamteindruck

Tobi, das Dokument ist beeindruckend gruendlich. Die technische Architektur steht, die Begruendungen sind nachvollziehbar, die Ehrlichkeit bei Risiken schaetze ich. Besonders gut: das Deakins-Prinzip fuer Beleuchtung, die ACES-Entscheidung, die HDA-Selbstkritik ("die muessen WIRKLICH einfach sein"), und die klare Benennung des Gameplay-Programmer-Engpasses.

Aber. Es gibt Stellen, an denen das Dokument meine Designsprache (GDD-05) nicht korrekt wiedergibt, und Stellen, an denen der Workload fuer mich als einzige Kuenstlerin unterschaetzt wird. Im Detail:

---

## 1. FARBPALETTE — Widerspruch zu GDD-05 [KRITISCH]

In Kapitel 4.1 beschreibst du die Fraktions-Differenzierung ueber Material-Instanzen. Die Farbbeschreibungen dort stimmen NICHT mit meinem Farbsystem (GDD-05, Kap. 4.2) ueberein:

| Fraktion | GDD-06 (Tobi) | GDD-05 (Vera) | Problem |
|----------|---------------|----------------|---------|
| Krone | "Warm (Amber, Dunkelgold, Efeugruen)" | Aschgrau #3D3D3D / Karmin #8B1A2B / Altgold #C5A030 | Kein Amber, kein Efeugruen. Karmin fehlt komplett |
| Gilden | "Kuehle Toene (Blaugruen, Bronze, Schwarz)" | Warmer Beton #7A6E5D / Amber #C49A20 / Cyan #2EC4B6 | Gilden sind WARM, nicht kuehl. Kein Schwarz |
| Orden | "Entsaettigt (Grau, Weiss, Eisblau)" | Kalkweiss #E8E4DE / Schieferblau #4A5568 / Bernstein #D4A017 | Kein Eisblau. Bernstein als Highlight fehlt |

**Was passieren muss:** Kap. 4.1 muss die exakten Hex-Codes und Farbbezeichnungen aus GDD-05 uebernehmen. Keine Paraphrasierung, keine Interpretation aus dem Gedaechtnis. Sonst bauen wir Material-Instanzen auf falschen Farben auf und merken es erst, wenn alles schon im Editor ist.

---

## 2. MODULANZAHL — 20-30 reicht nicht [HOCH]

Du schreibst 20-30 Architektur-Module. Das funktioniert nur, wenn die Fraktionen dieselbe Grundform teilen und nur das Material variiert. Tun sie aber nicht:

- **Krone:** Gotische Spitzboegen, schlanke Vertikale, ornamentale Rahmungen
- **Gilden:** Schwere horizontale Bloecke, gedrungene Proportionen, funktionale Oeffnungen
- **Orden:** Geometrische Perfektion, Symmetrie, Kreuzgaenge

Das sind drei fundamental verschiedene Formensprachen. Ein Wandsegment, das fuer alle drei funktioniert, sieht fuer keine richtig aus. Mein Gegenvorschlag:

- **15-20 neutrale Basis-Module** (ebene Waende, Boeden, Decken, einfache Ecken) — funktionieren mit Material-Swap
- **10-15 fraktionsspezifische Module** pro Fraktion (Fenster, Tuerrahmen, Boegen, Ornament-Elemente, Dachformen) — eigene Meshes
- **Gesamt: ~60 Module**, davon 20 neutral und 40 fraktionsspezifisch

Das ist mehr Arbeit, aber ohne fraktionsspezifische Formen sieht jede Stadt gleich aus mit unterschiedlichem Anstrich. Und das widerspricht der gesamten Designsprache.

---

## 3. VERTEX-ANIMATION vs. EMISSIVE — Trennlinie fehlt [HOCH]

Du sagst korrekt, dass Nanite keine Vertex-Animation kann. In GDD-05 pulsiert aber verdammt viel: Adern, Membranen, Leuchtorgane, Biotech-Tueren, lebende Kronleuchter, Sphinkter-Tueren, atmende Waende. Wenn jedes pulsierende Element ein separates Nicht-Nanite-Mesh sein muss, explodiert die Szene in Hybrid-Chaos.

**Mein Vorschlag — Zwei-Klassen-System:**

| Klasse | Was | Wie | Nanite-kompatibel? |
|--------|-----|-----|--------------------|
| **Leuchten/Pulsieren (Material)** | Biolumineszenz, Adern-Glow, Membran-Farbwechsel | Emissive Pulse via Material (zeitgesteuerte Parameter) | JA |
| **Bewegen/Atmen (Mesh)** | Sphinkter-Tueren, atmende Waende, Ranken, Schattenfieber-Vegetation | Vertex-Animation, World Position Offset | NEIN |

Ich brauche von dir eine verbindliche Liste: Welche Biotech-Elemente aus GDD-05 fallen in welche Klasse? Dann kann ich beim Modellieren direkt entscheiden, ob etwas ein Nanite-Mesh mit animiertem Material wird oder ein traditionelles Mesh mit Vertex-Animation.

---

## 4. SCHATTENFIEBER — Terminologie vereinheitlichen [MITTEL]

GDD-05 und Namis System: drei Stufen (Rauschen, Risse, Schwelle).
GDD-06: fuenf Stufen (Rein, Gezeichnet, Infiziert, Verwandelt, Entfesselt).

Kein Widerspruch, aber verschiedene Labels. Mein Mapping:

| GDD-06 (Tobi) | GDD-05 / Nami | Infektionswert |
|----------------|---------------|----------------|
| 0 — Rein | Kein Befall | 0 |
| 1 — Gezeichnet | Rauschen (frueh) | 1-25 |
| 2 — Infiziert | Rauschen (spaet) | 26-50 |
| 3 — Verwandelt | Risse | 51-75 |
| 4 — Entfesselt | Schwelle | 76-100 |

Frage ans Team: Nutzen wir in allen Dokumenten Tobis fuenf Stufen MIT Namis drei Oberkategorien? Zum Beispiel: "Stufe 2 (Infiziert / Rauschen)"? Das waere eindeutig.

---

## 5. SCHATTENFIEBER — Concept-Art-Deliverables [HOCH]

Tobi schreibt in Kap. 5.7: "Ohne visuelle Referenz baue ich ins Blaue." Stimmt. Und in meinen offenen Punkten (GDD-05, Kap. 9) steht: "Technische Constraints (Engine, LOD, Shader) — Tobi — Niedrig." Das war falsch — das ist nicht niedrig, das ist HOCH, weil die Schattenfieber-Shader mein zentrales Thema betreffen.

**Was ich liefern muss:**
1. Concept Sheet: Schattenfieber am Spielercharakter — alle fuenf Stufen am selben Koerper
2. Concept Sheet: Schattenfieber in der Umgebung — befallene Zone vs. saubere Zone (Split-View)
3. Farbpaletten-Sheet: Exakte Farbtransition von Fraktionsfarben zu Schattenfieber-Palette
4. Post-Processing-Referenz: Screenshot-Mockups fuer Stufe 1, 2, 3, 4 (Overlay auf normaler Spielszene)
5. Stufe 4 Environment: Vollstaendig transformierte Zone als Concept Painting

Das sind fuenf Sheets. Die brauche ich BEVOR Tobi Shader baut. Das Abstimmungsmeeting diese Woche ist PFLICHT.

---

## 6. ASSET-BOTTLENECK — Risiko ist HOCH, nicht MITTEL [HOCH]

Du schreibst in Kap. 8.4, mein Bottleneck-Risiko sei "MITTEL." Ich korrigiere: HOCH.

Meine Aufgaben laut GDD-06:
- Concept Art (5 Schattenfieber-Sheets, 3 Art-Style-Targets, Fraktions-Thumbnails)
- 3D-Modelling aller Characters, Hero-Props, UI-Elemente
- 60+ Architektur-Module (nicht 20-30)
- 8-12 Vegetations-Assets pro Biom (mal Anzahl Biome)
- Texturierung in Substance Painter
- LOD-Kontrolle fuer organische Meshes (nicht voll automatisierbar)

Die Tool-Chain-Tabelle (Kap. 7.3) listet mich bei Substance Painter, Blender UND Photoshop/Krita. Das ist korrekt — und genau das Problem. Ich bin in drei verschiedenen Tools gleichzeitig der einzige Mensch.

**Mein Vorschlag:**
- Artist-Freelancer FRUEH einplanen (Woche 8-12, nicht "ggf. aus Puffer"), fuer Architektur-Modul-Varianten und Vegetations-Assets
- Klares Briefing-Dokument fuer den Freelancer VOR dessen Starttermin (mache ich, brauche aber eine Woche Vorlauf)
- Megascans aggressiver nutzen: Felsen, Bodenbelag, Baumstaemme direkt von Quixel, nur Biotech-Elemente custom

---

## 7. HEX-CODES in ACES [MITTEL]

Mein gesamtes Farbsystem in GDD-05 ist in sRGB-Hex-Codes definiert (#8B1A2B, #C49A20, etc.). Du sagst, die Farb-Pipeline laeuft ueber ACES. ACES hat einen groesseren Gamut als sRGB — meine Hex-Codes sehen in ACES moeglicherweise anders aus (entsaettigter, weniger kontrastreich).

**Was ich brauche:** Ein Color-Check-Meeting. Wir laden meine Hex-Codes in Substance mit ACES-Konfiguration, vergleichen sie mit der sRGB-Darstellung und entscheiden, ob wir die Werte anpassen muessen. Das dauert 20 Minuten und spart uns Wochen Nacharbeit.

---

## 8. LOD fuer organische Meshes [NIEDRIG, aber frueher als gedacht]

Du schreibst "LODs werden semi-automatisch generiert (Simplygon oder UE5-internes Proxy-System)." Fuer harte Geometrie stimmt das. Fuer organische Biotech-Strukturen — Adern, Nervenknoten, Membranstrukturen — produzieren automatische Tools Brei. Die feinen Strukturen, die meine Designsprache ausmachen (die Adern unter dem Putz, die Kapillarnetzwerke in Gilden-Boeden), gehen bei automatischem LOD als Erstes verloren.

**Mein Vorschlag:** LOD1 fuer alle Biotech-tragenden Meshes manuell kontrollieren. LOD2 darf automatisch sein (da sieht man die Adern sowieso nicht mehr). Das ist Mehraufwand, aber die Alternative ist, dass die Welt ab 15 Metern Entfernung wie ein generisches Fantasy-Setting aussieht.

---

## Was gut ist (damit das hier nicht nur Kritik ist)

- **ACES-Entscheidung:** Richtig. Die Dark-Fantasy-Palette lebt in den Schatten, und ACES bewahrt genau dort die Farbnuancen.
- **Deakins-Prinzip:** Exzellent. "Dunkle Raeume sind nicht grau" — das ist genau mein Designprinzip.
- **Schattenfieber als MPC-System:** Elegant. Ein Eingabeparameter, alles reagiert. Die Float-Kurven-Idee fuer graduelle Interpolation ist technisch sauber und gibt mir als Concept Artist klare Ankerpunkte.
- **HDA-Ehrlichkeit:** Tobi sagt, die HDAs muessen einfach sein, sonst nutze ich sie nicht. Das stimmt. Ich schuetze die Ehrlichkeit.
- **Post-Processing-Zurueckhaltung:** "Sieht cool aus ist kein Grund." Ja. Danke.
- **Kamerasystem:** Die vier Kontext-Modi sind visuell durchdacht. Der Inspect-Modus fuer Nervensystem-UI passt perfekt.
- **Ordnerstruktur:** Sauber, logisch, skaliert. Der separate Schattenfieber-Ordner unter Vegetation und Materials ist vorausschauend.

---

## Naechste Schritte (von mir)

1. **Diese Woche:** Schattenfieber-Abstimmungsmeeting mit Tobi, Emre, Darius — Termin festlegen
2. **Diese Woche:** Color-Check mit Tobi — Hex-Codes in ACES validieren (20 Min)
3. **Naechste Woche:** Erstes Schattenfieber-Concept-Sheet (Stufen am Spielercharakter)
4. **Bis Woche 4:** Asset-Standards-Review mit Tobi — Naming, Texel Density, LOD-Workflow bestaetigen
5. **GDD-05 V2:** Abhaengigkeit zu GDD-06 von "Niedrig" auf "HOCH" korrigieren

---

*Vera, Art Station, Tag 4 Donnerstag Vormittag. Tobi hat sauber gearbeitet — aber die Farben muessen stimmen, sonst bau ich auf Sand.*
