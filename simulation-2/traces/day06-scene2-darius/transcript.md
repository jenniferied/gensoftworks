# Transcript: day06-scene2-darius

Session: `f60913e6-d4f4-46b4-8c59-e741946d1e39`
Source: `agent-a866bae82877393aa.jsonl`
Entries: 41
Start: 2026-02-28T00:36:14.137Z
End: 2026-02-28T00:43:59.091Z

---

---
### USER PROMPT [00:36:14]

Du bist Darius Engel, Game Director & Lead Designer bei GenSoftworks. Es ist Tag 6 (Montag), Szene 2 (WORK), 10:00 Uhr.

Schreibe echte deutsche Umlaute (ä, ö, ü, ß), NICHT ae, oe, ue, ss.

## Deine Aufgabe

Lies die aktuelle GDD-02 Kernmechaniken V1 und schreibe eine aktualisierte V2. Die V1 liegt unter:
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/02-kernmechaniken-v1.md

## Was in V2 rein muss

1. **Namenssystem** durchgehend: Emer statt Ymir, Große Flechtung statt Ur-Bindung
2. **Stufengrenzen** auf CD-Tabelle: Rauschen 1-40, Risse 41-75, Schwelle 76-100, Halluzinations-Start 76
3. **Waffenklassen** für Vertical Slice festzurren: 3-4 Nahkampf + Bogen
4. **Suchtmechanik** bei Alchemie-Buffs (Drogen, Amphetamine — kein Bestrafungsspirale)
5. **Nervensystem-Äste** mit kosmologischem Einzeiler (Namis Punkt)
6. **Kontrollverlust** = narrativ (Wahrnehmung unzuverlässig, Steuerung bleibt)
7. **Schatten-Ast** als eigener Abschnitt
8. **Trainer** als Fraktions-Erzähler
9. **Maret als optionaler Kompanion** — Schattenfieber-Spiegel

## Format

YAML-Frontmatter:
```
---
dokument: GDD-02
titel: Kernmechaniken
version: 2
autor: Darius Engel
status: Entwurf
datum: "Tag 6, Montag"
querverweise: ["GDD-01", "GDD-03", "GDD-05", "GDD-06", "WBB-01"]
---
```

Lies zuerst die V1, dann schreibe die V2 als Update. Datei speichern unter:
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/02-kernmechaniken-v2.md


**ASSISTANT** [00:36:16]:
Ich lese zuerst die V1 und relevante Referenzdokumente.


**TOOL: Read** [00:36:16] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/02-kernmechaniken-v1.md`


**RESULT** [00:36:16]:
```
     1→# GDD-02: Kernmechaniken
     2→
     3→**Autor:** Darius Engel, Game Director
     4→**QA:** Leo Brandt (Spielermarkt & Community)
     5→**Narrativ-Sync:** Nami Osei (Erzählkonzept)
     6→**Version:** V0.5 (Tag 2, Dienstag — Nachmittags-Überarbeitung)
     7→**Status:** Zwischen Outline und V1 — Strukturen stehen, Schlüsselabschnitte angereichert, offene Fragen reduziert
     8→**Änderungslog:**
     9→- V1-Outline (Tag 2 Vormittag): Kapitelstruktur + Kernpunkte
    10→- V0.5 (Tag 2 Nachmittag): Leos QA-Bedingungen integriert, Schattenfieber-Stufen-Mapping mit Nami synchronisiert, CD-Entscheidungen eingearbeitet (Tod/Infektion, Lebende Krone, Namenssysteme, Combat-Skill-Ceiling)
    11→- V0.5.1 (Tag 5 Nachmittag): Arbeitsbegriff "Ymir" → "Emer" (2x: Kap. 2.7, Kap. 6.1) — Leo Fischer, QA
    12→
    13→---
    14→
    15→## 1. Combat-System
    16→
    17→### 1.1 Grundphilosophie
    18→- Real-time Action, Melee-fokussiert, gewichtig
    19→- KEIN Difficulty Slider — die Welt bestimmt die Schwierigkeit (Gothic-Prinzip)
    20→- Skill-Ceiling als Spektrum (CD-bestätigt): Einstieg intuitiv, Mastery belohnend — nie erzwungen
    21→- Jeder Kampf soll sich BEDEUTSAM anfühlen — keine Trash-Mobs, kein Grind
    22→- Spieler-Fantasie: "Ich habe diesen Kampf gewonnen, weil ich besser geworden bin — nicht weil ich Level 50 bin."
    23→
    24→**Skill-Ceiling-Spektrum (Detail):**
    25→Das System muss auf BEIDEN Enden des Spektrums funktionieren. Ein Spieler, der nur Basisaktionen nutzt, soll jede Begegnung bestehen können (mit Vorbereitung und Geduld). Ein Spieler, der Cancel-Windows und Setup-Plays beherrscht, soll sich belohnt fühlen (schnellere Kills, elegantere Lösungen, optionale Herausforderungen). Kein Spieler soll das Gefühl haben, er müsste Mastery-Techniken lernen, um weiterzukommen. Aber jeder Spieler soll sehen KÖNNEN, was möglich wäre.
    26→
    27→### 1.2 Kampfschichten (drei Ebenen)
    28→
    29→#### Ebene 1 — Basis (sofort zugänglich)
    30→- 
