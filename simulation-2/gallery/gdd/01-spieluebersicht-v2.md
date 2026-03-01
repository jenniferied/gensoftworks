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
