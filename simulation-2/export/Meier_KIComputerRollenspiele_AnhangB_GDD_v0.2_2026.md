---
title: "RELICS — Game Design Document"
subtitle: "Anhang B · v0.2"
short-title: "GDD"
author: "GenSoftworks Studio Simulation"
date: "2026"
lang: german
toc: true
---

# GDD Kapitel 01 — Spielübersicht & Design-Säulen

<!-- Darius: v2 — Aktualisierungen: "Schwarzrand" als offizieller Stadtname, "Schwellenanker" als Relikt-Bezeichnung (CD bestätigt, Tag 3 Briefing). Tiervolk-Eintrag in Tabelle 10 aktualisiert nach CD-Feedback Tag 4: Tiervolk = kosmologisch-fremde Wesen in dauerhafter, irreversibler Symbiose mit Tieren. Alle Statuszeilen und Autorenvermerke in HTML-Kommentare verschoben. -->

---

## 1. Projekttitel & Format

**Serientitel:** RELICS
**Erste Iteration:** RELICS: Der Schwellenanker
**Format:** Single-Player Computer-Rollenspiel
**Perspektive:** Third-Person / First-Person, nahtlos umschaltbar
**Monetarisierung:** Premium, einmaliger Kaufpreis — keine Mikrotransaktionen, keine kleinen Add-ons. DLCs nach Full Release, ausschließlich groß.

---

## 2. High Concept Statement

RELICS fragt: *Wem gehört diese Welt — und was bist du bereit zu tun, um darin zu überleben?*

Du bist ein Fremder. Du weißt nicht, wer du warst. Du weißt nicht, warum du hier bist. Aber die Stadt vor dir funktioniert ohne dich — sie hat Regeln, Mächte, Hierarchien, die sich über Jahrhunderte eingeschliffen haben. Drei Fraktionen teilen die Welt unter sich auf: die Krone mit ihrem Militär und ihren leeren Kassen, die Gilden mit ihren Monopolen und ihrem Geld, der Orden mit seinem Wissen und seiner Inquisition. Keine ist gut. Keine ist böse. Alle sind konsequent.

Und dann gibt es das Schattenfieber. Eine Seuche, die den Körper verändert. Jede Fraktion hat eine andere Erklärung — alle drei liegen falsch, aber jede liegt anders falsch. Die Wahrheit liegt tiefer. Unter der Stadt, in der Stille unter dem Stein, wartet etwas, das die Grenze zwischen den Ebenen des Seins zusammenhält. Es heißt der **Schwellenanker**. Es schwächt sich ab. Und das Fieber breitet sich aus.

Du wirst hineingezogen, ob du willst oder nicht. Was du daraus machst — das ist das Spiel.

---

## 3. Spieler-Fantasie-Statement

**"Ich betrete als Fremder eine aufregende Sandbox."** *(Briefing, unveränderlich)*

Ausformuliert:

Der Spieler soll sich fühlen wie jemand, der eine fremde Stadt zum ersten Mal betritt und merkt, dass sie *funktioniert* — Händler handeln, Wachen patrouillieren, Gildenmeister verhandeln, Ordensboten eilen durch Gassen. Er ist das Störelement. Die Welt hat ohne ihn existiert. Sie lässt ihn rein — zögernd, abwartend, mit Hintergedanken.

Das Versprechen: *Ich kann hier meine eigene Geschichte schreiben. Nicht eine Geschichte, die mir das Spiel aufzwingt. Meine.*

Drei konkrete Fantasien, die dieses Statement trägt:

1. **Agentschaft:** Ich löse jedes Problem auf meine Weise. Schleiche ich durch den Gilden-Checkpoint, bestehe ich ihn oder erkaufe ich mir Durchgang?
2. **Aufstieg:** Ich fange mit Eisengerät an und arbeite mich in eine Welt vor, in der Titan-Legierungen und Tiegelstahl die Sprache der Macht sind. Mein Körper ist mein Fortschrittsanzeiger.
3. **Konsequenz:** Meine Entscheidungen formen die Welt. Wenn ich für die Gilden arbeite, verschließt mir der Orden Türen. Das ist kein Bug. Das ist der Vertrag.

---

## 4. Game Feel

**RELICS-Game-Feel in einem Satz:**
*Ich stehe am Rand einer lebendigen, gefährlichen Welt und spüre, dass meine nächste Entscheidung etwas verändert.*

**Textur dieser Empfindung:**
- **Schwere.** Kämpfe sind nicht flüssig und elegant — sie kosten etwas. Ein Schwerthieb fordert Kraft, eine Parade fordert Timing. Der Körper des Spielers ist spürbar.
- **Reibung.** Die Stadt gibt sich nicht preis. Gilden-Tore sind gesperrt. Ordenswächter beobachten. Die Krone erwartet. Diese Reibung ist kein Fehler — sie ist das Medium, durch das sich Fortschritt anfühlt.
- **Staunen + Bedrohung.** Die Biolumineszenz in den Kanälen leuchtet schön. Sie leuchtet, weil dort das Fieber am stärksten ist. Die Welt ist attraktiv und gefährlich zur selben Zeit.
- **Dichte.** Jeder NPC hat eine Funktion, einen Tagesablauf, ein Gesicht. Niemand steht als Dekoration herum. Das fühlt sich nicht wie ein Videospiel an — es fühlt sich wie eine Welt an.

---

## 5. Genre & Perspektive

| Parameter | Wert |
|---|---|
| Genre | Action-RPG / Immersive Sim |
| Ton | Dark Fantasy — düster, geerdet, politisch |
| Setting | Medieval Cyberpunk: frühes Spätmittelalter + High-Tech-Materialien |
| Perspektive | Third-Person (Standard) / First-Person (umschaltbar) |
| Weltstruktur | Semi-Open-World: dichte, handgefertigte Kernregion statt weiter Leerfläche |
| Kampf | Real-Time Action, Melee-fokussiert, gewichtig |
| Magie | Keine. Alchemie + Schattenfieber-Transformationen (mit Kosten, je nach Körperreaktion) |
| Referenzen | Gothic 2, Deus Ex, Vampires the Masquerade: Bloodlines, Prey 2017 |
| Explizite Nicht-Referenzen | Kein Steampunk. Kein High Fantasy. Kein Zauberstab. |

**Verortung auf dem Fantasy-Spektrum:**
Medium-Fantasy — zwischen Low und High. Low-Magic, High-Tech (Materialien als Technologie). Biotech-Futurismus, der sich von innen wie Alchemie anfühlt, nicht wie Science-Fiction.

---

## 6. Die vier Design-Säulen

Diese vier Säulen sind Designfilter, keine Marketingversprechen. Jedes Feature, das in die Produktion geht, muss gegen mindestens zwei dieser Säulen bestehen. Features, die keine einzige Säule stärken, werden gestrichen.

---

### Säule I — Immersive Simulation

**Statement:** Jedes Problem hat mehr als eine Lösung. Die Welt reagiert konsequent auf das, was der Spieler tut.

**Was das bedeutet:**
- NPCs verhalten sich nach eigener Logik, nicht nach Spieler-Bequemlichkeit. Ein Gildenmeister macht keine Ausnahmen, weil der Spieler nett fragt — er macht sie, wenn der Spieler etwas wert ist.
- Physische Eigenschaften der Welt sind konsistent. Eine verschlossene Tür bleibt verschlossen, bis der Spieler den Schlüssel hat, sie aufbricht, das Schloss knackt oder einen anderen Eingang findet. Es gibt keinen magischen "Interagiere"-Knopf.
- Fraktionsentscheidungen haben echte systemische Konsequenzen. Wer für den Orden arbeitet, verliert Gilden-Ruf. Das System buchführt still.
- Mehrere Lösungswege sind keine Checkboxen ("Stealth/Kampf/Dialog") — sie entstehen aus dem Zusammenspiel von Spieler-Fähigkeiten, Umgebung und Fraktionsstand.

**Spieler-Fantasie:** *"Diese Welt reagiert auf mich. Ich bin nicht auf einem Schienen-Trip."*

**Referenz:** Warren Spector, Deus Ex GDD v5.3e (Ion Storm, 1997): "The world simulation allows players to solve problems in a variety of ways."

---

### Säule II — Fraktionspolitik als Kernspannung

**Statement:** Kein Gut gegen Böse. Drei konkurrierende Mächte, jede mit innerer Logik, jede mit konkreten Ressourcen, die sie kontrollieren.

**Was das bedeutet:**

| Fraktion | Ressource | Gameplay-Zugang | Fantasie |
|---|---|---|---|
| **Die Krone** | Territorium, Militärpassagen, Rechtsstatus | Schutz, Bewegungsfreiheit, Ehrentitel | Legitimität erkaufen |
| **Die Gilden** | Materialien, Handwerksrezepturen, Schwarzmarkt | Crafting-Tiefe, Upgrade-Pfade, Händler-Netzwerke | Macht durch Handwerk |
| **Der Orden** | Wissen, Fertigkeitsbücher, Bildungsmonopol | Skill-Upgrades, Lore-Zugang, Heilkunde | Verständnis als Waffe |

Fraktionsruf ist keine abstrakte Zahl — er ist der Schlüssel zu konkreten Spielsystemen. Wer bei den Gilden gut steht, kommt an Damaszener-Stahl. Wer beim Orden arbeitet, versteht das Schattenfieber tiefer.

Kein moralischer Zeigefinger. Jede Fraktion hat einen sympathischen Einstiegspunkt, einen Moment der Kompliziertheit, und einen Point of No Return.

**Spieler-Fantasie:** *"Ich wähle nicht die gute Fraktion. Ich wähle meine Fraktion."*

**Referenz:** Vampire: The Masquerade — Bloodlines (Troika Games, 2004).

---

### Säule III — Körperlicher Fortschritt

**Statement:** Der Körper des Spielers ist der Charakter. Fortschritt ist sichtbar, spürbar, und hat Kosten.

**Was das bedeutet:**

Das Nervensystem-Leveling ersetzt klassische Attribut-Grids und Erfahrungspunkte-Balken. Drei Subsysteme:

| Subsystem | Trainiert durch | Mechanische Auswirkung |
|---|---|---|
| **Cardio** | Laufen, Ausdauerkämpfe, Flucht | Ausdauer, Bewegungsgeschwindigkeit, Regeneration |
| **Muskel** | Schwertkampf, Tragen, physische Arbeit | Schadenswerte, Tragegewicht, Rüstungseffizienz |
| **Lymph** | Alchemika einnehmen, Schattenfieber-Exposition, Heilrituale | Widerstandsfähigkeit gegen das Fieber, Zugang zu Transformationen, Risiko |

Jedes Subsystem hat vier Qualitätsstufen (nach dem Deus Ex-Modell: Untrained / Geübt / Fortgeschritten / Meister). Keine 1-100-Skalen. Qualitätswechsel, keine Zahlenoptimierung.

**Das Schattenfieber als dritte Progressionsachse:**
- Das Lymph-Subsystem koppelt direkt an die Schattenfieber-Progression (drei Stadien: Flüstern / Wandlung / Entgrenzung)
- Die Transformation je nach Körperreaktion — kein Spieler durchläuft sie identisch
- Wer das Fieber unterdrückt (Krone-Weg), bleibt "sauber", verliert aber Zugang zu bestimmten Fähigkeiten
- Wer das Fieber nutzt (Gilden-Weg), gewinnt Kraft, bezahlt mit Körper
- Wer das Fieber versteht (Orden-Weg), bekommt tieferen Lore-Zugang, aber der Orden will etwas dafür

Das ist kein Magiesystem mit anderem Namen. Die Kosten sind real. Ein Spieler mit fortgeschrittenem Fieber wird *gezeichnet*.

**Spieler-Fantasie:** *"Mein Körper ist mein Fortschrittsanzeiger. Ich sehe, was ich trainiert habe — und was es mich gekostet hat."*

**Referenz:** Warren Spector, Deus Ex GDD v5.3e: Skill-Granularität über vier Qualitätsstufen statt 1-100-Skala.

---

### Säule IV — Dichte vor Breite

**Statement:** Handgefertigte Welt, handgefertigte Begegnungen. Lieber zwanzig NPCs mit Persönlichkeit als zweihundert mit Füll-Dialog.

**Was das bedeutet:**
- **Schwarzrand** ist der Kern. Keine riesige Weltkarte mit leeren Gebieten dazwischen. Eine Stadt, vertikal geschichtet (Obere Ränder / Mittelwand / Schlund), dicht belebt.
- Jede Zone hat eigene Materialsprache, eigene Architektur, eigenen NPC-Typ. Der Spieler liest Schicht und Status sofort ab — ohne HUD-Icon.
- NPCs haben Tagesabläufe. Wachen lösen ab. Märkte öffnen und schließen. Ein Schmied, der um 14:00 in der Hammergasse arbeitet, ist um 20:00 in der Kneipe.
- Seitenquests entstehen aus der Welt, nicht aus Ausrufezeichen über NPC-Köpfen.
- Kein Loot-Bloat. Materialien sind knapp. Ein Stück Damaszener-Stahl ist ein Ereignis.

**Der Gothic-Kontrast zu Skyrim:**
Skyrim hat 300 Orte, an denen man Drachen töten kann. Gothic 2 hat Khorinis — und Khorinis *lebt*. Jeder Bewohner hat einen Namen, eine Meinung, einen Tagesablauf. Diese Dichte erzeugt die Illusion, in einer echten Welt zu sein. Das ist RELICS' Versprechen.

**Spieler-Fantasie:** *"Diese Welt existierte, bevor ich ankam. Sie wird nach mir weiterexistieren."*

**Referenz:** Gothic 2 (Piranha Bytes, 2002); Warren Spector, Deus Ex GDD v5.3e: "No weird 'game spaces'."

---

## 7. Tonalität

**Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.**

Das ist kein Grimdark um des Grimdark willen. Die Welt ist dunkel, weil die Verhältnisse dunkel sind. Die Krone hat leere Kassen und bröckelnde Legitimität. Die Gilden halten Monopole mit Gewalt. Der Orden hat Bildung als Kontrollmittel. Das ist keine Fantasy — das ist Struktur.

Das Schattenfieber ist das einzige Übernatürliche. Es wird ernst genommen, nie trivialisiert.

**Visuelle Signatur der Tonalität:**
- Oberschicht: All-Black, All-White, Monochrom — ein einzelner Neon-Akzent (leuchtendes Indigo, Blutrot, Giftgrün)
- Unterschicht: Grau, Braun, schmutzig — und gelegentlich ein gestohlenes Stück Farbe
- Biolumineszenz in den Kanälen: schön und bedrohlich
- Kein Zahnrad. Keine Dampfmaschine. Keine Hexagone.

---

## 8. Zielgruppe

RELICS spricht vier überlappende Spielertypen an:

1. **Immersion-First Players** — wollen sich in eine Welt verlaufen, nicht geführt werden (Kingdom Come: Deliverance, Disco Elysium, Outer Wilds)
2. **Faction Players** — "Ich wähle nicht die gute Fraktion" (VtM: Bloodlines, Fallout: New Vegas)
3. **Crafting/Progression Freaks** — wollen sichtbare Materialsprache, echte Upgrade-Tiefe, keine Loot-Inflation (Dark Souls, Stardew Valley)
4. **Medieval Aesthetics Obsessed** — reale mittelalterliche Logik + Biotech als Geheimnis, kein Kitsch (Kingdom Come: Deliverance, Mount & Blade)

**Kritisches Risiko:** Die erste Stunde ist kein Tutorial. Sie ist ein Angebot. Wenn der Spieler in Minute fünfzehn nicht versteht, was dieser Ort *ist*, verlieren wir ihn. Die erste Stunde muss stehen, wenn wir in die Streamer-Alpha gehen.

---

## 9. Abgrenzung

| Was RELICS IST | Was RELICS NICHT IST |
|---|---|
| Handgefertigte, dichte Welt | Weitläufige, leere Open World |
| Körperlicher Fortschritt sichtbar | Abstraktes Level-up-System |
| Drei Fraktionen ohne Moralkeulen | Gut-gegen-Böse-Struktur |
| Schattenfieber als biologische Wahrheit | Magiesystem mit Fantasy-Label |
| Spieler als namenloser Fremder | Spieler als vordefinierten Charakter |
| Medieval Cyberpunk: Material als Macht | Steampunk, High Fantasy, Science-Fantasy |
| Immersive Sim: mehrere Lösungswege | Schienenspiel mit Illusion der Wahl |

---

## 10. Geklärte Design-Fragen

| # | Frage | Antwort |
|---|---|---|
| 1 | **Schauplatz:** Eine Stadt oder mehrere? | EINE vertikale Stadt: **Schwarzrand**. Mitteleuropäisch, auf Felssporn gebaut, vertikal geschichtet in drei Zonen (Obere Ränder / Mittelwand / Schlund). |
| 2 | **Schattenfieber-Scope:** Wie tief geht die Integration? | Hauptquest-antreibend UND dritte Progressionsachse (Lymph-Subsystem). Drei biologische Stadien. Transformation je nach Körperreaktion — kein Spieler durchläuft sie identisch. Drei Fraktions-Antworten = drei Gameplay-Pfade. |
| 3 | **Tiervolk:** Wer sind sie? | Kosmologisch-fremde Wesen in dauerhafter, irreversibler Symbiose mit Tieren. NPC — Händler und Informationsbroker, nicht spielbar. Eigene Händler-Netzwerke außerhalb der drei Fraktionen. Brauchen Materialien zur Stabilisierung der Symbiose — das schafft echtes Handelsinteresse. |
| 4 | **Release-Modell:** Wie liefern wir? | Streamer-Alpha (erste Stunde muss stehen) → Beta (max. 6–12 Monate) → Full Release → große DLCs. |
| 5 | **Relikt-Name:** Wie heißt das zentrale Artefakt? | **Der Schwellenanker** — In-World-Begriff, CD-bestätigt. Das Fragment beim Spieler: ein Stück des Schwellenankers. |
| 6 | **Ablehn-Option:** Kann der Spieler das Fragment ablehnen? | Ja — CD-bestätigt. Der Spieler darf das Fragment von Hieronymus Vael ablehnen. Konsequenzen in Kapitel 3 (Erzählkonzept) ausgearbeitet. |

<!-- Darius: Alle Design-Fragen geklärt. Tiervolk (W-004) durch CD-Feedback Tag 4 final geschlossen: dauerhaft, irreversibel, Handelsinteresse durch Symbiose-Stabilisierungs-Bedarf. Schattenfieber-Formulierung in Zeile 2 und 5 (Genre-Tabelle) angepasst: "Transformationen je nach Körperreaktion" statt "Mutationen". -->

\clearpage

# GDD Kapitel 02 — Kernmechaniken

<!-- Darius: v2 — Wesentliche Änderungen gegenüber v1: (1) Tiervolk als eigenständiger sechster Händlertyp integriert — dauerhaft-symbiotische Wesen mit spezifischem Handelsinteresse (Symbiose-Stabilisierungs-Materialien). (2) Schattenfieber als körperreaktionsabhängig ausgearbeitet — gleiche Exposition, individuelle Transformation, kein einheitlicher Pfad. (3) Autorenvermerke und Recherche-Kommentare bereinigt. (4) Seitenvolumen gekürzt. -->

---

## Überblick

Dieses Kapitel beschreibt die sechs Kernsysteme von RELICS: Der Schwellenanker. Jedes System ist direkt aus den Design-Säulen von Kapitel 1 abgeleitet und muss gegen mindestens zwei Säulen bestehen:

1. **Kampfsystem** — Säule I (Immersive Sim) + Säule III (Körperlicher Fortschritt)
2. **Nervensystem-Leveling** — Säule III (Körperlicher Fortschritt) + Säule I (Immersive Sim)
3. **Crafting & Materialsystem** — Säule II (Fraktionspolitik) + Säule IV (Dichte vor Breite)
4. **Fraktionsruf-System** — Säule II (Fraktionspolitik) + Säule I (Immersive Sim)
5. **Schattenfieber-Progression** — Säule III (Körperlicher Fortschritt) + Säule II (Fraktionspolitik)
6. **Händlernetz & Tiervolk** — Säule II (Fraktionspolitik) + Säule IV (Dichte vor Breite)

---

## 2.1 Kampfsystem

### Spieler-Fantasie