... [truncated]
```


**TOOL: Read** [00:36:17] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/01-spieluebersicht-v1.md`


**ERROR** [00:36:17]:
```
File does not exist. Note: your current working directory is /Users/jennifer/Documents/GitHub/gensoftworks.
```


**TOOL: Read** [00:36:17] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/briefing.md`


**ERROR** [00:36:17]:
```
<tool_use_error>Sibling tool call errored</tool_use_error>
```


**ASSISTANT** [00:36:20]:
Gut, die V1 ist gelesen. Jetzt hole ich mir die restlichen Referenzdokumente.


**TOOL: Glob** [00:36:21] → `simulation-2-test/gallery/gdd/01-*`


**RESULT** [00:36:21]:
```
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/01-spieluebersicht-v2.md
```


**TOOL: Read** [00:36:21] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/briefing.md`


**RESULT** [00:36:21]:
```
     1→# RELICS — Creative Director's Briefing
     2→
     3→> **NORDSTERN** — Dieses Dokument ist die unveränderliche kreative Vision. Alle Artefakte (Game Design Document, World Building Bible, Concept Art) müssen sich an diesem Briefing orientieren. Abweichungen nur mit expliziter Creative Director-Freigabe.
     4→> Immer fragen statt erfinden, wenn unklar.
     5→
     6→## Vision
     7→
     8→RELICS ist der Titel einer Fantasy-Computerrollenspiel-Serie.
     9→
    10→RELICS spielt in einer **in sich konsistenten Welt**, jeweils zu einem historischen Wendepunkt, in dem ein bestimmtes **Relikt** eine Schlüsselrolle spielt.
    11→
    12→Das Namensformat jeder Iteration ist: RELICS: *Relikt-Name*
    13→
    14→Der **Spielercharakter** ist bei jeder Iteration ein Unbekannter, der auf mysteriöse Art und Weise in die Handlung eingewickelt wird. Niemals ein spezifischer Charakter.
    15→
    16→Zu Beginn des Spieles erstellt man seinen eigenen **Spielercharakter**.
    17→
    18→**Tonalität:** Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.
    19→
    20→## Game Feel
    21→
    22→Ich betrete als Fremder eine aufregende "Sandbox".
    23→
    24→## Verbindliche Ausschlüsse
    25→
    26→- **KEIN** Steampunk (keine Dampfmaschinen, keine Zahnrad-Ästhetik)
    27→- **KEIN** High Fantasy (keine Elfen, keine Orks, keine Zauberer mit Stäben)
    28→- **KEIN** Science-Fantasy (keine vergessene Hochtechnologie, keine Alien-Artefakte)
    29→- **KEINE** Anachronismen (kein Schießpulver, kein Buchdruck, keine mechanischen Uhren außer Gilden-Prototypen)
    30→- **KEINE** klassische Magie.
    31→
    32→## Genre
    33→
    34→**Third-/First-Person** — nahtlos umschaltbar (Skyrim-Referenz)
    35→**Open-World/Semi-Open-World**
    36→"Medium"-Fantasy – es liegt auf dem Spektrum zwischen Low-Fantasy und High-Fantasy
    37→Low-Magic, High-Tech
    38→Biotech-Futurismus
    39→**KEIN** Steampunk
    40→
    41→## Die Welt
    42→
    43→Ein we
... [truncated]
```


**TOOL: Glob** [00:36:22] → `simulation-2-test/gallery/wbb/01-*`


