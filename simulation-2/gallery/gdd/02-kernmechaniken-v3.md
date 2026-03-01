# GDD Kapitel 02 — Kernmechaniken

<!-- Darius: v3 — Massive Kürzung für Seitenbudget (83→60 PDF-Seiten). Tiervolk-Abschnitt 2.6 auf Tabelle komprimiert. Systeminteraktionen 2.7 von 7 auf 4 Kerninteraktionen gekürzt. Balancing-Detailwerte in HTML-Kommentare. Bilder von Pinnwand eingebaut. Keine neuen Inhalte. Orden-Symbol = SIEGEL (kein Kreuz). -->

---

## Überblick

Sechs Kernsysteme, jedes direkt aus den Design-Säulen abgeleitet:

1. **Kampfsystem** — Säule I + III
2. **Nervensystem-Leveling** — Säule III + I
3. **Crafting & Materialsystem** — Säule II + IV
4. **Fraktionsruf-System** — Säule II + I
5. **Schattenfieber-Progression** — Säule III + II
6. **Händlernetz & Tiervolk** — Säule II + IV

---

## 2.1 Kampfsystem

### Spieler-Fantasie

*"Jeder Kampf kostet mich etwas. Wenn ich gewinne, habe ich es mir verdient."*

### Designprinzipien

Kämpfe sollen sich anstrengend anfühlen, nicht befriedigend-flüssig. Das Kampfsystem ist eine mechanische Umsetzung von Schwere und Konsequenz.

**Referenz:** Gothic 2 (Kampf als Risiko), Dark Souls (Positionierung, Gewicht, Kosten).

### Kernmechaniken

**Ausdauersystem (Stamina):** Zentrale Kampfressource. Jede Aktion kostet Ausdauer — leichte Angriffe wenig, schwere viel, Parade moderat. Erschöpfung macht anfällig. Kapazität und Regeneration sind mit dem Cardio-Subsystem verknüpft (→ 2.2).

**Positionierung:** Angriffe von hinten ignorieren Vorderrüstung, Seitenangriffe umgehen Paraden. Engpässe sind überlebensnotwendig gegen Gruppen.

**Waffenklassen:**

| Klasse | Stärke | Besonderheit |
|---|---|---|
| Einhandschwert | Ausgewogen, schnell | Schildkombination |
| Zweihandschwert | Hoher Schaden, Reichweite | Rüstungsdurchdringung |
| Dolch | Sehr schnell, niedrige Kosten | Schleich-Finisher |
| Axt | Stark gegen Rüstung | Ignoriert anteilig Rüstungsschutz |
| Streitkolben | Effektiv gegen Platte | Betäubungseffekt |
| Bogen | Distanz, leise | Schwachstellen-Targeting |
| Armbrust | Höchste Durchschlagskraft | Durchdringt schwere Rüstung |

Keine Waffe ist "die beste" — Auswahl hängt von Gegner, Umgebung und Muskel-Stand ab.

**Alchemie im Kampf:** Stärkungstränke mit Nachkater, langsame Heilmittel, Schwellensubstrat-Extrakte mit Lymph-Kosten.

**Kampf vs. Ausweichen:** Das System belohnt nicht maximale Kämpfe. Soziale Lösungen, Stealth, alternative Routen existieren als gleichwertige Optionen.

---

## 2.2 Nervensystem-Leveling

### Spieler-Fantasie

*"Ich sehe meinen Fortschritt. Ich sehe, was er mich gekostet hat."*

### Das System

Drei Subsysteme ersetzen klassische Erfahrungspunkte vollständig. Skill-by-Use, vier Qualitätsstufen (Untrained / Geübt / Fortgeschritten / Meister). Visualisierung: halbtransparente Körperansicht mit leuchtenden Nervenbahnen.

![Schwellenanker: Relikt-Zustände](../../pinwall/favorites/relikt-drei-zustaende-v2_nano-banana-pro.png)

*Konzeptbild: Die drei Relikt-Zustände — ruhend, aktiviert, aufgelöst. Die biolumineszente Gefäßsprache gilt auch für das Nervensystem-Leveling-Interface.*

### Die drei Subsysteme

