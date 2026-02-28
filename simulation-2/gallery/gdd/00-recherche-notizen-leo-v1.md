# RELICS: Spieler-Analyse & Community Research
**Leo Fischer | QA Lead | Tag 1, Szene 2**

## Die Frage
Wer spielt RELICS? Welche Communities würden das anfeuern? Und wo liegen die Fallstricke?

---

## Zielgruppe — Overlapping Circles

RELICS spricht folgende Spielertypen an:

### 1. **Immersion-First Players** (Disco Elysium, Outer Wilds, Kingdom Come Deliverance)
- Wollen sich in eine Welt **verlaufen**, nicht geklopft werden
- Lieben Dark Fantasy mit Zähnen (Elden Ring für Story-Hasser ist hier NICHT das Vorbild — sondern Hollow Knight)
- Fordern: Welt-Kohärenz, Keine Handholding, "Feeling" vor Tutorial
- Risk: Unsere erste Stunde muss knallhart geerdet sein

### 2. **Faction Player** (Baldur's Gate, Vampires the Masquerade: Bloodlines, New Vegas)
- "Ich wähle NICHT die gute Fraktion" ist ihr Satz
- Wollen Krone vs. Gilden vs. Orden spielen, ohne moralischen Zeigefinger
- Fordern: Faction-Quests, die nicht Gut/Böse sondern pragmatisch sind
- Risk: Wenn alle drei Fraktionen gleich mächtig sind, kann es sich zu "Middling" anfühlen

### 3. **Crafting/Progression Freaks** (Dark Souls, Hades, Stardew)
- Lieben sichtbare Materialsprache (das Briefing: Material = Status)
- Wollen Schwerter, die AUSSEHEN wie Schmiede-Gilde vs. Orden-Protottypen
- Fordern: Crafting-Tiefe, Upgrade-Sichtbarkeit, Materialknappheit
- Risk: Wenn wir zu viele Loot-Drops machen, wird es bloat

### 4. **Medieval Aesthetics Obsessed** (Mount & Blade, Kingdom Come)
- Lieben realistische Rüstung, Handwerk, kein Fantasy-Kitsch
- Cyberpunk-Elemente könnte sie ABSCHRECKEN, wenn es Steampunk riecht
- Fordern: Echte mittelalterliche Logik + "Tech als Geheimnis" statt sichtbar
- Risk: Biotech muss sich wie **Alchemie** anfühlen, nicht wie Sci-Fi

---

## Konkurrenzvergleich — Was sichert unser Territory?

| Spiel | Stärke | Schwäche | RELICS kann hier siegen |
|-------|--------|----------|------------------------|
| **Kingdom Come: Deliverance** | Immersion, Realismus | Langweilig, Missionen sind fetch-quests | Faction-Drama, Material-Upgrade-Sichtbarkeit |
| **Skyrim** | Open World, Vielfalt | Oberflächlich, Fraktionen sind austauschbar | Erde, politische Tiefe, Material-Bedeutung |
| **Elden Ring** | Combat, Mystery | Unzusammenhängend, Story ist optional | Narrative Tiefe, Klare Quest-Struktur |
| **Baldur's Gate 3** | Fraktionsgameplay, Verzweigung | Rundenbasiert, Team-RPG, zu viel Erzählung | Real-time, Solo-Agentschaft, Handwerk |
| **Cyberpunk 2077** | Ästhetik, Fraktionen | Spielwelt fühlt sich leblos an | Medieval = weniger "Simulationslast" |

---

## Kritische Risiken aus Spielersicht

### 1. **Medieval Cyberpunk = Identitätskrise**
Wenn es nach zwei Stunden unklar ist, ob das "Fantasy mit Tech-Flavor" oder "Cyberpunk mit Pferd" ist, springt Chat ab. Das Briefing sagt: **Material = Macht**. Das ist das Unterscheidungsmerkmal.

**Test-Kriterie:** Eine Waffe aus der Schmiede-Gilde vs. Orden sieht SOFORT anders aus. Nicht "Ordnung vs. Chaos", sondern "Legierung vs. Biotech".

### 2. **Die erste Stunde wird zum Gatekeep**
Spieler von Disco Elysium wollen keine 20-Minuten-Dialoge bei der Character-Creation. Spieler von KCD wollen rein. **Wir können nicht beide bedienen.**

**Angebot:** Tutorial-Quest, die *spielt* statt erklärt. Du wachst auf, kennst dein Handwerk nicht, musst dich beweisen. Die Welt antwortet auf deine Wahl sofort.

### 3. **Schattenfieber ist das Eisen auf der Map**
Das ist unsere "Magie ohne Magie"-Lösung. Wenn es mystisch wirkt statt biologisch, fühlt es sich wie Betrug an. Spieler merken sofort: "Das ist doch nur Magie mit anderm Namen."

**Test-Kriterie:** Schattenfieber muss sichtbar, körperlich, mit Kosten sein. Ein Spieler, der sich damit erweitert, wird GEZEICHNET. Nicht "Superkraft", sondern "Infiziert".

### 4. **Faction-Gleichgewicht ist zerbrechlich**
Krone + Gilden + Orden = drei Pole. Aber wenn zwei davon sich gegen eins verbünden, kollabiert die Spiel-Wahrheit. **Asymmetrie ist okay**, aber die Spieler müssen verstehen, warum jede Fraktion für jemanden attraktiv ist.

- Krone: Tradition, Militär, Ehre (für Cliché-Hater riskant)
- Gilden: Geld, Macht, Autonomie (für Anarchists)
- Orden: Wissen, Kontrolle, Sicherheit (für Authoritarians)

---

## Community-Radar

### Communities die RELICS lieben würden:
- /r/elderscrolls (wenn wir Open-World-Feeling liefern)
- /r/darksouls (Immersion, Material-Bedeutung)
- /r/kingdomcome (Realismus, aber fantasy-erlaubt)
- /r/Bloodborne (Gothic, Geerdet, Kämpfe mit Gewicht)
- /r/HollowKnight (Dichte statt Breite)

### Communities die sauer wären:
- Skyrim-Puristen ("Was ist dieses Cyberpunk-Zeug?")
- Cyberpunk-Fans ("Warum habt ihr mein Neon genommen?")
- Turnip-Boy-Casual-Players ("Zu düster, zu viel Mathmachiniken")

---

## Fazit für GDD Kapitel 2 (Kernmechaniken)

**Die erste halbe Stunde ist nicht Tutorial. Sie ist Angebot.**

Du wachst auf. Du kennst dein Handwerk nicht. Ein NPC braucht einen beschädigten Dolch repariert. Du hast zwei Wege: Schmiede-Gilde aufsuchen (Schulden) oder im Schwarzmarkt wild herumfummeln (Risiko). Beide Optionen sind spielbar.

In dieser halben Stunde lernt der Spieler:
- Das Gefühl von Material-Klasse (Gold Delaine vs. Tiegelstahl fühlt sich unterschiedlich an)
- Dass Welt-NPCs nicht warten (Krone patrouilliert, Orden späht, Gilden verhandeln)
- Dass Schattenfieber eine Bedrohung IST, nicht eine Quest-Lore-Notiz

Das ist der Spieler-Hook. Nicht Story. **Agentschaft.**