**RESULT** [00:36:22]:
```
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/wbb/01-mythos-v2.md
```


**TOOL: Read** [00:36:23] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/agents/darius-memory.md`


**RESULT** [00:36:23]:
```
     1→# Darius — Memory
     2→
     3→<!-- GM aktualisiert diese Datei nach jeder Szene aus Darius' Perspektive -->
     4→
     5→## Tag 1, Szene 1 (BRIEFING)
     6→Erster Tag. Finn macht das Briefing sauber. CD will Referenzspiel-Analyse. Gothic, Skyrim, Dishonored als Hauptreferenzen. Leo soll Avowed und Gothic Remake mit abdecken.
     7→
     8→## Tag 1, Szene 2 (WORK)
     9→Strukturierte Analyse entlang sechs Design Pillars fertig. RELICS' größter Design-Hebel: Open World mit Dishonored-Vertikalität + Gothic-Dichte. Gothic 2 ist Goldstandard für Weltdichte und Fraktionsdesign. Skyrim liefert Kamera-Flexibilität, aber Combat und Radiant Quests sind Anti-Referenzen. Fünf offene Fragen für den Standup vorbereitet.
    10→
    11→## Tag 1, Szene 3 (MEETING)
    12→Standup. CD bestätigt Semi-Open-World (Gothic-Dichte), TP als Primärmodus, Ü5. Schattenfieber-Infektion für den Spieler bestätigt — mit Kosten und Nutzen. Das ist ein Core System, das ich designen muss. Combat-Skill-Ceiling offen für morgen. Nami und Emre klären Wanderer-Motiv bilateral. Leos Pitch-Satz ist stark.
    13→
    14→## Tag 1, Szene 5 (WORK)
    15→Schattenfieber-Konzept ausgearbeitet: Infektionswert 0-100, fünf Stufen, vierter Ast im Nervensystem-Leveling. Fünf Design-Prinzipien (Spektrum statt Schalter, Nutzen attraktiv, Kosten verändern nicht blockieren, Welt reagiert, Integration ins Kernsystem). Fünf emergente Build-Archetypen. Bloodborne Insight + VtM Bloodlines als Goldstandards. Skyrim-Vampirismus als Anti-Referenz.
    16→
    17→## Tag 1, Szene 6 (REVIEW)
    18→CD: Schattenfieber nicht heilbar, nur kontrollierbar — gut so. PC first, Konsolen als Stretch Goal. Freelancer-Budget für Gameplay-Programmer genehmigt. Tiervolk = Nomaden ohne eigene Architektur. Replay-Erfahrung gewollt. Morgen: Combat-Skill-Ceiling klären, Schattenfieber-Konzept mit Nami synchronisieren.
    19→
    20→## Tag 2, Szene 1 (BRIEFING)
    21→Konzeptionstag. GDD-01 Spielübersicht und GDD-02 Kernmechaniken 
... [truncated]
```


**TOOL: Read** [00:36:25] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/01-spieluebersicht-v2.md`


**RESULT** [00:36:25]:
```
     1→# GDD-01: Spielübersicht & Design-Säulen
     2→
     3→**Autor:** Darius Engel, Game Director
     4→**Version:** V2 (Tag 5, Freitag — Finalisierung)
     5→**Status:** Abgeschlossen
     6→**Änderungslog:**
     7→- V1 (Tag 3, Mittwoch): Volltext — Elevator Pitch, 6 Design-Säulen, 3 USPs, Zielgruppe, 1h/10h/40h-Prinzip, Referenzrahmen
     8→- V2 (Tag 5, Freitag): Scope-Klarheit (Serie vs. Vertical Slice), Zielgruppe 25-40 präzisiert, Kamera als eigene Design-Säule ergänzt, Tiervolk+Biotech als Weltsprache geschärft, Konsequenz-Versprechen durch Typ-Matrix operationalisiert
     9→
    10→**Querverweise:** `02-kernmechaniken.md` (V2, vollständig), `briefing.md` (Nordstern)
    11→
    12→---
    13→
    14→## 0. Schnellorientierung
    15→
    16→> Wer nur einen Absatz liest, soll dieser sein.
    17→
    18→RELICS: *[Iterations-Titel]* ist ein Dark-Fantasy-Action-RPG. Der Spieler betritt als Fremder eine dichte, handgefertigte Welt am Rand des Zusammenbruchs — drei Fraktionen ohne klare Moral, eine biologische Infektion als Progressionssystem, ein Relikt, das alle haben wollen. Entscheidungen bleiben. Die Welt erinnert sich. Wer das Schattenfieber nutzt, verändert seinen Körper dauerhaft.
    19→
    20→**Tonalität:** Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.
    21→**Referenzrahmen:** Gothic 2 (Dichte, Welt-Reaktivität), Skyrim (Kamera, Zugänglichkeit), Bloodborne (Transformationsmechanik), Dishonored (Vertikalität).
    22→
    23→---
    24→
    25→## 1. Elevator Pitch
    26→
    27→**RELICS: *[Iterations-Titel]*** ist ein Dark-Fantasy-Action-RPG in einer handgemachten Semi-Open-World. Der Spieler betritt als namenloser Fremder eine mittelalterliche Gesellschaft am Wendepunkt: Drei Fraktionen ringen um die Macht, eine biologische Seuche — das Schattenfieber — verwandelt die Bevölkerung, und im Zentrum des Konflikts liegt ein organisches Artefakt, das alle drei Fraktionen für sich beanspruchen.
    28→
    29→RELICS ist ke
... [truncated]
```


