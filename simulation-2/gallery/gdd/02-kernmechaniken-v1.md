# GDD Kapitel 02 — Kernmechaniken

<!-- Status: v1 | Tag 3, Mittwoch | Autor: Darius Engel -->
<!-- Darius: Dieses Kapitel definiert alle Kernsysteme von RELICS: Der Schwellenanker. Jedes System ist aus den vier Design-Säulen abgeleitet. Spieler-Fantasie-Statement steht über jeder Mechanik-Beschreibung — ist das nicht da, ist das Feature raus. -->

---

## Überblick

Dieses Kapitel beschreibt die fünf Kernsysteme von RELICS: Der Schwellenanker. Jedes System ist direkt aus den Design-Säulen von Kapitel 1 abgeleitet und muss gegen mindestens zwei Säulen bestehen:

1. **Kampfsystem** — Säule I (Immersive Sim) + Säule III (Körperlicher Fortschritt)
2. **Nervensystem-Leveling** — Säule III (Körperlicher Fortschritt) + Säule I (Immersive Sim)
3. **Crafting & Materialsystem** — Säule II (Fraktionspolitik) + Säule IV (Dichte vor Breite)
4. **Fraktionsruf-System** — Säule II (Fraktionspolitik) + Säule I (Immersive Sim)
5. **Schattenfieber-Progression** — Säule III (Körperlicher Fortschritt) + Säule II (Fraktionspolitik)

---

## 2.1 Kampfsystem

### Spieler-Fantasie

*"Jeder Kampf kostet mich etwas. Wenn ich gewinne, habe ich es mir verdient."*

### Designprinzipien

Das Kampfsystem von RELICS ist kein Showroom für Combo-Systeme. Es ist eine mechanische Umsetzung von Schwere und Konsequenz — den zwei Kerneigenschaften des Game-Feel-Statements aus Kapitel 1. Kämpfe sollen sich anstrengend anfühlen, nicht befriedigend-flüssig. Der Spieler soll nach einem schweren Kampf *erschöpft* sein, nicht triumphierend-leicht.

**Referenz:** Gothic 2 (Piranha Bytes, 2002) — Kampf als Risiko, nicht als Komfort. Dark Souls (FromSoftware, 2011) — Positionierung, Gewicht, Kosten.

### Kernmechaniken des Kampfes

**Ausdauersystem (Stamina)**

Die zentrale Ressource im Kampf ist nicht Gesundheit, sondern Ausdauer. Jede Aktion kostet Ausdauer:
- Leichter Angriff: geringe Kosten
- Schwerer Angriff: hohe Kosten
- Parade / aktive Abwehr: moderate Kosten
- Ausweichen / Rollen: moderate Kosten
- Sprinten, Springen: kontinuierliche Kosten

Ist die Ausdauer erschöpft, wird der Spieler anfällig: Angriffe treffen schwerer, Paraden schlagen durch, der Spieler kann sich nicht mehr aktiv bewegen. Ausdauer regeneriert mit kurzer Verzögerung nach der letzten Aktion — ein aktiver Kampf ohne Pausen lässt den Spieler langsam zusammenbrechen.

Ausdauerkapazität und Regenerationsrate sind direkt mit dem Cardio-Subsystem des Nervensystem-Levelings verknüpft (→ Abschnitt 2.2).

**Trefferzonen & Positionierung**

RELICS kennt keine abstrakten Trefferwahrscheinlichkeiten. Positionierung ist eine direkte taktische Variable:
- Angriffe von hinten ignorieren Rüstungsschutz der Vorderseite
- Angriffe von der Seite umgehen aktive Paraden
- Flankieren ist das stärkste taktische Mittel — und das, was Gegner aktiv versuchen

Der Spieler kämpft in der Regel alleine gegen Gruppen. Positionierung an Engpässen (Türrahmen, Treppenstufen, enge Gassen) ist keine Spielhilfe, sondern überlebensnotwendig.

**Waffenklassen und ihre Eigenlogik**

| Waffenklasse | Stärke | Schwäche | Besondere Eigenschaft |
|---|---|---|---|
| **Einhandschwert** | Ausgewogen, schnell | Mittlere Reichweite, mittlerer Schaden | Kann mit Schild kombiniert werden |
| **Zweihandschwert** | Hoher Schaden, gute Reichweite | Hohe Ausdauerkosten, langsamer | Kann Schilde durchschlagen (Rüstungsdurchdringung) |
| **Dolch** | Sehr schnell, niedrige Ausdauerkosten | Geringer Schaden, kurze Reichweite | Finisher-Angriffe möglich (Schleich-Umgebung) |
| **Axt** | Hoher Schaden gegen Rüstung | Langsam, keine Parade-Option | Ignoriert anteilig Rüstungsschutz |
| **Streitkolben** | Effektiv gegen Plattenrüstung | Langsam, hohe Ausdauerkosten | Betäubungseffekt bei vollem Treffer |
| **Bogen** | Distanzangriff, leise | Nachladezeit, unbrauchbar in Nahkampf | Schwachstellen-Targeting möglich |
| **Armbrust** | Hohe Durchschlagskraft | Sehr lange Nachladezeit | Kann schwere Rüstung durchdringen |