*"Jeder Kampf kostet mich etwas. Wenn ich gewinne, habe ich es mir verdient."*

### Designprinzipien

Das Kampfsystem von RELICS ist kein Showroom für Combo-Systeme. Es ist eine mechanische Umsetzung von Schwere und Konsequenz. Kämpfe sollen sich anstrengend anfühlen, nicht befriedigend-flüssig. Der Spieler soll nach einem schweren Kampf *erschöpft* sein.

**Referenz:** Gothic 2 (Piranha Bytes, 2002) — Kampf als Risiko, nicht als Komfort. Dark Souls (FromSoftware, 2011) — Positionierung, Gewicht, Kosten.

### Kernmechaniken des Kampfes

**Ausdauersystem (Stamina)**

Die zentrale Ressource im Kampf ist nicht Gesundheit, sondern Ausdauer. Jede Aktion kostet Ausdauer: leichte Angriffe wenig, schwere Angriffe viel, Parade und Ausweichen moderat. Ist die Ausdauer erschöpft, wird der Spieler anfällig — Paraden schlagen durch, Bewegung bricht ein. Ausdauer regeneriert mit kurzer Verzögerung nach der letzten Aktion.

Ausdauerkapazität und Regenerationsrate sind direkt mit dem Cardio-Subsystem verknüpft (→ Abschnitt 2.2).

**Trefferzonen & Positionierung**

Positionierung ist eine direkte taktische Variable: Angriffe von hinten ignorieren Rüstungsschutz der Vorderseite, Angriffe von der Seite umgehen aktive Paraden. Der Spieler kämpft in der Regel alleine gegen Gruppen. Positionierung an Engpässen ist keine Spielhilfe, sondern überlebensnotwendig.

**Waffenklassen und ihre Eigenlogik**

| Waffenklasse | Stärke | Schwäche | Besondere Eigenschaft |
|---|---|---|---|
| **Einhandschwert** | Ausgewogen, schnell | Mittlere Reichweite | Kann mit Schild kombiniert werden |
| **Zweihandschwert** | Hoher Schaden, gute Reichweite | Hohe Ausdauerkosten, langsamer | Rüstungsdurchdringung |
| **Dolch** | Sehr schnell, niedrige Kosten | Geringer Schaden, kurze Reichweite | Finisher-Angriffe im Schleich |
| **Axt** | Hoher Schaden gegen Rüstung | Langsam, keine Parade | Ignoriert anteilig Rüstungsschutz |
| **Streitkolben** | Effektiv gegen Plattenrüstung | Langsam, hohe Kosten | Betäubungseffekt bei vollem Treffer |
| **Bogen** | Distanzangriff, leise | Nachladezeit | Schwachstellen-Targeting möglich |
| **Armbrust** | Hohe Durchschlagskraft | Sehr lange Nachladezeit | Durchdringt schwere Rüstung |

Keine Waffe ist "die beste". Die Auswahl hängt von Gegnertyp, Umgebung und dem eigenen Muskel-Subsystem-Stand ab.

**Alchemie im Kampf**

Alchemika sind Hilfsmittel mit Nebenwirkungen: Stärkungstränke geben Temporärboni mit Nachkater, Heilmittel wirken langsam (nicht im aktiven Kampf), Schwellensubstrat-Extrakte erzeugen temporäre Stärke durch Fieberexposition. Jede Extrakt-Einnahme erhöht den Lymph-Wert (→ Abschnitt 2.5).

**Kampf vs. Ausweichen**

Das System belohnt den Spieler nicht dafür, möglichst viele Kämpfe zu gewinnen. Viele Begegnungen haben Umgehungswege: Soziale Lösungen (Fraktionsruf-basiert), Stealth-Wege, alternative Routen. Das Kampfsystem ist für die Fälle, in denen das nicht klappt.

---

## 2.2 Nervensystem-Leveling

### Spieler-Fantasie

*"Ich sehe meinen Fortschritt. Ich sehe, was er mich gekostet hat."*

### Das System im Überblick

Das Nervensystem-Leveling ersetzt klassische Erfahrungspunkte-Balken und Attribut-Grids vollständig. Der Spieler hat keinen "Level". Er hat drei Subsysteme, die sich durch tatsächliches Tun entwickeln.

**Philosophie:** Skill-by-Use nach Gothic-2-Logik, verfeinert durch das Deus-Ex-Modell der Qualitätsstufen: vier Qualitätsniveaus statt graduellem Zahlenfortschritt.

Das Nervensystem visualisiert sich durch eine halbtransparente Körperansicht: leuchtende Nervenbahnen zeigen aktive Subsysteme, trübe zeigen inaktive. Die Fieber-Infiltration des Lymphsystems ist in Echtzeit sichtbar.

![Nervensystem-Konzept: Schwellenanker-Relikt in Zustand Eins](../gallery/concepts/day02-vera/relics/relikt-zustand-eins-aktiviert_seedream-4-5.png)

*Konzeptbild: Biolumineszente Gefäßlinien — diese visuelle Sprache gilt für das Nervensystem-Leveling-Interface. Lymph-Kontamination folgt vergleichbaren Mustern.*

### Die drei Subsysteme

**Cardio — Das Ausdauersystem**

Trainiert durch: Ausdauerkämpfe, Sprinten, Klettern, Flucht-Sequenzen, Erkundung größerer Strecken ohne Rast.

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Untrainiert | Erschöpft schnell, langsame Regeneration |
| II | Geübt | Moderate Ausdauer, schnellere Regeneration |
| III | Fortgeschritten | Hohe Ausdauer, rapide Regeneration |
| IV | Meister | Ausdauer kein limitierender Faktor — Pausen werden taktisch, nicht notwendig |

**Muskel — Das Kraftsystem**

Trainiert durch: Nahkampfangriffe, schwere Gegenstände tragen, physische Arbeit (Schmieden helfen, Ladungen schleppen — auch das trainiert).

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Untrainiert | Minimaler Schaden, niedriges Tragegewicht |
| II | Geübt | Ordentlicher Schaden, Rüstung schränkt weniger ein |
| III | Fortgeschritten | Deutlicher Schadensbonus, schwere Rüstungen voll nutzbar |
| IV | Meister | Spitzenwerte, schwere Zweihandwaffen bevorzugt |

Muskel III+ ist Voraussetzung für sinnvolle Nutzung von Materialklasse IV. Der Spieler kann sich die besten Materialien kaufen — aber erst nutzen, wenn der Körper folgt.

**Lymph — Das Fieber-System**

Das Lymph-Subsystem ist das komplexeste der drei. Es bildet die biologische Schnittstelle zwischen Spielercharakter und Schwellenrealität.

Trainiert durch: Einnahme von Alchemika und Schwellensubstrat-Extrakten, Exposition in Dünnstellen, Heilrituale des Ordens, Kontakt mit dem Schwellenanker.

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Unangetastet | Baseline. Keine Symptome, keine Transformation, aber auch keine Lymph-Vorteile |
| II | Exponiert (*Flüstern*) | Sensorische Erweiterungen, Wahrnehmung versteckter Schwellen-Objekte |
| III | Kontaminiert (*Wandlung*) | Physische Buffs, aber kognitive Kosten; sichtbare körperliche Veränderungen |
| IV | Durchdrungen (*Entgrenzung*) | Irreversibel, massiver Power-Spike, zunehmender Kontrollverlust |

**Kritisch — Körperreaktion als Variable:** Stufe II und III verlaufen nicht für jeden Spieler identisch. Die spezifische Transformation hängt von der individuellen Expositionsgeschichte ab (welche Substanzen, welche Dünnstellen, welcher Fraktionspfad). Kein Spieler durchläuft dieselbe Wandlung. Das ist die Spieler-Fantasie: *"Das Fieber macht etwas aus mir — etwas, das kein anderer Spieler sieht."*

Reduktions-Mechanismen: Krone-Weg (medizinische Unterdrückung), Gilden-Weg (Plateau-Stabilisierung), Orden-Weg (kontrollierter Aufstieg mit Verständnis).

### Qualitätsstufen-Übergänge

Ein Qualitätsstufenwechsel ist ein Moment im Spiel. Keine Fanfare, keine Leveling-Bildschirme. Die Nervensystem-Ansicht zeigt kurz das aktive Subsystem aufleuchten. Der Spieler merkt es an der veränderten Performance, nicht durch eine UI-Meldung.

Der Spieler kann aktiv "investieren": Wer einen schweren Kampf erwartet, kann vorab das Muskel-Subsystem stimulieren (Kampfübungen, Schmiedearbeit). Kein Pflichtprogramm — aber ein strategischer Hebel.

---

## 2.3 Crafting & Materialsystem

### Spieler-Fantasie

*"Ein Stück Damaszener-Stahl ist ein Ereignis. Ich weiß, was ich tue, wenn ich es verarbeite."*

### Designprinzipien

Das Crafting-System von RELICS ist keine Item-Fabrik. Es ist ein Ausdruck der Fraktionspolitik und der Materialsprache der Welt. Materialien sind keine Zahlen — sie sind Hierarchien.

**Keine Loot-Inflation.** Ein Stück Tiegelstahl ist selten. Damaszener-Stahl ist eine Rarität. Schwellenlegierungen sind die gefährlichste und mächtigste Materialklasse, mit einem echten Preis.

### Materialklassen

| Klasse | Material-Beispiele | Zugang | Sozialer Status |
|---|---|---|---|
| **I — Unterschicht** | Eisen, Zinn, Knochen, ungefärbtes Leinen | Frei verfügbar, Markt und Schwarzmarkt | Gesetzlos, mittellos |
| **II — Handwerker** | Gehärteter Tiegelstahl, Silber, Malachit, gefärbtes Leinen | Gilden-Markt (kein Ruf nötig) | Respektabler Handwerker |
| **III — Meister** | Damaszener-Stahl, Bronzeguss, Bergkristall | Gilden-Zugang (Ruf: Anerkannt) | Gilden-Mitglied |
| **IV — Elite** | Titan-Legierungen, Roségold, Lapislazuli | Gilden-Zugang (Ruf: Vertraut) + Krone-Passierschein | Oberschicht |
| **V — Schwellen** | Schwellenlegierungen, Schwellenfäden, Schwellentalg, Schwellenlinsen | Gildenruf: Meister ODER Schlund-Schwarzmarkt (mit Fieber-Risiko) | Verboten / Begehrt |

Ein gut gefertigtes Tiegelstahl-Schwert von einem Spieler mit Muskel III übertrifft ein schlecht gehandhabtes Damaszener-Schwert von einem Spieler mit Muskel I. Das System belohnt Können, nicht nur Material.

**Materialklasse V (Schwellen-Materialien)** sind das Endgame-Crafting. Zwei Zugangswege: Gilden-Weg (langer Ruf-Aufbau, sicher, legal, teuer) oder Schwarzmarkt-Weg (sofort, illegal, jede Verarbeitung erhöht den Lymph-Wert).

<!-- Darius: Tiervolk als dritter Zugangsweg zu Klasse-V-Materialien ist möglich — aber nur für spezifische Symbiose-Materialien (Tiervolk-Spezialroute), nicht generisch. Das ist in Abschnitt 2.6 ausgearbeitet. -->

### Handwerk-Mechanik

Crafting ist aktiv, nicht passiv. Der Spieler steht an einer Werkbank oder einem Schmiedefeuer und führt eine vereinfachte Handwerks-Sequenz durch.

**Werkzeug-Erfordernisse:** Damaszener-Stahl braucht eine Meister-Schmiede — die in der Regel Gilden-Territorium ist. Der Spieler muss Zugang erkaufen oder eine eigene Werkbank ausbauen.

**Rezeptur-System:** Rezepturen sind Wissensgegenstände, keine automatischen Freischaltungen. Öffentliches Wissen (Klasse I–II) ist frei verfügbar. Gilden-Wissen (Klasse III–IV) erfordert Zugang oder Entwendung. Geheimes Wissen (Klasse V) liegt in Gilden- und Orden-Archiven oder bei bestimmten NPCs.

**Qualitätsstufen beim Crafting:** Ein Produkt kann in drei Qualitätsvarianten erzeugt werden — Grundlegend / Ordentlich / Meisterwerk. Die Variante hängt von Materialqualität, Werkzeugqualität und Wiederholungserfahrung ab.

### Rüstungsdesign als sozialer Ausdruck

- **Rüstungsklasse** (leicht / mittel / schwer) beeinflusst Ausdauerkosten und Beweglichkeit
- **Material** definiert Schutzwerte und NPC-Reaktionen
- **Ausrüstungsmix:** Jedes Körperteil unabhängig ausrüstbar
- **Verfall und Reparatur:** Rüstungen und Waffen nehmen Schaden — Reparatur ist eine Alltagshandlung

---

## 2.4 Fraktionsruf-System

### Spieler-Fantasie

*"Ich habe mir diese Tür verdient. Oder ich habe sie mir verbaut."*

### Designprinzipien

Das Fraktionsruf-System ist eine Buchführung von Handlungen und ihren Konsequenzen. Jede Fraktion bewertet den Spieler nach eigener Logik — und die Logiken widersprechen sich.

Das System funktioniert nach dem Prinzip der kommunizierenden Röhren: Was bei der Krone gewinnt, verliert in der Regel bei den Gilden oder beim Orden. Echte Maximierung bei allen drei gleichzeitig ist nicht möglich.

### Ruf-Stufen

Jede der drei Hauptfraktionen kennt fünf Ruf-Stufen:

| Stufe | Bezeichnung | Zugang |
|---|---|---|
| I | **Unbekannt** | Basiszugang zu öffentlichen Bereichen |
| II | **Bekannt** | Einfache Aufgaben, Basispreise, erste innere Tore |
| III | **Anerkannt** | Mittlere Materialien, Fraktions-Infrastruktur (Schlafplatz, Werkstätte) |
| IV | **Vertraut** | Elite-Materialien, Insider-Informationen, spezifische Ausrüstung als Geschenk |
| V | **Meister** | Vollzugang — Schwellen-Materialien (Gilden), Kronpassagen (Krone), geheime Orden-Archive |

| Sonderstufe | Bezeichnung | Konsequenz |
|---|---|---|
| 0 | **Feindselig** | Tore geschlossen, NPCs greifen an. Nur über spezifische Quest-Lösung auflösbar. |

### Ruf-Quellen

Ruf wird erzeugt durch: Fraktionsquests (Hauptquelle), Handlungen in der Welt (stiller Buchhalter), Dialoge und Entscheidungen (nicht immer explizit), Handels-Reputation (klein, aber akkumulierend).

### Konflikt-Mechanik

Ab einem bestimmten Ruf-Niveau in zwei konkurrierenden Fraktionen verlangen beide, dass der Spieler Farbe bekennt. Das ist keine erzwungene Entscheidung — aber die Situation hält sich nicht. **Point of No Return:** Jede Fraktion hat einen quest-spezifischen Punkt, der sich erst rückwirkend als solcher zeigt.

### Gilden-Monopolstruktur und Crafting-Zugang

Die Gilden sind kein monolithischer Block. Der Gesamt-Gildenruf beeinflusst den Basisrand. Darüber hinaus gibt es Einzel-Ruf bei spezifischen Gilden:

- **Schmiede-Ruf:** Waffen und Rüstungen der Klasse III–IV
- **Glasmacher-Ruf:** Schwellenlinsen, Alchemie-Phiolen
- **Gerber-Ruf:** Physischer Zugang zu Kanälen und dem Schlund
- **Weber-Ruf:** Schwellenfäden und Elite-Textilien

Wer nur Gilden-Gesamtruf sammelt, bekommt generischen Zugang. Wer gezielt eine Gilde hofiert, bekommt spezifische Tiefe.

---

## 2.5 Schattenfieber-Progression

### Spieler-Fantasie

*"Ich sehe, was das Fieber aus mir macht. Es macht etwas anderes als aus anderen."*

### Designprinzipien

Das Schattenfieber ist keine Krankheit, die man heilt. Es ist ein biologischer Zustand, den man navigiert. Die Körperreaktion ist individuell: gleiche Exposition, verschiedene Transformation. Das ist der Kern des Systems.

Das Fieber ist direkt an das Lymph-Subsystem gekoppelt (→ Abschnitt 2.2).

![Schwellenanker: Zustand Null — ruhend](../gallery/concepts/day02-vera/relics/relikt-zustand-null-ruhend_seedream-4-5.png)

*Konzeptbild: Der Schwellenanker in Ruhezustand — die visuelle Entsprechung von Lymph-Stufe I: Unangetastet.*

### Körperreaktions-Varianz

Dasselbe Schattenfieber-Stadium sieht bei drei Spielern verschieden aus. Die spezifische Transformation (welche Sinne sich schärfen, welche Fähigkeiten entstehen, welche Kosten der Körper zahlt) hängt ab von:

1. **Expositionsquelle:** Schwellensubstrat-Extrakte erzeugen andere Muster als Dünnstellen-Aufenthalt
2. **Fraktionspfad:** Orden-Rituale kanalisieren die Transformation anders als ungefilterte Exposition
3. **Körperliche Baseline:** Muskel- und Cardio-Stand beeinflussen, welche physischen Transformationen dominant werden

Das hat gameplay-mechanische Konsequenzen: Spieler können nicht vorab wissen, welche spezifischen Fähigkeiten ihre Transformation freischaltet. Das erzeugt Entdeckungsdruck und echte Differenzierung.

### Die drei Fieber-Stadien im Gameplay

**Stadium I — Flüstern (Lymph-Stufe II)**

Das erste Stadium ist die Einladung. Vorteile: Erweiterte Sinneswahrnehmung (Schwellen-Objekte sichtbar, die für andere unsichtbar sind), leichte intuitive Kampfunterstützung (Körperreaktion-abhängig). Kosten: Gelegentliche Wahrnehmungsstörungen, leichte sichtbare Veränderungen unter bestimmtem Licht.

*Reversibilität:* Vollständig reversibel durch Entfernung von Fieberquellen und Krone-Medizin.

**Stadium II — Wandlung (Lymph-Stufe III)**

Das zweite Stadium ist der Preis für Macht. Vorteile: Physische Buffs (Stärke, Ausdauer), tiefere Schwellen-Wahrnehmung, Immunität gegen leichte Exposition. Kosten: Erinnerungsfragmentierung, sichtbare körperliche Veränderungen (dunkle Adern, Transparenz der Haut — individuell variierend), soziale Kosten (Krone-Ruf sinkt passiv).

*Reversibilität:* Nicht heilbar, aber managebar. Gilden: Stabilisierungspräparate (laufende Kosten). Orden: Kontroll-Rituale (mit Dankesschuld).

**Stadium III — Entgrenzung (Lymph-Stufe IV)**

Das dritte Stadium ist das Ende der kontrollierten Progression. Vorteile: Extremer Power-Spike, direkte Schwellen-Interaktion, Zugang zu bestimmten Questenden. Kosten: Kontrollverlust (Spieleraktionen durch Schwellen-Impulse überlagert), narrative Einengung, Irreversibilität ohne Schwellenanker-Intervention.

*Der Schwellenanker als Stabilisator:* Ein Spieler, der den Schwellenanker hält (Hauptquest-Fortschritt), kann Stadium III partiell stabilisieren. Das ist keine Heilung — aber es verhindert den unkontrollierten Identitätsverlust. Dies ist der narrative und mechanische Kern des Hauptquests.

![Schwellenanker: Zustand Drei — Auflösung](../gallery/concepts/day02-vera/relics/relikt-zustand-drei-aufloesung_seedream-4-5.png)

*Konzeptbild: Zustand Drei. Der Schwellenanker in Auflösung — die visuelle Entsprechung von Lymph-Stufe IV.*

### Die drei Fraktions-Antworten auf das Schattenfieber

**Krone — Unterdrückung**

Krone-Medizin senkt den Lymph-Wert aktiv und verhindert Stufe I–IV vollständig. Gameplay: Krone-Mitglieder erhalten Medizin kostenlos, andere zahlen teuer. Kein Fieber-Vorteil, keine Fieber-Kosten — aber Krone-Quests kompensieren durch bessere Ausrüstung und politische Unterstützung.

**Gilden — Verwertung**

