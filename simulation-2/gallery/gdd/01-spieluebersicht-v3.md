# GDD Kapitel 01 — Spielübersicht & Design-Säulen

<!-- Darius: v3 — Kürzung für Seitenbudget (83→60 PDF-Seiten). Keine neuen Inhalte. Abschnitte gestrafft, Abgrenzungstabelle komprimiert, Tabelle 10 auf Kernfakten reduziert. Bilder von Pinnwand eingebaut. Orden-Symbol: SIEGEL (bestätigt, kein Kreuz). -->

---

## 1. Projekttitel & Format

**Serientitel:** RELICS
**Erste Iteration:** RELICS: Der Schwellenanker
**Format:** Single-Player Computer-Rollenspiel
**Perspektive:** Third-Person / First-Person, nahtlos umschaltbar
**Monetarisierung:** Premium — keine Mikrotransaktionen. Große DLCs nach Full Release.

---

## 2. High Concept Statement

RELICS fragt: *Wem gehört diese Welt — und was bist du bereit zu tun, um darin zu überleben?*

Du bist ein Fremder. Die Stadt vor dir funktioniert ohne dich — sie hat Regeln, Mächte, Hierarchien, die sich über Jahrhunderte eingeschliffen haben. Drei Fraktionen teilen die Welt: die Krone mit ihrem Militär und leeren Kassen, die Gilden mit ihren Monopolen, der Orden mit seinem Wissen und seiner Inquisition. Keine ist gut. Keine ist böse. Alle sind konsequent.

Und dann gibt es das Schattenfieber. Eine Seuche, die den Körper verändert. Jede Fraktion hat eine andere Erklärung — alle liegen falsch, aber jede liegt anders falsch. Unter der Stadt wartet der **Schwellenanker**: das, was die Grenze zwischen den Ebenen des Seins zusammenhält. Er schwächt sich ab. Das Fieber breitet sich aus.

Du wirst hineingezogen, ob du willst oder nicht. Was du daraus machst — das ist das Spiel.

---

## 3. Spieler-Fantasie-Statement

**"Ich betrete als Fremder eine aufregende Sandbox."** *(Briefing, unveränderlich)*

Drei konkrete Fantasien:

1. **Agentschaft:** Ich löse jedes Problem auf meine Weise — schleichen, kämpfen, verhandeln.
2. **Aufstieg:** Vom Eisengerät zu Titan-Legierungen. Mein Körper ist mein Fortschrittsanzeiger.
3. **Konsequenz:** Meine Entscheidungen formen die Welt. Wer für die Gilden arbeitet, dem verschließt der Orden Türen.

---

## 4. Game Feel

*Ich stehe am Rand einer lebendigen, gefährlichen Welt und spüre, dass meine nächste Entscheidung etwas verändert.*

- **Schwere.** Kämpfe kosten etwas. Schwerthieb fordert Kraft, Parade fordert Timing.
- **Reibung.** Die Stadt gibt sich nicht preis. Gilden-Tore sind gesperrt. Ordenswächter beobachten.
- **Staunen + Bedrohung.** Biolumineszenz in den Kanälen leuchtet schön — weil dort das Fieber am stärksten ist.
- **Dichte.** Jeder NPC hat eine Funktion, einen Tagesablauf. Niemand steht als Dekoration herum.

---

## 5. Genre & Perspektive

| Parameter | Wert |
|---|---|
| Genre | Action-RPG / Immersive Sim |
| Ton | Dark Fantasy — düster, geerdet, politisch |
| Setting | Medieval Cyberpunk: frühes Spätmittelalter + High-Tech-Materialien |
| Perspektive | Third-Person (Standard) / First-Person (umschaltbar) |
| Weltstruktur | Semi-Open-World: dichte, handgefertigte Kernregion |
| Kampf | Real-Time Action, Melee-fokussiert, gewichtig |
| Magie | Keine. Alchemie + Schattenfieber-Transformationen (je nach Körperreaktion) |
| Referenzen | Gothic 2, Deus Ex, VtM: Bloodlines, Prey 2017 |

Medium-Fantasy — Low-Magic, High-Tech. Biotech-Futurismus, der sich von innen wie Alchemie anfühlt.

---

## 6. Die vier Design-Säulen

Jedes Feature muss gegen mindestens zwei Säulen bestehen. Features, die keine stärken, werden gestrichen.

### Säule I — Immersive Simulation

*"Diese Welt reagiert auf mich. Ich bin nicht auf einem Schienen-Trip."*

Jedes Problem hat mehr als eine Lösung. NPCs verhalten sich nach eigener Logik. Verschlossene Türen bleiben verschlossen, bis der Spieler den Schlüssel hat, sie aufbricht oder einen anderen Eingang findet. Fraktionsentscheidungen haben echte systemische Konsequenzen. Mehrere Lösungswege entstehen aus dem Zusammenspiel von Fähigkeiten, Umgebung und Fraktionsstand.

**Referenz:** Warren Spector, Deus Ex GDD v5.3e: "The world simulation allows players to solve problems in a variety of ways."

### Säule II — Fraktionspolitik als Kernspannung

*"Ich wähle nicht die gute Fraktion. Ich wähle meine Fraktion."*

| Fraktion | Ressource | Gameplay-Zugang |
|---|---|---|
| **Die Krone** | Territorium, Militärpassagen, Rechtsstatus | Schutz, Bewegungsfreiheit, Ehrentitel |
| **Die Gilden** | Materialien, Handwerksrezepturen, Schwarzmarkt | Crafting-Tiefe, Upgrade-Pfade, Händler-Netzwerke |
| **Der Orden** | Wissen, Fertigkeitsbücher, Bildungsmonopol | Skill-Upgrades, Lore-Zugang, Heilkunde |