Keine Waffe ist "die beste". Die Auswahl ist eine taktische Entscheidung, die vom Gegnertyp, der Umgebung und dem eigenen Muskel-Subsystem-Stand abhängt.

**Alchemie im Kampf**

Alchemika sind keine Magie-Substitute. Sie sind Hilfsmittel mit Nebenwirkungen:
- **Stärkungstränke:** Temporäre Ausdauer-Regeneration, Schadensbonus — mit Nachkater (reduzierte Werte nach Wirkende)
- **Heilmittel:** Langsame, anhaltende Heilung — nicht sofort. In einem aktiven Kampf nutzen sie wenig, danach sehr viel.
- **Schwellensubstrat-Extrakte:** Hochriskante Kampfmittel, die temporäre Stärke durch Schattenfieber-Exposition erzeugen. Jede Einnahme erhöht den Fieber-Wert im Lymph-Subsystem.
- **Rauch- und Blendmittel:** Taktische Werkzeuge für Rückzug und Neupositionierung

Alchemika werden im Crafting-System hergestellt oder über Gilden und Händler erworben (→ Abschnitt 2.3).

**Kampf vs. Ausweichen**

Das System belohnt den Spieler nicht dafür, möglichst viele Kämpfe zu gewinnen. Es belohnt ihn dafür, dass er in der Welt navigiert. Viele Begegnungen haben Umgehungswege: Soziale Lösungen (Fraktionsruf-basiert), Stealth-Wege, alternative Routen. Das Kampfsystem ist für die Fälle, in denen das nicht klappt — oder für die Spieler, die es genau so wollen.

---

## 2.2 Nervensystem-Leveling

### Spieler-Fantasie

*"Ich sehe meinen Fortschritt. Ich sehe, was er mich gekostet hat."*

### Das System im Überblick

Das Nervensystem-Leveling ist das Herz von RELICS' Progressionsdesign. Es ersetzt klassische Erfahrungspunkte-Balken und Attribut-Grids vollständig. Der Spieler hat keinen "Level". Er hat drei Subsysteme, die sich durch tatsächliches Tun entwickeln.

**Philosophie:** Ein Schwertkämpfer wird zum Schwertkämpfer, indem er kämpft. Nicht indem er Erfahrungspunkte sammelt und Punkte verteilt. Diese "Skill-by-Use"-Logik stammt direkt aus Gothic 2 — aber RELICS verfeinert sie durch das Deus-Ex-Modell der Qualitätsstufen statt graduellem Zahlenfortschritt.

Das Nervensystem visualisiert sich durch eine halbtransparente Körperansicht, die während des Levelings eingeblendet werden kann: leuchtende Nervenbahnen zeigen aktive Subsysteme, trübe zeigen inaktive, und die Fieber-Infiltration des Lymphsystems ist in Echtzeit sichtbar.

![Nervensystem-Konzept: Schwellenanker-Relikt in Zustand Eins](../concepts/day02-vera/relics/relikt-zustand-eins-aktiviert_seedream-4-5.png)

*Konzeptbild: Biolumineszente Gefäßlinien — dieselbe visuelle Sprache gilt für das Nervensystem-Leveling-Interface. Lymph-Kontamination folgt vergleichbaren Mustern.*

### Die drei Subsysteme

**Cardio — Das Ausdauersystem**

Das Cardio-Subsystem bestimmt alle Ausdauer-bezogenen Parameter: wie lange der Spieler laufen kann, wie schnell er sich erholt, wie viele Kampfaktionen er in Serie ausführen kann, bevor er pausieren muss.

*Trainiert durch:* Ausdauerkämpfe (Kämpfe, die lange dauern), Sprinten, Klettern, Flucht-Sequenzen, Erkundung größerer Strecken ohne Rast.

*Vier Qualitätsstufen:*

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Untrainiert | Erschöpft schnell, langsame Regeneration, eingeschränkte Kampfdauer |
| II | Geübt | Moderate Ausdauer, schnellere Regeneration, kann kurze Sprintphasen nutzen |
| III | Fortgeschritten | Hohe Ausdauer, rapide Regeneration, Ausdauer ist selten ein Engpass |
| IV | Meister | Ausdauer ist kein limitierender Faktor. Kampf-Pausen werden taktisch, nicht notwendig |