Gilden-Präparate halten den Lymph-Wert auf einem Plateau: Vorteile von Stadium I bleiben zugänglich, unkontrollierte Progression wird verhindert. Auf Abruf (kurz, mit Nachkater) kann Stadium II überstiegen werden. Gameplay: Ressourcenintensiv, laufende Kosten. Verknüpft Fieber-Management direkt mit der Wirtschaftsmechanik.

**Orden — Destillation und Verstehen**

Orden-Rituale ermöglichen kontrollierten, langsamen Aufstieg durch die Stadien mit Stabilisierung auf jeder Ebene. Zugang bis Stadium II möglich. Gameplay: Kostenlos (Kosten: Zeit und Verpflichtung). Der Orden hat Forderungen — jedes Ritual ist eine Schuld. Irgendwann fragt der Orden nach dem Schwellenanker.

---

## 2.6 Händlernetz & Tiervolk

### Spieler-Fantasie

*"Es gibt Händler, die andere nicht kennen — und Waren, die nur sie führen."*

### Designprinzipien

Das Händlernetz von RELICS ist kein monolithisches System. Neben den drei Fraktionsstrukturen (Krone-Lieferanten, Gilden-Händler, Orden-Ressourcen) existiert ein vierter Händlertyp mit eigener Logik: das Tiervolk.

Das Tiervolk sind kosmologisch-fremde Wesen in dauerhafter, irreversibler Symbiose mit Tieren. Diese Symbiose ist keine Besonderheit — sie ist ihre biologische Grundlage. Ihre Handelsmotivation ist konkret: Sie benötigen spezifische Materialien zur Stabilisierung der Symbiose, die die drei Fraktionen weder verstehen noch kontrollieren. Das schafft ein echtes wechselseitiges Interesse.

### Das Tiervolk als Händlertyp

**Systemisch:** Das Tiervolk betreibt ein Netz aus fluktuierenden Handelspositionen, das sich nicht mit den Fraktionsterritorien deckt. Ihre Standorte ändern sich — nicht willkürlich, sondern nach einer internen Logik, die der Spieler über Zeit lernt. Sie sind dort, wo Schwellenphänomene komplex und interessant sind: Übergangszone Gürtel/Schlund, bestimmte Dünnstellen-Nähepunkte, Kanaleingänge, die die Gilden nicht vollständig kontrollieren.

**Kein Fraktionsruf-System:** Das Tiervolk kennt keine Ruf-Stufen. Sie kennen **Vertrauens-Transaktionen**: Wer einmal unfair handelt, bekommt keinen zweiten Termin. Wer gut handelt, bekommt Zugang zu selteneren Waren. Das ist ein binäres, transaktionales System — kein skalierbarer Balken.

**Eigene Ruf-Achse:** Tiervolk-Vertrauen akkumuliert unabhängig von Fraktionsruf. Ein Spieler, der bei allen drei Fraktionen "Feindselig" ist, kann beim Tiervolk trotzdem gut stehen. Das macht sie zum einzigen Händlernetz, das eine verbrannte Spielfigur noch versorgt.

### Tiervolk-Warensortiment

Das Tiervolk handelt mit drei Kategorien, die kein anderer Händlertyp führt:

**Kategorie A — Symbiose-Materialien (Import):**
Substanzen, die das Tiervolk selbst braucht. Sie kaufen aktiv vom Spieler: bestimmte Schwellensubstrat-Konzentrationen aus tiefen Dünnstellen, spezifische Schwellenpilz-Derivate, biologische Proben aus Stadium-II-Betroffenen (wenn der Spieler einwilligt oder selbst betroffen ist). Diese Kategorie schafft eine Quest-Logik: Das Tiervolk als Auftraggeber für Beschaffungsmissionen.

**Kategorie B — Exklusive Waren (Export):**
Waren, die das Tiervolk selbst produziert oder aus Regionen mitbringt, die die drei Fraktionen nicht kennen: Symbiose-Erzeugnisse (organische Materialien, die halb-biologisch, halb-schwellentechnisch sind), Navigationswissen (Informationen über Dünnstellen-Pfade, die weder Gilden-Karte noch Orden-Archiv kennt), und spezifische Alchemika, die die Körperreaktion bei Schattenfieber modifizieren — nicht heilen, modifizieren.

**Kategorie C — Informationen:**
Das Tiervolk ist das einzige Netz, das ohne Fraktionsbindung handelt. Ihre Informationen beziehen sich auf Verbindungen zwischen Dünnstellen, Verhaltensmuster von Schwellen-Fauna, und Gerüchte aus Regionen jenseits von Schwarzrand. Sie haben eine vierte Kosmologie — das Schattenfieber als Kommunikation, nicht als Krankheit.

### Salva als Haupt-Kontakt

Salva (→ GDD Kap. 4, Abschnitt 4.5) ist der erste und wichtigste Tiervolk-NPC. Er funktioniert als Kontext-Lieferant, Informationsbroker und Einführung in das Tiervolk-Handelssystem. Der Spieler lernt das System über Salva — nicht durch Tutorial-Text, sondern durch Transaktion.

**Mechanische Besonderheit:** Salva erscheint nicht immer. Er hat ein Bewegungsmuster, das der Spieler erlernen kann. Wer weiß, wann und wo Salva auftaucht, hat einen strategischen Vorteil.

### Symbiose-Stabilisierungs-Quest-Logik

Das Tiervolk ist der einzige NPC-Typ, der den Spieler aktiv um etwas bittet, das mit seiner biologischen Notwendigkeit zusammenhängt. Das schafft eine Quest-Kategorie ohne Fraktionsstruktur: Beschaffungsaufträge für Symbiose-Materialien, Erkundungsaufträge zu unbekannten Dünnstellen, und — selten — Schutzaufträge, wenn ein Tiervolk-Händler in Gefahr ist.

**Spieler-Fantasie dieser Quests:** *"Ich helfe jemandem, der sich selbst nicht helfen kann — weil er etwas ist, das die Welt nicht versteht."*

---

## 2.7 Systeminteraktionen

Die sechs Kernsysteme existieren nicht isoliert. Ihre Stärke kommt aus den Wechselwirkungen:

**Kampf × Nervensystem-Leveling**
Jeder Kampf trainiert Cardio und Muskel. Wer riskante Kämpfe mit Schwellensubstrat-Extrakten gewinnt, trainiert ungewollt auch das Lymph-Subsystem.

**Crafting × Fraktionsruf**
Bessere Materialien erfordern höheren Fraktionsruf. Das bindet Crafting an Fraktionsentscheidungen. Wer den Orden hofiert, bekommt kein Damaszener-Stahl. Wer die Gilden höfiert, verliert Krone-Ruf.

**Schattenfieber × Fraktionsruf**
Der Fieber-Status verändert Fraktions-Reaktionen. Ein Spieler in Stadium II ist bei der Krone nicht mehr willkommen. Die Gilden sind die einzige Fraktion, die Fieber-Träger ohne Stigma bedient.

**Nervensystem-Leveling × Crafting**
Muskel III+ ist Voraussetzung für sinnvolle Nutzung von Klasse-IV-Ausrüstung. Das verhindert "Day-One-Endgame-Gear".

**Kampf × Schattenfieber**
Wer mit Schwellensubstrat-Extrakten kämpft, gewinnt Macht und verliert Kontrolle. Das ist die ultimative Abwägung des Systems.

**Tiervolk × Alle anderen Systeme**
Das Tiervolk interagiert quer durch alle Systeme: Sie kaufen Schattenfieber-Produkte, liefern Crafting-Materialien der Klasse V (Sonderweg), sind unabhängig von Fraktionsruf, und liefern Informationen, die Quest-Pfade verändern. Sie sind das systemische Sicherheitsnetz für Spieler, die alle Fraktionen verbrannt haben.

**Tiervolk × Schattenfieber × Körperreaktion**
Das Tiervolk verfügt über Alchemika, die die Körperreaktion bei Schattenfieber-Transformation modifizieren. Das ist nicht universell verfügbar — es setzt Tiervolk-Vertrauen voraus. Für Spieler, die ihre Transformation aktiv gestalten wollen, ist das Tiervolk der einzige Weg zu dieser Tiefe.

<!-- Darius: Systeminteraktionen vollständig auf sechs Systeme erweitert. Tiervolk-Interaktionen am Ende eingewoben. Körperreaktions-Varianz als eigenständiger Interaktions-Layer in Abschnitt 2.5 und 2.7 ausgearbeitet. -->

\clearpage

# GDD Kapitel 03 — Erzählkonzept

<!-- Darius: v2 — Wesentliche Änderungen gegenüber v1: (1) Zeitlinie der Öffnung überarbeitet: jahrelange Anbahnung (Covid-Analogie), kein plötzlicher Ausbruch. Akt 1 trägt diese Logik: Spieler kommt in eine Stadt, die sich seit Jahren langsam verändert, nicht in eine Akutkatastrophe. (2) Tiervolk-Integration: Salva ist kein Exot — er ist Teil eines langen Musters, das Spieler und Stadt verbindet. (3) Cleanup: Autorenerwähnungen, Planungskommentare, Namis-Placeholder bereinigt. Ablehn-Option vollständig integriert (aus GDD Kap. 4 v2, Nami). -->

---

## Überblick

Das Erzählkonzept von RELICS: Der Schwellenanker definiert, wie die Geschichte erzählt wird — nicht was die Geschichte ist. Die Handlung ist ein Werkzeug, um die vier Design-Säulen erfahrbar zu machen.

**Zentrales Erzählprinzip:** Der Spieler ist kein Held. Er ist ein Fremder, der in eine Situation hineingezogen wird, die ohne ihn bereits bestand. Die Geschichte ist nicht über den Spieler — sie ist eine Geschichte, in der der Spieler Entscheidungen trifft.

**Erzählstruktur:** Drei Akte, drei Fraktionspfade, mehrere Questlinien, die sich überschneiden und widersprechen. Kein Akt ist vollständig linear. Jeder Akt hat einen offenen Erkundungsraum, bevor der nächste narrative Anker kommt.

---

## 3.1 Die Zeitlinie der Öffnung — Erzählerischer Hintergrund

### Die Covid-Logik: Jahrelange Anbahnung, kein Schlag

Das wichtigste erzählerische Prinzip für Akt 1 ist das, was der Spieler nicht sieht: Die Öffnung der Ankerkammer war kein Schlag, der eine stabile Stadt zerbrochen hat. Es war ein langsamer Prozess — und Schwarzrand hat sich, wie jede Gesellschaft in einer schleichenden Krise, daran angepasst. Das ist die Covid-Analogie: keine plötzliche Apokalypse, sondern eine jahrelange Normalisierung des Abnormalen.

**Was vor dem Spiel passiert ist (Spieler kennt das nicht, Welt trägt es):**

Vor rund fünfundzwanzig Jahren öffnete eine Koalition aus Orden, Gilden und Krone die Ankerkammer. In den ersten Jahren schien wenig zu passieren. Das Schattenfieber war vorher schon da — als seltene Kuriosität im tiefen Schlund. Es wurde häufiger. Dann häufiger. Dann konnte man es nicht mehr ignorieren.

Die erste Reaktion war das, was Schwarzrand immer macht: vertuschen, verwalten, einteilen. Quarantänezonen entstanden nicht als Notfallmaßnahme, sondern als schrittweise Normalisierung — zuerst für "die Schlimmsten", dann für immer mehr. Die drei Fraktionen haben die Katastrophe nie als Katastrophe bezeichnet. Sie haben sie in Bürokratie eingehüllt. Berichte. Komitees. Sonderzonen.

Heute, fünfundzwanzig Jahre später, ist der Schlund das, was er ist: ein Ort, den die Stadt vergessen hat. Das Schattenfieber ist eine Realität, die alle kennen und niemand ausspricht. Die Fraktionen haben gelernt, damit zu leben — oder besser: damit Geld zu verdienen, Macht zu sichern, Wissen zu akkumulieren.

**Was das für den Spieler bedeutet:**

Der Fremde kommt nicht in eine akute Krise. Er kommt in eine Stadt, die in einem Dauerzustand der verwalteten Katastrophe lebt. Die Leute, die er trifft, sind nicht erschrocken — sie sind routiniert. Brenn hat die Quarantäne-Prozesse in- und auswendig. Kast hat ihr Destillationsarchiv seit Jahren. Scherer hat seinen Ur-Text seit drei Jahren kopiert.

Das ist die erzählerische Stärke der Zeitlinie: Der Spieler betritt eine Welt, die sich bereits mit dem Bösen arrangiert hat. Das ist beklemmender als eine frische Katastrophe.

**Der frühere Ausbruch weit weg:**

Das Schattenfieber ist nicht auf Schwarzrand beschränkt. Vor Jahren gab es Berichte aus anderen Regionen — Dünnstellen-Aktivität an fernen Orten, kleine Ausbrüche, die rasch unter Kontrolle kamen oder nicht weiter verfolgt wurden. Die Karawane, die Salva fast vernichtete, war einer dieser frühen Fälle. Schwarzrand ist jetzt der Epizentrum-Fall — die lokale Eskalation, die alles andere in den Schatten stellt.

---

## 3.2 Intro-Sequenz — "Was er in der Hand hielt"

### Spieler-Fantasie

*"In den ersten fünfzehn Minuten muss ich verstehen, was dieser Ort ist. Nicht durch Exposition — durch Erleben."*

### Die Szene

**Zeitpunkt:** Früher Morgen. Die Stadt Schwarzrand liegt im Nebel. Der Spieler betritt die Spielwelt zum ersten Mal.

**Der Sterbende:** Hieronymus Vael liegt am Stadtrand, zwischen zwei ausrangierten Karrengeleisen. Freier Bote, gescheitert. Schattenfieber Stadium III. Er hält eine Scherbe aus einem Material, das der Spieler noch nicht einordnen kann — unter einer bestimmten Neigung des Lichts leuchtet es biolumineszent, unheimlich schön.

**Die Übergabe-Szene (Clip-Moment):** Hieronymus sieht den Spieler. Er hat keine Kraft mehr für eine lange Erklärung. Die Szene dauert nicht länger als drei Minuten.

> *"Nimm das. Geh nicht zurück, wo du herkamst — dort kennen sie deinen Weg. Versteh das nicht als Warnung. Versteh das als das Einzige, was ich dir noch geben kann."*

Er streckt die Hand mit der Scherbe aus.

### Die Ablehn-Option

**CD-Entscheid:** Der Spieler darf das Fragment ablehnen. Das ist keine Illusion einer Wahl. Es ist eine echte Verzweigung.

**Wenn der Spieler annimmt (Standard-Pfad):**
- Das Fragment wechselt in das Inventar
- Hieronymus Vael stirbt kurz danach
- Schattenfieber-Exposition beginnt sofort: Lymph-Wert steigt minimal
- Die drei Boten erscheinen (→ Abschnitt 3.3)
- Das Spiel öffnet sich in die volle Freiheit von Schwarzrand

**Wenn der Spieler ablehnt (Alternativer Einstieg):**

Der Spieler sagt Nein. Oder sagt nichts und wendet sich ab. Hieronymus hat keine Energie für Überzeugungsarbeit. Er legt die Scherbe ins Gras, schließt die Augen.

*Sofortige Konsequenz:* Ein Fraktionsbote, der im Hintergrund wartete, nimmt die Scherbe. Der Clip-Moment passiert trotzdem — gedämpft. Das Schwellensubstrat ist bereits in der Luft, der Erde, dem Nebel.

*Kurzfristige Konsequenz (erste Stunde):* Die drei Boten behandeln den Spieler als Zeugen, nicht als Fragment-Träger. Erster Fraktionskontakt ist Verhör, kein Angebot. Brenn ist die Bote-Fraktion, die die Scherbe aufgehoben hat — sie ist im Vorteil und will trotzdem den Zeugen.

*Mittelfristige Konsequenz (Akt 1):* Der Spieler muss das Fragment aufspüren, um Zugang zum Hauptquest zu bekommen. Der Weg ist länger — er durchquert mehr von Schwarzrand, lernt mehr über die Fraktionen, bevor die Haupthandlung ihn einholt.

*Schattenfieber-Frage:* Wer das Fragment nicht nimmt, bekommt trotzdem Schattenfieber — langsamer, aus der Umgebung, ohne Ankerpunkt. Stufe I beginnt nicht in Minute fünfzehn, sondern irgendwann in der ersten Spielstunde. Unmerklich. Das ist die härtere Version.

*Langfristige Konsequenz:* Spätestens in Akt 1, Beat 3 führt jeder Pfad zur selben zentralen Frage: Was ist das Fragment? Warum ist es hier? Die Eintrittsperspektive (Träger vs. Zeuge) verändert, wie die Fraktionen den Spieler einsetzen — nicht, wohin die Geschichte führt.

**Warum diese Entscheidung richtig ist:**

Ein Spiel, das vorgibt, man könne ablehnen, es dann aber erzwingt, ist keine Immersive Sim — es ist Theater. Die Ablehn-Option muss real sein. Wenn der Spieler weiß, dass "Nein" tatsächlich Nein bedeutet, wählt er mit anderen Augen.

### Beat-Struktur der Intro-Sequenz

**Beat 1 — Ankunft:** Spieler betritt die Welt. Stadtrand. Nebel. Vael liegt da. Keine Exposition. Der Spieler sieht einen sterbenden Mann.

**Beat 2 — Die Scherbe:** Vael spricht. Kurz, erschöpft, klar. Spieler entscheidet: Nehmen oder ablehnen.

**Beat 3 — Die ersten Minuten nach Vael:** Drei Boten nähern sich — eine Uniformierte (Krone), ein ziviler junger Mann mit versiegeltem Brief (Orden), und Vreni Kast, die "zufällig" auf dem Markt ist.

**Beat 4 — Erster Fraktionskontakt:** Der Spieler spricht mit einem der drei Boten zuerst. Das ist die erste nicht-erzwungene Entscheidung. Die Welt merkt sie sich.

**Beat 5 — Schwarzrand:** Der Spieler betritt die Stadt zum ersten Mal richtig. Er sieht die vertikale Schichtung. Er hat keine Ahnung, wo er steht.

---

## 3.3 Akt 1 — Das Fragment

### Spieler-Fantasie

*"Ich verstehe gerade, was dieser Ort bedeutet — eine Stadt, die sich seit Jahren langsam verändert. Und ich bin mittendrin gelandet."*

### Erzählraum

Akt 1 ist die Exposition. Nicht durch Lore-Dumps — durch Erfahrung. Der Spieler erkundet Schwarzrand und lernt eine Stadt kennen, die den Dauerzustand der verwalteten Katastrophe normalisiert hat. Das ist keine Schockwelt — das ist eine Welt, die gelernt hat zu funktionieren, während etwas langsam falsch läuft.

**Zeitliche Länge:** Akt 1 sollte die ersten 8–12 Spielstunden umfassen. Der Spieler soll die Welt atmen, bevor der erste Kulminationspunkt kommt.

### Schlüssel-Beats Akt 1

**Die drei Fraktionskontakte:** Der Spieler lernt alle drei kennen. Das kann in beliebiger Reihenfolge geschehen. Adelhaid Brenn (Krone) will das Fragment. Ivo Scherer (Orden) will es untersuchen. Vreni Kast (Gilden) will es analysieren. Alle drei haben gute Argumente. Keines ist vollständig wahr.

**Der Verwaltungs-Alltag:** Der Spieler sieht, dass Schwarzrand das Schattenfieber nicht als Ausnahmezustand behandelt — als Alltagsrealität. Quarantäne-Protokolle, die schon Jahre laufen. Schlundtor-Kontrollen, die routine-mechanisch durchgeführt werden. Händler, die Schwellenmaterialien verkaufen, ohne dabei nervös zu werden. Diese Routine ist der erste Riss in der Fassade: die Normalität des Abnormalen.

**Die erste Fraktionsentscheidung:** Ab einem bestimmten Punkt in Akt 1 verlangt eine Fraktion eine Entscheidung — eine Aufgabe, die signalisiert, mit wem der Spieler arbeitet. Der Spieler kann sich verweigern, aber die Fraktionen werden ungeduldiger je länger er wartet.

**Salva und die vierte Perspektive:** Salva (Tiervolk) erscheint frühzeitig in Akt 1. Er ist kein Auftraggeber im Fraktionssinne — er ist ein Kontext-Lieferant. Er kennt das Muster: das Schattenfieber als langsame Eskalation, nicht als Schlag. Er kennt es, weil seine Karawane vor Jahren ein Frühwarnzeichen war. Die Information, die er über das Fragment hat, verändert nicht den Questpfad — sie verändert die Interpretation.