| Subsystem | Trainiert durch | Mechanische Auswirkung | Stufe IV (Meister) |
|---|---|---|---|
| **Cardio** | Sprinten, Ausdauerkämpfe, Klettern, Flucht | Ausdauer, Bewegungsgeschwindigkeit, Regeneration | Ausdauer kein limitierender Faktor |
| **Muskel** | Nahkampf, Tragen, physische Arbeit | Schadenswerte, Tragegewicht, Rüstungseffizienz | Schwere Zweihandwaffen bevorzugt |
| **Lymph** | Alchemika, Schwellensubstrat-Exposition, Heilrituale | Fieber-Widerstand, Transformationen, Risiko | Irreversibel, massiver Power-Spike + Kontrollverlust |

<!-- Darius: Balancing-Detailwerte pro Stufe: Cardio I→IV Ausdauerkapazität 100/150/220/300, Regeneration 5/8/14/22 pro Sek. Muskel I→IV Schadensmodifikator ×1.0/×1.3/×1.7/×2.2, Tragegewicht 30/50/75/110. Lymph-Akkumulation: Schwellensubstrat-Extrakt +8 Lymph, Dünnstellen-Aufenthalt +2/min, Ordensritual +4 (kontrolliert). Stufenschwellen: I→II bei 100 Nutzungspunkten, II→III bei 350, III→IV bei 800. -->

**Qualitätsstufen-Übergänge:** Kein Fanfare, keine Leveling-Bildschirme. Die Nervensystem-Ansicht leuchtet kurz auf. Der Spieler merkt es an der Performance.

**Muskel III+ ist Voraussetzung** für sinnvolle Nutzung von Materialklasse IV — die besten Materialien kaufen reicht nicht, der Körper muss folgen.

**Körperreaktion als Variable (Lymph):** Stufe II und III verlaufen nicht identisch. Die Transformation hängt von Expositionsquelle, Fraktionspfad und körperlicher Baseline ab. *"Das Fieber macht etwas aus mir — etwas, das kein anderer Spieler sieht."*

---

## 2.3 Crafting & Materialsystem

### Spieler-Fantasie

*"Ein Stück Damaszener-Stahl ist ein Ereignis."*

### Materialklassen

| Klasse | Beispiele | Zugang | Status |
|---|---|---|---|
| **I** | Eisen, Zinn, Knochen | Frei verfügbar | Gesetzlos |
| **II** | Tiegelstahl, Silber, Malachit | Gilden-Markt | Handwerker |
| **III** | Damaszener-Stahl, Bergkristall | Gilden-Ruf: Anerkannt | Gilden-Mitglied |
| **IV** | Titan-Legierungen, Roségold | Gilden-Ruf: Vertraut + Krone-Pass | Oberschicht |
| **V** | Schwellenlegierungen, -fäden, -linsen | Gilden: Meister ODER Schlund-Schwarzmarkt | Verboten |

Keine Loot-Inflation. Ein Klasse-III-Schwert mit Muskel III übertrifft ein Klasse-IV-Schwert mit Muskel I.

### Handwerk-Mechanik

- **Aktives Crafting:** Werkbank, vereinfachte Handwerks-Sequenz
- **Werkzeug-Erfordernisse:** Meister-Schmieden sind Gilden-Territorium
- **Rezepturen:** Wissensgegenstände, nicht automatische Freischaltungen. Klasse I–II frei, III–IV erfordern Gilden-Zugang, V liegt in Gilden/Orden-Archiven.
- **Qualitätsvarianten:** Grundlegend / Ordentlich / Meisterwerk — abhängig von Material, Werkzeug und Erfahrung

### Rüstung als sozialer Ausdruck

Rüstungsklasse beeinflusst Ausdauerkosten, Material definiert Schutzwerte und NPC-Reaktionen. Jedes Körperteil unabhängig ausrüstbar. Verfall und Reparatur als Alltagshandlung.

---

## 2.4 Fraktionsruf-System

### Spieler-Fantasie

*"Ich habe mir diese Tür verdient. Oder ich habe sie mir verbaut."*

### Ruf-Stufen