*Progression:* Jede Qualitätsstufe erfordert eine bestimmte Anzahl an "Ausdauer-Ereignissen" — Kampfrunden, Sprintmeter, Kletterakte. Das Spiel trackt diese unsichtbar und zeigt nur die aktuelle Qualitätsstufe an. Der Übergang ist spürbar, nicht abrupt: Der Spieler merkt, dass er weiter laufen kann, bevor die Stufe visuell bestätigt wird.

**Muskel — Das Kraftsystem**

Das Muskel-Subsystem bestimmt alle physischen Stärkeparameter: Schadensausgabe im Nahkampf, maximales Tragegewicht, Effizienz schwerer Rüstungen.

*Trainiert durch:* Nahkampfangriffe (jeder Treffer zählt, auch verpasste), schwere Gegenstände tragen und transportieren, physische Arbeit (optionale Tätigkeiten in der Welt: Schmieden helfen, Ladungen schleppen — auch das trainiert).

*Vier Qualitätsstufen:*

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Untrainiert | Minimaler Nahkampfschaden, niedriges Tragegewicht, mittelschwere Rüstungen beschränken Mobilität |
| II | Geübt | Ordentlicher Nahkampfschaden, Rüstung schränkt weniger ein, kann kompetent kämpfen |
| III | Fortgeschritten | Deutlicher Schadensbonus, schwere Rüstungen voll nutzbar, Tragegewicht kein Problem |
| IV | Meister | Spitzenwerte. Schwere Zweihandwaffen werden zu bevorzugten Werkzeugen, maximale Rüstungseffizienz |

*Besonderheit:* Das Muskel-Subsystem interagiert mit dem Crafting-System. Wer auf Stufe III oder IV ist, kann schwere Waffen und Rüstungen überhaupt erst sinnvoll nutzen. Damaszener-Stahl-Ausrüstung auf einem Stufe-I-Spieler ist Verschwendung.

**Lymph — Das Fieber-System**

Das Lymph-Subsystem ist das komplexeste und gefährlichste der drei. Es bildet die biologische Schnittstelle zwischen dem Spielercharakter und der Schwellenrealität.

*Trainiert durch:* Einnahme von Alchemika und Schwellensubstrat-Extrakten, Exposition in Dünnstellen (die tiefen Bereiche von Schwarzrand), Heilrituale des Ordens (die ebenfalls das Lymphsystem verändern, aber auf kontrollierte Weise), Kontakt mit dem Schwellenanker.

*Vier Qualitätsstufen:*

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Unangetastet | Baseline. Keine Schattenfieber-Symptome, keine Mutation, aber auch keine Vorteile durch das Lymphsystem |
| II | Exponiert (Flüstern) | Erste Schattenfieber-Symptome. Sensorische Erweiterungen: Farben intensiver, Geräusche mit Nachklang. Gameplay-Vorteil: Wahrnehmen versteckter Schwellen-Objekte. |
| III | Kontaminiert (Wandlung) | Sichtbare physische Veränderungen. Physische Buffs (Stärke, Ausdauer durch Fieber). Kognitive Kosten: Erinnerungen unzuverlässig, gelegentliche Wahrnehmungsstörungen im Gameplay |
| IV | Durchdrungen (Entgrenzung) | Irreversibel. Massiver Power-Spike, aber der Spieler verliert zunehmend die Kontrolle. Nur über bestimmte Orden-Rituale oder Schwellenanker-Interaktion partiell stabilisierbar |

*Kritische Eigenschaft:* Das Lymph-Subsystem kennt keine einfache Progression von I nach IV. Es gibt Kontaminations-Akkumulation, die sich durch Fieberquellen aufbaut, und Reduktions-Mechanismen:
- Krone-Weg: Medizinische Unterdrückung — Lymph-Wert senken, aber kein Aufstieg in Stufe II–IV möglich
- Gilden-Weg: Kontrollierte Nutzung — Lymph-Wert auf einem Plateau halten, Vorteile von Stufe II extrahieren
- Orden-Weg: Destillation und Verstehen — langsamer Aufstieg mit Stabilisierung, tiefer Lore-Zugang, aber der Orden hat Forderungen

*Das Schattenfieber-Risiko:* Wer unkontrolliert in Dünnstellen operiert oder zu viele Extrakte nimmt, riskiert einen unkontrollierten Sprung von Stufe II zu Stufe III oder von III zu IV. Stufe IV ohne stabilisierende Intervention ist faktisch ein langsamer Game-Over-Zustand — der Spieler wird immer schwerer kontrollierbar, bis er die Handlungsfähigkeit verliert.