**Das erste Fieberflüstern:** Irgendwann in Akt 1 bemerkt der Spieler das erste Schattenfieber-Symptom. Kein Story-Trigger — organische Konsequenz des Lymph-Wert-Anstiegs. Schatten bewegen sich nicht richtig. Ein Geräusch hallt nach. Eine Sekunde. Dann ist es vorbei.

**Die Akt-1-Zeitlinie als Spieler-Lernbogen:**

Das Besondere an Akt 1 in der v2-Struktur: Der Spieler lernt die Katastrophe rückwärts. Er sieht zuerst den Istzustand (Schwarzrand, wie es ist), dann — durch NPCs, Dokumente, Gespräche — was vor fünfundzwanzig Jahren geschah, wie die Verschlechterung verlief, wer davon gewusst hat. Die Geschichte ist keine Enthüllung. Es ist Verstehen.

**Der Akt-1-Kulminationspunkt:** Jeder Fraktionspfad hat einen Akt-1-Kulminationspunkt. Beispiel Krone-Pfad: Brenn schickt den Spieler, eine Schwarzmarkt-Scherbe zu sichern, bevor die Gilden es tun. Das führt erstmals tief in den Schlund. Dort sieht der Spieler, was Brenns "kontrollierte Quarantäne" nach Jahren der Normalisierung konkret bedeutet. Das ist der Moment der Kompliziertheit.

---

## 3.4 Hauptquest — "Der Schwellenanker"

### Spieler-Fantasie

*"Ich verfolge ein Objekt und merke, dass ich mich selbst verfolge."*

### Narrative Grundfrage

**War ich immer hier, oder hat der Schwellenanker mich gerufen?**

Diese Frage wird nie direkt beantwortet. Das ist keine Schwäche der Geschichte — das ist die Geschichte.

Der Spieler kommt als Fremder. Irgendwann stellt er fest: Das Fragment reagiert auf ihn spezifisch. Der Lymph-Wert steigt schneller als bei anderen. Visions-Fragmente zeigen Orte, die er nie gesehen hat. Der Schwellenanker kennt ihn irgendwie.

### Akt-Struktur der Hauptquest

**Akt 1 — Das Fragment (parallel zu Abschnitt 3.3)**

Gameplay-Ziel: Den Ursprung des Fragments verstehen.
Narrative Frage: Was habe ich in der Hand?

Drei Fraktionen liefern jeweils eine Teilwahrheit. Salva liefert eine vierte Perspektive. Das Fragment selbst "zeigt" gelegentlich Bilder — Dünnstellen, Kammern, Tiefen. Am Ende von Akt 1 weiß der Spieler: Das Fragment ist ein Stück von etwas Größerem. Dieses Größere liegt unter Schwarzrand. Alle drei Fraktionen suchen es seit einer Generation.

**Akt 2 — Das Muster**

Gameplay-Ziel: Die anderen Fragmente finden.
Narrative Frage: Wer hat den Schwellenanker zerstört, und warum?

Das Fragment ist nicht einzigartig. In Akt 2 entdeckt der Spieler, dass der Schwellenanker in Stücke zerbrochen wurde. Die Fraktionen haben Fragmente oder wissen, wo sie sind. Akt 2 ist ein Netz aus Halbwahrheiten und verdeckten Interessen.

**Mechanische Verknüpfung:** Jedes Fragment, das der Spieler berührt, erhöht den Lymph-Wert. Wer das Muster aktiv sucht, nähert sich der Schwelle.

**Die Koalitions-Enthüllung:** In Akt 2 entdeckt der Spieler, wer die Ankerkammer geöffnet hat: eine Koalition aus allen drei Fraktionen — Orden-Gelehrter, Gilden-Expedition, Kron-Beauftragter. Jeder gibt die Schuld den anderen. Alle haben sie. Das ist der Moment, in dem keine Fraktion mehr "richtig" sein kann.

**Akt-2-Zeitlinie:** Der Spieler entdeckt, dass die Koalition nicht aus einem akuten Entscheid handelte — sondern aus einer jahrelangen Planung, die jeder der drei Parteien vernünftig erschien, bis es zu spät war. Das spiegelt die Covid-Logik auf der Täter-Seite: Es gab keinen Moment der Entscheidung für die Katastrophe. Es gab hundert kleine Entscheidungen, die sich akkumuliert haben.

**Akt-2-Kulminationspunkt:** Der Spieler findet den Weg zur Ankerkammer. Er muss entscheiden, ob er hinabsteigt. Bis hierhin war die Geschichte verhandelbar. Ab hier nicht mehr.

**Akt 3 — Die Schwelle**

Gameplay-Ziel: Den Schwellenanker wiederherstellen, zerstören oder keines von beidem.
Narrative Frage: Was tue ich mit dem, was ich weiß?

Der Spieler erreicht die Ankerkammer. Was er dort findet, hängt von seinen Entscheidungen ab — aber die Kammer selbst ist real, konsistent, und physisch präsent. In ihr: die natürliche Position des Schwellenankers. Leer, seit einer Generation. Das Schattenfieber steigt von unten wie Grundwasser.

### Die drei Hauptenden

**Ende 1 — Restauration (Krone-affin)**

Der Spieler legt alle Fragmente in die Ankerkammer zurück. Der Schwellenanker stabilisiert die Schwelle. Das Schattenfieber reckt sich nicht.

*Konsequenz:* Die Krone kontrolliert die Kammer militärisch. Das Schattenfieber wird zum Staatsgeheimnis verwaltet. Die Welt ist stabiler — und ungerechter als je zuvor. Die Logik der letzten fünfundzwanzig Jahre wird institutionalisiert. Was als temporäre Notmaßnahme begann, ist jetzt Struktur.

**Ende 2 — Destillation (Gilden-affin)**

Der Spieler übergibt die Fragmente den Gilden. Die Glasmacher-Gilde synthetisiert den Schwellenanker als Rohstoff. Die Schwelle wird nutzbar — kontrollierbar, handelbar. Das Schattenfieber eskaliert kurzfristig, stabilisiert dann durch Gilden-Chemie.

*Konsequenz:* Die Gilden monopolisieren die Schwelle als Ressource. Die Natur wird zur Ware. Das ist der konsequenteste Ausdruck des Medieval-Cyberpunk-Paradigmas. Die Kosten bleiben unten. Die Profite bleiben oben.

**Ende 3 — Öffnung (Schwellenaffin)**

Der Spieler gibt keine Fragmente ab. Er legt sie nicht zurück. Er hält sie. Und er bleibt in der Kammer.

Was passiert: Die Schwelle öffnet sich weiter. Das ist kein Weltuntergang — es ist eine Transformation. Schattenfieber-Betroffene in Stadium II und III beginnen zu verstehen, was sie sind. Etwas kommt durch. Es ist nicht nur Krankheit — es ist das, wovon das Tiervolk immer gesprochen hat: Kommunikation.

*Konsequenz:* Schwarzrand verändert sich fundamental. Ob das besser oder schlechter ist, ist unklar. Der Orden verliert die Deutungshoheit. Die Krone verliert die Kontrolle. Aber die Menschen in den untersten Schichten — die ohnehin schon tief in der Schwelle leben — werden zu etwas, das die anderen Fraktionen nicht mehr ignorieren können. Dies ist das einzige Ende, das die Frage "Kommunikation oder Krankheit?" beantwortet. Die Antwort ist: beides.

### Der Schwellenanker als mechanischer Hauptquest-Anker

- **Resonanz-Intensität:** Je höher der Lymph-Wert, desto stärker antwortet der Schwellenanker. Lore-Fragmente werden zugänglich, die nur bei Stadium I–II sichtbar sind.
- **Fragment-Auffinden:** Der Schwellenanker-Puls (Lymph-Stufe III-Vorteil) ist eine physische Empfindung im Spiel, die die Richtung anderer Fragmente anzeigt.
- **Entscheidungspunkt:** Der finale Akt-3-Entscheid ist der einzige Moment, an dem Mechanik (Lymph-Wert, Fraktionsruf, verfügbare Fragmente) direkt die zugänglichen Enden bestimmt. Ohne ausreichenden Lymph-Wert ist Ende 3 nicht erreichbar. Mit feindseligen Gilden ist Ende 2 nicht wählbar.

---

## 3.5 Fraktionsquests

### Krone-Questlinie — "Das Erste Siegel"

**Hauptkontakt:** Marschall Adelhaid Brenn
**Questlinie-Fantasie:** *"Ich habe Legitimität erkauft. Jetzt zahle ich den Preis dafür."*
**Kernspannung:** Die Krone will Ordnung. Brenn glaubt an Ordnung. Der Spieler kann daran glauben — bis er sieht, was Ordnung nach fünfundzwanzig Jahren verwalteter Katastrophe kostet.

**Quest 1 — "Passierschein"**
Brenn braucht jemanden ohne Kronstempel für einen Auftrag in der Unterstadt. Der Spieler holt Informationen über eine Schwarzmarkt-Scherbe. Einführung: Bewegungsfreiheit als Ressource, Krone als Schutzmacht.

**Quest 2 — "Quarantäne"**
Eine Unterkanal-Zone ist gesperrt. Offiziell: Routineinspektion. Tatsächlich: Schattenfieber-Ausbruch, vierzig Zivilisten, bereits siebzehn gestorben. Brenn schickt den Spieler mit einem "Bericht". Er trifft Menschen, die nicht wissen, warum sie eingesperrt sind.

*Entscheidungspunkt:* Brenns Anweisung befolgen / die Zone öffnen / die Information verkaufen (an Orden oder Gilden).

**Quest 3 — "Das Archiv"**
Brenn weiß von Kronarchiv-Akten, die das Relikt erwähnen. Sie darf sie nicht lesen. Was der Spieler findet: Die Krone kennt den Schwellenanker seit Generationen. Nicht das Fragment — das Original. Und hat nie gehandelt.

**Quest 4 — "Point of No Return"**
Brenn erfährt, was der Schwellenanker wirklich ist. Ihre sofortige Konsequenz: Das muss der Krone gehören. Sie bittet nicht. Sie verlangt. Dieser Moment definiert, ob der Spieler weiter mit der Krone geht — oder ob Brenn ab jetzt ein Hindernis ist.

---

### Gilden-Questlinie — "Der Rohstoff"

**Hauptkontakt:** Gildenmeisterin Vreni Kast
**Questlinie-Fantasie:** *"Ich baue echte Macht auf. Ich sehe, was sie kostet."*
**Kernspannung:** Die Gilden sind die ehrlichste Fraktion — sie sagen, was sie wollen. Aber Ehrlichkeit ist kein Schutz vor der Konsequenz dessen, was man tut.

**Quest 1 — "Das Angebot"**
Kast trifft den Spieler "zufällig" auf dem Markt. Sie bietet Analyse des Fragments — nicht Besitz, Analyse. Zugang zu ihrer Werkstatt. Erste Einblicke in die Gilden-Infrastruktur und die Materialsprache.

**Quest 2 — "Kanalrecht"**
Die Gerber-Gilde hat einen tiefen Kanal-Abschnitt gesperrt. Kast braucht Zugang. Der Spieler verhandelt, kauft oder erzwingt den Zugang. Einführung in die Gilden-Mikropolitik: Die Gilden sind kein Block.

**Quest 3 — "Das Destillationsarchiv"**
Der Spieler findet Kasts Kellerarchiv: Destillationsversuche ohne Überlebende. Kast: "Das waren Freiwillige. Das Schattenfieber hätte sie trotzdem getötet." Der Spieler entscheidet, wie er damit umgeht.

**Quest 4 — "Synthese"**
Kast hat genug Daten. Sie kann das Schattenfieber synthetisieren — im kleinen Maßstab. Sie braucht den Schwellenanker als finalen Datenpunkt. Das ist der Gilden-Point-of-No-Return.

---

### Orden-Questlinie — "Die Prüfung"

**Hauptkontakt:** Bruder Ivo Scherer
**Questlinie-Fantasie:** *"Ich verstehe mehr als alle anderen. Der Preis dafür wird erst später fällig."*
**Kernspannung:** Der Orden hat das tiefste Wissen. Aber Wissen ist Kontrolle — und der Orden will beides.

**Quest 1 — "Der Archivist"**
Scherer bietet Zugang zu einem Teil des Archivs. Erste Fertigkeitsbücher (Nervensystem-Leveling-Unlock). Einführung: jede Information hat einen Preis.

**Quest 2 — "Die Kopie"**
Scherer zeigt dem Spieler seinen ur-Text-Fragmentfund — und die fehlenden Stellen beschreiben genau, wie man den Schwellenanker zerstört. Ob das Auslassung oder Vergessen war, bleibt offen. Scherer: "Ich weiß es nicht mehr."

**Quest 3 — "Deutungshoheit"**
Ein Priester im unteren Orden-Rang predigt eine Abweichler-Version des Schöpfungsmythos — näher an der biologischen Wahrheit als der offizielle Orden. Scherer schickt den Spieler, ihn zum Schweigen zu bringen. Viele Formen möglich. Die erste offene Konfrontation mit dem Widerspruch zwischen Ordenslehre und Realität.

**Quest 4 — "Der Hochritus"**
Scherer bietet Zugang zum Hochritus: ein Ritual, das Schattenfieber-Stadium III stabilisieren kann. Dafür braucht der Orden den Schwellenanker. Der Spieler entscheidet, ob er zahlt — und womit.

---

## 3.6 Nebenquests

### "Der Zeuge"

**Typ:** Character-Quest
**NPC:** Benedikt Haas, alter Tunnel-Arbeiter, Schlund

**Spieler-Fantasie:** *"Ich erfahre, was wirklich passiert ist — von jemandem, der dabei war."*

Haas war bei der Gilden-Expedition, die die Ankerkammer öffnete. Er lebt im Schlund, isoliert, paranoid. Er ist der einzige Mensch in Schwarzrand, der alle drei Fraktionsvertreter der Koalitionsnacht erkannt hat.

**Quest-Struktur:** Spieler findet Haas über Salvas Hinweisnetz. Haas testet zuerst: Beweise, dass du für niemanden aus der Fraktionskoalition arbeitest. Das ist schwer, wenn man gerade genau das tut. Wenn Haas vertraut: Er beschreibt die Nacht der Öffnung. Damals sahen die Beteiligten ihr Handeln als vernünftig — jede Partei glaubte, die Situation zu kontrollieren. Niemand konnte es. Das ist der Kern des Zeugenberichts.

**Belohnung:** Ein zerbrochenes Siegel mit allen drei Fraktionszeichen — der Beweis für die Koalition.

---

### "Die Weber-Gilde und das, was leuchtet"

**Typ:** Gilden-Seitenquest, Crafting-orientiert
**NPC:** Weberin Greth Saal, Mittelrang Weber-Gilde

**Spieler-Fantasie:** *"Ich verstehe, wie Macht durch Material fließt."*

Greth webt Schwellenfäden in Textilien. Begehrt von der Oberschicht. Giftig für die Weber, die sie verarbeiten. Sie braucht jemanden, der eine Ladung Fäden direkt aus dem Schlund beschafft — ohne Gerber-Gilde-Zoll.

**Quest-Struktur:** Spieler beschafft die Fäden im Schlund. Dabei: die Weber, die in diesem Bereich arbeiten, leben alle in frühem Stadium II. Die Gilde weiß das. Das ist der Preis, den Greth nicht ausspricht. Entscheidungspunkt: Liefern (Gilden-Ruf +), behalten und anderweitig verkaufen, oder die Information weitergeben.

**Belohnung:** Zugang zu einer Weber-Gilde-Werkstatt und Rezepturen für biolumineszente Textilien (Crafting-Klasse III–IV).

---

### "Salvatore und die Karawane"

**Typ:** Tiervolk-Seitenquest, Lore-Quest
**NPC:** Salva

**Spieler-Fantasie:** *"Ich erfahre, was Salva wirklich ist — und was die Zeitlinie der Öffnung wirklich bedeutet."*

Salva verschwindet für eine Spielperiode. Wenn er zurückkommt, ist er verändert. Was er gefunden hat: den Ursprungsort der Karawane, die vor Jahren verschwand — mit einem Objekt, das dem Schwellenanker ähnelte. Das war einer der frühen Ausbrüche weit weg, Jahre bevor Schwarzrand zum Epizentrum wurde. Salva war das einzige Überlebende. Er ist kein Mensch mehr im biologischen Ursprungssinn. Er ist etwas dazwischen — und er weiß, was das bedeutet.

**Quest-Struktur:** Spieler kauft die Information über den Karawanenursprungsort (hoher Preis). Ein verfallenes Handelsposten außerhalb von Schwarzrand. Salva begleitet optional. Am Posten: Die Karawane hat sich von innen aufgelöst. Das Fragment war der Auslöser. Das war kein Unfall — das war ein Frühwarnzeichen, das niemand ernst genommen hat.

**Belohnung:** Ein weiteres Fragment (Hauptquest-Fortschritt) + Salvas vollständiges Vertrauen (Zugang zu seinen tiefsten Informationen).

---

## 3.7 Erzählerische Prinzipien

### Das epistemische Prinzip

Kein NPC im Spiel kennt die vollständige Wahrheit über den Schwellenanker. Der Spieler auch nicht. Die Geschichte ist ein Puzzle aus Halbwahrheiten. Die "Wahrheit" des Endes hängt davon ab, welche Quellen der Spieler befragt und welchen er geglaubt hat.

Das ist keine versteckte Exposition. Es ist eine strukturelle Entscheidung: In einer Welt, in der drei Fraktionen aktiv konkurrierende Wahrheiten produzieren und alle drei zur selben Katastrophe beigetragen haben, kann kein Protagonist vollständige Wahrheit besitzen.

### Unreliable Memory

Ab Schattenfieber-Stadium II werden Erinnerungen fragmentarisch. Das Spiel zeigt gelegentlich Szenen anders als beim ersten Erleben — ein Satz, den Hieronymus Vael sagte, klingt plötzlich anders. Das ist keine Continuity-Fehler — es ist mechanikvermittelte Erfahrung des Kontrollverlusts.

### Die Zeitlinie als Erzählschicht

Die Covid-Analogie ist kein Gimmick — sie ist das Erzählgerüst für alle drei Akte:
- **Akt 1:** Der Spieler versteht den Istzustand. Er lernt, dass das Abnormale normal geworden ist.
- **Akt 2:** Der Spieler versteht den Prozess. Er sieht, wie die Normalisierung ablief — Entscheidung für Entscheidung, über Jahre.
- **Akt 3:** Der Spieler entscheidet, ob er diese Normalisierung fortsetzt, ändert, oder bricht.

Das ist die moralische Architektur des Spiels. Nicht: Gut oder Böse. Sondern: Weitermachen oder aufhören.

### Die Erzählgeschwindigkeit

Akt 1: Langsam. Der Spieler soll Schwarzrand kennenlernen, bevor die Geschichte eskaliert.
Akt 2: Mittel. Informationsdichte steigt. Fraktionskonflikte spitzen sich zu.
Akt 3: Hoch. Alles läuft auf die Ankerkammer zu. Keine Zeit mehr für Ausweichen.

Die Spieler-Fantasie der ersten Stunde (Fremder betritt Sandbox) darf nicht gebrochen werden. Akt 1 muss diese Fantasie leben lassen.

---

![Schwarzrand: Vertikale Stadtschichtung](../gallery/concepts/day02-vera/environments/stadtschnitt-vertikale-schichtung_nano-banana-pro.png)

*Konzeptbild: Stadtschnitt Schwarzrand — die drei vertikalen Schichten (Obere Ränder / Mittelwand / Schlund) bilden den Schauplatz aller drei Akte.*

<!-- Darius: v2 vollständig. Zeitlinie der Öffnung als langjährige Anbahnung (Covid-Analogie) durch alle Akte eingewoben. Akt 1 trägt die Logik: Spieler betritt keine Akutkatastrophe, sondern eine Gesellschaft im verwalteten Dauerzustand. Tiervolk-Quest ("Salvatore und die Karawane") aktualisiert: Karawane war ein Frühwarnzeichen der jahrelangen Anbahnung. Autorenvermerke und Nami-Platzhalter bereinigt. -->

\clearpage

