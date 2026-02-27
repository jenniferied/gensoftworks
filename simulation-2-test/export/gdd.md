---
title: "RELICS — Game Design Document"
author: "GenSoftworks Studio Simulation"
date: "2026"
lang: german
toc: true
---

# GDD-01: Spielübersicht & Design-Säulen

**Autor:** Darius Engel, Game Director
**Version:** V2 (Tag 5, Freitag — Finalisierung)
**Status:** Abgeschlossen
**Änderungslog:**
- V1 (Tag 3, Mittwoch): Volltext — Elevator Pitch, 6 Design-Säulen, 3 USPs, Zielgruppe, 1h/10h/40h-Prinzip, Referenzrahmen
- V2 (Tag 5, Freitag): Scope-Klarheit (Serie vs. Vertical Slice), Zielgruppe 25-40 präzisiert, Kamera als eigene Design-Säule ergänzt, Tiervolk+Biotech als Weltsprache geschärft, Konsequenz-Versprechen durch Typ-Matrix operationalisiert

**Querverweise:** `02-kernmechaniken.md` (V2, vollständig), `briefing.md` (Nordstern)

---

## 0. Schnellorientierung

> Wer nur einen Absatz liest, soll dieser sein.

RELICS: *[Iterations-Titel]* ist ein Dark-Fantasy-Action-RPG. Der Spieler betritt als Fremder eine dichte, handgefertigte Welt am Rand des Zusammenbruchs — drei Fraktionen ohne klare Moral, eine biologische Infektion als Progressionssystem, ein Relikt, das alle haben wollen. Entscheidungen bleiben. Die Welt erinnert sich. Wer das Schattenfieber nutzt, verändert seinen Körper dauerhaft.

**Tonalität:** Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.
**Referenzrahmen:** Gothic 2 (Dichte, Welt-Reaktivität), Skyrim (Kamera, Zugänglichkeit), Bloodborne (Transformationsmechanik), Dishonored (Vertikalität).

---

## 1. Elevator Pitch

**RELICS: *[Iterations-Titel]*** ist ein Dark-Fantasy-Action-RPG in einer handgemachten Semi-Open-World. Der Spieler betritt als namenloser Fremder eine mittelalterliche Gesellschaft am Wendepunkt: Drei Fraktionen ringen um die Macht, eine biologische Seuche — das Schattenfieber — verwandelt die Bevölkerung, und im Zentrum des Konflikts liegt ein organisches Artefakt, das alle drei Fraktionen für sich beanspruchen.

RELICS ist kein Spiel über Auserwählte und Prophezeiungen. Es ist ein Spiel über Machterwerb in einer Welt, die sich nicht dafür interessiert, ob der Spieler überlebt. Keine Magie, keine Elfen, keine vorbestimmte Heldenreise. Stattdessen: Biotech-Alchemie, körperliche Progression durch ein physiologisches Nervensystem-Leveling und eine Seuche, die dem Spieler übermenschliche Fähigkeiten bietet — wenn er bereit ist, den Preis dafür zu zahlen.

Die zentrale Spieler-Fantasie lautet: **Ich betrete als Fremder eine aufregende Sandbox.** Eine Welt, die existiert, bevor der Spieler sie betritt, und die weiterexistiert, wenn er sie verlässt. Eine Welt, in der jede Entscheidung Konsequenzen hat und keine Entscheidung die einzig richtige ist.

**Tonalität:** Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.

**Genre:** Third-/First-Person Action-RPG (nahtlos umschaltbar), Semi-Open-World, Medium-Fantasy, Low-Magic, Biotech-Futurismus.

**Plattform:** PC (Primär), Konsolen als Stretch Goal.

**Engine:** Unreal Engine 5.

---

## 2. Scope-Klarheit: Serie vs. Diese Iteration

> V2-Ergänzung. Dieser Abschnitt fehlte in V1. Er schützt das Team vor Scope-Creep und das Versprechen vor Überdehnung.

### Was RELICS als Serie verspricht
RELICS ist eine Series. Jede Iteration spielt in derselben Welt, zu einem anderen historischen Wendepunkt, mit einem anderen Relikt im Zentrum. Die Welt wächst iterationsübergreifend — aber jede Iteration ist für sich spielbar.

### Was *diese Iteration* liefert (Vertical Slice)

Ein Vertical Slice ist kein kleineres Spiel — er ist ein Qualitätsversprechen. Er zeigt, wie das vollständige Spiel sich anfühlen wird. Nicht alles ist drin. Was drin ist, ist vollständig.

| Deliverable | Scope |
|-------------|-------|
| **Region** | Eine zusammenhängende Kernregion (~4–6 km²), Gothic-Dichte, handplatziert |
| **Hauptquest** | Vollständig — drei Akte, drei Fraktionspfade, drei Endvarianten (Tragen / Zerstören / Weitergeben) |
| **Nebenquests** | 2 vollständige Nebenquests als Systemdemonstration |
| **Fraktionen** | Alle drei Fraktionen spielbar und reaktiv — kein Stub, keine Halbimplementierung |
| **Schattenfieber** | Alle fünf Stufen technisch implementiert; Stufe 0–2 vollständig spielbar im Slice |
| **Kamera** | FP/TP nahtlos, vollständig — kein Ladebildschirm, kein Menü |
| **Tiervolk** | Als NPCs und Händler implementiert; Schwarzmarkt-Mechanik funktionstüchtig |
| **Alchemie** | 15–20 Basisrezepte; alle sechs Produktkategorien vertreten |

**Was nicht im Vertical Slice ist:** Weitere Regionen, vollständige Rezeptliste, Multiplayer / Coop (nie geplant).

**Design-Test:** Wenn ein Playtester sagt "Wann kommt der Rest?" — dann hat der Scope-Abschnitt funktioniert.

---

## 3. Die sieben Design-Säulen

> V2-Änderung: V1 hatte sechs Säulen. Kamera wurde als eigene Säule ergänzt (war in V1 nur in Säule 1 und im Referenzrahmen erwähnt). Die übrigen sechs Säulen wurden inhaltlich geschärft, nicht umstrukturiert.

Design-Säulen sind Entscheidungsfilter. Wenn ein Feature, eine Mechanik oder eine Quest eine Säule verletzt, wird sie geändert oder gestrichen — nicht verhandelt.

---

### Säule 1 — Spielerwelt-Immersion

Der Spieler beginnt als Niemand. Er hat keinen Namen, keinen Ruf, keine Vorgeschichte, die ihm Türen öffnet. Macht wird in RELICS verdient — durch Taten, durch Beziehungen, durch die Bereitschaft, Risiken einzugehen.

Das bedeutet konkret: kein Quest-Marker, der dem Spieler sagt, wohin er gehen soll. Keine Tutorial-Hand. Die Welt kommuniziert durch Architektur, NPC-Verhalten und Umweltdetails. Jeder NPC hat einen Tagesablauf und eine Funktion — nicht nur im Quest-System. Geheimnisse sind durch genaues Hinsehen findbar, nicht durch Radar-Pulse. Gebiete haben feste Schwierigkeit — wer zu früh kommt, verliert. Komm später wieder.

**Referenz:** Gothic 2. Die Minentäler-Region hat eine physische Schwierigkeitsarchitektur — wer rechts abbiegt, stirbt. Wer links abbiegt, kommt weiter. Kein Marker sagt dir, welche Richtung die richtige ist.

**Validierungstest:** Kann der Spieler in jeder Situation das Gefühl haben, dass seine Entscheidung — nicht ein Skript — zum aktuellen Zustand der Welt geführt hat?

**Spieler-Fantasie:** *"Ich lerne diese Welt, weil ich ihr zuhöre — nicht weil mir jemand sagt, wohin ich gehen soll."*

---

### Säule 2 — Konsequenz ohne Gnadenfrist

Entscheidungen haben Konsequenzen. "Konsequenz" ist in RELICS kein Konzept — es ist eine Mechanik. Konkret:

| Konsequenz-Typ | Zeitrahmen | Mechanismus |
|----------------|-----------|-------------|
| **Sofort** | Im Moment der Aktion | NPC stirbt, Gespräch bricht ab, Alarm ausgelöst |
| **Kurzfristig** | Bis zum nächsten Aktwechsel | Fraktion reagiert, Questlines öffnen/schließen, Händlerzugang verändert sich |
| **Langfristig** | Bleibt bis zum Ende | Weltzustand ändert sich, NPCs sind dauerhaft weg, Endpfade werden durch frühere Entscheidungen beeinflusst |
| **Körperlich** | Permanent, irreversibel | Schattenfieber-Hard-Cap — die Infektion vergisst nicht |

Was das NICHT bedeutet: Strafe für Fehler. Es bedeutet: Echte Entscheidungen haben echtes Gewicht. Die dramatischste Konsequenz ist oft nicht der tote NPC — sondern der lebende NPC, der sich nun anders verhält.

**Validierungstest:** Wenn ein Spieler nach 30 Stunden sagt "Ach so, DESHALB ist der Schmied feindlich" — dann hat diese Säule funktioniert.

**Spieler-Fantasie:** *"Ich lebe mit meinen Entscheidungen. Ich kann sie nicht rückgängig machen. Das macht sie bedeutsam."*

---

### Säule 3 — Kamera als Spieler-Autonomie

> V2-Ergänzung als eigenständige Säule. Kamera ist nicht UI. Kamera ist Identität.

Der Spieler wählt, wie er die Welt erlebt. First-Person und Third-Person sind nahtlos umschaltbar — kein Ladebildschirm, kein Menü.

**First Person:**
- Maximale Immersion — der Spieler IST in der Welt
- Räumliche Präsenz in engen Umgebungen (Katakomben, Kanalisation, Gefängnisse)
- Schattenfieber-Wahrnehmungsveränderungen wirken stärker in FP

**Third Person:**
- Vollständige Ausrüstungs-Customization sichtbar — *Ich sehe, was ich trage*
- Bessere Kampfübersicht in komplexen Begegnungen
- Vertikalität erfahrbar — der Spieler sieht seinen Charakter klettern

Wer in FP spielt, erlebt eine andere Tonalität als wer in TP spielt. Beide Erfahrungen müssen vollständig und gleichwertig sein. Das ist ein Designversprechen, kein technisches Deliverable.

**Referenz:** Skyrim — nahtloser FP/TP-Wechsel als Industriestandard. RELICS übernimmt das Prinzip, setzt es aber auf einem visuell reicheren Biotech-Mittelalter-Fundament um.

**Validierungstest:** Kann ein Spieler, der ausschließlich in FP spielt, genauso viel vom Spiel erleben wie ein Spieler, der ausschließlich in TP spielt?

**Spieler-Fantasie:** *"Das ist mein Charakter. Ich bestimme, aus welcher Perspektive ich ihn erlebe."*

---

### Säule 4 — Körperliche Progression

RELICS ersetzt abstrakte Skill-Trees durch ein physiologisches Leveling-System. Der Spieler investiert Punkte in vier Nervensystem-Äste: Cardio/Atmung, Muskel/Skelett, Lymph/Immun und — ab dem ersten Punkt Schattenfieber-Infektion — den Schatten-Ast. Die Darstellung ist eine halbtransparente Nervensystem-Ansicht des Körpers. Progression ist sichtbar, greifbar, körperlich.

Fähigkeiten werden nicht in einem Menü freigeschaltet. Sie werden bei Trainern in der Welt gelernt — NPCs, die ihre Dienste an Fraktionszugehörigkeit, Reputation und Vorbedingungen knüpfen. Welcher Fraktion der Spieler sich anschließt, bestimmt, welche Fähigkeiten er überhaupt lernen KANN.

Perks sind transformativ, nicht numerisch. "Du kannst jetzt im Sprint angreifen" statt "+20% Schwertschaden".

**Vollständige Mechanik:** → `02-kernmechaniken.md`, Kapitel 3

**Validierungstest:** Kann der Spieler seinen Build einem anderen Spieler erklären, ohne Zahlenwerte zu nennen — nur durch Beschreibung dessen, was er tun kann?

**Spieler-Fantasie:** *"Dieser Körper ist meiner — ich entscheide, was er wird."*

---

### Säule 5 — Biotech-Futurismus als Weltsprache

> V2-Schärfung: Biotech war in V1 als USP gelistet, aber nicht als Design-Säule verankert. Es ist beides.

RELICS spielt nicht in der Vergangenheit. Es spielt in einer anderen Gegenwart — einer Welt, deren Biologie andere Wege gegangen ist.

**Was Biotech-Futurismus bedeutet:**
- **Leveling ist körperlich:** Vier physiologische Nervensystem-Äste. Progression ist sichtbar — nicht als Zahlenwerte, sondern als Körper-Visualisierung.
- **Alchemie ist Wissenschaft:** Keine Magie. Gifte, Stimulanzien, Suppressiva, Kontaktmittel. Alchemie ist gefährlich, weil sie in einer Welt stattfindet, die auf einem toten Urwesen gebaut ist.
- **Schattenfieber ist Biologie:** Die Seuche transformiert den Körper — keine mystische Verwandlung, sondern ein physiologischer Prozess mit mechanischen Konsequenzen.
- **Ästhetik:** Mehr futuristisch, weniger heruntergekommen. High Fashion Mittelalter. Die Mächtigen sehen wie die Mächtigen aus.

**Was Biotech-Futurismus NICHT bedeutet:** Steampunk, vergessene Hochtechnologie, Science-Fantasy-Alien-Artefakte.

**Validierungstest:** Wenn jemand RELICS als "Steampunk-Spiel" beschreibt, hat diese Säule nicht funktioniert. Das ist die Anti-Formulierung.

**Spieler-Fantasie:** *"Diese Welt hat eine eigene Logik — und wenn ich sie verstehe, kann ich sie benutzen."*

---

### Säule 6 — Tiervolk als soziale Schicht

> V2-Schärfung: Das Tiervolk war in V1 im Fraktionsabschnitt kurz erwähnt. Es ist eine eigenständige Design-Entscheidung mit mechanischer Relevanz.

Das Tiervolk ist keine Rasse im Fantasy-Sinne. Es ist eine Gesellschaftsschicht.

**Funktion in der Spielwelt:**
- **Händler:** Tiervolk kontrolliert den Schwarzmarkt und den Graumarkt. Seltene Alchemie-Zutaten, gestohlene Waren, Informationen. Der Spieler braucht das Tiervolk für Inhalte, die über legale Wege nicht erreichbar sind.
- **Diebe:** Tiervolk operiert in den Rändern der Gesellschaft — Dächer, Kanalisation, Schmugglerwege. Ihre Vertikalität überschneidet sich mit den Level-Design-Prinzipien des Spiels.
- **NICHT Handwerker:** Das Tiervolk stellt nichts her, was die menschliche Gesellschaft bereits produziert. Sie handeln mit dem, was anderen zu riskant oder zu illegal ist.

**Ästhetik-Direktive (Briefing):**
- Leicht alien vs. menschlich clean — der Unterschied ist subtil, aber real
- Weniger tribal, mehr urban-marginalisiert
- Temporäre Materialien in permanenten Strukturen (improvisierte Nischen, nomadische Markierungen)

**Mechanische Relevanz:**
- Exklusive Alchemie-Zutaten (inkl. Schattenfieber-Suppressiva) nur über Tiervolk-Händler
- Schmugglerrouten als alternative Zugangspfade zu gesperrten Gebieten
- Ab Infektionsstufe 2 verändert sich die Tiervolk-Reaktion auf den Spieler: "einer von uns, der nicht ganz zur Norm gehört"

**Validierungstest:** Wenn ein Spieler Stufe-0-Alchemie maximieren will, muss er mit dem Tiervolk interagieren. Wenn ein Spieler alle Gebiete erkunden will, muss er ihre Routen kennen.

**Spieler-Fantasie:** *"Die Gesellschaft hat Regeln. Das Tiervolk kennt die Lücken."*

---

### Säule 7 — Vertikales Raumdesign

RELICS behandelt den Raum als drei Dimensionen. Städte sind nicht nur Grundrisse — sie haben begehbare Dachlandschaften, Keller, Kanalisation, Brücken und Turmebenen. Die Wildnis bietet Klippen, Höhlen, Baumkronen, Flussbetten und Bergpässe.

Zu jedem Ziel führen mindestens drei Wege: Der Hauptweg (sicher, lang), der Schleichweg (riskant, kurz) und der Vertikalweg (Geschick erforderlich, belohnend).

Das Prinzip lautet: **Was du siehst, kannst du erreichen.** Sightline-Navigation statt Kompassnadel.

**Referenz:** Dishonored — vertikale Raumtiefe als Gameplay-Prinzip. RELICS überträgt es auf eine persistente Open World, nicht auf abgeschlossene Missionen.

**Validierungstest:** Gibt es für jede Spielersituation mindestens zwei räumlich unterschiedliche Lösungswege — einen horizontalen und einen vertikalen?

**Spieler-Fantasie:** *"Ich finde Wege, die andere nicht sehen."*

---

## 4. Alleinstellungsmerkmale (USPs)

| # | USP | In einem Satz | Unterschied zu Referenz |
|---|-----|--------------|------------------------|
| **USP 1** | Biologische Transformation als Kern-Progression | Das Schattenfieber verändert Körper und Welt dauerhaft — und es gibt keine Heilung, nur Kontrolle | Skyrim-Vampirismus ist reversibel und marginal. Bloodborne-Beasthood ist temporär. RELICS macht es permanent und zentral. |
| **USP 2** | Welt-Reaktivität statt Marker-Quests | Die Welt erinnert sich. NPCs haben Gedächtnisse. Konsequenzen kommen — auch wenn der Spieler sie vergessen hat. | Gothic 2 ist der nächste Vergleich. RELICS setzt diesen Standard 2025 neu. |
| **USP 3** | Open-World mit Immersive-Sim-Vertikalität | Weltdichte und Exploration eines Gothic-artigen RPG + räumliche Tiefe und Systeminteraktion einer Immersive Sim | Kein existierendes Referenzspiel bietet beides. Gothic/Skyrim sind horizontal. Dishonored ist abgeschlossen. |

---

## 5. Zielgruppe

> V2-Schärfung: V1 definierte Kernzielgruppe als "22-35 Jahre". Präzisiert auf 25-40 auf Basis des CD-Profils: erfahrene Spieler, die Gothic und BG3 kennen, aber berufstätig und zeitkritisch sind.

### Kernzielgruppe: Erfahrene RPG-Spieler, 25–40 Jahre

Diese Spieler kennen Gothic, Skyrim, vielleicht Bloodborne. Sie wissen, was ein gutes RPG von einem schlechten unterscheidet. Sie haben weniger Zeit als früher — aber sie spielen tiefer, wenn das Spiel es verdient.

**Was sie wollen:**
- Keine Tutorial-Hände, die ihnen jeden Schritt erklären
- Tiefe, die sich durch Spielen erschließt — nicht durch Handbuch oder Wiki
- Konsequenzen, die sich echt anfühlen
- Eine Welt, die ihnen das Gefühl gibt, sie zu erkunden — nicht eine Quest-Liste abzuhaken

**Was sie nicht wollen:**
- Grind als Zeitfüller
- Artificial Difficulty (Feind-HP skaliert mit Level)
- Moral-Kompasse im HUD
- Mikrotransaktionen

**Spielzeit-Erwartung:**

| Spielzeit | Erfahrung |
|-----------|-----------|
| **1 Stunde** | Die Welt hat mich. Ich verstehe die Grundregeln. Ich habe eine erste Entscheidung getroffen, die sich bedeutsam anfühlte. Ich will mehr. |
| **10 Stunden** | Ich kenne eine Fraktion gut, zwei oberflächlich. Ich habe meine Schattenfieber-Position definiert. Ich habe mindestens eine unerwartete Konsequenz gespürt. |
| **40 Stunden** | Ich habe eine Welt erlebt, nicht ein Spiel gespielt. Ich kann einen anderen Durchlauf beginnen und weiß, dass er sich fundamental anders anfühlt. |

**Drei Kernkommunities innerhalb der Zielgruppe:**

| Community | Was sie suchen | RELICS-Angebot |
|-----------|---------------|----------------|
| **Gothic-Community** | Weltdichte, keine Kompromisse, NPC-Gedächtnisse | Säule 1 + Säule 2 — Welt als Spiel, echte Konsequenz |
| **Immersive-Sim-Fans** | Systemtiefe, mehrere Lösungswege, emergentes Gameplay | Säule 7 + USP 3 — Vertikalität in Open World |
| **Action-RPG-Community** | Skill-basierter Kampf, Feedback-Qualität, Progression | Säule 4 + GDD-02 Combat — Skill-Ceiling als Spektrum |

### Sekundärzielgruppe: Narrative-RPG-Fans, 20–30 Jahre

Kennen Baldur's Gate 3, Disco Elysium, VtM: Bloodlines. Suchen Fraktionsdynamik, moralische Ambiguität, Weltreaktivität. RELICS ist für sie zugänglich über Erzählung und Fraktionspolitik.

### Monetarisierung

Klassisches Premium-Modell. Kein Free-to-Play, keine Mikrotransaktionen, keine Season Passes.
- **Alpha:** Kostenloser Zugang für ausgewählte Content Creators und Streamer.
- **Beta:** Steam Early Access, voraussichtlich ein Jahr vor Release.
- **Release:** Vollpreistitel.
- **Post-Launch:** Story-DLCs mit substantiellem Umfang, hochwertige Merchandise-Linie.

---

## 6. Spielerfahrung

Die Spielerfahrung folgt einem emotionalen Bogen in drei Phasen. Das übergeordnete Game Feel: **Ich betrete als Fremder eine aufregende Sandbox.**

### Die erste Stunde — "Diese Welt ist gefährlich und aufregend."

Der Spieler erstellt seinen Charakter und betritt die Welt ohne Nichts: kein Geld, keine Waffe, keine Verbindungen. Die ersten Begegnungen sind sorgfältig gesetzt — nicht als Tutorial, sondern als Weltexposition. Der Spieler trifft auf alle drei Fraktionen als Teil der lebenden Welt, nicht als Questgeber.

Die erste Kampfbegegnung ist brutal, lehrreich und überlebbar. Sie lehrt das Basisvokabular (Angriff, Block, Ausweichen, Ausdauer-Management) und vor allem eine Haltung: In dieser Welt kämpft man nicht leichtfertig.

Am Ende der ersten Stunde hat der Spieler Optionen — keine Hauptquest-Verpflichtung, keine vorgegebene Richtung.

### Zehn Stunden — "Ich verstehe diese Welt."

Der Spieler hat sich orientiert. Er kennt die Stadt, hat Verbindungen, Rivalitäten, Schulden. Das Schattenfieber ist ihm begegnet — optional hat er seine erste Infektion erlebt und die Schattensinne aktiviert. Dieser Moment ist designt, um zu begeistern, nicht zu erschrecken: "Das war es wert. Was kommt noch?"

Am Ende der zehnten Stunde hat der Spieler das Gefühl, Teil dieser Welt zu sein.

### Vierzig Stunden — "Meine Entscheidungen haben diese Welt geformt."

Der Spieler hat seine Fraktion gewählt und die exklusive Questline fortgeführt. Sein Schattenfieber-Status definiert seinen Spielstil. Die Welt hat sich verändert: Fraktionsverhältnisse, NPC-Verhalten, zugängliche Orte. Und der Spieler weiß: Ein zweiter Durchgang mit einer anderen Fraktion und einem anderen Schattenfieber-Pfad wäre eine fundamental andere Erfahrung.

---

## 7. Referenzrahmen

| Referenz | Was RELICS nimmt | Was RELICS NICHT nimmt |
|----------|-----------------|------------------------|
| **Gothic 2** | Weltdichte, Trainer-System, Null-zu-Held-Bogen, feste Gebiets-Schwierigkeit | Veraltete Zugangshürden ohne Onboarding-Logik |
| **Skyrim** | Kamera (FP/TP), Zugänglichkeit, Sightline-Navigation | Level-Skalierung, Quest-Marker-Abhängigkeit, Auserwählten-Narrativ |
| **Bloodborne** | Transformationsmechanik, Wahrnehmungswandel als Gameplay-System | Punishing difficulty als Selbstzweck, Obskurantismus |
| **VtM: Bloodlines** | Fraktionsgameplay, soziale Konsequenzen einer Transformation | Fester Protagonist |
| **Dishonored** | Vertikales Raumdesign, Systeminteraktion, Feedback-Qualität | Science-Fantasy-Technologie-Ästhetik |
| **Baldur's Gate 3** | Proof of Concept: großes CRPG kann kommerziell erfolgreich sein | Rundenbasierter Kampf, festes Team |
| **The Witcher (NICHT)** | — | Fester Protagonist; kein vorgegebener Charakter, keine vorgegebene Moral |
| **Skyrim-Vampirismus (NICHT)** | — | Ungewollte Infektion, keine sofortige Power Fantasy |

---

## 8. Spieler-Fantasien — Der Test

Jede Mechanik, jede Quest, jede Design-Entscheidung muss einer der folgenden Spieler-Fantasien dienen. Wenn sie das nicht tut, wird sie gestrichen.

| # | Spieler-Fantasie | System, das sie trägt |
|---|-----------------|----------------------|
| F1 | "Ich lerne diese Welt, weil ich ihr zuhöre." | Säule 1 — Welt als Spiel, keine Quest-Marker |
| F2 | "Ich lebe mit meinen Entscheidungen." | Säule 2 — Konsequenz-Typen-Matrix, Schattenfieber-Hard-Cap |
| F3 | "Das ist mein Charakter, aus meiner Perspektive." | Säule 3 — Kamera-Autonomie FP/TP |
| F4 | "Dieser Körper ist meiner — ich entscheide, was er wird." | Säule 4 — Nervensystem-Leveling, Schattenfieber-Transformation |
| F5 | "Diese Welt hat eine Logik — ich begreife sie." | Säule 5 — Biotech-Futurismus, Alchemie-System, Fraktionspolitik |
| F6 | "Die Gesellschaft hat Regeln. Ich kenne die Lücken." | Säule 6 — Tiervolk-Schwarzmarkt, Schmugglerrouten |
| F7 | "Ich finde Wege, die andere nicht sehen." | Säule 7 — Vertikalität, Schattensinne, Alchemie-Tricks |

---

## 9. Offene Fragen (V2-Stand)

| # | Frage | Zuständig | Priorität |
|---|-------|----------|-----------|
| 1 | Iterations-Titel — welcher Name ersetzt [Iterations-Titel]? | CD-Entscheidung | Hoch — vor Marketing-Materialien |
| 2 | Schnellreise: Ja/Nein? Empfehlung: Erst zweiter Akt, als narrativer Unlock | Darius + Finn | Mittel |
| 3 | Tages-/Nachtzyklus: Gameplay-Auswirkungen? NPC-Routinen, Schattenfieber-Intensität? | Darius + Tobi | Mittel |
| 4 | Tiervolk — eigener Name im RELICS-Namenssystem? | Emre (Namenssystem) | Offen — abhängig von Emres Namenssystem-Abschluss |

---

*Darius Engel, Game Design Corner, Tag 5 (Freitag) — V2-Finalisierung*
*"Macht es Spaß? Was ist die Spieler-Fantasie hier?" — beantwortet.*

\clearpage

# GDD-02: Kernmechaniken

**Autor:** Darius Engel, Game Director
**QA:** Leo Brandt (Spielermarkt & Community)
**Narrativ-Sync:** Nami Osei (Erzaehlkonzept)
**Version:** V0.5 (Tag 2, Dienstag — Nachmittags-Ueberarbeitung)
**Status:** Zwischen Outline und V1 — Strukturen stehen, Schluesselabschnitte angereichert, offene Fragen reduziert
**Aenderungslog:**
- V1-Outline (Tag 2 Vormittag): Kapitelstruktur + Kernpunkte
- V0.5 (Tag 2 Nachmittag): Leos QA-Bedingungen integriert, Schattenfieber-Stufen-Mapping mit Nami synchronisiert, CD-Entscheidungen eingearbeitet (Tod/Infektion, Lebende Krone, Namenssysteme, Combat-Skill-Ceiling)
- V0.5.1 (Tag 5 Nachmittag): Arbeitsbegriff "Ymir" → "Emer" (2x: Kap. 2.7, Kap. 6.1) — Leo Fischer, QA

---

## 1. Combat-System

### 1.1 Grundphilosophie
- Real-time Action, Melee-fokussiert, gewichtig
- KEIN Difficulty Slider — die Welt bestimmt die Schwierigkeit (Gothic-Prinzip)
- Skill-Ceiling als Spektrum (CD-bestaetigt): Einstieg intuitiv, Mastery belohnend — nie erzwungen
- Jeder Kampf soll sich BEDEUTSAM anfuehlen — keine Trash-Mobs, kein Grind
- Spieler-Fantasie: "Ich habe diesen Kampf gewonnen, weil ich besser geworden bin — nicht weil ich Level 50 bin."

**Skill-Ceiling-Spektrum (Detail):**
Das System muss auf BEIDEN Enden des Spektrums funktionieren. Ein Spieler, der nur Basisaktionen nutzt, soll jede Begegnung bestehen koennen (mit Vorbereitung und Geduld). Ein Spieler, der Cancel-Windows und Setup-Plays beherrscht, soll sich belohnt fuehlen (schnellere Kills, elegantere Loesungen, optionale Herausforderungen). Kein Spieler soll das Gefuehl haben, er muesste Mastery-Techniken lernen, um weiterzukommen. Aber jeder Spieler soll sehen KOENNEN, was moeglich waere.

### 1.2 Kampfschichten (drei Ebenen)

#### Ebene 1 — Basis (sofort zugaenglich)
- Leichter Angriff, schwerer Angriff, Block, Ausweichen
- Ausdauer-Management: Jede Aktion kostet Ausdauer, Uebertreiben wird bestraft
- Ziel-Lock-On optional (nicht erzwungen)
- Jeder Spieler kann sofort kaempfen — Gothic-Gewicht, Skyrim-Zugaenglichkeit

#### Ebene 2 — Fortgeschritten (erlernt durch Trainer + Uebung)
- Parade/Riposte: Praezises Timing-Fenster, belohnt mit Gegenangriff
- Positionierung: Flankenangriffe, Rueckenattacken, Hoehenvorteile (Vertikalitaet!)
- Waffenspezifische Kombos: Abhaengig von Waffenklasse, erlernt bei Trainern
- Umgebungsinteraktion: Objekte treten/werfen, Engstellen nutzen, Gegner in Fallen locken

#### Ebene 3 — Mastery (belohnend, nie erzwungen)
- Cancel-Windows: Fortgeschrittene Spieler koennen Animationen unterbrechen fuer Feints
- Setup-Plays: Alchemie-Vorbereitung (Oele, Gifte) + Positionierung + Timing als koordinierte Strategie
- Schattenfieber-Combat-Integration: Schattenreflex (erweitertes Parry-Window), Fieber-Puls (AoE, kostet HP)
- Perfekte Paraden: Winzigstes Timing-Fenster, maximal belohnend (Spezial-Riposte)

### 1.3 Waffenklassen (vorlaeufig)
- **Schwerter** (Einhand/Zweihand): Allrounder, mittlere Geschwindigkeit, ausgewogenes Moveset
- **Aexte/Haemmer** (Einhand/Zweihand): Langsam, hoher Schaden, Schildbrecher
- **Dolche/Kurzwaffen**: Schnell, niedriger Einzelschaden, Combo-orientiert, Giftapplikation
- **Boegen**: Ranged, Haltungsschaden, kein Hauptwaffen-Fokus (Unterstuetzung)
- **Armbrueste**: Schwerer Ranged-Schaden, lange Nachladezeit, Situationswaffe
- **Schilde**: Defensiv, Block-Effizienz, Schildstoss als Unterbrechung

**Offene Frage:** Waffenklassen-Anzahl fuer den Vertical Slice? Empfehlung: 3-4 Nahkampf + 1 Ranged fuer V1.

### 1.4 Feinddesign-Prinzipien
- Feinde haben EIGENE Movesets, nicht nur skalierte Spieler-Angriffe
- Feindtypen definiert durch Verhalten, nicht nur durch Werte: Aggressive, Defensive, Taktiker, Infizierte
- Infizierte Feinde nutzen Schattenfieber-Faehigkeiten — Vorschau fuer den Spieler ("Das koennte ICH auch")
- Keine Level-Skalierung: Gebiete haben feste Feindstaerke. Manche Gegner sind zu frueh zu stark. Komm spaeter wieder.

### 1.5 Tod und Konsequenz
- Tod ist ein Rueckschlag, kein Game Over — Checkpoint-System mit fairen Abstaenden
- Keine Erfahrungspunkt-Strafe bei Tod
- **Tod beeinflusst den Infektionswert NICHT** (CD-bestaetigt). Begruendung: Tod ist bereits Strafe genug. Infektionsanstieg bei Tod wuerde Risk/Reward des Schattenfieber-Systems untergraben und die bewusste Entscheidung zur Nutzung verwischen.
- Konsequenz durch WELT-Reaktion: Bestimmte Situationen veraendern sich bei erneutem Versuch (NPC-Kommentare, veraenderte Wachpositionen)

---

## 2. Schattenfieber-System

> **QA-Einschaetzung (Leo):** 40% des QA-Aufwands entfaellt auf das Schattenfieber-System. Es ist gleichzeitig groesster USP und groesstes Risiko. Die folgenden drei nicht-verhandelbaren Bedingungen sind das Ergebnis von Leos Community- und Marktanalyse.

### 2.1 Drei Nicht-Verhandelbare Bedingungen (QA-validiert)

Diese drei Bedingungen haben Veto-Recht ueber jede Schattenfieber-Designentscheidung. Wenn ein Feature eine dieser Bedingungen verletzt, wird es geaendert oder gestrichen — ohne Ausnahme.