Fraktionsruf ist der Schlüssel zu konkreten Spielsystemen. Kein moralischer Zeigefinger.

![Fraktion Krone — Materialpalette](../../pinwall/favorites/fraktion-krone-materialpalette_seedream-4-5.png)

*Konzeptbild: Krone-Materialpalette — Titan-Legierungen, Edelstahl, Damaszener-Stahl. Militärischer Anspruch, leere Grandeur.*

![Fraktion Gilden — Materialpalette](../../pinwall/favorites/fraktion-gilden-materialpalette-v2_nano-banana-2.png)

*Konzeptbild: Gilden-Materialpalette — Erdtöne, Malachit, Bernstein, Bronzehammer. Material als Macht.*

![Fraktion Orden — Materialpalette](../../pinwall/favorites/fraktion-orden-materialpalette_seedream-4-5.png)

*Konzeptbild: Orden-Materialpalette — Indigo-Siegel, versiegelte Dokumente, blutroter Siegellack. Wissen als Kontrolle.*

### Säule III — Körperlicher Fortschritt

*"Mein Körper ist mein Fortschrittsanzeiger. Ich sehe, was ich trainiert habe — und was es mich gekostet hat."*

Nervensystem-Leveling ersetzt klassische Attribut-Grids. Drei Subsysteme (Cardio, Muskel, Lymph), vier Qualitätsstufen (Untrained / Geübt / Fortgeschritten / Meister). Skill-by-Use — keine Erfahrungspunkte. Das Schattenfieber als dritte Progressionsachse: Lymph-Subsystem koppelt an Fieber-Stadien. Transformation je nach Körperreaktion — kein Spieler durchläuft sie identisch.

**Referenz:** Warren Spector, Deus Ex GDD v5.3e: Skill-Granularität über vier Qualitätsstufen.

### Säule IV — Dichte vor Breite

*"Diese Welt existierte, bevor ich ankam. Sie wird nach mir weiterexistieren."*

**Schwarzrand** ist der Kern. Eine Stadt, vertikal geschichtet (Obere Ränder / Mittelwand / Schlund), dicht belebt. Jede Zone hat eigene Materialsprache, Architektur, NPC-Typen. NPCs haben Tagesabläufe. Kein Loot-Bloat — Damaszener-Stahl ist ein Ereignis.

**Der Gothic-Kontrast zu Skyrim:** Skyrim hat 300 Orte, Gothic 2 hat Khorinis — und Khorinis *lebt*. Das ist RELICS' Versprechen.

---

## 7. Tonalität

**Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.**

Die Welt ist dunkel, weil die Verhältnisse dunkel sind — nicht um des Grimdark willen. Das Schattenfieber ist das einzige Übernatürliche und wird nie trivialisiert.

- Oberschicht: All-Black, Monochrom — ein einzelner Neon-Akzent
- Unterschicht: Grau, Braun — gelegentlich ein gestohlenes Stück Farbe
- Biolumineszenz: schön und bedrohlich zugleich
- Kein Zahnrad. Keine Dampfmaschine. Keine Hexagone.

---

## 8. Zielgruppe

1. **Immersion-First Players** — Kingdom Come, Disco Elysium, Outer Wilds
2. **Faction Players** — VtM: Bloodlines, Fallout: New Vegas
3. **Crafting/Progression Freaks** — Dark Souls, Stardew Valley
4. **Medieval Aesthetics Obsessed** — Kingdom Come, Mount & Blade

**Kritisches Risiko:** Die erste Stunde ist kein Tutorial — sie ist ein Angebot. Minute fünfzehn muss vermitteln, was dieser Ort *ist*.

---

## 9. Abgrenzung

| RELICS IST | RELICS IST NICHT |
|---|---|
| Handgefertigte, dichte Welt | Leere Open World |
| Körperlicher Fortschritt sichtbar | Abstraktes Level-up |
| Drei Fraktionen ohne Moralkeulen | Gut gegen Böse |
| Schattenfieber als biologische Wahrheit | Magiesystem mit Label |
| Medieval Cyberpunk: Material als Macht | Steampunk / High Fantasy |
| Immersive Sim: mehrere Lösungswege | Schienenspiel |

---

## 10. Geklärte Design-Fragen

| # | Frage | Antwort |
|---|---|---|
| 1 | Schauplatz | EINE vertikale Stadt: **Schwarzrand** (Felssporn, drei Zonen) |
| 2 | Schattenfieber-Scope | Hauptquest + dritte Progressionsachse. Transformation je nach Körperreaktion. |
| 3 | Tiervolk | Kosmologisch-fremde Wesen in dauerhafter Symbiose mit Tieren. NPC-Händler, nicht spielbar. |
| 4 | Release-Modell | Streamer-Alpha → Beta (6–12 Mo.) → Full Release → große DLCs |
| 5 | Relikt-Name | **Der Schwellenanker** — CD-bestätigt. Fragment beim Spieler. |
| 6 | Ablehn-Option | Ja — Spieler darf Fragment ablehnen. Echte Verzweigung (→ Kap. 3). |

<!-- Darius: Alle Design-Fragen geschlossen. Orden-Symbol = SIEGEL (nicht Kreuz) — in allen Texten durchgängig korrekt. Fantasie-Spalte aus Fraktionstabelle entfernt für Kürze — lebt in Kap. 2 weiter. -->