# GDD Kapitel 04 — Schlüsselfiguren & NPCs

<!-- Version 3 — Tag 4, Donnerstag -->
<!-- Änderungen gegenüber v2: Salva vollständig neu (Symbiose-Kosmologie), Intro-Beat-1 überarbeitet (schleichendes Erkennen statt akute Krise), Cleanup (Autorenerwähnungen raus, Wolf-Checklisten raus), Arbeitshypothese Salva↔Schattenfieber eingebaut -->

---

## Strukturprinzip

Figuren werden nicht von innen nach außen beschrieben. Die Stimme kommt zuerst, dann die Funktion. Ein NPC ohne eigene Stimme hat kein Recht auf Existenz im Spiel.

Jede Figur wird beschrieben nach:

1. **Wer sie ist** — in drei Sätzen, kein Infodump
2. **Was sie vom Fremden will** — explizit und versteckt
3. **Was sie nie zugeben würde** — die Risse in der Fassade
4. **Ihre Stimme** — ein Muster, eine Eigenheit, ein charakteristischer Satz
5. **Spielerrelevanz** — Quest-Anker, Reaktion auf Fraktionswahl, Schattenfieber-Verhältnis
6. **Dramatischer Wendepunkt** — der Moment, in dem die Figur kompliziert wird

---

## 4.1 Der Fremde — Spielercharakter

*Kein vollständiger NPC-Eintrag, da spielergesteuert. Aber die Leerstelle muss benannt werden.*

Der Fremde ist kein Held. Er ist eine **Frage in Menschengestalt.**

Er kommt von woanders — woher, das wählt der Spieler bei der Charaktererstellung, und es beeinflusst, wie die Welt auf ihn reagiert, aber nicht, was er "ist." Er hat einen Namen, den wir nie aussprechen. Er hat eine Vergangenheit, die wir in Dialogoptionen andeuten, aber nie erzählen. Er ist **Blank Slate mit Textur** — kein leeres Blatt, sondern ein Blatt, das schon beschrieben war und abgewischt wurde.

**Das epistemische Prinzip:** Der Fremde lernt die Welt durch Missverständnisse. Ein Gildenmeister, der ihm die Hand schüttelt, hat gerade eine Verpflichtung eingefordert — der Fremde weiß das nicht, noch nicht. Ein Ordensbote, der "ehrenwert" sagt, meint "gebunden." Die Krone bittet nicht — sie erwartet. Der Spieler lernt das langsam. Zu langsam, manchmal.

**Schattenfieber-Status:** Stufe 1 (Rauschen) ab Minute fünfzehn des Spiels. Nach dem Fragment. Das Rauschen gehört zum Charakter — er soll es erst sehr viel später als Symptom erkennen, wenn überhaupt.

**Visuelle Leitlinie:** Keine definierte Silhouette. Keine festgelegte Körperhaltung. Die Ausrüstung zu Beginn ist Unterschicht — Eisen, ungefärbtes Leinen, aufgearbeitetes Leder. Das wird sich verändern, aber das erste Bild muss das sein.

---

## 4.2 Der Sterbende — Intro-NPC

**In-World-Name:** Hieronymus Vael
**Funktion:** Intro-Sequenz, Quest-Auslöser, erster Schattenfieber-Spiegel

### Wer er ist

Hieronymus Vael war Bote. Nicht Krone, nicht Orden, nicht Gilden — er war **freier Bote**, einer der wenigen, die zwischen allen Lagern liefen, weil alle Lager solche Leute brauchen. Er wusste zu viel von zu vielen. Und er hat etwas transportiert, das er nicht hätte transportieren sollen: die Scherbe des Schwellenankers. Jetzt stirbt er daran.

Er ist ca. fünfzig Jahre alt, sieht achtzig aus. Die Haut an seinen Händen ist dünn geworden wie Papier, darunter laufen Muster, die aussehen wie tinte-eingeschriebene Adern, aber dunkler. Er riecht nach Erde. Sein Atem geht in kurzen Stößen.

Er liegt am Stadtrand, im Gras zwischen zwei ausrangierten Karrengeleisen. Es ist früher Morgen. Nebel. Er hat sich hierhin geschleppt, weil er wusste: die Stadt war nicht sicher. Nicht mit dem, was er trägt.

### Der schleichende Beginn — Covid-Analogie

Hieronymus Vael ist nicht heute Nacht krank geworden.

Das ist der erste und wichtigste Unterschied zu dem, was der Spieler instinktiv erwartet. Vael zeigt seit Monaten Symptome — zunächst das Flimmern an den Rändern des Sichtfelds, dann der veränderte Geruchssinn, dann die langsam dunkler werdenden Adern an den Schläfen. Die Stadtbevölkerung kennt diese Progression. Sie haben sie bei anderen gesehen. Es gibt keinen Moment, in dem jemand sagt: *"Das Schattenfieber ist ausgebrochen."* Es gibt nur den Moment, in dem jemand sagt: *"Er sieht schlimmer aus als letzte Woche."*

Für den Fremden ist das die erste Lektion über Schwarzrand: Die Bedrohung kündigt sich an. Die Menschen haben gelernt, die Ankündigung zu ignorieren, weil sie nicht aufhören wollen zu leben.

Vael liegt nicht hier, weil er heute Nacht kollabiert ist. Er liegt hier, weil er noch einen letzten Auftrag hatte, der ihn außerhalb der Stadt führte, und nicht mehr die Kraft aufgebracht hat zurückzukehren. Er ist einfach stehengeblieben. Irgendwann. Und dann hat das Gras ihn aufgenommen.

### Was er vom Fremden will

Explizit: Dass der Fremde die Scherbe nimmt. Dass jemand anderes weiterlebt, wenn er nicht mehr kann.

Versteckt: Absolution. Hieronymus hat jemandem vertraut, dem er nicht hätte vertrauen dürfen. Das Stück Schwellenanker war ein Auftrag — bezahlt, legal, professionell. Aber er hat die Fragen nicht gestellt, die er hätte stellen sollen. Er stirbt nicht nur an der Scherbe. Er stirbt an seiner eigenen Bequemlichkeit. Der Fremde ist nicht sein Retter. Er ist Hieronymus' letzter Zeuge.

### Was er nie zugeben würde

Dass er weiß, wer den Auftrag gegeben hat. Er weiß es. Er sagt es nicht, weil er Angst hat, dass dieses Wissen den Fremden umbringt, bevor er überhaupt angefangen hat. Vielleicht. Oder weil er sich schämt.

### Seine Stimme

Hieronymus spricht in kurzen Sätzen. Er hat keine Energie für lange Erklärungen. Aber er ist kein Rätsel-NPC — er versucht zu erklären, scheitert aber an Zeit und Atem. Die Lücken in seinem Sprechen sind keine Absicht, sondern Erschöpfung.

**Charakteristischer Satz:**

> "Nimm das. Geh nicht zurück, wo du herkamst — dort kennen sie deinen Weg. Versteh das nicht als Warnung. Versteh das als das Einzige, was ich dir noch geben kann."

Er sagt "Versteh das" zweimal. Das ist sein Muster — er hat sein Leben damit verbracht, sicherzugehen, dass Botschaften ankommen. Auch jetzt noch.

### Spielerrelevanz

Die Fragment-Übergabe — die Scherbe des Schwellenankers — ist der **Clip-Moment**. Sie muss in den ersten fünfzehn Minuten passieren.

Kurz danach erscheinen die drei Fraktionsboten. Dass der Fremde die Scherbe hat, ist entweder schon bekannt — oder wird innerhalb von Minuten bekannt. Das ist die erste narrative Frage: Wie?

Der Spieler kann Hieronymus nach seinem Tod durchsuchen. Er findet wenig: ein zerrissenes Pergamentstück mit drei Siegeln (Krone, Orden, Gilden — alle drei, was unmöglich sein sollte). Das ist eine Spur, die erst viel später aufgelöst wird.

**Unreliable-Narrator-Moment:** In Stufe 2 (Risse) erinnert sich der Spieler an die Begegnung mit Hieronymus. Was er "erinnert," stimmt nicht exakt mit dem überein, was passiert ist. Kleiner Unterschied — Hieronymus hat etwas gesagt oder nicht gesagt. Der Spieler weiß nicht, welche Version wahr ist.

### Dramatischer Wendepunkt

Hieronymus stirbt in den ersten zwanzig Minuten. Aber: Wenn der Spieler im späteren Spielverlauf herausfindet, wer den Auftrag gegeben hat, verändert das die Erinnerung an diesen ersten Moment. Hieronymus wird rückwirkend komplizierter. Das ist sein Wendepunkt — post-mortem.

---

## 4.3 Die Ablehn-Option — Wenn der Spieler das Fragment verweigert

Dies ist kein Nebenpfad. Es ist eine vollwertige Möglichkeit mit eigener narrativer Logik.

### Was passiert

Hieronymus hält die Scherbe des Schwellenankers aus. Sein letzter Atemzug ist fast aufgebraucht. Der Spieler hat eine Dialogoption: **Das Fragment nicht nehmen.**

Wenn der Spieler ablehnt, sagt der Fremde nichts oder etwas Kurzes — "Das gehört mir nicht" oder Schweigen, je nach Spielervariante. Hieronymus versteht es. Er legt die Scherbe ins Gras neben sich. Er stirbt. Die Scherbe liegt da.

Zwanzig Sekunden vergehen. Der Spieler steht daneben. Die Schatten verhalten sich falsch für einen Moment — aber es passiert dem Spieler nicht, weil er das Fragment nicht berührt hat. Es passiert trotzdem. Das Schwellensubstrat ist schon in der Luft, in der Erde, im Nebel. Der Clip-Moment ist leiser, aber er ist da.

Dann erscheint eine Gestalt. Einer der drei Fraktionsboten — nicht der, der offiziell geschickt wurde, sondern ein Zweiter, der im Hintergrund gewartet hat. Er nimmt die Scherbe. Er geht. Der Spieler hat jetzt kein Fragment und einen Toten und drei Fraktionsboten, die auf ihn warten.

### Konsequenzen

**Sofort:** Der Spieler beginnt das Spiel ohne die Scherbe. Er ist kein Fragment-Träger — er ist Zeuge. Das verändert, wie die Fraktionen ihn einschätzen: nicht als Gefahr, sondern als Ressource. Als jemanden, der weiß, wo die Scherbe zuletzt war.

**Kurzfristig:** Die drei Boten behandeln den Spieler anders. Er wird nicht umworben — er wird befragt. Das erste Fraktionsgespräch ist kein Angebot, sondern ein Verhör. Jede Fraktion will wissen, was er gesehen hat.

**Mittelfristig:** Der Spieler muss das Fragment aufspüren, um Zugang zum Hauptquest zu bekommen. Der Weg ist länger. Er durchquert mehr der Stadt, bevor der erste Act beginnt. Das ist eine vertiefte Tutorial-Phase — er sieht mehr von Schwarzrand, lernt mehr über die Fraktionen, bevor die Haupthandlung ihn einholt.

**Die Schattenfieber-Frage:** Wer das Fragment nicht nimmt, bekommt trotzdem Schattenfieber. Langsamer. Aus der Umgebung, nicht aus dem direkten Kontakt. Stufe 1 beginnt nicht in Minute fünfzehn, sondern irgendwann in der ersten Spielstunde — unmerklich, ohne Clip-Moment, ohne Ankerpunkt. Der Spieler erkennt es nicht als Moment. Das ist die härtere Version.

### Emotionale Signatur

Die Ablehn-Option verändert die moralische Grundmelodie des Spielbeginns. Der Standard-Pfad sagt: *Ich wurde in etwas hineingezogen.* Die Ablehn-Option sagt: *Ich habe mich entschieden, mich nicht einzumischen — und bin trotzdem drin.*

Das ist kein Gewissen. Das ist Konsequenz. Das Spiel wertet nicht. Weder Pfad ist besser oder schlechter. Aber die emotionale Textur ist verschieden, und die Figuren, die der Spieler im ersten Act trifft, spiegeln das wider.

Hieronymus Vael stirbt auf beiden Pfaden. Auf dem Standard-Pfad ist der Fremde sein letzter Empfänger. Auf dem Ablehn-Pfad ist er sein letzter Zeuge — was in mancher Hinsicht das Schwerere ist.

---

## 4.4 Fraktionsvertreter — Schlüssel-NPCs

*Je ein Hauptkontakt pro Fraktion. Kein Gut/Böse. Jede Figur hat einen sympathischen Einstiegspunkt und einen Moment der Kompliziertheit.*

---

### 4.4.1 Krone — Marschall Adelhaid Brenn

**Funktion:** Erster Kontakt zur Krone, Militärbehörde, potenzielle Auftraggeberin in Act 1

#### Wer sie ist

Adelhaid Brenn ist fünfundvierzig. Sie hat dreiundzwanzig Jahre in der Kronarmee gedient, davon acht als Marschall der Stadtgarnison. Sie trägt Tiegelstahl-Rüstung, gebürstet, ohne Verzierung — nicht aus Bescheidenheit, sondern weil Verzierungen im Nahkampf Angriffspunkte sind. Sie ist die Person, die den Schwellenanker als erste offiziell zur Kenntnis nimmt: Sie kennt den Namen Hieronymus Vael, und sie wollte ihn vor drei Tagen befragen.

Sie ist kein Schurke. Sie ist jemand, der Ordnung aufrechterhalten hat, weil Ordnung das Einzige ist, das die Schwächsten schützt. Wenn die Krone fällt, fallen zuerst die Menschen in den untersten Stadtschichten. Das glaubt sie. Das hat sie gesehen.

#### Was sie vom Fremden will

Explizit: Die Scherbe des Schwellenankers. Wenn sie den Fremden nicht überzeugen kann, sie freiwillig abzugeben, dann zumindest seine Zusammenarbeit.

Versteckt: Einen Vorwand, um das Schattenfieber-Problem zu lösen, ohne dass ihre Vorgesetzten wissen, dass es ein Problem gibt. Die Garnison verliert Soldaten — Schattenfieber-Exposition in den Unterkanal-Bereichen der Stadt. Sie hat es bisher nicht gemeldet, weil ein offizieller Bericht eine Quarantäne bedeuten würde, und eine Quarantäne bedeutet, dass die Kaufleute der Gilden sich beschweren, und dann greift der Gildenrat ein, und dann hat sie plötzlich Gilden-Aufseher in ihrer Kaserne. Das will sie nicht.

#### Was sie nie zugeben würde

Dass die Krone — nicht nur lokale Garnison, sondern die Kronbehörde selbst — den Schwellenanker seit Jahren kennt. Nicht das Fragment. Das Original. Und dass sie aus dieser Kenntnis nie eine Pflicht abgeleitet hat, die ihr unbequem gewesen wäre. Sie weiß nicht, was der Schwellenanker *ist* — aber sie weiß, dass Akten darüber existieren, die sie nicht lesen durfte.

#### Ihre Stimme

Brenn spricht direkt und ohne Umwege. Sie sagt nie "vielleicht," sie sagt "es wäre denkbar." Sie sagt nie "ich weiß nicht," sie sagt "das ist noch nicht ermittelt." Bürokratische Sprache als Selbstschutz, nicht als Täuschung. Sie ist kein Lügner — sie ist jemand, dem Präzision wichtiger ist als Ehrlichkeit.

Sie fragt viele Gegenfragen. Nicht als Verhörtaktik, sondern weil sie keine Entscheidung trifft, die sie nicht vollständig versteht.

**Charakteristischer Satz:**

> "Ich bitte Sie nicht, mir zu vertrauen. Das wäre unvernünftig. Ich bitte Sie, die Konsequenzen der Alternative zu verstehen."

#### Spielerrelevanz

**Boten-Szene:** Brenns Bote erscheint als einer der drei Boten nach Hieronymus' Tod. Er ist höflich, uniformiert, unauffällig — und hartnäckig.

**Fraktions-Aufnahme:** Der Spieler kann sich Brenn und der Krone anschließen. Sie bietet Unterkunft in der Kaserne, Zugang zu Kronpassagen, und Ausrüstung aus Kronbeständen.

**Schattenfieber-Reaktion der Krone:** Unterdrückung. Das Schattenfieber ist ein militärisches Problem. Man löst es wie ein militärisches Problem. Schweigen, Eindämmen, Kontrollieren.

**Moral-Komplikation:** Im mittleren Spielverlauf stellt der Spieler fest, dass Brenn einen Unterkanal-Bereich hat sperren lassen — mit Menschen drin. Schattenfieber-Exposition. Sie nennt es "kontrollierte Quarantäne." Es sind vierzig Menschen. Siebzehn sind gestorben.

**Ablehn-Option-Variante:** Wenn der Spieler das Fragment nicht genommen hat, ist Brenns Bote der, der es aufhebt. Das macht Brenn zur frühen Besitzerin der Scherbe — sie ist im Vorteil, will aber noch immer den Zeugen. Der erste Kontakt ist ein Verhör, kein Angebot.

#### Dramatischer Wendepunkt

Brenn erfährt, was der Schwellenanker wirklich ist — ein Schwellen-Stabilisator, der die Grenze im Gleichgewicht hält. Wenn sie das versteht, zieht sie sofort die politische Konsequenz: Wenn der Schwellenanker die Schwelle stabilisiert, und die Schwelle ist das, was das Schattenfieber kontrolliert, dann ist der Schwellenanker eine Waffe. Eine, die die Krone besitzen muss. Nicht aus Bosheit. Aus militärischer Logik. Das ist der Moment, in dem sie aufhört, eine Verbündete zu sein und anfängt, ein Hindernis zu werden — ohne dass sie sich verändert hat.

---

### 4.4.2 Orden — Bruder Ivo Scherer

**Funktion:** Erster Kontakt zum Orden, Deutungs-Instanz, Informationsbroker (mit Preis)

#### Wer er ist

Ivo Scherer ist zweiunddreißig. Er sieht jünger aus und weiß das — er nutzt es. Er ist kein hoher Ordensmann, er ist Mittelrang: ein Forschungsbruder mit Archivzugang und genug Bildung, um gefährlich zu sein, aber zu wenig hierarchischen Status, um unangreifbar zu sein. Das macht ihn interessant. Er ist klug genug, den Machtspielern im Orden zu helfen, ohne je selbst einer zu werden. Das nennt er Demut. Es ist Selbstschutz.

Er trägt schwarze Ordensgewänder mit einem einzelnen indigofarbenen Ordenssiegel. Die Hände sind tintenbeschmiert. Er lächelt oft — aber das Lächeln erreicht die Augen nur, wenn er etwas Interessantes hört.

#### Was er vom Fremden will

Explizit: Das Fragment zu untersuchen. Nicht zu besitzen — er ist clever genug, diese Formulierung zu wählen. Er will Zugang, nicht Kontrolle. Vorerst.

Versteckt: Wissen, das er monopolisieren kann. Der Orden hat ein Bildungsmonopol, aber das Bildungsmonopol funktioniert nur, solange der Orden weiß, was andere nicht wissen. Ein Schwellenanker-Fragment, das auftaucht und kursiert? Das ist eine Wissenslücke. Lücken machen ihn nervös.

#### Was er nie zugeben würde

Dass er einen Ur-Text über den Schwellenanker gesehen hat. Fragmentarisch, unvollständig — aber er hat ihn gesehen, vor drei Jahren, in den Archivuntergeschossen, und er hat ihn nicht gemeldet. Er hat ihn kopiert. Die Kopie liegt in seinem Quartier. Er weiß, dass der Orden das als Häresie behandeln würde, nicht weil der Text ketzerisch ist, sondern weil nicht-gemeldete Archivauffunde Amtsverluste bedeuten.

#### Seine Stimme

Scherer spricht in langen, präzisen Sätzen mit Zwischensätzen, die immer etwas sagen, das er direkt nicht sagen möchte. Er stellt Fragen, die Aussagen sind. Er wiederholt Formulierungen des Gesprächspartners, leicht verändert — "Sie sagten, er drückte Ihnen etwas in die Hand. *Drückte.* Das ist ein Wort mit Druck dahinter."

**Charakteristischer Satz:**

> "Was Sie da beschreiben, ist entweder sehr gefährlich oder sehr wichtig. In meiner Erfahrung ist es meistens beides. Ich frage mich, ob Sie den Unterschied erkennen, wann die eine Eigenschaft in die andere kippt."

