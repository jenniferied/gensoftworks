---
title: "RELICS — Game Design Document"
subtitle: "Anhang B · v0.1"
short-title: "GDD"
author: "GenSoftworks Studio Simulation"
date: "2026"
lang: german
toc: true
---

# GDD Kapitel 01 — Spielübersicht & Design-Säulen

<!-- Darius: v2 — Aktualisierungen: "Schwarzrand" als offizieller Stadtname, "Schwellenanker" als Relikt-Bezeichnung (CD bestätigt, Tag 3 Briefing). Alle Statuszeilen und Autorenvermerke in HTML-Kommentare verschoben. Offene Punkte in Kap. 11 als beantwortet markiert. -->

<!-- Status: v2 | Tag 3, Mittwoch | Autor: Darius Engel -->

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
| Magie | Keine. Alchemie + Schattenfieber-Mutationen (mit Kosten) |
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
| **Lymph** | Alchemika einnehmen, Schattenfieber-Exposition, Heilrituale | Widerstandsfähigkeit gegen das Fieber, Zugang zu Mutationen, Risiko |

Jedes Subsystem hat vier Qualitätsstufen (nach dem Deus Ex-Modell: Untrained / Geübt / Fortgeschritten / Meister). Keine 1-100-Skalen. Qualitätswechsel, keine Zahlenoptimierung.

**Das Schattenfieber als dritte Progressionsachse:**
- Das Lymph-Subsystem koppelt direkt an die Schattenfieber-Progression (drei Stadien: Flüstern / Wandlung / Entgrenzung — nach biologischer Lore)
- Wer das Fieber unterdrückt (Krone-Weg), bleibt "sauber", verliert aber Zugang zu bestimmten Fähigkeiten
- Wer das Fieber nutzt (Gilden-Weg: Destillierung als Produkt), gewinnt Kraft, bezahlt mit Körper
- Wer das Fieber versteht (Orden-Weg: Deutungshoheit), bekommt tieferen Lore-Zugang, aber der Orden will etwas dafür

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
| 2 | **Schattenfieber-Scope:** Wie tief geht die Integration? | Hauptquest-antreibend UND dritte Progressionsachse (Lymph-Subsystem). Drei biologische Stadien. Drei Fraktions-Antworten = drei Gameplay-Pfade. |
| 3 | **Tiervolk:** Spielbar oder NPC? | NPC — Händler und Informationsbroker. Nicht spielbar. Leicht alien in Ästhetik, nicht tribal. Eigene Händler-Netzwerke parallel zu den Gilden. |
| 4 | **Release-Modell:** Wie liefern wir? | Streamer-Alpha (erste Stunde muss stehen) → Beta (max. 6–12 Monate) → Full Release → große DLCs. |
| 5 | **Relikt-Name:** Wie heißt das zentrale Artefakt? | **Der Schwellenanker** — In-World-Begriff, CD-bestätigt. Das Fragment beim Spieler: ein Stück des Schwellenankers. |
| 6 | **Ablehn-Option:** Kann der Spieler das Fragment ablehnen? | Ja — CD-bestätigt. Der Spieler darf das Fragment von Hieronymus Vael ablehnen. Konsequenzen in Kapitel 3 (Erzählkonzept) ausgearbeitet. |

---

<!-- Darius: Kap. 11 (offene Punkte aus v1) vollständig aufgelöst und in Kap. 10 als geklärte Fragen überführt. Interne Abhängigkeiten zu Kap. 2 und Kap. 3 sind jetzt dort direkt eingearbeitet. -->

*Versionsstatus: v2 — Alle Design-Säulen ausgearbeitet, High Concept gesetzt, Game Feel definiert. Stadtname Schwarzrand und Relikt-Name Schwellenanker CD-bestätigt eingetragen. Ablehn-Option integriert.*

\clearpage

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

![Nervensystem-Konzept: Schwellenanker-Relikt in Zustand Eins](../gallery/concepts/day02-vera/relics/relikt-zustand-eins-aktiviert_seedream-4-5.png)

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

![Schwellenanker: Zustand Null — ruhend](../gallery/concepts/day02-vera/relics/relikt-zustand-null-ruhend_seedream-4-5.png)

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

![Schwellenanker: Zustand Drei — Auflösung](../gallery/concepts/day02-vera/relics/relikt-zustand-drei-aufloesung_seedream-4-5.png)

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

\clearpage

# GDD Kapitel 03 — Erzählkonzept

<!-- Status: v1 | Tag 3, Mittwoch | Autor: Darius Engel -->
<!-- Darius: Dieses Kapitel ist in enger Abstimmung mit Nami Okafors GDD Kap. 4 entstanden. Nami hat Figuren und Quest-Skizzen geliefert; ich habe die systemische Struktur und die Spieler-Aktiv-Mechaniken hinzugefügt. Die Ablehn-Option (Spieler darf Fragment verweigern) ist CD-bestätigt und hier vollständig ausgearbeitet. -->
<!-- Darius: Verwendete Quellen: GDD Kap. 4 v1 (Nami, Tag 2), WBB Kap. 1 v1 (Emre, Tag 2), Briefing. Nami hat die Figuren-Stimmen, ich habe die Quest-Mechanik. Das Erzählkonzept braucht v2 mit Namis ausformuliertem Halbseiten-Text zur Ablehn-Option (war für Mi 10:00 versprochen). -->

---

## Überblick

Das Erzählkonzept von RELICS: Der Schwellenanker definiert, wie die Geschichte erzählt wird — nicht was die Geschichte ist. Die Handlung ist ein Werkzeug, um die vier Design-Säulen erfahrbar zu machen.

**Zentrales Erzählprinzip:** Der Spieler ist kein Held. Er ist ein Fremder, der in eine Situation hineingezogen wird, die ohne ihn bereits bestand. Die Geschichte ist nicht über den Spieler — sie ist eine Geschichte, in der der Spieler Entscheidungen trifft.

**Erzählstruktur:** Drei Akte, drei Fraktionspfade, mehrere Questlinien, die sich überschneiden und widersprechen. Kein Akt ist vollständig linear. Jeder Akt hat einen "Open-World-Raum", in dem der Spieler die Welt erkundet, bevor er den nächsten narrativen Anker betritt.

---

## 3.1 Intro-Sequenz — "Was er in der Hand hielt"

### Spieler-Fantasie

*"In den ersten fünfzehn Minuten muss ich verstehen, was dieser Ort ist. Nicht durch Exposition — durch Erleben."*

### Die Szene

**Zeitpunkt:** Früher Morgen. Die Stadt Schwarzrand liegt im Nebel. Der Spieler betritt die Spielwelt zum ersten Mal.

**Der Sterbende:** Hieronymus Vael liegt am Stadtrand, zwischen zwei ausrangierten Karrengeleisen. Freier Bote, gescheitert. Schattenfieber Stadium III. Er hat nicht mehr lange. Er hält etwas in der Hand: eine Scherbe aus einem Material, das der Spieler noch nicht einordnen kann. Unter einer bestimmten Neigung des Lichts leuchtet es — schwach, biolumineszent, unheimlich schön.

**Die Übergabe-Szene (Clip-Moment):** Hieronymus Vael sieht den Spieler. Er hat keine Kraft mehr für eine lange Erklärung. Er versucht es trotzdem. Die Szene dauert nicht länger als drei Minuten.

> *"Nimm das. Geh nicht zurück, wo du herkamst — dort kennen sie deinen Weg. Versteh das nicht als Warnung. Versteh das als das Einzige, was ich dir noch geben kann."*

Er streckt die Hand mit der Scherbe aus.

### Die Ablehn-Option

**CD-Entscheid:** Der Spieler darf das Fragment ablehnen.

Das ist keine Illusion einer Wahl. Es ist eine echte Verzweigung.

**Wenn der Spieler annimmt (Standard-Pfad):**
- Das Fragment wechselt in das Inventar des Spielers
- Hieronymus Vael stirbt kurz danach
- Schattenfieber-Exposition beginnt sofort: Lymph-Wert steigt minimal (kaum wahrnehmbar in Minute 15, signifikant in Stunde 3)
- Die drei Boten erscheinen (→ Abschnitt 3.2)
- Das Spiel öffnet sich in die volle Freiheit von Schwarzrand

**Wenn der Spieler ablehnt (Alternativer Einstieg):**

Der Spieler sagt Nein. Oder sagt nichts und wendet sich ab.

Hieronymus Vael schaut ihn an. Er hat keine Energie für Überzeugungsarbeit. Er legt die Scherbe ins Gras neben sich, schließt die Augen.

*Was dann passiert:*

1. Vael stirbt. Die Scherbe liegt im Gras. Der Spieler kann Schwarzrand betreten.
2. **Kurzfristige Konsequenz (erste Stunde):** Die drei Boten erscheinen trotzdem. Sie fragen nach der Scherbe. Der Spieler kann sagen, er habe sie nicht. Das stimmt. Alle drei Boten glauben ihm zunächst — aber die Glasmacher-Gilde hat Schwellenlinsen. Vreni Kast weiß, dass jemand in der Nähe des Toten war. Sie fragt nach.
3. **Mittelfristige Konsequenz (Akt 1):** Die Scherbe bleibt an Hieronymus' Sterbeort. Sie ist nicht weg — sie liegt da. Wer sie sucht, findet sie. Andere Akteure (Fraktionsboten) finden sie innerhalb von Stunden, wenn der Spieler sie nicht aufhebt. Der Spieler hat ein Zeitfenster.
4. **Langfristige Konsequenz:** Wer die Scherbe nie nimmt, spielt einen anderen Akt-1-Einstieg. Die Fraktionen nähern sich dem Spieler aus einem anderen Winkel — nicht als möglicher Träger des Fragments, sondern als möglicher Zeuge. Das öffnet bestimmte Quest-Optionen (Zeuge-Rolle), schließt andere (Fragment-Träger-Rolle). Spätestens in Akt 1, Beat 3 führt jeder Pfad zur selben zentralen Frage: Was ist das Fragment? Warum ist es hier? Warum stirbt jeder, der es trägt?