| Stufe | Bezeichnung | Zugang |
|---|---|---|
| 0 | **Feindselig** | Tore geschlossen, NPCs greifen an |
| I | **Unbekannt** | Öffentliche Bereiche |
| II | **Bekannt** | Basisaufgaben, erste innere Tore |
| III | **Anerkannt** | Mittlere Materialien, Fraktions-Infrastruktur |
| IV | **Vertraut** | Elite-Materialien, Insider-Informationen |
| V | **Meister** | Vollzugang (Schwellen-Materialien / Kronpassagen / Orden-Archive) |

**Kommunizierende Röhren:** Was bei der Krone gewinnt, verliert bei Gilden oder Orden. Maximierung bei allen drei gleichzeitig ist nicht möglich.

**Ruf-Quellen:** Fraktionsquests (Hauptquelle), Welthandlungen (stiller Buchhalter), Dialoge, Handels-Reputation.

**Point of No Return:** Jede Fraktion hat einen quest-spezifischen Punkt, der sich erst rückwirkend als solcher zeigt.

<!-- Darius: Ruf-Schwellenwerte (Balancing): Unbekannt→Bekannt bei 50 RP, Bekannt→Anerkannt bei 200, Anerkannt→Vertraut bei 500, Vertraut→Meister bei 1000. Feindselig-Schwelle bei -100. Cross-Faction-Verlust: +10 Krone = -3 Gilden, -5 Orden (asymmetrisch je nach Quest). -->

### Gilden-Mikropolitik

Neben dem Gesamt-Gildenruf gibt es Einzel-Ruf bei spezifischen Gilden (Schmiede, Glasmacher, Gerber, Weber). Wer gezielt eine Gilde hofiert, bekommt spezifische Tiefe statt generischen Zugang.

---

## 2.5 Schattenfieber-Progression

### Spieler-Fantasie

*"Ich sehe, was das Fieber aus mir macht. Es macht etwas anderes als aus anderen."*

Das Schattenfieber ist keine Krankheit, die man heilt — es ist ein biologischer Zustand, den man navigiert. Direkt an das Lymph-Subsystem gekoppelt (→ 2.2).

![Schwellenanker: Hero Shot — aktiviert](../../pinwall/favorites/relikt-hero-shot-aktiviert_gpt-image-1-5.png)

*Konzeptbild: Schwellenanker in aktiviertem Zustand — biolumineszente Gefäßlinien, die visuelle Sprache der Schattenfieber-Transformation.*

### Die drei Fieber-Stadien

| Stadium | Lymph-Stufe | Vorteile | Kosten | Reversibilität |
|---|---|---|---|---|
| **Flüstern** | II | Erweiterte Sinne, Schwellen-Objekte sichtbar | Wahrnehmungsstörungen, leichte Veränderungen | Vollständig reversibel |
| **Wandlung** | III | Physische Buffs, Immunität gegen leichte Exposition | Erinnerungsfragmentierung, sichtbare Veränderungen, Krone-Ruf sinkt | Nicht heilbar, managebar |
| **Entgrenzung** | IV | Extremer Power-Spike, direkte Schwellen-Interaktion | Kontrollverlust, narrative Einengung | Irreversibel ohne Schwellenanker |

**Körperreaktions-Varianz:** Dasselbe Stadium sieht bei drei Spielern verschieden aus. Transformation hängt ab von: Expositionsquelle, Fraktionspfad, körperlicher Baseline.

### Drei Fraktions-Antworten

| Fraktion | Strategie | Gameplay |
|---|---|---|
| **Krone** | Unterdrückung — Lymph-Wert aktiv senken | Kein Fieber-Vorteil/Kosten, kompensiert durch Ausrüstung |
| **Gilden** | Verwertung — Plateau bei Stadium I, kurzzeitig Stadium II | Ressourcenintensiv, bindet an Wirtschaftsmechanik |
| **Orden** | Destillation — kontrollierter Aufstieg mit Stabilisierung | Kostenlos (Preis: Zeit, Verpflichtung, Schuld) |

**Der Schwellenanker als Stabilisator:** Ein Spieler mit Fragment kann Stadium III partiell stabilisieren — keine Heilung, aber Schutz vor Identitätsverlust. Das ist der mechanische Kern des Hauptquests.