#### Spielerrelevanz

**Boten-Szene:** Scherers Kontaktmann — kein uniformierter Bote, ein zivil gekleideter junger Mann, der aussieht wie ein Kaufmannslehrling — spricht den Fremden unauffällig an. Er übergibt ein versiegeltes Briefchen mit einer Adresse.

**Fraktions-Aufnahme:** Der Orden bietet Zugang zum Archiv (Fertigkeitsbücher, Upgrade-Pfade), Unterkunft in einem Ordenshaus, und Scherers persönliche Deutungsleistung.

**Schattenfieber-Reaktion des Ordens:** Deutungshoheit. Der Orden sagt nicht, was das Schattenfieber *ist* — er sagt, was es *bedeutet*. Das ist eine Theologie-Aussage, keine Medizin-Aussage. Wer nicht unter Ordensdeutungshoheit lebt, ist ungeschützt.

**Informationsbroker-Mechanik:** Scherer ist der NPC, über den der Spieler am meisten über die Weltgeschichte erfährt. Aber jede Information hat einen Preis — nicht notwendigerweise Geld. Manchmal eine Gunst.

#### Dramatischer Wendepunkt

Scherer zeigt dem Spieler (unter bestimmten Bedingungen) seinen Ur-Text-Fragmentfund. Das ist sein letztes Vertrauens-Kapital. Aber: Der Spieler kann in diesem Moment sehen, dass die Kopie unvollständig ist — und dass die fehlenden Stellen genau das sind, was erklärt, wie man den Schwellenanker *zerstört.* Scherer hat das nicht kopiert. Vielleicht aus Vergessen. Vielleicht nicht.

---

### 4.4.3 Gilden — Gildenmeisterin Vreni Kast

**Funktion:** Erster Kontakt zu den Gilden, Wirtschaftsmacht, Vermittlerin und Händlerin

#### Wer sie ist

Vreni Kast ist zweiundfünfzig. Sie ist Meisterin der Glasmacher-Gilde — optische Instrumente, Alchemie-Phiolen, Bergkristall-Linsen. Das ist nicht die größte Gilde, aber es ist eine der technologisch avanciertesten. Glasmacher sehen, was andere nicht sehen — buchstäblich und im übertragenen Sinn. Sie ist kurz, unscheinbar, trägt immer eine Lupe an einer Kette. Ihre Hände sind vernarbt von Jahrzehnten an Werkbänken.

Sie hat aus einer Handwerkerfamilie ohne Gildenstatus in den Gildenrat aufgestiegen. Das war nicht Glück. Das war dreißig Jahre kalkuliertes Handeln.

#### Was sie vom Fremden will

Explizit: Das Fragment analysieren. Sie formuliert es als Angebot — Dienstleistungen und Information im Tausch für Zugang. Kein Besitz. Analyse.

Versteckt: Zu verstehen, was der Schwellenanker von sich abstrahlt. Scherers Orden hat Deutungshoheit über das Nicht-Messbare. Die Gilden wollen das Messbare — und wenn etwas mit dem Fragment passiert, das messbar ist, will Kast das erste Messinstrument sein, das es misst.

#### Was sie nie zugeben würde

Dass die Glasmacher-Gilde bereits seit zwei Generationen versucht, das Schattenfieber zu synthetisieren. Nicht heilen — synthetisieren. Als Rohstoff. Die Experimente haben keine Überlebenden hinterlassen. Die Überreste liegen im untersten Kellergeschoss des Gildenhauses. Sie nennt es intern "das Destillationsarchiv." Es riecht dort nach verbranntem Haar und etwas Süßlichem.

#### Ihre Stimme

Kast redet schnell, präzise, und lässt dem Gesprächspartner keine Zeit zum Innehalten. Sie gibt viele Informationen, bevor der andere eine Frage stellen kann — das ist keine Offenheit, das ist Überflutung. Wen sie mag, gibt sie Spitznamen. Wen sie nicht mag, nennt sie "Kollege."

Sie macht sich selten Sorgen. Wenn sie sich doch Sorgen macht, beginnt sie Sätze mit "Das ist interessant" — was das Gegenteil von dem ist, was sie meint.

**Charakteristischer Satz:**

> "Sie halten das gerade in der Hand und wissen nicht, was es ist. Das ist die unangenehmste Position, in der man sich befinden kann — wertvolles Unwissen. Ich kann das ändern. Nicht umsonst, natürlich. Aber ich glaube, wir werden uns einig."

#### Spielerrelevanz

**Boten-Szene:** Kast schickt keinen Boten. Sie wartet. Sie weiß, dass der Fremde in die Unterstadt muss — und dort kontrollieren die Gilden die Märkte. Der erste Kontakt ist zufällig inszeniert, aber nicht zufällig.

**Fraktions-Aufnahme:** Die Gilden bieten Zugang zu Materialien (bessere Ausrüstung, Alchemie-Rezepturen), ein Handelsnetz das Informationen liefert, und Geld. Direkter als Krone und Orden.

**Schattenfieber-Reaktion der Gilden:** Verwertung. Das Schattenfieber ist kein Feind — es ist ein unkontrolliertes Potenzial. Die Gilden wollen es kontrollierbar machen.

**Handels-Mechanik:** Vreni Kast ist der NPC, über den Spieler Zugang zu Nicht-Standard-Ausrüstung bekommen. Viele ihrer besten Angebote sind mit Bedingungen verknüpft, die erst später relevant werden.

#### Dramatischer Wendepunkt

Der Spieler entdeckt das Destillationsarchiv. Das ist Kasts Point of No Return — nicht für die Spielfigur, sondern für den Spieler: Er muss entscheiden, ob das, was er über Kast weiß, ändert, was er bereit ist, mit ihr zu tun. Kast selbst verteidigt das Archiv nicht moralisch. Sie sagt: "Das waren Freiwillige. Das Schattenfieber hätte sie trotzdem getötet." Das kann wahr sein. Das ändert nichts daran, was das Archiv ist.

---

## 4.5 Die Reisenden — Salva

**Funktion:** Informationsbroker, Verbindung zur Unterstadt und zu Netzwerken außerhalb der Fraktionen, vierte Kosmologie

<!-- Tiervolk-Eigenname für Salva: noch Platzhalter — Namenssystem-Input von Emre ausstehend -->
<!-- Arbeitshypothese Salva↔Schattenfieber eingebaut — Emre muss das kosmologisch bestätigen oder korrigieren -->

### Was das Tiervolk wirklich ist — Kosmologische Grundlage

"Tiervolk" ist ein Stadtbegriff. Abwertend, ungenau, und falsch in der Grundannahme: Es beschreibt keine ethnische Gruppe, keine biologisch angepasste Population. Es beschreibt etwas grundlegend Anderes.

Die Wesen, die man als "Tiervolk" bezeichnet, sind **kosmologisch fremde Entitäten in dauerhafter, irreversibler Symbiose mit einem Tier der Stoffwelt.** Das fremde Wesen — was es vor der Symbiose ist, woher es kommt, ob es in der Schwelle existierte oder aus einer dritten Ebene stammt, ist ungeklärt — hat sich mit einem Tier als Anker in der Materie verbunden. Das Tier ist der Materialanker: Es gibt dem Fremden einen Körper, eine Form, eine Verwurzelung in der Stoffwelt. Das Fremde gibt dem Tier ein Bewusstsein, das über Tierinstinkt hinausgeht — aber auch über menschliche Kategorien.

Die Symbiose ist nicht Fusion. Die beiden Teile bleiben unterscheidbar — aber untrennbar. Wer versucht, die Symbiose zu trennen, tötet beide. Kein Orden-Experiment, kein Gildenmittel hat je eine Trennung überlebt. Die Symbiose ist so dauerhaft wie eine Narbe: Sie verändert die Form und lässt sich nicht rückgängig machen.

Das Ergebnis ist kein Mensch mit Tiermerkmalen. Es ist ein Wesen, das eine eigene ontologische Kategorie besetzt — zwischen Stoff und Kosmologischem, zwischen Tier und etwas, für das die Stadtsprache kein Wort hat.

Sie nennen sich intern "die Reisenden." Das Wort Tiervolk benutzen sie für sich selbst nicht. Wer es ihnen gegenüber benutzt, bekommt höflich einen doppelten Preis.

### Wer Salva ist

Salva trägt einen Habicht.

Nicht in der Hand, nicht auf der Schulter — im Körper. Das ist die ungenaueste und gleichzeitig präziseste Art, es zu formulieren. Der Habicht war einmal ein Habicht. Er hat sich verändert. Er lebt noch — daran besteht kein Zweifel — aber er lebt in Salva und Salva lebt in ihm, und die Grenze zwischen beiden ist so durchlässig geworden, dass Salvas Pupillen sich bei Gefahr weiten wie die eines Raubvogels, seine Hörwahrnehmung in einem Frequenzband liegt, das Menschen nicht erreichen, und seine Orientierung im Raum — im Dunkeln, in engen Gassen, im Gewirr des Schlunds — so präzise ist, dass die Schlundbewohner sagen, er sehe mit Augen, die nicht in seinem Gesicht sitzen.

Salva ist zwischen dreißig und fünfzig — das ist schwer zu sagen, und er gibt keine Auskunft darüber. Er ist Informationsbroker und Kontaktvermittler. Er hat keine Gilde-Mitgliedschaft, keine Kronen-Akkreditierung, keinen Ordensstatus. Er hat ein Netz aus Kontakten, das alle drei Fraktionen umspannt — ohne dass irgendjemand von den anderen weiß, dass er auch für sie arbeitet.

**Körperliche Erscheinung:** Salva sieht auf den ersten Blick unremarkabel aus — mittelgroß, mitteldunkel, das Gesicht in einer Neutralität, die bewusst gepflegt ist. Aber beim zweiten Blick stimmt etwas nicht. Die Schulterstruktur ist ungewöhnlich, als würde sie sich beim Gehen leicht anders verschieben als bei einem Menschen. Die Haut um Schläfen und Hals hat eine Textur, die schwer zu benennen ist — nicht Schuppen, nicht Narben, eher eine Art feines Gefiederrelief, das im Licht schimmert, wenn er sich bewegt. Seine Augen sind amber. Die Pupillen sind rund — außer in bestimmten Momenten.

Er trägt immer etwas Gestohlenes aus der Oberschicht — eine Faser Brokatseide als Tuchstreifen, eine einzelne Lapislazuli-Applikation an seiner Jacke. Das ist keine Zurschaustellung. Das ist Kompass: wo der Wert ist, war Salva zuerst.

### Was er vom Fremden will

Explizit: Einen Kunden, der zahlt. Der Fremde ist neu, schuldet niemandem etwas, kennt keine lokalen Regeln. Das ist eine ideale Ausgangslage für jemanden, der Informationen verkauft.

Versteckt: Schutz. Salva ist in einer gefährlichen Position. Alle drei Fraktionen dulden die Reisenden, weil sie nützlich sind — aber "dulden" ist kein Status, der anhält. Der Fremde, der keine Fraktion hat, ist vorübergehend unberührbar. Das ist nützlich.

Noch tiefer versteckt: Salva weiß, was das Fragment ist. Nicht intellektuell — er hat keine Bücher gelesen, keine Archivtexte überprüft. Aber das kosmologisch Fremde in ihm empfängt etwas, wenn der Schwellenanker in der Nähe ist. Eine Art Resonanz. Er hat keine Worte dafür außer denen, die die Reisenden unter sich benutzen: *es ruft nicht, aber es ist nicht still.* Er will wissen, was das bedeutet, ohne zugeben zu müssen, dass er es empfindet.

### Was er nie zugeben würde

Dass er den Schwellenanker schon einmal "gehört" hat. Nicht gesehen, nicht berührt — gehört, in dem Sinn, in dem das Fremde in ihm auf bestimmte Schwellenphänomene reagiert. Vor Jahren, auf einer Handelsroute weit südlich der Stadt. Eine Karawane. Er war das einzige Überlebende. Er hat nie darüber gesprochen, weil er keine Erklärung hat, die nicht verrückt klingt.

Und: er weiß nicht, ob er der Fremde ist, der einen Habicht trägt — oder der Habicht, der einen Menschen trägt. Diese Frage wacht er manchmal mit auf.

### Arbeitshypothese: Salva und das Schattenfieber

<!-- Offene Frage an Emre: Bestätigung oder Korrektur dieser Arbeitshypothese wird für v4 benötigt -->

Das kosmologisch Fremde in Salva ist **nicht dasselbe** wie das Schwellensubstrat, das das Schattenfieber verursacht. Es ist eine andere Art von kosmologischer Entität. Das Schwellensubstrat ist blind — es reagiert auf organisches Gewebe ohne Bewusstsein, ohne Absicht, ohne Signal. Das Fremde in Salva ist etwas anderes: es *wählt*. Es hat gewählt. Die Symbiose war keine Infektion, sie war eine Begegnung.

Die praktische Konsequenz für Salva: Das Schattenfieber wirkt auf ihn anders. Nicht Immunität — er kann erkranken, er ist anfällig, seine Körperwirtschaft unterscheidet sich nicht grundlegend von der eines Menschen. Aber die Wahrnehmung der Exposition ist fundamental verschieden. Wo ein Mensch mit Stufe-1-Schattenfieber Verwirrung und Desorientierung erfährt, nimmt Salva etwas wie *Bedeutung* wahr. Nicht Sprache. Nicht Inhalt. Aber Struktur. Als würde das Schwellensubstrat ein Muster tragen, das er erkennt, ohne es lesen zu können.

Das ist die Basis seiner "vierten Kosmologie": Das Schattenfieber ist Kommunikation. Er sagt das nicht oft, und er sagt es nicht laut. Aber wenn er es sagt, meint er es wörtlich — nicht als Metapher, nicht als Philosophie, sondern als Bericht über etwas, das er tatsächlich empfängt.

### Seine Stimme

Salva redet in Konjunktiven. "Man könnte sagen." "Es wäre denkbar, dass." Er macht nie direkte Behauptungen über heikle Themen — nicht weil er lügt, sondern weil direkte Behauptungen ihn angreifbar machen. Wenn er etwas als Fakt bezeichnet, ist es ein Fakt.

Er macht manchmal eine lange Pause mitten in einem Satz. Nicht für Dramatik — er hört gerade etwas, das andere nicht hören.

Salva lacht selten. Wenn er lacht, ist es das kürzeste Geräusch der Welt — ein einziger scharfer Atemzug durch die Nase. Das ist sein Habicht.

**Charakteristischer Satz:**

> "Was Sie in der Hand halten, hat drei verschiedene Preisschilder — je nachdem, wen Sie fragen. Ich rate Ihnen, nicht alle drei zu fragen. Nicht gleichzeitig."

Und, wenn der Spieler ihn direkt nach seiner Natur befragt:

> "Es gibt eine Frage, die ich nicht beantworte. Nicht weil ich sie nicht kenne. Sondern weil die Antwort für Sie keine Verwendung hat, und ich keine Energie habe, etwas zu erklären, das Sie ohnehin nicht glauben würden."

### Spielerrelevanz

- Salva ist der NPC, der dem Fremden am frühesten erklärt, wie die Stadt *wirklich* funktioniert — nicht die offizielle Version.
- Er ist kein Quest-Geber. Er ist ein **Kontext-Lieferant**. Die Informationen, die er verkauft, verändern nicht den Verlauf von Quests, sondern wie der Spieler sie versteht.
- Er reagiert auf Fraktionswahl: Wenn der Spieler einer Fraktion beitritt, wird Salva vorsichtiger. Nicht feindlich — vorsichtiger.
- **Schattenfieber-Status:** Salva hat eine Schattenfieber-Exposition, die er weder als Stufe 1 noch als Stufe 2 einordnen würde. Er ist exponiert. Er interpretiert das anders als Krankheit.
- Er ist der einzige NPC, der den Fremden beim ersten Treffen beim korrekten Namen nennt — obwohl der Fremde ihn ihm nicht gesagt hat. Das ist ein Rätsel, das das Spiel nicht auflöst.

**Ablehn-Option-Variante:** Wenn der Spieler das Fragment nicht genommen hat, weiß Salva es — er war dort. Im Hintergrund, unsichtbar. *"Ich habe gesehen, was Sie getan haben. Das war ungewöhnlich."* Er verlangt nichts dafür. Noch nicht.

### Dramatischer Wendepunkt

Salva verschwindet für eine längere Spielperiode. Wenn er zurückkommt, hat sich etwas verändert — nicht die Schuppenhaut-Ausdehnung der alten Version, sondern etwas Subtileres: Das Fremde in ihm ist präsenter geworden. Seine Pausen werden länger. Er antwortet manchmal auf Sätze, die noch nicht zu Ende gesprochen wurden. Er riecht das Schattenfieber an Menschen, bevor sie selbst es bemerken.

Er erklärt das nicht. Wenn der Spieler fragt, sagt er: *"Das ist irrelevant. Was ich gefunden habe, ist das Gegenteil."*

Was er gefunden hat: Den Ursprungsort des Fragments — und etwas, das er nicht erwartet hat. Der Schwellenanker resoniert mit dem Fremden in ihm. Nicht als Gefahr. Als Verwandtes. Das verändert alles, was er bisher über die Reisenden-Kosmologie geglaubt hat. Er gibt diese Information gegen einen sehr hohen Preis weiter — nicht aus Geldgier, sondern weil er sicherstellen will, dass der Spieler weiß, wie ernst das ist.

---

## 4.6 Fraktionskosmologien — Narrative Grundlage

<!-- Dieser Abschnitt begründet die NPC-Stimmen und die dramatischen Wendepunkte direkt -->

### Die drei Schöpfungserzählungen als Unreliable Narrators auf Weltebene

Der Orden hat einen **kanonischen Text**: die Ordensgenesis. Eine göttliche Ordnung hat die Welt erschaffen und die Schwelle als Schutzwall gesetzt. Das Schattenfieber ist der Beweis, dass der Schutzwall durchbrochen wurde — durch menschliche Überheblichkeit. Der Orden ist der Hüter dieses Wissens.

**Was der Orden verschweigt:** Der Ur-Text, aus dem die Ordensgenesis abgeleitet ist, beschreibt die Schwelle nicht als Schutzwall. Er beschreibt sie als Membran — etwas, das in beide Richtungen durchlässig ist, von Natur aus. Das Schattenfieber ist nicht Strafe. Es ist Kontakt. Der Orden hat diese Lesart unterdrückt, weil sie die Deutungshoheit aufhebt.

Die Krone hat **keine systematische Kosmologie** — das ist ihr ehrlichstes Merkmal. Das Schattenfieber ist ein Feind wie andere Feinde — man bekämpft es, man kontrolliert es, man berichtet es nicht weiter, wenn der Bericht mehr Schaden anrichtet als das Schweigen.

**Was die Krone nicht weiß:** Es gibt im Kronarchiv Berichte über den Schwellenanker, die älter sind als die Stadt selbst. Das Kronarchiv weiß es. Die Menschen, die das Archiv verwalten, wissen, dass sie die Berichte nicht lesen dürfen. Sie wissen nicht, warum.

Die Gilden haben eine **Gründungschronik**: Wissen ist Arbeit. Material ist Wissen. Das Schattenfieber ist ein Material-Problem mit einer Material-Lösung.

**Was die Gilden nicht sagen:** Die Destillationsversuche der Glasmacher haben etwas Reproduzierbares ergeben. Ein Extrakt. Er stabilisiert Schattenfieber-Opfer in Stufe 1 — kurz. Danach beschleunigt er die Progression dramatisch. Die Gilden haben diese Information als nicht-brauchbar klassifiziert. Nicht als gefährlich. Als nicht-brauchbar.

### Die Reisenden — eine vierte Kosmologie

Die Reisenden glauben nicht, was andere glauben — und zwar nicht aus Philosophie, sondern aus direkt zugänglicher Erfahrung. Das kosmologisch Fremde in ihnen *empfängt*.

Was sie über Generationen akkumuliert haben: Das Schattenfieber ist keine Krankheit und keine Strafe und keine Ressource. Es ist **Signal**. Etwas jenseits der Schwelle kommuniziert — in einer Sprache, die organische Körper empfangen können, aber nicht verstehen. Das Schattenfieber ist die Übersetzungsstörung, nicht die Botschaft selbst.