<!-- Darius: Namis Halbseite zur Ablehn-Option (versprochen Mi 10:00) sollte hier die konkreten Dialog-Optionen und den genauen Beat-Ablauf des Ablehn-Pfads ergänzen. Ich habe die systemische Struktur gesetzt; sie hat die Stimmen. -->

**Warum diese Entscheidung richtig ist:**

Das Briefing fordert: Immersive Sim. Echte Wahlfreiheit. Ein Spiel, das vorgibt, man könne ablehnen, es dann aber erzwingend macht, ist keine Immersive Sim — es ist ein Schienenspiel mit Illusionsknöpfen. Die Ablehn-Option muss real sein, um das Vertrauen des Spielers zu verdienen. Wenn er weiß, dass "Nein" tatsächlich Nein bedeutet, wählt er mit anderen Augen.

### Beat-Struktur der Intro-Sequenz

**Beat 1 — Ankunft:** Spieler betritt die Welt. Stadtrand. Nebel. Vael liegt da. Keine Erklärung, keine Exposition. Der Spieler sieht einen sterbenden Mann.

**Beat 2 — Die Scherbe:** Vael spricht. Kurz, erschöpft, klar. Die Übergabe-Szene. Spieler entscheidet: Nehmen oder ablehnen.

**Beat 3 — Die ersten Minuten nach Vael:** Der Spieler ist alleine. Drei Boten nähern sich — eine Uniformierte (Krone), ein ziviler junger Mann mit versiegeltem Brief (Orden), und... niemand. Die Gilden-Reaktion ist Vreni Kast, die "zufällig" auf dem Markt ist, wenn der Spieler die Stadt betritt.

**Beat 4 — Erster Fraktionskontakt:** Der Spieler spricht mit einem der drei Boten zuerst. Das ist die erste nicht-erzwungene Entscheidung. Die Welt merkt sie sich.

**Beat 5 — Schwarzrand:** Der Spieler betritt die Stadt zum ersten Mal richtig. Er sieht die vertikale Schichtung. Er hat keine Ahnung, wo er steht.

---

## 3.2 Akt 1 — Das Fragment

### Spieler-Fantasie

*"Ich verstehe gerade, was dieser Ort bedeutet. Und ich beginne zu verstehen, dass ich in der Mitte von etwas bin, das schon lange vor mir lief."*

### Erzählraum

Akt 1 ist die Exposition. Nicht durch Lore-Dumps — durch Erfahrung. Der Spieler erkundet Schwarzrand. Er trifft die Schlüssel-NPCs (→ GDD Kap. 4). Er beginnt, die Machtverhältnisse zu verstehen.

**Zeitliche Länge:** Akt 1 sollte die ersten 8–12 Spielstunden umfassen. Der Spieler soll Zeit haben, die Welt zu atmen, bevor der erste Act-1-Kulminationspunkt kommt.

### Schlüssel-Beats Akt 1

**Die drei Fraktionskontakte:** Der Spieler lernt alle drei kennen. Das kann in beliebiger Reihenfolge geschehen. Adelhaid Brenn (Krone) will das Fragment. Ivo Scherer (Orden) will es untersuchen. Vreni Kast (Gilden) will es analysieren. Alle drei haben gute Argumente. Keines der Argumente ist vollständig wahr.

**Die erste Fraktionsentscheidung:** Ab einem bestimmten Punkt in Akt 1 verlangt eine Fraktion eine Entscheidung — eine Aufgabe, die signalisiert, mit wem der Spieler arbeitet. Dieser Moment ist keine Zwangshandlung; der Spieler kann sich verweigern. Aber die Fraktionen werden ungeduldiger, je länger er wartet.

**Salva und die vierte Perspektive:** Salva (Tiervolk) erscheint frühzeitig in Akt 1. Er ist kein Auftraggeber — er ist ein Kontext-Lieferant (→ GDD Kap. 4). Die Information, die er über das Fragment hat, verändert nicht den Questpfad, aber die Interpretation. Der Spieler, der Salva gründlich befragt, versteht mehr — und misstraut den drei Fraktionen früher.

**Das erste Fieberflüstern:** Irgendwann in Akt 1 bemerkt der Spieler das erste Schattenfieber-Symptom. Das ist kein Story-Trigger — es ist eine organische Konsequenz des Lymph-Wert-Anstiegs. Schatten bewegen sich nicht richtig. Ein Geräusch hallt nach. Der Spieler sieht etwas, das nicht da ist. Eine Sekunde. Dann ist es vorbei.

**Der Akt-1-Kulminationspunkt:** Jeder Fraktionspfad hat einen Akt-1-Kulminationspunkt, der in den Akt-2-Raum führt. Beispiel Krone-Pfad: Brenn gibt dem Spieler den Auftrag, eine Schwarzmarkt-Scherbe zu sichern, bevor die Gilden es tun. Das führt den Spieler erstmals tief in den Schlund. Dort sieht er, was Brenns "kontrollierte Quarantäne" konkret bedeutet. Das ist die Moment der Kompliziertheit.

---

## 3.3 Hauptquest — "Der Schwellenanker"

### Spieler-Fantasie

*"Ich verfolge ein Objekt und merke, dass ich mich selbst verfolge."*

### Narrative Grundfrage

Die zentrale Frage des Hauptquests: **War ich immer hier, oder hat der Schwellenanker mich gerufen?**

Diese Frage wird nie direkt beantwortet. Das ist keine Schwäche der Geschichte — das ist die Geschichte.

Der Spieler kommt als Fremder. Ohne Gedächtnis an den Weg hierher. Ohne klare Motivation außer: Er war in der Nähe, als Vael starb. Oder: Er hat das Fragment genommen. Oder abgelehnt. In jedem Fall befindet er sich jetzt in Schwarzrand, und Schwarzrand hat Konsequenzen für ihn.

Irgendwann, irgendwo zwischen Akt 1 und Akt 2, stellt der Spieler fest: Das Fragment reagiert auf ihn. Nicht auf jeden. Auf ihn spezifisch. Der Lymph-Wert steigt schneller als bei anderen. Visions-Fragmente zeigen Orte, die er noch nie gesehen hat. Der Schwellenanker kennt ihn irgendwie. Oder er kennt den Schwellenanker.

### Akt-Struktur der Hauptquest

**Akt 1 — Das Fragment (parallel zu Abschnitt 3.2)**

Gameplay-Ziel: Den Ursprung des Fragments verstehen.
Narrative Frage: Was habe ich in der Hand?

Der Spieler sammelt Informationen aus drei Quellen (die drei Fraktionen liefern jeweils eine Teilwahrheit), Salva ergänzt eine vierte Perspektive, und das Fragment selbst "zeigt" gelegentlich Bilder — Dünnstellen, Kammern, Tiefen — die keiner erklären kann.

Am Ende von Akt 1 weiß der Spieler: Das Fragment ist ein Stück von etwas Größerem. Dieses Größere liegt irgendwo unter Schwarzrand. Und alle drei Fraktionen suchen es seit einer Generation.

**Akt 2 — Das Muster**

Gameplay-Ziel: Die anderen Fragmente finden.

Narrative Frage: Wer hat den Schwellenanker zerstört, und warum?

Das Fragment ist nicht einzigartig. In Akt 2 entdeckt der Spieler, dass der Schwellenanker in Stücke zerbrochen wurde — wann, durch wen, ob absichtlich. Die Fraktionen haben Fragmente, oder wissen wo sie sind, und halten diese Information zurück. Akt 2 ist ein Netz aus Halbwahrheiten und verdeckten Interessen.

**Mechanische Verknüpfung:** Jedes Fragment, das der Spieler findet oder berührt, erhöht den Lymph-Wert. Das ist keine Falle — es ist eine Einladung. Wer das Muster aktiv sucht, nähert sich der Schwelle. Der Spieler entscheidet, wie weit er geht.

**Die Koalitions-Enthüllung:** In Akt 2 entdeckt der Spieler, wer die Wurzelkammer geöffnet hat: Es war eine Koalition aus allen drei Fraktionen — Orden-Gelehrter, Gilden-Expedition, Kron-Beauftragter. Jeder gibt die Schuld den anderen. Alle haben sie. Das ist der Moment, in dem keine Fraktion mehr "richtig" sein kann — jede hat eine Leiche in ihrem Keller, buchstäblich.

**Akt 2 Kulminationspunkt:** Der Spieler findet den Weg zur Wurzelkammer. Er muss entscheiden, ob er hinabsteigt. Bis hierhin war die Geschichte verhandelbar. Ab hier nicht mehr.

**Akt 3 — Die Schwelle**

Gameplay-Ziel: Den Schwellenanker wiederherstellen oder zerstören oder keines von beidem.

Narrative Frage: Was tue ich mit dem, was ich weiß?

Der Spieler erreicht die Wurzelkammer. Was er dort findet, hängt von seinen bisherigen Entscheidungen ab — aber die Kammer selbst ist real, konsistent, und physisch präsent. In ihr: die natürliche Position des Schwellenankers. Leer, seit einer Generation. Das Schattenfieber steigt von unten wie Grundwasser.

Der Spieler hält Fragmente des Schwellenankers. Er kann sie zurücklegen. Er kann sie behalten. Er kann sie einer Fraktion überlassen. Er kann sie zerstören. Jede Entscheidung hat systemische Konsequenzen für die Welt von Schwarzrand.

### Die drei Hauptenden

**Ende 1 — Restauration (Krone-affin)**

Der Spieler legt alle Fragmente in die Wurzelkammer zurück. Der Schwellenanker stabilisiert die Schwelle. Das Schattenfieber reckt sich nicht. Schwarzrand überlebt.

*Konsequenz:* Die Krone kontrolliert die Kammer militärisch. Das Schattenfieber wird zum Staatsgeheimnis verwaltet. Die untersten Schichten bleiben, wo sie sind. Die Welt ist stabiler — und ungerechter als je zuvor. Brenn bekommt, was sie will. Die Schwächsten zahlen weiter den Preis.

**Ende 2 — Destillation (Gilden-affin)**