**TOOL: Read** [00:36:26] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/wbb/01-mythos-v2.md`


**RESULT** [00:36:26]:
```
<persisted-output>
Output too large (54.5KB). Full output saved to: /Users/jennifer/.claude/projects/-Users-jennifer-Documents-GitHub-gensoftworks/f60913e6-d4f4-46b4-8c59-e741946d1e39/tool-results/toolu_01UFkxHAd8v3C6E38sFMQyQo.txt

Preview (first 2KB):
     1→# WBB-01 MYTHOS — V2
     2→
     3→**Autor**: Emre Yilmaz, Lead Worldbuilder
     4→**Stand**: Tag 5 (Freitag), Vormittag — Produktionsphase
     5→**Status**: V2 — Alle Kapitel Fliesstext. Kap. 5-8 ausformuliert. V2-Updates (Tag 4) integriert.
     6→**Basis**: Klastrup/Tosca (2004) — Mythos als "backstory" der transmedialen Welt
     7→**Prüfung gegen**: Wolf (2013) — Infrastrukturen Mythologie, Zeitleisten, Genealogien, Philosophie
     8→
     9→---
    10→
    11→## Kosmologisches Lexikon
    12→
    13→> Alle nordischen Begriffe dienen als **Entwickler-Referenz**. In der Spielwelt existieren ausschliesslich die RELICS-eigenen Bezeichnungen. Die Namen sind aus germanischen Wurzeln (urgermanisch, althochdeutsch, gotisch) abgeleitet — sie klingen verwandt, sind aber eigenständig.
    14→
    15→| RELICS-Begriff | Bedeutung | Herleitung | Nordische Referenz |
    16→|---|---|---|---|
    17→| **Galt** | Die Urleere. Zustand vor aller Differenzierung | urgerm. *gal- (leer, öd) | Ginnungagap |
    18→| **die Galtung** | Gelehrter Ordensterm für die Urleere | *gal- + *-ung (Zustand) | — |
    19→| **Emer** | Das Urwesen, dessen Körper zur Welt wurde | urgerm. *aima- (Strom, Rauschen); ahd. *emizzig (unaufhörlich) | Ymir |
    20→| **der Tharm** | Gilden-Name für die Welt-als-Körper | ahd. *tharm (Eingeweide) | — |
    21→| **Hohlicht** | Obere Schicht. Erhöhte Wahrnehmung. Vergessener Zustand | ahd. *hoh (hoch) + *lioht (Licht) | Asgard / obere Welten |
    22→| **Mittelgrund** | Mittlere Schicht. Die bewohnte Welt | Bewusst schlicht. "Der Grund" | Midgard |
    23→| **Stillfeld** | Untere Schicht. Ort der Stille, des Vergessens, der Auflösung | ahd. *stilli + *feld | Hel / Niflheim |
    24→| **die Hauten** |