### Qualitätsstufen-Übergänge

Ein Qualitätsstufenwechsel ist ein Moment im Spiel. Keine Fanfare, keine Leveling-Bildschirme. Die Nervensystem-Ansicht zeigt kurz das aktive Subsystem aufleuchten — eine visuelle Bestätigung, keine Unterbrechung. Der Spieler merkt es an der veränderten Spielperformance, nicht durch eine UI-Meldung.

Der Spieler kann aktiv "investieren": Wer weiß, dass ein schwerer Kampf bevorsteht, kann vorab gezielt das Muskel-Subsystem stimulieren (Kampfübungen mit einem Trainer, Schmiedearbeit). Das ist die optionale Vorbereitung — keine Pflicht, aber ein strategischer Hebel.

---

## 2.3 Crafting & Materialsystem

### Spieler-Fantasie

*"Ein Stück Damaszener-Stahl ist ein Ereignis. Ich weiß, was ich tue, wenn ich es verarbeite."*

### Designprinzipien

Das Crafting-System von RELICS ist keine Item-Fabrik. Es ist ein Ausdruck der Fraktionspolitik und der Materialsprache der Welt. Materialien sind keine Zahlen — sie sind Hierarchien. Wer welches Material verarbeitet, definiert, wo er in der sozialen Ordnung steht.

**Keine Loot-Inflation.** Ein Stück Tiegelstahl ist selten. Damaszener-Stahl ist eine Rarität. Schwellenlegierungen sind die gefährlichste und mächtigste Materialklasse, mit einem echten Preis.

### Materialklassen

RELICS hat fünf Materialklassen. Jede ist mit einer Fraktionszugehörigkeit und einem sozialen Status verknüpft:

| Klasse | Material-Beispiele | Zugang | Sozialer Status |
|---|---|---|---|
| **I — Unterschicht** | Eisen, Zinn, Knochen, ungefärbtes Leinen | Frei verfügbar, Markt und Schwarzmarkt | Gesetzlos, mittellos |
| **II — Handwerker** | Gehärteter Tiegelstahl, Silber, Malachit, gefärbtes Leinen | Gilden-Markt (kein Ruf nötig) | Respektabler Handwerker |
| **III — Meister** | Damaszener-Stahl, Bronzeguss, Bergkristall | Gilden-Zugang (Ruf: Anerkannt) | Gilden-Mitglied, mittlerer Stand |
| **IV — Elite** | Titan-Legierungen, Roségold, Lapislazuli | Gilden-Zugang (Ruf: Vertraut) + Krone-Passierschein | Oberschicht, Gildenmeister |
| **V — Schwellen** | Schwellenlegierungen, Schwellenfäden, Schwellentalg, Schwellenlinsen | Hoher Gildenruf (Ruf: Meister) ODER Schlund-Schwarzmarkt (mit Fieber-Risiko) | Verboten / Begehrt |

**Materialklasse I–II** sind für den gesamten Spielverlauf das Brot-und-Butter-Material. Ein gut gefertigtes Tiegelstahl-Schwert von einem Spieler mit Muskel III übertrifft ein schlecht gehandhabtes Damaszener-Schwert von einem Spieler mit Muskel I. Das System belohnt Können, nicht nur Material.

**Materialklasse V (Schwellen-Materialien)** sind das Endgame-Crafting. Zwei Zugangswege:
1. Gilden-Weg: Langer Ruf-Aufbau, sicher, legal, teuer
2. Schwarzmarkt-Weg: Sofort verfügbar, illegal, und jedes Stück Schwellenmaterial, das nicht durch Gildenverarbeitung gesichert ist, trägt Schattenfieber-Exposition — jede Verarbeitung erhöht den Lymph-Wert

### Handwerk-Mechanik

Crafting in RELICS ist aktiv, nicht passiv. Der Spieler sitzt nicht in einem Menü — er steht an einer Werkbank (oder einem Schmiedefeuer) und führt eine vereinfachte Handwerks-Sequenz durch.

**Werkzeug-Erfordernisse:** Verschiedene Materialien brauchen verschiedene Werkzeugqualitäten. Eisen lässt sich mit einer einfachen Feldschmiede verarbeiten. Damaszener-Stahl braucht eine Meister-Schmiede — die in der Regel Gilden-Territorium ist. Der Spieler muss also entweder Zugang zu Gilden-Infrastruktur erkaufen oder seine eigene Werkbank schrittweise ausbauen.