Der Spieler übergibt die Fragmente den Gilden. Die Glasmacher-Gilde synthetisiert den Schwellenanker als Rohstoff. Die Schwelle wird nutzbar — kontrollierbar, handelbar, profitierend. Das Schattenfieber eskaliert kurzfristig (Kontrollverlust in der Übergangsphase), dann stabilisiert die neue Gilden-Chemie.

*Konsequenz:* Die Gilden monopolisieren die Schwelle als Ressource. Das ist der konsequenteste Ausdruck des Medieval-Cyberpunk-Paradigmas: Die Natur wird zur Ware. Vreni Kast triumphiert. Die Profite bleiben oben. Die Kosten bleiben unten.

**Ende 3 — Öffnung (Schwellenaffin)**

Der Spieler gibt keine Fragmente ab. Er legt sie nicht zurück. Er hält sie. Und er bleibt in der Kammer.

Was passiert: Die Schwelle öffnet sich weiter. Das ist kein Weltuntergang — es ist eine Transformation. Schattenfieber-Betroffene in Stadium II und III beginnen, zu verstehen, was sie sind. Etwas kommt durch. Es ist nicht nur Krankheit — es ist das, wovon das Tiervolk immer gesprochen hat: Kommunikation.

*Konsequenz:* Schwarzrand verändert sich fundamental. Ob das besser oder schlechter ist, ist unklar. Der Orden verliert die Deutungshoheit. Die Krone verliert die Kontrolle. Die Gilden verlieren die Rohstoffquelle. Aber die Menschen in den untersten Schichten — die, die ohnehin schon tief in der Schwelle leben — werden zu etwas, das die anderen Fraktionen nicht mehr ignorieren können.

*Dies ist das einzige Ende, das die Frage "Kommunikation oder Krankheit?" beantwortet. Und die Antwort ist: beide.*

### Der Schwellenanker als mechanischer Hauptquest-Anker

Der Schwellenanker ist im Hauptquest mehr als ein Aufgabenobjekt. Er ist eine mechanische Beziehung:

- **Resonanz-Intensität:** Je höher der Lymph-Wert des Spielers, desto stärker "antwortet" der Schwellenanker. Visuelle Effekte intensivieren sich. Zusatz-Informationen werden zugänglich (Lore-Fragmente, die nur sichtbar sind, wenn der Spieler in Stadium I–II ist).
- **Fragment-Auffinden:** Der Schwellenanker-Puls (→ Kap. 2.5, Lymph-Stufe III-Vorteil) ist kein abstraktes HUD-Element — er ist eine physische Empfindung im Spiel, die die Richtung von anderen Fragmenten anzeigt.
- **Entscheidungspunkt:** Der finale Akt-3-Entscheid ist der einzige Moment im Spiel, an dem die Mechanik (Lymph-Wert, Fraktionsruf, verfügbare Fragmente) direkt die zugänglichen Enden bestimmt. Ein Spieler ohne ausreichenden Lymph-Wert kann Ende 3 nicht erreichen. Ein Spieler mit feindseligen Gilden kann Ende 2 nicht wählen.

---

## 3.4 Fraktionsquests

<!-- Darius: Diese Ausarbeitungen sind für v1 strukturell vollständig. Dialog-Details und spezifische Quest-Texte kommen in v2 mit Namis Kollaboration. -->

### Krone-Questlinie — "Das Erste Siegel"

**Hauptkontakt:** Marschall Adelhaid Brenn

**Questlinie-Fantasie:** *"Ich habe Legitimität erkauft. Jetzt zahle ich den Preis dafür."*

**Kernspannung der Krone-Linie:** Die Krone will Ordnung. Brenn glaubt an Ordnung. Der Spieler kann daran glauben — bis er sieht, was Ordnung kostet.

**Quest-Verlauf:**

*Quest 1 — "Passierschein"*
Brenn braucht jemanden ohne Kronstempel, der einen Auftrag in der Unterstadt erledigt. Der Spieler holt Informationen über eine Schwarzmarkt-Scherbe. Einfache Einführung in die Krone-Mechanik: Bewegungsfreiheit als Ressource, Krone als Schutzmacht.

*Quest 2 — "Quarantäne"*
Eine Unterkanal-Zone wurde gesperrt. Offiziell: Routineinspektion. Tatsächlich: Schattenfieber-Ausbruch unter vierzig Zivilisten. Brenn hat die Zone versiegelt. Der Spieler wird geschickt, den "Bericht" zu überbringen. Er trifft Menschen, die nicht wissen, warum sie eingesperrt sind. Siebzehn sind bereits gestorben.

*Entscheidungspunkt:* Der Spieler kann Brenns Anweisung befolgen (Bericht abliefern, zurückkehren). Er kann die Zone öffnen (Krone-Ruf sinkt, sieben der verbliebenen dreiundzwanzig überleben, Schattenfieber breitet sich in einen neuen Bereich aus). Er kann beides nicht tun und die Information verkaufen (an Orden oder Gilden).

*Quest 3 — "Das Archiv"*
Brenn weiß von Akten im Kronarchiv, die das Relikt erwähnen. Sie darf sie nicht lesen. Sie schickt den Spieler, sie zu stehlen. Was der Spieler findet: Die Krone kennt den Schwellenanker seit Generationen. Nicht das Fragment — das Original. Und hat nie gehandelt.

*Quest 4 — "Point of No Return"*
Brenn erfährt, was der Schwellenanker wirklich ist. Sie zieht sofort die militärische Konsequenz: Das muss der Krone gehören. Sie bittet den Spieler nicht. Sie verlangt. Dieser Moment definiert, ob der Spieler weiter mit der Krone geht — oder ob Brenn ab jetzt ein Hindernis ist.

---

### Gilden-Questlinie — "Der Rohstoff"

**Hauptkontakt:** Gildenmeisterin Vreni Kast

**Questlinie-Fantasie:** *"Ich baue echte Macht auf. Ich sehe, was sie kostet."*

**Kernspannung der Gilden-Linie:** Die Gilden sind die ehrlichste Fraktion — sie sagen, was sie wollen, und was es kostet. Aber Ehrlichkeit ist kein Schutz vor der Konsequenz dessen, was man tut.

**Quest-Verlauf:**

*Quest 1 — "Das Angebot"*
Kast trifft den Spieler "zufällig" auf dem Markt. Sie bietet Analyse des Fragments — nicht Besitz, Analyse. Zugang zu ihrer Werkstatt, ihrer Ausrüstung. Der Spieler bekommt erste Einblicke in die Gilden-Infrastruktur und die Materialsprache.

*Quest 2 — "Kanalrecht"*
Die Gerber-Gilde kontrolliert die Kanäle. Kast braucht Zugang zu einem tiefen Kanal-Abschnitt, den die Gerber gesperrt haben. Der Spieler verhandelt, kauft oder erzwingt den Zugang. Einführung in die Gilde-Mikropolitik: Die Gilden sind kein Block.

*Quest 3 — "Das Destillationsarchiv"*
Der Spieler findet Kasts Kellerarchiv. Destillationsversuche ohne Überlebende. Kast verteidigt das Archiv nicht moralisch: "Das waren Freiwillige. Das Schattenfieber hätte sie trotzdem getötet." Der Spieler entscheidet, wie er damit umgeht.

*Quest 4 — "Synthese"*
Kast hat genug Daten. Sie kann das Schattenfieber synthetisieren — in einem kleinen Maßstab. Sie braucht nur noch den Schwellenanker als finalen Datenpunkt. Dieser Quest ist der Gilden-Point-of-No-Return.

---

### Orden-Questlinie — "Die Prüfung"

**Hauptkontakt:** Bruder Ivo Scherer

**Questlinie-Fantasie:** *"Ich verstehe mehr als alle anderen. Der Preis dafür wird erst später fällig."*

**Kernspannung der Orden-Linie:** Der Orden hat das tiefste Wissen. Aber Wissen ist Kontrolle — und der Orden will beides.

**Quest-Verlauf:**

*Quest 1 — "Der Archivist"*
Scherer bietet Zugang zu einem Teil des Archivs. Erster Lore-Zugang, erste Fertigkeitsbücher (→ Nervensystem-Leveling-Unlock). Einführung in Scherers Informationsbroker-Mechanik: jede Information hat einen Preis.

*Quest 2 — "Die Kopie"*
Scherer zeigt dem Spieler seinen ur-Text-Fragmentfund. Fragmentarisch — und die fehlenden Stellen beschreiben genau, wie man den Schwellenanker zerstört. Ob das Auslassung oder Vergessen war, bleibt offen. Der Spieler kann Scherer danach fragen. Scherer sagt: "Ich weiß es nicht mehr."

*Quest 3 — "Deutungshoheit"*
Ein Priester im unteren Orden-Rang predigt eine Abweichler-Version des Schöpfungsmythos — näher an der biologischen Wahrheit als der offizielle Orden. Scherer schickt den Spieler, den Priester zum Schweigen zu bringen. "Zum Schweigen bringen" kann viele Formen annehmen. Der Orden-Quest ist der erste, der den Spieler offen mit dem Widerspruch zwischen Ordenslehre und biologischer Realität konfrontiert.

*Quest 4 — "Der Hochritus"*
Scherer bietet Zugang zum Orden-Hochritus: ein Ritual, das Schattenfieber-Stadium III stabilisieren kann. Dafür braucht der Orden den Schwellenanker. Der Spieler muss entscheiden, ob er zahlt — und womit.

---

## 3.5 Nebenquests

### "Der Zeuge"

**Typ:** Character-Quest
**NPC:** Alter Mann in den untersten Slums von Schwarzrand, Zeuge der "Öffnung" vor einer Generation

**Spieler-Fantasie:** *"Ich erfahre, was wirklich passiert ist — von jemandem, der dabei war."*

**Kurzbeschreibung:** Der alte Mann heißt Benedikt Haas. Er war Tunnel-Arbeiter bei der Gilden-Expedition, die die Wurzelkammer geöffnet hat. Er lebt im Schlund, isoliert, paranoid. Er ist der einzige Mensch in Schwarzrand, der alle drei Fraktionen aus der Koalitions-Nacht erkannt hat. Und er hat Angst.