**Bedingung 1: TRANSPARENZ VOR INFEKTION**
- Der Spieler muss JEDERZEIT wissen, welche Aktion seinen Infektionswert erhoehen kann und um wie viel
- Keine versteckten Infektionsquellen. Keine "Ueberraschung, du bist jetzt infiziert"
- UI-Feedback: Klarer Indikator wenn der Spieler sich in einer infektionserhoehenden Situation befindet (visuell, auditiv, haptisch)
- Infektionserhoehende Aktionen muessen eine explizite Bestaetigung haben ODER einen klar wahrnehmbaren Moment der bewussten Entscheidung bieten
- **Goldstandard**: Bloodborne Insight — der Spieler sammelt Insight durch spezifische, erkennbare Aktionen (Bosse sehen, Madman's Knowledge nutzen). Es gibt keine versehentliche Insight-Erhoehung
- **Anti-Referenz**: Skyrim Vampirismus — Infektion passiert im Kampf durch einen zufaelligen Statuseffekt, den Spieler oft nicht bemerken. Der haeufigste Community-Complaint: "Ich wusste nicht, dass ich Vampir werde"

**Bedingung 2: SOFORTIGE POWER FANTASY NACH INFEKTION**
- Ab dem ERSTEN PUNKT Infektionswert muss der Spieler etwas Cooles koennen, das er vorher nicht konnte
- Kein "Stufe 1 ist nur Nachteile, die guten Sachen kommen spaeter" — das widerspricht der Kernfantasie
- Schattensinne (Stufe 1) muessen sofort als Upgrade erlebbar sein: Verstecktes sehen, Emotionen lesen, eine ZWEITE SCHICHT der Welt wahrnehmen
- Der Spieler soll nach der ersten Infektion denken: "Das war es wert. Was kommt noch?"
- **Goldstandard**: Bloodborne — der erste Insight-Punkt zeigt sofort die Puppe im Hunter's Dream. Die Welt veraendert sich. Der Spieler fuehlt sich belohnt.

**Bedingung 3: KEIN VERSEHENTLICHES INFIZIEREN**
- Infektion darf NIEMALS durch Zufall, Unachtsamkeit oder unklare Mechaniken passieren
- Jeder Infektionspunkt muss auf eine BEWUSSTE SPIELERENTSCHEIDUNG zurueckfuehrbar sein
- Kampf gegen Infizierte = Infektionsrisiko? Dann muss das VOR dem Kampf klar kommuniziert werden, und der Spieler muss eine taktische Wahl haben (Distanzwaffen, Alchemie-Schutz, Umgehen)
- Story-Events, die Infektion erhoehen: Muessen als Entscheidung praesentiert werden, nicht als Cutscene-Zwang
- **Design-Test**: Wenn ein Spieler nach 20 Stunden sagt "Ich wollte Stufe 0 bleiben, aber irgendwie bin ich Stufe 2" — dann haben wir versagt

### 2.2 Systemuebersicht
- Permanenter Infektionswert: 0-100
- Fuenf mechanische Stufen mit spuerbaren Schwellen
- Vierter Ast im Nervensystem-Leveling (nur ab Stufe 1+)
- NICHT heilbar, nur kontrollierbar (CD-bestaetigt)
- Jede Stufe = andere Spielerfahrung, KEINE ist schlechter als die andere

### 2.3 Stufen-Mapping: Mechanik x Narrativ x Wahrnehmung

Die folgende Tabelle synchronisiert Darius' fuenf mechanische Stufen mit Namis drei narrativen Zustaenden (Rauschen, Risse, Schwelle). Die narrativen Zustaende sind KEINE separaten Systeme — sie sind die erlebbare Oberflaechenerscheinung der mechanischen Stufen.

| Mech. Stufe | Wert | Name | Narrativer Zustand (Nami) | Kern-Fantasie | Zentrale Faehigkeit | Narrative Auswirkung |
|-------------|------|------|---------------------------|---------------|---------------------|---------------------|
| 0 | 0 | Rein | Gesund | Underdog, rein menschlich | Volle Nervensystem-Effizienz, uneingeschraenkte Sozialinteraktion | Standard-Erzaehlung: klare, zuverlaessige Wahrnehmung |
| 1 | 1-25 | Gezeichnet | Rauschen | "Ich sehe, was andere nicht sehen" | Schattensinne (passiv): Verstecktes sichtbar, Emotionsauren | Subtile Textveraenderungen in Dialogen. Umgebungshinweise, die andere nicht sehen. Einzelne Worte in NPC-Saetzen verschieben sich. Spieler bemerkt es vielleicht nicht sofort. |
| 2 | 26-50 | Infiziert | Rauschen → Risse (Uebergang) | Maechtig, aber sichtbar anders | Schattenreflex, Schatten-Schritt, Schmerzunterdrueckung | Uebergangszone: Hinweise werden deutlicher, erste fragwuerdige Wahrnehmungen. Gespraechsoptionen erscheinen, die andere nicht hoeren. |
| 3 | 51-75 | Verwandelt | Risse | Kein Mensch mehr, aber maechtig | Schattenprojektion, Fieber-Puls, Tiefensicht | Alternative Dialoge mit Figuren, die moeglicherweise anders reden als erwartet. Fragwuerdige Questgeber. NPCs reagieren irritiert auf Antworten, die der Spieler fuer normal haelt. |
| 4 | 76-100 | Entfesselt | Schwelle | Das Monster — und vielleicht ist das okay | Schattenform, Fieber-Ruf, Schattenwurzeln + Kontrollverlust-Episoden | Parallel-Narrativ: Dialoge mit Figuren, die moeglicherweise nicht existieren. Daseinsebenen werden durchlaessig. Der Spieler kann nicht mehr unterscheiden, welche Gespraeche "echt" sind. |

**Uebergangs-Design:**
- Stufenuebergaenge sind KEINE harten Schalter. Der Infektionswert bestimmt die Intensitaet innerhalb einer Stufe graduell.
- Beispiel: Bei Wert 15 sind Schattensinne schwaecher als bei Wert 24. Es gibt keinen Moment, in dem alles "anspringt".
- Die narrativen Zustaende haben weiche Grenzen: "Rauschen" beginnt ab dem ersten Infektionspunkt und intensiviert sich. "Risse" setzt schrittweise ab ca. Wert 40 ein. "Schwelle" wird ab ca. Wert 70 spuerbar.
- **QA-Relevanz (Leo)**: Genau dieser graduelle Uebergang ist der Grund fuer den hohen QA-Aufwand. Jeder der ~100 Infektionswerte muss sich in der Spielerfahrung "richtig" anfuehlen.

### 2.4 Infektionsfortschritt

**Steigerung:**
- Umgebungsexposition (verseuchte Orte, Kampf gegen Infizierte) — NUR mit vorheriger Warnung (Bedingung 1+3). Der Spieler sieht/hoert/spuert, dass ein Ort verseucht ist, BEVOR er ihn betritt.
- Bewusste Nutzung (Schattenfieber-Faehigkeiten einsetzen: ~0.5-1 Punkt pro Einsatz) — jede Faehigkeitsnutzung zeigt den Infektionsanstieg im UI
- Story-Events (Schluesselmomente, Boss-Begegnungen) — IMMER als bewusste Spielerentscheidung praesentiert, nie als Cutscene-Zwang
- Kontakt mit der Lebenden Krone (siehe 2.7) — Relikt-Interaktion als hochriskante, hochbelohnende Infektionsquelle
- Tod erhoet den Infektionswert NICHT (CD-bestaetigt)

**Senkung:**
- Alchemie-Suppressiva (-3 bis -5 Punkte, teuer, Wirkung nimmt bei hohem Wert ab)
- Orden-Reinigung (-10 bis -15 Punkte, nur bei Orden-Allianz, ab Stufe 3 verweigert)
- Ruhe und Isolation (-1/Tag, nur bis Stufe 2)

**Hard Cap:** Infektionswert kann NIE unter die hoechste je erreichte Stufenschwelle fallen. Die Infektion vergisst nicht.

### 2.5 Kosten-Nutzen-Matrix

> Die Tabelle muss gegen Bedingung 2 (sofortige Power Fantasy) validiert werden. JEDE Zeile ab Stufe 1 muss einen klaren, sofort erlebbaren Vorteil haben, der die Kosten aufwiegt — zumindest im Moment der Entscheidung.

| Stufe | Nutzen (sofort erlebbar) | Kosten (wachsend) | Stufe-0-Aequivalent |
|-------|-------------------------|-------------------|---------------------|
| 0 | Volle Systemeffizienz, voller Weltzugang, vollstaendige Alchemie-Wirkung | Kein Zugang zu Schattenfaehigkeiten, keine zweite Wahrnehmungsschicht | — |
| 1 | **Schattensinne** (Exploration-Vorteil): Verstecktes sichtbar, Emotionsauren, neue Wege | Lymph -5%, Misstrauen aufmerksamer NPCs | Volle Alchemie als Alternative zu Schattensinnen |
| 2 | **Aktive Kampf-Faehigkeiten**: Schattenreflex, Schatten-Schritt — neue Kampfdimension | Lymph -15%, Cardio -10%, sichtbar infiziert, Krone distanziert | Fortgeschrittene Trainer-Faehigkeiten (Ebene 2+3) |
| 3 | **Fortgeschrittene Faehigkeiten**, +15% Melee, Tiefensicht | Alle Aeste -25%, Krone feindlich, Orden jagt | Meister-Alchemie + Positionierung + Setup-Plays |
| 4 | **Apex-Faehigkeiten**, massive Kampfkraft, volle Doppelwahrnehmung | Alle Aeste -40-50%, Kontrollverlust, soziale Isolation | Kein direktes Aequivalent — Stufe 0 hat dafuer volle soziale Integration |

**Stufe-0-Aequivalent (neu):** Jede Schattenfieber-Stufe hat eine nicht-infizierte Alternative, die denselben Spielraum abdeckt, aber mit anderen Mitteln. Das sichert ab, dass Stufe 0 sich NIE wie "der langweilige Weg" anfuehlt.

### 2.6 Weltreaktivitaet
- NPCs reagieren auf Infektionsstufe (Angst, Mitleid, Nuetzlichkeit, Feindschaft)
- Fraktionen verschieben Zugang: Orden schliesst frueh, Krone spaeter, Gilden pragmatisch
- Infizierte NPCs erkennen den Spieler ab Stufe 2+ als "einen von ihnen"
- Moegliche emergente vierte Fraktion: Untergrund der Infizierten (offene Frage fuer Emre/Nami)
- Umgebungseffekte: Tiere fliehen, Pflanzen reagieren (ab Stufe 3+)

### 2.7 Das Relikt: Die Lebende Krone

> CD-Entscheidung: Das Relikt dieser Iteration ist die **Lebende Krone** — ein Biotech-Artefakt aus der Ur-Bindung.

- Die Lebende Krone ist ein organisches Artefakt, das auf die kosmologische Ur-Bindung (WBB-01, Kap. 4) zurueckgeht
- Sie ist LEBENDIG im woertlichen Sinne: Sie reagiert, waechst, veraendert sich — Biotech auf kosmologischer Ebene
- Fraktions-Interpretationen:
  - **Krone**: Dynastisches Erbe, Legitimation der Herrschaft, Zeichen goettlichen Auftrags
  - **Gilden**: Das wertvollste Handelsgut der Welt, Machtinstrument ohne ideologische Bindung
  - **Orden**: Erkenntniswerkzeug, Schluessel zum Verstaendnis der Ur-Bindung und der Daseinsebenen
- Schattenfieber-Verbindung: Die Lebende Krone und das Schattenfieber greifen auf dasselbe "Emer-Material" zu (WBB-01, Kap. 6). Die Krone ist die kontrollierte Form, das Schattenfieber die unkontrollierte.
- Kontakt mit der Krone KANN den Infektionswert erhoehen — massiv, aber unter Bedingung 1 und 3 (Transparenz, bewusste Entscheidung)

**Offene Fragen zum Relikt:**
- [ ] Wie interagiert der Spieler physisch mit der Krone? Tragen? Beruehren? Studieren? (Emre + Darius)
- [ ] Kann die Krone das Schattenfieber kontrollieren, nicht nur erhoehen? (CD-Rueckfrage)
- [ ] Visuelle Erscheinung: Organisch, pulsierend, wurzelartig? (Vera)

### 2.8 Transparenz-UI (QA-Anforderung)

> Direkte Umsetzung von Bedingung 1. Dieses UI-Modul ist KEIN "nice-to-have" — es ist systemkritisch.

- **Infektionsanzeige**: Permanenter Balken/Indikator (nicht als Zahl, sondern als organische Visualisierung — passend zum Nervensystem-UI)
- **Warnhinweis**: Wenn der Spieler eine infektionssteigernde Zone betritt, Aktion ausfuehrt oder Story-Entscheidung trifft → visueller + auditiver Cue BEVOR die Erhoehung eintritt
- **Faehigkeitskosten**: Jede Schattenfieber-Faehigkeit zeigt ihren Infektionskosten-Wert im Tooltip
- **Stufenwarnung**: Wenn der Spieler kurz vor einer neuen Stufenschwelle steht (5 Punkte entfernt), bekommt er einen besonderen Hinweis — die Schwelle ist permanent
- **Design-Vorgabe fuer Vera**: Die Infektionsanzeige soll sich organisch in die Nervensystem-Visualisierung einfuegen. Kein separates HUD-Element, sondern Teil desselben koerperlichen Systems.

### 2.9 Offene Design-Fragen (aktualisiert)

- [x] ~~Tod und Schattenfieber~~ → Tod erhoet den Wert NICHT (CD-bestaetigt)
- [ ] Spezialisierungen innerhalb der Stufen (verschiedene Manifestationen) — V2-Feature?
- [ ] Interaktion mit dem Tiervolk (immun? anders infiziert?) — abhaengig von Emres WBB-01
- [ ] Balancing Stufe 0 vs. Stufe 4 — Stufe-0-Aequivalent-Spalte ist ein erster Ansatz, muss durchgetestet werden (QA mit Leo)
- [ ] Kontrollverlust-Episoden (Stufe 4): Laenge, Frequenz, Trigger — muessen Bedingung 3 respektieren (Spieler darf nicht das Gefuehl haben, die Kontrolle "versehentlich" verloren zu haben; der Kontrollverlust muss als Konsequenz einer BEWUSST getroffenen Entscheidung lesbar sein)
- [ ] Narrativer Zustand "Schwelle" (Stufe 4): Welche Questgeber sind "echt"? Gibt es eine Metaebene, die dem Spieler Hinweise gibt? (Nami + Darius)

---

## 3. Nervensystem-Leveling

### 3.1 Systemuebersicht
- Vier physiologische Aeste statt klassischer Skill-Trees
- Begrenzte Leveling-Punkte pro Level-Up — Ressourcenkonkurrenz erzwingt Spezialisierung
- Visuelle Darstellung: Halbtransparente Nervensystem-Ansicht des Koerpers (Biotech-Futurismus)
- Progression ist KOERPERLICH, nicht abstrakt

### 3.2 Die vier Aeste

| Ast | Systeme | Kern-Attribute | Gameplay-Effekte |
|-----|---------|---------------|-----------------|
| **Cardio/Atmung** | Herz, Lunge, Kreislauf | Ausdauer, Regeneration, Bewegung | Sprint-Dauer, Schwimmen, Ausweich-Distanz, Erholungsrate |
| **Muskel/Skelett** | Muskeln, Knochen, Sehnen | Staerke, Resistenz, Waffenhandhabung | Schadensoutput, Block-Stabilitaet, Tragekapazitaet, Waffenfreischaltung |
| **Lymph/Immun** | Immunsystem, Stoffwechsel | Alchemie-Effizienz, Gift-Resistenz, Heilung | Trank-Wirkung, Krankheitsresistenz, passive Regeneration, Schattenfieber-Unterdrueckung |
| **Schatten** | Schattennervensystem | Schattensinne, Faehigkeiten, Wahrnehmung | NUR ab Infektionsstufe 1+; siehe Schattenfieber-System |

### 3.3 Trainer-System
- Faehigkeiten werden bei NPCs in der Welt gelernt, NICHT im Menu geklickt
- Jede Fraktion hat EXKLUSIVE Trainer (fuer bestimmte Faehigkeiten/Waffenstile)
- Trainer verlangen: Geld + Ruf + Vorbedingung (z.B. "Zeig mir, dass du parieren kannst")
- Gothic-Referenz: Die Welt ist das Klassenzimmer

### 3.4 Perks/Faehigkeiten-Prinzip
- TRANSFORMATIV, nicht numerisch — Perks veraendern WIE man spielt, nicht nur Zahlenwerte
- Korrekt: "Du kannst jetzt im Sprint angreifen" / "Paraden reflektieren Projektile"
- Falsch: "+20% Schwertschaden" / "+50 HP"
- Numerische Steigerungen kommen durch die Ast-Investition selbst, nicht durch einzelne Perks

### 3.5 Offene Design-Fragen
- [ ] Punkte pro Level-Up: Feste Anzahl oder skalierend?
- [ ] Max-Level: Reicht fuer wie viele Aeste? Empfehlung: 2 Aeste voll + 1 halb ODER 3 Aeste mittel
- [ ] Respec moeglich? Wenn ja, unter welchen Bedingungen? (Trainer? Kosten? Einmalig?)
- [ ] Visuelle Darstellung: Wie genau sieht die Nervensystem-Ansicht im UI aus? (Vera)

---

## 4. Alchemie und Crafting

### 4.1 Design-Philosophie
- Alchemie ersetzt Magie — es ist das primaere "uebernatuerliche" Werkzeug fuer Stufe-0-Spieler
- Wenige, bedeutsame Rezepte statt endloser Crafting-Listen
- Zutaten-Beschaffung als Explorations-Motivation
- Crafting ist NICHT endlos wiederholbar (begrenzte Zutaten, keine Respawn-Pflanzen)
- **Biotech-Forschung IST gefaehrlich** (CD-bestaetigt): Alchemie ist nicht sicher. Experimente koennen schiefgehen, Nebenwirkungen sind real. Das ist keine Bestrafungsmechanik, sondern Weltkonsequenz — in einer Welt, die auf einem toten Urwesen gebaut ist, ist jeder Eingriff in die Biologie ein Risiko.

### 4.2 Produktkategorien

| Kategorie | Funktion | Beispiele |
|-----------|----------|-----------|
| **Heilung** | HP-Wiederherstellung, Regeneration | Heiltrank (sofort), Regenerationstinktur (ueber Zeit) |
| **Combat-Buffs** | Temporaere Kampfverstaerkung | Waffenoele (Elementarschaden), Reflexelixier (Parry-Window +), Staerketrank |
| **Schattenfieber-Kontrolle** | Infektionswert beeinflussen | Suppressiva (senkt Wert), Stabilisatoren (verhindert Anstieg temporaer), Booster (erhoeht Wert bewusst fuer Faehigkeits-Burst) |
| **Gifte** | Offensiv, Waffen-Applikation | Laehmendes Gift (Ausdauer-Entzug), Nervenagent (Wahrnehmungsstoerung beim Feind), Kontaktgift (Falle) |
| **Utility** | Exploration, Ueberleben | Nachtsicht-Tinktur, Atem-Verlaengerer (Unterwasser), Klettergrip (verbesserte Haftung) |
| **Schutz** (neu) | Anti-Infektions-Praeparate | Schattenresistenz-Oel (temporaerer Schutz in verseuchten Zonen), Immunbooster (Infektionsanstieg halbiert fuer X Minuten) |

Die neue Kategorie "Schutz" ist ein direktes Ergebnis von Bedingung 3 (kein versehentliches Infizieren). Stufe-0-Spieler brauchen taktische Werkzeuge, um infektionsgefaehrliche Gebiete und Kaempfe zu bestreiten, OHNE sich zu infizieren. Das macht Alchemie fuer reine Spieler genauso wertvoll wie Schattenfieber-Faehigkeiten fuer infizierte Spieler.

### 4.3 Herstellungsprozess
- Zutaten finden (Exploration, Handel, Beute)
- Rezepte lernen (Trainer-Prinzip: Alchemisten-NPCs, Lore-Fragmente, Experiment)
- Herstellung an Alchemie-Stationen (feste Orte in der Welt, NICHT tragbar)
- Qualitaetsstufen: Basis → Verbessert → Meister (abhaengig von Lymph-Ast und Trainer-Rang)

### 4.4 Schnittstelle zu anderen Systemen
- **Lymph-Ast:** Bestimmt Trank-Wirkung und verfuegbare Rezepte
- **Schattenfieber:** Suppressiva als wichtigste Produktkategorie; hoher Infektionswert = schwaechere Alchemie-Wirkung (Trade-Off!)
- **Combat:** Waffenoele und Gifte als taktische Vorbereitung vor Kaempfen
- **Fraktionen:** Exklusive Rezepte pro Fraktion (Orden: Reinigungsmittel, Gilden: Handelsgifte, Krone: Militaertraenke)
- **Stufe-0-Spielpfad:** Schutz-Kategorie als mechanisches Aequivalent zu Schattenfieber-Resistenz (QA-validiert)

### 4.5 Offene Design-Fragen
- [ ] Rezeptanzahl fuer den Vertical Slice? Empfehlung: 15-20 Basisrezepte
- [ ] Experiment-System: Kann der Spieler Zutaten frei kombinieren? Oder nur bekannte Rezepte?
- [ ] Suchtmechanik: Haben Combat-Buffs Nebenwirkungen bei Ueberkonsum? (passt zur Briefing-Referenz "Echte Drogen, Amphetamine")
- [ ] Tiervolk als Alchemie-Haendler: Exklusive Zutaten? Andere Tradition?

---

## 5. Exploration und Weltnavigation

### 5.1 Weltstruktur
- Semi-Open-World: Eine zusammenhaengende Kernregion (~4-6 km²)
- Gothic-Dichte: Wenig Leerraum, hohe POI-Dichte, handplatziert
- Keine Schnellreise (oder: spaet freischaltbar, als Luxus, nicht als Notwendigkeit)
- Zusammenhaengende Oberwelt ohne Ladebildschirme

### 5.2 Vertikalitaet
- Staedte: Begehbare Dachlandschaften, Keller, Kanalisation, Bruecken, Turmebenen
- Wildnis: Klippen, Hoehlen, Baumkronen, Flussbetten, Bergpaesse
- Immer mehrere Wege: Hauptweg (sicher, lang), Schleichweg (riskant, kurz), Vertikalweg (Geschick erforderlich)
- Dishonored-Prinzip: Der Raum hat drei Dimensionen

### 5.3 Belohnungsstruktur
- Neugier wird IMMER belohnt: Abseits der Wege = Alchemie-Zutaten, Lore-Fragmente, versteckte NPCs, Schattenfieber-Hotspots
- Keine Quest-Marker auf der Karte (oder: minimal, abschaltbar) — Beschreibungen, Sightlines, NPC-Hinweise
- Umweltpuzzles: Kombination aus Beobachtung, Alchemie und Schattensinnen
- Handplatzierte Schaetze mit narrativer Einbettung (Warum liegt das hier? Wer hat es versteckt?)

### 5.4 Sichtbarkeitsschichten (Schattenfieber-Integration)
- Stufe 0: Normale Wahrnehmung — Geheimtueren und Fallen nur durch genaues Hinsehen findbar
- Stufe 1+: Schattensinne enthuellen versteckte Objekte, Geheimgaenge, vergiftete Gegenstaende
- Stufe 2+: Emotionsauren an NPCs, Tiefensicht fuer Schatzsuche
- Die Welt hat ZWEI Schichten — und Schattenfieber zeigt die zweite
- **Stufe-0-Alternative**: Alchemie (Nachtsicht-Tinktur), genaue Beobachtung, NPC-Hinweise — andere Methode, gleicher Inhalt (QA-validiert)

### 5.5 Points of Interest (Typen)

| Typ | Beispiele | Belohnung |
|-----|----------|-----------|
| **Siedlungen** | Staedte, Doerfer, Einzelhoefe | NPCs, Quests, Trainer, Handel |
| **Dungeons** | Katakomben, Minen, Ruinen, Ordensfestungen | Ausruestung, Lore, Boss-Gegner |
| **Schattenfieber-Zonen** | Verseuchte Gebiete, Ritualstaetten | Infektionsrisiko (mit Vorwarnung!), seltene Alchemie-Zutaten, Lore |
| **Landmarken** | Aussichtspunkte, Statuen, Ruinen | Kartenenthuelllung, Orientierung, Lore |
| **Verstecke** | Schmugglerlager, Diebesverstecke, Tiervolk-Lager | Handel (Schwarzmarkt), Quests, Alchemie |

### 5.6 Offene Design-Fragen
- [ ] Schnellreise: Ja/Nein? Wenn ja, unter welchen Bedingungen? Empfehlung: Erst im zweiten Akt, als narrative Belohnung
- [ ] Karte: Wie viel zeigt die Spielerkarte? Empfehlung: Handgezeichnet, wird durch Exploration aufgedeckt
- [ ] Tages-/Nachtzyklus: Welche Gameplay-Auswirkungen? NPC-Routinen, Gegnerverhalten, Schattenfieber-Intensitaet?
- [ ] Wetter: Reiner Atmosphaere-Effekt oder Gameplay-relevant? (z.B. Regen = besseres Schleichen, Nebel = eingeschraenkte Sicht)

---

## 6. Querschnittsthemen

### 6.1 Namenssysteme

> CD-Entscheidung: RELICS verwendet eigene Namenssysteme, KEINE nordisch/germanischen Namen in der Spielwelt.

- Fraktionen, Orte, Charaktere und Artefakte tragen eigene Namen, die zur Welt gehoeren
- Germanische Mythologie ist INSPIRATION, nicht Vorlage fuer die Nomenklatur
- Emres WBB-01 nutzt nordische Begriffe (Emer, Ginnungagap, etc.) als Arbeitsbegriffe — diese muessen VOR der V1-Produktion durch RELICS-eigene Namen ersetzt werden
- **Auswirkung auf GDD-02**: Stufennamen ("Rein", "Gezeichnet", "Infiziert", "Verwandelt", "Entfesselt") sind Arbeitsnamen und muessen geprueft werden — passen sie zum eigenen Namenssystem?
- **Zustaendig**: Emre (Namenssystem-Framework) + Nami (Charakternamen) + Darius (Systemnamen)

### 6.2 Build-Archetypen (emergent, nicht vordefiniert)

| Build | Schattenfieber | Schwerpunkte | Spielstil |
|-------|---------------|-------------|-----------|
| Reiner Krieger | Stufe 0 | Muskel + Cardio | Schwere Waffen, Ausdauer, volles Parry |
| Alchemist | Stufe 0-1 | Lymph + Cardio | Trank-fokussiert, Gifte, Buff-Oele, Schutz-Praeparate |
| Schattenspaether | Stufe 1-2 | Schatten + Cardio | Exploration, Stealth, Schatten-Schritt |
| Hybrid-Kaempfer | Stufe 2-3 | Muskel + Schatten | Risk/Reward, explosive Spitzen |
| Schattenbestie | Stufe 3-4 | Schatten (voll) | Glass Cannon, sozialer Aussenseiter, Parallel-Narrativ |

### 6.3 System-Interaktionen

```
COMBAT <-> SCHATTENFIEBER
  Schattenreflex erweitert Parry
  Fieber-Puls als AoE (kostet HP)
  Infizierte Feinde = Vorschau eigener Faehigkeiten
  Schutz-Alchemie als Stufe-0-Alternative (QA)

SCHATTENFIEBER <-> NERVENSYSTEM
  Vierter Ast konkurriert um Leveling-Punkte
  Hohe Infektion = schwache konventionelle Aeste
  Spezialisierung vs. Breite

ALCHEMIE <-> SCHATTENFIEBER
  Suppressiva senken Infektionswert
  Booster erhoehen ihn bewusst
  Schutz-Praeparate verhindern Anstieg (Stufe-0-Werkzeug)
  Lymph-Ast bestimmt Alchemie-Effizienz

EXPLORATION <-> SCHATTENFIEBER
  Verseuchte Zonen erhoehen Infektion (MIT Vorwarnung)
  Schattensinne enthuellen versteckte Inhalte
  Stufe-0-Alternative: Alchemie + Beobachtung
  Exploration belohnt mit Alchemie-Zutaten

FRAKTIONEN <-> SCHATTENFIEBER
  Infektionsstufe beeinflusst Fraktionszugang
  Exklusive Trainer/Rezepte pro Fraktion
  Orden bietet Reinigung, jagt aber ab Stufe 3

NARRATIV <-> SCHATTENFIEBER (Nami-Sync)
  Rauschen: Subtile Textverschiebungen (Stufe 1-2)
  Risse: Alternative Dialoge, fragwuerdige Questgeber (Stufe 3)
  Schwelle: Parallel-Narrativ, unentscheidbare Realitaet (Stufe 4)
  Schattenfieber-Dialoge sind spielbar, nicht nur atmosphaerisch
```

### 6.4 Balancing-Leitlinien
- Stufe 0 = gleichwertig zu Stufe 4 — ANDERE Erfahrung, nicht schlechtere
- Keine "Best Build"-Situation — Trade-Offs muessen echt sein
- Die Welt-Schwierigkeit wird durch Geographie bestimmt, nicht durch Slider
- Vertikaler Fortschritt (maechtig werden) UND horizontaler Fortschritt (anders werden)
- Stufe-0-Aequivalent-Tabelle (2.5) als Balancing-Grundlage
- QA-Schleife: Leo prueft jede Mechanik aus Spielersicht — 40% Fokus auf Schattenfieber

### 6.5 QA-Risikomatrix (Leo-Input)

| Risiko | Schwere | Wahrscheinlichkeit | Mitigation |
|--------|---------|---------------------|------------|
| Versehentliche Infektion | KRITISCH | Hoch (ohne Massnahmen) | Bedingung 3 + Schutz-Alchemie + UI-Warnungen |
| Stufe 0 fuehlt sich leer an | HOCH | Mittel | Stufe-0-Aequivalente, exklusive Alchemie-Inhalte |
| Stufenuebergaenge fuehlbar machen | HOCH | Hoch | Gradueller Uebergang, QA pro Infektionswert |
| Kontrollverlust frustriert statt fasziniert | MITTEL | Mittel | Transparenz, Spieler muss Konsequenz vorher verstehen |
| Community-Backlash "nicht heilbar" | MITTEL | Sicher | Transparente Kommunikation VOR Release, "kontrollierbar" als Frame |
| Schattenfieber-Dialoge brechen Quests | HOCH | Hoch | Systematisches Testing aller Quest-States x Infektionsstufen |

---

## 7. Zusammenfassung: Naechste Schritte

| Aufgabe | Verantwortlich | Timeline | Status |
|---------|---------------|---------|--------|
| QA-Schleife: Spielerperspektive auf GDD-02 | Darius + Leo | Tag 2 Nachmittag | ERLEDIGT (V0.5) |
| Schattenfieber-Stufen-Mapping mit Nami | Darius + Nami | Tag 2 Nachmittag | ERLEDIGT (V0.5) |
| Schutz-Alchemie-Kategorie mit Nami validieren (narrativer Sinn) | Darius + Nami | Tag 3 | Offen |
| Lebende Krone: Interaktionsdesign | Darius + Emre | Tag 3 | Offen |
| RELICS-eigene Namenssysteme | Emre + Nami + Darius | Tag 3-4 | Offen |
| Combat-Detail: Waffenklassen-Movesets | Darius | Tag 3 (V1) | Offen |
| Alchemie-Rezeptliste (V1) inkl. Schutz-Kategorie | Darius | Tag 3 (V1) | Offen |
| Balancing-Framework (Stufe 0 vs. Stufe 4) | Leo + Darius | Tag 3 (V1) | Vorbereitet (Aequivalent-Tabelle) |
| Kontrollverlust-Episoden: Detail-Design | Darius + Vera + Tobi | Tag 4 | Offen |
| Transparenz-UI: Wireframes | Vera + Darius | Tag 4 | Offen |

---

*Darius Engel, Game Design Corner, Tag 2 Nachmittag — V0.5 nach QA-Schleife mit Leo und Stufen-Sync mit Nami*
*Leo Fischer, Tag 5 Nachmittag — V0.5.1: Ymir → Emer (Kap. 2.7 + 6.1)*

\clearpage

# GDD-03 — Erzaehlkonzept

**Autorin:** Nami Okafor, Narrative Design
**Version:** V2 (Tag 5, Freitag — Finalisierung)
**Status:** Volltext finalisiert; Beat-Sheet auf Szenenebene ausgearbeitet; Charakter-Quest-Figur definiert (Maret); Fraktionsquests auf Szenenebene konkretisiert
**Aenderungslog:**
- V1 (Tag 3, Mittwoch): Ausformulierter Volltext — Narrative Prinzipien, Drei-Akt-Bogen, Quest-Architektur V1, Dialogsystem, Schattenfieber als narratives System, Wanderer-Identitaet
- V2 (Tag 5, Freitag): Beat-Sheet auf Szenenebene (Hauptquest, 3.3); Fraktionsquests von Skizze zu konkreten Beats (3.4); Charakter-Quest-Figur Maret eingesetzt (3.6); Dialog-Beispiele erweitert; offene Fragen aktualisiert
**Abhaengigkeiten:** WBB-01 Mythos (Emre, V1, integriert), GDD-01 Spieluebersicht (Darius, V1, integriert), GDD-02 Kernmechaniken (Darius/Leo, V0.5, integriert), GDD-04 Schluesselfiguren (Nami, V1 heute, verlinkt)

---

## 1. Narrative Prinzipien

Die folgenden vier Prinzipien sind keine Empfehlungen. Sie sind Gesetze. Jede Quest, jeder Dialog, jede Cutscene, jeder Umgebungstext in RELICS muss gegen mindestens eines dieser Prinzipien validierbar sein. Wenn ein narrativer Inhalt gegen ein Prinzip verstoesst, wird er ueberarbeitet oder gestrichen. Es gibt keine Ausnahmen, und es gibt keine Szene, die zu klein ist, um geprueft zu werden.

### 1.1 Fremder als Zustand

Der Spieler ist kein Held mit Amnesie. Er ist kein Auserwaehlter, der seine Bestimmung noch nicht kennt. Er ist kein Soeldner mit dunkler Vergangenheit. Er ist ein Niemand — und das ist sein staerkstes Werkzeug.

Fremdheit ist in RELICS kein narratives Problem, das im Laufe der Geschichte geloest wird. Sie ist der Aggregatzustand der gesamten Spielerfahrung. Der Spieler beginnt als Fremder und er endet als Fremder — auch wenn sich die Form seiner Fremdheit veraendert hat. Wer einer Fraktion beitritt, hoert nicht auf, fremd zu sein. Er tauscht eine Art der Fremdheit gegen eine andere: die Fremdheit des Aussenseiters gegen die Fremdheit dessen, der dazugehoert und trotzdem nicht ganz passt. Wer die Lebende Krone beruehrt, wird nicht einheimischer — er wird fremder, auf eine Art, die tiefer reicht als Geografie.

Dieses Prinzip hat eine konkrete Design-Konsequenz: Kein NPC in RELICS erklaert dem Spieler die Welt, als waere er ein Tourist. NPCs leben in ihrer Welt. Sie setzen voraus, was jeder weiss. Sie erwaehnen beilaeufig, was fuer sie selbstverstaendlich ist. Der Spieler muss zuhoeren, beobachten, kombinieren. Die Welt schuldet ihm keine Exposition — er muss sich das Verstaendnis verdienen, so wie er sich Zugang zu Fraktionen, Trainern und Gebieten verdienen muss.

**Validierungstest:** Gibt es in dieser Szene einen Moment, in dem ein NPC dem Spieler etwas erklaert, das er einem Einheimischen nie erklaeren wuerde? Dann ueberarbeiten.

### 1.2 Fraktionen als Sprachen

In RELICS haben die drei Fraktionen nicht nur unterschiedliche Ziele. Sie haben unterschiedliche Woerter fuer dieselben Dinge. Die Krone nennt die kosmologische Erosion "die Faulung" und meint damit Strafe. Die Gilden nennen sie "den Schwund" und meinen damit Verlust. Der Orden nennt sie "die Entflechtung" und meint damit ein Geheimnis. Dasselbe Phaenomen, drei Vokabulare, drei Weltsichten, die sich nicht auf einen gemeinsamen Nenner bringen lassen — weil der gemeinsame Nenner voraussetzen wuerde, dass eine der drei Perspektiven objektiv ist, und das ist keine von ihnen.

Fraktionszugehoerigkeit veraendert in RELICS nicht primaer, was der Spieler SAGEN kann. Sie veraendert, was er ZU HOEREN BEKOMMT. Ein Krone-alliierter Spieler erhaelt Informationen in der Sprache der Krone — in ihren Metaphern, mit ihren Auslassungen, nach ihren Prioritaeten. Ein Gilden-alliierter Spieler erhaelt dieselben Informationen anders gerahmt, mit anderen Betonungen, mit anderen blinden Flecken. Der Spieler, der RELICS zweimal spielt — einmal als Krone, einmal als Orden — erlebt nicht zwei verschiedene Geschichten. Er erlebt dieselbe Geschichte in zwei verschiedenen Sprachen und begreift erst durch den Vergleich, was in beiden Versionen fehlte.

Emres WBB-01 liefert das kosmologische Fundament fuer dieses Prinzip. Die Schoepfungsgeschichte des Emer existiert in drei Versionen, und keine ist falsch. Die Krone singt von Sigvalts Pflicht-Opfer, die Gilden schreiben von Erthags Investition, der Orden verschluesselt Halvards Erkenntnis. Der Spieler wird im Laufe des Spiels alle drei Versionen hoeren — und muss selbst entscheiden, ob er eine glaubt, alle drei zusammenfuegt oder keine von ihnen fuer bare Muenze nimmt.

**Validierungstest:** Koennte dieselbe Information, die in dieser Szene vermittelt wird, von einer anderen Fraktion voellig anders praesentiert werden — mit anderem Vokabular, anderer Betonung, anderen Auslassungen? Wenn nicht, ist sie fraktionsneutral und muss geprueft werden, ob das beabsichtigt ist.

### 1.3 Raeume als Erzaehler

Der beste Expositions-NPC in RELICS ist kein NPC. Es ist ein leerer Thronsaal, in dem noch Blut auf dem Boden steht. Ein verlassener Marktplatz, auf dem die Waagen noch haengen. Ein Ordensarchiv, in dem jemand systematisch Seiten aus Kodizes gerissen hat.

Environmental Storytelling ist in RELICS kein Bonus, kein Easter Egg, kein Nice-to-Have. Es ist der primaere Erzaehlkanal fuer Weltgeschichte. Die Vergangenheit wird nicht erzaehlt — sie wird hinterlassen. Was geschehen ist, steht nicht in Buechern (obwohl es auch dort steht), sondern in der Anordnung von Gegenstaenden, in der Architektur von Gebaeuden, in den Rissen in den Waenden und den Flecken auf den Boeden. Der Spieler, der genau hinsieht, versteht mehr als der Spieler, der nur Dialoge abklappert. Beide Spielweisen sind gueltig — aber die Umgebung belohnt Aufmerksamkeit auf eine Art, die kein Dialogbaum bieten kann.

Dieses Prinzip erfordert enge Abstimmung mit Vera (Art Direction) und Emre (Topos). Jeder Raum braucht eine Erzaehlabsicht — nicht jeder Raum muss eine Geschichte erzaehlen, aber kein Raum darf zufaellig aussehen. Auch Leere ist eine Aussage, wenn sie gestaltet ist.

**Validierungstest:** Koennte der Spieler diese Szene verstehen, wenn er alle Dialoge ueberspringt und nur die Umgebung beobachtet? Wenn nicht: Fehlt dem Raum etwas, oder ist der Dialog eine Kruecke?

### 1.4 Schattenfieber als Unreliable Narrator

Das Schattenfieber veraendert nicht nur den Koerper des Spielers und nicht nur seine mechanischen Faehigkeiten. Es veraendert die Erzaehlung selbst. Was der Spieler sieht und hoert, ist ab einem bestimmten Infektionsgrad nicht mehr zuverlaessig — und das Spiel sagt ihm nicht, wann dieser Punkt erreicht ist.

Das ist kein Bug. Das ist kein unfairer Design-Trick. Das ist der Kern der narrativen Erfahrung von RELICS.

Ein Spieler mit hohem Schattenfieber erlebt eine andere Geschichte als ein Spieler ohne. Er sieht Dinge, die der andere nicht sieht. Er hoert Saetze, die der andere nicht hoert. Er fuehrt Gespraeche mit Figuren, die moeglicherweise nicht existieren — oder die existieren, aber anders reden, als der saubere Spieler es erlebt. Die Frage, welche Version die "wahre" ist, ist eine Frage, die RELICS nicht beantwortet. Moeglicherweise ist die Version des infizierten Spielers naeher an der kosmologischen Realitaet — an dem, was hinter den Hauten liegt. Moeglicherweise ist sie reine Halluzination. Moeglicherweise beides.

Dieses Prinzip ist gleichzeitig der groesste narrative Reiz und das groesste Design-Risiko von RELICS. Es funktioniert nur, wenn die Schattenfieber-Varianten SPIELBAR sind — wenn sie nicht nur atmosphaerisches Rauschen erzeugen, sondern mechanisch relevante Informationen liefern, die zu echten Spielerentscheidungen fuehren. Schattenfieber-Dialoge duerfen keine Sackgassen sein. Sie muessen alternative Wege oeffnen, die nur dem infizierten Spieler zugaenglich sind — genauso, wie die "saubere" Version Wege oeffnet, die dem Infizierten verschlossen bleiben.

**Validierungstest:** Ist jede Schattenfieber-Dialogvariante mechanisch relevant — fuehrt sie zu einer Spielerentscheidung, einer Information, einem Zugang, der sonst fehlt? Wenn sie nur atmosphaerisch ist, reicht das nicht.

---

## 2. Erzaehlrahmen

### 2.1 Praemisse

In einem Mittelgrund am Rande der Faulung ringt ein Fremder um seinen Platz in einer Welt, die ihm keinen schuldet.

Das Relikt dieser Iteration — die Lebende Krone — ist das Objekt, um das die Handlung kreist. Die Krone ist kein MacGuffin. Sie ist kein Schatz, den man am Ende aufhebt und den Abspann sieht. Die Lebende Krone ist ein Organismus, der mit seinem Traeger verschmilzt, die Hauten zwischen den Daseinsebenen stabilisiert und jeden, der sie beruehrt, fundamental veraendert. Sie ist Machtsymbol, kosmologisches Werkzeug und Fluch zugleich — und jede Fraktion sieht nur den Aspekt, der zu ihrer Weltsicht passt.

Die zentrale Frage der Hauptquest lautet nicht: Wer bekommt die Krone? Sie lautet: Was geschieht mit dem, der sie traegt — und was geschieht mit der Welt, wenn niemand sie traegt?

### 2.2 Drei-Akt-Struktur

#### Akt I — Ankunft (ca. 20% Spielzeit)

Der Spieler kommt als Fremder in den Mittelgrund. Ohne Namen, ohne Ruf, ohne Verbindungen. Er hat nicht einmal einen klaren Grund, hier zu sein — jedenfalls keinen, den er kennt.

**Beat 1 — Gastrecht.** Die erste Stunde ist ein Gastrecht-Szenario. Der Spieler wird aufgenommen — misstrauisch, widerwillig, aber aufgenommen, denn das Gastrecht ist in dieser Welt keine Hoeflichkeit, sondern eine kosmologische Verpflichtung. Wo Gastrecht gebrochen wird, werden die Hauten duenner — Aberglaube, sagen die Gilden. Wahrheit, fluestert der Orden. Die Gastrecht-Sequenz dient als narratives Tutorial: Der Spieler lernt, dass Worte in dieser Welt Gewicht haben, dass Versprechen Konsequenzen haben, und dass jede der drei Fraktionen unter "Gastfreundschaft" etwas anderes versteht. Kein UI-Popup erklaert ihm das. Er erlebt es.

**Beat 2 — Die drei Stimmen.** Im Verlauf von Akt I begegnet der Spieler allen drei Fraktionen in ihrem natuerlichen Kontext. Keine Rekrutierungsszenen, keine Fraktions-Expo. Stattdessen: Ein Krone-Soldat, der eine Strasse bewacht und den Spieler passieren laesst — oder nicht, je nachdem, wie er sich im Gastrecht-Szenario verhalten hat. Eine Gilden-Haendlerin, die dem Spieler Arbeit anbietet — keine edle, eine dreckige. Ein Ordenspriester, der Infizierte segnet oder verbannt, je nach Stimmung und Laune seines Vorgesetzten. Der Spieler beobachtet, bewertet, waehlt nicht — noch nicht.

**Beat 3 — Das erste Zeichen.** Am Ende von Akt I erlebt der Spieler den ersten Kontakt mit den Auswirkungen der Lebenden Krone. Nicht mit dem Artefakt selbst — das kommt spaeter. Sondern mit dem, was es hinterlassen hat: Ein Ort, an dem die Hauten duenn sind. Ein NPC, der Dinge sieht, die nicht da sind — oder die nur ER sieht. Ein Stueck Welt, das sich falsch anfuehlt, das zu viel ist, das nicht ganz in den Mittelgrund passt. Der Spieler versteht noch nicht, was er gesehen hat. Aber er hat es gesehen, und das reicht.

*Akt-I-Ziel:* Der Spieler hat ein Gefuehl fuer die Welt, ein grobes Verstaendnis der Fraktionsdynamik und eine Frage, die ihn in Akt II treibt: Was ist hier falsch?

#### Akt II — Verstrickung (ca. 50% Spielzeit)

Die laengste Phase. Der Spieler wird hineingezogen — nicht als Auserwaehlter, sondern als Unbeteiligter, der zu viel gesehen hat. Das Schattenfieber wird narrativer Faktor. Die Fraktionen werden konkreter, dringlicher, fordernder. Die Lebende Krone tritt als Streitobjekt in die Handlung ein.

**Beat 4 — Fraktionspositionierung.** Der Spieler wird aufgefordert, sich zu positionieren. Nicht beitreten — noch nicht. Aber eine Fraktion unterstuetzen, einen Auftrag uebernehmen, sich einem Lager zuordnen. Diese Positionierung oeffnet Zugaenge: neue NPCs, neue Orte, neue Informationen. Sie schliesst noch nichts — aber sie verschiebt die Gewichte.

**Beat 5 — Die Krone tritt ein.** Der Spieler erfaehrt, was die Lebende Krone ist — und dass alle drei Fraktionen sie wollen, aus voellig unterschiedlichen Gruenden. Die Krone beansprucht sie als dynastisches Erbe: Wer die Krone traegt, haelt die Welt zusammen. Die Gilden wollen sie kontrollieren: ein unbezahlbares Gut, das den Markt sprengt. Der Orden will sie studieren: ein Erkenntnisschluessel, der alle Geheimnisse oeffnen koennte. Der Spieler sieht, wie die Krone die letzten Traeger veraendert hat — die "nicht mehr ganz von dieser Art" waren, wie die vorsichtigen Chroniken es formulieren. Die Krone frass ihre Traeger, sagen die direkteren.

**Beat 6 — Point of No Return.** Der Spieler muss sich einer Fraktion verpflichten. Oder er versucht, neutral zu bleiben — was moeglich ist, aber Konsequenzen hat: Neutralitaet in einem Machtkampf ist keine neutrale Position. Alle drei Fraktionen behandeln den Neutralen als potenzielle Bedrohung, als jemanden, der sich nicht einordnen laesst. Das Tiervolk kennt diesen Zustand — sie sind es gewohnt, keiner Seite zu gehoeren. Ob der Spieler das als Freiheit oder als Isolation erlebt, haengt davon ab, wie er spielt.

**Beat 7 — Schattenfieber-Eskalation.** Wenn der Spieler infiziert ist, veraendern sich ab hier Szenen. Dialoge verschieben sich. NPCs reagieren anders — nicht nur sozial (Angst, Mitleid, Abscheu), sondern informativ: Sie sagen andere Dinge, weil der infizierte Spieler andere Fragen stellt oder andere Antworten hoert. Die Hauten werden duenner an bestimmten Orten, und der Spieler — wenn sein Infektionsgrad hoch genug ist — beginnt, die Schichten wahrzunehmen: Fragmente des Stillfelds, Echos des Hohlichts. Ob das real ist oder Halluzination, wird nicht geklaert.

*Akt-II-Ziel:* Der Spieler hat sich positioniert, die Krone als zentrales Objekt erkannt und verstanden, dass jede Loesung einen Preis hat, den keine Fraktion offen ausspricht.

#### Akt III — Konsequenz (ca. 30% Spielzeit)

Das Endspiel. Die Faulung beschleunigt sich. Die Hauten werden duenner. Die Frage ist nicht mehr, ob jemand die Krone tragen wird, sondern wer — und was danach von ihm uebrig bleibt.

**Beat 8 — Die Krone erreichen.** Der Spieler gelangt — durch fraktionsspezifische Wege — an die Lebende Krone. Was er dort vorfindet, haengt von seinem Schattenfieber-Status ab. Ein sauberer Spieler sieht ein Artefakt in einem Thronsaal oder einer Krypta oder einem Labor. Ein infizierter Spieler sieht mehr — oder weniger: Die Krone ist lebendig, sie pulsiert, sie reagiert auf seine Naehe. Bei hoher Infektionsstufe verschwimmt die Grenze zwischen dem Objekt und dem Ort, der es beherbergt. Der Raum atmet. Die Waende erinnern sich.

**Beat 9 — Entscheidung.** Der Spieler steht vor der zentralen Entscheidung. Sie ist fraktionsspezifisch und schattenfieberspezifisch — die Kombination aus beidem erzeugt die Varianz.

Die Krone-Route fragt: Traegst du die Krone, um die Ordnung zu bewahren — obwohl du weisst, was sie mit ihren Traegern macht? Ist Pflicht mehr wert als dein Selbst?

Die Gilden-Route fragt: Kontrollierst du die Krone, ohne sie zu tragen — als Ressource, als Instrument, als Ware? Und was passiert mit der Welt, wenn niemand sie traegt und die Hauten weiter duenner werden?

Die Orden-Route fragt: Studierst du die Krone, oeffnest du die Erkenntnis — und riskierst du dabei, das zu entfesseln, was die Flechtung einst gebunden hat?

Die neutrale Route fragt: Laesst du die Krone, wo sie ist? Und kannst du mit der Antwort leben, dass du die Welt ihrem Schicksal ueberlassen hast?

**Beat 10 — Konsequenz.** Die Folgen der Entscheidung sind nicht als Cutscene erzaehlt, sondern spielbar. Der Spieler erlebt — in einer finalen Sequenz, die je nach Fraktionswahl und Infektionsgrad variiert — was seine Entscheidung bedeutet. Kein Erzaehler fasst zusammen. Kein Textcrawl erklaert, was danach geschah. Der Spieler sieht es selbst — so gut er sehen kann. Und wenn sein Schattenfieber hoch genug ist, sieht er moeglicherweise mehr als das, was wirklich passiert. Oder weniger. Oder beides.

*Akt-III-Ziel:* Der Spieler hat eine Entscheidung getroffen, deren Konsequenzen er spuert, aber nicht vollstaendig ueberschaut. Er hat das Gefuehl, dass ein zweiter Durchgang — mit einer anderen Fraktion, einem anderen Infektionsgrad — eine andere Wahrheit zeigen wuerde.

### 2.3 Erzaehlton

Drei Regeln fuer den Ton von RELICS:

**Knapp, nie expositiv.** NPCs erklaeren die Welt nicht — sie leben darin. Kein Charakter haelt einen Vortrag ueber die Geschichte der Grossen Flechtung. Stattdessen erwaehnt eine Krone-Wache beilaeufig "das Flechtfest", als waere es Allgemeinwissen — und der Spieler muss selbst herausfinden, was damit gemeint ist.

**Poetisch, nie opulent.** Die Sprache darf Gewicht haben. Ein Satz darf schoen sein. Aber jedes Wort muss verdient sein. Gotische Grandeur heisst nicht, dass NPCs in Metaphern schwimmen. Es heisst, dass die richtigen Woerter an den richtigen Stellen fallen — und dass Stille ebenso viel sagt wie Sprache.

**Politisch, nie neutral.** Jedes Gespraech in RELICS hat Subtext. Niemand sagt genau das, was er meint. Die Krone-Wache, die dem Spieler den Weg weist, weist ihm gleichzeitig seinen Platz zu. Die Gilden-Haendlerin, die ihm einen fairen Preis macht, kalkuliert gleichzeitig seinen Nutzen. Der Ordenspriester, der ihm Wissen anbietet, prueft gleichzeitig seine Zuverlaessigkeit. RELICS ist ein Spiel, in dem hoefliche Gespraeche gefaehrlicher sein koennen als offene Feindschaft.

---

## 3. Quest-Architektur

### 3.1 Grundregeln

**Regel 1: Kein Filler.** Es gibt keine Quests, die nur existieren, um eine Spielstrecke zu fuellen. Keine Fetch-Quests. Kein "Bring mir zehn Kraeuterbeutel." Jede Quest muss mindestens eines der vier narrativen Prinzipien spuerbar machen. Wenn eine Quest diesen Test nicht besteht, wird sie gestrichen — nicht ueberarbeitet, gestrichen.

**Regel 2: Kein Auserwaehlter.** Der Spieler wird in keine Quest als prophezeiter Held gerufen. Er stolpert hinein, wird hineingezogen, wird benutzt oder bittet sich selbst an. Das Motiv ist nie "Du bist der Einzige, der das kann." Das Motiv ist: "Du bist hier, du schuldest mir etwas, und ich sehe keinen besseren Kandidaten."

**Regel 3: Konsequenz ueber Aufloesung.** Quests muessen kein gutes Ende haben. Sie muessen nicht einmal ein klares Ende haben. Was sie haben muessen, ist Konsequenz — das Gefuehl, dass die Entscheidung des Spielers etwas veraendert hat, das sich nicht zuruecknehmen laesst. Der beste Ausgang einer Quest ist nicht der gluecklichste, sondern der, den der Spieler vor sich selbst verantworten kann.

### 3.2 Intro-Sequenz / Tutorial Quest

**Titel:** Der Gast

**Funktion:** Der Spieler erlernt die Kernmechaniken DURCH eine narrative Situation. Kein UI-Tutorial, keine schwebenden Textboxen. Die Welt ist das Tutorial.

**Setting:** Der Spieler kommt als Fremder an — die Umstaende seines Kommens bleiben vage, absichtlich. Er erreicht einen Grenzort: nicht die Hauptstadt, nicht das Zentrum, sondern die Peripherie, dort, wo Kontrolle duenner ist und Gastrecht noch etwas bedeutet.

**Narrativer Bogen:** Ein lokaler Wirt gewaehrt dem Spieler Gastrecht. Die Regeln des Gastrechts — Feuer, Nahrung, Schutz; dafuer Rede und Gegenrede — werden nicht als Textbox erklaert, sondern als soziale Situation erlebt. Der Spieler muss antworten, sich verhalten, eine Haltung einnehmen. Ein Konflikt entsteht — ein kleiner, lokaler, dringender Konflikt, der die Fraktionsdynamik im Miniatur zeigt. Die Loesung des Konflikts lehrt Kampfbasis, Gespraechsfuehrung und Umgebungsbeobachtung.

**Laenge:** 15-20 Minuten.

**Prinzip-Validierung:** Fremder als Zustand. Raeume als Erzaehler.

### 3.3 Hauptquest — Die Lebende Krone (Beat-Sheet V2)

**Struktur:** Drei Akte, zehn Beats. Die Beats sind nicht streng linear — manche koennen in variabler Reihenfolge absolviert werden, manche sind fraktionsspezifisch, manche veraendern sich mit dem Schattenfieber-Status. Zwei harte Verzweigungspunkte: Beat 6 (Fraktionsverpflichtung) und Beat 9 (Entscheidung). Dazwischen weiche Varianz.

| Beat | Akt | Titel | Beschreibung (V2 — Szenenebene) | SF-Varianz |
|------|-----|-------|--------------------------------|------------|
| 1 | I | **Gastrecht** | Ankunft am Grenzort. Ein Wirt prueft den Spieler — nach Gastrechts-Formel, aber mit Krone-Beauftragten im Ruecken. Der Spieler muss entscheiden: Wahrheit oder Rolle. Erste Mechanik-Exposition. | Keine |
| 2 | I | **Die drei Stimmen** | Drei kurze, nicht-ausdehnbare Begegnungen: (a) Krone-Sergeant, der eine Strasse sperrt; (b) Gildenhilfsarbeiter, der Informationen verkauft; (c) Ordenspriester, der einen Infizierten in der Menge beobachtet. Spieler beobachtet, entscheidet nichts. | Keine |
| 3 | I | **Das erste Zeichen** | Ein Ort am Stadtrand — ein aufgegebenes Gehoefte mit duennen Hauten. Kein Questgeber, kein Marker. Der Spieler findet es durch Neugier oder durch den Seher Maret, der ihn hinfuehrt. Die Erfahrung ist uninterpretierbar. Sie bleibt. | Keine direkte — Maret ist auch ohne SF erreichbar |
| 4 | II | **Fraktionsannaehrung** | Erste Auftrag-Szene fuer eine Fraktion (Spielerwahl). Auftrag ist klein, dreckig, konsequent: Der Spieler macht sich nuetzlich. Ein zweiter NPC beobachtet. Er wird spaeter wichtig. | SF-Stufe 1+: Umgebungshinweise verschieben sich, ein Satz im Briefing ist leicht anders |
| 5 | II | **Die Krone tritt ein** | Spieler erfaehrt vom Artefakt. Nicht durch Exposition — durch eine Konsequenz: Jemand, der die Krone beruehrt hat, ist gerade dabei, damit umzugehen. Was von ihm uebrig ist, sieht der Spieler. Was die Fraktionen dazu sagen, lernt er durch drei kurze Reaktions-Szenen. | SF-Stufe 1+: Schattensinne zeigen, was andere nicht sehen: Der betroffene NPC ist nicht ganz weg. Er ist noch hier — in einer anderen Schicht |
| 6 | II | **Point of No Return** | Fraktionsverpflichtung oder bewusste Neutralitaet. Szene: Ein Rat der drei Fraktionen fordert den Spieler auf, Position zu beziehen. Nicht mit Worten — mit einer Handlung, die nicht zurueckgenommen werden kann. | SF-Stufe 2+: Der Spieler hoert einen vierten Satz im Rat, den niemand gesprochen hat |
| 7 | II | **Die Suche** | Fraktionsspezifischer Questpfad zur Krone. Drei verschiedene Wege (Krone: durch Archiv-Zugang; Gilden: durch Haendlernetz; Orden: durch Schattenfieber-Kartierung). Jeder Weg zeigt andere Seite desselben Artefakts. | SF-Stufe 3+: Alternative Questgeber auf dem Weg — fragwuerdige Figuren, die nur der Infizierte sieht |
| 8 | III | **Die Krone erreichen** | Spieler steht vor dem Artefakt. Der Ort ist je nach Fraktionsweg verschieden. Die Krone reagiert auf die Naehe des Spielers — leise, fast unmerklich fuer einen sauberen Spieler, ueberwaeltigend fuer einen infizierten. | SF-Stufe 3+: Der Raum erinnert sich. Die Waende zeigen Echos vergangener Traeger |
| 9 | III | **Entscheidung** | Vier Wege (Krone/Gilden/Orden/neutral), ausformuliert in Abschnitt 2.2. Keine Option ist eindeutig richtig. Jede hat einen Preis, den die Fraktion nicht kommuniziert hat. | SF-Stufe 4: Parallel-Narrativ. Der Spieler weiss nicht sicher, welche Entscheidung er getroffen hat |
| 10 | III | **Konsequenz** | Spielbare Folge-Sequenz, ca. 10-15 Minuten. Kein Textcrawl. Der Spieler sieht das Ergebnis durch eigene Augen — so klar oder so verzerrt, wie seine Infektion es erlaubt. | SF-Stufe 4: Das Ende ist eine andere Geschichte |

### 3.4 Fraktionsquests (V2 — konkrete Beats)

Jede Fraktionsquest hat ein zentrales Dilemma, das die Fraktion in sich spaltet. Die Quest fuehrt den Spieler in die Fraktion HINEIN, in ihre Risse, in ihre Widersprueche, in das, was sie sich selbst nicht eingestehen will.

#### Die Krone — "Pflicht und Verfall"

**Schluessfigur:** Aldine Vor, Kronenfuehrerin (→ GDD-04)
**Thema:** Loyalitaet gegenueber einer sterbenden Ordnung.
**Ton:** Elegisch. Formell. Die Sprache der Pflicht, die sich selbst ueberlebt hat.
**Kern-Dilemma:** Die Krone weiss — tief in sich, an den Stellen, die sie nicht anschaut —, dass die alte Ordnung nicht zurueckkommt. Die letzten Traeger der Lebenden Krone waren veraendert. Die Dynastie ist moeglicherweise am Ende. Und die tragischste Ironie: Die Krone setzt Biotechnologie ein, die genau die Hauten destabilisiert, die die Lebende Krone stabilisieren soll. Sie untergreabt ihre eigene Grundlage, ohne es zu wissen.

| Beat | Titel | Szenenbeschreibung |
|------|-------|--------------------|
| 1 | **Dienst** | Spieler beweist sich als brauchbar — kein Titel, keine Ehre, nur Funktion. Aldine Vor beobachtet ihn durch einen Bericht, nicht durch persoenliche Begegnung. Sie entscheidet auf Basis von Nuetzlichkeit. |
| 2 | **Der innere Riss** | Spieler entdeckt, dass eine Krone-Einheit Biotech-Substanzen einsetzt, die die Faulung verstaerken. Nicht absichtlich. Aus Unwissen. Oder aus Gleichgueltigkeit. Der Offizier, den der Spieler befragt, weiss es nicht. Aldine Vor weiss es. Sie hat es priorisiert weggesehen. |
| 3 | **Der letzte Traeger** | Spieler findet Spuren des letzten Krone-Traegers der Lebenden Krone. Was von ihm uebrig ist, widerspricht der offiziellen Version. Aldine Vor weiss es. Sie hat ihn begraben lassen, ohne Zeremonie, ohne Bericht. |
| 4 | **Loyalitaet oder Einsicht** | Spieler muss entscheiden: Die Wahrheit verschweigen und die Krone-Fraktion stabil halten — oder sie aussprechen und die Fraktion in eine Krise stuerzen, die moeglicherweise der Beginn von etwas Besserem ist. Aldine Vor fragt ihn nicht danach. Sie setzt voraus, dass er schweigt. |

**Letzter Dialog — Aldine Vor, wenn der Spieler schweigt:**

> "Du hast es gesehen. Ich sehe, dass du es gesehen hast. Und du sagst nichts. Das ist die erste intelligente Entscheidung, die du in meinem Dienst getroffen hast."
> *(Pause)*
> "Die Ordnung haelt nicht, weil sie stark ist. Sie haelt, weil genug Menschen so tun, als ob."

**Letzter Dialog — Aldine Vor, wenn der Spieler die Wahrheit ausspricht:**

> "Du hast es gesagt. Ich hoere es. Es veraendert nichts. Es wird nichts veraendern. Die Ordnung ist kein Glaube, der bricht, wenn man aufhoert zu glauben. Sie ist eine Struktur, die haelt, weil Strukturen haelten, bis sie es nicht mehr tun."
> *(Pause)*
> "Das ist kein Kommentar zu deiner Entscheidung. Es ist eine Feststellung. Ich werde nicht vergessen, dass du sie getroffen hast."

#### Die Gilden — "Der Preis aller Dinge"

**Schluessfigur:** Cress, Gildenfuehrer (→ GDD-04)
**Thema:** Freiheit durch Besitz — und der Punkt, an dem Freiheit in Gleichgueltigkeit umschlaegt.
**Ton:** Pragmatisch. Direkt. Bildreich. Die Sprache des Handels, die alles als Ware behandelt.
**Kern-Dilemma:** Die Gilden verstehen die Welt als Markt. Alles hat einen Preis, und wer den Preis kennt, hat Macht. Aber die Lebende Krone sprengt diese Logik — ein Gut ohne Preis durchbricht den Handel. Die Gilden reagieren, indem sie Wissen UEBER die Krone handeln. Irgendwann muss jemand die Krone anfassen, und die Gilden wollen nicht derjenige sein — denn der Preis des Tragens ist der einzige Preis, den sie nicht kalkulieren koennen.

| Beat | Titel | Szenenbeschreibung |
|------|-------|--------------------|
| 1 | **Der dreckige Job** | Spieler erhaelt einen Auftrag, den kein Gildenmitglied offiziell ausfuehren darf. Der Auftrag ist legitim nach Gilden-Logik: Kein Risiko fuer die Gilde, klarer Preis fuer den Spieler. Der Spieler ist deniable. Das ist keine Beleidigung — es ist ein Angebot. |
| 2 | **Das unbezahlbare Gut** | Spieler geraet in den Informationshandel rund um die Krone. Er hat eine Information, die Cress will. Cress hat eine Information, die der Spieler braucht. Der Tausch ist fair. Die Frage ist, wessen Information gefaehrlicher ist. |
| 3 | **Der Preis des Wissens** | Spieler muss entscheiden, welche Information er weitergibt und an wen. Cress will das Wissen ueber den letzten Krone-Traeger — um es zu verkaufen, an wen auch immer den hoechsten Preis zahlt. Die Krone wuerde dafuer zahlen. Und der Orden. Und andere. |
| 4 | **Gleichgueltigkeit oder Opfer** | Spieler steht vor der Frage: Laesst er andere den Preis zahlen — das Dorf, die Infizierten, die Fremden, die keiner Fraktion gehoeren? Oder zahlt er selbst? Cress fragt das nicht explizit. Er macht ein Angebot. Und wartet. |

**Letzter Dialog — Cress, unabhaengig von der Entscheidung:**

> "Du hast entschieden. Gut. Entscheidungen, die nicht stattfinden, sind kein Geschaeft, sie sind Aufschub, und Aufschub kostet mehr als die Entscheidung selbst. Das weisst du jetzt."
> *(Kurze Pause)*
> "Ich respektiere, was du getan hast. Ich wuerde es nicht getan haben. Das ist kein Urteil — das ist eine Feststellung von Marktwert. Dein Marktwert ist gestiegen. Vielleicht nicht in der Waehrung, in der du denkst."

#### Der Orden — "Die Last des Wissens"

**Schluessfigur:** Cassius, Ordensfuehrer (→ GDD-04)
**Thema:** Wissen als Waffe und als Kaefig.
**Ton:** Praezise. Kuenstlich ruhig. Nominalisierungen, unpersoenliche Konstruktionen.
**Kern-Dilemma:** Der Orden versteht die kosmologische Wahrheit besser als jede andere Fraktion. Er ahnt den Zusammenhang zwischen Schattenfieber und Biotechnologie. Aber dieses Wissen nutzt er nicht zur Heilung — er nutzt es zur Kontrolle. Er bietet Reinigung an (gegen Loyalitaet). Er sammelt Tiervolk-Ueberlieferungen — und veroeffentlicht sie nicht. Die Frage, die der Orden sich nicht stellt: Ab wann schuetzt man nicht mehr die Wahrheit, sondern nur noch die eigene Macht ueber die Wahrheit?

| Beat | Titel | Szenenbeschreibung |
|------|-------|--------------------|
| 1 | **Der Novize** | Spieler erhaelt Zugang zu den aeusseren Kodizes — das, was der Orden zeigen darf. Cassius empfaengt den Spieler nicht persoenlich. Ein Untergebener. Cassius liest den Bericht danach und benotet den Spieler. Der Spieler weiss nicht, dass er geprueft wird. |
| 2 | **Das Verschlossene** | Spieler entdeckt, dass bestimmtes Wissen gesperrt ist — auch fuer ihn. Er findet Luecken in den Kodizes: herausgerissene Seiten, versiegelte Archive, Kammern, die existieren, aber nicht auf dem Grundriss stehen. Cassius bestaetigt, dass das Wissen existiert. Er sagt nicht, warum es gesperrt ist. Er sagt: "Es gibt Informationen, deren Freigabe mehr schadete als nuetzte." |
| 3 | **Die Versuchung** | Spieler bekommt die Moeglichkeit, die Lebende Krone zu studieren — was der Orden offiziell verbietet, inoffiziell duldet fuer vertrauenswuerdige Agenten. Die Studium-Szene zeigt dem Spieler mehr als er erwartet. Zu viel, vielleicht. Cassius war dabei, sagt nichts, notiert alles. |
| 4 | **Kontrolle oder Offenheit** | Spieler muss entscheiden: Wissen teilen (und die Kontrolle des Ordens brechen) oder Wissen hueten (und die Kontrolle legitimieren). Cassius fragt den Spieler danach — direkt, unverhuellt, das erste Mal ohne seinen theologischen Umweg. Es ist das einzige direkte Gespraech, das sie fuehren. |

**Letzter Dialog — Cassius, wenn der Spieler das Wissen teilt:**

> "Du hast es veroeffentlicht. Ich hatte nicht gedacht, dass du es tun wuerdest."
> *(Lange Pause)*
> "Ich luge jetzt nicht, wenn ich sage: Ich bin nicht sicher, ob das ein Fehler war. Und die Tatsache, dass ich nicht sicher bin, ist selbst ein Datum, das ich nicht erwartet hatte."

**Letzter Dialog — Cassius, wenn der Spieler das Wissen huetet:**

> "Du hast gehuetet. Das ist die Entscheidung, auf die hin ich dich ausgebildet habe."
> *(Pause)*
> "Ich sage dir jetzt etwas, das ich niemandem sage: Ich weiss nicht, ob es die richtige war. Das ist keine Schwaeche. Das ist die Last, die mit dem Wissen kommt, das du nun traegst. Willkommen."

### 3.5 Staedte-Quest

**Titel:** Mittelgrund

**Thema:** Die Kernstadt als Mikrokosmos — keine Krieg, aber die Vorbeben. Die Stadt funktioniert noch — gerade so.

**Format:** Verschachtelte Miniatur-Auftraege, die zusammen ein Bild ergeben. Kein einzelner Questgeber, kein linearer Strang. Stattdessen: Ein Haendler, der Schutzgeld zahlt. Eine Wache, die wegsieht. Ein Priester, der Infizierte registriert — oder versteckt, je nachdem, wem man glaubt. Ein Tiervolk-Haendler (→ GDD-04, Rho), der bestohlen wird und keine Klage einreichen kann, weil das Recht des Gastrechts nicht das Recht der Buerger ist.

Das Tiervolk ist in der Stadt als Nomaden, Haendler und Diebe praesent — nicht als Handwerker, nicht als Buerger. Sie kennen den Status des Fremden aus eigener Erfahrung und spiegeln den Spieler: Du bist wie wir. Du gehoerst nicht hierher. Und vielleicht ist das kein Nachteil.

**Prinzip-Validierung:** Fraktionen als Sprachen. Raeume als Erzaehler.

### 3.6 Charakter-Quest

**Titel:** Der Spiegel
**Figur:** Maret, der Seher (→ GDD-04)

*(V1-Placeholder geschlossen: Die Charakter-Quest-Figur war in V1 als [OFFEN] markiert. Sie ist jetzt Maret — der einzige NPC in RELICS, der das Schattenfieber in seiner finalen Form ueberlebt hat und auf der anderen Seite nicht wahnsinnig, aber kaputt in einer anderen Weise ist. Vollstaendiges Figurenprofil: GDD-04.)*

**Funktion:** Eine tiefe Beziehung zu einer Figur — nicht als Romanze, sondern als Spiegel des Spielers.

**Thema:** Maret sieht den Spieler als Mensch — nicht als Werkzeug, nicht als Bedrohung, nicht als Gelegenheit. Er fragt, warum der Spieler geblieben ist. Er hoert die Antwort. Er hat selbst keine.

**Schattenfieber-Varianz:** Wenn der Spieler infiziert ist, veraendert sich diese Beziehung fundamental. Nicht weil Maret den Spieler ablehnt — sondern weil die Wahrnehmung des Spielers die Beziehung verzerrt. Ab Stufe "Risse" hoert der Spieler Dinge, die Maret nicht gesagt hat — oder die er gesagt hat, aber anders gemeint. Ab "Schwelle" weiss der Spieler nicht mehr, ob die Gespraeche, die er mit Maret fuehrt, tatsaechlich stattfinden. Die Beziehung wird zur Frage: Kann man jemandem vertrauen, wenn man sich selbst nicht mehr trauen kann?

Und Maret, der selbst an der Grenze gelebt hat: Er weiss das. Er warnt nicht. Er haelt die Hand hin.

**Prinzip-Validierung:** Fremder als Zustand. Schattenfieber als Unreliable Narrator.

### 3.7 Kleinere Seitenquests (3x)

#### Seitenquest 1 — "Rausch"

Ein NPC auf Schattenfieber-Stufe "Schwelle". Der Spieler trifft ihn an einem Ort, der nicht ganz real ist — oder der nur fuer den NPC nicht ganz real ist. Der NPC ist nicht feindlich. Er ist freundlich, hilfsbereit, eloquent. Er bietet dem Spieler Informationen an, die sich als wahr herausstellen — aber nur, wenn der Spieler selbst infiziert genug ist, um sie zu pruefen.

Die Frage der Quest: Ist das, was ein Wahnsinniger sieht, weniger wahr als das, was ein Gesunder sieht?

**Prinzip:** Schattenfieber als Unreliable Narrator.

#### Seitenquest 2 — "Gastrecht"

Ein Tiervolk-Haendler wird bestohlen. Alle drei Fraktionen haben eine Version der Geschichte. Der Haendler selbst sagt wenig — er fragt den Spieler, was das Gastrecht wert ist, wenn es nicht geschuetzt wird.

Die Frage der Quest: Wem glaubt man, wenn jede Version in sich logisch ist — und wenn die Wahrheit vielleicht in keiner von ihnen liegt?

**Prinzip:** Fraktionen als Sprachen. Fremder als Zustand.

#### Seitenquest 3 — "Stille"

Ein Ort ohne NPCs. Keine Dialoge. Keine Questgeber. Nur ein verlassener Hof und die Ueberreste einer Geschichte, die der Spieler aus Gegenstaenden und Architektur rekonstruieren muss. Was hier geschah, wird nie explizit ausgesprochen.

Die Quest hat keinen Abschluss im klassischen Sinne — sie ist abgeschlossen, wenn der Spieler versteht. Oder wenn er aufhoert zu suchen.

**Prinzip:** Raeume als Erzaehler.

---

## 4. Dialogsystem

### 4.1 Grundstruktur

**Keine Moral-Achse.** Es gibt keine farbcodierten Antwortoptionen, keine Karma-Punkte, kein "Paragon/Renegade"-System. Der Spieler sieht Antworten, nicht Bewertungen. Was eine Antwort bedeutet, zeigt sich in der Reaktion der Welt — nicht in einer Statistik.

**Qualitaet ueber Quantitaet.** Zwei bis vier Antwortoptionen pro Dialogknoten. Nie mehr. Wenn eine Szene sechs Optionen braucht, ist die Szene zu breit und muss fokussiert werden. Jede Option muss sich anfuehlen wie etwas, das ein Mensch tatsaechlich sagen wuerde — nicht wie ein Gameplay-Hebel.

**Kein stummer Protagonist.** Der Spieler hat eine Stimme. Er spricht in Saetzen, nicht in Stichpunkten. Ob diese Saetze vertont werden, ist eine Scope-Frage (GDD-06), aber im Skript existieren sie vollstaendig. Der Spieler hat keine vordefinierte Persoenlichkeit — aber er hat eine Sprache, die sich nach den Entscheidungen des Spielers formt.

**Kontextuelle Optionen.** Fraktionszugehoerigkeit, Schattenfieber-Stufe und bisherige Entscheidungen schalten Optionen frei oder veraendern ihren Wortlaut. Schattenfieber-Optionen sind nicht markiert — keine UI-Hinweise, kein Icon. Sie stehen neben normalen Optionen, als waeren sie selbstverstaendlich. Der Spieler, der nicht weiss, dass es sie gibt, sieht sie nicht.

### 4.2 Fraktions-Register

#### Die Krone — Pflichtsprache

Formell, archaisch tendierend, haeufiges Passiv. Die Krone spricht in Pflichten, nicht in Wuenschen. "Es wurde angeordnet." "Es obliegt dem Fremden, sich auszuweisen." "Die Ordnung verlangt." Das Subjekt verschwindet oft hinter der Sache.

Die Krone nennt die kosmologische Erosion "die Faulung" und meint damit Strafe. Sie spricht vom "Flechtfest", als waere es gestern gewesen. Sie erwaehnt Sigvalt wie einen Grossvater, der noch im Nebenzimmer sitzt.

Ihr blinder Fleck: Die Krone redet nie ueber den Widerspruch zwischen ihrem Ordnungsanspruch und ihrem Biotech-Einsatz.

**Beispiel — Aldine Vor, erstes Gespraech:**

> "Ihr Anliegen ist registriert. Die Entscheidung ueber seine Berechtigung obliegt dem Verfahren. Das Verfahren dauert drei Tage. Wenn die Ordnung Eure Anwesenheit erfordert, werdet Ihr benachrichtigt. Wenn nicht, habt Ihr drei Tage, Eure Angelegenheiten anderweitig zu regeln."

#### Die Gilden — Wertsprache

Direkt, bildreich, durchsetzt von Sprichwoertern und Handelsmetaphern. Die Gilden reden in Preisen, Renditen und Bilanzen — auch ueber Dinge, die keine Waren sind. "Was kostet dich das?" ist keine Frage nach Geld.

Die Gilden nennen die Welt "den Tharm" — die Eingeweide. Die kosmologische Erosion ist fuer sie "der Schwund" — ein Verlust, der kalkuliert werden kann.

Ihr blinder Fleck: Die Gilden koennen nicht denken, was kein Preis hat.

**Beispiel — Cress, Erstbegegnung:**

> "Du fragst nach dem Haendler. Das ist bemerkenswert direkt. Direktheit ist eine Qualitaet, die ich schaetze — in der richtigen Dosierung. Die Dosierung hier ist: angemessen. Also: Ich kenne den Haendler. Ich kenne, was er weiss. Ich kenne, was das wert ist. Die Frage ist, was du weisst und was das fuer mich wert waere. Das ist keine rhetorische Frage."

#### Der Orden — Wissenssprache

Praezise, kuenstlich ruhig, dominiert von Nominalisierungen und unpersoenlichen Konstruktionen. Der Orden verschluesselt nicht durch Luege, sondern durch Auslassung — er sagt nie etwas Falsches, aber er sagt selten alles.

Der Orden nennt die kosmologische Erosion "die Entflechtung" — ein Prozess, der verstanden werden muss, nicht gefuerchtet.

Sein blinder Fleck: Der Orden verwechselt Verstehen mit Kontrolle.

**Beispiel — Cassius, mittenin einem Gespraech (V2-Ergaenzung):**

> "Die Frage, die du stellen wolltest, lautet: Warum habt ihr das verborgen. Das ist eine korrekte Frage. Die Antwort lautet: Nicht weil es falsch ist, was dort steht. Sondern weil die Konsequenz seiner Bekanntheit schaedlicher waere als die Konsequenz seiner Verborgenheit. Das ist eine Kalkulation, keine Zuneigung zur Unwahrheit. Ich hoffe, du erkennst den Unterschied."

#### Das Tiervolk — Wegsprache

Oral, rhythmisch, durchzogen von Gastrecht-Formeln und Weg-Metaphern. Das Tiervolk spricht in Bildern, die sich bewegen. "Der Weg fragt nicht, wohin du willst." "Wer Gastrecht bricht, kreuzt seinen eigenen Pfad."

Ihr blinder Fleck: Das Tiervolk romanisiert seine eigene Aussenseiterposition. Ob sie wirklich frei sind oder nur gelernt haben, ihre Unfreiheit schoen zu finden — das ist eine Frage, die RELICS dem Spieler ueberlasst.

**Beispiel — Rho, der Haendler, zum Spieler:**

> "Du fragst, ob ich Angst habe. Das ist eine seltene Frage von jemandem wie dir. Die meisten fragen, was ich weiss oder was ich habe. Du fragst, was ich fuehle. Das koennte bedeuten, dass du neugierig bist. Das koennte bedeuten, dass du die Antwort verwenden willst. Das koennte beides bedeuten. Der Weg unterscheidet nicht zwischen Neugier und Kalkul — er fuehrt beide ans Ziel."

### 4.3 Schattenfieber-Dialoge

Das Schattenfieber veraendert Dialoge auf drei Ebenen. Die Veraenderungen sind graduell — kein harter Schalter bei einem bestimmten Wert.

#### Rauschen (Infektionswert ca. 1-40)

Subtil. Einzelne Woerter in NPC-Dialogen sind veraendert — "kalt" statt "kuehl", "Fleisch" statt "Boden", "atmen" statt "wehen". Die Saetze sind grammatisch korrekt und inhaltlich plausibel. Der Unterschied ist da, aber er draengt sich nicht auf.

Ausserdem: Umgebungshinweise, die nur fuer den infizierten Spieler sichtbar sind — ein leises Pulsieren, ein Fluestern, eine Bewegung im Augenwinkel.

**Design-Regel:** Rauschen-Veraenderungen muessen so subtil sein, dass ein Spieler sie beim ersten Durchgang fuer normale Textvariation halten koennte.

#### Risse (Infektionswert ca. 41-80)

Spuerbar. Ganze Gespraechsoptionen erscheinen, die dem sauberen Spieler nicht zur Verfuegung stehen. Nicht markiert. NPCs reagieren irritiert auf Antworten, die der Spieler fuer normal haelt. Fragwuerdige Questgeber treten auf.

**Design-Regel:** Riss-Dialoge muessen MECHANISCH RELEVANT sein — echte Informationen, echte Zugaenge, echte Entscheidungen.

#### Schwelle (Infektionswert ca. 81-100)

Fundamental. Der Spieler kann nicht mehr unterscheiden, welche Gespraeche "echt" sind. Dialoge mit Figuren, die moeglicherweise nicht existieren. Das Parallel-Narrativ der Schwelle ist eine ANDERE Geschichte — in sich so kohaerente und mechanisch relevant wie die des sauberen Spielers.

**Design-Regel:** Schwelle-Dialoge duerfen den Spieler NICHT in Sackgassen fuehren. Auch im Zustand maximaler narrativer Instabilitaet muss jeder Dialogpfad zu einem spielbaren Ergebnis fuehren.

---

## 5. Schattenfieber als narratives System

### 5.1 Kosmologische Grundlage

Das Schattenfieber ist keine Krankheit im medizinischen Sinne. Es ist ein kosmologischer Zustand — das Ergebnis davon, dass die Hauten duenner werden, dass die Grosse Flechtung sich loest, dass die Trennung der Daseinsebenen nicht mehr haelt. Wer vom Schattenfieber betroffen ist, kommt unkontrolliert mit dem Emer-Material in Kontakt — mit dem Stoff, aus dem die Welt gemacht ist, der aber aelter ist als die Welt und sich an Zustaende erinnert, die vor der ersten Trennung lagen.

Emres WBB-01 stellt die Verbindung her: Biotechnologie und Schattenfieber greifen auf dasselbe Material zu. Biotech ist die kontrollierte Manipulation, Schattenfieber die unkontrollierte Reaktion. Gleiche Quelle, verschiedene Auspraegung.

### 5.2 Narratives Stufenmodell (Sync mit GDD-02, Tabelle 2.3)

| Narrativer Zustand | Infektionswert | Mechanischer Name (GDD-02) | Kern-Erfahrung |
|---|---|---|---|
| Gesund | 0–19 | Rein | Klare, zuverlaessige Wahrnehmung. Die vollstaendige Geschichte — aber nicht die ganze Wahrheit |
| Rauschen | 20–50 | Gezeichnet → Infiziert | Zweite Textur der Welt. Der Spieler bemerkt sie — vielleicht. Odin-Opfer in seiner mildesten Form |
| Risse | 51–75 | Verwandelt | Die Trennung der Schichten beginnt zu versagen. Andere Informationen. Andere Moeglichkeiten. Andere Unsicherheiten |
| Schwelle | 76–100 | Entfesselt | Der Spieler steht an der Haut. RELICS ist jetzt ein anderes Spiel. Nicht schlechter. Anders |

*Randfall (bilateral mit Darius zu klaeren): GDD-02 definiert Stufe 2 als Wert 26–50 "Infiziert (Uebergang Rauschen→Risse)". Das passt zur Uebergangszone — Rauschen beginnt ab ~20, Risse beginnen graduell ab ~40. Der Schreibtext fuer die Uebergangszone (Wert 40–50) folgt in V3.*

### 5.3 Das Opfermotiv

In der Mythologie, die Emre geschrieben hat, hat Wissen immer einen Preis. Halvard gab sein Auge. Sigvalt gab seine Hand. Erthag gab sich selbst. Das Schattenfieber ist das spielmechanische Echo dieses mythologischen Prinzips.

Das Opfer ist echt. Es ist nicht reversibel (CD-bestaetigt). Die Infektion vergisst nicht. Wer einmal die zweite Schicht gesehen hat, kann nicht mehr so tun, als gaebe es sie nicht.

Das ist die tiefste Verbindung zwischen Narrativ und Mechanik in RELICS: Das Schattenfieber ist kein Buff-System mit narrativem Anstrich. Es ist eine Erzaehlhaltung, die zum Spielsystem geworden ist.

### 5.4 Replay-Narrativ

RELICS ist ein Spiel, das man zweimal spielen soll. Nicht muss — soll. Der erste Durchgang erzaehlt eine vollstaendige Geschichte. Der zweite — mit anderer Fraktion, anderem Infektionsgrad — kommentiert und stellt in Frage.

RELICS beantwortet die Frage "Welche Version ist wahr?" nicht. Die Weigerung, sie zu beantworten, ist das Erlebnis.

### 5.5 Drei Fraktions-Deutungen des Schattenfiebers

**Die Krone — "Anomalie":** Bedrohung der Ordnung, Zeichen des Verfalls. Ab Stufe 3 ist der Krone-Zugang massiv eingeschraenkt.

**Die Gilden — "Gelegenheit":** Kontrollierbare Ressource. Sie handeln mit Suppressiva, kalkulieren den Marktwert der Faehigkeiten. Ihre Gefahr liegt nicht in der Ablehnung, sondern in der Instrumentalisierung.

**Der Orden — "Zeichen":** Kosmologisches Signal, das studiert werden muss. Der Orden bietet Reinigung an — gegen Loyalitaet und Information. Ab Stufe 3 verweigert er die Reinigung: Ein Spieler auf dieser Stufe ist zu wertvoll als Forschungsobjekt.

---

## 6. Der Wanderer — Spielercharakter-Identitaet

### 6.1 Das Motiv

Emres WBB-01 beschreibt das Halvard-Wanderer-Motiv: Ein maechtiges Wesen, das verkleidet reist — unter falschen Namen, als Bettler, als Niemand. Halvard pruefte die Gastfreundschaft.

RELICS kehrt dieses Motiv um. Der Spieler IST schwach. Er ist kein Gott in Verkleidung. Aber die Welt behandelt ihn, als KOENNTE er mehr sein — und diese Behandlung IST eine Art von Macht.

### 6.2 Gastrecht als Spieler-Mechanik

Das Gastrecht ist eine lebende kulturelle Praxis, die dem Spieler konkrete mechanische Zugaenge verschafft. Feuer, Nahrung, Schutz. Rede und Gegenrede. Bruch hat Konsequenzen.

Jede Fraktion interpretiert das Gastrecht anders (Details: Abschnitt 4.2, Fraktions-Register).

### 6.3 Spieler und Tiervolk — Status-Verwandte

Der Spieler und das Tiervolk teilen denselben Status: Gaeste. Diese Verwandtschaft erzeugt narratives Potenzial auf drei Achsen: Solidaritaet, Konkurrenz, Spiegel.

Das Tiervolk zeigt dem Spieler, was er werden koennte, wenn er nie dazugehoert.

### 6.4 Die Lebende Krone und der Wanderer

Was geschieht, wenn der Wanderer — dieser Niemand, dieser Fremde — in Kontakt mit einem Artefakt kommt, das mit seinem Traeger verschmilzt?

Die Krone hat bisher Koenige veraendert — Menschen mit Legitimation. Der Spieler hat nichts davon. Er ist eine leere Seite — und die Krone, die lebt, die waechst, die reagiert, hat noch nie eine leere Seite beruehrt. Was sie damit macht, ist die Geschichte, die RELICS erzaehlt.

---

## 7. Synchronisation mit anderen GDD-Kapiteln

| Abhaengigkeit | Kapitel | Status | Handlungsbedarf |
|---|---|---|---|
| Schattenfieber-Stufenmapping | GDD-02, Abschnitt 2.3 | Synchronisiert | Uebergangszone-Text (Wert 40-50) folgt V3 |
| Schluesselfiguren | GDD-04 (V1 heute) | Verlinkt | Fraktionsfuehrer-Stimmen integriert |
| Kosmologie und Mythos | WBB-01 (V1) | Integriert | Seher-Visionen: Was sieht Maret genau? (offene Frage) |
| Topos und Geografie | WBB-02 | Abhaengig (teilweise) | Ortsnamen fuer Quest-Lokalisierung fehlen noch |
| Art Direction | GDD-05 (Vera) | Abhaengig | Schattenfieber-Visualisierung, Krone-Design |
| Technik/Produktion | GDD-06 (Tobi/Finn) | Abhaengig | Vertonung ja/nein, Branching-Komplexitaet |

---

## 8. Offene Fragen (aktualisiert V2)

| Nr. | Frage | An wen | Prioritaet | Kontext |
|---|---|---|---|---|
| 1 | Wie viele Enden? | CD | Hoch | Empfehlung: 3 Fraktionsenden + 1 neutrales Ende + SF-Varianten = ca. 6-8 Endvarianten |
| 2 | Gibt es Begleiter/Companions? | CD / Darius | Hoch | Empfehlung: Max. 1-2 temporaere Begleiter, keine permanente Party |
| 3 | Romanze-System ja/nein? | CD | Mittel | Empfehlung: Keine klassische Romanze, aber tiefe emotionale Bindung moeglich (Maret als Kandidat) |
| 4 | Vertonung ja/nein? | Finn / CD | Mittel | Bestimmt Dialoglaenge, Tonalitaet, Scope |
| 5 | SF-Schwellenwerte finalisieren | Darius | Hoch | Uebergangszone 40-50: Schreibtext folgt V3 nach Absprache |
| 6 | Was SIEHT ein Betroffener auf Schwelle-Stufe? | Emre / CD | Hoch | Hohlicht-Fragmente? Stillfeld? Beides? Fundamentale Entscheidung fuer Seher-Visionen |
| 7 | Maret als Charakter-Quest-Figur: Genehmigung? | CD | Hoch | GDD-04 V1 liegt heute vor — Maret ist der Seher, der auf Schwelle-Stufe ueberlebt hat. Bestaetigung erbeten |

---

*Nami Okafor, Schreibstube, Tag 5 Freitag. V2 ist finalisiert. Der Beat-Sheet hat jetzt Szenenebene. Die Fraktionsquests haben echte Dialoge. Maret ist jetzt eine Person, nicht mehr ein Placeholder. Die offenen Fragen sind weniger als gestern — das ist genug fuer heute.*

*Malkav sitzt auf der Druckerausgabe und beurteilt sie.*

\clearpage

# GDD-04 — Schluesselfiguren & NPCs

**Autorin:** Nami Okafor, Narrative Design
**Version:** V1 (Tag 5, Freitag — Erstanlage)
**Status:** Outline mit ausformulierten Stimmen; drei Fraktionsfuehrer, ein Seher-NPC, ein Tiervolk-Vertreter
**Abhaengigkeiten:** GDD-03 Erzaehlkonzept (Nami, V2), WBB-01 Mythos (Emre, V1), GDD-01 Spieluebersicht (Darius), Briefing (Fraktionen, Tiervolk-Direktiven)

---

## Lesehilfe: Figuren-Format

Jede Figur hat drei Pflichtbestandteile:

- **Stimme** — ein unverwechselbarer Sprachrhythmus, der sofort erkennbar ist, wenn man ihn laut liest. Kein Steckbrief, keine Zusammenfassung. Beispieldialoge immer inklusive.
- **Funktion** — was tut diese Figur im narrativen System? Blocker, Ermoegliger, Spiegel, Zerstoerer?
- **Widerspruch** — etwas, das der Spieler erst spaet versteht. Nicht: "der Schurke ist eigentlich gut." Sondern: "die Person, die ich mochte, hat Dinge getan, die ich nicht verzeihen kann — und sie hat einen Grund, den ich verstehe."

Archetypische Figuren — der edle Krieger, der weisen Ratgeber, die geheimnisvolle Seherin — sind kein Ziel. Sie sind das, was man produziert, wenn man aufhoert zu denken.

---

## 1. Aldine Vor — Fraktionsfuehrerin der Krone

### Basisdaten

- **Fraktion:** Die Krone
- **Funktion im Spiel:** Quest-Geberin (Kronenquest "Pflicht und Verfall"), Point-of-No-Return-Figur (Beat 6), narrativer Spiegel fuer den Spieler in Akt II
- **Alter:** 54
- **Aeusseres:** Militaerische Haltung — nicht durch Disziplin, sondern durch Erschoepfung, die sich zu Haltung verfestigt hat. Kleidung funktional, nicht opulent. Kein Schmuck ausser einem kleinen Siegel an der linken Hand — das Siegel ist nicht das ihrer Familie, sondern das ihres Vorgaengers, den sie abgeloest hat.

### Hintergrund

Aldine Vor ist nicht in die Krone-Fuehrerschaft hineingeboren. Sie hat sie erkaempft — nicht durch Verwandtschaft, sondern durch zwanzig Jahre Verwaltung in den Grenzregionen, wo die Krone duenn war und sie die Ordnung allein haelt. Ihr Vater war ein Krone-Hauptmann, dem die Kronentreue die Haende abgehackt hatte — buchstaeblich, durch einen Befehl, den er haette verweigern sollen und nicht verweigerte. Er lebte danach noch siebzehn Jahre, ein Denkmal an das, was Pflicht kostet.

Aldine Vor glaubt nicht an die Krone als Institution. Sie glaubt an die Krone als Notwendigkeit — das Einzige, das zwischen dem Mittelgrund und dem Chaos steht, das sie in den Grenzregionen erlebt hat. Wenn sie die Krone schuetzt, schuetzt sie nicht Tradition. Sie schuetzt die Abwesenheit von dem, was sie gesehen hat, wenn Tradition zusammenbricht.

### Stimme

Die Krone spricht in Pflichten, nicht in Wuenschen — und Aldine Vor ist die vollkommenste Instanz dieses Registers.

Ihr Stil: Parataxe. Kurze Saetze. Passiv wo moeglich. Das Subjekt verschwindet hinter der Sache. Wenn sie bittet, klingt es wie ein Befehl, dem ein Schritt fehlt. Wenn sie dankt, klingt es wie eine Quittung.

**Erstbegegnung (Spieler hat sich durch eine Krone-Aufgabe bewiesen):**

> "Euer Dienst ist registriert. Er entspricht den Anforderungen, die ich gestellt habe. Das ist eine Feststellung, keine Lob."
> *(Pause)*
> "Es gibt weitere Anforderungen. Ob Ihr ihnen entsprechen wuerdet, ist unklar. Die Vergangenheit buergt nicht fuer die Zukunft — das ist der Fehler derer, die in Dynastien denken. Ich denke in Funktion."

**Im dritten Akt, wenn der Spieler die Wahrheit ueber den Biotech-Einsatz aufgedeckt hat:**

> "Ihr habt es gesagt. Das veraendert nichts. Ich sage Euch, warum: Weil die Ordnung nicht bricht, wenn man ihr die Wahrheit zeigt. Sie bricht, wenn die Menschen aufhoeren, so zu tun, als wuerde sie halten."
> *(Lange Pause)*
> "Ich tue das jeden Tag. Ihr koennt urteilen, wenn Ihr gefunden habt, was Ihr tun wuerdet, wenn die Alternative Chaos ist. Nicht theoretisch. Tatsaechlich."

**Allein, nachts, wenn der Spieler sie beobachten kann (keine Reaktion auf den Spieler):**

> *(Zu sich selbst, leise)* "Sigvalt gab seine Hand. Die Krone fragte nicht, ob er wollte. Die Krone fragt nie. Das ist ihr einziges Versprechen."

### Funktion

**Blocker und Ermoegliger gleichzeitig.** Aldine Vor schliesst Tueren und oeffnet sie — aber immer mit Konsequenz. Sie gibt dem Spieler Zugang zu Krone-Ressourcen, zu Archiven, zu Informationen, die sonst unzugaenglich waeren. Aber jeder Zugang bindet. Der Spieler merkt irgendwann, dass er nicht fuer die Krone arbeitet — sondern dass die Krone ihn arbeiten laesst, weil er etwas hat, das sie braucht, und weil sie ihn beobachtet, ob er weiss was er hat.

**Narrativer Spiegel.** Aldine Vor ist, was der Spieler werden koennte, wenn er sich fuer die Ordnung entscheidet und lange genug dabei bleibt: jemand, der an das System glaubt, weil die Alternative schlimmer ist, und der gelernt hat, dass "schlimmer" kein Argument ist, sondern ein Zustand.

### Widerspruch

Der Spieler mag Aldine Vor moeglicherweise. Oder er respektiert sie zumindest. Sie ist nicht zynisch — sie glaubt wirklich, was sie tut. Sie glaubt an die Ordnung, weil sie gesehen hat, was ohne sie passiert.

Und dann entdeckt der Spieler: Aldine Vor weiss seit Jahren, dass der Krone-Biotech-Einsatz die Faulung beschleunigt. Nicht aus Bosheit. Aus einer Kalkulation: Wenn sie es offentlich macht, bricht die Ordnung. Wenn sie schweigt, haelt die Ordnung — vielleicht lange genug, damit jemand anderes eine Loesung findet.

Sie hat sich entschieden zu schweigen. Sie lebt jeden Tag mit dieser Entscheidung. Und sie wuerde sie wieder treffen.

---

## 2. Cress — Fraktionsfuehrer der Gilden

### Basisdaten

- **Fraktion:** Die Gilden
- **Funktion im Spiel:** Quest-Geber (Gildenquest "Der Preis aller Dinge"), Informationsbroker, narrativer Ermoegliger mit verdeckter Agenda
- **Alter:** 41
- **Aeusseres:** Gut gekleidet, nicht prunkvoll. Der Unterschied ist bewusst — Prunk signalisiert, dass man versucht, Macht zu zeigen. Cress zeigt keine. Er traegt sie. Sein Aeusseres sagt: Ich bin erfolgreicher als du ohne anstrengend darauf hinzuweisen. Haende gepflegt — er arbeitet mit Stift und Siegel, nicht mit Werkzeug, und das sieht man.

### Hintergrund

Cress kommt aus einer Handwerker-Familie im Nordquartier einer Gildenstadt — sein Vater war Weber, seine Mutter Faerberin, beide handelten mit dem, was sie herstellten, bis die Gilde den Preis festlegte und der Festpreis bedeutete, dass der Vater nicht mehr kaufen konnte, was er brauchte, um das herzustellen, das er verkaufte.

Cress lernte frueh: Das System ist kein Feind und kein Freund. Es ist eine Logik. Wer die Logik kennt, gewinnt. Wer gegen sie kaempft, verliert nicht das Spiel — er spielt das falsche Spiel.

Er hat Leute aus der Armut gezogen. Er hat Staedte gebaut. Er hat Handelsrouten eroefffnet, die Regionen verbanden, die vorher isoliert waren. Er hat auch Leute sterben lassen, wenn es billiger war. Er sieht keinen Widerspruch.

### Stimme

Die Gilden sprechen in Preisen und Angeboten — und Cress ist der technisch vollkommenste Sprecher dieses Registers. Er ist nie aggressiv. Er ist nie drueckend. Er ist verbindlich und unvermeidlich.

Sein Stil: Viele Konjunktive. "Koennte." "Vielleicht." "Wenn die Umstaende guenstig sind." Der Preis kommt immer am Ende des Satzes, wenn man schon zugehoert hat. Er stellt keine Forderungen — er beschreibt Optionen. Die Optionen sind alle so geformt, dass eine davon immer unattraktiv ist.

**Erstbegegnung:**

> "Du hast Fragen. Das ist gut — Fragen bedeuten Interesse, und Interesse bedeutet, dass ein Gespraech stattfinden koennte, das fuer beide Seiten produktiv waere. Mein Name ist Cress. Du weisst das vermutlich schon — wenn du hier bist, hast du dich vorbereitet, und wenn du dich vorbereitet hast, weisst du, an wen du dich wendest."
> *(Kurze Pause)*
> "Was ich noch nicht weiss, ist, was du hast. Das ist der interessante Teil."

**Mitte des Spiels, wenn der Spieler herausfindet, fuer wen Cress das Wissen ueber die Lebende Krone weiterverkaufen wuerde:**

> "Du bist enttaeuscht. Das sehe ich. Das ist auch verstaendlich — du hattest ein Bild von mir, und das Bild war, glaube ich, angenehmer als die Realitaet."
> *(Pause)*
> "Ich sage dir, was die Realitaet ist: Ich verkaufe das Wissen. Nicht weil ich gleichgueltig bin. Sondern weil Wissen, das nicht zirkuliert, stirbt. Das ist keine Rechtfertigung. Das ist eine Beschreibung."

**Wenn der Spieler ihn direkt nach dem Dorf fragt, das die Bruecke opfert:**

> "Das Dorf. Ja. Ich weiss, was du sagen willst. Ich sage dir etwas: Das Dorf weiss es auch. Sie wissen, dass die Bruecke gebaut wird. Sie wissen, was es bedeutet. Sie haben Optionen gehabt."
> *(Pausiert)*
> "Die Optionen waren schlecht. Das gebe ich zu. Aber schlecht ist keine Ausrede. Schlecht bedeutet: jemand hat eine schlechtere Kalkulation gemacht als ich. Kein moralisches Urteil. Eine Feststellung."

### Funktion

**Instrumentalisierer.** Cress gibt dem Spieler, was er braucht — aber immer mit einem Restbetrag, den der Spieler nicht sieht, bis er ihn zahlt. Er ist kein Feind. Er ist eine Konsequenz. Wer mit ihm arbeitet, arbeitet fuer seine Ziele. Das ist transparent. Er sagt es. Aber Transparenz macht es nicht weniger wahr.

**Informationsbroker.** Cress weiss, was die anderen Fraktionen wissen — weil er die Information kauft. Er bietet dem Spieler Wissen an, das er nicht anderswo bekommt. Der Preis des Wissens ist immer: Cress bekommt gleichwertiges Wissen zurueck.

### Widerspruch

Cress ist nicht herzlos. Das ist der Widerspruch.

Er kommt aus der Unterschicht. Er weiss, was Armut bedeutet, was es bedeutet, wenn das System die Preise setzt und man kein Mitspracherecht hat. Er hasst das. Er hat sein Leben damit verbracht, aus dieser Position herauszukommen. Und er hat dabei ein System gebaut, das andere in dieselbe Position setzt — weil er gelernt hat, dass das System die einzige Sprache ist, die bleibt.

Der Spieler, der das herausfindet, steht vor einer Frage: Ist Cress ein Heuchler? Oder ist er jemand, der so tief ins System eingearbeitet wurde, dass er vergessen hat, was er dagegen hatte?

Cress hat die Antwort. Er sagt sie nicht, weil er sie fuer eine Schwaeche haelt.

---

## 3. Cassius — Fraktionsfuehrer des Ordens

### Basisdaten

- **Fraktion:** Der Orden
- **Funktion im Spiel:** Quest-Geber (Ordensquest "Die Last des Wissens"), Wissensbroker mit Kontrollabsicht, narrativer Antagonist ohne Bosheit
- **Alter:** 67
- **Aeusseres:** Ordenstrachtung, aber abgenutzt — die Zeichen des Rangs sind da, aber nicht gepflegt. Er hat aufgehoert, Zeichen zu pflegen, weil die Sache selbst ihm wichtiger ist als ihr Symbol. Sehr ruhige Bewegungen. Er bewegt sich, als haette er gelernt, dass schnelle Bewegungen Verwirrung stiften, und Verwirrung ist Information-Verlust.

### Hintergrund

Cassius war Novize, dann Schueler, dann Archivar, dann Rat, dann — nach einer Kette von Ereignissen, die er als "logische Konsequenzen" bezeichnet — Ordensfuehrer. Niemand wollte das Amt. Cassius wollte es auch nicht. Er uebernahm es, weil die Alternative war, jemanden in das Amt zu lassen, der nicht verstand, was das Amt bedeutete.

Er versteht die Welt so gut wie irgendwer in der Spielwelt. Er weiss, dass die Hauten duenner werden. Er weiss, dass das Schattenfieber und die Biotechnologie dasselbe Material verwenden. Er weiss, dass die Lebende Krone nicht eine Loesung ist, sondern eine Komplikation. Er weiss, dass der Orden — wenn er handeln wuerde, offen handeln wuerde — vielleicht etwas verbessern koennte.

Und er haelt das Wissen trotzdem zurueck. Weil Wissen, das unkontrolliert zirkuliert, Panik erzeugt. Und Panik ist schlimmer als Unwissen. Cassius hat Panik gesehen — in einer Grenzregion, vor dreissig Jahren, als jemand die Wahrheit ueber das Schattenfieber veroeffentlichte. Sieben Stadte brannten. Er war dabei.

### Stimme

Der Orden spricht in Fragen und Schweigen — und Cassius ist der Meister dieses Registers. Er stellt Fragen, auf die er die Antworten bereits kennt. Er schlaegt die Antwort in Fragen ein, weil er weiss, dass eine Aussage abgelehnt werden kann, eine Frage aber antwortet werden muss — und die Antwort gehoert dann dem Fragenden.

Sein Stil: Praezise. Nominalisierungen. Unpersoenliche Konstruktionen. Lange Pausen, in denen er dem Spieler Zeit gibt, sich selbst zu verraten. Wenn er direkt ist, ist es ein Zeichen, dass er entschieden hat, dem Spieler zu vertrauen. Das passiert selten.

**Erstbegegnung (Spieler wurde vom Orden untersucht, ohne es zu wissen):**

> "Ihr habt gewartet. Das ist bemerkenswert — die meisten warten nicht. Sie stellen sofort Fragen, als waere die Frage wichtiger als die Antwort."
> *(Pausiert)*
> "Das ist sie nicht. Die Frage ist die Form. Die Antwort ist der Inhalt. Ich bin an beidem interessiert. Ihr seid, vermute ich, primaer an letzterem. Das macht Euch erklaerbar."

**Wenn der Spieler fragt, warum Seiten aus den Archiven fehlen:**

> "Ihr fragt, warum. Das ist die naheliegendste Frage, die man stellen kann — und deshalb ist sie meistens nicht die richtige."
> *(Lange Pause)*
> "Die richtigere Frage waere: Was geschaehe, wenn die Seiten nicht fehlten? Ich beantworte Eure Frage trotzdem: Die Seiten fehlen, weil ihre Verfuegbarkeit zu einem Zeitpunkt, an dem bestimmte Informationen noch nicht zugeordnet werden konnten, schlechter gewesen waere als ihre Abwesenheit. Das ist keine Rechtfertigung. Es ist eine Kalkulation."

**Einziges direktes Gespraech, Ordensquest Beat 4 — wenn der Spieler entschieden hat:**

> "Du hast entschieden. Ich bin froh, dass es vorbei ist."
> *(Pause — laenger als ueblich)*
> "Ich war nicht sicher, was du tun wuerdest. Das kommt selten vor. Ich bin alt genug, dass es selten vorkommt. Es ist kein angenehmes Gefuehl. Es ist auch kein unangenehmes. Es ist... das Gefuehl, dass etwas noch offen ist. Das halte ich fest."

### Funktion

**Der Wissens-Hueter als narrative Zentralgestalt.** Cassius ist die Figur, die am meisten weiss — und die deshalb am meisten Schaden anrichten kann, ohne es zu wollen. Er schuetzt nicht die Wahrheit. Er schuetzt die Kontrolle ueber die Wahrheit. Das ist ein Unterschied, den er zumindest intellektuell anerkennt.

**Spiegel fuer den Orden-Spieler.** Wer den Orden-Pfad spielt, sieht in Cassius eine moegliche Zukunft: jemand, der so viel weiss, dass er nicht mehr anders kann, als zu kontrollieren. Das ist keine Bosheit. Das ist eine Konsequenz.

### Widerspruch

Cassius glaubt wirklich, was er tut. Das ist das Erschreckende.

Er hat nicht beschlossen, ein Kontrolleur zu sein. Er hat beschlossen, Schaden zu verhindern. Und Schaden-Verhinderung hat — ueber dreissig Jahre, ueber eine Reihe von plausiblen Entscheidungen — einen Kontrolleur aus ihm gemacht.

Der Spieler, der seinen Questpfad abschliesst, versteht das. Und versteht, dass Cassius es auch weiss. Und weiss, dass Cassius es trotzdem nicht aendern wird — weil die Alternative, nach seiner Kalkulation, immer noch schlimmer ist.

Das ist kein Villain. Das ist ein Mensch, der sich in seiner eigenen Logik eingesperrt hat und zu klug ist, den Schluessel nicht zu sehen, und zu muede, ihn zu benutzen.

---

## 4. Maret — Der Seher

### Basisdaten

- **Fraktion:** Keine. Frueherer Orden-Archivar, jetzt nicht mehr.
- **Funktion im Spiel:** Charakter-Quest "Der Spiegel" (→ GDD-03, Abschnitt 3.6), Einstiegspunkt fuer Schattenfieber-Narrativ, optionale Figur (nur fuer Spieler, die ihn suchen — oder infizierte Spieler ab Stufe 1)
- **Alter:** Unbekannt. Er erinnert sich an das Flechtfest als Kind. Das macht ihn alt. Er sieht juenger aus. Das ist das Schattenfieber.
- **Aeusseres:** Ordentlich, fast pedantisch ordentlich — Gegenbewegung zu seinem Inneren. Die Kleider sind geflickt, aber sauber geflickt. Er lebt in einem kleinen Zimmer am Rand der Stadt, das er vollgeschrieben hat: an den Waenden, auf losen Blaettern, auf dem Boden, ueber den Fenstern. Die Schrift ist lesbar. Sie ist auch nicht immer chronologisch.

### Hintergrund

Maret war Archivar des Ordens — gut, vielleicht zu gut. Er war der erste, der die Verbindung zwischen Schattenfieber und Biotechnologie systematisch dokumentierte. Er legte das Ergebnis Cassius vor. Cassius las es, dankte ihm, und entschied, dass die Dokumentation nicht zirkulieren duerfe.

Maret war damit nicht einverstanden. Er war damit so nicht einverstanden, dass er versuchte, die Dokumentation zu duplizieren und zu veroeffentlichen. Cassius fand es heraus. Maret wurde nicht bestraft — er wurde entlassen. Ohne Feind, ohne Skandal. Einfach: entlassen.

Maret zog sich zurueck. Er hatte waehrend seiner Archivarbeit Schattenfieber-Exposition gehabt — keine schwerere als jeder Archivar, der nahe an den betroffenen Texten gearbeitet hat, aber genug. Er infizierte sich weiter, absichtlich oder nicht (er selbst weiss es nicht mehr). Er ist jetzt bei Stufe "Schwelle" — der einzige bekannte Ueberlebende auf dieser Stufe, der noch funktioniert.

"Funktioniert" ist das Wort, das er selbst benutzt. Nicht "lebt". Nicht "ueberleben". Funktioniert.

### Stimme

Maret ist keine Orakel-Figur. Er spricht nicht in Raetseln, weil Raetsel profetisch klingen sollen. Er spricht in Fragmenten, weil seine Wahrnehmung in Fragmenten ist — er verliert den Faden nicht, weil er ihn nie vollstaendig hat. Er weiss, welche Schicht er gerade sieht, und welche er sehen sollte, und ob sie dieselbe sind.

Sein Stil: Ruhig, fast akademisch — das ist sein Archivar-Hintergrund, der blieb. Dann: abrupt. Dann: zurueck. Die Luecken in seinen Saetzen sind nicht dramatisch — sie sind der Moment, in dem er eine andere Schicht ueberprueft.

**Erste Begegnung (Spieler findet ihn am Ort des "ersten Zeichens", Beat 3 Hauptquest):**

> "Du bist neu hier. Ich meine: neu in dem, was du siehst."
> *(Pause — er schaut an einer Stelle hinter dem Spieler, wo nichts ist)*
> "Entschuldige. Manchmal ueberlagern sich die Schichten, und ich muss ueberpruefen, welche... aktuell ist. Du bist in der richtigen. Das weiss ich, weil du mich ansiehst."

**Wenn der Spieler ihn nach dem Schattenfieber fragt:**

> "Was du wissen willst, ist: Wie ist es. Das ist die Frage, die alle stellen. Ich sage dir, wie es ist."
> *(Kurze Pause)*
> "Es ist wie... stell dir vor, du schreibst auf Papier, und das Papier ist durchsichtig, und darunter liegt ein anderes Blatt, und auf dem anderen Blatt steht auch etwas. Manchmal lesbar. Manchmal nicht. Manchmal ist das, was darunter steht, wichtiger als das, was ich sehe. Manchmal stimmt es nicht."
> *(Pause)*
> "Ich habe aufgehoert, sicher zu sein, welches welches ist. Das klingt schlimmer, als es ist. Oder genau so schlimm. Ich kann das nicht von hier aus beurteilen."

**Zum infizierten Spieler — wenn er merkt, dass der Spieler auch sieht:**

> "Du siehst es. Ich sehe, dass du es siehst. Das ist selten. Nicht — nicht angenehm oder unangenehm. Nur: selten."
> *(Lange Pause. Er sieht den Spieler direkt an — das macht er selten)*
> "Pass auf: Was du siehst, ist nicht immer falsch. Aber was du siehst, ist auch nicht immer das, was da ist. Das klingt wie eine Warnung. Es ist keine Warnung. Es ist eine Beschreibung."
> *(Pause)*
> "Ich haette mich gewuenscht, dass mir das jemand frueh gesagt haette. Ich sage es dir jetzt."

**Spaet im Spiel, wenn Spieler ihn nach Cassius fragt:**

> "Cassius."
> *(Pause)*
> "Er hat nicht Unrecht gehabt. Das ist das Schwierige. Er hatte Gruende. Gute Gruende. Ich hatte auch Gruende. Auch gute."
> *(Pause — laenger diesmal)*
> "Ich weiss nicht, wer richtig hatte. Ich weiss, was passiert ist, und ich weiss, was ich geglaubt habe, und ich weiss, dass beides gleichzeitig wahr sein kann. Das ist auch etwas, was man im Fieber lernt."

### Funktion

**Emotionaler Kern fuer infizierte Spieler.** Maret ist die einzige Figur, die dem Spieler sagt, was es bedeutet, auf Schattenfieber-Schwelle zu leben — nicht als Warnung, nicht als Prophezeiung, sondern als Erfahrungsbericht. Er ist der Beweis, dass das Schattenfieber nichts gibt, ohne alles zu nehmen. Und er ist die Person, die trotzdem da ist.

**Bruecke zwischen Orden-Wissen und Spieler-Erfahrung.** Maret weiss, was der Orden weiss — er hat es archiviert. Aber er weiss es nicht als Machtinstrument. Er weiss es als jemandem, dem das Wissen etwas gekostet hat.

**Optionaler Questgeber.** Die Charakter-Quest "Der Spiegel" ist nur zugaenglich, wenn der Spieler Maret sucht oder infiziert ist. Kein Quest-Marker. Der Spieler findet Maret durch Neugier, durch das "erste Zeichen" in Akt I, oder — wenn infiziert — durch die Schattensinne, die zeigen, wo er ist.

### Widerspruch

Maret ist der sympathischste Charakter in RELICS — das ist seine Gefahr.

Der Spieler mochte ihn. Maret ist ehrlich, ruhig, nicht bedrohlich, und er sagt dem Spieler Dinge, die andere nicht sagen. Maret hat auch — absichtlich oder nicht (er weiss es selbst nicht mehr) — andere Infizierte gefunden und ihnen geholfen, ihre Infektionswerte zu steigern, in dem Glauben, dass hoehere Werte tiefere Einsicht bedeuten.

Manche dieser Menschen haben das ueberlebt. Manche nicht.

Maret weiss das. Er hat keine Entschuldigung. Er hat eine Erklaerung: Er dachte, er huelfe. Er ist nicht sicher, ob das eine Entschuldigung ist.

Das ist die Frage, die der Spieler spaet im Spiel stellt — und die Maret nicht abweist. Er sagt: "Ich weiss es nicht." Das ist die ehrlichste Antwort, die irgendeine Figur in RELICS gibt.

---

## 5. Rho — Tiervolk-Haendler

### Basisdaten

- **Fraktion:** Keine — Tiervolk, nomadisch, Haendler
- **Funktion im Spiel:** Staedtequest "Mittelgrund" (zentrale Figur), Seitenquest 2 "Gastrecht" (Quest-Geber), Informationsquelle fuer Spieler, die das Tiervolk-Netz zugang erarbeitet haben
- **Alter:** 38
- **Tierart-Referenz:** Raptor-artig — schlanke Proportionen, Federnzeichnung am Kopf (keine Federn, aber Haare in Federmuster), grosse Augen mit seitlichem Sehfeld. Bewegungen schnell, sehr praezise. Kein tribal-Element in Kleidung oder Verhalten — Stadtwear, gut ausgesucht, fraktionsneutral.
- **Aeusseres:** Zieht keine Aufmerksamkeit auf sich, ohne unsichtbar zu sein. Das ist eine Faehigkeit, kein Zufall. Er traegt nichts, das ihn eindeutig einer Fraktion zuordnet. Er traegt auch nichts, das ihn eindeutig als Tiervolk markiert — ausser dem, was er nicht verstecken kann. Er hat nicht gelernt, sich zu verstecken. Er hat gelernt, sich nicht anzubieten.

### Hintergrund

Rho ist in einer Tiervolk-Handelskarawane aufgewachsen — vier Generationen desselben Handelsweges durch denselben Mittelgrund, denselben drei Staedte, dieselben Gastrecht-Abkommen, die jede Generation neu aushandeln muss, weil kein Abkommen ueber den Tod der unterzeichnenden Generation gilt.

Er kennt den Mittelgrund besser als die meisten Einheimischen. Er kennt die Staedte als System — wer wirklich entscheidet, wer das Schutzgeld nimmt, welche Krone-Patrouillen kaeuflich sind, welche Gilden-Lager illegal handeln, welche Orden-Stationen die Tiervolk-Berichte verschwinden lassen. Er kennt das, weil sein Ueberleben davon abhing, es zu kennen.

Er ist kein Dieb. Aber er kennt Diebe, arbeitet manchmal mit ihnen, und verurteilt sie nicht. Das Recht gilt nicht fuer das Tiervolk — also gilt das Recht des Tiervolk nicht nach dem Recht. Es gilt nach einer anderen Logik. Rho hat diese Logik.

### Stimme

Das Tiervolk spricht in der Wegsprache — oral, rhythmisch, Weg-Metaphern, Gastrecht-Formeln. Rho spricht das auch — aber er ist lange genug in der Stadt, dass er die Stadtsyntax drueber gelegt hat. Das Ergebnis: Die Wegsprache klingt unter der Stadt-Sprache. Wenn er ruhig ist, hoert man die Stad. Wenn er angespannt ist, hoert man den Weg.

Sein Stil: Abgewaegt, beobachtend. Er stellt Fragen, die er nicht als Fragen formuliert. Er gibt Informationen, die er nicht als Informationen bezeichnet. Er hat gelernt, dass Direktheit riskant ist, und dass das, was er weiss, teurer ist, wenn er es nicht sofort anbietet.

**Erstbegegnung (Spieler naehert sich dem Marktstand):**

> "Du hast mich schon zweimal angeschaut. Das dritte Mal bin ich sicher."
> *(Pause — er arrangiert etwas auf dem Stand, ohne aufzusehen)*
> "Ich verkaufe Getreidewaren aus dem Nordquartier und Gewuerze aus dem Weg-Netz. Beides ist gut und beides hat einen fairen Preis. Wenn du das nicht suchst, ist es trotzdem gut zu wissen, was ich offiziell tue."

**Wenn der Spieler nach dem Tiervolk-Netz fragt:**

> "Der Weg fragt nicht, wer du bist. Das stimmt. Aber die, die den Weg kennen, fragen sehr wohl, warum jemand fragt."
> *(Kurze Pause)*
> "Ich frage: Warum fragst du? Nicht als Ablehnung. Als Einstieg. Der Weg braucht keinen Grund. Ich schon."

**Wenn der Spieler die Seitenquest "Gastrecht" beginnt (Rhos Ware wurde gestohlen):**

> "Es gibt drei Versionen davon, was passiert ist. Die Krone-Version, die Gilden-Version, und die des Priesters. Du wirst alle drei hoeren, wenn du herumfragst."
> *(Pause)*
> "Keine davon stimmt. Ich sage dir das nicht, damit du die richtige Version suchst. Ich sage es, damit du weisst, warum ich nicht zur Wache gegangen bin."

**Spaet im Spiel, wenn Spieler Vertrauen erworben hat:**

> "Ich zeige dir etwas, das ich wenigen zeige."
> *(Er zeigt dem Spieler eine handgezeichnete Karte des Tiervolk-Wegnetzes — nicht die Stadt, sondern die Verbindungen zwischen den Gaesterechtspunkten, den Schlafsplaetzen, den Schutzzonen)*
> "Das ist die Stadt, die die Krone nicht sieht. Das sind die Knochen unter den Steinen. Wir haben sie so gelegt, als eure Vorvaetern die Steine draufgebaut haben. Gastrecht braucht keine Mauern. Es braucht nur Erinnerung."

### Funktion

**Informationsquelle ausserhalb der Fraktionen.** Rho weiss, was das Tiervolk-Netz weiss — und das ist oft mehr als die Fraktionen wissen, weil das Tiervolk die Stadt von unten kennt. Er ist kein einfacher Informationsbroker: Er gibt Information gegen Vertrauen, nicht gegen Geld. Vertrauen erarbeitet der Spieler durch Handlungen, nicht durch Dialoge.

**Spiegel-Figur fuer den Spieler.** Rho und der Spieler sind beide Fremde in der Stadt. Rho zeigt, was es bedeutet, jahrelang Fremder zu sein — nicht als Tragoedie, sondern als Praxis. Er hat Strukturen entwickelt, um zu ueberleben. Manche sind schoener als andere.

**Eingang ins Tiervolk-Subnetz.** Fuer Spieler, die den Tiervolk-Pfad erkunden, ist Rho der Zugangspunkt zu einem Sub-Netz aus NPCs, Informationen und optionalen Szenen, die keine andere Fraktion bietet.

### Widerspruch

Rho praesentiert sich als pragmatisch, neutral, ausserhalb der Fraktions-Logik. Das stimmt teilweise.

Es stimmt nicht, was er mit bestimmten Informationen gemacht hat. Er hat Krone-Schwachstellen an Gilden-Kontakte verkauft. Nicht aus Boesartigkeit — aus Notwendigkeit, aus einer Situation, in der das Tiervolk-Netz bedroht war und er Schutz brauchte. Er hat einen Krone-Offizier kompromittiert, um eine Karawane zu schuetzen. Der Offizier verlor seine Stelle. Seine Familie wurde mitbeststraft.

Rho weiss das. Er hat es nicht vergessen. Er hat entschieden, dass es noetig war — und er wuerde es wieder tun.

Der Spieler, der das herausfindet, steht vor einer Figur, die genau das tat, was er moeglicherweise selbst getan hat — in einer anderen Quest, fuer andere Gruende. Das ist kein Zufall. Das ist Spiegel-Funktion.

---

## 6. Offene Figuren (V2-Aufgaben)

Diese Figuren sind als Bedarf identifiziert, aber noch nicht ausgearbeitet. V2 schliesst sie.

| Figur | Funktion | Quest-Verbindung | Prioritaet |
|---|---|---|---|
| Grenzhauptmann Aldric | Tutorial-Figur (Beat 1, Intro-Quest "Der Gast") | Intro-Tutorial | Hoch |
| Haendlerin Sefa | Gildenkontakt, Erstbegegnung | Beat 2, "Die drei Stimmen" | Mittel |
| Ordenspriester (unbenannt) | Ordenskontakt, Erstbegegnung; Krone-Infizierten-Reaktion | Beat 2, "Die drei Stimmen" | Mittel |
| Letzter Krone-Traeger | Spur-NPC (moeglicherweise nicht mehr lebendig) | Kronenquest Beat 3 | Hoch |
| Novize mit Ordensarchiv-Zugang | Ordensinnenansicht, Zugang fuer Beat 1 Ordensquest | Ordensquest Beat 1 | Niedrig |

---

## 7. Synchronisation

| Abhaengigkeit | Kapitel | Status |
|---|---|---|
| Fraktions-Sprachen und Dialekte | GDD-03, Abschnitt 4.2 | Verlinkt — Dialoge aus GDD-04 ersetzen Platzhalter in GDD-03 |
| Schattenfieber-Seher-Funktion | GDD-03, Abschnitt 3.6 | Maret ist gesetzt — Cassius-Absprache fuer Seher-Visionen offen |
| Tiervolk-Design | Briefing + Vera GDD-05 | Rhos Aeusseres muss mit Vera abgestimmt werden (kein tribal, leicht alien) |
| Kosmologische Figuren-Referenzen | WBB-01 (Emre) | Halvard, Sigvalt, Erthag als Mythos-Figuren integriert — keine eigene Spieler-Begegnung |

---

*Nami Okafor, Schreibstube, Tag 5 Freitag. Alle fuenf Figuren haben Stimmen. Ich habe Aldine Vors letzten Dialog laut vorgelesen — zweimal. Er klingt richtig. Das ist selten genug.*

*Nines hat die Handnotizen zum Seher vom Tisch geworfen. Der Seher haette das verstanden.*

\clearpage

# GDD-05: Visuelle Designsprache & Art Direction

> **Status:** V2 — Finalisiert (Produktionstag, Tag 5)
> **Autorin:** Vera Kowalski, Concept Art & Environment Design
> **Letzte Aktualisierung:** Tag 5, Szene 2
> **Aenderungslog:**
> - V1 (Tag 3): Volltext, Fraktionsvisuals, Biotech-Grammatik, Farbsystem, Mode, Tiervolk, Schattenfieber, Environments
> - V2 (Tag 5): Stufe-0-Baseline ergänzt (Kap. 7.2), Stufengrenzen-Referenztabelle einheitlich, Gameplay-Orte neu (Kap. 8.5), Dominanzprinzip in Kap. 5.4, ACES-Validierungshinweis in Kap. 4.4
> **Abhaengigkeiten:** WBB-01 Mythos (Emre), WBB-02 Topos (Emre, V1 ausstehend), GDD-02 Kernmechaniken (Darius), GDD-04 Schluesselfiguren (Nami)

---

## 1. Art Direction — Ueberblick

### 1.1 Visuelle Vision

RELICS sieht aus wie eine Welt, die aus einem Koerper gewachsen ist — weil sie es ist.

Die Art Direction von RELICS gruendet auf einer einzigen kosmologischen Tatsache: Die Welt wurde aus dem Emer geformt, dem Urwesen, dessen Fleisch zu Erde, dessen Blut zu Gewaessern, dessen Knochen zu Gebirgen wurde. Die Welt ist kein toter Gegenstand. Sie ist ein verwandelter Organismus. Alles, was die Bewohner des Mittelgrunds bauen, tragen und benutzen, arbeitet mit dem Schoepfungsmaterial selbst — und das sieht man.

Das Leitprinzip heisst **Organische Gotik**: eine Architektur- und Designsprache, in der gotische Monumentalitaet auf biologische Logik trifft. Gebaeude wirken nicht konstruiert, sondern gewachsen. Kleidung ist nicht genaeht, sondern gezuechtet. Technologie pulsiert, atmet, reagiert. Nichts in dieser Welt ist mechanisch. Es gibt keine Zahnraeder, keine Dampfmaschinen, keine Schaltkreise. Es gibt Adern, Membranen, Nervenknoten und Stoffwechsel.

Die Tonalitaet ist duester, geerdet und politisch. Gotische Grandeur trifft feudale Brutalitaet. Aber — und das ist entscheidend — RELICS ist nicht heruntergekommen. Die Welt ist nicht postapokalyptisch. Sie ist futuristisch in einem organischen Sinne: fortschrittlich, ambitioniert, erschreckend elegant. Was hier verfaellt, verfaellt mit Grandeur. Was hier bluueht, blueht mit Zaeaehnen.

**Verbindliche Ausschluesse:**
- Kein Steampunk, keine Zahnrad-Aesthetik, keine mechanische Technologie
- Kein High Fantasy (keine Elfen, Orks, Zauberer mit Staeben)
- Keine Anachronismen (kein Schiesspulver, kein Buchdruck)
- Keine klassische Magie — alles ist Biologie, Chemie, Koerper

### 1.2 Aesthetische Saeulen

Drei Saeulen tragen jede visuelle Entscheidung in RELICS:

**Organik.** Technologie ist gewachsen, nie gebaut. Kabel sind Adern. Displays sind Membranen. Server sind Nervenknoten. Diese Uebersetzungslogik ist nicht metaphorisch — sie ist woertlich. Die Bewohner des Mittelgrunds arbeiten mit dem Emer-Material, dem Stoff, aus dem die Welt besteht. Ihre Technologie sieht aus wie Biologie, weil sie Biologie IST.

**Grandeur.** Alles in RELICS ist monumental. Staedte sind vertikal, Thronsaele erdrueeckend, Gildenhaallen kathedralenhaft. Selbst im Verfall bleibt die Grandeur — sie wird nur tragischer. Ein eingestuerzter Bogen ist nicht haesslich; er ist eine Ruine, die noch immer Ehrfurcht einfloeesst. Die visuelle Sprache lehnt sich an Gaudi, an gotische Kathedralen und an den Brutalismus: Formen, die den Betrachter klein machen.

**Ambivalenz.** Nichts in RELICS ist rein schoen oder rein haesslich. Die praeachtigste Halle hat Adern unter dem Putz. Das abstossendste Schattenfieber-Gewebe hat eine verstoeoerrende Eleganz. Das Biotech, das den Alltag erleichtert, und das Schattenfieber, das Koerper zersetzt, stammen aus derselben Quelle — dem Emer. Der Spieler soll nie sicher sein, ob das, was er sieht, bewundernswert oder beaengstigend ist. Idealerweise beides gleichzeitig.

### 1.3 Die Lebende Krone — Visuelles Leitmotiv

Die Lebende Krone, das Relikt dieser Iteration, ist das zentrale Designobjekt von RELICS und gleichzeitig die Verdichtung aller visuellen Prinzipien.

Sie ist ein organisches Artefakt aus der Grossen Flechtung — dem Akt, der die Daseinsebenen trennte. Sie besteht aus dem reinsten Emer-Material: lebendig, pulsierend, reagierend. Wer sie traegt, wird von ihr durchwachsen. Wurzelartige Strukturen dringen in den Schaedel, das Nervensystem, den Koerper des Traegers. Fruehere Traeger zeigten minimale Veraenderung. Die letzten Traeger waren nicht mehr ganz menschlich.

Die Krone ist kein Schmuckstueck. Sie ist ein Organismus. Sie waechst. Ihre Oberflaeche veraendert sich mit der Zeit, mit dem Traeger, mit dem Zustand der Hauten. Sie ist gleichzeitig das machtvollste und das gefaehrlichste Objekt der Welt. Und sie sieht genau so aus: betoeoerrend und zutiefst verstoeoerrend.

**Visuelle Merkmale der Lebenden Krone:**
- Grundform: Asymmetrisch, organisch, nie geometrisch perfekt. Kein Kronenreif — eher ein Geflecht aus Strukturen, die an Knochen, Koralle und Nervenstrang erinnern
- Oberflaeche: Transluzent an manchen Stellen, opak an anderen. Unter der Oberflaeche pulsieren schwache Lichtimpulse — wie ein langsamer Herzschlag
- Farbgebung: Blasses Elfenbein bis Bernstein, durchzogen von dunkleren Adern. An den Kontaktstellen zum Traeger: roetlich, wie frisches Gewebe
- Reaktivitaet: Die Krone bewegt sich. Nicht viel — aber genug, um den Betrachter zu verunsichern. Feine Haerchen oder Fasern an ihrer Unterseite suchen Kontakt
- Transformation: Je laenger sie getragen wird, desto mehr verschmilzt sie mit dem Traeger. Bei fortgeschrittener Symbiose (oder Parasitismus) sind Krone und Schaedel nicht mehr zu trennen

Die Lebende Krone ist der visuelle Beweis fuer das Leitprinzip von RELICS: Biotech ist kein Werkzeug. Es ist das Schoepfungsmaterial selbst — lebendig, eigenwillig und nie vollstaendig kontrollierbar.

### 1.4 Referenzkorridor

| Kategorie | Referenz | Was wir uebernehmen |
|-----------|----------|---------------------|
| Architektur | Antoni Gaudi (Sagrada Familia) | Organische Kurven, Rippen als Tragwerk, Natur als Konstruktionsprinzip |
| Architektur | Brutalismus (Barbican, Habitat 67) | Schwere, rohe Materialitaet, Funktion als Aesthetik, Monumentalitaet |
| Architektur | Gotische Kathedralen | Vertikalitaet, Strebewerk, Lichtdramatik |
| Mode | Burgundische Hofmode (15. Jh.) | Hennin, Houppelande, Mi-parti, ueberladene Silhouetten |
| Mode | Alexander McQueen | Skulpturale Silhouetten, Koerper als Material, Provokation durch Eleganz |
| Mode | Iris van Herpen | 3D-gedruckte Strukturen, organische Formen, Mode als Organismus |
| Spiele | Elden Ring | Monumentalitaet, Environmental Storytelling, Raumschoepfung |
| Spiele | Control (Remedy) | Brutalismus als Spielraum, uebernatuerliche Verfremdung bekannter Raeume |
| Spiele | Hollow Knight | Organische Formensprache, Insekten-Eleganz, Atmosphaere durch Silhouette |
| Spiele | Cyberpunk 2077 | Biotech-Integration in Alltag, Koerpermodifikation als Normalitaet |
| Kunst | HR Giger | Verschmelzung von Organischem und Technischem, Biomechanik |
| Kunst | Zdzislaw Beksinski | Duesterer Surrealismus, Koerper als Landschaft, Atmosphaere des Unbehagens |

---

## 2. Fraktionsvisuals

### 2.1 Kernprinzip: Drei Dialekte, eine Sprache

Alle drei Fraktionen des Mittelgrunds — die Krone, die Gilden und der Orden — nutzen dasselbe Biotech. Sie arbeiten mit demselben Emer-Material. Ihre Technologie hat denselben biologischen Ursprung. Aber sie nutzen sie voellig unterschiedlich, und das sieht man.

Die Krone verbirgt ihr Biotech hinter Prunk — es sickert durch den Verfall hindurch. Die Gilden stellen ihr Biotech offen zur Schau — es ist Werkzeug, Statussymbol, Infrastruktur. Der Orden leugnet sein Biotech oeffentlich — es operiert hinter makellosen Fassaden.

Drei Dialekte, eine Sprache. Der Spieler lernt das Biotech-Vokabular in einer Fraktion und erkennt es dann in den anderen wieder — aber verzerrt, anders betont, mit anderem Subtext. Ein Gilden-Nervenstrang, der offen an einer Hauswand verlaeuft, ist Infrastruktur. Derselbe Nervenstrang, der unter dem Putz eines Kronenpalasts hervorleuchtet, ist ein Zeichen des Verfalls. Derselbe Nervenstrang, der hinter einer Ordensklostermauer entdeckt wird, ist ein Skandal.

### 2.2 Die Krone — Grandeur im Zerfall

**Leitbild:** Ein Ballsaal, in dem die Waende atmen.

Die Krone ist die aelteste Fraktion, die sich am laengsten auf das Relikt — die Lebende Krone — beruft. Ihre visuelle Identitaet spiegelt genau das wider: vergangene Groesse, die unter ihrem eigenen Gewicht nachgibt. Die Krone-Aesthetik ist nie erbaermlich, nie schmuddelig. Sie ist tragisch. Eine Koenigin in einem Kleid, das atemberaubend schoen ist — und an den Saaeumen leise zerfaellt.

**Architektur:**
Die Architektur der Krone ist Palastgotik: hohe, schlanke Boegen, die einen Anspruch auf Vertikalitaet formulieren, den die Substanz nicht mehr traegt. Thronsaele mit Deckengewoelben, die sich unter dem eigenen Gewicht leicht kruemmen. Fassaden aus behauenem Stein, durchzogen von feinen Rissen, durch die ein schwaches, warmes Leuchten dringt — das Biotech, das unter dem Putz lebt.

Die Krone-Gebaeude waren einst vollstaendig versiegelt. Das Biotech unter der Oberflaeche war unsichtbar, ein Geheimnis der Baumeister. Aber die Zeit hat die Versiegelung aufgebrochen. Der Verfall entbloesst, was verborgen sein sollte: pulsierendes Gewebe unter abgeplatztem Stuck, biolumineszente Adern in gerissenen Waenden, organische Strukturen, die sich durch Fensterrahmen arbeiten. Die Krone versucht, diese Stellen zu reparieren, zu uebertuenchen, zu verhaengen. Es reicht nie ganz.

Einhaendige Statuen stehen in den Thronsaelen und an den Portalen — Sigvalt, der seine Hand gab, um die Grosse Flechtung zu halten. Die geopferte Hand ist das zentrale Symbol der Krone-Herrschaft: Macht durch Opfer, Pflicht durch Verlust. Die Statuen sind alt, verwittert, aber nie vernachlaessigt. Sie werden gepflegt wie Ahnengraeber.

Kronleuchter aus Biolumineszenz haengen in den grossen Hallen. Kein Feuer — lebende Lichtorgane, gezuechtet und in Schmiedeeisenrahmen gefasst. Ihr Licht ist warm, leicht goldgelb, aber nie gleichmaessig. Es pulsiert kaum wahrnehmbar, wie ein Herzschlag, der langsamer wird.

**Leitform:** Vertikale, schlanke Boegen. Spitze nach oben, schmal wie ein Seufzer. Anspruch auf Hoehe, den die Substanz nicht mehr traegt.

**Materialsprache:** Verblasster Samt, angelaufenes Gold, lebendiger Stein. Brokat, dessen Faeden sich bei genauem Hinsehen bewegen. Poliertes Holz, unter dem eine weiche, warme Schicht liegt. Alles in der Krone war einmal praechtiger.

**Ikonographie:**
- Sigvalts geopferte Hand (einhaendige Statuen, Handmotiv in Wappen und Siegeln)
- Die Krone selbst als abstrahiertes Symbol — nicht die Lebende Krone, sondern ihre stilisierte Form
- Vertikale Linien, aufwaerts gerichtete Spitzen — der Anspruch auf Hoehe

### 2.3 Die Gilden — Organischer Brutalismus

**Leitbild:** Eine Fabrik, die lebt.

Die Gilden sind die oekonomische Macht des Mittelgrunds. Sie sehen in der Welt einen Tharm — ein Eingeweide, ein Material, mit dem man arbeiten kann. Ihre visuelle Identitaet ist ehrlich bis zur Haerte: hier wird nichts verborgen, nichts beschoenigt, nichts mystifiziert. Biotech ist Infrastruktur. Wenn eine Wand eine Ader braucht, dann sieht man die Ader.

**Architektur:**
Die Gilden-Architektur ist organischer Brutalismus: massiv, funktional, ungeschoent. Schwere horizontale Bloecke aus gegossenem Material, durchzogen von sichtbaren organischen Systemen. Die Gebaeude der Gilden atmen. Man kann es sehen — die leichte Ausdehnung und Kontraktion der Fassade, die rhythmische Bewegung der Membranfenster. Man kann es hoeren — ein tiefes, gleichmaessiges Summen in den Waenden. Und wenn man die Hand auf den Beton legt, spuert man Waerme.

Gildenhallen sind kathedralenhaft in ihrem Ausmass, aber voellig anders in ihrer Wirkung. Wo die Krone nach oben strebt, breiten sich die Gilden horizontal aus. Lagerhallen mit frei liegenden Deckenrippen, die wie Brustkoerbe aussehen. Marktplaetze, deren Bodenfliesen ein feines Netzwerk von Kapillaren zeigen — Naehrstofftransport fuer die lebenden Waende ringsum. Kontore, deren Schreibpulte aus Chitin gefertigt sind und deren Tinten in organischen Behaeltern pulsieren.

Die Gilden bauen nicht — sie zuechten. Ein neues Gebaeude wird nicht errichtet, sondern GESETZT. Man legt einen Biotech-Kern in das Fundament und laesst das Gebaeude wachsen, geformt durch Leitkulturen und Naehrstoff-Lenkung. Der Prozess dauert Jahre. Das Ergebnis ist ein Gebbaeude, das lebt, atmet, altert und stirbt. Die Gilden wissen das. Sie kalkulieren die Lebensdauer ein.

**Leitform:** Schwere horizontale Bloecke. Breite Boegen, gedrungene Proportionen. Funktionalitaet als Aesthetik: Was eine Pumpe ist, sieht aus wie eine Pumpe.

**Materialsprache:** Roher Beton (oder sein organisches Aequivalent — gegossenes Emer-Material), Chitin-Verkleidung, transluzente Membran-Fenster. Metalle nur als Beschlag und Rahmen. Alles hat eine Funktion, nichts ist Dekoration.

**Ikonographie:**
- Erthags Prinzip: die Waage, der Vertrag, der Preis aller Dinge
- Die Flechtung als Handwerksmotiv — verflochtene Linien in Gildenwappen, Knotenornamente
- Horizontale Linien, Symmetrie, Ausgleich — nichts wird umsonst gegeben

### 2.4 Der Orden — Die makellose Luege

**Leitbild:** Ein Krankenhaus, das dich beobachtet.

Der Orden ist die gefaehrlichste Fraktion — visuell, weil er die unschuldigste ist. Die Fassaden des Ordens sind geometrisch perfekt, aus geschliffenem Kalkstein, ohne Ornament, ohne sichtbare Technologie, ohne den kleinsten Hinweis auf das, was dahinter liegt. Zisterzienser-Strenge als Architekturprogramm: Reinheit, Klarheit, Kontrolle.

Dahinter liegt etwas anderes.

**Architektur — die Fassade:**
Von aussen sind Ordensgebaeude die schoensten Bauwerke des Mittelgrunds. Nicht prunkvoll wie die Krone, nicht wuchtig wie die Gilden — schlicht schoen. Perfekte Proportionen, weisser Stein, Kreuzgaenge mit sanftem Lichteinfall. Klostergaerten, in denen medizonische Krauter wachsen. Bibliotheken mit Holzregalen und Pergamentbuechern. Schulraeume mit Kreidewaenden. Der Orden bildet aus. Der Orden heilt. Der Orden bewahrt Wissen. Das ist die Botschaft der Architektur, und sie ist nicht gelogen — sie ist nur nicht die ganze Wahrheit.

**Architektur — dahinter:**
Hinter den makellosen Fassaden betreibt der Orden die fortschrittlichste Biotech-Forschung des Mittelgrunds. Die Innenbereiche, zu denen nur hohe Raenge Zugang haben, sind ein Negativbild der Fassade: Nervenstrang-Korridore, Waende aus pulsierendem Gewebe, Raeume, in denen organische Ueberwachungsnetze jeden Schritt registrieren. Augen in den Waenden. Ohren in den Boeden. Ein Netzwerk aus lebendem Sensorgewebe, das den Orden ueber alles informiert, was in seinen Mauern geschieht.

Die Ordensarchitektur hat zwei Schichten, und der Uebergang zwischen ihnen ist das spannendste architektonische Element in RELICS. Es gibt Tueren, hinter denen der weisse Kalkstein ploetzlich in feuchtes, warmes Gewebe uebergeht. Korridore, die als ordentliche Kreuzgaenge beginnen und in organische Tunnel muenden. Treppen, deren Stufen ab einer gewissen Tiefe nicht mehr aus Stein bestehen, sondern aus etwas, das unter dem Fuss leicht nachgibt.

**Halvards Symbolik:**
Das zentrale Symbol des Ordens ist Halvards Auge — das geopferte Auge des Halvard, der es gab, um die Flechtung zu SEHEN. Das verbliebene Auge sah die Welt. Das geopferte Auge sah das Hohlicht — fuer immer. Halvards Raben sind das allgegenwaertige Motiv: in Steinrelief an den Fassaden, als Wetterfahnen auf den Daechern, als Stickerei auf den Roben. Die Raben sind Halvards Augen in der Welt — und die Orden-Architektur spiegelt genau das wider: eine Struktur, die alles sieht.

Das Augenmotiv taucht in der Geheimarchitektur oeffentlich auf. Nicht als Dekoration — als Funktion. Die organischen Sensorknoten in den Waenden SIND Augen: biologische Ueberwachungsorgane, die registrieren, filtern, weiterleiten. Wer die Geheimebene des Ordens betritt, wird von Dutzenden dieser Augen beobachtet. Sie blinzeln.

**Leitform:** Perfekte Symmetrie aussen, organisches Chaos innen. Kreise, Boegen, gleichmaessige Proportionen — die geometrische Perfektion, die nur durch vollstaendige Kontrolle moeglich ist.

**Materialsprache:** Geschliffener Kalkstein (aussen), Messing-Akzente fuer Beschlaege und Instrumente. Dahinter: pulsierendes Gewebe, Nervenstrangbuendel, organische Membranen. Der Kontrast zwischen Fassade und Innerem ist das staerkste visuelle Statement des Ordens.

**Ikonographie:**
- Halvards Auge (das geopferte Auge als zentrales Symbol, allgegenwaertig)
- Halvards Raben (Ueberwachung, Wissen, Praesenz)
- Geschlossene Formen — Kreise, konzentrische Ringe, das Auge als Form

---

## 3. Biotech-Grammatik

### 3.1 Das Prinzip

Biotech in RELICS ist keine Metapher. Es ist die logische Konsequenz einer Welt, die aus einem lebenden Koerper geformt wurde. Wenn die Erde Fleisch ist, die Fluesse Blut, die Berge Knochen — dann ist jede Technologie, die mit diesem Material arbeitet, zwangslaeufig biologisch. Die Bewohner des Mittelgrunds haben ueber Generationen gelernt, das Emer-Material zu kultivieren, zu zuechten, zu formen. Sie nennen es nicht "Technologie". Fuer sie ist es Handwerk, Heilkunde, Alchemie. Aber fuer den Spieler — und fuer uns als Gestalter — ist es Biotech.

### 3.2 Uebersetzungsregeln

Jedes technologische Element der realen Welt hat ein organisches Aequivalent in RELICS. Diese Uebersetzung ist verbindlich fuer alle Assets:

| Reale Technologie | RELICS-Aequivalent | Visuelle Umsetzung |
|---|---|---|
| Kabel, Leitungen | Adern, Sehnen | Pulsierende Straenge unter/auf Oberflaechen, erkennbarer Fluessigkeitstransport |
| Displays, Anzeigen | Membranen | Transluzente, biolumineszente Flaechen, die Muster zeigen (keine Pixel, sondern organische Leuchtmuster) |
| Server, Datenspeicher | Nervenknoten, Ganglien | Kompakte organische Verdickungen an Knotenpunkten, warm, leicht pulsierend |
| Energieleitung | Stoffwechsel, Naehrloesung | Sichtbarer Fluessigkeitstransport in Adern, Farbe veraendert sich mit Energiegehalt |
| Sensoren, Kameras | Augen, Haerchen, Poren | Organische Sensororgane: Augen (Orden), Haerchen die auf Beruehrung reagieren (Gilden), Poren die Stoffe aufnehmen (Krone) |
| Beleuchtung | Biolumineszenz | Leuchtorgane in verschiedenen Formen — Kugeln, Straenge, Flaechen. Fraktionsabhaengig in Farbtemperatur |
| Tueren, Schleusen | Sphinkter, Membranen | Organische Oeffnungen, die sich dehnen und zusammenziehen. Geschlossene Membranen als Tueren (Gilden), Steintueren mit organischem Schloss (Krone/Orden) |
| Heizung, Klimatisierung | Koerperwaerme, Stoffwechsel | Gebaeude regulieren ihre Temperatur selbst. Waende strahlen Waerme ab. Bei Kaelte ziehen sich Oeffnungen zusammen. |

### 3.3 Sichtbarkeitsgrade

Die Sichtbarkeit von Biotech ist die wichtigste Differenzierung zwischen den Fraktionen. Dieselbe Technologie sieht in drei verschiedenen Kontexten voellig unterschiedlich aus:

| Grad | Krone | Gilden | Orden |
|------|-------|--------|-------|
| **Versteckt** | Standard — Biotech gehoert unter den Putz | Selten — warum verstecken, was funktioniert? | Oeffentliche Norm — der Orden LEUGNET Biotech |
| **Sichtbar** | Nur bei Verfall — das Verborgene dringt durch | Standard — offen, funktional, pragmatisch | Nur intern — in den Geheimebenen, hinter verschlossenen Tueren |
| **Dominant** | Nie — waere ein Eingestaendnis des Verfalls | Prestigebauten — die Gildenhalle als atmendes Monument | Geheime Labore — hier ist die Biologie total, Architektur existiert nicht mehr |

### 3.4 Skala

Biotech existiert auf drei Skalen, und jede hat eigene Designregeln:

**Mikro (Koerper und Gegenstaende):** Biotech in Kleidung, Schmuck, Werkzeug, Waffen. Feine Adern in Lederhandschuhen. Ein Schwertgriff, der sich der Hand anpasst. Ein Amulett, das warm wird, wenn der Traeger krank ist. Auf dieser Skala ist Biotech intim, persoenlich, fast unauffaellig.

**Meso (Moebel und Raeume):** Biotech in Tueren, Moebeln, Beleuchtung, Raumkontrolle. Membrantueren in Gildenhaeusern. Leuchtorgane in Krone-Kronleuchtern. Organische Schlossmeechnismen in Ordensarchiven. Auf dieser Skala wird Biotech raumbildend: es definiert, wie ein Raum funktioniert, sich anfuehlt, reagiert.

**Makro (Gebaeude und Infrastruktur):** Biotech in Architektur, Stadtinfrastruktur, Verteidigung. Gebaeude, die atmen (Gilden). Stadtmauern, die Wunden heilen (Krone). Ueberwachungsnetzwerke, die eine ganze Festung durchziehen (Orden). Auf dieser Skala ist Biotech die Stadt selbst. Die Grenze zwischen Gebaeude und Organismus verschwindet.

---

## 4. Farbsystem

### 4.1 Grundprinzip: 70/20/10

Jede Fraktionspalette folgt der 70/20/10-Regel: 70% Basis (die dominante Stimmung), 20% Akzent (die Fraktionsidentitaet), 10% Highlight (das Besondere, Seltene, Auffaellige). Diese Verteilung ist verbindlich fuer alle Assets — Environments, Charaktere, UI-Elemente.

### 4.2 Fraktionspaletten

**Die Krone**

| Rolle | Farbe | Hex | Verwendung |
|-------|-------|-----|------------|
| 70% Basis | Aschgrau | `#3D3D3D` | Stein, Schatten, verwitterte Flaechen, Hintergrund |
| 20% Akzent | Karmin | `#8B1A2B` | Wappen, Textilien, Biotech-Glow unter dem Putz, Blut |
| 10% Highlight | Altgold | `#C5A030` | Kronenreste, Ornamente, Biolumineszenz in Thronsaelen |

Das Karmin der Krone ist WARM — es erinnert an altes Blut, an Samt, an das Leuchten unter der Haut. Es ist nie grell. Es ist die Farbe von etwas, das einmal lebendig war und langsam erkaltet. Das Altgold erscheint nur in Momenten: ein Kronleuchter, ein Wappen, ein Sonnenstrahl auf einem vergoldeten Rahmen. Es ist die Erinnerung an bessere Zeiten.

**Die Gilden**

| Rolle | Farbe | Hex | Verwendung |
|-------|-------|-----|------------|
| 70% Basis | Warmer Beton | `#7A6E5D` | Architektur, Boeden, Arbeitsflaechen, Alltag |
| 20% Akzent | Amber | `#C49A20` | Handel, Licht, Reichtum, biologische Fluessigkeiten |
| 10% Highlight | Cyan | `#2EC4B6` | Biotech-Fluessigkeit in Adern, aktive Membranen, Gildenstempel |

Amber und Cyan bilden ein komplementaeres Spannungsfeld. Das Amber steht fuer Handel, Waerme, Profit — alles, was die Gilden nach aussen zeigen. Das Cyan ist die Farbe des Biotech im Betrieb: die Fluessigkeit in den Adern, das Leuchten aktiver Membranen, der Stoff, mit dem gearbeitet wird. Zusammen erzeugen sie eine Palette, die gleichzeitig einladend und industriell wirkt.

**Der Orden**

| Rolle | Farbe | Hex | Verwendung |
|-------|-------|-----|------------|
| 70% Basis | Kalkweiss | `#E8E4DE` | Fassade, Reinheit, Kontrolle, die oeffentliche Seite |
| 20% Akzent | Schieferblau | `#4A5568` | Roben, Schatten, Autoritaet, Strenge |
| 10% Highlight | Bernstein | `#D4A017` | Geheime Biotech-Anlagen, Warnfarbe, das Verborgene |

Die Palette des Ordens hat eine doppelte Lesart. Von aussen: Kalkweiss und Schieferblau — kuuehl, ruhig, vertrauenswuerdig. Die Farben einer Institution, der man seine Kinder anvertraut. Von innen: Bernstein — die Farbe des versteckten Biotech, der warme, beunruhigende Kontrast zum kuuehlen Aeusseren. Bernstein ist die Farbe von Harz, von eingeschlossenem Leben, von Dingen, die konserviert und kontrolliert werden. Wenn der Spieler im Orden Bernstein sieht, weiss er: hier beginnt die Wahrheit.

### 4.3 Globale Akzente

Bestimmte Farben gehoeren keiner Fraktion, sondern der Welt:

| Kontext | Farben | Hex | Bedeutung |
|---------|--------|-----|-----------|
| Schattenfieber | Violett-Schwarz + Giftgruen | `#2D0A31` + `#39FF14` | Kosmologische Erosion, krank-organisch, ALARM |
| Wildnis | Moosgruen, Erdtoene, Nebel-Grau | `#5C6B3C`, `#8B7355`, `#9E9E9E` | Natur jenseits der Fraktionen, der Mittelgrund als Landschaft |
| Tiervolk | Ocker, Terrakotta, Sand | `#CC7722`, `#C04000`, `#C2B280` | Warme Naturtoene, fremd aber nicht bedrohlich |

### 4.4 Farbregeln

**Regel 1: Fraktionsfarben mischen sich nicht.** Der Spieler erkennt Zugehoerigkeit an der Palette. Kein Krone-Gebaeude hat Cyan-Akzente. Kein Gilden-Kontor hat Karmin-Textilien. Die Farbsprache ist eindeutig und nicht verhandelbar.

**Regel 2: Uebergangszonen sind neutral.** Maerkte, Grenzgebiete, Karawanenwege nutzen die neutrale Wildnis-Palette. Hier treffen sich die Fraktionen, und die Abwesenheit von Fraktionsfarben macht das visuell spuerbar.

**Regel 3: Schattenfieber bricht JEDE Palette.** Egal welche Fraktionsfarben einen Raum dominieren — wenn das Schattenfieber einbricht, ueberschreibt Violett-Schwarz plus Giftgruen alles. Das ist das staerkste visuelle Alarmsignal in RELICS: Wenn sich die Farben aendern, stimmt etwas fundamental nicht.

**Regel 4: Die Lebende Krone hat keine Fraktionsfarbe.** Die Krone ist aelter als alle Fraktionen. Ihre Farben — Elfenbein, Bernstein, duenkle Adern — gehoeren nur ihr. Wenn sie in einer Szene auftaucht, ist sie farblich fremd. Das ist Absicht.

**Hinweis fuer Shader-Implementation (V2, ACES-Validiert):** Alle Hex-Codes in diesem Dokument sind sRGB-Werte, kalibriert fuer UE5-Rendering mit aktivem ACES-Tonemapping. ACES hebt Mitteltöne und saettigt Farben leicht ab — warme Toene (Altgold `#C5A030`, Amber `#C49A20`, Bernstein `#D4A017`) sind bewusst tiefer gesetzt als Display-Normal, um nach ACES-Kompression korrekt zu erscheinen. Giftgruen (`#39FF14`) ist HDR-intensiv — soll im SDR-Bereich saturiert wirken, im HDR-Bereich leuchten. Keine Abweichungen von diesen Werten ohne Abstimmung mit Vera und Tobi.

---

## 5. Mode & Ruestung

### 5.1 Leitprinzip: High Fashion Mittelalter + Biotech-Layer

Mode in RELICS ist kein Nebenprodukt. Sie ist ein Erzaehlmedium. Was ein Charakter traegt, sagt dem Spieler: zu welcher Fraktion gehoert er, wie wohlhabend ist er, wie viel Biotech hat er Zugang, und — bei fortgeschrittenem Schattenfieber — was passiert mit seinem Koerper.

Die Basis ist die burgundische Hofmode des 15. Jahrhunderts: Hennin (die hohen, spitzen Hauben), Houppelande (die weiten, bodenlangen Uebergewaender), Mi-parti (die laengsgeteilten Farben). Diese historische Grundlage wird durch einen Biotech-Layer erweitert: organische Elemente, die in die Kleidung integriert sind — nicht als Ersatz, sondern als Erweiterung.

Biotech in der Mode ist ein Statussymbol. Wie bei Schmuck: Wer es sich leisten kann, traegt Kleidung, die lebt. Ein Kragen, dessen Stoff sich der Koerpertemperatur anpasst. Handschuhe mit feinen Adern, die den Puls des Traegers spueren. Ein Umhang, der bei Wind seine Dichte veraendert. Das ist Luxus, keine Notwendigkeit — und genau deshalb erzaehlt es Geschichten.

### 5.2 Fraktionsmode

**Krone — Zeremoniell, ueberladen, fragil:**
Die Krone-Mode ist der sichtbarste Ausdruck des Verfalls. Aeusserlich: atemberaubend. Samt und Brokat in Karmin und Altgold, Schichtung ueber Schichtung, Silhouetten, die Raum beanspruchen. Die Houppelande der hohen Krone-Adeligen sind so weit, dass sie Tueren fuellen. Die Hennin so hoch, dass sie bei jedem Schritt leicht schwanken.

Darunter — wer genau hinsieht — lebt etwas. Die Unterkleidung der Krone-Elite ist organisch: ein eng anliegender Anzug aus lebendem Gewebe, das den Koerper stuetzt, waermt und — bei den Aeltesten — zusammenhaelt. Die praechtigen Obergewaender verbergen, dass manche Krone-Adelige ihren Koerper ohne dieses Biotech-Korsett nicht mehr aufrecht halten koennten. Die Mode ist Fassade, die Biotech-Unterschicht ist Notwendigkeit.

**Gilden — Pragmatisch-elegant:**
Die Gilden tragen Mode als Investition. Leder und Chitin-Panzerung, praezise geschnitten, sichtbar teuer, aber nie verschwendereisch. Gilden-Mode sagt: Ich bin erfolgreich, und ich kann es mir leisten, gut auszusehen, waehrend ich arbeite.

Biotech ist offen integriert: verstaerkte Naehte aus organischem Material, Taschen mit Membranverschluessen, Stiefel mit Sohlen, die sich dem Untergrund anpassen. Die reichsten Gildenhaendler tragen Umhaenge aus gezuechtetem Stoff — ein Material, das kein Weber herstellen kann, sondern nur ein Biotech-Zuechter. Das ist der Gilden-Luxus: nicht Dekoration, sondern ueberlegene Funktion.

**Orden — Asketisch-uniform:**
Die Roben des Ordens sind weiss, bodenlang, ohne Verzierung. Schieferblau fuer die Umhaenge, Messing fuer die Schnallen. Die niedrigen Raenge sehen alle gleich aus. Das ist Absicht. Der Orden verlangt Selbstaufloesung — die Individualitaet verschwindet hinter der Uniform.

Die hohen Raenge tragen dasselbe — aber wer genau hinsieht, bemerkt Details. Ein leicht unnatuerlich glattes Gesicht. Haende, die keine Falten haben. Augen, die im falschen Licht bernsteinfarben schimmern. Die Biotech-Implantate des Ordens sind nicht sichtbar — sie sind unter der Haut. Subdermal. Nahtlos. Die makellosen Koerper der hohen Ordensvertreter sind ihr bestgehuetretes Geheimnis und ihr offensichtlichstes Zeichen — fuer den, der hinzusehen weiss.

### 5.3 Ruestungsphilosophie

Ruestung in RELICS ist nicht geschmiedet — sie ist gezuechtet. Organische Panzerung aus kultiviertem Chitin, gehaertetem Kollagen und verstaerkten Sehnenstrukturen. Keine Plattenruestung, keine Kettenhemden im klassischen Sinne. Die Schutzbekleidung der Welt folgt derselben biologischen Logik wie alles andere.

**Leichte Ruestung:** Verstaerkte Kleidung mit eingewachsenen Chitin-Platten an kritischen Stellen. Flexibel, leise, unauffaellig. Gilden-Soeldner und Tiervolk bevorzugen diesen Typ.

**Mittlere Ruestung:** Vollstaendige Chitin-Schale ueber einem organischen Unterbau. Die Platten sind ineinander verzahnt wie ein Exoskelett. Beweglich, aber deutlich sichtbar als Ruestung. Standard fuer Krone-Soldaten.

**Schwere Ruestung:** Dickes, mehrschichtiges organisches Material — fast wie ein zweiter Koerper. Die Ruestung waechst um den Traeger herum und muss regelmaessig genaehrt werden (Naehrloesung, Pflege). Ordensritter und Elite-Kronengarden tragen diesen Typ. Er ist beeindruckend und leicht verstoeoerrend: die Grenzen zwischen Traeger und Ruestung verschwimmen bei laengerem Tragen.

**Gezuechtete Ruestung als Luxusgut:** Die Gilden kontrollieren die Zucht der besten Ruestungsmaterialien. Eine massgeschneiderte Gilden-Ruestung ist ein Vermoegen wert — und ein Statussymbol. Sie passt sich dem Traeger an, heilt kleine Beschaedigungen selbst und waechst mit (bis zu einem gewissen Grad). Wer eine solche Ruestung traegt, sagt damit: Ich bin die Investition wert.

**OFFEN:** Detaillierte Ruestungsklassen und ihre Kampf-Mechanik — Abstimmung mit Leo (GDD-02) und Darius erforderlich. Visuelle Differenzierung der Ruestungsstufen in Concept Art: V3.

### 5.4 Spieler-Customization & Dominanzprinzip

Der Spielercharakter kann Ruestung und Kleidung individuell kombinieren (CD-Vorgabe). Das System muss visuell lesbar bleiben: Fraktionszugehoerigkeit, Ruestungsklasse und Schattenfieber-Status muessen auf einen Blick erkennbar sein, auch bei frei kombinierten Sets.

**Dominanzprinzip — Torso-Primat:**

Die Fraktionszugehoerigkeit eines Outfits wird durch den Torso-Slot definiert. Der Torso ist der visuell dominanteste Koerperbereiche im Third-Person-Spiel — er ist immer sichtbar, er traegt die groesste Flaeche an Fraktionsfarben und Ikonographie.

| Kombination | Visuelles Ergebnis | Fraktionslesbarkeit |
|-------------|-------------------|---------------------|
| Torso Fraktion A + alle anderen Slots Fraktion A | Reine Fraktion | Eindeutig Fraktion A |
| Torso Fraktion A + bis zu 2 Slots Fraktion B | Fraktion A mit Akzenten | Fraktion A erkennbar, B als Kontrast lesbar |
| Torso Fraktion A + 3+ Slots Fraktion B | Gemischtes Set | Visuell neutral — Haendler-Lesart, keine eindeutige Fraktionszugehoerigkeit |
| Torso neutral (Tiervolk/Wildnis) + beliebige Slots | Neutrales Set | Kein Fraktionssignal |

**Schattenfieber ueberschreibt das Dominanzprinzip.** Ab Infektionsstufe 2 (Risse, Wert 41+) sind am Koerper des Spielers Schattenfieber-Zeichen sichtbar — unabhaengig davon, welches Outfit getragen wird. Die Fraktionszugehoerigkeit bleibt lesbar, aber das Schattenfieber-Signal ist dominant. Kein Outfit verbirgt fortgeschrittene Infektion.

**NPC-Reaktion auf gemischte Sets:** NPCs lesen Fraktionszugehoerigkeit am Outfit. Gemischte Sets erzeugen ambivalente NPC-Reaktionen — kein Fraktions-Bonus, kein Fraktions-Malus. Das koennen erfahrene Spieler gezielt einsetzen, um Fraktionssignale zu neutralisieren. Design-Entscheidung: Das ist kein Bug, sondern eine Spieloption.

---

## 6. Tiervolk — Visuelle Identitaet

### 6.1 Leitprinzip: Alien-Elegant, nicht Tribal

Das Tiervolk ist fremd. Nicht fremdartig wie ein Fantasywesen aus einem Kinderbuch — fremd wie etwas, das fast menschlich ist, aber nicht ganz. Die Differenz ist subtil und genau deshalb verstoeoerrend. Die CD-Vorgabe ist klar: "Leicht alien vs. menschlich clean." Das Tiervolk soll den Spieler faszinieren und leicht verunsichern, nie abstossen und nie verharmlosen.

Das Tiervolk hat keine eigene Architektur. Sie sind Nomaden, Gaeste in den Fraktionsstaedten. Haendler und Diebe, keine Handwerker. Sie bauen nicht — sie bewegen sich. Ihre visuelle Identitaet liegt deshalb vollstaendig in ihren Koerpern, ihrer Kleidung und ihren Objekten.

### 6.2 Koerperdesign

Die Tier-Merkmale des Tiervolks sind nicht offensichtlich. Kein Fellkoerper, keine Schnauze, keine Schweife. Stattdessen: Pupillenformen, die nicht menschlich sind — schlitzfoerrmig, horizontal, sternfoermig. Hautstrukturen, die an Schuppen, Federn oder feinstes Fell erinnern, aber erst bei Naehe sichtbar werden. Proportionen, die knapp daneben liegen: Finger ein Gelenk zu lang, Haelse etwas zu beweglich, Schultern in einem Winkel, der menschlich nicht funktionieren wueerde.

Kein Mitglied des Tiervolks sieht aus wie ein bestimmtes Tier. Die Merkmale sind gemischt, individuell, irreduzibel. Sie erinnern an ETWAS — aber der Spieler kann nie genau sagen, woran. Das ist der Kern des Designs: das Unheimliche im Fast-Vertrauten.

Bewegungsmuster verstaerken den Effekt. Ein Tiervolk-Haendler dreht den Kopf eine Spur zu weit. Eine Tiervolk-Diebin bewegt sich mit einer Geschmeidigkeit, die kein Mensch hat. Ein Tiervolk-Aeltester sitzt in einer Haltung, die bequem aussieht, aber fuer ein menschliches Skelett unmoeglich waere. Das sind keine grossen Gesten — es sind Details, die sich addieren.

### 6.3 Kleidung & Schmuck

Die Kleidung des Tiervolks erzaehlt ihre Geschichte: zusammengesammelt aus allen Fraktionen, zusammengetragen auf Wanderungen, umgearbeitet mit eigenen Techniken. Ein Tiervolk-Haendler traegt vielleicht einen Krone-Samtumhang ueber Gilden-Lederstiefeln, befestigt mit Orden-Messingschnallen. Die Kombination ist eklektisch, nie zufaellig — sie verraet, in welcher Fraktionsstadt er zuletzt war, mit wem er gehandelt hat, wo er willkommen war.

Daneben existiert eine eigene Schmucktradition: Knochen, Bernstein, Flusskiesel, gefundene Biotech-Fragmente. Die Fragmente sind besonders aussagekraeftig — das Tiervolk sammelt abgestorbene oder abgefallene Biotech-Stuecke und verarbeitet sie zu Schmuck. Was fuer die Fraktionen Abfall ist, wird fuer das Tiervolk Ornament. Das ist kein Primitivismus — es ist eine andere Wertschaetzung desselben Materials.

### 6.4 Farbpalette

Warme Naturtoene als Basis: Ocker (`#CC7722`), Terrakotta (`#C04000`), Sand (`#C2B280`). Diese Palette setzt sich von allen drei Fraktionspaletten ab und signalisiert sofort: hier ist jemand, der keiner Fraktion gehoert. In ihrem Eigendesign — dem, was nicht von Fraktionen zusammengetragen ist — verwendet das Tiervolk keine Fraktionsfarben. Kein Karmin, kein Amber, kein Kalkweiss. Ihre Farben sind die Farben der Wege zwischen den Staedten: Staub, Lehm, Sonnenbraun.

---

## 7. Schattenfieber — Visuelle Manifestation

### 7.0 Referenztabelle: Stufen und Grenzen

> Diese Tabelle ist verbindlich und identisch in GDD-02, GDD-03 und GDD-05. Keine Abweichungen. (CD-Entscheidung, Tag 4, Szene 3.)

| Infektionswert | Narrativer Zustand (Nami/GDD-03) | Mech. Stufe (Darius/GDD-02) | Visueller Status (Vera/GDD-05) |
|---------------|----------------------------------|------------------------------|-------------------------------|
| 0 | Gesund | Stufe 0 — Rein | Stufe-0-Baseline: keine Schattenzeichen |
| 1–40 | Rauschen | Stufe 1–2 (Gezeichnet/Infiziert) | Subtile Schattenzeichen, schwaches Schimmern |
| 41–75 | Risse | Stufe 3 (Verwandelt) | Sichtbare Schattenzeichen, Koerperveraenderung |
| 76–100 | Schwelle | Stufe 4 (Entfesselt) | Erschreckende Transformation, Koerpergrenze uneindeutig |

Halluzinations-Start: Wert 76 (Beginn Stufe 4/Schwelle).

### 7.1 Leitprinzip: Die falsche Organik

Biotech ist schoeen-organisch. Schattenfieber ist krank-organisch. Beide stammen aus derselben Quelle — dem Emer-Material —, aber das Schattenfieber ist die unkontrollierte Variante, und das sieht man. Wo Biotech pulsiert, zuckt das Schattenfieber. Wo Biotech waechst, wuchert das Schattenfieber. Wo Biotech leuchtet (in Amber, Cyan, Altgold), glueeht das Schattenfieber in FALSCHEN Farben: Violett-Schwarz (`#2D0A31`) und Giftgruen (`#39FF14`).

Das Schattenfieber-Farbsignal ist das staerkste visuelle Alarmsignal in RELICS. Es bricht jede bestehende Palette, jede Fraktionsaesthetik, jede architektonische Ordnung. Wenn der Spieler in einem Krone-Palast Giftgruen sieht, weiss er sofort: etwas ist sehr falsch. Das Signal muss unmissverstaendlich sein — kein subtiler Uebergang, sondern ein visueller Bruch.

### 7.2 Vier visuelle Zustaende

**Stufe 0: Baseline — Rein (Infektionswert 0)**

Der uninfizierte Spieler ist die visuelle Nulllinie. Alles, was Schattenfieber ab Wert 1 zeigt, definiert sich als Abweichung von diesem Zustand.

Am Koerper: Keine Auffaelligkeiten. Normale Hautfarbe, normale Pupillen, normale Schatten. Das Nervensystem-UI (GDD-02, Kap. 3) zeigt alle vier Aeste in vollem, klarem Licht — keine Schatten-Ueberlagerungen, kein Violett-Schwarz. Augen reagieren normal auf Licht. Schatten fallen korrekt.

In der Umgebung: Der Spieler sieht nur die erste Schicht der Welt. Verstecktes Biotech ist unsichtbar. Emotionen von NPCs sind nicht ablesbar. Schattenfieber-Zonen sind erkennbar durch physische Warnsignale (Geruch, Temperatur, Licht) — aber nicht durch Schattensinne.

Gameplay-Relevanz: Stufe 0 ist kein Nachteil — sie ist ein anderer Spielstil. Volle Systemeffizienz aller Nervensystem-Aeste (Cardio, Muskel, Lymph). Volle Alchemie-Wirksamkeit. Keine sozialen Einschraenkungen. Das Stufe-0-Aequivalent zu Schattensinnen ist Alchemie plus Trainerfaehigkeiten — andere Mittel, gleichwertiger Spielraum.

**Rauschen: Infektionswert 1–40**

Am Koerper: Subtil. Adern unter der Haut, die leicht dunkler erscheinen als normal. Bei bestimmten Lichtwinkeln ein schwaches violettes Schimmern auf der Haut. Pupillen, die in Schattenzonen kurz aufleuchten — ein gruenlicher Reflex, wie Katzenaugen im Dunkeln. Nichts davon ist auf den ersten Blick sichtbar. Man muss wissen, worauf man achtet.

In der Umgebung: Fast unsichtbar. Kerzen flackern etwas laenger, bevor sie erloeschen. Schatten fallen in leicht falsche Richtungen. An verseuchten Orten: ein feiner violetter Dunst ueber dem Boden, Pflanzen, deren Blaetter sich einrollen. Der Spieler bemerkt es vielleicht nicht bewusst — aber die Atmosphaere aendert sich.

**Risse: Infektionswert 41–75**

Am Koerper: Sichtbar. Die Hautstruktur veraendert sich — nicht ueberall, aber an exponierten Stellen. Die Adern treten hervor und pulsieren in einem eigenen Rhythmus, der nicht zum Herzschlag passt. An den Haenden, am Hals, im Gesicht erscheinen asymmetrische Muster: Verdickungen, Verfaerbungen, Strukturen, die an Narben erinnern, aber wachsen. Schatten um den Betroffenen verhalten sich FALSCH — sie sind zu lang, zu dunkel, zu beweglich.

In der Umgebung: Unuebersehbar. Schattenfieber-Zonen haben eine klare visuelle Grenze: eine Linie, an der die Farben entsaettigen, das Licht kippelt, die Flora mutiert. Innerhalb der Zone: Baeume mit Wucherungen, Steine, die schwitzen, Gras, das in giftgruenen Adern leuchtet. Die Luft ist dichter. Partikel schweben, die kein Staub sind.

**Schwelle: Infektionswert 76–100**

Am Koerper: Erschreckend. Die Koerpergrenze des Betroffenen wird uneindeutig. Gewebe dehnt sich ueber die natuerliche Silhouette hinaus — Fasern, Ranken, dünne Stege aus organischem Material, die den Koerper mit der Umgebung zu verbinden scheinen. Bei Kontakt loesen sie sich auf, wachsen aber nach. Die Haut ist stellenweise transluzent — darunter leuchtet es schwach giftgruen. Die Augen sind vollstaendig veraendert: keine menschliche Iris mehr, sondern ein gleichmaessiges Leuchten.

In der Umgebung: Totalbefall. Die Grenze zwischen "gesund" und "befallen" existiert nicht mehr in diesen Zonen. Die gesamte Umgebung ist transformiert: Gebaeude, die von organischem Material ueberwuchert sind, Boeden, die nachgeben wie Haut, Lichtquellen, die in Violett-Schwarz und Giftgruen pulsieren. Die Luft zittert. Die Physik scheint FALSCH — Wasser fliesst in die falsche Richtung, Schatten bewegen sich eigenstaendig, die Schwerkraft hat Aussetzer. Die Hauten zwischen den Daseinsebenen sind hier duenn, und man sieht es.

### 7.3 Designregeln fuer Schattenfieber

**Regel 1: Schattenfieber ist KEIN Biotech.** Biotech ist kontrolliert, funktional, gewollt. Schattenfieber ist unkontrolliert, parasitaer, kosmologisch. Obwohl beide aus dem Emer-Material stammen, muessen sie visuell klar unterscheidbar sein. Biotech hat warme, natuerliche Toene (Amber, Cyan, Elfenbein). Schattenfieber hat kalte, unnatuerliche Toene (Violett-Schwarz, Giftgruen). Biotech pulsiert gleichmaessig. Schattenfieber zuckt, flackert, stoesst.

**Regel 2: Schattenfieber ist NIE schoen.** Biotech darf aesthetisch ansprechend sein — die Ambivalenz liegt in der Funktion, nicht in der Form. Schattenfieber dagegen darf nie schoen aussehen. Es kann FASZINIEREND sein, es kann IMPOSANT sein, aber nie in einer Weise, die der Spieler als angenehm empfindet. Das visuelle Unbehagen ist die Hauptfunktion.

**Regel 3: Schattenfieber bricht Regeln.** Die visuellen Regeln, die fuer den Rest der Welt gelten — Farbpaletten, Lichtlogik, Physik —, gelten in Schattenfieber-Zonen nicht. Das ist die staerkste visuelle Aussage: hier endet die Ordnung. Die Flechtung versagt. Die Hauten werden duenn. Das Galt — der Urzustand VOR aller Differenzierung — scheint durch.

---

## 8. Environments & Architektur

### 8.1 Leitprinzip: Der Mittelgrund als lebender Koerper

Die bewohnte Welt — der Mittelgrund — ist kein unbelebter Schauplatz. Sie ist der verwandelte Koerper des Emer, und die Bewohner haben sich darauf eingerichtet, AUF und IN einem Organismus zu leben. Das Environment Design spiegelt das wider: Landschaften, die subtil organisch wirken. Felsen, deren Maserung an Muskelgewebe erinnert. Fluesse, deren Verlauf sich ueber Jahrzehnte leicht veraendert — wie Adern, die sich verlagern. Hoehlen, die wie Organe geformt sind.

Diese organischen Untertoene sollen nie offensichtlich sein. Der Mittelgrund sieht auf den ersten Blick aus wie eine mitteleuropaeische Landschaft: dichte Waelder, sanfte Huegel, neblige Taeler, schroffe Gebirge. Erst auf den zweiten Blick — oder mit Schattensinnen — werden die Emer-Strukturen sichtbar: die Textur im Fels, das Muster im Boden, der Puls im Wasser.

### 8.2 Vertikalitaet als Designprinzip

Jede besiedelte Zone in RELICS nutzt die vertikale Achse. Staedte sind dreidimensionale Raeume: begehbare Dachlandschaften, Kellergewoeloebe, Kanalisation, Bruecken zwischen Gebaeuden, Tuerme, Aufzuege (organisch — Kapseln, die an Sehnen hoch- und runtergezogen werden). Der Spieler soll immer drei Optionen haben: oben, unten, durch.

Vertikalitaet ist auch ein Statussignal. In Krone-Staedten wohnen die Maechtigen OBEN — in den Tueremen und Soeollern, nahe am Himmel, nahe an Sigvalts Hoehe. In Gilden-Staedten wohnen die Maechtigen auf der ERDE — nah am Markt, nah am Tharm. In Ordensstaedten wohnen die Maechtigen UNTEN — in den Gewoeloeben, den Archiven, den geheimen Laboratorien.

### 8.3 Regionstypen

**Krone-Stadt: Verfallende Pracht.**
Enge, vertikale Gassen unter riesigen gotischen Boegen. Palastbezirke mit Fassaden, die einmal weiss waren und jetzt von Rissen und Biotech-Durchbruechen gezeichnet sind. Hohe Tuerme mit biolumineszenten Kronleuchtern, die nachts die Stadt in warmes Karmin-Gold tauchen. Statuen von Sigvalt an jeder Kreuzung — einhaendig, verwittert, von niemandem missachtet. Die Strassen sind gepflastert, aber die Fugen leuchten schwach: die Adern unter der Stadt sind hier nah an der Oberflaeche. Vorhallen, in denen Wandteppiche haengen, die sich langsam bewegen — weil das Material lebt.

**Gilden-Stadt: Industrielle Monumentalitaet.**
Breite Strassen, offene Marktplaetze, kathedralenhafte Gildenhallen mit sichtbaren Deckenrippen. Die Gebaeude atmen — woertlich. Waende, die sich leicht ausdehnen und zusammenziehen. Boeden mit Kapillarnetzwerken. Membranfenster, die sich bei Regen verdichten. Karawanenhoefe, in denen Tiervolk-Haendler ihre Waren auslegen. Kontore mit Chitin-Schreibpulten und Membran-Dokumenten. Fabrikgebaeude, in denen Biotech-Material gezuechtet wird — riesige Hallen, warm, feucht, pulsierend. Die Gilden-Stadt riecht nach Leben.

**Ordens-Stadt: Geometrische Perfektion.**
Von aussen die schoenste Siedlung des Mittelgrunds. Weisse Mauern, perfekte Proportionen, Kreuzgaenge mit sanftem Lichteinfall. Schulen, Hospitaeler, Bibliotheken — alles offen, alles einladend. Halvards Raben als Steinrelief an den Gebaeuden. Klostergaerten mit medizonischen Kraeuetern. Die Strassen sind breit und sauber. Kein Verfall, kein Dreck, keine Unordnung. Und unter der Oberflaeche: Nervenstrang-Korridore, Ueberwachungsorgane, Labore. Der Spieler, der tief genug in den Orden vordringt, erlebt den Moment, in dem der weisse Kalkstein aufhoert und das pulsierende Gewebe beginnt.

**Wildnis: Mitteleuropa mit Emer-Unterton.**
Dichte Waelder, neblige Taeler, schroffe Gebirge, Moorlandschaften. Auf den ersten Blick realistisch, auf den zweiten Blick subtil fremd: Felsen mit Muskelmaserung, Baeume, deren Rinde an Haut erinnert, Quellen, die in einem Rhythmus sprudeln. Ruinen vergangener Epochen, ueberwachsen und halb verdaut von der Landschaft — das Land nimmt zurueck, was auf ihm gebaut wurde. Einzelhoefe, Einsiedler, verlassene Wachposten. Die Wildnis ist schoeen und still und nicht sicher.

**Uebergangszonen: Neutrale Raeume.**
Maerkte, Karawanenwege, Grenzgebiete. Hier treffen die Fraktionen aufeinander, und die visuelle Sprache ist bewusst neutral: Erdtoene, keine Fraktionsfarben, einfache Architektur ohne Biotech-Praegung. Tiervolk-Praesenz ist hier am staerksten — ihre eklektische Kleidung und ihre fremden Koerper setzen sich gegen die neutrale Umgebung deutlich ab.

**Schattenfieber-Zonen: Die Entflechtung.**
Gebiete, in denen die Hauten duenn geworden sind. Die visuelle Transformation ist total: Farben entsaettigen und kippen in Violett-Schwarz, Giftgruen leuchtet in den Adern der Landschaft, Flora und Fauna sind mutiert. Die Physik verhaelt sich falsch. Licht bricht anders. Wasser fliesst aufwaerts. Schatten haben eigene Konturen. Diese Zonen sind die visuell intensivsten Orte in RELICS — und die gefaehrlichsten. Ihre Grenzen sind scharf: ein Schritt trennt die geordnete Welt vom Chaos. Die Hauten sind hier so duenn, dass das Stillfeld (oder das Hohlicht) durchscheint.

### 8.4 Beleuchtung

Beleuchtung in RELICS folgt zwei Logiken — natuerlich und kuenstlich — und einer Ausnahme.

**Natuerliches Licht:** Diffus, oft bedeckt, selten warm. Der Mittelgrund liegt in einer klimatischen Zone, die an Mitteleuropa erinnert: haeufig bewoelkt, haeufig neblig, selten strahlend. Die goldene Stunde (kurz vor Sonnenuntergang) ist ein seltener, wertvoller Moment — wenn sie eintritt, wird sie zum visuellen Geschenk. Concept Artists sollen die meisten Szenen in diffusem, kuuehlem Licht gestalten und die goldene Stunde sparsam einsetzen.

**Kuenstliches Licht:** Ausschliesslich Biolumineszenz. Keine Fackeln, keine Kerzen, keine Oellampen. Lichtorgane — gezuechtete biologische Leuchtkoerper — sind die einzige kuenstliche Lichtquelle. Ihre Farbtemperatur ist fraktionsabhaengig:
- Krone: Warm, goldgelb, pulsierend — wie Kerzenlicht, aber lebendiger (`#C5A030`)
- Gilden: Neutral bis kuehl, funktional, gleichmaessig — Arbeitslicht, das nie blendet (`#C49A20` bis `#2EC4B6`)
- Orden: Kuehl, weiss, gleichmaessig — Kliniklicht, das keine Schatten laesst (`#E8E4DE`)

**Die Ausnahme — Schattenfieber-Licht:** In Schattenfieber-Zonen verhaelt sich Licht physikalisch falsch. Schatten fallen in die falsche Richtung. Lichtquellen leuchten, ohne zu beleuchten. Farben kippen ins Violett-Schwarz. Giftgruene Adern leuchten von innen — sie brauchen keine Lichtquelle, sie SIND eine. Das Schattenfieber-Licht ist die Abwesenheit jeder visuellen Ordnung.

### 8.5 Gameplay-Orte: Fraktionsvarianten (V2 neu)

Bestimmte Gameplay-Orte kommen in allen drei Fraktionen vor — Alchemie-Station, Trainer, Haendler. Jede Fraktion interpretiert diese Orte anders. Die Fraktionsvariante ist visuell sofort lesbar.

**Alchemie-Station**

Alchemie ist in RELICS Biologie: Substanzen aus Emer-Material, destilliert, konzentriert, kombiniert. Jede Fraktion betreibt Alchemie, aber mit anderen Mitteln und anderen Zwecken.

| Fraktion | Visueller Charakter | Lage | Signalelemente |
|----------|---------------------|------|----------------|
| Krone | Privates Laboratorium hinter verhaengten Tueren. Elegantes Geraet aus Altgold und dunklem Glas. Die Gefaesse sind organisch geformt, die Fluessigkeiten pulsieren schwach in Karmin. Keine Beschriftung — Krone-Alchemie ist Geheimwissen. | Hinterraeume von Palaeesten, unter Kapellen | Altgold-Geraet, Karmin-Fluessigkeiten, verschlossene Gefaesse, kein Licht von aussen |
| Gilden | Oeffentliche Werkstatt. Alles sichtbar, alles beschriftet, alles zugaenglich (gegen Geld). Breite Arbeitsflaechen aus Chitin, grosse Membran-Behaelter, Amber-Biolumineszenz ueber den Stationen. Die Zutatenliste haengt an der Wand. | Erdgeschoss von Gildenhaeusern, Marktebene | Amber-Licht, offene Regale, Membran-Behaelter, Preisliste sichtbar |
| Orden | Scheinbar ein Krankenhaus-Vorbereitungsraum: weiss, steril, geordnet. Was wirklich passiert, ist nicht sofort erkennbar. Die Substanzen sind farblos. Die Geraete sehen wie medizinische Instrumente aus. Bernstein-Glow kommt aus Behaeltern, die verschlossen und etikettiert sind — mit Codes, nicht mit Namen. | Ordenshospitaeler, Innenbereiche | Kalkweiss, verschlossene Codes-Etiketten, Bernstein-Glow hinter Glas, keine sichtbaren Pflanzen |

**Trainer**

Trainer lehren Kampffaehigkeiten und koerperliche Techniken (GDD-02, Kap. 3.3). Jede Fraktion hat exklusive Trainer fuer bestimmte Waffenstile und Fertigkeiten. Optisch ist sofort erkennbar, welche Faehigkeiten hier gelehrt werden.

| Fraktion | Visueller Charakter | Lage | Signalelemente |
|----------|---------------------|------|----------------|
| Krone | Zeremonieller Uebungshof oder Fechtsaal. Hohe Decken, Holzdielen, einhaendige Statuen als stille Zuschauer. Krone-Trainer lehren Schwertkampf, Paraden, zeremonielle Kampfkunst. Kleidung: formal, Karmin-Akzente, keine sichtbare Ruestung — Haltung ist Ruestung. | Innenhoefen von Palaeesten und Adelsgebaeuden, obere Stadtebene | Einhaendige Statuen, Karmin-Wandverkleidung, Schwerttrophaaen, kein Biotech sichtbar |
| Gilden | Kaempfarena oder Soeldnerquartier. Pragmatisch, dreckig, effektiv. Stroe auf dem Boden, Chitin-Dummies, Waffenregale mit allem, was Funktion hat. Gilden-Trainer lehren Dolchkampf, Bogenarbeit, Guerilla-Taktiken. Kleidung: Arbeitskleidung mit organischen Verstarkungen. | Karawanenhoefe, Soeldnerunterkuenfte, Untergeschoss von Gildenhallen | Chitin-Trainingsgeraete, offene Waffenregale, Amber-Licht, sichtbare Kampfspuren |
| Orden | Meditativer Uebungsraum. Kalkweiss, minimale Einrichtung, symmetrisch. Orden-Trainer lehren Koerperkontrolle, Schmerzunterdrueckung, Konzentrationsarbeit — aber auch fortgeschrittene Kampftechniken, die nach aussen wie Heilkunde aussehen. | Innenbereiche von Ordensgebaeuden, untere Ebenen | Kalkweiss, keine Dekoration, geometrische Uebungsmarkierungen am Boden, Schieferblau-Roben des Trainers |

**Haendler**

Haendler verkaufen Waren, Informationen, Zugang. Tiervolk-Haendler sind die mobilen Generalisten. Fraktionshaendler spezialisieren sich auf ihre eigenen Produkte. Optisch klar unterscheidbar.

| Haendler-Typ | Visueller Charakter | Lage | Signalelemente |
|--------------|---------------------|------|----------------|
| Krone-Haendler | Privates Kontor mit schweren Vorhaengen. Nicht alles ist ausgestellt — die wertvollsten Waren sind hinter dem Ladentisch. Karmin-Textilien, Altgold-Preisschilder, Biolumineszenz als Beleuchtung. Haltung des Haendlers: erwartet Respekt. | Palastbezirke, Adelsmarkte | Verhang vor dem Eingang, Altgold-Schilder, versteckte Ware, koerpersprachlich kuehl |
| Gilden-Haendler | Oeffentlicher Stand oder grosses Kontor. Ware ist ausgestellt, Preise sind sichtbar, Verhandlung ist erwuenscht. Amber-Beleuchtung, Chitin-Theke, Membran-Verpackungen. Haltung des Haendlers: pragmatisch, laut, direkt. | Marktplaetze, Karawanenhoefe, Erdgeschoss | Offene Auslagen, sichtbare Preisliste, Amber-Licht, laute Umgebung |
| Orden-Haendler | Kein klassischer Handel — der Orden verkauft nicht, er verteilt. Zutritt nur bei Beziehungsstatus. Kalkweiss-Raum, geordnete Regale, alles etikettiert. Was der Orden gibt, kostet Information oder Loyalitaet, kein Geld. | Ordenshospitaeler, Bibliotheken | Kalkweiss, keine Preisschilder, Haendler in Ordensroben, erwartet Gegenleistung in Form von Information |
| Tiervolk-Haendler | Mobiler Stand, eklektische Ware aus allen Fraktionen. Ocker-Terrakotta-Tuecher als Auslageflaecheche, Knochen-Schmuck als Dekoration, Biotech-Fragmente als Raritaeten. Haltung des Haendlers: freundlich, beobachtend, immer bereit abzuhauen. | Uebergangszonen, Marktplaetze, Stadtgrenzen | Ocker-Erdtoene, gemischte Ware, mobiles Setup (kein fester Stand), Tiervolk-Proportionen |

---

## 9. Offene Punkte & Abhaengigkeiten

| Thema | Brauche von | Prioritaet | Status |
|-------|-------------|------------|--------|
| Architektur-Logik pro Region (Detail) | Emre (WBB-02 Topos) | Hoch | Ausstehend — Outline liegt vor, Volltext fehlt |
| Ruestungsklassen & Kampf-Visuals | Leo + Darius (GDD-02) | Hoch | Ausstehend — Waffenklassen stehen, Ruestung offen |
| Schluesselcharakter-Designs | Nami (GDD-04) | Mittel | Ausstehend — Outline liegt vor, Volltext fehlt |
| Schattenfieber-Gameplay-Kosten (visuell) | Darius (GDD-02) | Mittel | Teilweise — Stufen-Mapping liegt vor und abgestimmt |
| Nervensystem-UI-Visualisierung | Darius (GDD-02) | Mittel | Ausstehend — Wireframe in V3 |
| Technische Constraints (Engine, LOD, Shader) | Tobi (GDD-06) | Niedrig | V2 von Tobi mit 60 Modulen und Drei-Schichten-Rendering — Abstimmung laeuft |
| Kontrollverlust-Episoden visuell | Darius + Tobi | Niedrig | Erst ab V3 |

---

## 10. Naechste Schritte (V3)

- [ ] V3: Thumbnail-Skizzen fuer jede Fraktion (Architektur + Mode + Biotech)
- [ ] V3: Lebende Krone Concept Art (Referenzskizze + Transformationsstufen)
- [ ] V3: Schattenfieber-Stufenvisualisierung (Concept Sheet: vier Zustaende am selben Charakter — Stufe 0, Rauschen, Risse, Schwelle)
- [ ] V3: Wireframe fuer Nervensystem-UI (bilateral mit Darius)
- [ ] V3: Architektur-Detaillierung mit WBB-02 Topos (sobald Emre Volltext liefert)
- [ ] V3: Ruestungsklassen-Differenzierung (sobald Leo/Darius liefern)
- [ ] V3: Tiervolk-Charakterstudien (3 Typen: Haendler, Diebin, Aeltester)

---

> **Vera Kowalski, Art Station, Tag 5 Vormittag — V2 fertig. Alle Stufengrenzen korrekt. Stufe-0-Baseline drin. Gameplay-Orte: drei Fraktionen, drei Ortstypen. Dominanzprinzip steht. Hex-Codes ACES-validiert. Das ist sauber.**

\clearpage

# GDD-06 — Technische Spezifikation & Produktion

**Projekt:** RELICS
**Autoren:** Tobi Richter (Technik), Finn (Produktion)
**Version:** V2
**Stand:** Tag 5, Freitag — Produktionsphase
**Status:** Finalisiert. CD-Stufengrenzen eingearbeitet. Shader-Architektur spezifiziert. Hex-Codes aus GDD-05 1:1 übernommen.
**Aenderungslog:**
- V0.1 (Tag 2): Outline mit Kapitelstruktur und Kerntabellen
- V1 (Tag 3): Volltext, Budget-Aufschluesselung, Schattenfieber-Tech auf fuenf Stufen erweitert, Abstimmung mit GDD-02 (Darius) und GDD-01 (Design-Saeulen)
- V2 (Tag 5): Hex-Codes 1:1 aus GDD-05 eingetragen. Kap. 1.4 neu (Organische Shader-Architektur: Hauten-Shader, SSS, WPO, Nanite-Ausnahmen). Kap. 5.1 erweitert (Drei-Schichten-Rendering: Mittelgrund/Hohlicht/Stillfeld). Stufengrenzen auf CD-Lock korrigiert (Rauschen 1-40, Risse 41-75, Schwelle 76-100). Halluzinations-Interpolationsformel korrigiert (Start 76, nicht 70). Kap. 8.2 um Anforderungsprofil Gameplay-Programmer ergänzt (GAS als Pflicht-Kriterium).

---

## 1. Engine & Rendering

### 1.1 Engine-Wahl

RELICS wird in **Unreal Engine 5.4+** entwickelt (bestaetigt Tag 1, Szene 3). Die Engine-Entscheidung basiert auf drei Faktoren: Nanite und Lumen liefern die Rendering-Qualitaet, die der Dark-Fantasy-Look erfordert, ohne dass wir eine eigene Render-Pipeline bauen muessen. Das Gameplay Ability System (GAS) ist die einzige Engine-native Loesung, die Darius' dreischichtiges Combat-System (GDD-02, Kap. 1.2) ohne Drittanbieter-Middleware abbilden kann. Und die Marketplace-Infrastruktur ist fuer ein kleines Team wie unseres ein realer Produktionsfaktor — nicht als Ersatz fuer eigene Assets, sondern als Basis zum Anpassen.

**Zielplattform:** PC first (Windows). Konsolen sind ein Stretch Goal, das fruehestens nach dem Vertical Slice evaluiert wird. Die Entscheidung fuer PC first ist keine Einschraenkung, sondern eine bewusste Scope-Steuerung: Konsolen-Portierung erfordert Anpassungen an Controller-UI, Performance-Optimierung fuer fixe Hardware und Zertifizierungsprozesse, die unser aktuelles Team nicht stemmen kann.

**Singleplayer.** Kein Multiplayer-Backend, kein Koop, keine Online-Features. Das vereinfacht die Architektur erheblich und eliminiert eine ganze Kategorie technischer Risiken.

### 1.2 Rendering-Architektur

#### Nanite (Virtualisierte Geometrie)

Nanite ist das primaere Geometrie-System fuer alle statischen Hard-Surface-Meshes: Architektur, Props, Waffen, Terrain-Deko, Felsen. Die Kernidee: Kuenstler muessen keine manuellen LOD-Ketten mehr bauen. Nanite uebernimmt die geometrische Vereinfachung zur Laufzeit, was besonders bei modularen Architektur-Kits (Kap. 4.1) die Produktionsgeschwindigkeit drastisch erhoeht.

Einschraenkungen, die den Workflow betreffen:
- **Skeletal Meshes** (Charaktere, Kreaturen, NPCs) unterstuetzen kein Nanite. Hier verwenden wir klassische LOD-Ketten mit drei Stufen (High, Mid, Low). Vera modelliert High-Poly, die LODs werden semi-automatisch generiert (Simplygon oder UE5-internes Proxy-System).
- **Vegetation** ist ein Hybrid: Baumstaemme und grosse Gehoelze als Nanite-Meshes, Blaetter und Gras als traditionelle Alpha-Karten mit Dithering. Der Grund: Nanite kann keine Alpha-Masken verarbeiten, und Wind-Animation (World Position Offset) funktioniert nur mit traditionellen Meshes.
- **Vertex-Animation** ist ueber Nanite eingeschraenkt moeglich (s. Kap. 1.4 fuer Regelwerk). Starke WPO-Deformationen (Schattenfieber Stufe 3-4) muessen als traditionelle Meshes gebaut werden.

#### Lumen (Globale Beleuchtung)

Lumen ist das primaere GI-System. Wir verwenden keine gebackenen Lightmaps. Das ist eine fundamentale Entscheidung: In einer Welt, die auf Environmental Storytelling setzt (GDD-01, Saeule P4), muss Licht dynamisch auf Spieleraktionen reagieren koennen — eine Fackel geht aus, ein Feuer wird entzuendet, die Tageszeit wechselt. Gebackene Beleuchtung kann das nicht.

**Shipping-Konfiguration:** Hardware Ray Tracing (HW RT Lumen). Das liefert die beste Qualitaet bei Innenraeumen (die fuer RELICS' gotische Architektur zentral sind) und haelt die visuellen Artefakte minimal, die Software Lumen in engen Raeumen mit vielen Lichtquellen produziert.

**Fallback:** Software Lumen fuer Hardware ohne RT-Unterstuetzung (Minimum-Tier, siehe Kap. 6). Die visuellen Unterschiede sind akzeptabel, solange wir Innenraeume nicht auf mehr als 4-5 Bouncen angewiesen machen.

**Referenz-Look:** Control (Remedy) fuer Innenraeume — praezise Lichtfuehrung, dramatische Schatten, praktische Lichtquellen als Gestaltungselement. Alan Wake 2 fuer Aussenraeume — natuerliches Licht, atmosphaerische Streuung, keine ueberbelichteten Himmel.

#### Virtual Shadow Maps (VSM)

Standard bei Lumen-Projekten. VSM liefert hochaufloesende Schatten ohne die Artefakte klassischer Cascaded Shadow Maps. Das Budget: maximal 8-12 dynamische Lichtquellen gleichzeitig pro Szene. Das klingt nach wenig, ist aber ausreichend, wenn wir konsequent mit praktischen Lichtquellen arbeiten (Biolumineszenz-Organe, Feuer, Laternen) und globale Beleuchtung den Rest uebernimmt.

Risiko: VSM hat in UE 5.3/5.4 noch Performance-Spitzen bei vielen ueberlappenden Schatten. Epic verbessert das kontinuierlich, aber wir muessen in der Prototyping-Phase Worst-Case-Szenen testen (z.B. Marktplatz mit 12 Lichtorganen).

#### Farb-Pipeline

Die Farb-Pipeline ist eine der Entscheidungen, die unsichtbar ist, wenn sie funktioniert, und katastrophal, wenn sie es nicht tut. RELICS verwendet **ACES (Academy Color Encoding System)** als Arbeitsfarbraum ueber die gesamte Tool-Chain: Substance Designer/Painter, Houdini, Unreal Engine 5. Das stellt sicher, dass Farben konsistent bleiben, egal welches Tool sie erzeugt hat.

Warum ACES und nicht sRGB? Weil RELICS eine duester-farbige Palette braucht (Briefing: "Duester, aber farbig. Kein Entsaettigungs-Klischee.") und sRGB im Low-Key-Bereich Farbinformationen verliert. ACES hat einen groesseren dynamischen Umfang und bewahrt Farbnuancen in den Schatten — genau dort, wo unser Spiel lebt.

**Tone Mapping:** ACES als Standard-Tone-Mapper in UE5, mit der Option auf eine Custom LUT, wenn der generische ACES-Look zu "filmlastig" wirkt. Evaluation im Prototyp.

**Deakins-Prinzip (intern):** Roger Deakins arbeitet mit reduzierter Beleuchtung, aber nie mit entsaettigten Farben. Ein dunkler Raum ist nicht grau — er ist tiefblau, warm-orange am Rand, mit Farbtemperatur-Kontrast. Dieses Prinzip gilt fuer jeden beleuchteten Raum in RELICS.

### 1.3 Post-Processing Stack

Der Post-Processing Stack ist bewusst zurueckhaltend. Jeder Effekt muss einen narrativen oder gameplay-relevanten Grund haben. "Sieht cool aus" ist kein Grund.

| Effekt | Einstellung | Begruendung |
|--------|-------------|-------------|
| Color Grading | Gedaempfte Palette, fraktionsspezifisch | Krone: warme Verrottung (`#C5A030`/`#8B1A2B`). Gilden: kuehle Praezision (`#2EC4B6`/`#C49A20`). Orden: entsaettigt-kuehle Monochromie (`#E8E4DE`/`#4A5568`) |
| Vignette | Subtil (0.3-0.4) | Fokussiert den Blick, verstaerkt Tunneleffekt in engen Raeumen |
| Depth of Field | Cinematisch in Dialogen (f/2.8-Simulation), minimal im Gameplay | Dialog-Kamera braucht Bokeh fuer Portraitqualitaet. Im Gameplay wuerde DOF die Lesbarkeit stoeren |
| Bloom | Nur praktische Lichtquellen | Biolumineszenz-Organe, Feuer. Kein Lens-Flare. Kein Glow auf Materialien ohne Emissionsgrund |
| Motion Blur | Per-Object (Waffen-Swings, Feindangriffe) | Verstaerkt das Gewicht von Kampfaktionen. Kein Camera Motion Blur — das erzeugt Uebelkeit und stoert die Lesbarkeit |
| Film Grain | Optional (Spielereinstellung) | Manche Spieler moegen den filmischen Look, andere nicht. Keine Default-Aktivierung |
| Chromatische Aberration | Nur Schattenfieber (Kap. 5) | Kein genereller CA-Effekt. Ausschliesslich als Infektionsindikator |

### 1.4 Organische Shader-Architektur (NEU V2)

RELICS' Kern-Aesthetik ist organische Gotik (GDD-05, Kap. 1.1): Alles lebt, atmet, pulsiert. Das hat direkte Konsequenzen fuer die Shader-Architektur. Dieser Abschnitt definiert die technischen Regeln fuer organische Oberflaechen — Hauten, Membranen, Biotech-Gewebe — und grenzt ab, wo Nanite endet und traditionelle Meshes beginnen.

#### Hauten-Shader (Subsurface Scattering)

Organische Oberflaechen in RELICS benoetigen **Subsurface Scattering (SSS)**, um das Gefuehl von lebendigem Gewebe zu erzeugen: Licht dringt in die Oberflaeche ein und tritt an benachbarten Stellen wieder aus (wie Licht durch eine Hand). Das ist der visuelle Unterschied zwischen "Stein, der wie Haut aussieht" und "Haut".

**Shading Model:** `Subsurface Profile` (nicht das Legacy-`Subsurface`-Modell). Subsurface Profile implementiert Burley-SSS, das seit UE5.3 physikalisch korrekt ist und Wrap-Around-Beleuchtung liefert. Das ist fuer Biotech-Gewebe und Charakterhaut die einzige akzeptable Loesung.

**Performance-Budget:** Subsurface Profile ist Screen-Space und kostet ~0.3-0.5 ms pro Screen-Fill auf empfohlener Hardware. Das muss im Gesamtbudget eingerechnet werden. Massnahme: SSS nur dort einsetzen, wo es visuell notwendig ist. Nicht jede Steinwand braucht SSS — nur organische Elemente im Vordergrund.

**Asset-Kategorien mit SSS:**
- Spielercharakter (Haut, Hautpartien unter Ruestung)
- NPCs mit Gesichts-Nahaufnahmen (Dialog-Kamera)
- Biotech-Gewebe-Elemente (Membranen, Adern, Nervenknoten) — wenn Nahsicht-relevant
- Lebende Krone (GDD-05, Kap. 1.3): Transluzente Stellen mit SSS, opake Stellen ohne

**Asset-Kategorien OHNE SSS:**
- Hintergrund-Architektur (zu weit weg, nicht wahrnehmbar)
- Props und Geraetschaften (nicht organisch)
- Terrain (eigenes Material-System, kein SSS)

#### World Position Offset (WPO) — Regelwerk

WPO ermoeglicht Vertex-Displacement im Shader: atmende Waende, pulsierende Adern, schwankende Biotech-Elemente. Es ist das technische Fundament des "lebenden" Looks.

**Nanite + WPO:** Seit UE5.1 unterstuetzt Nanite WPO grundsaetzlich, aber mit Einschraenkungen. Nanite+WPO ist vertretbar fuer kleine Puls-Animationen (Displacement unter 5% der Mesh-Groesse). Fuer groessere Deformationen — insbesondere Schattenfieber Stufe 3-4 — nicht geeignet.

**Nanite-Ausnahmen-Katalog:**

| Asset-Typ | Nanite | WPO | Begruendung |
|-----------|--------|-----|-------------|
| Architektur (statisch, kein Biotech) | Ja | Nein | Reines Nanite, hoechste Performance |
| Architektur mit kleinen Biotech-Adern | Ja | Ja (klein) | Nanite+WPO, Displacement < 5% |
| Pulsierende Membran-Elemente | Nein | Ja | Traditionelles Mesh, staerkere Puls-Animation |
| Schattenfieber-Vegetation | Nein | Ja | Traditionelles Mesh, starke WPO-Deformation |
| Schattenfieber-Geometrie Stufe 3-4 | Nein | Ja | Traditionelles Mesh, atmende Waende, Barrel-Distortion |
| Baum-Staemme (Grossgehoelze) | Ja | Nein | Nanite, Wind ueber PCG-Instancing |
| Baum-Blaetter / Gras | Nein | Ja | Traditionell + Alpha-Karte, Wind-WPO |
| Charaktere / NPCs / Kreaturen | Nein | Nein | Skeletal Mesh, kein Nanite |
| Lebende Krone | Nein | Ja | Eigenes Material, SSS + WPO, langsame Bewegung |

**WPO-Performance-Budget:** 0.2 ms GPU bei maximaler WPO-Last (alle sichtbaren organischen Elemente aktiv). WPO-Intensitaet skaliert mit LOD-Distanz: unter 10m voll, 10-30m halbe Intensitaet, ueber 30m deaktiviert.

---

## 2. Kamerasystem

### 2.1 Architektur

Das Kamerasystem basiert auf UE5s **Spring Arm Component**. Die Entscheidung fuer Spring Arm (statt eines vollstaendig custom Kamerasystems) ist pragmatisch: Spring Arm loest Wandkollision, Lagging und Distanz-Management out of the box. Custom-Erweiterungen koennen darueber gebaut werden, ohne die Basis neu zu erfinden.

**Third Person ist der Primaermodus** (bestaetigt Tag 1). Der Spielercharakter ist sichtbar, customizable Ruestung und Kleidung sind ein visuelles Belohnungssystem (Briefing). Ein reiner First-Person-Modus wuerde den Animationsaufwand verdoppeln (Arm-Rigs, FP-Waffen-Meshes, separate Animationssets) und ist daher als V2/DLC-Stretch-Goal klassifiziert.

**Architektonische Vorbereitung fuer FP:** Die Spring-Arm-Architektur erlaubt einen Arm-Length-Wert von 0, was mathematisch einem FP-Modus entspricht. Wir bauen keine FP-Features, aber wir verbauen auch nichts, was FP spaeter unmoeglich machen wuerde. Kein Gameplay-Code darf die Existenz eines sichtbaren Spielercharakters voraussetzen.

**Zoom:** Stufenlos via Mausrad (PC) oder rechtem Stick (Controller). Der Zoom interpoliert zwischen den Kontext-Modi-Parametern, nicht nur die Arm-Distanz.

### 2.2 Kontext-Modi

Das Kamerasystem wechselt kontextabhaengig zwischen vier Modi. Der Wechsel ist kein harter Cut, sondern ein parametrischer Blend ueber die angegebene Dauer.

| Modus | Arm Length | FOV | Offset | Blend-Dauer | Ausloeser |
|-------|-----------|-----|--------|-------------|-----------|
| Exploration | 350 cm | 78 deg | Leicht rechts (+30 cm) | Standard | Default-Modus, aktiv bei freier Bewegung |
| Combat | 200 cm | 82 deg | Ueber Schulter (+50 cm, +20 cm hoch) | 0.3 s | Feind im Engagement-Radius oder Waffe gezogen |
| Dialog | 100 cm | 72 deg | Schulterblick, Blick auf NPC-Gesicht | 0.5 s | Dialog-Trigger |
| Inspect | 400 cm | 70 deg | Zentriert (Offset 0) | 0.3 s | Inventar, Karte, Nervensystem-UI |

**Exploration** ist der Ruhezustand. Die leichte Rechts-Verschiebung gibt dem Spieler Sichtfeld links vom Charakter — das ist intuitiver fuer rechtsdominante Spieler und laesst Raum fuer UI-Elemente am linken Rand.

**Combat** zieht die Kamera naeher heran und erhoeht das FOV leicht. Das erzeugt ein Gefuehl von Geschwindigkeit und Enge, ohne die Uebersicht zu verlieren. Die Schulter-Perspektive erlaubt praeziseres Zielen (relevant fuer Bogen/Armbrust).

**Dialog** simuliert einen cinematischen Schulterblick. Die niedrige Arm Length erzeugt Portraitqualitaet. Hier greift der DOF-Effekt (f/2.8-Simulation, siehe Kap. 1.3).

**Inspect** zieht die Kamera zurueck und zentriert, damit der Spieler seinen Charakter und dessen Ausruestung in voller Groesse sieht — wichtig fuer das Nervensystem-Leveling-UI (GDD-02, Kap. 3).

### 2.3 Kollision und Verhalten

- **Sphere Trace** fuer Wandkollision: Die Kamera faehrt naeher an den Charakter heran, statt durch Geometrie zu clippen. Radius: 12 cm (gross genug, um Ecken zu glaetten, klein genug, um nicht auf Moebel zu reagieren).
- **Enge Raeume:** Automatischer Nah-Zoom mit Minimum-Distance von 80 cm. Unter 80 cm wuerde der Charakter die gesamte Sicht blockieren.
- **Vegetation:** Dithering-Fadeout bei Kamera-Naehe (Radius 60 cm um Kameraposition). Keine harte Kollision mit Blaettern und Gras — das wuerde in einem bewaldeten Gebiet staendig die Kamera ruckeln lassen.
- **Camera Lag:** Speed 8-10. Das erzeugt eine geschmeidige Nachfuehrung, die sich organisch anfuehlt, ohne den Charakter "hinter sich herzuziehen".
- **Pitch Range:** -60 bis +70 Grad. Der erweiterte Aufwaerts-Bereich (+70) ist essentiell fuer Dishonored-Vertikalitaet (GDD-01, Saeule P6): Der Spieler muss nach oben schauen koennen, um Kletterwege und Dachlandschaften zu erkennen.

### 2.4 Offene Punkte

- [ ] Kamera-Blueprint V0.1 prototypen — Prio fuer diese Woche. Vier Modi muessen spielbar sein, bevor Combat-Prototyping beginnt
- [ ] FP-Vorbereitung: Smoke-Test mit Arm Length 0 — funktioniert das mit dem aktuellen Charakter-Mesh ohne Clipping-Artefakte?
- [ ] Controller-Konfiguration: Rechter Stick fuer Kamera, linker Trigger fuer Zoom? Abstimmung mit Darius (Combat-Controls)

---

## 3. Combat-Architektur

### 3.1 Grundsystem

Das Combat-System basiert auf dem **Gameplay Ability System (GAS)**, das in UE5 nativ integriert ist. GAS ist die einzige Engine-Loesung, die die Komplexitaet von Darius' dreischichtigem Combat-Design (GDD-02, Kap. 1.2) abbilden kann, ohne auf Drittanbieter-Middleware angewiesen zu sein. Das reduziert das Abhaengigkeitsrisiko, erfordert aber einen Entwickler mit GAS-Erfahrung (s. Anforderungsprofil Kap. 8.2).

**Fundamentale Abhaengigkeit:** Das Combat-System setzt einen **dedizierten Gameplay-Programmer** voraus. Kein Teammitglied hat die C++-Tiefe, um GAS auf Produktionsniveau zu implementieren. Das Freelancer-Budget (Kap. 8.2) ist primaer fuer diese Position reserviert. Ohne diese Person gibt es kein Combat, kein Vertical Slice, kein Spiel.

### 3.2 GAS-Architektur (V1 Scope)

| Komponente | GAS-Element | Implementierung | Prioritaet |
|------------|-------------|-----------------|------------|
| Basis-Attribute | Attribute Set | HP, Stamina, Infektionswert als GAS Attributes. Float-basiert, repliziert (Singleplayer: lokal) | Kern |
| Leichter/Schwerer Angriff | Gameplay Abilities | Ability-Klassen mit Montage-Referenz, Damage-Calculation, Stamina-Kosten | Kern |
| Block / Ausweichen | Gameplay Abilities | State-Machine: Idle > Block > Active. Parry = Frame-Window innerhalb von Block | Kern |
| Hit Detection | Animation Notifies | Notify-basiert: Sweep/Overlap bei definierten Frames. Keine Hitbox-Volumes, sondern Trace-basiert (praeziser, weniger Collider-Overhead) | Kern |
| Stamina-Management | GAS Gameplay Effects | Kosten pro Aktion als Gameplay Effect. Regeneration als Duration-Effect mit Period | Kern |
| Hit Reactions / Stagger | Gameplay Cues + Montages | Gameplay Cues triggern VFX/Sound, Montages uebernehmen die Animations-Reaktion | Kern |
| Schattenfieber-Faehigkeiten | Custom Abilities + MPC | Abilities mit doppeltem Kosten-System (Stamina + Infektionswert-Erhoehung). Post-Processing-Feedback ueber Material Parameter Collection | V1 nach Emre/Darius-Sync |
| Feind-KI | StateTree (UE5-nativ) | Verhaltenslogik in StateTree, Combat-Aktionen als GAS Abilities. Feinde nutzen dasselbe System wie der Spieler | Kern |
| Gameplay Tags | Tag-Hierarchie | `Combat.State.Blocking`, `Combat.State.Staggered`, `Infection.Level.Rauschen` etc. Tags steuern, welche Abilities wann aktivierbar sind | Kern |

**Waffentypen V1-Scope:** Schwert (Einhand) + Bogen. Das ist das Minimum, um die Kern-Combat-Loop zu validieren. Armbrust, Schild, Zweihand-Waffen und Dolche sind V2 (GDD-02, Kap. 1.3 definiert sechs Waffenklassen — wir liefern zwei fuer den Vertical Slice).

### 3.3 Animation

**Motion Matching** (UE 5.4+) ist das Bewegungssystem. Der Vorteil gegenueber klassischen Blend Trees: natuerlichere Uebergaenge zwischen Gehen, Laufen, Stoppen, Richtungswechsel. Das reduziert das "Eislaufen"-Problem, das viele Third-Person-Spiele haben, und unterstuetzt das gewichtige Kampfgefuehl (GDD-01, Saeule P2).

**Animations-Datenbank:** Motion Matching braucht grosse Datensaetze. Die Strategie ist dreistufig:
1. **Prototyping:** Mixamo als Basis. Kostenlos, sofort verfuegbar, ausreichend fuer Gameplay-Iteration
2. **Produktion:** Marketplace-Animation-Packs als Startpunkt. Packs mit gewichtigem Melee-Combat (z.B. "Medieval Combat Animset") als Grundlage, angepasst
3. **Hero-Animations:** Custom oder MoCap fuer Kern-Movesets. Budget-Abhaengig (Kap. 8.2)

**Control Rig:** IK fuer Fussplatzierung (Terrain-Anpassung), Waffenausrichtung (Aim Offset), und Rueckenpanzerung (Socket-basiert). Control Rig ist UE5-nativ und ersetzt die frueheren AnimDynamics-Workarounds.

**Gewichtiges Kampfgefuehl — technische Hebel:**
- **Hitlag:** 2-4 Frames Pause bei Treffer (sowohl Spieler als auch Feind). Erzeugt das Gefuehl von Masse und Impact
- **Camera Shake:** Subtil, richtungsabhaengig. Kein Bildschirm-Schuetteln, sondern ein kurzer Impuls in Angriffsrichtung
- **Zeitlupe:** Optional fuer kritische Treffer (0.2 s bei 0.7x Speed). Muss sich verdient anfuehlen, nicht inflationaer
- **Impact VFX:** Funken, Staub, Blutspuren. Niagara-Partikel, physikbasiert

### 3.4 Risiken und Mitigationen

| Risiko | Schwere | Mitigation | Fallback |
|--------|---------|------------|----------|
| Gameplay-Programmer verzoegert sich | KRITISCH | Suche beginnt sofort (Woche 1). Finn fuehrt Gespraeche | Marketplace-Combat-Framework als Bridge (Risiko: GAS-Inkompatibilitaet) |
| GAS-Lernkurve zu steil | HOCH | Lyra-Projekt (Epic) als Referenz-Implementierung. Iterativer Aufbau, keine Gross-Architektur am Anfang | GAS-Kurs/Beratung einkaufen (500-1000 EUR Budget) |
| Kampf fuehlt sich nicht "gewichtig" an | HOCH | Fruehe Prototyp-Iteration. Game-Feel-Workshop in Woche 6-7: Hitlag, Kamera, Sound als isolierte Variablen testen | Referenz-Videos von Gothic/Dark Souls als Benchmark-Reihe |
| Motion Matching Daten unzureichend | MITTEL | Frueh mit Mixamo-Daten testen. Marketplace-Packs evaluieren (Woche 4) | Fallback auf klassische Blend Trees (funktioniert, sieht schlechter aus) |

---

## 4. Asset-Pipeline

### 4.1 Modulares Kit-System

Die Asset-Strategie fuer RELICS ist modular. Das bedeutet: Wir bauen keine fertigen Gebaeude, sondern einen Baukasten aus ~60 Architektur-Modulen (Wand-Segmente, Ecken, Tuerrahmen, Fenster, Dach-Elemente, Fundamente, Biotech-Elemente, Membran-Einschluesse, organische Strukturen), aus denen sich hunderte Gebaeude-Varianten zusammensetzen lassen.

Dieses Prinzip ist nicht optional, sondern ueberlebensnotwendig: Vera ist die einzige dedizierte Kuenstlerin im Team. Ohne modulares System muessen wir jedes Gebaeude einzeln modellieren. Mit modularem System modelliert Vera die Module, und Level Design baut daraus eine Stadt.

**Fraktions-Differenzierung** erfolgt ueber Material-Instanzen, nicht ueber separate Meshes. Dieselbe Wand bekommt je nach Fraktion ein anderes Material. Hex-Codes 1:1 aus GDD-05 (Vera Kowalski, V1):

| Fraktion | Basis (70%) | Akzent (20%) | Highlight (10%) |
|----------|-------------|--------------|-----------------|
| Krone | `#3D3D3D` Aschgrau | `#8B1A2B` Karmin | `#C5A030` Altgold |
| Gilden | `#7A6E5D` Warmer Beton | `#C49A20` Amber | `#2EC4B6` Cyan |
| Orden | `#E8E4DE` Kalkweiss | `#4A5568` Schieferblau | `#D4A017` Bernstein |

**Globale Akzente (fraktionsunabhaengig):**

| Kontext | Farbe A | Farbe B | Farbe C |
|---------|---------|---------|---------|
| Schattenfieber | `#2D0A31` Violett-Schwarz | `#39FF14` Giftgruen | — |
| Wildnis/Neutral | `#5C6B3C` Moosgruen | `#8B7355` Erdton | `#9E9E9E` Nebel-Grau |
| Tiervolk | `#CC7722` Ocker | `#C04000` Terrakotta | `#C2B280` Sand |

Diese Hex-Codes sind verbindlich fuer alle Material-Instanzen. Jede Abweichung braucht explizite Abstimmung mit Vera (GDD-05) und dem CD.

**Fraktions-Material-Instanzen — Beschreibung:**
- **Krone:** Eleganter Zerfall. Aschgrau-Stein mit Karmin-Biotech-Glow in Rissen, Altgold-Ornamente. Farbreferenz: `#3D3D3D` Basis, `#8B1A2B` Glow, `#C5A030` Metallakzent
- **Gilden:** Industrielle Eleganz. Warmer Beton-Grundton, Amber-Licht auf funktionalen Elementen, Cyan in aktiven Adern. Farbreferenz: `#7A6E5D` Basis, `#C49A20` Licht, `#2EC4B6` Biotech-Fluid
- **Orden:** Monolithisch, doppelte Lesart. Kalkweiss-Fassade mit Schieferblau-Schatten; innen Bernstein fuer verborgenes Biotech. Farbreferenz: `#E8E4DE` Fassade, `#4A5568` Schatten, `#D4A017` Geheimebene

### 4.2 Standards

| Standard | Wert | Begruendung |
|----------|------|-------------|
| Texel Density (Hero) | 10.24 px/cm | Fuer Assets in Nahsicht (Waffen, Ruestungen, Interaktionsobjekte). Entspricht ~1024px auf 1m |
| Texel Density (Background) | 5.12 px/cm | Fuer Hintergrund-Assets (Architektur-Module, Terrain-Deko). Spart VRAM ohne sichtbaren Qualitaetsverlust |
| Naming (Static Mesh) | `SM_[Kat]_[Name]_[Var]` | z.B. `SM_Wall_Stone_01`, `SM_Door_Wood_Gilden_02` |
| Naming (Material Instance) | `MI_[Fraktion]_[Material]` | z.B. `MI_Krone_Stein_Verwittert`, `MI_Gilden_Bronze_Poliert` |
| Naming (Skeletal Mesh) | `SK_[Typ]_[Name]` | z.B. `SK_Char_PlayerMale`, `SK_Creature_Infizierter_01` |
| LOD (Skeletal) | 3 Stufen | LOD0: Voll, LOD1: 50%, LOD2: 25%. Automatisch via Simplygon oder UE5-Proxy |
| LOD (Static/Nanite) | Automatisch | Nanite uebernimmt. Kein manueller LOD-Workflow noetig |
| Textur-Format | BC7 (Farbe), BC5 (Normal) | Standard-Kompression fuer UE5. BC7 hat bessere Qualitaet als DXT5 bei gleicher Groesse |
| Max. Texturgroesse | 4096x4096 (Hero), 2048x2048 (Standard) | 4K nur fuer Hero-Assets. Alles andere 2K |

### 4.3 Prozedurale Systeme

#### Houdini-Terrain

Houdini ist das Kern-Tool fuer Terrain-Generierung. Der Workflow: Heightfield-Generation in Houdini, Erosion (hydraulisch + thermisch), Pfade und Strassen als Masken, Export ueber das Houdini Engine Plugin direkt in UE5.

**Scope:** 4-6 km2, organisiert ueber UE5 World Partition mit 256m x 256m Zellen. World Partition erlaubt, dass nur die sichtbaren Terrain-Zellen geladen werden — essentiell fuer die Semi-Open-World ohne Ladebildschirme (GDD-01, Saeule P4).

**HDAs fuer Vera:** Ich baue Houdini Digital Assets mit vereinfachter Oberflaeche. Vera soll nicht Houdini lernen muessen — sie soll Parameter schieben koennen: Biom-Typ (Wald, Sumpf, Fels), Vegetationsdichte, Hoehenvariation, Pfad-Breite. Das HDA generiert, sie iteriert, wir exportieren. Das ist der Produktivitaetshebel.

Ehrliche Einschaetzung: Die HDAs muessen WIRKLICH einfach sein. Vera ist eine schnelle Lernerin, aber Houdini hat die steilste Lernkurve in unserer gesamten Tool-Chain. Wenn die HDAs zu komplex werden, wird Vera sie nicht nutzen, und ich werde zum Flaschenhals. Erste HDA-Version muss in Woche 3 getestet werden.

#### PCG-Vegetation

UE5s Procedural Content Generation (PCG) Framework fuer regelbasierte Vegetations-Platzierung. Die Regeln: Neigung (Gras nicht an Steilhaengen), Hoehe (Baumgrenze), Bodentyp (Sumpfpflanzen nur in Feuchtgebieten), Distanz zu Pfaden (keine Baeume AUF dem Weg), Distanz zu Gebaeuden (Lichtung um Siedlungen).

Vera liefert 8-12 Vegetations-Assets pro Biom. PCG verteilt sie nach Regeln. Das spart hunderte Stunden manueller Platzierung.

#### Substance Designer

Prozedurale Materialien fuer sich wiederholende Oberflaechen: Stein, Holz, Metall, Erde. Substance-Graphen exportieren direkt in UE5-kompatible Texturen (Base Color, Normal, ORM). Die ACES-Konfiguration in Substance muss identisch zur UE5-Konfiguration sein — sonst driften die Farben.

### 4.4 Asset-Quellen

| Quelle | Einsatzbereich | Budget-Implikation | Risiko |
|--------|----------------|--------------------|--------|
| Vera (Eigenproduktion) | Characters, Hero-Props, Concept Art, UI-Elemente | Intern (Gehalt) | Flaschenhals — eine Person fuer alles Visuelle |
| Tobi (prozedural) | Terrain, Felsen, Materialien, Vegetation-Verteilung | Intern (Gehalt) + Houdini-Lizenz | Houdini-Know-how ist nicht uebertragbar |
| Megascans (UE5 inklusive) | Umgebungs-Assets: Felsen, Boden, Vegetation-Basis | Kostenlos (Quixel Bridge) | Qualitaet gut, aber generisch — braucht Anpassung fuer RELICS-Look |
| Marketplace (selektiv) | Basis-Assets zum Anpassen, Animation Packs, VFX | Budget: 2.000-3.000 EUR (Kap. 8.2) | Qualitaetsschwankung. Jedes Asset muss vor Kauf geprueft werden |
| Photogrammetrie (optional) | Texturen, Fels/Mauerwerk-Referenz | Gering (eigene Ausruestung) | Detmold/Lemgo-Umgebung als Quelle. Mittelalterliche Architektur vor der Haustuer |

---

## 5. Schattenfieber-Tech

### 5.1 Systemuebersicht & Drei-Schichten-Rendering (ERWEITERT V2)

Das Schattenfieber ist das technisch anspruchsvollste System in RELICS. Es ist kein einzelner Effekt, sondern ein Querschnittssystem, das Rendering, VFX, Gameplay, Audio und Narrative verbindet.

**Kernprinzip:** Der Infektionswert (0-100, Float) ist der einzige Eingabeparameter fuer spielerseitige Effekte. Alle visuellen Effekte leiten sich von diesem einen Wert ab. Das System interpoliert kontinuierlich — keine harten Stufenschalter (GDD-02, Kap. 2.3).

#### Drei-Schichten-Rendering (NEU V2)

Die Welt in RELICS besteht aus drei Daseinsebenen (WBB-01, Emre Yilmaz): **Mittelgrund** (die bewohnte Welt), **Hohlicht** (die untere Ebene, dunkler, komprimierter), **Stillfeld** (die obere Ebene, leerer, gefaehrlicher). Normal ist nur der Mittelgrund sichtbar. Ab Schattenfieber-Schwelle (Infektionswert 76+) oder in bestimmten Lore-Orten beginnen die anderen Ebenen durchzuschimmern.

Technisch: Jede Ebene ist ein eigenes Post-Processing-Volume-Profil. Priority-Blending steuert, welche Profile aktiv sind. Maximum 5 aktive PP-Segmente gleichzeitig.

| Schicht | PP-Profil | Visuelle Identitaet | Aktivierung |
|---------|-----------|---------------------|-------------|
| Mittelgrund | `PPV_Midground_Base` | Standard-Rendering. Fraktionsspezifisches Color Grading. Kein Zusatz-Overhead | Immer aktiv |
| Mittelgrund (Schattenfieber) | `PPV_SF_Player` | Spielerseitig MPC-gesteuert. Alle SF-Effekte Stufe 1-4 | Infektionswert > 0 |
| Hohlicht | `PPV_Hohlicht` | Tiefer, komprimierter. Farbpalette: Richtung `#2D0A31`, Schatten verlaengert, Kontrast erhoet. Geometrie wirkt schwerer | Infektionswert >= 76 ODER Zone-Trigger |
| Stillfeld | `PPV_Stillfeld` | Heller, leer, geometrisch verzerrt. Entsaettigung extrem, Kanten scharf. Schwindel-WPO auf Peripherie | Infektionswert >= 90 ODER Zone-Trigger |
| Befallene Zone | `PPV_Zone_Befallen` | Level-Volume. Unabhaengig von Spieler-Infektionswert. Schattenfieber-Farbprofil fuer alle sichtbar | Level-Placement |

**Maximale Gleichzeitigkeit:** 3 Profile im Normalfall (Base + SF_Player + ggf. Zone). 5 Profile als absolutes Maximum (Base + SF_Player + Hohlicht + Stillfeld + Zone — nur in spezifischen Endgame-Sequenzen).

**Zwei Schattenfieber-Farbprofile:**
- **Profil A (spielerseitig):** MPC-gesteuert. Skaliert mit Infektionswert. Intensitaet graduell. Nur der Spieler sieht dieses Profil in seiner vollen Intensitaet.
- **Profil B (zonenbasiert):** Level-Volume, feste Werte. Alle Spieler sehen befallene Zonen gleich. Unabhaengig von persoenlichem Infektionswert — das sind oeffentliche Warnzeichen.

*Zu validieren mit Emre: Anzahl der aktiven Segmente pro Szene. Standard: 3. Maximum: 5. Bestaetigungsbedarf.*

### 5.2 Technische Architektur (unveraendert)

Das System besteht aus drei Schichten:

**Schicht 1: Material Parameter Collection (MPC)**
Eine zentrale MPC (`MPC_Schattenfieber`) haelt den Infektionswert als skalaren Parameter. Alle Post-Processing-Materialien, Niagara-Systeme und Welt-Shader lesen diesen Wert. Aenderungen am Infektionswert propagieren automatisch in alle Systeme — kein manuelles Update noetig.

**Schicht 2: Post-Processing Volume**
Ein eigener Post-Processing Volume, der dem Spielercharakter folgt (nicht level-global). Die Material-Instanzen in diesem Volume lesen die MPC und skalieren ihre Effekte entsprechend.

**Schicht 3: Niagara VFX**
GPU-Partikel-Systeme, die ebenfalls die MPC lesen. Schattensporen, Flimmern, Verzerrungspartikel — alles skaliert mit dem Infektionswert.

### 5.3 Fuenf-Stufen-Rendering (KORRIGIERT V2 — CD-Lock Stufengrenzen)

CD-verbindliche Stufengrenzen: Rauschen 1-40, Risse 41-75, Schwelle 76-100.

| Stufe | Lore-Phase | Infektionswert | Post-Processing Effekte | Niagara VFX | Welt-Effekte | Technische Komplexitaet |
|-------|-----------|---------------|------------------------|-------------|--------------|------------------------|
| 0 (Rein) | — | 0 | Keine | Keine | Keine | Baseline |
| 1 (Rauschen Frueh) | Rauschen | 1-20 | Leichte Farbverschiebung in den Schatten (kuehler, blaeulicher). Subtiles Vignette-Pulsieren (0.05 Hz) | Vereinzelte Schattensporen (2-5 Partikel, kaum sichtbar) | Schattensinne: Versteckte Objekte erhalten Custom Stencil Outline | Niedrig |
| 2 (Rauschen Spaet) | Rauschen | 21-40 | + Chromatische Aberration (einsetzend, 0.05-0.15). Farbsaettigung beginnt zu verschieben (Gruen > Cyan am Rand) | + Partikel-Overlay dichter (10-15 Partikel). Emotionsauren an NPCs als farbige Niagara-Systeme | + Gespraechsoptionen-Shader: UI-Text fuer SF-Dialoge mit leichtem Glitch | Mittel |
| 3 (Risse) | Risse | 41-75 | + Geometrische Verzerrung am Bildrand (Barrel Distortion, animiert). Farbpalette kippt merklich. Depth-of-Field-Schimmer auf mittlerer Distanz. CA staerker (0.2-0.5) | + Schattenranken-Partikel am Bildrand. Tiefensicht als Niagara-Overlay (geologische Schichten, Adern im Terrain) | + Custom Stencil Buffer fuer Objekte, die nur ab Rissen sichtbar sind. Fragwuerdige NPCs mit Flimmer-Shader | Hoch |
| 4 (Schwelle) | Schwelle | 76-100 | + Halluzinatorische Elemente (s. Kap. 5.4). Vertex-Displacement auf Welt-Geometrie. Doppelbilder (Ghost-Rendering). Farbkanal-Separation. Hohlicht/Stillfeld beginnen durchzuschimmern (Kap. 5.1) | + Vollstaendiges Sporen-Feld. Schatten bewegen sich autonom. Lichtquellen flackern asynchron | + Parallel-Geometrie: Ganze Raum-Segmente in alternativer Version. NPCs ohne visuellen Unterschied zu "echten" NPCs | Sehr hoch |

### 5.4 Graduelle Interpolation — Technik (KORRIGIERT V2)

Der Trick ist, dass alle Effekte nicht bei Stufengrenzen "anspringen", sondern ueber Kurven interpoliert werden:

- **Farbverschiebung:** `Lerp(NormalMatrix, VerschobenMatrix, InfektionswertFloat / 100)`. Beginnt bei Wert 1, voll bei 100.
- **Chromatische Aberration:** Intensitaet = `max(0, (Infektionswert - 20) / 80)`. Beginnt bei ~20, erreicht Maximum bei 100.
- **Geometrische Verzerrung (Barrel):** Intensitaet = `max(0, (Infektionswert - 41) / 59)`. Beginnt bei 41 (Risse-Grenze), graduell bis 100.
- **Halluzinationen:** `max(0, (Infektionswert - 76) / 24)`. **Beginnt bei 76 (Schwelle-Grenze).** Maximum bei 100. *(V1-Fehler: Start bei 70 — korrigiert auf 76 per CD-Lock.)*
- **Hohlicht-Einblendung:** `max(0, (Infektionswert - 76) / 24)`. Gleiche Kurve wie Halluzinationen. Schwelle-Phase = Hohlicht beginnt sichtbar zu werden.
- **Stillfeld-Einblendung:** `max(0, (Infektionswert - 90) / 10)`. Erst bei 90, extrem kurzer Bereich. Sehr intensive Wirkung.

Alle Kurven sind in UE5 als **Float Curve Assets** hinterlegt und koennen im Editor angepasst werden, ohne Code zu aendern. Emre und Nami koennen diese Kurven mitgestalten — sie definieren, WANN sich etwas "richtig" anfuehlt.

### 5.5 Welt-Effekte (Befallene Zonen)

Befallene Zonen in der Spielwelt haben eigene Post-Processing Volumes (Profil B, s. Kap. 5.1) mit vorab gesetzten Schattenfieber-Effekten — unabhaengig vom Infektionswert des Spielers. Diese Zonen sind fuer ALLE Spieler sichtbar.

- **Biotech-Vegetation:** Organische Auswuechse, pulsierende Ranken. Vertex-Animation (kein Nanite), emissive Materialien mit Pulse-Funktion. Farben: `#2D0A31` + `#39FF14`
- **Boden-Shader:** Terrain-Material mit zusaetzlichem Schattenfieber-Layer (organische Textur, leicht animiert)
- **Niagara-Atmosphaere:** Schattensporen als GPU-Partikel, Nebel mit volumetrischem Scattering. Emres Nebel-Beschreibung ("Nebel, der sich anfuehlt wie Trauer") = technische Parameter: langsame Partikel, tiefe Saettigung in `#2D0A31`, Gewicht nach unten (negative Y-Geschwindigkeit), kaum horizontale Drift.

### 5.6 Performance-Implikation

Das Schattenfieber-System hat ein eigenes Performance-Budget von **2 ms GPU-Zeit** (bei empfohlener Hardware). Aufgeteilt:
- Post-Processing (alle aktiven Profile): 0.8 ms
- Niagara-Partikel: 0.7 ms (GPU-Partikel, LOD-aware)
- Custom Stencil / Welt-Effekte: 0.5 ms (nur in befallenen Zonen aktiv)
- Drei-Schichten-Overhead (Hohlicht/Stillfeld aktiv): +0.3 ms Reserve einplanen

Bei Stufe 0 ist das Budget nahe 0 ms. Das System kostet nur, wenn es aktiv ist.

### 5.7 Abhaengigkeiten und offene Punkte

| Abhaengigkeit | Von wem | Status | Dringlichkeit |
|--------------|---------|--------|---------------|
| Hauten-Segmentanzahl (3 oder 5 Standard?) | Emre (Lore-Logik) | Offen | MITTEL — Annahme 3 Standard, brauche Bestaetigung |
| Visueller Referenz Stufe 3-4 | Emre (Lore), Vera (Concept) | Offen | HOCH — ohne Referenz baue ich ins Blaue |
| Infektionswert-Gameplay-Logik | Darius (GDD-02) | V0.5 vorhanden | Mittel |
| Narrative Zustaende → visuelle Parameter | Nami | Rauschen/Risse/Schwelle definiert | Mittel |
| Audio-Verzerrung (Risse+) | Offen (kein Audio-Lead) | Nicht begonnen | Niedrig fuer V1, hoch fuer VS |
| Abstimmungsmeeting Schattenfieber-Tech | Tobi + Emre + Darius + Vera | Noch nicht terminiert | HOCH — naechste Woche |

---

## 6. Performance-Ziele

### 6.1 Hardware-Tiers

RELICS definiert drei Hardware-Tiers. Die Ziel-Framerates sind ambitioniert, aber durch Upscaling-Technologie erreichbar.

| Tier | GPU-Referenz | CPU-Referenz | RAM | Ziel-FPS | Aufloesung | Rendering |
|------|-------------|-------------|-----|----------|-----------|-----------|
| Minimum | GTX 1070 / RX 5700 | i5-8400 / R5 3600 | 16 GB | 30 fps | 1080p | Software Lumen, Low Settings, FSR Quality |
| Empfohlen | RTX 3070 / RX 6800 | i7-10700 / R7 5800X | 16 GB | 60 fps | 1440p | HW RT Lumen, High Settings, DLSS/FSR Quality |
| High-End | RTX 4080+ / RX 7900 XT | i7-12700+ / R7 7800X3D | 32 GB | 60 fps | 4K | Max Settings, RT Reflections, DLSS/FSR Performance |

**Redaktionelle Notiz:** Minimum-Tier (GTX 1070) ist provisorisch. GTX 1070 mit Software Lumen, Nanite und Schattenfieber-Effekten bei 30 fps ist ambitioniert. Der tatsaechliche Minimum-Tier wird nach Benchmark-Phase (Woche 6-8) final gesetzt — moeglicherweise auf GTX 1660 / RX 5500 XT verschoben. Das ist eine datenbasierte Entscheidung.

### 6.2 Upscaling (Pflicht)

Upscaling ist nicht optional, sondern ein Kern-Feature:
- **DLSS 3** (Nvidia): Super Resolution + Frame Generation
- **FSR 3** (AMD): Super Resolution + Fluid Motion Frames
- **XeSS** (Intel): Optional, niedriger Prio

DLSS und FSR sind der Grund, warum 60 fps bei 4K realistisch ist. Ohne Upscaling waere 4K/60 auf keiner Consumer-Hardware erreichbar.

Frame Generation als Option fuer unterstuetzte Hardware. Nicht als Standard aktiviert — Eingabe-Latenz ist bei Action-Combat relevant.

### 6.3 Performance-Budgets

| Kategorie | Budget | Begruendung |
|-----------|--------|-------------|
| Draw Calls | < 5.000 pro Frame | Nanite reduziert Draw Calls drastisch. 5.000 ist konservativ und laesst Raum fuer UI und Partikel |
| Dynamische Lichter | 8-12 gleichzeitig | VSM-Limit. Darueber hinaus Performance-Einbruch |
| Vegetation Draw Distance | Gras: 50-80 m, Baeume: 500 m | Gras ist der teuerste Vegetationstyp. Baeume als Impostors ab 300 m |
| NPC-Count (sichtbar) | 20-30 gleichzeitig | StateTree + Mass Entity System |
| Partikel (Schattenfieber) | GPU-Budget: 2 ms | Kap. 5.6. LOD-aware: Partikel-Count sinkt mit Distanz |
| Speicher (VRAM) | 6 GB (Minimum), 8 GB (Empfohlen) | Nanite-Geometrie + Streaming-Texturen + Lumen-Datenstrukturen |
| Level-Streaming | World Partition, 256 m Zellen | Laderadius: 3-4 Zellen um Spieler |
| SSS (Hauten-Shader) | 0.3-0.5 ms | Screen-Space-Overhead. Nur auf organischen Hero-Assets aktiv |
| WPO-System | 0.2 ms | Nur aktive organische Elemente im Sichtfeld |

---

## 7. Produktions-Pipeline

### 7.1 Versionskontrolle

Zwei Systeme, klar getrennt:

**Perforce (Helix Core)** fuer das UE5-Projekt. Das umfasst alle Binaer-Assets (Meshes, Texturen, Maps, Blueprints, Sound). Perforce ist der Industriestandard fuer Unreal-Projekte, weil es Binaer-Dateien nativ sperren kann (File Locking). Kein Git LFS fuer Engine-Assets.

**Git** fuer Dokumentation (GDD, WBB, dieses Dokument), Scripts, Pipeline-Tools.

### 7.2 Ordnerstruktur (UE5-Projekt)

```
Content/
  RELICS/
    Characters/
      Player/
      NPCs/
      Creatures/
    Environment/
      Architecture/
        Modules/
        Assembled/
      Vegetation/
        Trees/
        Ground/
        Schattenfieber/
      Terrain/
    Props/
      Weapons/
      Furniture/
      Interactive/
    Materials/
      Master/
      Instances/
        Krone/
        Gilden/
        Orden/
        Schattenfieber/
        Organisch/       -- NEU: SSS-Profile, WPO-Materialien
    VFX/
      Niagara/
        Combat/
        Schattenfieber/
        Environment/
    Audio/
    UI/
      HUD/
      Menus/
      Nervensystem/
    Blueprints/
      Core/
      Combat/
      Camera/
      AI/
      Schattenfieber/    -- MPC, PP-Volumes, alle fuenf Profile
    Maps/
      Persistent/
      Sublevels/
      Test/
    Data/
      DataTables/
      Curves/            -- Float Curves: SF-Parameter, Kamera-Blends, WPO-Intensitaet
      GameplayTags/
```

### 7.3 Tool-Chain

| Tool | Version | Einsatz | Verantwortlich | Lizenzkosten (jaehrlich) |
|------|---------|---------|----------------|-------------------------|
| Unreal Engine 5.4+ | Latest stable | Runtime, Level Design, Blueprints, Sequencer | Tobi, Darius, Gameplay-Programmer | Kostenlos (5% Royalty ab 1M USD) |
| Houdini Indie | 20.5+ | Terrain, prozedurale Assets, FX-Prototyping | Tobi | ~270 EUR/Jahr |
| Houdini Engine (UE5 Plugin) | Matching | Houdini-UE5-Bridge | Tobi | In Indie-Lizenz enthalten |
| Substance Painter | Latest | Texturierung, Materialien | Vera, Tobi | ~220 EUR/Jahr (Indie) |
| Substance Designer | Latest | Prozedurale Materialien | Tobi | In Substance-Abo enthalten |
| Blender | 4.x | 3D-Modelling, Rigging, UV-Layout | Vera | Kostenlos |
| Photoshop / Krita | Latest | Concept Art, Texturen, UI-Mockups | Vera | ~290 EUR/Jahr (PS) oder kostenlos (Krita) |
| Perforce Helix Core | Latest | Asset-Versionskontrolle | Tobi (Admin) | Kostenlos bis 5 User |
| Jira / Notion | TBD | Taskmanagement, Sprint-Planung | Finn | ~0-100 EUR/Jahr |
| DaVinci Resolve | 19+ | Color Grading Referenz, Trailer-Schnitt | Tobi | Kostenlos (Free Version) |

**Gesamte jaehrliche Tool-Kosten:** ~780-1.080 EUR.

---

## 8. Meilensteine & Budget

### 8.1 Phasen

| Phase | Zeitraum | Kern-Deliverables | Abhaengigkeit | Exit-Kriterium |
|-------|----------|-------------------|---------------|----------------|
| **Pre-Production** | Wochen 1-4 | GDD V1 + WBB V1 fertig. UE5-Projekt steht. Kamera-Prototyp spielbar. Terrain-Prototyp (1 km2). Art-Style-Targets validiert | Team komplett (minus Gameplay-Programmer) | CD gibt Design-Lock. Alle koennen im UE5-Projekt arbeiten |
| **Vertical Slice Prototype** | Wochen 5-12 | Spielbare Szene: 1 Region (~1 km2), Hauptquest-Ausschnitt (30 min Gameplay), Combat V1 (Schwert + Bogen, 3 Feindtypen), 1 Stadt (Blockout), Schattenfieber Stufe 0-2 | Gameplay-Programmer an Bord (spaetestens Woche 5) | Szene spielbar. Combat fuehlt sich "gewichtig" an |
| **Vertical Slice Polish** | Wochen 13-18 | VS spielbar und praesentabel: Beleuchtung (Lumen-Pass), Asset-Polish (Nanite, Material-Instanzen), Quest komplett, Performance-Ziele auf empfohlener Hardware, Schattenfieber Stufe 0-3 | Asset-Pipeline laeuft | VS vorzeigbar (CD, Publisher, Presse) |
| **Alpha** | Wochen 19-30 | Gesamte Kernregion (4-6 km2). Alle Quests (Greybox). Combat V2 (alle 6 Waffenklassen). Nervensystem-Leveling spielbar. Alchemie V1. Schattenfieber alle Stufen inkl. Drei-Schichten | Scope-Lock (spaetestens Ende Woche 18) | Feature-Complete |
| **Beta** | Wochen 31-40 | Content-Complete. Polish-Pass. QA-Runden. Performance-Optimierung. Balancing | QA-Kapazitaet | Alle bekannten Blocker gefixt |
| **Release** | Woche 40+ | Steam Early Access oder Full Release | CD-Entscheidung | Spielbar, stabil, repraesentativ |

### 8.2 Budget-Aufschluesselung (45.000 EUR Freelancer-Budget) — ERWEITERT V2

Das Freelancer-Budget ist begrenzt und muss strategisch eingesetzt werden.

| Position | Geschaetztes Budget | Zeitraum | Begruendung |
|----------|-------------------|----------|-------------|
| **Gameplay-Programmer (GAS/Combat)** | 20.000-25.000 EUR | Wochen 5-18 (14 Wochen) | Kritischste Abhaengigkeit. Ohne diese Person kein Combat, kein VS. ~1.400-1.800 EUR/Woche |
| **Animations-Assets** | 5.000-8.000 EUR | Wochen 8-18 | Marketplace-Packs + Custom-Anpassung. Motion-Matching-Datenbank. Ggf. MoCap-Session (~2.000 EUR fuer einen Tag) |
| **Audio/Sound Design** | 5.000-7.000 EUR | Wochen 13-30 | MetaSounds-Setup, Combat-SFX, Ambient, Schattenfieber-Audio |
| **QA-Support** | 3.000-5.000 EUR | Wochen 25-40 | Externe Tester fuer Schattenfieber-Stufenuebergaenge |
| **Marketplace-Assets** | 2.000-3.000 EUR | Laufend | Architektur-Bases, Vegetation-Packs, VFX-Bibliotheken |
| **Puffer** | 2.000-5.000 EUR | Reserve | Unvorhergesehenes |
| **Gesamt** | ~37.000-53.000 EUR | | Mittelwert: ~45.000 EUR |

**Anforderungsprofil Gameplay-Programmer (PFLICHT-Kriterien):**

- **GAS (Gameplay Ability System): Pflicht-Kriterium.** Wer kein nachweisbares GAS-Projekt vorweisen kann, kommt nicht in die engere Auswahl. Keine Ausnahmen.
- UE5 C++ auf Produktionsniveau (kein Blueprint-only)
- StateTree-Erfahrung oder Bereitschaft zur schnellen Einarbeitung (gute Dokumentation vorhanden)
- Freelancer-Erfahrung: Milestone-basierte Abrechnung muss akzeptabel sein
- Verfuegbarkeit ab Woche 5 (spaetestens)
- Kommunikationssprache Deutsch oder Englisch

**Wunsch-Kriterien (kein Ausschluss):**
- Erfahrung mit Third-Person-Action-Spielen (Gothic, Souls-artige als Referenz)
- Motion Matching Erfahrung (UE5)
- Vertrautheit mit ACES-Farb-Pipelines

**Suche beginnt:** Sofort (Woche 1). Finn fuehrt erste Gespraeche. Stellenbeschreibung: Abstimmung Tobi+Finn.

**Ehrliche Einschaetzung:** 45.000 EUR ist ein sehr knappes Budget. Der Gameplay-Programmer allein verbraucht die Haelfte. Wenn diese Person laenger als 14 Wochen braucht oder teurer ist als geschaetzt, wird der Rest des Budgets komprimiert. Risiko-Mitigation: Frueh mit der Suche beginnen, klaren Scope kommunizieren, Milestone-basierte Bezahlung vereinbaren.

---

## Anhang A: Offene Fragen (Priorisiert)

### Kritisch

1. **Schattenfieber-Abstimmung** mit Emre, Darius und Vera — Was genau passiert visuell auf jeder Stufe? Ich brauche Concept-Referenzen, bevor ich Shader baue. Vorschlag: 30-Minuten-Meeting, Vera skizziert live.
2. **Hauten-Segmentanzahl** mit Emre — 3 oder 5 gleichzeitig aktive PP-Segmente als Standard? Lore-Logik entscheidet.
3. **Asset-Standards-Review** mit Vera — Naming, Texel Density, LOD-Workflow, Hex-Code-Umsetzung in Material-Instanzen bestaetigen.
4. **Gameplay-Programmer-Profil** mit Finn — Stellenbeschreibung schreiben, Suche starten.

### Wichtig (Pre-Production)

5. **Dialog-System-Middleware** mit Nami — Yarn Spinner, Ink, oder UE5-eigenes System?
6. **Audio-Pipeline** — Wer verantwortet MetaSounds-Setup?
7. **Terrain-Biome** mit Emre — Wie viele, welche? Jedes Biom braucht HDA + Vegetations-Assets.

### Nachrangig (Vertical Slice)

8. **Konsolen-Stretch-Goal** — Erst nach VS Polish evaluieren (Woche 18).
9. **Lokalisierung** — Nur Deutsch? Deutsch + Englisch? Beeinflusst UI-Layout.
10. **Accessibility** — Farbblindheits-Modi, Untertitel-Groessen, Remapping. Frueh in UI-Architektur beruecksichtigen.

---

## Anhang B: Glossar

| Begriff | Erklaerung |
|---------|-----------|
| ACES | Academy Color Encoding System. Industriestandard fuer konsistenten Farbraum ueber mehrere Tools |
| GAS | Gameplay Ability System. UE5-natives Framework fuer Faehigkeiten, Attribute und Gameplay-Effekte |
| HDA | Houdini Digital Asset. Wiederverwendbarer, parametrischer Houdini-Node mit vereinfachter Oberflaeche |
| MPC | Material Parameter Collection. UE5-System, um globale Werte an alle Materialien gleichzeitig zu senden |
| Nanite | UE5-System fuer virtualisierte Geometrie. Automatisches LOD ohne kuenstlerischen Aufwand |
| Lumen | UE5-System fuer dynamische globale Beleuchtung. Kein Baking noetig |
| PCG | Procedural Content Generation. UE5-Framework fuer regelbasierte Asset-Platzierung |
| VSM | Virtual Shadow Maps. UE5-Schattensystem mit hoher Aufloesung |
| VS | Vertical Slice. Spielbarer, repraesentativer Ausschnitt des fertigen Spiels |
| MoCap | Motion Capture. Aufzeichnung realer Bewegungen fuer Spielanimationen |
| SSS | Subsurface Scattering. Lichtstreuung unterhalb einer Oberflaeche. Essentiell fuer organische/Haut-Materialien |
| WPO | World Position Offset. Vertex-Displacement im Shader. Grundlage fuer atmende, lebende Oberflaechen |
| PPV | Post-Processing Volume. UE5-Container fuer Screen-Space-Effekte |
| SF | Schattenfieber. Abkuerzung intern |

---

*Tobi Richter, Tech Corner, Tag 5 Freitag Vormittag — V2 fertig.*
*Aenderungen: Hex-Codes GDD-05 1:1, Kap. 1.4 Organische Shader-Architektur neu, Drei-Schichten-Rendering Kap. 5.1, Stufengrenzen CD-Lock, Halluzinations-Start korrigiert auf 76, Anforderungsprofil Gameplay-Programmer.*
*Naechster Schritt: Schattenfieber-Abstimmung terminieren, Hauten-Segmentanzahl mit Emre klaeren, Kamera-Blueprint V0.1.*

\clearpage