**Rezeptur-System:** Rezepturen sind keine automatischen Freischaltungen. Sie sind Wissen — Wissensgegenstände in der Welt:
- Öffentliches Wissen (Rezepturen für Klasse I–II): In der Welt verfügbar, NPCs zeigen sie, Bücher enthalten sie
- Gilden-Wissen (Rezepturen für Klasse III–IV): Nur durch Gilden-Zugehörigkeit oder Entwendung zugänglich
- Geheimes Wissen (Rezepturen für Klasse V): Liegt in Gilden-Archiven, Orden-Archiven, oder bei bestimmten NPCs mit eigenem Preis

**Qualitätsstufen beim Crafting:** Ein Produkt kann in drei Qualitätsvarianten erzeugt werden — Grundlegend / Ordentlich / Meisterwerk. Die Variante hängt ab von: Materialqualität, Werkzeugqualität, und einer kleinen Skill-Komponente (die sich mit Wiederholung verbessert — Muskel-Subsystem-Synergy). Meisterwerke sind selten, aber real, und bei bestimmten NPCs hochbegehrt (Trade-Commodity).

### Rüstungsdesign als sozialer Ausdruck

Die Rüstung des Spielers ist das visuelle Statusstatement. Das System erkennt das und macht es spielmechanisch relevant:

- **Rüstungsklasse** (leicht / mittel / schwer) beeinflusst Ausdauerkosten und Beweglichkeit
- **Material** definiert Schutzwerte und NPC-Reaktionen (ein Spieler in Tiegelstahl wird in Oberschicht-Bereichen anders angesprochen als einer in Eisen)
- **Ausrüstungsmix:** Der Spieler kann jedes Körperteil unabhängig ausrüsten. Eine Kombination von schwerer Schulterpartie mit leichten Beinen ist möglich und sinnvoll.
- **Verfall und Reparatur:** Rüstungen und Waffen nehmen Schaden. Reparatur ist eine Alltagshandlung. Das verhindert, dass der Spieler "set and forget" spielt — er muss aktiv mit seinem Equipment interagieren.

---

## 2.4 Fraktionsruf-System

### Spieler-Fantasie

*"Ich habe mir diese Tür verdient. Oder ich habe sie mir verbaut."*

### Designprinzipien

Das Fraktionsruf-System ist kein Gut-/Böse-Barometer. Es ist eine Buchführung von Handlungen und ihren Konsequenzen. Jede Fraktion bewertet den Spieler nach eigener Logik — und die Logiken widersprechen sich.

Das System funktioniert nach dem Prinzip der kommunizierenden Röhren: Was bei der Krone gewinnt, verliert in der Regel bei den Gilden oder beim Orden. Ausnahmen existieren (neutrale Handlungen), aber echte Maximierung bei allen drei gleichzeitig ist nicht möglich.

### Ruf-Stufen

Jede Fraktion kennt fünf Ruf-Stufen:

| Stufe | Bezeichnung | Zugang | Hinweistext |
|---|---|---|---|
| I | **Unbekannt** | Basiszugang zu öffentlichen Bereichen der Fraktion | "Sie sind neu hier." |
| II | **Bekannt** | Einfache Aufgaben verfügbar, Händler gewähren Basispreise, erste innere Tore offen | "Man hat von Ihnen gehört." |
| III | **Anerkannt** | Mittlere Materialien zugänglich, wichtigere NPCs sprechen direkt, Zugang zu Fraktions-Infrastruktur (Schlafplatz, Werkstätte) | "Sie haben sich als nützlich erwiesen." |
| IV | **Vertraut** | Elite-Materialien verfügbar, Insider-Informationen, Fraktions-Missionen auf hohem Niveau, spezifische Ausrüstung als Geschenk | "Sie sind einer von uns." |
| V | **Meister** | Vollzugang. Schwellen-Materialien (Gilden), Kronpassagen (Krone), geheime Orden-Archive, Entscheidungen beeinflussen Fraktionspolitik | "Ich vertraue Ihnen mein Leben an." |

**Ruf-Verlust:** Handlungen gegen eine Fraktion senken den Ruf. Ruf kann nicht "doppelt negativ" werden — die Mindststufe ist "Feindselig":

| Sonderstufe | Bezeichnung | Konsequenz |
|---|---|---|
| 0 | **Feindselig** | Tore geschlossen. NPCs greifen an oder fliehen. Keine Handelsinteraktion möglich. Nur über Quest-Lösung (spezifisch für jede Fraktion) auflösbar. |

### Ruf-Quellen