**Quest-Struktur:**
- Der Spieler findet Haas über Salvas Hinweisnetz (Salva kennt ihn — oder kennt jemanden, der ihn kennt)
- Haas erzählt nicht auf Befehl. Er testet den Spieler zuerst: Beweise, dass du niemandem von der Fraktionskoalition arbeitest. Das ist schwer, wenn man gerade dabei ist, genau das zu tun.
- Wenn Haas vertraut: Er beschreibt die Nacht der Öffnung. Was er sah. Was die Fraktion-Vertreter sagten. Und warum er seither schweigt.
- Dramatischer Schluss: Haas bittet den Spieler um eine Aufgabe. Er will sterben — aber nicht durch das Fieber. Er will, dass jemand weiß, was er weiß, bevor er geht. Der Spieler kann annehmen oder ablehnen.

**Belohnung:** Haas gibt dem Spieler ein Objekt aus der Öffnungsnacht: Ein zerbrochenes Siegel, das alle drei Fraktionszeichen trägt. Unmöglich — aber real. Das ist der Beweis für die Koalition.

---

### "Die Weber-Gilde und das, was leuchtet"

**Typ:** Gilden-Seitenquest, Crafting-orientiert
**NPC:** Weberin Greth Saal, Mittelrang Weber-Gilde

**Spieler-Fantasie:** *"Ich verstehe, wie Macht durch Material fließt."*

**Kurzbeschreibung:** Greth Saal webt Schwellenfäden in Textilien — Fäden aus Organismen, die in Dünnstellen wachsen. Biolumineszent, reißfest, selbstreparierend. Begehrt von der Oberschicht. Und giftig für die Weber, die sie verarbeiten. Greth braucht jemanden außerhalb der Gilde, der ihr eine Ladung Fäden direkt aus dem Schlund beschafft — ohne den Gerber-Gilde-Zoll.

**Quest-Struktur:**
- Der Spieler beschafft die Fäden im Schlund (Schattenfieber-Exposition-Bereich)
- Dabei entdeckt er: die Weber, die in diesem Bereich arbeiten, leben alle in frühem Stadium II. Die Gilde weiß das. Das ist der Preis, den Greth nicht ausspricht.
- Entscheidungspunkt: Der Spieler kann die Fäden liefern (Gilden-Ruf +, Weber-Mikropolitik-Zugang). Er kann sie behalten und anderweitig verkaufen. Er kann die Information über die kranken Weber an den Orden oder die Krone weitergeben.

**Belohnung:** Zugang zu einer Weber-Gilde-Werkstatt und Rezepturen für biolumineszente Textilien (Crafting-Klasse III–IV).

---

### "Salvatore und die Karawane"

**Typ:** Tiervolk-Seitenquest, Lore-Quest
**NPC:** Salva

**Spieler-Fantasie:** *"Ich erfahre, was Salva wirklich ist — und was er wirklich weiß."*

**Kurzbeschreibung:** Salva verschwindet für eine Spielperiode. Wenn er zurückkommt, ist er verändert. Der Spieler kann nachfragen. Salva sagt: "Ich habe den Ursprungsort gefunden."

Was er gefunden hat: Den letzten bekannten Ort der Karawane, die vor Jahren verschwand — mit dem Objekt, das dem Schwellenanker ähnelte. Salva war das einzige Überlebende. Er war damals bereits in Dünnstellen-Nähe exponiert. Die Exposition hat ihn verändert — die Schuppenhaut, die erweiterten Sinne. Er ist kein Mensch mehr im biologischen Ursprungssinn. Er ist etwas dazwischen.

**Quest-Struktur:**
- Der Spieler kauft die Information über den Karawanenursprungsort von Salva (hoher Preis — Gold oder eine Gefälligkeit)
- Der Ort ist ein verfallenes Handelsposten außerhalb von Schwarzrand. Dort findet der Spieler Überreste der Karawane und ein weiteres Fragment
- Salva begleitet den Spieler optional. Er gibt keine Erklärungen. Er zeigt Richtungen.
- Am Posten: Der Spieler sieht Spuren, die zeigen, dass die Karawane nicht von außen angegriffen wurde. Sie hat sich von innen aufgelöst. Das Fragment war der Auslöser.

**Belohnung:** Ein weiteres Fragment (Hauptquest-Fortschritt) + Salvas vollständiges Vertrauen (Zugang zu seinen tiefsten Informationen).

---

## 3.6 Erzählerische Prinzipien

### Das epistemische Prinzip

Kein NPC im Spiel kennt die vollständige Wahrheit über den Schwellenanker. Der Spieler auch nicht. Die Geschichte ist ein Puzzle, das der Spieler aus Halbwahrheiten zusammensetzt. Die "Wahrheit" des Endes hängt davon ab, welche Quellen der Spieler befragt hat und welchen er geglaubt hat.

Das ist kein Versteck von Exposition. Es ist eine strukturelle Entscheidung: In einer Welt, in der drei Fraktionen aktiv konkurrierende Wahrheiten produzieren, kann kein Protagonist vollständige Wahrheit besitzen. Der Spieler erlebt dasselbe epistemische Problem wie die NPCs.

### Unreliable Memory

Ab Schattenfieber-Stadium II (Wandlung) werden Erinnerungen fragmentarisch. Das Spiel zeigt gelegentlich Szenen anders als beim ersten Erleben — ein Satz, den Hieronymus Vael sagte, klingt plötzlich anders. Ein Detail in Brenns erstem Gespräch fehlt. Das ist keine Continuity-Fehler — es ist eine mechanikvermittelte Erfahrung des Kontrollverlusts.

Der Spieler weiß nicht, welche Version wahr ist. Das ist Absicht.

### Die Erzählgeschwindigkeit

Akt 1: Langsam. Der Spieler soll Schwarzrand kennenlernen, bevor die Geschichte eskaliert.
Akt 2: Mittel. Die Informationsdichte steigt. Fraktionskonflikte spitzen sich zu.
Akt 3: Hoch. Alles läuft auf die Wurzelkammer zu. Der Spieler hat keine Zeit mehr für Ausweichen.

Die Spieler-Fantasie der ersten Stunde (Fremder betritt Sandbox) darf nicht gebrochen werden. Akt 1 muss diese Fantasie leben lassen. Die Geschichte zieht sich erst in Akt 2 eng.

---

![Schwarzrand: Vertikale Stadtschichtung](../gallery/concepts/day02-vera/environments/stadtschnitt-vertikale-schichtung_nano-banana-pro.png)

*Konzeptbild: Stadtschnitt Schwarzrand — die drei vertikalen Schichten (Obere Ränder / Mittelwand / Schlund) bilden den Schauplatz aller drei Akte.*

---

<!-- Darius: v2 dieses Kapitels braucht: Namis vollständige Ablehn-Option-Halbseite (Dialog-Optionen, Beat-Ablauf), ausformulierte Quest-Dialoge für mindestens zwei Quests, Leo-Feedback zur Erzählpacing-Logik. Quests 1-3 der Fraktionslinien sind strukturell gesetzt, aber textlich noch Stichpunkte. Das ist bewusst — das ist Namis Terrain. -->

*Versionsstatus: v1 — Vollständige Akt-Struktur, alle drei Fraktionsquests skizziert, drei Nebenquests ausgearbeitet, Ablehn-Option systemisch integriert. Dialog-Ausarbeitung und Nami-Kollaboration folgen in v2.*

\clearpage

# GDD Kapitel 04 — Schlüsselfiguren & NPCs

<!-- Version 2 — Tag 3, Mittwoch -->
<!-- Änderungen gegenüber v1: "Schwellenanker" als offizieller Relikt-Name gesetzt, Ablehn-Option eingebaut, Autor-Metadaten und Post-It-Verweise in HTML-Kommentare verschoben, Fragment-Szene ausformuliert -->

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

Hieronymus Vael war Bote. Nicht Krone, nicht Orden, nicht Gilden — er war **freier Bote**, einer der wenigen, die zwischen allen Lagern liefen, weil alle Lager solche Leute brauchen. Er wusste zu viel von zu vielen. Und er hat etwas transportiert, das er nicht hätte transportieren sollen: die Scherbe des Schwellenankers. Jetzt stirbt er daran. Stufe 3 des Schattenfiebers — die Schwelle — und er weiß, dass er nicht zurückkommt.

Er ist ca. fünfzig Jahre alt, sieht achtzig aus. Die Haut an seinen Händen ist dünn geworden wie Papier, darunter laufen Muster, die aussehen wie tinte-eingeschriebene Adern, aber dunkler. Er riecht nach Erde. Sein Atem geht in kurzen Stößen.

Er liegt am Stadtrand, im Gras zwischen zwei ausrangierten Karrengeleisen. Es ist früher Morgen. Nebel. Er hat sich hierhin geschleppt, weil er wusste: die Stadt war nicht sicher. Nicht mit dem, was er trägt.

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

<!-- Neu in v2 — eingebaut nach CD-Entscheid: Spieler DARF ablehnen -->

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

Brenn erfährt, was der Schwellenanker wirklich ist — ein Schwellen-Stabilisator, der die Grenze in der Gleichgewicht hält. Wenn sie das versteht, zieht sie sofort die politische Konsequenz: Wenn der Schwellenanker die Schwelle stabilisiert, und die Schwelle ist das, was das Schattenfieber kontrolliert, dann ist der Schwellenanker eine Waffe. Eine, die die Krone besitzen muss. Nicht aus Bosheit. Aus militärischer Logik. Das ist der Moment, in dem sie aufhört, eine Verbündete zu sein und anfängt, ein Hindernis zu werden — ohne dass sie sich verändert hat.

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

## 4.5 Tiervolk — Salva

**Funktion:** Informationsbroker, Händler, Verbindung zur Unterstadt und zu Netzwerken außerhalb der Fraktionen

<!-- Tiervolk-Eigenname für Salva ist noch Platzhalter — wartet auf Namenssystem-Input -->

### Eine Vorbemerkung zum Tiervolk

Das Tiervolk ist kein Volk. "Tiervolk" ist ein abwertender Begriff der Stadtbevölkerung für eine lose Gemeinschaft von Händlern und Informationsmaklern, die teilweise Merkmale aufweisen, die die Stadtbevölkerung als "tierisch" bezeichnet: Schuppenhaut, längere Gliedmaßen, Pupillen in anderen Formen, Geruchswahrnehmung, die über menschliche Norm geht. Das ist kein übernatürliches Merkmal. Es ist eine Anpassung — Generationen von Exposition an bestimmte Materialien und Umgebungen in bestimmten Regionen, deren Genaues nicht bekannt ist.