---

## 2.6 Händlernetz & Tiervolk

### Spieler-Fantasie

*"Es gibt Händler, die andere nicht kennen — und Waren, die nur sie führen."*

![Tiervolk: Händler-Fuchs](../../pinwall/favorites/tiervolk-haendler-fuchs-exploration_seedream-4-5.png)

*Konzeptbild: Tiervolk-Händler — kosmologisch-fremde Wesen in dauerhafter Symbiose mit Tieren. Leicht alien, nicht tribal.*

Das Tiervolk sind kosmologisch-fremde Wesen in dauerhafter, irreversibler Symbiose mit Tieren. Ihre Handelsmotivation: Sie brauchen Materialien zur Stabilisierung der Symbiose.

| Eigenschaft | Fraktionshändler | Tiervolk |
|---|---|---|
| Standorte | Fest, territorial | Fluktuierend, schwellennah |
| Ruf-System | 5 Stufen, skalierbar | Binäres Vertrauen (fair/unfair) |
| Fraktionsbindung | An eine Fraktion gebunden | Unabhängig — versorgt auch verbrannte Spielfiguren |
| Spezialwaren | Materialklasse I–V via Ruf | Symbiose-Materialien, Navigations-Wissen, Körperreaktions-Alchemika |

**Salva** (→ Kap. 4) ist der Haupt-Kontakt: Informationsbroker, Kontext-Lieferant, Einführung ins Tiervolk-System. Er erscheint nicht immer — sein Bewegungsmuster ist erlernbar.

![Tiervolk: Marktszene](../../pinwall/favorites/tiervolk-marktszene-exploration_seedream-4-5.png)

*Konzeptbild: Tiervolk-Marktszene — fluktuierende Handelspositionen an Übergangszone Gürtel/Schlund.*

<!-- Darius: Tiervolk-Warenkategorien (Detail): A = Symbiose-Materialien (Import — Tiervolk kauft vom Spieler: Schwellensubstrat-Konzentrationen, Schwellenpilz-Derivate, biologische Proben). B = Exklusive Waren (Export — organische Materialien, Dünnstellen-Navigationswissen, Alchemika die Körperreaktion modifizieren). C = Informationen (Dünnstellen-Verbindungen, Schwellen-Fauna, Gerüchte jenseits Schwarzrand). Symbiose-Stabilisierungs-Quests: Beschaffung, Erkundung, seltene Schutzaufträge. -->

---

## 2.7 Systeminteraktionen

Die sechs Kernsysteme wirken zusammen. Vier Kerninteraktionen:

**Kampf × Nervensystem × Schattenfieber:** Jeder Kampf trainiert Cardio und Muskel. Wer mit Schwellensubstrat-Extrakten kämpft, gewinnt Macht und trainiert ungewollt das Lymph-System. Die ultimative Abwägung: kurzfristige Kampfkraft gegen langfristige Transformation.

**Crafting × Fraktionsruf:** Bessere Materialien erfordern höheren Fraktionsruf. Das bindet Crafting an Fraktionsentscheidungen. Muskel III+ ist Voraussetzung für Klasse-IV-Ausrüstung — "Day-One-Endgame-Gear" ist ausgeschlossen.

**Schattenfieber × Fraktionsruf:** Fieber-Status verändert Fraktions-Reaktionen. Stadium II schließt Krone-Zugänge. Die Gilden sind die einzige Fraktion, die Fieber-Träger ohne Stigma bedient.

**Tiervolk × Alle Systeme:** Das Tiervolk ist das systemische Sicherheitsnetz: unabhängig von Fraktionsruf, liefert Klasse-V-Materialien (Sonderweg), kauft Schattenfieber-Produkte, bietet Körperreaktions-Alchemika. Für verbrannte Spielfiguren der einzige verbleibende Zugang.

<!-- Darius: v3 vollständig. Gekürzt von ca. 14 auf ca. 8 Seiten. Tiervolk-Abschnitt 2.6 von Fließtext auf Tabelle + Kernaussagen. Systeminteraktionen 2.7 von 7 auf 4 konsolidiert. Balancing-Werte in Kommentare verschoben. Bilder von Pinnwand eingebaut. -->