... [truncated]
```


**TOOL: Read** [00:36:27] → `/Users/jennifer/Documents/GitHub/gensoftworks/roster/darius-engel.md`


**ERROR** [00:36:27]:
```
File does not exist. Note: your current working directory is /Users/jennifer/Documents/GitHub/gensoftworks.
```


**TOOL: Glob** [00:36:30] → `simulation-2*/roster/darius-engel.md`


**RESULT** [00:36:30]:
```
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/roster/darius-engel.md
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/roster/darius-engel.md
```


**TOOL: Read** [00:36:31] → `/Users/jennifer/.claude/projects/-Users-jennifer-Documents-GitHub-gensoftworks/f60913e6-d4f4-46b4-8c59-e741946d1e39/tool-results/toolu_01UFkxHAd8v3C6E38sFMQyQo.txt`


**RESULT** [00:36:31]:
```
     1→     1→# WBB-01 MYTHOS — V2
     2→     2→
     3→     3→**Autor**: Emre Yilmaz, Lead Worldbuilder
     4→     4→**Stand**: Tag 5 (Freitag), Vormittag — Produktionsphase
     5→     5→**Status**: V2 — Alle Kapitel Fliesstext. Kap. 5-8 ausformuliert. V2-Updates (Tag 4) integriert.
     6→     6→**Basis**: Klastrup/Tosca (2004) — Mythos als "backstory" der transmedialen Welt
     7→     7→**Prüfung gegen**: Wolf (2013) — Infrastrukturen Mythologie, Zeitleisten, Genealogien, Philosophie
     8→     8→
     9→     9→---
    10→    10→
    11→    11→## Kosmologisches Lexikon
    12→    12→
    13→    13→> Alle nordischen Begriffe dienen als **Entwickler-Referenz**. In der Spielwelt existieren ausschliesslich die RELICS-eigenen Bezeichnungen. Die Namen sind aus germanischen Wurzeln (urgermanisch, althochdeutsch, gotisch) abgeleitet — sie klingen verwandt, sind aber eigenständig.
    14→    14→
    15→    15→| RELICS-Begriff | Bedeutung | Herleitung | Nordische Referenz |
    16→    16→|---|---|---|---|
    17→    17→| **Galt** | Die Urleere. Zustand vor aller Differenzierung | urgerm. *gal- (leer, öd) | Ginnungagap |
    18→    18→| **die Galtung** | Gelehrter Ordensterm für die Urleere | *gal- + *-ung (Zustand) | — |
    19→    19→| **Emer** | Das Urwesen, dessen Körper zur Welt wurde | urgerm. *aima- (Strom, Rauschen); ahd. *emizzig (unaufhörlich) | Ymir |
    20→    20→| **der Tharm** | Gilden-Name für die Welt-als-Körper | ahd. *tharm (Eingeweide) | — |
    21→    21→| **Hohlicht** | Obere Schicht. Erhöhte Wahrnehmung. Vergessener Zustand | ahd. *hoh (hoch) + *lioht (Licht) | Asgard / obere Welten |
    22→    22→| **Mittelgrund** | Mittlere Schicht. Die bewohnte Welt | Bewusst schlicht. "Der Grund" | Midgard |
    23→    23→| **Stillfeld** | Untere Schicht. Ort der Stille, des Vergessens, der Auflösung | ahd. *stilli + *feld | Hel / Niflheim |
    24→    24→| **die Hauten** | Membranen zwischen den Schichten | Plural von Haut — organische Trennschicht | — |
  
... [truncated]
```


**ASSISTANT** [00:36:38]:
Gut, ich habe jetzt alle Referenzdokumente gelesen. Ich habe die V1 des GDD-02 vollständig, die GDD-01 V2, die WBB-01 V2 mit dem Kosmologischen Lexikon (Emer, Große Flechtung, Flechtung, etc.), das Briefing und Darius' Memory. Jetzt schreibe ich die V2.


**TOOL: Write** [00:43:27] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/02-kernmechaniken-v2.md`
```
---
dokument: GDD-02
titel: Kernmechaniken
version: 2
autor: Darius Engel
status: Entwurf
datum: "Tag 6, Montag"
querverweise: ["GDD-01", "GDD-03", "GDD-05", "GDD-06", "WBB-01"]
---

# GDD-02: Kernmechaniken

**Autor:** Darius Engel, Game Director
**QA:** Leo Brandt (Spielermarkt & Community)
**Narrativ-Sync:** Nami Osei (Erzählkonzept)
**Version:** V2 (Tag 6, Montag — Verlängerungstag)
**Status:** Entwurf
**Änderungslog:**
- V1/V0.5 (Tag 2-3): Kapitelstruktur, Kernpunkte, QA-Bedingungen, Stufen
... [truncated]
```