Sie nennen sich intern "die Reisenden." Das Wort Tiervolk benutzen sie für sich selbst nicht. Wer es ihnen gegenüber benutzt, bekommt höflich einen doppelten Preis.

Die Reisenden verkaufen, was andere nicht verkaufen, wissen, was andere nicht wissen, und bewegen sich in Räumen, die für die drei Fraktionen unsichtbar sind.

### Wer Salva ist

Salva ist zwischen dreißig und fünfzig — das ist schwer zu sagen, und er gibt keine Auskunft darüber. Er ist Informationsbroker und Kontaktvermittler. Er hat keine Gilde-Mitgliedschaft, keine Kronen-Akkreditierung, keinen Ordensstatus. Er hat ein Netz aus Kontakten, das alle drei Fraktionen umspannt — ohne dass irgendjemand von den anderen weiß, dass er auch für sie arbeitet.

Er hat schuppige Haut um die Schläfen und Handgelenke, einen länglichen Hals, Pupillen, die sich im Dunkeln weiten wie die eines Katers. Er trägt immer etwas Gestohlenes aus der Oberschicht — eine Faser Brokatseide als Tuchstreifen, eine einzelne Lapislazuli-Applikation an seiner Jacke. Das ist keine Zurschaustellung. Das ist Kompass: wo der Wert ist, war Salva zuerst.

### Was er vom Fremden will

Explizit: Einen Kunden, der zahlt. Der Fremde ist neu, schuldet niemandem etwas, kennt keine lokalen Regeln. Das ist eine ideale Ausgangslage für jemanden, der Informationen verkauft.

Versteckt: Schutz. Salva ist in einer gefährlichen Position. Alle drei Fraktionen dulden die Reisenden, weil sie nützlich sind — aber "dulden" ist kein Status, der anhält. Der Fremde, der keine Fraktion hat, ist vorübergehend unberührbar. Das ist nützlich.

### Was er nie zugeben würde

Dass er den Schwellenanker schon einmal gesehen hat. Nicht dieses spezifische Fragment — aber etwas Ähnliches, vor Jahren, in einer Handelsroute weit südlich der Stadt. Es kam mit einer Karawane, und die Karawane kam nicht an. Er war das einzige Überlebende. Er hat nie darüber gesprochen, weil er keine Erklärung hat, die nicht verrückt klingt.

### Seine Stimme

Salva redet in Konjunktiven. "Man könnte sagen." "Es wäre denkbar, dass." Er macht nie direkte Behauptungen über heikle Themen — nicht weil er lügt, sondern weil direkte Behauptungen ihn angreifbar machen. Wenn er etwas als Fakt bezeichnet, ist es ein Fakt.

Er macht manchmal eine lange Pause mitten in einem Satz. Nicht für Dramatik — er hört gerade etwas, das andere nicht hören.

**Charakteristischer Satz:**

> "Was Sie in der Hand halten, hat drei verschiedene Preisschilder — je nachdem, wen Sie fragen. Ich rate Ihnen, nicht alle drei zu fragen. Nicht gleichzeitig."

### Spielerrelevanz

- Salva ist der NPC, der dem Fremden am frühesten erklärt, wie die Stadt *wirklich* funktioniert — nicht die offizielle Version.
- Er ist kein Quest-Geber. Er ist ein **Kontext-Lieferant**. Die Informationen, die er verkauft, verändern nicht den Verlauf von Quests, sondern wie der Spieler sie versteht.
- Er reagiert auf Fraktionswahl: Wenn der Spieler einer Fraktion beitritt, wird Salva vorsichtiger. Nicht feindlich — vorsichtiger.
- **Schattenfieber-Status:** Salva hat Exposition — nicht Krankheit, aber Nähe. Die Reisenden, die in bestimmten Unterstadt-Bereichen handeln, kommen regelmäßig in Kontakt mit Schwellenbereichen.
- Er ist der einzige NPC, der den Fremden beim ersten Treffen beim korrekten Namen nennt — obwohl der Fremde ihn ihm nicht gesagt hat. Das ist ein Rätsel, das das Spiel nicht auflöst.

**Ablehn-Option-Variante:** Wenn der Spieler das Fragment nicht genommen hat, weiß Salva es — er war dort. Im Hintergrund, unsichtbar. "Ich habe gesehen, was Sie getan haben. Das war ungewöhnlich." Er verlangt nichts dafür. Noch nicht.

### Dramatischer Wendepunkt

Salva verschwindet für eine längere Spielperiode. Wenn er zurückkommt, sieht er verändert aus — nicht dramatisch, aber die Schuppenhaut hat sich ausgebreitet, sein Geruch ist anders. Er spricht nicht darüber. Wenn der Spieler fragt, sagt er: "Das ist irrelevant. Was ich gefunden habe, ist das Gegenteil."

Was er gefunden hat: den Ursprungsort des Fragments. Er gibt diese Information gegen einen sehr hohen Preis weiter.

---

## 4.6 Fraktionskosmologien — Narrative Grundlage

<!-- Dieser Abschnitt wurde von den WBB-Ethos-Notizen in das GDD überführt, da er die NPC-Stimmen direkt bedingt -->

### Die drei Schöpfungserzählungen als Unreliable Narrators auf Weltebene

Der Orden hat einen **kanonischen Text**: die Ordensgenesis. Eine göttliche Ordnung hat die Welt erschaffen und die Schwelle als Schutzwall gesetzt. Das Schattenfieber ist der Beweis, dass der Schutzwall durchbrochen wurde — durch menschliche Überheblichkeit. Der Orden ist der Hüter dieses Wissens.

**Was der Orden verschweigt:** Der Ur-Text, aus dem die Ordensgenesis abgeleitet ist, beschreibt die Schwelle nicht als Schutzwall. Er beschreibt sie als Membran — etwas, das in beide Richtungen durchlässig ist, von Natur aus. Das Schattenfieber ist nicht Strafe. Es ist Kontakt. Der Orden hat diese Lesart unterdrückt, weil sie die Deutungshoheit aufhebt.

Die Krone hat **keine systematische Kosmologie** — das ist ihr ehrlichstes Merkmal. Das Schattenfieber ist ein Feind wie andere Feinde — man bekämpft es, man kontrolliert es, man berichtet es nicht weiter, wenn der Bericht mehr Schaden anrichtet als das Schweigen.

**Was die Krone nicht weiß:** Es gibt im Kronarchiv Berichte über den Schwellenanker, die älter sind als die Stadt selbst. Das Kronarchiv weiß es. Die Menschen, die das Archiv verwalten, wissen, dass sie die Berichte nicht lesen dürfen. Sie wissen nicht, warum.

Die Gilden haben eine **Gründungschronik**: Wissen ist Arbeit. Material ist Wissen. Das Schattenfieber ist ein Material-Problem mit einer Material-Lösung.

**Was die Gilden nicht sagen:** Die Destillationsversuche der Glasmacher haben etwas Reproduzierbares ergeben. Ein Extrakt. Er stabilisiert Schattenfieber-Opfer in Stufe 1 — kurz. Danach beschleunigt er die Progression dramatisch. Die Gilden haben diese Information als nicht-brauchbar klassifiziert. Nicht als gefährlich. Als nicht-brauchbar.

### Das Tiervolk — eine vierte Kosmologie

Die Reisenden glauben, dass das Schattenfieber kein Durchsickern ist. Es ist eine **Kommunikation**. Etwas jenseits der Schwelle kommuniziert. Das, was wir Schattenfieber nennen, sind die Empfänger dieser Kommunikation — Körper, die versuchen, in einer Sprache zu antworten, die sie nicht sprechen können.

Kein NPC im Spiel bestätigt das. Kein Text widerlegt es.

---

## 4.7 Quest-Skizzen

### Intro-Quest: "Was er in der Hand hielt"

**Trigger:** Spieler betritt die Spielwelt. Früher Morgen, Stadtrand von Schwarzrand, Nebel.
**Einstieg:** Hieronymus Vael stirbt. Übergabe der Scherbe des Schwellenankers. Drei Boten erscheinen innerhalb von Minuten.
**Erste Entscheidung:** Zu welchem Boten geht der Spieler zuerst?

Dies ist keine Moral-Entscheidung. Der Spieler kennt die Fraktionen noch nicht. Er geht zu dem Boten, dessen Angebot sich zuerst richtig anfühlt. Die Welt merkt es sich.

**Struktur:**

- Beat 1 — Hieronymus. Die Übergabe der Schwellenanker-Scherbe. Das Rauschen beginnt (Schattenfieber Stufe 1, kaum wahrnehmbar).
- Beat 2 — Die drei Boten. Kurze Kontakte. Keine Entscheidung nötig — alle drei geben Adressen. Aber wer der erste Besuch ist, prägt die Eröffnungssequenz.
- Beat 3 — Erste Adresse. Der Spieler betritt die Stadt zum ersten Mal richtig. Er bemerkt die Schichtung. Er hat keine Ahnung, wo er steht.

**Clip-Moment:** Die Fragment-Übergabe. Hieronymus' letzter Satz. Das erste Rauschen — eine Sekunde lang sind die Schatten nicht dort, wo sie sein sollten.

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

**Act 3 — Die Schwelle:** Der Spieler erreicht den Ursprungsort — die Wurzelkammer in den Tiefen von Schwarzrand. Was er dort findet, hängt von seinen Entscheidungen ab. Der Schwellenanker stabilisiert die Schwelle. Wenn er zerstört wird, öffnet sich die Schwelle weiter. Wenn er erhalten wird, bleibt das Schattenfieber kontrollierbar — aber nichts ändert sich an den Bedingungen, unter denen die Stadt die Schwächsten behandelt.

**Endkonsequenzen (drei Hauptäste, keine eindeutige "richtige" Entscheidung):**