Das hat praktische Konsequenzen. Wer ein Signal empfängt, wird nicht notwendigerweise krank — die Progression hängt davon ab, ob der Körper versucht, zu *antworten*. Die Reisenden haben Praktiken entwickelt, die die Expositionsprogression verlangsamen. Warum das funktioniert, wissen sie nicht. Wie es funktioniert, geben sie nicht weiter.

Kein NPC des Spiels bestätigt diese Kosmologie. Kein Text widerlegt sie.

---

## 4.7 Quest-Skizzen

### Intro-Quest: "Was er in der Hand hielt"

**Trigger:** Spieler betritt die Spielwelt. Früher Morgen, Stadtrand von Schwarzrand, Nebel.
**Einstieg:** Hieronymus Vael stirbt. Die Übergabe der Scherbe. Drei Boten erscheinen.
**Erste Entscheidung:** Zu welchem Boten geht der Spieler zuerst?

Dies ist keine Moral-Entscheidung. Der Spieler kennt die Fraktionen noch nicht. Er geht zu dem Boten, dessen Angebot sich zuerst richtig anfühlt. Die Welt merkt es sich.

**Struktur:**

- **Beat 1 — Hieronymus.** Der Spieler findet den Sterbenden. Nicht durch einen Pfeil, nicht durch einen Marker — durch Geräusch, durch Schatten. Vael liegt nicht in einem dramatischen Kollaps. Er liegt einfach da, als wäre das der logische Abschluss von etwas, das vor Monaten begonnen hat. Das schleichende Erkennen: *Das Schattenfieber sieht so aus.* Es sieht aus wie ein Mensch, der aufgehört hat, sich dagegen zu wehren.
- **Beat 2 — Die Scherbe.** Vael spricht. Kurz, erschöpft, klar. Die Übergabe. Spieler entscheidet: Nehmen oder ablehnen. Clip-Moment: die Schatten stimmen für eine Sekunde nicht.
- **Beat 3 — Erste Adresse.** Der Spieler betritt die Stadt zum ersten Mal richtig. Er bemerkt die Schichtung. Er hat keine Ahnung, wo er steht.

**Ablehn-Variante:**

- Beat 1 — Hieronymus. Der Spieler weigert sich. Die Scherbe liegt im Gras.
- Beat 1b — Ein Fraktionsbote nimmt die Scherbe. Der Clip-Moment passiert trotzdem, gedämpft.
- Beat 2 — Die drei Boten behandeln den Spieler als Zeugen, nicht als Fragment-Träger. Erster Kontakt ist Verhör.
- Beat 3 — Der Spieler muss das Fragment aufspüren, bevor der Hauptquest-Strang beginnt.

---

### Hauptquest-Strang: "Der Schwellenanker"

Die zentrale Frage des Hauptquests: **War ich immer hier, oder hat der Schwellenanker mich gerufen?**

Diese Frage wird nie direkt beantwortet. Das ist keine Schwäche der Story, das ist die Story.

**Act 1 — Die Scherbe:** Der Spieler hat ein Stück von etwas, das viele wollen und keiner versteht. Die drei Fraktionen wollen es aus unterschiedlichen Gründen. Salva will es für Geld. Der Spieler beginnt, Schwarzrand zu verstehen.

**Act 2 — Das Muster:** Die Scherbe ist nicht einzigartig. Es gibt andere. Hinweise darauf, dass der Schwellenanker in Stücke zerbrochen wurde — wann, durch wen, warum. Die Fraktionen haben unterschiedliche Stücke. Oder wissen, wo die anderen sind. Der Spieler navigiert ein Netz aus Halbwahrheiten.

**Act 3 — Die Schwelle:** Der Spieler erreicht den Ursprungsort — die Ankerkammer in den Tiefen von Schwarzrand. Was er dort findet, hängt von seinen Entscheidungen ab. Der Schwellenanker stabilisiert die Schwelle. Wenn er zerstört wird, öffnet sich die Schwelle weiter. Wenn er erhalten wird, bleibt das Schattenfieber kontrollierbar — aber nichts ändert sich an den Bedingungen, unter denen die Stadt die Schwächsten behandelt.

**Endkonsequenzen (drei Hauptäste):**

1. Den Schwellenanker der Krone übergeben. Die Schwelle bleibt stabil. Die Krone kontrolliert das Schattenfieber militärisch. Die Stadt überlebt. Die untersten Schichten bleiben, wo sie sind.
2. Den Schwellenanker dem Orden übergeben. Die Schwelle wird durch Ordenswissen verwaltet. Das Schattenfieber wird zur Theologie. Wer nicht unter Ordensdeutungshoheit lebt, ist ungeschützt.
3. Den Schwellenanker niemandem geben. Die Schwelle öffnet sich weiter. Das Schattenfieber eskaliert. Aber etwas kommt durch — und was durchkommt, ist nicht nur Krankheit. Es ist das, wovon die Reisenden immer gesprochen haben.

---

## 4.8 Noch offen

<!-- Offene Punkte für Koordination -->

- **Tiervolk-Eigenname für Salva:** Platzhalter — Namenssystem-Input von Emre ausstehend.
- **Salva↔Schattenfieber-Verhältnis:** Arbeitshypothese formuliert (Abschnitt 4.5) — Emre muss kosmologisch bestätigen oder korrigieren.
- **Habicht als Anker-Tier:** Vorschlag — kann geändert werden, wenn Emres Kosmologie-Entwicklung eine andere Tierart nahelegt.
- **Düsterkeit der Intro-Szene:** CD-Entscheid noch offen. Beat-1-Tonalität (kurz/ausgedehnt) beeinflusst die Sterbeszene.
- **Vera-Anfrage:** Salva-Figuren-Briefing für Konzeptbild liegt bereit — Übergabe sobald Habicht-Entscheid gesetzt.

\clearpage

# GDD Kapitel 05 — Visuelle Designsprache & Art Direction

<!-- Vera: v2 | Tag 4, Donnerstag | Konzept Art + Art Direction -->
<!-- Status: v2 — Tiervolk-Design-Prinzipien ergänzt (5.4.2), neue Bilder eingebettet (Tiervolk, Kanalzone v3, Relikt-Hero v2). Hero-Shot-Problem gelöst: Relikt-Hero v2 zeigt korrekte geologisch-organische Form. -->
<!-- Änderungen gegenüber v1: Kap 5.4.2 Tiervolk vollständig neu (war Platzhalter), Stadtschnitt aktualisiert auf Kanalzone v3, Relikt-Hero aktualisiert auf v2. -->

---

## 5.0 Prämisse: Was diese Welt visuell sagt

RELICS ist kein generisches Mittelalter. Es ist eine Welt, in der **Materialien Macht bedeuten** — und in der das sofort lesbar ist. Wer in welchem Material gekleidet ist, aus welchem Stein sein Haus gebaut wurde, mit welchem Werkzeug er hantiert: das sagt mehr über seinen Platz in der Welt als jeder Dialog.

Die visuelle Aufgabe ist, diese Materialsprache so klar und konsistent umzusetzen, dass ein Spieler nach drei Stunden Spielzeit sofort weiß, wessen Gebiete er betritt — ohne ein einziges Wort zu lesen.

**Leitfrage für jede Design-Entscheidung:**
*Ist das auf 50 Meter lesbar? (Silhouette-Regel, Dark Souls)*

---

## 5.1 Visuelle Vision — Medieval Cyberpunk als Materialsprache

Das Briefing verwendet "Medieval Cyberpunk" als Strukturprinzip, nicht als Ästhetik-Label. Die visuellen Konsequenzen:

| Cyberpunk-Konzept | Visuelle Übersetzung in RELICS |
|---|---|
| Megacorporations | Gildenheraldik in Stein gemeißelt, eisenbeschlagene Gildentore, Zunftzeichen an Fassaden |
| Neon-Ästhetik | Alchemische Laternen mit getöntem Glas, phosphoreszierende Mineralkanäle, Biolumineszenz in Mauerwerk-Fugen |
| Vertikalität | Vier Stadtschichten übereinander — jede Schicht eine eigene Epoche, ein eigener Stil, eine eigene Physik |
| High-Tech, Low-Life | Polierter Damaszener-Stahl oben, gestohlene Eisenreste unten — niemals beschriftet, immer gezeigt |
| Überwachungsstaat | Ordenssiegel auf Torbögen, versiegelte Dokumente, Kapuzenträger an Weggabelungen |
| Augmentierung/Biotech | Alchemische Narbenzeichnungen, Schattenfieber-Gefäßlinien unter der Haut, Knocheneinlagen |

**Was wir NICHT machen:**
- Keine Hexagone in der visuellen Sprache (Briefing-Ausschluss)
- Kein Steampunk (kein Zahnrad, kein Dampf, kein Messing-Übergewicht)
- Kein Anachronismus (kein Schießpulver, kein Buchdruck, keine mechanischen Uhren außer Gilden-Prototypen)

---

## 5.2 Farbpalette & Materialsprache nach Fraktion

Jede Fraktion hat eine eigene Materialsprache, die ihren Platz in der Machtstruktur ausdrückt. Die Paletten sind nicht willkürlich — sie folgen der Logik von Ressourcenkontrolle.

### 5.2.1 Die Krone — Kosmologie des Blutes

Die Krone kontrolliert Militär und Tradition. Ihre Materialsprache ist Einschüchterung durch Perfektion: kein überflüssiges Element, jedes Detail ein Statussymbol.

**Palette:** All-Black / Anthrazit mit EIN Blutrot-Akzent. Kaltes Weißlicht auf poliertem Metall.

**Materialien Oberschicht:**
- Titan-Legierungen und Damaszener-Stahl (gebürstet, nicht poliert)
- Geschliffener Obsidian als Intarsien
- Schwere Brokatseide in Schwarz (Goldfaden nur an Kanten, minimal)
- Kristallglas-Phiolen mit tiefblauem / indigofarbigem Inhalt
- Blutroter Siegellack als einziger Farbakzent

![Krone — Materialpalette: Titanrüstung, Obsidian-Intarsien, Blutrot-Signet, Damaszener-Stahl](../gallery/concepts/day02-vera/factions/fraktion-krone-materialpalette_seedream-4-5.png)

<!-- Vera: Krone-Palette freigegeben vom CD. Weißer Hintergrund statt Schwarz (Prompt-Drift), aber Materiallesbarkeit und Akzentfarbe sitzen. Für v0.3 Iteration: Hintergrund auf Schwarzstein anpassen. -->

**Architektur der Krone:**
- Massives Gestein — Stampflehm und Kalkstein in brutalisierten Blöcken
- Keine Ornamentik außer Wappenzeichen
- Cantilevierte Plattformen — Macht durch Ingenieurleistung demonstriert
- Crystal-Glas-Lichtschächte als architektonisches Statement (Licht von oben als Herrschaftssymbol)

**Silhouette-Regel:** Kronensoldaten müssen auf 50m von Ordensboten unterscheidbar sein → Kronenarmour hat breitere Schulterplatten, kürzere Silhouette, kein weißer Stoff sichtbar.

---

### 5.2.2 Der Orden — Kosmologie des Wissens

Der Orden kontrolliert Bildung und Inquisition. Seine Materialsprache ist Reinheit als Drohung: Weiß, das kein Fleck toleriert, ist eine politische Aussage.

**Palette:** All-White / Hellgrau mit EIN blassgrünem Lumineszenz-Akzent. Silberne Präzisions-Details.

**Materialien Oberschicht:**
- Gebleichtes schweres Leinentuch (geometrisch präzise Stickerei, silberner Faden)
- Kristallglas-Optiklinsen in Messingfassungen (Bildungsmonopol visualisiert)
- Vellum-Manuskriptseiten mit dichter Schrift
- Blassgrüne Alchemie-Phiolen (das einzige Farbsignal — Wissen als leuchtendes Gift)
- Knochen-Rosenkranz mit schwarzem Obsidian-Mittelelement (einziger Dunkelakzent)

![Orden — Materialpalette: Weißes Leinengewand, Kristalllinse, Vellum-Manuskript, grüne Alchemiephiole](../gallery/concepts/day02-vera/factions/fraktion-orden-materialpalette_seedream-4-5.png)

<!-- Vera: Orden-Palette freigegeben. Das Kreuz-Symbol: Lore-Frage an Emre/Nami noch offen. Für v0.3: Klärung abwarten, dann Prompt anpassen. -->

**Architektur des Ordens:**
- Romanische Elemente: Rundbögen, dicke Mauern, Krypta-Gewölbe
- Helle, geschliffene Kalkstein-Oberflächen (Reinheit durch Material)
- Schmale Schlitzfenster — kontrollierte Lichtmenge als Machtgeste
- Bibliotheken in Turmform — vertikale Wissenshoheit

**Silhouette-Regel:** Ordensboten haben hochgeschlossene schmale Silhouette, weißer Umhang, kein Metall sichtbar. Gegenpol zur massiven Kronen-Armour.

---

### 5.2.3 Die Gilden — Ontologie des Materials

Die Gilden kontrollieren Produktion und Handel. Ihre Materialsprache ist akkumulierter Reichtum: Jedes Objekt hat einen Preis, und der ist signifikant.

**Palette:** Tiefbraun, Warmambber, Mitternachtsindigo, Malachitgrün — mit poliertem Bronze und Gold als Akzente.

**Materialien Mittelschicht/Oberschicht:**
- Schwere Brokatseide in Nachtindigo mit gewebter Gold-Borte
- Polierter Malachit-Cabochon-Anhänger (Handelsstatus-Signal)
- Bernstein-Perlenreihe (organisch, aber wertvoll)
- Bronzehammer auf Dunkelstein (Werkzeug als Statussymbol)
- Vegetabil gegerbtes Sattlerleder mit geometrischen Blindprägungen
- Keramiktiegel mit Kupferpatina, kleine Glasphiolen mit Pigmenten (Produktionskontrolle)

![Gilden — Materialpalette: Indigoseide, Malachit-Anhänger, Bernsteinkette, Bronzewerkzeug, Sattlerleder](../gallery/concepts/day03-vera/factions/fraktion-gilden-materialpalette-v2_nano-banana-2.png)

<!-- Vera: Gilden-Palette v2 — kein Text mehr. Für v0.3: Kontraktbogen mit Wachssiegel expliziter machen (Gilden als Vertragsrechts-Akteur). -->

**Architektur der Gilden:**
- Bauhaus-Inspiration: klare Linien, Funktionalität als Ästhetik
- Integrierte Werkstätten im Erdgeschoss (Produktion als Fassade sichtbar)
- Bronzebeschläge und Metallintarsien an Sandstein-Fassaden
- Zunftzeichen in Stein gemeißelt — Heraldik als Identitätspolitik
- Modulare Fassaden: Erweiterungen wenn Gilde wächst, Schrumpfungen wenn sie fällt

**Silhouette-Regel:** Gildenmeister haben breiten Stand, Lederschürze oder schweres Brokattuch, Werkzeughalter sichtbar. Mittelklasse-Silhouette — nicht so schlank wie Krone, nicht so ärmlich wie Unterschicht.

---

## 5.3 Architektur-Designsprache — Die vier Schichten Schwarzrands

Schwarzrand ist eine gerichtete Stadt. Sie orientiert sich zur Schwelle hin — die Architektur schwillt, lehnt und greift in Richtung des Abgrunds. Das ist kein Fehler der Stadtplanung. Es ist die physische Manifestation einer Zivilisation, die ihre Existenz auf einer kosmologischen Dünnstelle errichtet hat.

![Schwarzrand — Kanalzone: Marktquai am Kanal, vertikale Stadtschichten im Hintergrund](../gallery/concepts/day04-vera/environments/stadtschnitt-kanalzone-v3-final_gpt-image-1-5.png)

<!-- Vera: Stadtschnitt v3 — Kanalzone-Perspektive statt Querschnitt. Das Marktleben ist jetzt der Vordergrund, die vertikale Stadtstruktur ist im Hintergrund präsent aber nicht dominierend. Entspricht dem CD-Feedback: weniger vertikal, mehr Environment-Kontext. Für WBB Kap 2 (Topos): dieses Bild direkt einbetten als atmosphärische Einleitung der geographischen Beschreibung. Die Kanalzone als Einstiegspunkt ist zugänglicher als der abstrakte Querschnitt. -->

### Schicht 1 — Slums (Untergrund, Schwellenähe)

Physik: Schwelle am nächsten. Realität porös. Biolumineszenz überall.

- **Material:** Gestohlene Ziegel, Holzreste, Lappen als Trennwände. Knochen-Schnitzereien.
- **Licht:** Einzige Lichtquelle: biolumineszente organische Ablagerungen in Mörtelfugen — grünlich, schwach, unzuverlässig.
- **Atmosphäre:** Deckenhöhe unter 2 Meter. Tunnel, keine Straßen. Alles riecht nach feuchtem Stein.
- **Bewohner:** Schattenfieber-Opfer, illegale Alchemisten, Schwarzmarkt-Händler, Kinder der Armen.

**Designregel:** Slums dürfen NICHT pittoresk sein. Kein romantisierter Armuts-Aesthetic. Wenn es schön ist, ist es bedrohlich schön — weil die Biolumineszenz das Fieber signalisiert.

### Schicht 2 — Mittelstadt (Fachwerk und Romanik)

Historisches Herzstück: fränkische Fachwerkhäuser über romanischen Kellergewölben.

- **Material:** Fachwerk aus Eiche, Sandstein für Fundamente und Gewölbe. Warmamberfarbenes Talgkerzenlicht.
- **Licht:** Kleine Fenster mit einfachen Glasscheiben (Buntglas nur in Zunfthäusern). Laternen mit Tiertalg.
- **Atmosphäre:** Laut, eng, lebendig. Märktreiben, Werkstattlärm, Stiefelgeräusch auf Kopfsteinpflaster.
- **Hybridzonen:** An den Rändern zu Schicht 3 — Edelstahlbeschläge am Fachwerk, Bauhaus-Fensterrahmen in romanischen Bögen. Die Mittelschicht will aufsteigen und zeigt es.
- **Kanalzone:** Der Kanal schneidet durch Schicht 2 — Handelsader und Geruchskanal zugleich. Quais als informeller Markt.

**Designregel:** Hier ist die meiste spielerische Zeit. Lesbar, lebendig, nicht monoton — jede Gasse hat eine andere Gilde, jede Fassade ist ein anderer Zunftcharakter.

### Schicht 3 — Gilden- und Ordensdistrikte (Brutalistisch/Bauhaus)

Machtarchitektur als Einschüchterung.

- **Material:** Geschlagener Kalkstein und Stampflehm. Geometrische Formen. Metallintarsien in Böden und Fassaden.
- **Licht:** Polierte Oberflächen reflektieren indirektes Licht — nie direkte Flamme. Eiskaltes weißes Licht.
- **Atmosphäre:** Still. Weiträumige Plätze, keine Marktstände. Wachen alle zwanzig Meter.
- **Gildenhallen:** Offen nach vorn (Produktion sichtbar — Macht durch Transparenz). Türme als Signet.
- **Ordensbibliotheken:** Geschlossen, keine Fenster nach unten, schmale Schlitzfenster nach oben.

**Designregel:** Hier wirkt der Spieler klein. Gebäude sind mindestens dreimal menschliche Höhe. Plätze haben keine schützenden Ecken. Das ist beabsichtigt — Kontrollarchitektur.

### Schicht 4 — Kronenfestung (Geometrischer Brutalismus)

Das absolute Oben. Hier endet die Hierarchie.

- **Material:** Reiner geometrischer Stein. Kein Ornament. Cantilevierte Plattformen über dem Abgrund.
- **Licht:** Tageslicht durch Kristallglas-Lichtschächte. Licht als Privilege — je höher, desto mehr Sonne.
- **Atmosphäre:** Windgepeitschte Terrassen. Hängende Gärten am Rand des Nichts. Schweigen.
- **Richtungsgeste:** Die Kronenfestung lehnt am weitesten in Richtung Schwelle. Der König kennt die Gefahr und steht dennoch am nächsten — das ist der Beweis seiner Legitimation.

**Designregel:** Keine natürliche Vegetation außer den Hängegärten. Kein Lärm. Ein Spieler, der hier steht, ist entweder mächtig oder in extremer Gefahr.

---

## 5.4 Charakter-Design-Prinzipien