Ruf wird erzeugt durch:
- **Quests:** Hauptquelle. Direkte Fraktionsquests geben klaren Ruf-Gain. Offene Quests von Fraktions-NPCs geben Ruf bei der entsprechenden Fraktion.
- **Handlungen in der Welt:** Wächter der Krone angreifen = Krone-Ruf verloren, unabhängig davon ob die Wachen "böse" waren. Gilden-Eigentum stehlen = Gilden-Ruf verloren. Das System beobachtet still.
- **Dialoge und Entscheidungen:** Bestimmte Gespräche haben Ruf-Konsequenzen, die nicht explizit angezeigt werden. Der Spieler spürt sie an veränderten NPC-Reaktionen.
- **Handels-Reputation:** Wer konsequent bei einer Fraktion kauft, gewinnt langfristig Ruf (klein, aber akkumulierend).

### Konflikt-Mechanik: Wenn Fraktionen kollidieren

Ab einem bestimmten Ruf-Niveau in zwei konkurrierenden Fraktionen verlangen beide, dass der Spieler "Farbe bekennt." Das ist kein Quest — das ist eine stille Kulminierung. Ein Gildenmeister sagt dem Spieler: "Ich habe gehört, Sie arbeiten auch für den Orden. Das ist eine Frage, die ich nicht nochmals stellen will." Das Spiel erzwingt keine Entscheidung — aber es macht deutlich, dass die Situation sich nicht halten lässt.

**Point of No Return:** Jede Fraktion hat einen quest-spezifischen Punkt, an dem der Spieler sich endgültig entscheiden muss. Diese Punkte kommen nicht gleichzeitig und werden dem Spieler nicht explizit als "Point of No Return" angezeigt. Er merkt erst rückwirkend, wann er die Entscheidung getroffen hat.

### Gilden-Monopolstruktur und Crafting-Zugang

Das Fraktionsruf-System bei den Gilden ist speziell: Die Gilden sind kein monolithischer Block. Es gibt sieben große Gilden (Schmiede, Glasmacher, Weber, Gerber, Goldschmiede, Kerzenzieher, Pergamenter), und der Ruf bei der Gilden-Fraktion insgesamt beeinflusst den Basisrand. Darüber hinaus gibt es Einzel-Ruf bei spezifischen Gilden:

- **Schmiede-Ruf:** Zugang zu Waffen und Rüstungen der Klasse III–IV
- **Glasmacher-Ruf:** Zugang zu Optik-Instrumenten, Schwellenlinsen, alchemistischen Phiolen
- **Gerber-Ruf:** Zugang zu Kanälen und dem Schlund — physischer Zugang, nicht nur Handel
- **Weber-Ruf:** Schwellenfäden und Elite-Textilien

Wer nur Gilden-Gesamtruf sammelt, ohne einzelne Gilden zu pflegen, bekommt generischen Zugang. Wer gezielt eine Gilde hofiert, bekommt spezifische Tiefe.

---

## 2.5 Schattenfieber-Progression

### Spieler-Fantasie

*"Ich sehe, was das Fieber aus mir macht. Ich entscheide, wie weit ich gehe."*

### Designprinzipien

Das Schattenfieber ist keine Krankheit, die man heilt. Es ist ein Zustand, den man navigiert. Drei Fraktionen, drei Strategien. Keine davon ist optimal — alle haben Kosten und Vorteile.

Das Fieber ist direkt an das Lymph-Subsystem gekoppelt (→ Abschnitt 2.2). Die Stadien des Lymph-Subsystems entsprechen den Schattenfieber-Stufen. Dieser Abschnitt beschreibt die Gameplay-Konsequenzen und die Fraktions-Antworten im Detail.

![Schwellenanker: Zustand Null — ruhend](../concepts/day02-vera/relics/relikt-zustand-null-ruhend_seedream-4-5.png)

*Konzeptbild: Der Schwellenanker in Ruhezustand. Die visuelle Sprache des Ruhezustands spiegelt die Baseline des Lymph-Subsystems (Stufe I: Unangetastet).*

### Die drei Fieber-Stadien im Gameplay

**Stadium I — Flüstern (Lymph-Stufe II: Exponiert)**

Das erste Stadium ist die Einladung. Es gibt nichts zu verlieren, aber etwas zu gewinnen:

*Vorteile:*
- Erweiterte Sinneswahrnehmung: Der Spieler sieht Schwellen-Objekte, die für andere unsichtbar sind (bestimmte versteckte Durchgänge, Schwellensubstrat-Konzentrationen, die den Weg zu Schwarzmarkt-Ressourcen weisen)
- Leichte intuitive Kampfunterstützung: Gegnerbewegungen werden einen Herzschlag früher "wahrgenommen" — kein Kampf-Autoziel, aber eine kleine Reaktionszeitverlängerung

*Kosten:*
- Gelegentliche Wahrnehmungsstörungen: Schatten an falscher Stelle, Geräusche ohne Quelle. Keinen spielmechanischen Nachteil — aber der Spieler merkt, dass etwas nicht stimmt
- Sichtbare leichte Veränderung: Unter bestimmtem Licht sind die Lymph-Muster unter der Haut sichtbar. Bestimmte NPCs reagieren darauf.