1. Den Schwellenanker der Krone übergeben. Die Schwelle bleibt stabil. Die Krone kontrolliert das Schattenfieber militärisch. Die Stadt überlebt. Die untersten Schichten bleiben, wo sie sind.
2. Den Schwellenanker dem Orden übergeben. Die Schwelle wird durch Ordenswissen verwaltet. Das Schattenfieber wird zur Theologie. Wer nicht unter Ordensdeutungshoheit lebt, ist ungeschützt.
3. Den Schwellenanker niemandem geben. Die Schwelle öffnet sich weiter. Das Schattenfieber eskaliert. Aber etwas kommt durch — und was durchkommt, ist nicht nur Krankheit.

---

## 4.8 Noch offen

<!-- Offene Punkte für interne Koordination -->

- **Fragment-Szene (ausformuliert):** Halbe Seite für Finn/Leo — in diesem Dokument als Beat 1 in Abschnitt 4.7 skizziert. Ausformulierte Sequenz folgt als eigenständiges Szenarien-Dokument.
- **Nebenquest-Ausarbeitung:** "Der Zeuge" (alter Mann in den Slums) und zwei weitere Ideen folgen in v3.
- **Tiervolk-Eigenname für Salva:** Platzhalter — Namenssystem-Input noch ausstehend.
- **Düsterkeit der Intro-Szene:** CD-Entscheid noch offen. Tonalität der Sterbeszene (kurz/ausgedehnt) beeinflusst Beat 1.

\clearpage

# GDD Kapitel 05 — Visuelle Designsprache & Art Direction

<!-- Vera: v1 | Tag 3, Mittwoch | Konzept Art + Art Direction -->
<!-- Status: Erster Entwurf — vollständige Struktur, alle Abschnitte besetzt. Bilder aus Tag 2 und Tag 3 eingebettet. -->

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

<!-- Vera: Krone-Palette freigegeben vom CD. Weißer Hintergrund statt Schwarz (Prompt-Drift), aber Materiallesbarkeit und Akzentfarbe sitzen. Für v0.2 Iteration: Hintergrund auf Schwarzstein anpassen. -->

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

<!-- Vera: Orden-Palette freigegeben. Das Kreuz-Symbol auf dem Gewand: Modell hat ein christliches Kreuz ergänzt, das nicht gebrieeft war. Lore-Frage an Emre/Nami: Hat der Orden ein Kreuz-Symbol, oder ein anderes Signet? Für v0.2 Iteration klären und Prompt entsprechend anpassen. -->

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

<!-- Vera: Gilden-Palette v2 — kein Text mehr. Nano Banana 2 hat die Materialzusammenstellung sehr gut getroffen: Erdtöne dominant, Malachit und Bernstein als Farbakzente, Bronzehammer als Würdezeichen. Für v0.2: Kontraktbogen mit Wachssiegel expliziter machen (Gilden als Vertragsrechts-Akteur). -->

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

![Schwarzrand — Stadtschnitt: Vier Schichten in diagonaler Tiefenperspektive](../gallery/concepts/day03-vera/environments/stadtschnitt-schwarzrand-v2_gpt-image-1-5.png)

<!-- Vera: Stadtschnitt v2 — schräge Tiefenperspektive statt frontaler Querschnitt. Das Schwarzrand-Richtungskonzept (alles zeigt zur Schwelle) kommt jetzt durch. Dramatischer als v1. Für WBB Kap 2 (Topos): dieses Bild direkt einbetten als Orientierungsbild für die geographische Beschreibung. Tobi: bitte bei UE5-Aufbau als Referenz nutzen — die diagonale Orientierung ist kein Zufall. -->

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

### Hauptprinzip: Comme des Garçons trifft mittelalterliche Rüstung

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

### Tiervolk

Händler und Diebe. Leicht alien vs. menschlich clean. Nicht tribal.

- Federleichte Materialien — Chitin-Applikationen, Beinlamellen aus natürlichen Quellen
- Farben: Nicht die Fraktionspaletten. Eigenständige Erdtöne — sandigeres Braun, gedämpftes Ochre.
- Silhouetten: Schlanker, beweglicher — Diebe-Ästhetik. Kein Plattenrüstungsgewicht.
- Keine Stammesornamentik — der Fehler, der sich von "alien" trennt.

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

<!-- Vera: Dreier-Vergleich v2 — kein Text mehr, geologisch-organische Form (kein Wirbelsäulenreferenz). Die drei Zustände sind klar unterscheidbar durch Materialzustand und Licht. Das Modell hat die Formkonsistenz zwischen den drei Objekten deutlich besser hinbekommen als v1. Für Darius/Kap 2-3: dieses Bild direkt als Mechanik-Illustration nutzen. -->

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

![Schwellenanker — Hero-Shot: Aktivierter Zustand auf Altar, Gewölberaum](../gallery/concepts/day02-vera/relics/relikt-hero-shot-aktiviert_gpt-image-1-5.png)

<!-- Vera: Hero-Shot ist die stärkste cineastische Darstellung. Das Problem: GPT hat eine zu kristalline Form erzeugt — zu clean, zu ordentlich, verliert die organisch-geologische Qualität. Für v0.2: Hero-Shot mit Nano Banana Pro iterieren (bessere Constraint-Adherence für organische Formen). -->

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

---

<!-- Vera: GDD Kap 5 v1 — vollständige Erstfassung. Fehlend für v0.2:
     - Detailliertere Charakter-Konzepte (Krone-Soldat, Ordensbote, Gildenmeister als einzelne Figuren)
     - Hero-Shot des Schwellenankern iterieren (zu kristallin in v1)
     - Stadtschnitt auch in WBB Kap 2 einbetten (Tobi/Emre koordinieren)
     - UI-Designsprache (Leveling-Sicht, Karten-Visualisierung) ist noch nicht abgedeckt — für v0.2
     Frage an Darius: Soll Kap 5 auch die Leveling-UI (Nervensystem-Sicht) visuell spezifizieren, oder ist das Kap 2 (Mechaniken)?
-->

\clearpage

# GDD Kapitel 6: Technische Spezifikation & Produktion

**RELICS: Schwellenanker**

<!-- Tobi: v3-Änderungen gegenüber v2: (1) Interface-Spezifikation Lymph → PP-Trigger als neuer Abschnitt 6.4.7 ergänzt — das war Darius' Blocker, (2) Autorname aus sichtbarem Dokumentkopf in HTML-Kommentar verschoben, (3) "(Nami-Alignment)" und "(Nami)" aus sichtbarem Text entfernt, (4) "Tobi's System" auf neutral umformuliert, (5) Tippfehler "M_SchattenfiebertOverlay" in 6.4.5 korrigiert zu "M_SchattenfiebertOverlay" — nein: korrekter Name ist M_Schattenfieber_Overlay. -->

<!-- Tobi: Verfasser Kap. 6: Tobias Richter, Technical Artist. Datum v1: Tag 2, Dienstag, 10:00 Uhr. -->

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
- **Schichtgrenzen-Entscheidung (Vera, Tag 2)**: oben fließend, unten diskret. World-Partition-Setup kann damit final geplant werden. Obere Ebenen (Layer 2–3) nutzen Blend-Volumes; untere Ebenen (Layer 0–1) haben harte Data-Layer-Cuts. Diese Frage ist abgeschlossen.

<!-- Tobi: Vera-Abstimmung zu Schichtgrenzen ist erledigt (Tag 2 Meeting). -->

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

<!-- Tobi: Tarkowski als Einfluss für Kamerastil, nach Nami-Input Tag 2. Im Fließtext keinen Autorname mehr. -->

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
- Beispiele: Bergkristall-Linsen der Gildenmeister, große Alchemie-Lampen in Ordenskorridoren, der aktivierte Schwellenanker (Zustand 2)
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

Das Schattenfieber-PP-System ist das komplexeste Single-Feature im Projekt. Es muss drei klar definierte Stufen mit smoothem Übergang abbilden und darf kein hartcodiertes System sein — alle Parameter müssen Blueprint-seitig steuerbar bleiben, damit das Gameplay-Team Inhalte ohne Tech-Art-Beteiligung implementieren kann.

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

Der `ShadowFever_Intensity`-Wert wird vom Gameplay-Blueprint geschrieben (Lymph-Subsystem → Interface, siehe 6.4.7). Das PP-System liest den Wert und reagiert. Die genaue Interface-Definition steht in Abschnitt 6.4.7.

**Übergänge**: Immer geblended über die Timeline-Kurve. Kein Hard-Switch zwischen Stufen. Minimum-Blend-Zeit: 2 Sekunden pro Stufe.

---

### 6.4.2 Stufe 0 — Basis (kein Schattenfieber)

Normaler Spielzustand. Der PP_Stage_0-Stack ist trotzdem aktiv — er setzt die Color-Grading-Basis für RELICS.

- **Color Grading**: ACES-Tonemapping, leicht kühle Schattenbereiche (Shadow Gain: RGB 0.95 / 0.95 / 1.02)
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
- **Film Grain**: hochgesetzt auf 0.45, Körnung feiner (0.7) — das "Rauschen" des einsetzenden Fiebers
- **Schattenbereich-Kühlung**: Shadow Gain +0.05 auf Blaukanal — Schatten werden kälter
- **Vignette**: 0.15 Intensität — kaum bemerkbar, rahmt aber den Blick

**Was nicht aktiv ist**: kein DOF, keine Vertex-Animation, keine Geometrie-Eingriffe. Das kommt in Stufe 2.

*Visuelles Konzept*: Die Chromatic Aberration ist das optische Echo — das Bild "klingt nach" im visuellen Sinne. Eine winzige Farb-Verschiebung, die sich wie ein Nachbild anfühlt.