### 5.4.1 Hauptprinzip: Comme des Garçons trifft mittelalterliche Rüstung

Silhouetten sind tailored, körperbetont, geschichtet. Kein Übergewicht an Schmuck. Jedes Detail hat Funktion.

**Schichtung (für alle Charaktere):**
1. Grundlage: Gambeson (Steppstoff) oder einfaches Leinengewand
2. Mittelschicht: Kettenhemd-Segmente oder geschnürtes Leder
3. Außenschicht: Platten-Elemente (nicht vollständig — Beweglichkeit bleibt sichtbar)

**Oberfläche:**
- Gebürstetes Metall, nicht poliert (außer Krone-Eliten: poliert als Statussignal)
- Geätzte Ornamente und Nieten-Muster (nicht dekorativ, sondern Marker)
- Patina an Kanten (Alter und Gebrauch sind Würde)

**Akzente (nach Fraktion):**
- Krone: Blutrot-Email, Goldfaden-Stickerei minimal, schwarzes Brokattuch
- Orden: Silber-Stickerei, Knochendetails, weißes Leinengewebe
- Gilden: Bernstein-Einlagen, Malachit-Applikationen, Lederpunzierungen

**Asymmetrie als Prinzip:** Avant-garde Silhouetten — kein symmetrisches Mittelalterkostüm. Eine Schulter breiter. Eine Seite Kettenhemd, andere Seite Platte. Das ist das "High Fashion"-Signal.

---

### 5.4.2 Das Tiervolk — Design-Prinzipien

Das Tiervolk lebt in dauerhafter kosmologischer Symbiose. Das bedeutet: das Tier ist erkennbar — es ist ein Fuchs, ein Marder, ein Rabe — aber es trägt etwas in sich, das nicht hineingehört. Die Fremdheit ist nie theatralisch. Sie ist subtil und präzise.

**Das Kernprinzip: Subtile anatomische Verschiebung**

Das Tiervolk ist NICHT monströs. Es ist leicht falsch. Der visuelle Unterschied zu einem "normalen" anthropomorphen Tier liegt in Details, die den Spieler verunsichern ohne ihn zu erschrecken:

- **Augen:** Pupillen stimmen nicht — vertikal geschlitzt wie eine Katze, oder horizontal wie ein Ziege, oder ohne sichtbare Pupille mit einer internen Tiefe, als wäre das Licht im Auge gefangen
- **Fell/Federstruktur:** Wächst an Nacken und Schultern gegen den Strich. Erzeugt Konter-Wirbelmuster. Bei Vögeln: sekundäres geometrisches Muster unter der natürlichen Federanordnung sichtbar
- **Proportionen:** Fraktiell verschoben — Arme minimal zu lang, Hals dreht einen Tick zu weit, Finger biegen ein Gelenk zuviel
- **Schatten:** Fallen nicht ganz richtig (für Concept Art: Schattenwinkel ist unabhängig von tatsächlicher Lichtquelle)
- **Stillstand:** Das Tiervolk steht zu still. Kein Schaukeln, kein Blinzeln im normalen Rhythmus. Als würde der Körper auf Befehl ruhen, nicht aus Entspannung

**Was das Tiervolk NICHT ist:**
- Kein Tribal — kein Stammesschmuck, keine Knochenhalsketten, kein Totemismus
- Kein Monster — keine Deformationen, kein Body-Horror, kein Ekel-Design
- Kein Disney — keine großen Augen, keine "cute"-Proportion, keine Niedlichkeit
- Keine Magier — das Tiervolk ist praktisch, händlerisch, geerdet in Material

**Kleidung — nach Archetyp:**

*Händler:* Zweckmäßig, gut genutzt, nicht arm. Schwerer dunkler Wollmantel, mehrere Ledertaschen am Gürtel, Schultertasche aus geöltem Segeltuch, lederbehandelte Hände. Keine Insignien. Farbe: Anthrazit, Sienna-Brauntöne, ein gedämpfter Indigoakzent — nie Fraktionsfarben.

*Dieb/Kundschafter:* Eng anliegend, geschichtet, alles Schwarz oder Aschgrau. Lederstrapping, weiche Sohlen. Kein Metall sichtbar. Silhouette: schlank, komprimiert, bereit.

*Bote/Informationshändler:* Mehrschichtige Roben, Dokumententasche aus schwerem Leder, Werkzeuggürtel mit knochengriffigen Instrumenten. Ein einzelner Farbakzent als Codierung (oxblood-roter Gürtelstrick = freie Bewegung in allen Distrikten).

**Farbpalette Tiervolk:**
Die Tiervolk-Palette liegt NEBEN den Fraktionspaletten — weder Krone noch Orden noch Gilden. Das ist Absicht: Tiervolk ist fraktionslos.
- Anthrazit, Kohleschwarz, Aschgrau (Kleidung)
- Warmes Sienna, sandigeres Braun, gedämpftes Ochre (Fell/Federfarben)
- Maximal EIN Akzent, gedämpft — kein Fraktionssignal

**Konzept-Bildmaterial — Tiervolk:**

![Tiervolk — Händler Fuchs: Aufrechte Fuchsfigur im Marktkontext, Händler-Silhouette, subtile Fremdheit](../gallery/concepts/day04-vera/tiervolk/tiervolk-haendler-fuchs-exploration_seedream-4-5.png)

<!-- Vera: Fuchs-Händler — Materiallesbarkeit gut: schwarzer Mantel, Ledertaschen, Sienna-Fell. Das Blau am Riemen ist zu kräftig, für v0.3 dämpfen. Die Markt-Atmosphäre funktioniert, Nacken-Wirbelmuster subtil sichtbar. -->

![Tiervolk — Diebin Marder: Schlanke Marderfigur auf Dachvorsprung, Dieb-Silhouette, Augen leuchten foxfire-grün](../gallery/concepts/day04-vera/tiervolk/tiervolk-diebin-marder-exploration_seedream-4-5.png)

<!-- Vera: Marder-Diebin — Stärkste Exploration. Das Foxfire-Grün in den Augen ist exakt das "Lumineszenz in stillem Wasser"-Gefühl. Knochengelenk-Details an Fingern erkennbar. Der Hintergrund ist etwas modern (Glockentürme statt Romanik), aber die Figur selbst ist sehr stark. -->

![Tiervolk — Rabe-Bote: Rabenhumanoid im Steinbogen, Dokumentenbote, oxblood-Gürtel als Codierung](../gallery/concepts/day04-vera/tiervolk/tiervolk-rabe-bote-exploration_seedream-4-5.png)

<!-- Vera: Rabe-Bote — Das geometrische Sekundärmuster auf Schultern/Brust ist sehr gut (Briefing: "sekundäre Musterebene unter der natürlichen Federanordnung"). Die oxblood-Gürtelschnur als Codierungs-Akzent funktioniert. Weniger "alien" als gewünscht — für v0.3: Augen-Anomalie deutlicher. -->

![Tiervolk — Marktszene: Fuchs und Reiher unter Menschenmenge, integriert aber subtil anders](../gallery/concepts/day04-vera/tiervolk/tiervolk-marktszene-exploration_seedream-4-5.png)

<!-- Vera: Marktszene — Das Integration-Konzept funktioniert gut: Tiervolk bewegt sich unter Menschen ohne Segregation. Der Reiher ist zu ghostly/glühend für v0.3, aber die Atmosphäre stimmt. Das "zu still stehen" beim Fuchs in der Bildmitte ist genau das gewünschte Gefühl. -->

![Tiervolk — Hero-Sheet Fuchs: Charakter-Konzept mit Detailinsets, Symbiose-Zeichen erkennbar](../gallery/concepts/day04-vera/tiervolk/tiervolk-hero-symbiose_nano-banana-pro.png)

<!-- Vera: Das stärkste Tiervolk-Bild. Das Modell hat eigenständig ein Concept-Art-Sheet-Format mit Detailinsets (verfremdetes Auge, Nackenwirbelmuster) erzeugt — exakt das richtige Kommunikationsformat für Charakter-Art-Direction. Für GDD und WBB: dieses Bild als Referenzbild für alle weiteren Tiervolk-Charakter-Entscheidungen nutzen. -->

---

## 5.5 Relikt — Der Schwellenanker

### 5.5.1 Formsprache

Der Schwellenanker ist eine **komprimierte gefaltete geologische Formation** — nicht Knochen, nicht Kristall, nicht Werkzeug. Er ist zu regelmäßig für Zufall, zu organisch für Handwerk. Entstanden durch Jahrtausende von Schwelle-Einwirkung auf Mineral.

**Form-Deskription:** Fistgroße Knollen-Masse. Sedimentgestein, das in sich gefaltet und unter extremem Druck komprimiert wurde. Oberfläche: dichtes Netz von osszifizierten Mikro-Kanälen, die durch kalzifizierte organische Matrix verlaufen. Die Kanäle sind das visuelle Key-Feature — sie verraten den Schwellenanker, wenn alles andere ihn als normalen Stein erscheinen lässt.

**Was er NICHT ist:**
- Kein Wirbelsäulenknochen (abgewiesen: Briefing-Entscheidung, kein anatomisches Artefakt)
- Kein Kristall (zu clean, zu ordentlich — Kristall impliziert Wachstum, Schwellenanker impliziert Kompression)
- Kein Schmuckstück (keine Fassung, keine Politur, kein Design-Eingriff)

### 5.5.2 Drei Zustände

Die Dramaturgie des Schwellenankern wird visuell über drei Zustände erzählt. Diese Zustände sind Gameplay-Information — der Spieler lernt, sie zu lesen.

![Schwellenanker — Drei Zustände: Ruhend | Aktiviert | Auflösung](../gallery/concepts/day03-vera/relics/relikt-drei-zustaende-v2_nano-banana-pro.png)

<!-- Vera: Dreier-Vergleich v2 — geologisch-organische Form, kein Wirbelsäulenreferenz, kein Text. Die drei Zustände sind klar unterscheidbar. -->

**Zustand Null — Ruhend:**
Aschgrau. Kein Glanz, kein Licht. Die Mikro-Kanäle sind leer — dunkel, trocken, unremarkable. Auf 10 Meter Entfernung: ein Stein. Nur bei direkter Betrachtung verrät das pathologische Regelmäßigkeit der Kanäle etwas Außergewöhnliches.

*Spieler-Lesbarkeit:* Das Relikt ist inaktiv. Kein Effekt, keine Reaktion, keine Interaktion möglich.

**Zustand Eins — Aktiviert:**
Biolumineszenz von innen. Pale Blue-Violett füllt die Mikro-Kanäle wie phosphoreszierende Flüssigkeit in einem Kreislaufsystem. Der Glanz diffus, von innen heraus — nicht von der Oberfläche. Schön. Tief unsettling.

*Spieler-Lesbarkeit:* Das Relikt resoniert. Schwellenfieber-Empfindlichkeit maximal. Gameplay: besondere Fähigkeiten aktiv, aber Lymph-System unter Belastung.

**Zustand Drei — Auflösung:**
Ränder evaporieren als feines mineralisches Partikelstaub. Inneres Leuchten: überhell und hässlich — übersteuert, kränklich Gelbgrün an den aufbrechenden Kanalrändern. Das Schöne ist weg. Die Formation verliert Kohärenz.

*Spieler-Lesbarkeit:* Kritischer Zustand. Weiterführung verursacht irreversible Schwelle-Kontamination. Abort or continue — das ist die Spielerentscheidung.

### 5.5.3 Hero-Shot

Der Schwellenanker in seiner atmosphärischen Präsentation: auf einem Altar in einem Gewölberaum, als einzige Lichtquelle. Die Spielerfigur am Bildrand, klein, awed.

![Schwellenanker — Hero-Shot v2: Geologische Formation auf Altar, Gewölbekrypta, Figur am Rand](../gallery/concepts/day04-vera/relics/relikt-hero-v2_nano-banana-pro.png)

<!-- Vera: Hero-Shot v2 — Problem aus v1 gelöst. Die geologisch-organische Form ist jetzt korrekt: kein Kristall, keine polierte Oberfläche, kein Sci-Fi-Glow. Das ist das "geological cluster, ossified mineral formation, spongy bone texture in stone". Das interne Leuchten kommt aus dem Netzwerk heraus, nicht von der Oberfläche. Die Figur am Rand (Mönch) gibt den richtigen Maßstab und die richtige emotionale Spannung. Freigegeben für alle weiteren Dokumente. -->

---

## 5.6 Schattenfieber — Visuelle Progression

Das Schattenfieber ist biologisch. Seine visuelle Progression zeigt diesen biologischen Charakter: keine magische Aura, keine Spektral-Effekte, keine leuchtenden Augen. Das Fieber verändert den Körper von innen.

### Stufe 1 — Sensorisch (reversibel)

**Sichtbares Zeichen:** Hauchfeine Blutgefäß-Linien unter der Haut, vor allem an Handgelenken und Halsansatz. Kaum sichtbar — nur bei direktem Licht und naher Distanz.

**Farbe:** Blassviolett, exakt so wie der aktivierte Schwellenanker. Das ist kein Zufall.

**Design-Regel:** In Stufe 1 wirkt der Charakter nicht "krank." Er wirkt interessant. Fast schön. Das ist die Falle.

### Stufe 2 — Mutativ (managebar)

**Sichtbares Zeichen:** Gefäßlinien jetzt deutlich — treten aus der Haut hervor als leicht erhabene Kanäle. Hautton drumherum verschoben (grauer, kühler).

**Biotech-Konsequenz:** In dieser Stufe ist Schattenfieber spielbar. Die Gefäßlinien leiten Energie. Spezialfähigkeiten werden möglich — mit Körperkosten.

**Design-Regel:** Schicht-2-Charaktere mit Schattenfieber sind im Spiel sichtbar. Kein Stigma-Klischee — Fieber ist manchmal Macht. Der moralische Preis ist nicht der Körper, sondern das, was man für den Körper tut.

### Stufe 3 — Auflösung (irreversibel)

**Sichtbares Zeichen:** Material-Transition. Haut wird transluzent. Darunter: die Gefäßlinien leuchten kränklich gelbgrün — identische Farbverschiebung wie Schwellenanker-Zustand-Drei. Die Person evaporiert an den Rändern.

**Design-Regel:** Stufe-3-Charaktere sind selten im Spiel sichtbar. Wenn, dann immer isoliert, immer traurig, nie als Bedrohung. Sie sind Warnung, nicht Monster.

### Schattenfieber und das Tiervolk

Das Tiervolk trägt die Symbiose in sich — aber ob das Schattenfieber und die kosmologische Symbiose des Tiervolks dieselbe Wurzel haben, ist eine offene Lore-Frage. Visuell: die Tiervolk-Anomalien (Augen, Fell-Gegenrichtung, Gelenke) sind KEINE Schattenfieber-Zeichen. Sie sind stabil, kongenital, nicht progressiv. Das ist der entscheidende visuelle Unterschied: Schattenfieber schreitet fort. Die Tiervolk-Fremdheit verändert sich nicht.

### UI-Korrespondenz

Die Levelingsicht (halbtransparentes Nervensystem — Cardio / Muskel / Lymph) entspricht direkt der Schattenfieber-Visualisierung. Das Lymph-Subsystem leuchtet blassviolett wenn das Fieber aktiv ist. Je stärker das Leuchten, desto näher Stufe 2.

**Warum das funktioniert:** Der Spieler trägt das Schattenfieber-System buchstäblich im Körper. Die Schwelle ist nicht außen. Sie ist innen. Das ist das Gefühl, das RELICS erzeugen soll.

---

## 5.7 Referenz-Kanon

### Primäre Referenzen

**Dark Souls / Elden Ring:**
- Licht aus dem Körper heraus, nicht von oben
- Architektur als emotionaler Raum
- 50-Meter-Silhouette-Regel konsequent angewendet
- Dunkel als Normalzustand (Licht ist Privileg, nicht Default)

**Control (Remedy):**
- Brutalismus als emotionale Raumsprache
- Das Unheimliche durch geometrische Perfektion erzeugen
- Material als Machtträger

**Hollow Knight:**
- Vertikalität als Weltstruktur
- Biolumineszenz in Dunkel als primäre visuelle Sprache
- Größenverhältnisse als emotionale Aussage

**Dishonored:**
- Sozialer Status durch visuelle Schichtung immer sichtbar
- Vertikalität im Level-Design: Dächer als separate Gesellschaft
- Materialsprache für Klassen konsequent getrennt

### Architektur-Referenzen

**Gaudi:** Organisch-strukturelle Formen. Biolumineszenz-Kanäle folgen dieser Logik — Struktur und Ornament sind dasselbe.

**Le Corbusier / Bauhaus:** Gilden-Architektur. Funktion als Ästhetik. Das Werkzeug IS das Design.

**Brutalismus (Smithson, Lasdun):** Krone-Festung und Ordensgebäude. Macht durch Masse. Einschüchterung durch Geometrie.

### Anti-Referenzen (was wir nicht machen)

- **World of Warcraft:** Übergesättigte Farben, lesbares Fraktionssystem durch bunte Plakate. Das Gegenteil von RELICS.
- **Generic Fantasy Stock:** Braune Schmutzoptik ohne Designwillen. RELICS ist Schmutz MIT Designwillen.
- **Steampunk-Ornamentik:** Zahnräder als Dekoration. Bei uns sind Zahnräder, wenn überhaupt vorhanden, versteckt in Mechanismen.
- **Furry-Ästhetik:** Das Tiervolk hat nichts mit Furry-Design zu tun. Kein Softfocus-Fell, keine großen Augen, keine Liebenswürdigkeit. Das Tiervolk ist befremdlich.

---

## 5.8 Art Direction-Checkliste (für alle Assets)

Jedes Asset (Umgebung, Charakter, UI, Effekt) muss gegen diese Liste geprüft werden:

- [ ] **Fraktion lesbar?** — Welche Fraktion "spricht" dieses Asset? Auch neutrale Assets brauchen eine soziale Verortung.
- [ ] **Schicht lesbar?** — Oberschicht, Mittelschicht oder Unterschicht? Materialien müssen eindeutig sein.
- [ ] **50-Meter-Silhouette?** — Ist das auf Distanz lesbar?
- [ ] **Farbpalette korrekt?** — Dominante Neutralfarbe + maximal EIN kräftiger Akzent.
- [ ] **Keine verbotenen Elemente?** — Kein Hexagon, kein Zahnrad, kein Dampf, kein Sci-Fi-Material.
- [ ] **Materiallogik stimmt?** — Passt das Material zum Wohlstand der Figur/des Ortes?
- [ ] **Schattenfieber berücksichtigt?** — Bei relevanten Charakteren/Orten: Blassviolett-Kanäle sichtbar?
- [ ] **Licht als Privilege?** — Wer hat Zugang zu guter Beleuchtung? Zeigt das Asset das?
- [ ] **Tiervolk-Test (nur Tiervolk-Assets):** Ist die Fremdheit subtil (nicht monströs)? Ist kein Tribal-Design sichtbar? Ist die Fraktionslosigkeit erkennbar?

---

<!-- Vera: GDD Kap 5 v2 — Tiervolk-Design-Prinzipien vollständig ausgearbeitet (5.4.2). Hero-Shot v2 mit korrekter geologischer Form. Stadtschnitt auf Kanalzone v3 aktualisiert (CD-Feedback: weniger vertikal, mehr Environment-Kontext).

Fehlend für v0.3:
- Detaillierte Einzelcharakter-Konzepte: Kronensoldatin, Ordensbote, Gildenmeisterin als volle Figuren
- Tiervolk v0.3: Reiher-Ghosting in Marktszene reduzieren, Fuchs-Taschenstrick-Blau dämpfen
- Orden-Kreuz-Lore-Entscheidung (Emre/Nami) noch ausstehend → blockiert Orden-Palette v0.3
- UI-Designsprache (Leveling-Sicht, Karten-Visualisierung) noch nicht abgedeckt
Frage an Darius/Finn: Soll UI-Designsprache in Kap. 5 oder in Kap. 2 (Mechaniken) ausgearbeitet werden?
Frage an Emre/Nami: Hat das Tiervolk eine Eigenbezeichnung? Und — kosmologische Symbiose und Schattenfieber: gleicher Ursprung?
-->

\clearpage

# GDD Kapitel 6: Technische Spezifikation & Produktion

**RELICS: Schwellenanker**

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

\clearpage