*Reversibilität:* Vollständig reversibel durch Entfernung von Fieberquellen und Krone-Medizin. Der Spieler kann hier jederzeit zurück.

**Stadium II — Wandlung (Lymph-Stufe III: Kontaminiert)**

Das zweite Stadium ist der Preis für Macht:

*Vorteile:*
- Deutliche physische Buffs: Erhöhte Stärke und Ausdauer (überlagert Muskel- und Cardio-Subsystem)
- Tiefere Schwellen-Wahrnehmung: Der Spieler nimmt Dünnstellen intuitiv wahr, kann Schwellensubstrat "spüren" (Mechanik: Kompass-ähnlicher Puls in Dünnstellen-Richtung)
- Immunität gegen leichte Schattenfieber-Exposition: Kontaminierte Bereiche, die andere töten würden, kann der Spieler bereisen

*Kosten:*
- Erinnerungsfragmentierung: Gelegentlich berichtet das Spiel eine Szene anders als beim ersten Erleben. Nicht gameplaymäßig einschränkend, aber psychologisch belastend
- Sichtbare Mutation: Dunkle Adern, teilweise Transparenz der Haut, veränderte Augen. Oberschicht-NPCs verweigern Interaktion. Bestimmte Questlinien werden unzugänglich (Orden-Questlinie kürzt sich dramatisch).
- Soziale Kosten: Krone-Ruf nimmt passiv ab, solange Stadium II aktiv ist

*Reversibilität:* Nicht heilbar, aber managebar. Gilden bieten Stabilisierungspräparate (teuer, laufende Kosten). Orden bietet Kontroll-Rituale (kostenlos, aber mit Dankesschuld).

**Stadium III — Entgrenzung (Lymph-Stufe IV: Durchdrungen)**

Das dritte Stadium ist das Ende der kontrollierten Progression:

*Vorteile:*
- Extremer Power-Spike: Der Spieler ist physisch auf dem Maximum. Übernatürliche Stärke, Schwellenwahrnehmung permanent aktiv, temporäre Unverwundbarkeit möglich
- Direkte Schwellen-Interaktion: Der Spieler kann Orte und Objekte berühren, die im normalen Zustand unzugänglich sind. Bestimmte Questenden werden erst hier zugänglich.

*Kosten:*
- Kontrollverlust: Spieleraktionen werden gelegentlich durch "Schwellen-Impulse" überlagert — die Figur handelt für Sekunden autonom
- Narrativer Sackweg: Ab Stadium III sind bestimmte Quest-Outcomes unmöglich. Der Spieler kann die Geschichte nicht mehr in bestimmte Richtungen lenken.
- Irreversibilität: Ohne Schwellenanker-Intervention oder Orden-Hochritual kein Zurück.

*Der Schwellenanker als Stabilisator:* Ein Spieler, der den Schwellenanker hält (Hauptquest-Fortschritt), kann Stadium III partiell stabilisieren. Das ist keine Heilung — aber es verhindert das unkontrollierte Durchgleiten in den Identitätsverlust. Dies ist der narrative und mechanische Kern des Hauptquests.

![Schwellenanker: Zustand Drei — Auflösung](../concepts/day02-vera/relics/relikt-zustand-drei-aufloesung_seedream-4-5.png)

*Konzeptbild: Zustand Drei. Der Schwellenanker in Auflösung — die visuelle Entsprechung von Lymph-Stufe IV. Die Grenzen zwischen Objekt und Umgebung lösen sich auf.*

### Die drei Fraktions-Antworten auf das Schattenfieber

**Krone — Unterdrückung**

Die Krone behandelt das Schattenfieber als militärisches Problem. Ihre Ärzte und Quartiermeister bieten Krone-Medizin: Suppressoren, die den Lymph-Wert aktiv senken und Stufe I reversieren.

*Gameplay:*
- Krone-Medizin ist kostenlos für Krone-Mitglieder, teuer für andere
- Unterdrückung verhindert alle Fieber-Vorteile — aber auch alle Fieber-Kosten
- Krone-Weg-Spieler sind das "saubere" Spielprofil: sozial akzeptiert, alle Questlinien offen, aber ohne Fieber-Buffs auf physische Ressourcen angewiesen

*Trade-off:* Wer den Krone-Weg geht, verzichtet auf die Macht des Fiebers. Krone-Quests kompensieren das durch bessere Ausrüstung, Zugang zu Tiegelstahl-Waffen, und politische Unterstützung.

**Gilden — Verwertung**