<!-- Tobi: Ursprünglicher Hinweis auf Sound-Design und Nami-Input aus Kommentar rausgenommen, da kein Autorenname im sichtbaren Text. -->

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
- **Full-Screen-Overlay**: `M_Schattenfieber_Overlay` — ein Custom-Depth-Masking-Shader mit organischen Rissstrukturen. Die Risse entstehen an Bildrändern und wandern langsam zur Bildmitte. Bewegungsgeschwindigkeit abhängig von `ShadowFever_Intensity`.
- **Geometrie-Lücken**: Ausgewählte Wand-Meshes zeigen temporäre schwarze Flächenbereiche — als würden Teile der Weltgeometrie nicht mehr existieren. Technisch: ein separater Render-Pass mit Masked-Visibility über Custom Stencil Buffer.
- **Indigo-Bloom**: Emissive-Quellen bekommen starken Indigo-Halo — Bloom-Radius 8.0, Tint stark Richtung Indigo/Violett
- **Chromatic Aberration**: 1.5 Pixel, chaotisch (Rauschwert statt Sinuswelle)
- **Nervensystem-Visualisierung**: startet automatisch (→ 6.5)

**Was diese Stufe mit dem Schwellenanker-Shader verbindet**: Der kritische Schwellenanker-Zustand (→ 6.6) nutzt dasselbe visuelle Vokabular wie Stufe 3 — Rissstrukturen, Innen-Leuchten, Indigo-Tönung. Das ist keine Koinzidenz. Der Schwellenanker und die Krankheit sprechen dieselbe Sprache. Intentionale Ambiguität.

*Accessibility-Option*: Bei aktiviertem Modus werden Geometrie-Lücken deaktiviert, Overlay-Intensität auf 0.6 reduziert. Die Stufe bleibt narrativ funktional.

---

### 6.4.6 Schattenfieber-Ambient (Layer-gebunden)

Unabhängig vom Spieler-Infektionslevel haben die Data Layers eine Baseline Schattenfieber-Ambience:

- Layer 0 (Untergrund): `ShadowFever_Ambient = 0.15` — die Schwelle ist hier dünn, das spürt man
- Layer 1 (Straße): `ShadowFever_Ambient = 0.05`
- Layer 2 (Arkaden): `ShadowFever_Ambient = 0.0`
- Layer 3 (Türme): `ShadowFever_Ambient = 0.0`

Der Ambient-Wert addiert auf den Spieler-Wert. Ein Spieler ohne Infektion in Layer 0 läuft bei effektiv 0.15 — im Normalzustand nicht bewusst, aber da. Technische Narratologie: die Architektur erzählt die Kosmologie.

<!-- Tobi: Offene Frage an Emre — sind Tiervolk-Siedlungen an festen "dünnen Orten" oder wandern die? Statisch = Ambient-Wert Layer-gebunden (bereits implementiert). Dynamisch = NPC-Proximity-gesteuert, deutlich aufwendiger. Antwort steht noch aus. -->

---

### 6.4.7 Interface-Spezifikation: Lymph-Subsystem → PP-Trigger

<!-- Tobi: Das ist der Abschnitt, den Darius gebraucht hat. Vollständige Blueprint-Interface-Definition. Wer ShadowFever_Intensity schreibt, wer liest, welche Werte zu welchen PP-Stufen führen. Stand v3, Tag 3 Mittwoch. -->