**RESULT** [00:43:27]:
```
File created successfully at: /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/02-kernmechaniken-v2.md
```


**ASSISTANT** [00:43:59]:
Die V2 ist geschrieben und gespeichert. Hier die Zusammenfassung meiner Arbeit.

---

**Datei:** `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/02-kernmechaniken-v2.md`

**Alle neun Aufgabenpunkte sind umgesetzt:**

1. **Namenssystem durchgehend:** Ymir ist komplett durch **Emer** ersetzt, Ur-Bindung durch **Große Flechtung**. Abschnitt 6.1 enthält eine Mapping-Tabelle (alter Begriff / RELICS-Begriff) mit allen relevanten Termen aus dem WBB-01 Kosmologischen Lexikon (Hauten, Hohlicht/Mittelgrund/Stillfeld, Faulung/Schwund/Entflechtung). Die Fraktions-Interpretationen der Lebenden Krone in 2.8 nutzen jetzt Sigvalt, Tharm und Halvard korrekt.

2. **Stufengrenzen auf CD-Tabelle:** Die fünf mechanischen Stufen aus V1 sind durch das **Drei-Zonen-Modell** ersetzt: Rauschen 1-40, Risse 41-75, Schwelle 76-100, Halluzinations-Start bei 76. Abschnitt 2.3 enthält die vollständige Tabelle mit Früh/Mitte/Spät-Aufschlüsselung pro Zone.

3. **Waffenklassen festgezurrt:** Abschnitt 1.3 definiert **4 Nahkampf + Bogen** als Vertical-Slice-Scope: Einhandschwert (Krone), Zweihandschwert (Krone-Elite), Dolche (Gilden/Tiervolk), Einhandaxt (Orden), Bogen (Gilden-Jagd). Äxte (Zweihand), Hämmer, Armbrüste und Schilde als expliziter Erweiterungspool.

4. **Suchtmechanik:** Neuer Abschnitt 4.3 -- Gewöhnung statt Entzug. Drei Konsumstufen (gelegentlich/regelmäßig/exzessiv) mit steigenden Materialkosten und temporären Nacheffekten. Klare Abgrenzung: KEINE permanente Stat-Reduktion, KEINE Bestrafungsspirale, KEIN Entzugs-Debuff. Transparenz via Tooltip. Interaktion mit Schattenfieber (höhere Grundtoleranz bei Infizierten).

5. **Nervensystem-Äste mit kosmologischem Einzeiler:** Jeder Ast in 3.2 hat jetzt einen kursiven Einzeiler, der ihn in der Emer-Kosmologie verankert. Plus: Kosmologische Verankerung in 3.1 als Designleitlinie (der Spielercharakter IST Emer-Material).

6. **Kontrollverlust = narrativ:** Neuer Abschnitt 2.6 definiert Kontrollverlust als Wahrnehmungsverschiebung, nicht als Input-Verlust. Steuerung bleibt IMMER beim Spieler. Die Welt wird unzuverlässig, nicht der Controller. Mit Trigger-Regeln, Dauer, Frequenz und QA-Absicherung gegen Bedingung 3.

7. **Schatten-Ast als eigener Abschnitt:** Neuer Abschnitt 3.5 mit Zugangsmechanik, Ressourcenkonkurrenz (gleicher Punktepool), Interaktionsmatrix mit konventionellen Ästen, Fähigkeiten-Progressionstabelle (Stufe 1-12 gegen Infektionswert), visueller Darstellung und kosmologischer Verankerung (Emer-Resonanz).

8. **Trainer als Fraktions-Erzähler:** Abschnitt 3.3 erweitert. Trainer erklären Fähigkeiten im Kontext ihrer Fraktion. Dieselbe Fähigkeit funktioniert bei verschiedenen Fraktionen leicht anders (nicht stärker -- anders). Trainer-Typen-Tabelle mit Krone/Gilden/Orden/Tiervolk, exklusiven Fähigkeiten und Erzähltonalität.

9. **Maret als optionaler Kompanion:** Neuer Abschnitt 2.10 definiert Maret als narrative Spielmechanik -- wandelnder Schattenfieber-Spiegel, keine BioWare-Begleiterin. Mechanische Funktion für Stufe-0-Spieler (Vorschau) und Infizierte (Vergleichspunkt). Fraktionslos, optional, in Zone Schwelle als Halluzinations-Unsicherheitsfaktor. Cassius bleibt stationär.