Die Gilden sehen das Schattenfieber als Rohstoff. Ihre Alchemisten bieten Stabilisierungspräparate, die den Lymph-Wert auf einem Plateau halten: Die Vorteile von Stadium I bleiben zugänglich, die unkontrollierte Progression zu Stadium II wird verhindert.

*Gameplay:*
- Gilden-Präparate sind teuer und müssen regelmäßig erneuert werden (laufende Ressourcenkosten)
- Wer mit Gilden-Zugang arbeitet, kann Stadium I kontrolliert halten — und bei Bedarf (für kurze Zeit, mit Nachkater) auf Stadium II übersteigen
- Gilden-Weg-Spieler sind das "pragmatische" Spielprofil: sie nutzen das Fieber als Werkzeug, zahlen dafür regelmäßig, und halten Optionen offen

*Trade-off:* Ressourcenintensiv. Wer keine konstante Einnahmequelle hat, kann den Gilden-Weg nicht aufrechterhalten. Das verknüpft Fieber-Management direkt mit der Wirtschaftsmechanik.

**Orden — Destillation und Verstehen**

Der Orden behandelt das Schattenfieber als Prüfung und als Zugang zu Wissen. Ihre Rituale ermöglichen kontrollierten, langsamen Aufstieg durch die Stufen — mit Stabilisierung auf jeder Ebene.

*Gameplay:*
- Orden-Rituale sind kostenlos (Kosten: Zeit und Verpflichtung gegenüber dem Orden)
- Wer den Orden-Weg geht, kann das Fieber tiefer nutzen als der Gilden-Weg — bis in Stadium II hinein, stabil
- Orden-Weg-Spieler sind das "tiefste" Spielprofil: Sie verstehen das Schattenfieber am besten, haben den tiefsten Lore-Zugang, aber der Orden hat eine Agenda

*Trade-off:* Der Orden will etwas. Jedes Ritual ist eine Schuld. Irgendwann fragt der Orden nach dem Schwellenanker.

---

## 2.6 Systeminteraktionen

Die fünf Kernsysteme existieren nicht isoliert. Ihre Stärke kommt aus den Wechselwirkungen:

**Kampf × Nervensystem-Leveling**
Jeder Kampf trainiert Cardio und Muskel. Ein Spieler, der kämpft, wird besser im Kampf. Das ist die direkteste Feedback-Schleife. Aber: Wer riskante Kämpfe mit Schwellensubstrat-Extrakten gewinnt, trainiert auch das Lymph-Subsystem — ungewollt.

**Crafting × Fraktionsruf**
Bessere Materialien erfordern höheren Fraktionsruf. Das bindet Crafting an Fraktionsentscheidungen. Wer den Orden hofiert, bekommt kein Damaszener-Stahl — der Orden handelt nicht mit Waffen. Wer die Gilden höfiert, verliert Krone-Ruf. Crafting-Optimierung ist Fraktions-Optimierung.

**Schattenfieber × Fraktionsruf**
Der Fieber-Status des Spielers verändert Fraktions-Reaktionen. Ein Spieler in Stadium II ist bei der Krone nicht mehr willkommen. Ein Spieler in Stadium I wird vom Orden besonders aufmerksam behandelt (sie wollen wissen, wie weit er bereits ist). Die Gilden sind die einzige Fraktion, die aktive Fieber-Träger ohne Stigma bedient — weil sie sie als Kunden brauchen.

**Nervensystem-Leveling × Crafting**
Muskel-Stufe III+ ist Voraussetzung für sinnvolle Nutzung von Klasse-IV-Ausrüstung. Der Spieler kann sich die besten Materialien kaufen — aber erst nutzen, wenn der Körper folgt. Das verhindert "Day-One-Endgame-Gear" und macht die Progression organisch.

**Kampf × Schattenfieber**
Wer mit Schwellensubstrat-Extrakten kämpft, gewinnt Macht und verliert Kontrolle. Der schnellste Weg zum Kampfsieg ist oft der direkteste Weg in Stadium III. Das ist die ultimative Abwägung des Systems.

---

<!-- Darius: Offene Punkte für interne Klärung — nicht im sichtbaren Dokument. W-001/W-002 aus Emres WBB (Schwellensubstrat als Substanz vs. Feld, Kippmoment Stufe I → II) müssen vor v2 dieses Kapitels synchronisiert werden. Leo-QA-Pass auf Balancing-Werte (Ruf-Schwellenwerte, Lymph-Akkumulation) steht aus. -->

*Versionsstatus: v1 — Alle fünf Kernsysteme ausgearbeitet. Balancing-Werte (konkrete Zahlenwerte) folgen in v2 nach Leo-QA-Sync. Systeminteraktionen definiert. Spieler-Fantasie-Statements verifiziert.*