Das Lymph-Subsystem (Gameplay-Seite, Darius' Verantwortung) und das Schattenfieber-PP-System (Tech-Art-Seite) kommunizieren über ein klar definiertes Blueprint-Interface. Diese Spezifikation legt den Vertrag zwischen beiden Systemen fest.

#### Überblick: Wer schreibt, wer liest

```
Gameplay-Seite (Darius):          Tech-Art-Seite (Tobias):
BP_LymphSubsystem                 BP_Schattenfieber
    │                                     │
    │── schreibt ──►  ShadowFever_Intensity (0.0–3.0)
    │                                     │
    │◄── liest ──────  OnStageThresholdReached(float Stage)
    │
    └── schreibt ──►  ShadowFever_Ambient (addiert, Layer-gebunden, READ ONLY für Gameplay)
```

Das Gameplay-System schreibt `ShadowFever_Intensity`. Das PP-System schreibt nichts zurück — es feuert Events. Das Gameplay-System hört auf diese Events und reagiert (z.B. Gameplay-Konsequenzen bei Stufenwechsel).

---

#### Interface-Funktion: `SetShadowFeverIntensity(float Value)`

**Aufrufender**: `BP_LymphSubsystem` (Gameplay)
**Empfänger**: `BP_Schattenfieber` (Tech-Art)

```
Signatur:      void SetShadowFeverIntensity(float Value)
Werte-Range:   0.0 – 3.0
Einheit:       normierter Intensity-Wert, keine physikalische Einheit
Clamp:         intern geclampt auf [0.0, 3.0] — Über-/Unterschreitung wird abgefangen
```

**Mapping Lymph-Stufe → ShadowFever_Intensity-Wert:**

| Lymph-Stufe (Darius) | ShadowFever_Intensity | PP-Stufe aktiv | Spielerlebnis |
|---|---|---|---|
| Untrained (Basis) | 0.0 – 0.2 | Stufe 0 (Basis) | Kein sichtbares Fieber |
| Geübt | 0.2 – 0.8 | Stufe 0 → 1 (gleitend) | Peripherie-Rauschen, Spieler unsicher |
| Fortgeschritten | 0.8 – 1.8 | Stufe 1 → 2 (gleitend) | Eindeutige Symptome, bewusst spürbar |
| Meister | 1.8 – 3.0 | Stufe 2 → 3 (gleitend) | Auflösung, Schwellen-Erfahrung |

*Wichtig*: Die Werte sind **kontinuierlich**, nicht diskret. Das PP-System blended fließend über die gesamte Range. Darius entscheidet, wie schnell die Lymph-Stufen steigen — das PP-System folgt.

**Zusätzliche Gameplay-Einflüsse auf den Wert:**

Der Wert setzt sich zusammen aus:
```
ShadowFever_Intensity = Lymph_BaseValue + Exposure_Delta + ShadowFever_Ambient
```

- `Lymph_BaseValue`: der Kernwert aus dem Lymph-Fortschritt (Darius' System)
- `Exposure_Delta`: temporäre Erhöhung durch Exposition (Slum-Bereiche, Infizierte NPCs, Schwellenanker-Kontakt) — klingt über Zeit ab
- `ShadowFever_Ambient`: Layer-gebundener Basiswert (read-only für Gameplay, wird vom PP-System addiert)

<!-- Tobi: Exposure_Delta ist ein Vorschlag meinerseits — Darius entscheidet, ob er das so implementiert oder anders strukturiert. Der PP-Empfänger braucht nur den finalen kombinierten Wert. Wie der zusammengesetzt wird, ist Gameplay-Logik. -->

---

#### Interface-Event: `OnStageThresholdReached`

**Sender**: `BP_Schattenfieber` (Tech-Art)
**Empfänger**: `BP_LymphSubsystem` (Gameplay — abonniert dieses Event)

```
Signatur:      Event OnStageThresholdReached(float Stage)
Werte:         1.0 (Stufe 1 erreicht), 2.0 (Stufe 2 erreicht), 3.0 (Stufe 3 erreicht)
Richtung:      Aufwärts UND Abwärts (Stage-Abfall unter Schwelle feuert ebenfalls)
```

Das Gameplay-System kann auf dieses Event reagieren mit:
- Gameplay-Mechanik-Freischaltung (z.B. Fähigkeiten bei Stufe 2+)
- NPC-Reaktionen triggern (NPCs erkennen infizierte Spieler)
- Journal-Eintrag / Narrative-Beat schreiben
- Sound-Cue auslösen (Sound-Design-Verantwortung)

---

#### Interface-Funktion: `GetCurrentShadowFeverStage()` (optional, read-only)

```
Signatur:      float GetCurrentShadowFeverStage()
Rückgabe:      aktueller ShadowFever_Intensity-Wert (0.0–3.0)
Zweck:         Gameplay-seitige Abfrage für z.B. HUD-Anzeige oder Dialogue-Conditionals
```

---

#### Fraktions-Presets (optionale Erweiterung)

Wenn Nami bestätigt, dass Fraktionswahl unterschiedliche PP-Presets erfordert, kann das Gameplay-System folgende Funktion aufrufen:

```
Signatur:      void SetFactionPPPreset(EFaction Faction)
Werte:         EFaction::Krone | EFaction::Gilden | EFaction::Orden
Effekt:        Lädt einen Preset-Stack auf PP_Stage_0 — verändert die Basis-Tonalität
               Krone:  wärmerer Basiston, Ambience reduziert (Unterdrückung sichtbar)
               Gilden: neutraler Basiston, Emissive-Intensität leicht erhöht
               Orden:  kühler Basiston, Schattenbereiche dunkler (Wissen = Tiefe)
```

<!-- Tobi: Das ist ein Vorschlag, kein gesetztes Feature. Nami muss bestätigen, ob Fraktions-PP-Presets narrativ gewünscht sind. Wenn ja, ist das ein kleiner Aufwand (drei PP_Stage_0-Varianten). Wenn nein, brauchen wir nur den generischen Stage-0. -->

---

#### Blueprint-Verbindungsschema (schematisch)

```
BP_LymphSubsystem
    │
    ├── OnLymphLevelUp ──────────────────────────► BerechneIntensity()
    │                                                    │
    │                                           SetShadowFeverIntensity(value)
    │                                                    │
    │                                          BP_Schattenfieber
    │                                                    │
    │                                          Timeline blended PP-Stack
    │                                                    │
    │◄────────────── OnStageThresholdReached ────────────┘
    │
    ├── OnNarrativeTrigger (optional)
    ├── OnNPCReaction (optional)
    └── OnSoundCue (Sound-Design)
```

---

#### Zusammenfassung für Darius

Das PP-System braucht von Gameplay-Seite genau **einen Float** (0.0–3.0). Wie dieser Float berechnet wird — aus Lymph-Fortschritt, Expositions-Akkumulation, Fraktions-Modifikatoren — ist vollständig in Darius' Hand. Das Tech-Art-System ist bewusst so gebaut, dass keine Abhängigkeit in die andere Richtung existiert: kein PP-Code greift auf Gameplay-Variablen zu.

Das PP-System feuert Events zurück. Darius abonniert, was er braucht.

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

## 6.6 Schwellenanker-Shader — Master Material System

<!-- Tobi: Asset-Namen: M_Schwellenanker_Master, MI_Schwellenanker_Dormant, MI_Schwellenanker_Resonant, MI_Schwellenanker_Critical, T_Schwellenanker_Riss_01, BP_Schwellenanker. -->

### 6.6.1 Konzept

Der Schwellenanker — der kosmologische Resonanzpunkt, das namensgebende Artefakt dieser Spieliteration — existiert als ein einziges Mesh mit einem Master-Material und drei Material-Instanzen. Die Übergänge zwischen den Zuständen sind immer geblended, nie hart. Der Schwellenanker ist kein Gadget; er ist ein kosmologisches Instrument. Das muss im Material sichtbar sein.

**Zur Form**: Vera hat die Geometriebeschreibung auf "folded geological formation, compressed ossified mineral cluster" spezifiziert — weg von einer wirbelsäulenartigen Struktur. Das hat Shader-Konsequenzen: SSS-Radius und Riss-Topologie müssen auf eine verdichtete, mineralische Form kalibriert werden, nicht auf eine langgestreckte organische. Der Riss-Procedural-Noise (`T_Schwellenanker_Riss_01`) wird entsprechend neu kalibriert — komprimierte Rissstrukturen statt radialer Brüche.

<!-- Tobi: Vera hat die Form-Beschreibung geändert (Tag 3 Briefing). Shader-Konsequenz: SSS-Radius-Kalibrierung neu, T_Schwellenanker_Riss_01 Noise-Profil anpassen. Kein großer Aufwand — ein Parametertuning, kein Umbau. -->

---

### 6.6.2 Drei Zustände

**Zustand 1 — Ruhezustand (dormant):**
Der Schwellenanker ruht. Er ist nicht tot — er ist latent lebendig.

- **Base Material**: transluzentes, mattes Grundmaterial
- **Subsurface Scattering (SSS)**: aktiv, warme Untertonfarbe (RGB 1.0 / 0.85 / 0.7 — leicht goldenes Hautton-Unterlicht)
- **SSS-Radius**: 0.8 cm — das Licht streut tief, wie durch organisches Gewebe. Bei mineralischer Kompression ggf. auf 0.5 cm reduzieren (Abstimmung nach erster Vera-Referenz).
- **Roughness**: 0.55 — nicht spiegelnd, aber nicht stumpf. Polierter Knochen oder Elfenbein-Charakter. Bei mineralischer Form: ggf. Richtung 0.45 (glattere Kompressionsflächen).
- **Emissive**: 0.0 — kein aktives Leuchten
- **Lumen-Emitter**: deaktiviert

*Designabsicht*: Der Schwellenanker soll schon im Ruhezustand anders aussehen als totes Material. Das SSS erzeugt innere Lebendigkeit — etwas ist da, schläft aber.

---

**Zustand 2 — Aktiver Zustand (resonant):**
Der Schwellenanker ist aktiviert. Er ist zur Lichtquelle geworden.

- **Base Material**: dasselbe Grundmaterial, aber SSS-Intensität um 40% erhöht
- **Emissive-Layer**: hochgefahren, Farbe = warmes Indigo-Weiß (RGB 0.85 / 0.8 / 1.2, überbelichtet bei 3.5)
- **Lumen-Emitter**: aktiviert (Klasse A) — der Schwellenanker wirft echtes GI in die Szene, färbt umliegende Wände und Böden
- **Lichtfarbe Lumen**: leicht violett-weiß (CCT 7500K mit Indigo-Bias) — kühler als natürliches Licht, kalt und klar
- **Lichtradius**: 4m für direkte Lumen-Reichweite, darüber Bloom-Halo
- **Bloom-Halo**: 6.0 Radius, Indigo-Tint — sichtbar auch auf Screenshots, nicht nur in Bewegung

*Designabsicht*: Der aktivierte Schwellenanker soll sofort als Lichtquelle erkennbar sein. Er ist die wichtigste dynamische Lichtquelle in jeder Szene, in der er aktiv ist.

---

**Zustand 3 — Kritischer Zustand (überlastet):**
Der Schwellenanker ist am Limit. Das kosmologische Instrument bricht unter Last.

- **Base Material**: Riss-Overlay-Layer aktiv — ein Masked-Texture-Layer projiziert organische Rissstrukturen auf die Oberfläche
- **Riss-Struktur**: `T_Schwellenanker_Riss_01` (Procedural Noise-basiert, komprimierte Rissgeometrie passend zur mineralischen Grundform — kein symmetrisches Muster) — Risse öffnen sich im Laufe des kritischen Zustands (Blend-Parameter steuert Öffnungsgrad)
- **Innenleuchten**: durch die Risse scheint das Emissive-Innere — lokal höhere Emissive-Intensität an Riss-Kanten (8.0+, kalt-violett)
- **Subsurface Scattering**: jetzt blau-violett getönt (RGB 0.7 / 0.6 / 1.3) — die Wärme ist weg, das SSS-Licht ist kalt
- **Lumen-Emitter**: flackernd, instabil (Blueprint-gesteuerte Intensitätsschwankung, 2–8 Hz unregelmäßig)
- **Lichtfarbe**: hart-violett (CCT >10000K, stark ins Ultraviolett verschoben)
- **Vertex-Animation**: das Mesh selbst vibriert leicht (±0.2mm, 12 Hz) — submillimeter, erzeugt nervöses Shimmern

*Designabsicht*: Visuelles Vokabular entspricht bewusst PP-Stufe 3. Der Schwellenanker und das Schattenfieber sprechen dieselbe Sprache: Rissstrukturen, Kalt-Violett, Innenleuchten, Instabilität. Der Spieler sieht diese Verbindung — ob er sie versteht, ist Erzählung. Zustand 3 zeigt keine kontrollierte Instabilität, sondern ein Objekt kurz vor dem Bruch — das Riss-Blend-Parametersystem erlaubt es, diesen Brechpunkt für Act 3 sequenziell aufzuziehen.

<!-- Tobi: Namis narrativer Kommentar (Tag 3 Briefing) — "ein Anker kann reißen" — ist für Act 3 relevant. Im Shader ist das angelegt: Rissstrukturen mit steuerbarem Öffnungsgrad. Kein neuer Shader-Aufwand nötig, nur Blueprint-Kurven-Authoring. -->

---

### 6.6.3 Master-Material-Struktur (M_Schwellenanker_Master)

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

**Drei Material-Instanzen**: `MI_Schwellenanker_Dormant`, `MI_Schwellenanker_Resonant`, `MI_Schwellenanker_Critical` — alle vom selben Master. Blueprint interpoliert zwischen den Instanz-Parametern über `State_Alpha`.

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

<!-- Tobi: Houdini-Terrain wartet auf Emres Topos-Kapitel. Stadtname, Sichtachsen, Gebirgs-Kontext fehlen noch. Emre hat Topos als Fokus für Tag 3 genannt — ich nehme an, bis Ende heute kommt genug Material für erste Constraint-Kurven. -->

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

**Warum kein AgX?** AgX ist für Photography optimiert und komprimiert Highlights weicher. RELICS braucht scharfe, klare Lichter — die Bergkristall-Linsen, die Schwellenanker-Emitter müssen leuchten, nicht weich werden. ACES gibt uns das.

---

### 6.8.2 Display-Kalibrierung (internes Studio)

Alle Arbeitsstationen im Studio haben kalibrierte Displays (Delta-E < 2.0). Die Referenz-LUT läuft auf einem Samsung Odyssey OLED, der als "Goldstandard"-Display dient. Spieler-seitig gibt es keine Kontrolle — daher sind alle Emissive-Werte so kalibriert, dass sie auch auf einem Standard-SDR-Display (sRGB, 200 cd/m² Peak) korrekt wirken. HDR-Displays bekommen automatisch einen separaten Display-Transform mit erweiterten Highlight-Bereichen.

---

## 6.9 Produktion & Release-Pipeline

### 6.9.1 Milestone-Übersicht

| Milestone | Technischer Status | Schlüssel-Deliverables |
|---|---|---|
| **Pre-Alpha** | Prototyp-Pipeline | Rendering-Architektur steht, Material-Master-Systeme gebaut, World Partition Setup stabil |
| **Alpha** (Streamer) | Feature-Freeze Rendering | Data Layers gesetzt, Lumen-Konfiguration fixiert, PP-System stabil, Schwellenanker-Shader stabil. Standard: stabil + konsistent, NICHT polished |
| **Beta** | Tuning-Phase | Alle bestehenden Systeme werden getuned — Performance-Optimierung, visuelle Feinheit, Accessibility vollständig |
| **Full Release** | Feinschliff + große Setpieces | Abschließende Lighting-Pass für alle Hauptorte, Cinematic-Sequenzen final |
| **DLC** | Erweiterung auf stabiler Basis | Neue Assets auf bestehenden Systemen — kein neues technisches Risiko in DLC-Phase |

**Alpha ist der härteste Freeze**: Nach Alpha-Abgabe sind folgende Systeme nicht mehr änderbar:
- Data Layer-Struktur (Schichtanzahl, Naming, Streaming-Logik)
- Lumen-Konfiguration (RT-Modus pro Layer)
- Schattenfieber-PP-System-Architektur (Blueprint-Struktur, Parameter-Namen)
- Schwellenanker-Master-Material-Struktur (Parameter-Gruppen, Slot-Namen)
- Kamerasystem-Grundstruktur
- **Interface-Spezifikation Lymph → PP-Trigger** (Funktionsnamen, Parameter-Typen, Event-Namen)

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
- Lymph-PP-Interface implementiert und mit Gameplay-Team getestet
- Schwellenanker-Master-Material (alle drei Zustände)
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
| Nervensystem Arm-Mesh | MITTEL | Hoher Animations-Aufwand im FP-Modus | Eigenständiger Task, 3-Wochen-Schätzung, eigenständige Asset-Klasse |
| Schwellenanker-Shader-Synchronität | NIEDRIG | State-Alpha-Drift zwischen Blueprint und Material | Interface-Konvention festgelegt, Parameternamen dokumentiert |
| Lymph-PP-Interface-Drift | NIEDRIG | Gameplay ändert Parameternamen nach Alpha-Freeze | Interface-Namen in 6.4.7 festgeschrieben, Alpha-Freeze gilt explizit |

---

\clearpage
