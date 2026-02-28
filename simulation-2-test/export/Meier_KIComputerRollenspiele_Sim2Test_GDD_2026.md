---
title: "RELICS — Game Design Document"
author: "GenSoftworks Studio Simulation"
date: "2026"
lang: german
toc: true
---

# GDD-01: Spielübersicht & Design-Säulen


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
| **USP 2** | Welt-Reaktivität statt Marker-Quests | Die Welt erinnert sich. NPCs haben Gedächtnisse. Konsequenzen kommen — auch wenn der Spieler sie vergessen hat. | Gothic 2 ist der nächste Vergleich. RELICS setzt diesen Standard 2026 neu. |
| **USP 3** | Open-World mit Immersive-Sim-Vertikalität | Weltdichte und Exploration eines Gothic-artigen RPG + räumliche Tiefe und Systeminteraktion einer Immersive Sim | Kein existierendes Referenzspiel bietet beides. Gothic/Skyrim sind horizontal. Dishonored ist abgeschlossen. |

---

## 5. Zielgruppe


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
| **Baldur's Gate 3** | Proof of Concept: großes Computer-Rollenspiel kann kommerziell erfolgreich sein | Rundenbasierter Kampf, festes Team |
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

\clearpage

# GDD-02: Kernmechaniken


---

## 1. Combat-System

### 1.1 Grundphilosophie
- Real-time Action, Melee-fokussiert, gewichtig
- KEIN Difficulty Slider — die Welt bestimmt die Schwierigkeit (Gothic-Prinzip)
- Skill-Ceiling als Spektrum (CD-bestätigt): Einstieg intuitiv, Mastery belohnend — nie erzwungen
- Jeder Kampf soll sich BEDEUTSAM anfühlen — keine Trash-Mobs, kein Grind
- Spieler-Fantasie: "Ich habe diesen Kampf gewonnen, weil ich besser geworden bin — nicht weil ich Level 50 bin."

**Skill-Ceiling-Spektrum (Detail):**
Das System muss auf BEIDEN Enden des Spektrums funktionieren. Ein Spieler, der nur Basisaktionen nutzt, soll jede Begegnung bestehen können (mit Vorbereitung und Geduld). Ein Spieler, der Cancel-Windows und Setup-Plays beherrscht, soll sich belohnt fühlen (schnellere Kills, elegantere Lösungen, optionale Herausforderungen). Kein Spieler soll das Gefühl haben, er müsste Mastery-Techniken lernen, um weiterzukommen. Aber jeder Spieler soll sehen KÖNNEN, was möglich wäre.

### 1.2 Kampfschichten (drei Ebenen)

#### Ebene 1 — Basis (sofort zugänglich)
- Leichter Angriff, schwerer Angriff, Block, Ausweichen
- Ausdauer-Management: Jede Aktion kostet Ausdauer, Übertreiben wird bestraft
- Ziel-Lock-On optional (nicht erzwungen)
- Jeder Spieler kann sofort kämpfen — Gothic-Gewicht, Skyrim-Zugänglichkeit

#### Ebene 2 — Fortgeschritten (erlernt durch Trainer + Übung)
- Parade/Riposte: Präzises Timing-Fenster, belohnt mit Gegenangriff
- Positionierung: Flankenangriffe, Rückenattacken, Höhenvorteile (Vertikalität!)
- Waffenspezifische Kombos: Abhängig von Waffenklasse, erlernt bei Trainern
- Umgebungsinteraktion: Objekte treten/werfen, Engstellen nutzen, Gegner in Fallen locken

#### Ebene 3 — Mastery (belohnend, nie erzwungen)
- Cancel-Windows: Fortgeschrittene Spieler können Animationen unterbrechen für Feints
- Setup-Plays: Alchemie-Vorbereitung (Öle, Gifte) + Positionierung + Timing als koordinierte Strategie
- Schattenfieber-Combat-Integration: Schattenreflex (erweitertes Parry-Window), Fieber-Puls (Aö, kostet HP)
- Perfekte Paraden: Winzigstes Timing-Fenster, maximal belohnend (Spezial-Riposte)

### 1.3 Waffenklassen (vorläufig)
- **Schwerter** (Einhand/Zweihand): Allrounder, mittlere Geschwindigkeit, ausgewogenes Moveset
- **Äxte/Hämmer** (Einhand/Zweihand): Langsam, hoher Schaden, Schildbrecher
- **Dolche/Kurzwaffen**: Schnell, niedriger Einzelschaden, Combo-orientiert, Giftapplikation
- **Bögen**: Ranged, Haltungsschaden, kein Hauptwaffen-Fokus (Unterstützung)
- **Armbrüste**: Schwerer Ranged-Schaden, lange Nachladezeit, Situationswaffe
- **Schilde**: Defensiv, Block-Effizienz, Schildstoss als Unterbrechung

**Offene Frage:** Waffenklassen-Anzahl für den Vertical Slice? Empfehlung: 3-4 Nahkampf + 1 Ranged für V1.

### 1.4 Feinddesign-Prinzipien
- Feinde haben EIGENE Movesets, nicht nur skalierte Spieler-Angriffe
- Feindtypen definiert durch Verhalten, nicht nur durch Werte: Aggressive, Defensive, Taktiker, Infizierte
- Infizierte Feinde nutzen Schattenfieber-Fähigkeiten — Vorschau für den Spieler ("Das könnte ICH auch")
- Keine Level-Skalierung: Gebiete haben feste Feindstärke. Manche Gegner sind zu früh zu stark. Komm später wieder.

### 1.5 Tod und Konsequenz
- Tod ist ein Rückschlag, kein Game Over — Checkpoint-System mit fairen Abständen
- Keine Erfahrungspunkt-Strafe bei Tod
- **Tod beeinflusst den Infektionswert NICHT** (CD-bestätigt). Begründung: Tod ist bereits Strafe genug. Infektionsanstieg bei Tod würde Risk/Reward des Schattenfieber-Systems untergraben und die bewusste Entscheidung zur Nutzung verwischen.
- Konsequenz durch WELT-Reaktion: Bestimmte Situationen verändern sich bei erneutem Versuch (NPC-Kommentare, veränderte Wachpositionen)

---

## 2. Schattenfieber-System

> **QA-Einschätzung (Leo):** 40% des QA-Aufwands entfällt auf das Schattenfieber-System. Es ist gleichzeitig grösster USP und grösstes Risiko. Die folgenden drei nicht-verhandelbaren Bedingungen sind das Ergebnis von Leos Community- und Marktanalyse.

### 2.1 Drei Nicht-Verhandelbare Bedingungen (QA-validiert)

Diese drei Bedingungen haben Veto-Recht über jede Schattenfieber-Designentscheidung. Wenn ein Feature eine dieser Bedingungen verletzt, wird es geändert oder gestrichen — ohne Ausnahme.

**Bedingung 1: TRANSPARENZ VOR INFEKTION**
- Der Spieler muss JEDERZEIT wissen, welche Aktion seinen Infektionswert erhöhen kann und um wie viel
- Keine versteckten Infektionsquellen. Keine "Überraschung, du bist jetzt infiziert"
- UI-Feedback: Klarer Indikator wenn der Spieler sich in einer infektionserhöhenden Situation befindet (visuell, auditiv, haptisch)
- Infektionserhöhende Aktionen müssen eine explizite Bestätigung haben ODER einen klar wahrnehmbaren Moment der bewussten Entscheidung bieten
- **Goldstandard**: Bloodborne Insight — der Spieler sammelt Insight durch spezifische, erkennbare Aktionen (Bosse sehen, Madman's Knowledge nutzen). Es gibt keine versehentliche Insight-Erhöhung
- **Anti-Referenz**: Skyrim Vampirismus — Infektion passiert im Kampf durch einen zufälligen Statuseffekt, den Spieler oft nicht bemerken. Der häufigste Community-Complaint: "Ich wusste nicht, dass ich Vampir werde"

**Bedingung 2: SOFORTIGE POWER FANTASY NACH INFEKTION**
- Ab dem ERSTEN PUNKT Infektionswert muss der Spieler etwas Cooles können, das er vorher nicht konnte
- Kein "Stufe 1 ist nur Nachteile, die guten Sachen kommen später" — das widerspricht der Kernfantasie
- Schattensinne (Stufe 1) müssen sofort als Upgrade erlebbar sein: Verstecktes sehen, Emotionen lesen, eine ZWEITE SCHICHT der Welt wahrnehmen
- Der Spieler soll nach der ersten Infektion denken: "Das war es wert. Was kommt noch?"
- **Goldstandard**: Bloodborne — der erste Insight-Punkt zeigt sofort die Puppe im Hunter's Dream. Die Welt verändert sich. Der Spieler fühlt sich belohnt.

**Bedingung 3: KEIN VERSEHENTLICHES INFIZIEREN**
- Infektion darf NIEMALS durch Zufall, Unachtsamkeit oder unklare Mechaniken passieren
- Jeder Infektionspunkt muss auf eine BEWUSSTE SPIELERENTSCHEIDUNG zurückführbar sein
- Kampf gegen Infizierte = Infektionsrisiko? Dann muss das VOR dem Kampf klar kommuniziert werden, und der Spieler muss eine taktische Wahl haben (Distanzwaffen, Alchemie-Schutz, Umgehen)
- Story-Events, die Infektion erhöhen: Müssen als Entscheidung präsentiert werden, nicht als Cutscene-Zwang
- **Design-Test**: Wenn ein Spieler nach 20 Stunden sagt "Ich wollte Stufe 0 bleiben, aber irgendwie bin ich Stufe 2" — dann haben wir versagt

### 2.2 Systemübersicht
- Permanenter Infektionswert: 0-100
- Fünf mechanische Stufen mit spürbaren Schwellen
- Vierter Ast im Nervensystem-Leveling (nur ab Stufe 1+)
- NICHT heilbar, nur kontrollierbar (CD-bestätigt)
- Jede Stufe = andere Spielerfahrung, KEINE ist schlechter als die andere

### 2.3 Stufen-Mapping: Mechanik x Narrativ x Wahrnehmung

Die folgende Tabelle synchronisiert Darius' fünf mechanische Stufen mit Namis drei narrativen Zuständen (Rauschen, Risse, Schwelle). Die narrativen Zustände sind KEINE separaten Systeme — sie sind die erlebbare Oberflächenerscheinung der mechanischen Stufen.

| Mech. Stufe | Wert | Name | Narrativer Zustand (Nami) | Kern-Fantasie | Zentrale Fähigkeit | Narrative Auswirkung |
|-------------|------|------|---------------------------|---------------|---------------------|---------------------|
| 0 | 0 | Rein | Gesund | Underdog, rein menschlich | Volle Nervensystem-Effizienz, uneingeschränkte Sozialinteraktion | Standard-Erzählung: klare, zuverlässige Wahrnehmung |
| 1 | 1-25 | Gezeichnet | Rauschen | "Ich sehe, was andere nicht sehen" | Schattensinne (passiv): Verstecktes sichtbar, Emotionsauren | Subtile Textveränderungen in Dialogen. Umgebungshinweise, die andere nicht sehen. Einzelne Worte in NPC-Sätzen verschieben sich. Spieler bemerkt es vielleicht nicht sofort. |
| 2 | 26-50 | Infiziert | Rauschen → Risse (Übergang) | Mächtig, aber sichtbar anders | Schattenreflex, Schatten-Schritt, Schmerzunterdrückung | Übergangszone: Hinweise werden deutlicher, erste fragwürdige Wahrnehmungen. Gesprächsoptionen erscheinen, die andere nicht hören. |
| 3 | 51-75 | Verwandelt | Risse | Kein Mensch mehr, aber mächtig | Schattenprojektion, Fieber-Puls, Tiefensicht | Alternative Dialoge mit Figuren, die möglicherweise anders reden als erwartet. Fragwürdige Questgeber. NPCs reagieren irritiert auf Antworten, die der Spieler für normal hält. |
| 4 | 76-100 | Entfesselt | Schwelle | Das Monster — und vielleicht ist das okay | Schattenform, Fieber-Ruf, Schattenwurzeln + Kontrollverlust-Episoden | Parallel-Narrativ: Dialoge mit Figuren, die möglicherweise nicht existieren. Daseinsebenen werden durchlässig. Der Spieler kann nicht mehr unterscheiden, welche Gespräche "echt" sind. |

**Übergangs-Design:**
- Stufenübergänge sind KEINE harten Schalter. Der Infektionswert bestimmt die Intensität innerhalb einer Stufe graduell.
- Beispiel: Bei Wert 15 sind Schattensinne schwächer als bei Wert 24. Es gibt keinen Moment, in dem alles "anspringt".
- Die narrativen Zustände haben weiche Grenzen: "Rauschen" beginnt ab dem ersten Infektionspunkt und intensiviert sich. "Risse" setzt schrittweise ab ca. Wert 40 ein. "Schwelle" wird ab ca. Wert 70 spürbar.
- **QA-Relevanz (Leo)**: Genau dieser graduelle Übergang ist der Grund für den hohen QA-Aufwand. Jeder der ~100 Infektionswerte muss sich in der Spielerfahrung "richtig" anfühlen.

### 2.4 Infektionsfortschritt

**Steigerung:**
- Umgebungsexposition (verseuchte Orte, Kampf gegen Infizierte) — NUR mit vorheriger Warnung (Bedingung 1+3). Der Spieler sieht/hört/spürt, dass ein Ort verseucht ist, BEVOR er ihn betritt.
- Bewusste Nutzung (Schattenfieber-Fähigkeiten einsetzen: ~0.5-1 Punkt pro Einsatz) — jede Fähigkeitsnutzung zeigt den Infektionsanstieg im UI
- Story-Events (Schlüsselmomente, Boss-Begegnungen) — IMMER als bewusste Spielerentscheidung präsentiert, nie als Cutscene-Zwang
- Kontakt mit der Lebenden Krone (siehe 2.7) — Relikt-Interaktion als hochriskante, hochbelohnende Infektionsquelle
- Tod erhöt den Infektionswert NICHT (CD-bestätigt)

**Senkung:**
- Alchemie-Suppressiva (-3 bis -5 Punkte, teuer, Wirkung nimmt bei hohem Wert ab)
- Orden-Reinigung (-10 bis -15 Punkte, nur bei Orden-Allianz, ab Stufe 3 verweigert)
- Ruhe und Isolation (-1/Tag, nur bis Stufe 2)

**Hard Cap:** Infektionswert kann NIE unter die höchste je erreichte Stufenschwelle fallen. Die Infektion vergisst nicht.

### 2.5 Kosten-Nutzen-Matrix

> Die Tabelle muss gegen Bedingung 2 (sofortige Power Fantasy) validiert werden. JEDE Zeile ab Stufe 1 muss einen klaren, sofort erlebbaren Vorteil haben, der die Kosten aufwiegt — zumindest im Moment der Entscheidung.

| Stufe | Nutzen (sofort erlebbar) | Kosten (wachsend) | Stufe-0-Äquivalent |
|-------|-------------------------|-------------------|---------------------|
| 0 | Volle Systemeffizienz, voller Weltzugang, vollständige Alchemie-Wirkung | Kein Zugang zu Schattenfähigkeiten, keine zweite Wahrnehmungsschicht | — |
| 1 | **Schattensinne** (Exploration-Vorteil): Verstecktes sichtbar, Emotionsauren, neue Wege | Lymph -5%, Misstrauen aufmerksamer NPCs | Volle Alchemie als Alternative zu Schattensinnen |
| 2 | **Aktive Kampf-Fähigkeiten**: Schattenreflex, Schatten-Schritt — neue Kampfdimension | Lymph -15%, Cardio -10%, sichtbar infiziert, Krone distanziert | Fortgeschrittene Trainer-Fähigkeiten (Ebene 2+3) |
| 3 | **Fortgeschrittene Fähigkeiten**, +15% Melee, Tiefensicht | Alle Äste -25%, Krone feindlich, Orden jagt | Meister-Alchemie + Positionierung + Setup-Plays |
| 4 | **Apex-Fähigkeiten**, massive Kampfkraft, volle Doppelwahrnehmung | Alle Äste -40-50%, Kontrollverlust, soziale Isolation | Kein direktes Äquivalent — Stufe 0 hat dafür volle soziale Integration |

**Stufe-0-Äquivalent (neu):** Jede Schattenfieber-Stufe hat eine nicht-infizierte Alternative, die denselben Spielraum abdeckt, aber mit anderen Mitteln. Das sichert ab, dass Stufe 0 sich NIE wie "der langweilige Weg" anfühlt.

### 2.6 Weltreaktivität
- NPCs reagieren auf Infektionsstufe (Angst, Mitleid, Nützlichkeit, Feindschaft)
- Fraktionen verschieben Zugang: Orden schliesst früh, Krone später, Gilden pragmatisch
- Infizierte NPCs erkennen den Spieler ab Stufe 2+ als "einen von ihnen"
- Mögliche emergente vierte Fraktion: Untergrund der Infizierten (offene Frage für Emre/Nami)
- Umgebungseffekte: Tiere fliehen, Pflanzen reagieren (ab Stufe 3+)

### 2.7 Das Relikt: Die Lebende Krone


- Die Lebende Krone ist ein organisches Artefakt, das auf die kosmologische Ur-Bindung (WBB-01, Kap. 4) zurückgeht
- Sie ist LEBENDIG im wörtlichen Sinne: Sie reagiert, wächst, verändert sich — Biotech auf kosmologischer Ebene
- Fraktions-Interpretationen:
  - **Krone**: Dynastisches Erbe, Legitimation der Herrschaft, Zeichen göttlichen Auftrags
  - **Gilden**: Das wertvollste Handelsgut der Welt, Machtinstrument ohne ideologische Bindung
  - **Orden**: Erkenntniswerkzeug, Schlüssel zum Verständnis der Ur-Bindung und der Daseinsebenen
- Schattenfieber-Verbindung: Die Lebende Krone und das Schattenfieber greifen auf dasselbe "Emer-Material" zu (WBB-01, Kap. 6). Die Krone ist die kontrollierte Form, das Schattenfieber die unkontrollierte.
- Kontakt mit der Krone KANN den Infektionswert erhöhen — massiv, aber unter Bedingung 1 und 3 (Transparenz, bewusste Entscheidung)

### 2.8 Transparenz-UI (QA-Anforderung)

> Direkte Umsetzung von Bedingung 1. Dieses UI-Modul ist KEIN "nice-to-have" — es ist systemkritisch.

- **Infektionsanzeige**: Permanenter Balken/Indikator (nicht als Zahl, sondern als organische Visualisierung — passend zum Nervensystem-UI)
- **Warnhinweis**: Wenn der Spieler eine infektionssteigernde Zone betritt, Aktion ausführt oder Story-Entscheidung trifft → visueller + auditiver Cue BEVOR die Erhöhung eintritt
- **Fähigkeitskosten**: Jede Schattenfieber-Fähigkeit zeigt ihren Infektionskosten-Wert im Tooltip
- **Stufenwarnung**: Wenn der Spieler kurz vor einer neuen Stufenschwelle steht (5 Punkte entfernt), bekommt er einen besonderen Hinweis — die Schwelle ist permanent
- **Design-Vorgabe für Vera**: Die Infektionsanzeige soll sich organisch in die Nervensystem-Visualisierung einfügen. Kein separates HUD-Element, sondern Teil desselben körperlichen Systems.

## 3. Nervensystem-Leveling

### 3.1 Systemübersicht
- Vier physiologische Äste statt klassischer Skill-Trees
- Begrenzte Leveling-Punkte pro Level-Up — Ressourcenkonkurrenz erzwingt Spezialisierung
- Visuelle Darstellung: Halbtransparente Nervensystem-Ansicht des Körpers (Biotech-Futurismus)
- Progression ist KÖRPERLICH, nicht abstrakt

### 3.2 Die vier Äste

| Ast | Systeme | Kern-Attribute | Gameplay-Effekte |
|-----|---------|---------------|-----------------|
| **Cardio/Atmung** | Herz, Lunge, Kreislauf | Ausdauer, Regeneration, Bewegung | Sprint-Dauer, Schwimmen, Ausweich-Distanz, Erholungsrate |
| **Muskel/Skelett** | Muskeln, Knochen, Sehnen | Stärke, Resistenz, Waffenhandhabung | Schadensoutput, Block-Stabilität, Tragekapazität, Waffenfreischaltung |
| **Lymph/Immun** | Immunsystem, Stoffwechsel | Alchemie-Effizienz, Gift-Resistenz, Heilung | Trank-Wirkung, Krankheitsresistenz, passive Regeneration, Schattenfieber-Unterdrückung |
| **Schatten** | Schattennervensystem | Schattensinne, Fähigkeiten, Wahrnehmung | NUR ab Infektionsstufe 1+; siehe Schattenfieber-System |

### 3.3 Trainer-System
- Fähigkeiten werden bei NPCs in der Welt gelernt, NICHT im Menu geklickt
- Jede Fraktion hat EXKLUSIVE Trainer (für bestimmte Fähigkeiten/Waffenstile)
- Trainer verlangen: Geld + Ruf + Vorbedingung (z.B. "Zeig mir, dass du parieren kannst")
- Gothic-Referenz: Die Welt ist das Klassenzimmer

### 3.4 Perks/Fähigkeiten-Prinzip
- TRANSFORMATIV, nicht numerisch — Perks verändern WIE man spielt, nicht nur Zahlenwerte
- Korrekt: "Du kannst jetzt im Sprint angreifen" / "Paraden reflektieren Projektile"
- Falsch: "+20% Schwertschaden" / "+50 HP"
- Numerische Steigerungen kommen durch die Ast-Investition selbst, nicht durch einzelne Perks

## 4. Alchemie und Crafting

### 4.1 Design-Philosophie
- Alchemie ersetzt Magie — es ist das primäre "übernatürliche" Werkzeug für Stufe-0-Spieler
- Wenige, bedeutsame Rezepte statt endloser Crafting-Listen
- Zutaten-Beschaffung als Explorations-Motivation
- Crafting ist NICHT endlos wiederholbar (begrenzte Zutaten, keine Respawn-Pflanzen)
- **Biotech-Forschung IST gefährlich** (CD-bestätigt): Alchemie ist nicht sicher. Experimente können schiefgehen, Nebenwirkungen sind real. Das ist keine Bestrafungsmechanik, sondern Weltkonsequenz — in einer Welt, die auf einem toten Urwesen gebaut ist, ist jeder Eingriff in die Biologie ein Risiko.

### 4.2 Produktkategorien

| Kategorie | Funktion | Beispiele |
|-----------|----------|-----------|
| **Heilung** | HP-Wiederherstellung, Regeneration | Heiltrank (sofort), Regenerationstinktur (über Zeit) |
| **Combat-Buffs** | Temporäre Kampfverstärkung | Waffenöle (Elementarschaden), Reflexelixier (Parry-Window +), Stärketrank |
| **Schattenfieber-Kontrolle** | Infektionswert beeinflussen | Suppressiva (senkt Wert), Stabilisatoren (verhindert Anstieg temporär), Booster (erhöht Wert bewusst für Fähigkeits-Burst) |
| **Gifte** | Offensiv, Waffen-Applikation | Lähmendes Gift (Ausdauer-Entzug), Nervenagent (Wahrnehmungsstoerung beim Feind), Kontaktgift (Falle) |
| **Utility** | Exploration, Überleben | Nachtsicht-Tinktur, Atem-Verlängerer (Unterwasser), Klettergrip (verbesserte Haftung) |
| **Schutz** (neu) | Anti-Infektions-Präparate | Schattenresistenz-Öl (temporärer Schutz in verseuchten Zonen), Immunbooster (Infektionsanstieg halbiert für X Minuten) |

Die neue Kategorie "Schutz" ist ein direktes Ergebnis von Bedingung 3 (kein versehentliches Infizieren). Stufe-0-Spieler brauchen taktische Werkzeuge, um infektionsgefährliche Gebiete und Kämpfe zu bestreiten, OHNE sich zu infizieren. Das macht Alchemie für reine Spieler genauso wertvoll wie Schattenfieber-Fähigkeiten für infizierte Spieler.

### 4.3 Herstellungsprozess
- Zutaten finden (Exploration, Handel, Beute)
- Rezepte lernen (Trainer-Prinzip: Alchemisten-NPCs, Lore-Fragmente, Experiment)
- Herstellung an Alchemie-Stationen (feste Orte in der Welt, NICHT tragbar)
- Qualitätsstufen: Basis → Verbessert → Meister (abhängig von Lymph-Ast und Trainer-Rang)

### 4.4 Schnittstelle zu anderen Systemen
- **Lymph-Ast:** Bestimmt Trank-Wirkung und verfügbare Rezepte
- **Schattenfieber:** Suppressiva als wichtigste Produktkategorie; hoher Infektionswert = schwächere Alchemie-Wirkung (Trade-Off!)
- **Combat:** Waffenöle und Gifte als taktische Vorbereitung vor Kämpfen
- **Fraktionen:** Exklusive Rezepte pro Fraktion (Orden: Reinigungsmittel, Gilden: Handelsgifte, Krone: Militärtränke)
- **Stufe-0-Spielpfad:** Schutz-Kategorie als mechanisches Äquivalent zu Schattenfieber-Resistenz (QA-validiert)

## 5. Exploration und Weltnavigation

### 5.1 Weltstruktur
- Semi-Open-World: Eine zusammenhängende Kernregion (~4-6 km²)
- Gothic-Dichte: Wenig Leerraum, hohe POI-Dichte, handplatziert
- Keine Schnellreise (oder: spät freischaltbar, als Luxus, nicht als Notwendigkeit)
- Zusammenhängende Oberwelt ohne Ladebildschirme

### 5.2 Vertikalität
- Städte: Begehbare Dachlandschaften, Keller, Kanalisation, Brücken, Turmebenen
- Wildnis: Klippen, Höhlen, Baumkronen, Flussbetten, Bergpässe
- Immer mehrere Wege: Hauptweg (sicher, lang), Schleichweg (riskant, kurz), Vertikalweg (Geschick erforderlich)
- Dishonored-Prinzip: Der Raum hat drei Dimensionen

### 5.3 Belohnungsstruktur
- Neugier wird IMMER belohnt: Abseits der Wege = Alchemie-Zutaten, Lore-Fragmente, versteckte NPCs, Schattenfieber-Hotspots
- Keine Quest-Marker auf der Karte (oder: minimal, abschaltbar) — Beschreibungen, Sightlines, NPC-Hinweise
- Umweltpuzzles: Kombination aus Beobachtung, Alchemie und Schattensinnen
- Handplatzierte Schätze mit narrativer Einbettung (Warum liegt das hier? Wer hat es versteckt?)

### 5.4 Sichtbarkeitsschichten (Schattenfieber-Integration)
- Stufe 0: Normale Wahrnehmung — Geheimtüren und Fallen nur durch genaues Hinsehen findbar
- Stufe 1+: Schattensinne enthüllen versteckte Objekte, Geheimgänge, vergiftete Gegenstände
- Stufe 2+: Emotionsauren an NPCs, Tiefensicht für Schatzsuche
- Die Welt hat ZWEI Schichten — und Schattenfieber zeigt die zweite
- **Stufe-0-Alternative**: Alchemie (Nachtsicht-Tinktur), genaue Beobachtung, NPC-Hinweise — andere Methode, gleicher Inhalt (QA-validiert)

### 5.5 Points of Interest (Typen)

| Typ | Beispiele | Belohnung |
|-----|----------|-----------|
| **Siedlungen** | Städte, Dörfer, Einzelhöfe | NPCs, Quests, Trainer, Handel |
| **Dungeons** | Katakomben, Minen, Ruinen, Ordensfestungen | Ausrüstung, Lore, Boss-Gegner |
| **Schattenfieber-Zonen** | Verseuchte Gebiete, Ritualstätten | Infektionsrisiko (mit Vorwarnung!), seltene Alchemie-Zutaten, Lore |
| **Landmarken** | Aussichtspunkte, Statuen, Ruinen | Kartenenthülllung, Orientierung, Lore |
| **Verstecke** | Schmugglerlager, Diebesverstecke, Tiervolk-Lager | Handel (Schwarzmarkt), Quests, Alchemie |

## 6. Querschnittsthemen

### 6.1 Namenssysteme


- Fraktionen, Orte, Charaktere und Artefakte tragen eigene Namen, die zur Welt gehören
- Germanische Mythologie ist INSPIRATION, nicht Vorlage für die Nomenklatur
- Emres WBB-01 nutzt nordische Begriffe (Emer, Ginnungagap, etc.) als Arbeitsbegriffe — diese müssen VOR der V1-Produktion durch RELICS-eigene Namen ersetzt werden
- **Auswirkung auf GDD-02**: Stufennamen ("Rein", "Gezeichnet", "Infiziert", "Verwandelt", "Entfesselt") sind Arbeitsnamen und müssen geprüft werden — passen sie zum eigenen Namenssystem?
- **Zuständig**: Emre (Namenssystem-Framework) + Nami (Charakternamen) + Darius (Systemnamen)

### 6.2 Build-Archetypen (emergent, nicht vordefiniert)

| Build | Schattenfieber | Schwerpunkte | Spielstil |
|-------|---------------|-------------|-----------|
| Reiner Krieger | Stufe 0 | Muskel + Cardio | Schwere Waffen, Ausdauer, volles Parry |
| Alchemist | Stufe 0-1 | Lymph + Cardio | Trank-fokussiert, Gifte, Buff-Öle, Schutz-Präparate |
| Schattenspäther | Stufe 1-2 | Schatten + Cardio | Exploration, Stealth, Schatten-Schritt |
| Hybrid-Kämpfer | Stufe 2-3 | Muskel + Schatten | Risk/Reward, explosive Spitzen |
| Schattenbestie | Stufe 3-4 | Schatten (voll) | Glass Cannon, sozialer Aussenseiter, Parallel-Narrativ |

### 6.3 System-Interaktionen

```
COMBAT <-> SCHATTENFIEBER
  Schattenreflex erweitert Parry
  Fieber-Puls als Aö (kostet HP)
  Infizierte Feinde = Vorschau eigener Fähigkeiten
  Schutz-Alchemie als Stufe-0-Alternative (QA)

SCHATTENFIEBER <-> NERVENSYSTEM
  Vierter Ast konkurriert um Leveling-Punkte
  Hohe Infektion = schwache konventionelle Äste
  Spezialisierung vs. Breite

ALCHEMIE <-> SCHATTENFIEBER
  Suppressiva senken Infektionswert
  Booster erhöhen ihn bewusst
  Schutz-Präparate verhindern Anstieg (Stufe-0-Werkzeug)
  Lymph-Ast bestimmt Alchemie-Effizienz

EXPLORATION <-> SCHATTENFIEBER
  Verseuchte Zonen erhöhen Infektion (MIT Vorwarnung)
  Schattensinne enthüllen versteckte Inhalte
  Stufe-0-Alternative: Alchemie + Beobachtung
  Exploration belohnt mit Alchemie-Zutaten

FRAKTIONEN <-> SCHATTENFIEBER
  Infektionsstufe beeinflusst Fraktionszugang
  Exklusive Trainer/Rezepte pro Fraktion
  Orden bietet Reinigung, jagt aber ab Stufe 3

NARRATIV <-> SCHATTENFIEBER (Nami-Sync)
  Rauschen: Subtile Textverschiebungen (Stufe 1-2)
  Risse: Alternative Dialoge, fragwürdige Questgeber (Stufe 3)
  Schwelle: Parallel-Narrativ, unentscheidbare Realität (Stufe 4)
  Schattenfieber-Dialoge sind spielbar, nicht nur atmosphärisch
```

### 6.4 Balancing-Leitlinien
- Stufe 0 = gleichwertig zu Stufe 4 — ANDERE Erfahrung, nicht schlechtere
- Keine "Best Build"-Situation — Trade-Offs müssen echt sein
- Die Welt-Schwierigkeit wird durch Geographie bestimmt, nicht durch Slider
- Vertikaler Fortschritt (mächtig werden) UND horizontaler Fortschritt (anders werden)
- Stufe-0-Äquivalent-Tabelle (2.5) als Balancing-Grundlage
- QA-Schleife: Leo prüft jede Mechanik aus Spielersicht — 40% Fokus auf Schattenfieber

### 6.5 QA-Risikomatrix (Leo-Input)

| Risiko | Schwere | Wahrscheinlichkeit | Mitigation |
|--------|---------|---------------------|------------|
| Versehentliche Infektion | KRITISCH | Hoch (ohne Massnahmen) | Bedingung 3 + Schutz-Alchemie + UI-Warnungen |
| Stufe 0 fühlt sich leer an | HOCH | Mittel | Stufe-0-Äquivalente, exklusive Alchemie-Inhalte |
| Stufenübergänge fühlbar machen | HOCH | Hoch | Gradueller Übergang, QA pro Infektionswert |
| Kontrollverlust frustriert statt fasziniert | MITTEL | Mittel | Transparenz, Spieler muss Konsequenz vorher verstehen |
| Community-Backlash "nicht heilbar" | MITTEL | Sicher | Transparente Kommunikation VOR Release, "kontrollierbar" als Frame |
| Schattenfieber-Dialoge brechen Quests | HOCH | Hoch | Systematisches Testing aller Quest-States x Infektionsstufen |

---

\clearpage

# GDD-03 — Erzählkonzept


---

## 1. Narrative Prinzipien

Die folgenden vier Prinzipien sind keine Empfehlungen. Sie sind Gesetze. Jede Quest, jeder Dialog, jede Cutscene, jeder Umgebungstext in RELICS muss gegen mindestens eines dieser Prinzipien validierbar sein. Wenn ein narrativer Inhalt gegen ein Prinzip verstoesst, wird er überarbeitet oder gestrichen. Es gibt keine Ausnahmen, und es gibt keine Szene, die zu klein ist, um geprüft zu werden.

### 1.1 Fremder als Zustand

Der Spieler ist kein Held mit Amnesie. Er ist kein Auserwählter, der seine Bestimmung noch nicht kennt. Er ist kein Söldner mit dunkler Vergangenheit. Er ist ein Niemand — und das ist sein stärkstes Werkzeug.

Fremdheit ist in RELICS kein narratives Problem, das im Laufe der Geschichte gelöst wird. Sie ist der Aggregatzustand der gesamten Spielerfahrung. Der Spieler beginnt als Fremder und er endet als Fremder — auch wenn sich die Form seiner Fremdheit verändert hat. Wer einer Fraktion beitritt, hört nicht auf, fremd zu sein. Er tauscht eine Art der Fremdheit gegen eine andere: die Fremdheit des Aussenseiters gegen die Fremdheit dessen, der dazugehört und trotzdem nicht ganz passt. Wer die Lebende Krone berührt, wird nicht einheimischer — er wird fremder, auf eine Art, die tiefer reicht als Geografie.

Dieses Prinzip hat eine konkrete Design-Konsequenz: Kein NPC in RELICS erklärt dem Spieler die Welt, als wäre er ein Tourist. NPCs leben in ihrer Welt. Sie setzen voraus, was jeder weiss. Sie erwähnen beiläufig, was für sie selbstverständlich ist. Der Spieler muss zuhören, beobachten, kombinieren. Die Welt schuldet ihm keine Exposition — er muss sich das Verständnis verdienen, so wie er sich Zugang zu Fraktionen, Trainern und Gebieten verdienen muss.

**Validierungstest:** Gibt es in dieser Szene einen Moment, in dem ein NPC dem Spieler etwas erklärt, das er einem Einheimischen nie erklären würde? Dann überarbeiten.

### 1.2 Fraktionen als Sprachen

In RELICS haben die drei Fraktionen nicht nur unterschiedliche Ziele. Sie haben unterschiedliche Wörter für dieselben Dinge. Die Krone nennt die kosmologische Erosion "die Faulung" und meint damit Strafe. Die Gilden nennen sie "den Schwund" und meinen damit Verlust. Der Orden nennt sie "die Entflechtung" und meint damit ein Geheimnis. Dasselbe Phänomen, drei Vokabulare, drei Weltsichten, die sich nicht auf einen gemeinsamen Nenner bringen lassen — weil der gemeinsame Nenner voraussetzen würde, dass eine der drei Perspektiven objektiv ist, und das ist keine von ihnen.

Fraktionszugehörigkeit verändert in RELICS nicht primär, was der Spieler SAGEN kann. Sie verändert, was er ZU HÖREN BEKOMMT. Ein Krone-alliierter Spieler erhält Informationen in der Sprache der Krone — in ihren Metaphern, mit ihren Auslassungen, nach ihren Prioritäten. Ein Gilden-alliierter Spieler erhält dieselben Informationen anders gerahmt, mit anderen Betonungen, mit anderen blinden Flecken. Der Spieler, der RELICS zweimal spielt — einmal als Krone, einmal als Orden — erlebt nicht zwei verschiedene Geschichten. Er erlebt dieselbe Geschichte in zwei verschiedenen Sprachen und begreift erst durch den Vergleich, was in beiden Versionen fehlte.

Emres WBB-01 liefert das kosmologische Fundament für dieses Prinzip. Die Schöpfungsgeschichte des Emer existiert in drei Versionen, und keine ist falsch. Die Krone singt von Sigvalts Pflicht-Opfer, die Gilden schreiben von Erthags Investition, der Orden verschlüsselt Halvards Erkenntnis. Der Spieler wird im Laufe des Spiels alle drei Versionen hören — und muss selbst entscheiden, ob er eine glaubt, alle drei zusammenfügt oder keine von ihnen für bare Münze nimmt.

**Validierungstest:** Könnte dieselbe Information, die in dieser Szene vermittelt wird, von einer anderen Fraktion völlig anders präsentiert werden — mit anderem Vokabular, anderer Betonung, anderen Auslassungen? Wenn nicht, ist sie fraktionsneutral und muss geprüft werden, ob das beabsichtigt ist.

### 1.3 Räume als Erzähler

Der beste Expositions-NPC in RELICS ist kein NPC. Es ist ein leerer Thronsaal, in dem noch Blut auf dem Boden steht. Ein verlassener Marktplatz, auf dem die Waagen noch hängen. Ein Ordensarchiv, in dem jemand systematisch Seiten aus Kodizes gerissen hat.

Environmental Storytelling ist in RELICS kein Bonus, kein Easter Egg, kein Nice-to-Have. Es ist der primäre Erzählkanal für Weltgeschichte. Die Vergangenheit wird nicht erzählt — sie wird hinterlassen. Was geschehen ist, steht nicht in Büchern (obwohl es auch dort steht), sondern in der Anordnung von Gegenständen, in der Architektur von Gebäuden, in den Rissen in den Wänden und den Flecken auf den Böden. Der Spieler, der genau hinsieht, versteht mehr als der Spieler, der nur Dialoge abklappert. Beide Spielweisen sind gültig — aber die Umgebung belohnt Aufmerksamkeit auf eine Art, die kein Dialogbaum bieten kann.

Dieses Prinzip erfordert enge Abstimmung mit Vera (Art Direction) und Emre (Topos). Jeder Raum braucht eine Erzählabsicht — nicht jeder Raum muss eine Geschichte erzählen, aber kein Raum darf zufällig aussehen. Auch Leere ist eine Aussage, wenn sie gestaltet ist.

**Validierungstest:** Könnte der Spieler diese Szene verstehen, wenn er alle Dialoge überspringt und nur die Umgebung beobachtet? Wenn nicht: Fehlt dem Raum etwas, oder ist der Dialog eine Krücke?

### 1.4 Schattenfieber als Unreliable Narrator

Das Schattenfieber verändert nicht nur den Körper des Spielers und nicht nur seine mechanischen Fähigkeiten. Es verändert die Erzählung selbst. Was der Spieler sieht und hört, ist ab einem bestimmten Infektionsgrad nicht mehr zuverlässig — und das Spiel sagt ihm nicht, wann dieser Punkt erreicht ist.

Das ist kein Bug. Das ist kein unfairer Design-Trick. Das ist der Kern der narrativen Erfahrung von RELICS.

Ein Spieler mit hohem Schattenfieber erlebt eine andere Geschichte als ein Spieler ohne. Er sieht Dinge, die der andere nicht sieht. Er hört Sätze, die der andere nicht hört. Er führt Gespräche mit Figuren, die möglicherweise nicht existieren — oder die existieren, aber anders reden, als der saubere Spieler es erlebt. Die Frage, welche Version die "wahre" ist, ist eine Frage, die RELICS nicht beantwortet. Möglicherweise ist die Version des infizierten Spielers näher an der kosmologischen Realität — an dem, was hinter den Hauten liegt. Möglicherweise ist sie reine Halluzination. Möglicherweise beides.

Dieses Prinzip ist gleichzeitig der grösste narrative Reiz und das grösste Design-Risiko von RELICS. Es funktioniert nur, wenn die Schattenfieber-Varianten SPIELBAR sind — wenn sie nicht nur atmosphärisches Rauschen erzeugen, sondern mechanisch relevante Informationen liefern, die zu echten Spielerentscheidungen führen. Schattenfieber-Dialoge dürfen keine Sackgassen sein. Sie müssen alternative Wege öffnen, die nur dem infizierten Spieler zugänglich sind — genauso, wie die "saubere" Version Wege öffnet, die dem Infizierten verschlossen bleiben.

**Validierungstest:** Ist jede Schattenfieber-Dialogvariante mechanisch relevant — führt sie zu einer Spielerentscheidung, einer Information, einem Zugang, der sonst fehlt? Wenn sie nur atmosphärisch ist, reicht das nicht.

---

## 2. Erzählrahmen

### 2.1 Prämisse

In einem Mittelgrund am Rande der Faulung ringt ein Fremder um seinen Platz in einer Welt, die ihm keinen schuldet.

Das Relikt dieser Iteration — die Lebende Krone — ist das Objekt, um das die Handlung kreist. Die Krone ist kein MacGuffin. Sie ist kein Schatz, den man am Ende aufhebt und den Abspann sieht. Die Lebende Krone ist ein Organismus, der mit seinem Träger verschmilzt, die Hauten zwischen den Daseinsebenen stabilisiert und jeden, der sie berührt, fundamental verändert. Sie ist Machtsymbol, kosmologisches Werkzeug und Fluch zugleich — und jede Fraktion sieht nur den Aspekt, der zu ihrer Weltsicht passt.

Die zentrale Frage der Hauptquest lautet nicht: Wer bekommt die Krone? Sie lautet: Was geschieht mit dem, der sie trägt — und was geschieht mit der Welt, wenn niemand sie trägt?

### 2.2 Drei-Akt-Struktur

#### Akt I — Ankunft (ca. 20% Spielzeit)

Der Spieler kommt als Fremder in den Mittelgrund. Ohne Namen, ohne Ruf, ohne Verbindungen. Er hat nicht einmal einen klaren Grund, hier zu sein — jedenfalls keinen, den er kennt.

**Beat 1 — Gastrecht.** Die erste Stunde ist ein Gastrecht-Szenario. Der Spieler wird aufgenommen — misstrauisch, widerwillig, aber aufgenommen, denn das Gastrecht ist in dieser Welt keine Höflichkeit, sondern eine kosmologische Verpflichtung. Wo Gastrecht gebrochen wird, werden die Hauten dünner — Aberglaube, sagen die Gilden. Wahrheit, flüstert der Orden. Die Gastrecht-Sequenz dient als narratives Tutorial: Der Spieler lernt, dass Worte in dieser Welt Gewicht haben, dass Versprechen Konsequenzen haben, und dass jede der drei Fraktionen unter "Gastfreundschaft" etwas anderes versteht. Kein UI-Popup erklärt ihm das. Er erlebt es.

**Beat 2 — Die drei Stimmen.** Im Verlauf von Akt I begegnet der Spieler allen drei Fraktionen in ihrem natürlichen Kontext. Keine Rekrutierungsszenen, keine Fraktions-Expo. Stattdessen: Ein Krone-Soldat, der eine Strasse bewacht und den Spieler passieren lässt — oder nicht, je nachdem, wie er sich im Gastrecht-Szenario verhalten hat. Eine Gilden-Händlerin, die dem Spieler Arbeit anbietet — keine edle, eine dreckige. Ein Ordenspriester, der Infizierte segnet oder verbannt, je nach Stimmung und Laune seines Vorgesetzten. Der Spieler beobachtet, bewertet, wählt nicht — noch nicht.

**Beat 3 — Das erste Zeichen.** Am Ende von Akt I erlebt der Spieler den ersten Kontakt mit den Auswirkungen der Lebenden Krone. Nicht mit dem Artefakt selbst — das kommt später. Sondern mit dem, was es hinterlassen hat: Ein Ort, an dem die Hauten dünn sind. Ein NPC, der Dinge sieht, die nicht da sind — oder die nur ER sieht. Ein Stück Welt, das sich falsch anfühlt, das zu viel ist, das nicht ganz in den Mittelgrund passt. Der Spieler versteht noch nicht, was er gesehen hat. Aber er hat es gesehen, und das reicht.

*Akt-I-Ziel:* Der Spieler hat ein Gefühl für die Welt, ein grobes Verständnis der Fraktionsdynamik und eine Frage, die ihn in Akt II treibt: Was ist hier falsch?

#### Akt II — Verstrickung (ca. 50% Spielzeit)

Die längste Phase. Der Spieler wird hineingezogen — nicht als Auserwählter, sondern als Unbeteiligter, der zu viel gesehen hat. Das Schattenfieber wird narrativer Faktor. Die Fraktionen werden konkreter, dringlicher, fordernder. Die Lebende Krone tritt als Streitobjekt in die Handlung ein.

**Beat 4 — Fraktionspositionierung.** Der Spieler wird aufgefordert, sich zu positionieren. Nicht beitreten — noch nicht. Aber eine Fraktion unterstützen, einen Auftrag übernehmen, sich einem Lager zuordnen. Diese Positionierung öffnet Zugänge: neue NPCs, neue Orte, neue Informationen. Sie schliesst noch nichts — aber sie verschiebt die Gewichte.

**Beat 5 — Die Krone tritt ein.** Der Spieler erfährt, was die Lebende Krone ist — und dass alle drei Fraktionen sie wollen, aus völlig unterschiedlichen Gründen. Die Krone beansprucht sie als dynastisches Erbe: Wer die Krone trägt, hält die Welt zusammen. Die Gilden wollen sie kontrollieren: ein unbezahlbares Gut, das den Markt sprengt. Der Orden will sie studieren: ein Erkenntnisschlüssel, der alle Geheimnisse öffnen könnte. Der Spieler sieht, wie die Krone die letzten Träger verändert hat — die "nicht mehr ganz von dieser Art" waren, wie die vorsichtigen Chroniken es formulieren. Die Krone frass ihre Träger, sagen die direkteren.

**Beat 6 — Point of No Return.** Der Spieler muss sich einer Fraktion verpflichten. Oder er versucht, neutral zu bleiben — was möglich ist, aber Konsequenzen hat: Neutralität in einem Machtkampf ist keine neutrale Position. Alle drei Fraktionen behandeln den Neutralen als potenzielle Bedrohung, als jemanden, der sich nicht einordnen lässt. Das Tiervolk kennt diesen Zustand — sie sind es gewohnt, keiner Seite zu gehören. Ob der Spieler das als Freiheit oder als Isolation erlebt, hängt davon ab, wie er spielt.

**Beat 7 — Schattenfieber-Eskalation.** Wenn der Spieler infiziert ist, verändern sich ab hier Szenen. Dialoge verschieben sich. NPCs reagieren anders — nicht nur sozial (Angst, Mitleid, Abscheu), sondern informativ: Sie sagen andere Dinge, weil der infizierte Spieler andere Fragen stellt oder andere Antworten hört. Die Hauten werden dünner an bestimmten Orten, und der Spieler — wenn sein Infektionsgrad hoch genug ist — beginnt, die Schichten wahrzunehmen: Fragmente des Stillfelds, Echos des Hohlichts. Ob das real ist oder Halluzination, wird nicht geklärt.

*Akt-II-Ziel:* Der Spieler hat sich positioniert, die Krone als zentrales Objekt erkannt und verstanden, dass jede Lösung einen Preis hat, den keine Fraktion offen ausspricht.

#### Akt III — Konsequenz (ca. 30% Spielzeit)

Das Endspiel. Die Faulung beschleunigt sich. Die Hauten werden dünner. Die Frage ist nicht mehr, ob jemand die Krone tragen wird, sondern wer — und was danach von ihm übrig bleibt.

**Beat 8 — Die Krone erreichen.** Der Spieler gelangt — durch fraktionsspezifische Wege — an die Lebende Krone. Was er dort vorfindet, hängt von seinem Schattenfieber-Status ab. Ein sauberer Spieler sieht ein Artefakt in einem Thronsaal oder einer Krypta oder einem Labor. Ein infizierter Spieler sieht mehr — oder weniger: Die Krone ist lebendig, sie pulsiert, sie reagiert auf seine Nähe. Bei hoher Infektionsstufe verschwimmt die Grenze zwischen dem Objekt und dem Ort, der es beherbergt. Der Raum atmet. Die Wände erinnern sich.

**Beat 9 — Entscheidung.** Der Spieler steht vor der zentralen Entscheidung. Sie ist fraktionsspezifisch und schattenfieberspezifisch — die Kombination aus beidem erzeugt die Varianz.

Die Krone-Route fragt: Trägst du die Krone, um die Ordnung zu bewahren — obwohl du weisst, was sie mit ihren Trägern macht? Ist Pflicht mehr wert als dein Selbst?

Die Gilden-Route fragt: Kontrollierst du die Krone, ohne sie zu tragen — als Ressource, als Instrument, als Ware? Und was passiert mit der Welt, wenn niemand sie trägt und die Hauten weiter dünner werden?

Die Orden-Route fragt: Studierst du die Krone, öffnest du die Erkenntnis — und riskierst du dabei, das zu entfesseln, was die Flechtung einst gebunden hat?

Die neutrale Route fragt: Lässt du die Krone, wo sie ist? Und kannst du mit der Antwort leben, dass du die Welt ihrem Schicksal überlassen hast?

**Beat 10 — Konsequenz.** Die Folgen der Entscheidung sind nicht als Cutscene erzählt, sondern spielbar. Der Spieler erlebt — in einer finalen Sequenz, die je nach Fraktionswahl und Infektionsgrad variiert — was seine Entscheidung bedeutet. Kein Erzähler fasst zusammen. Kein Textcrawl erklärt, was danach geschah. Der Spieler sieht es selbst — so gut er sehen kann. Und wenn sein Schattenfieber hoch genug ist, sieht er möglicherweise mehr als das, was wirklich passiert. Oder weniger. Oder beides.

*Akt-III-Ziel:* Der Spieler hat eine Entscheidung getroffen, deren Konsequenzen er spürt, aber nicht vollständig überschaut. Er hat das Gefühl, dass ein zweiter Durchgang — mit einer anderen Fraktion, einem anderen Infektionsgrad — eine andere Wahrheit zeigen würde.

### 2.3 Erzählton

Drei Regeln für den Ton von RELICS:

**Knapp, nie expositiv.** NPCs erklären die Welt nicht — sie leben darin. Kein Charakter hält einen Vortrag über die Geschichte der Grossen Flechtung. Stattdessen erwähnt eine Krone-Wache beiläufig "das Flechtfest", als wäre es Allgemeinwissen — und der Spieler muss selbst herausfinden, was damit gemeint ist.

**Poetisch, nie opulent.** Die Sprache darf Gewicht haben. Ein Satz darf schön sein. Aber jedes Wort muss verdient sein. Gotische Grandeur heisst nicht, dass NPCs in Metaphern schwimmen. Es heisst, dass die richtigen Wörter an den richtigen Stellen fallen — und dass Stille ebenso viel sagt wie Sprache.

**Politisch, nie neutral.** Jedes Gespräch in RELICS hat Subtext. Niemand sagt genau das, was er meint. Die Krone-Wache, die dem Spieler den Weg weist, weist ihm gleichzeitig seinen Platz zu. Die Gilden-Händlerin, die ihm einen fairen Preis macht, kalkuliert gleichzeitig seinen Nutzen. Der Ordenspriester, der ihm Wissen anbietet, prüft gleichzeitig seine Zuverlässigkeit. RELICS ist ein Spiel, in dem höfliche Gespräche gefährlicher sein können als offene Feindschaft.

---

## 3. Quest-Architektur

### 3.1 Grundregeln

**Regel 1: Kein Filler.** Es gibt keine Quests, die nur existieren, um eine Spielstrecke zu fuellen. Keine Fetch-Quests. Kein "Bring mir zehn Kräuterbeutel." Jede Quest muss mindestens eines der vier narrativen Prinzipien spürbar machen. Wenn eine Quest diesen Test nicht besteht, wird sie gestrichen — nicht überarbeitet, gestrichen.

**Regel 2: Kein Auserwählter.** Der Spieler wird in keine Quest als prophezeiter Held gerufen. Er stolpert hinein, wird hineingezogen, wird benutzt oder bittet sich selbst an. Das Motiv ist nie "Du bist der Einzige, der das kann." Das Motiv ist: "Du bist hier, du schuldest mir etwas, und ich sehe keinen besseren Kandidaten."

**Regel 3: Konsequenz über Auflösung.** Quests müssen kein gutes Ende haben. Sie müssen nicht einmal ein klares Ende haben. Was sie haben müssen, ist Konsequenz — das Gefühl, dass die Entscheidung des Spielers etwas verändert hat, das sich nicht zurücknehmen lässt. Der beste Ausgang einer Quest ist nicht der glücklichste, sondern der, den der Spieler vor sich selbst verantworten kann.

### 3.2 Intro-Sequenz / Tutorial Quest

**Titel:** Der Gast

**Funktion:** Der Spieler erlernt die Kernmechaniken DURCH eine narrative Situation. Kein UI-Tutorial, keine schwebenden Textboxen. Die Welt ist das Tutorial.

**Setting:** Der Spieler kommt als Fremder an — die Umstände seines Kommens bleiben vage, absichtlich. Er erreicht einen Grenzort: nicht die Hauptstadt, nicht das Zentrum, sondern die Peripherie, dort, wo Kontrolle dünner ist und Gastrecht noch etwas bedeutet.

**Narrativer Bogen:** Ein lokaler Wirt gewährt dem Spieler Gastrecht. Die Regeln des Gastrechts — Feuer, Nahrung, Schutz; dafür Rede und Gegenrede — werden nicht als Textbox erklärt, sondern als soziale Situation erlebt. Der Spieler muss antworten, sich verhalten, eine Haltung einnehmen. Ein Konflikt entsteht — ein kleiner, lokaler, dringender Konflikt, der die Fraktionsdynamik im Miniatur zeigt. Die Lösung des Konflikts lehrt Kampfbasis, Gesprächsführung und Umgebungsbeobachtung.

**Länge:** 15-20 Minuten.

**Prinzip-Validierung:** Fremder als Zustand. Räume als Erzähler.

### 3.3 Hauptquest — Die Lebende Krone (Beat-Sheet V2)

**Struktur:** Drei Akte, zehn Beats. Die Beats sind nicht streng linear — manche können in variabler Reihenfolge absolviert werden, manche sind fraktionsspezifisch, manche verändern sich mit dem Schattenfieber-Status. Zwei harte Verzweigungspunkte: Beat 6 (Fraktionsverpflichtung) und Beat 9 (Entscheidung). Dazwischen weiche Varianz.

| Beat | Akt | Titel | Beschreibung (V2 — Szenenebene) | SF-Varianz |
|------|-----|-------|--------------------------------|------------|
| 1 | I | **Gastrecht** | Ankunft am Grenzort. Ein Wirt prüft den Spieler — nach Gastrechts-Formel, aber mit Krone-Beauftragten im Rücken. Der Spieler muss entscheiden: Wahrheit oder Rolle. Erste Mechanik-Exposition. | Keine |
| 2 | I | **Die drei Stimmen** | Drei kurze, nicht-ausdehnbare Begegnungen: (a) Krone-Sergeant, der eine Strasse sperrt; (b) Gildenhilfsarbeiter, der Informationen verkauft; (c) Ordenspriester, der einen Infizierten in der Menge beobachtet. Spieler beobachtet, entscheidet nichts. | Keine |
| 3 | I | **Das erste Zeichen** | Ein Ort am Stadtrand — ein aufgegebenes Gehöfte mit dünnen Hauten. Kein Questgeber, kein Marker. Der Spieler findet es durch Neugier oder durch den Seher Maret, der ihn hinführt. Die Erfahrung ist uninterpretierbar. Sie bleibt. | Keine direkte — Maret ist auch ohne SF erreichbar |
| 4 | II | **Fraktionsannährung** | Erste Auftrag-Szene für eine Fraktion (Spielerwahl). Auftrag ist klein, dreckig, konsequent: Der Spieler macht sich nützlich. Ein zweiter NPC beobachtet. Er wird später wichtig. | SF-Stufe 1+: Umgebungshinweise verschieben sich, ein Satz im Briefing ist leicht anders |
| 5 | II | **Die Krone tritt ein** | Spieler erfährt vom Artefakt. Nicht durch Exposition — durch eine Konsequenz: Jemand, der die Krone berührt hat, ist gerade dabei, damit umzugehen. Was von ihm übrig ist, sieht der Spieler. Was die Fraktionen dazu sagen, lernt er durch drei kurze Reaktions-Szenen. | SF-Stufe 1+: Schattensinne zeigen, was andere nicht sehen: Der betroffene NPC ist nicht ganz weg. Er ist noch hier — in einer anderen Schicht |
| 6 | II | **Point of No Return** | Fraktionsverpflichtung oder bewusste Neutralität. Szene: Ein Rat der drei Fraktionen fordert den Spieler auf, Position zu beziehen. Nicht mit Worten — mit einer Handlung, die nicht zurückgenommen werden kann. | SF-Stufe 2+: Der Spieler hört einen vierten Satz im Rat, den niemand gesprochen hat |
| 7 | II | **Die Suche** | Fraktionsspezifischer Questpfad zur Krone. Drei verschiedene Wege (Krone: durch Archiv-Zugang; Gilden: durch Händlernetz; Orden: durch Schattenfieber-Kartierung). Jeder Weg zeigt andere Seite desselben Artefakts. | SF-Stufe 3+: Alternative Questgeber auf dem Weg — fragwürdige Figuren, die nur der Infizierte sieht |
| 8 | III | **Die Krone erreichen** | Spieler steht vor dem Artefakt. Der Ort ist je nach Fraktionsweg verschieden. Die Krone reagiert auf die Nähe des Spielers — leise, fast unmerklich für einen sauberen Spieler, überwältigend für einen infizierten. | SF-Stufe 3+: Der Raum erinnert sich. Die Wände zeigen Echos vergangener Träger |
| 9 | III | **Entscheidung** | Vier Wege (Krone/Gilden/Orden/neutral), ausformuliert in Abschnitt 2.2. Keine Option ist eindeutig richtig. Jede hat einen Preis, den die Fraktion nicht kommuniziert hat. | SF-Stufe 4: Parallel-Narrativ. Der Spieler weiss nicht sicher, welche Entscheidung er getroffen hat |
| 10 | III | **Konsequenz** | Spielbare Folge-Sequenz, ca. 10-15 Minuten. Kein Textcrawl. Der Spieler sieht das Ergebnis durch eigene Augen — so klar oder so verzerrt, wie seine Infektion es erlaubt. | SF-Stufe 4: Das Ende ist eine andere Geschichte |

### 3.4 Fraktionsquests (V2 — konkrete Beats)

Jede Fraktionsquest hat ein zentrales Dilemma, das die Fraktion in sich spaltet. Die Quest führt den Spieler in die Fraktion HINEIN, in ihre Risse, in ihre Widersprüche, in das, was sie sich selbst nicht eingestehen will.

#### Die Krone — "Pflicht und Verfall"

**Schlüssfigur:** Aldine Vor, Kronenführerin (→ GDD-04)
**Thema:** Loyalität gegenüber einer sterbenden Ordnung.
**Ton:** Elegisch. Formell. Die Sprache der Pflicht, die sich selbst überlebt hat.
**Kern-Dilemma:** Die Krone weiss — tief in sich, an den Stellen, die sie nicht anschaut —, dass die alte Ordnung nicht zurückkommt. Die letzten Träger der Lebenden Krone waren verändert. Die Dynastie ist möglicherweise am Ende. Und die tragischste Ironie: Die Krone setzt Biotechnologie ein, die genau die Hauten destabilisiert, die die Lebende Krone stabilisieren soll. Sie untergreabt ihre eigene Grundlage, ohne es zu wissen.

| Beat | Titel | Szenenbeschreibung |
|------|-------|--------------------|
| 1 | **Dienst** | Spieler beweist sich als brauchbar — kein Titel, keine Ehre, nur Funktion. Aldine Vor beobachtet ihn durch einen Bericht, nicht durch persönliche Begegnung. Sie entscheidet auf Basis von Nützlichkeit. |
| 2 | **Der innere Riss** | Spieler entdeckt, dass eine Krone-Einheit Biotech-Substanzen einsetzt, die die Faulung verstärken. Nicht absichtlich. Aus Unwissen. Oder aus Gleichgültigkeit. Der Offizier, den der Spieler befragt, weiss es nicht. Aldine Vor weiss es. Sie hat es priorisiert weggesehen. |
| 3 | **Der letzte Träger** | Spieler findet Spuren des letzten Krone-Trägers der Lebenden Krone. Was von ihm übrig ist, widerspricht der offiziellen Version. Aldine Vor weiss es. Sie hat ihn begraben lassen, ohne Zeremonie, ohne Bericht. |
| 4 | **Loyalität oder Einsicht** | Spieler muss entscheiden: Die Wahrheit verschweigen und die Krone-Fraktion stabil halten — oder sie aussprechen und die Fraktion in eine Krise stürzen, die möglicherweise der Beginn von etwas Besserem ist. Aldine Vor fragt ihn nicht danach. Sie setzt voraus, dass er schweigt. |

**Letzter Dialog — Aldine Vor, wenn der Spieler schweigt:**

> "Du hast es gesehen. Ich sehe, dass du es gesehen hast. Und du sagst nichts. Das ist die erste intelligente Entscheidung, die du in meinem Dienst getroffen hast."
> *(Pause)*
> "Die Ordnung hält nicht, weil sie stark ist. Sie hält, weil genug Menschen so tun, als ob."

**Letzter Dialog — Aldine Vor, wenn der Spieler die Wahrheit ausspricht:**

> "Du hast es gesagt. Ich höre es. Es verändert nichts. Es wird nichts verändern. Die Ordnung ist kein Glaube, der bricht, wenn man aufhört zu glauben. Sie ist eine Struktur, die hält, weil Strukturen hälten, bis sie es nicht mehr tun."
> *(Pause)*
> "Das ist kein Kommentar zu deiner Entscheidung. Es ist eine Feststellung. Ich werde nicht vergessen, dass du sie getroffen hast."

#### Die Gilden — "Der Preis aller Dinge"

**Schlüssfigur:** Cress, Gildenführer (→ GDD-04)
**Thema:** Freiheit durch Besitz — und der Punkt, an dem Freiheit in Gleichgültigkeit umschlägt.
**Ton:** Pragmatisch. Direkt. Bildreich. Die Sprache des Handels, die alles als Ware behandelt.
**Kern-Dilemma:** Die Gilden verstehen die Welt als Markt. Alles hat einen Preis, und wer den Preis kennt, hat Macht. Aber die Lebende Krone sprengt diese Logik — ein Gut ohne Preis durchbricht den Handel. Die Gilden reagieren, indem sie Wissen ÜBER die Krone handeln. Irgendwann muss jemand die Krone anfassen, und die Gilden wollen nicht derjenige sein — denn der Preis des Tragens ist der einzige Preis, den sie nicht kalkulieren können.

| Beat | Titel | Szenenbeschreibung |
|------|-------|--------------------|
| 1 | **Der dreckige Job** | Spieler erhält einen Auftrag, den kein Gildenmitglied offiziell ausführen darf. Der Auftrag ist legitim nach Gilden-Logik: Kein Risiko für die Gilde, klarer Preis für den Spieler. Der Spieler ist deniable. Das ist keine Beleidigung — es ist ein Angebot. |
| 2 | **Das unbezahlbare Gut** | Spieler gerät in den Informationshandel rund um die Krone. Er hat eine Information, die Cress will. Cress hat eine Information, die der Spieler braucht. Der Tausch ist fair. Die Frage ist, wessen Information gefährlicher ist. |
| 3 | **Der Preis des Wissens** | Spieler muss entscheiden, welche Information er weitergibt und an wen. Cress will das Wissen über den letzten Krone-Träger — um es zu verkaufen, an wen auch immer den höchsten Preis zahlt. Die Krone würde dafür zahlen. Und der Orden. Und andere. |
| 4 | **Gleichgültigkeit oder Opfer** | Spieler steht vor der Frage: Lässt er andere den Preis zahlen — das Dorf, die Infizierten, die Fremden, die keiner Fraktion gehören? Oder zahlt er selbst? Cress fragt das nicht explizit. Er macht ein Angebot. Und wartet. |

**Letzter Dialog — Cress, unabhängig von der Entscheidung:**

> "Du hast entschieden. Gut. Entscheidungen, die nicht stattfinden, sind kein Geschäft, sie sind Aufschub, und Aufschub kostet mehr als die Entscheidung selbst. Das weisst du jetzt."
> *(Kurze Pause)*
> "Ich respektiere, was du getan hast. Ich würde es nicht getan haben. Das ist kein Urteil — das ist eine Feststellung von Marktwert. Dein Marktwert ist gestiegen. Vielleicht nicht in der Währung, in der du denkst."

#### Der Orden — "Die Last des Wissens"

**Schlüssfigur:** Cassius, Ordensführer (→ GDD-04)
**Thema:** Wissen als Waffe und als Käfig.
**Ton:** Präzise. Künstlich ruhig. Nominalisierungen, unpersönliche Konstruktionen.
**Kern-Dilemma:** Der Orden versteht die kosmologische Wahrheit besser als jede andere Fraktion. Er ahnt den Zusammenhang zwischen Schattenfieber und Biotechnologie. Aber dieses Wissen nutzt er nicht zur Heilung — er nutzt es zur Kontrolle. Er bietet Reinigung an (gegen Loyalität). Er sammelt Tiervolk-Überlieferungen — und veröffentlicht sie nicht. Die Frage, die der Orden sich nicht stellt: Ab wann schützt man nicht mehr die Wahrheit, sondern nur noch die eigene Macht über die Wahrheit?

| Beat | Titel | Szenenbeschreibung |
|------|-------|--------------------|
| 1 | **Der Novize** | Spieler erhält Zugang zu den äusseren Kodizes — das, was der Orden zeigen darf. Cassius empfängt den Spieler nicht persönlich. Ein Untergebener. Cassius liest den Bericht danach und benotet den Spieler. Der Spieler weiss nicht, dass er geprüft wird. |
| 2 | **Das Verschlossene** | Spieler entdeckt, dass bestimmtes Wissen gesperrt ist — auch für ihn. Er findet Lücken in den Kodizes: herausgerissene Seiten, versiegelte Archive, Kammern, die existieren, aber nicht auf dem Grundriss stehen. Cassius bestätigt, dass das Wissen existiert. Er sagt nicht, warum es gesperrt ist. Er sagt: "Es gibt Informationen, deren Freigabe mehr schadete als nützte." |
| 3 | **Die Versuchung** | Spieler bekommt die Möglichkeit, die Lebende Krone zu studieren — was der Orden offiziell verbietet, inoffiziell duldet für vertrauenswuerdige Agenten. Die Studium-Szene zeigt dem Spieler mehr als er erwartet. Zu viel, vielleicht. Cassius war dabei, sagt nichts, notiert alles. |
| 4 | **Kontrolle oder Offenheit** | Spieler muss entscheiden: Wissen teilen (und die Kontrolle des Ordens brechen) oder Wissen hüten (und die Kontrolle legitimieren). Cassius fragt den Spieler danach — direkt, unverhüllt, das erste Mal ohne seinen theologischen Umweg. Es ist das einzige direkte Gespräch, das sie führen. |

**Letzter Dialog — Cassius, wenn der Spieler das Wissen teilt:**

> "Du hast es veröffentlicht. Ich hatte nicht gedacht, dass du es tun würdest."
> *(Lange Pause)*
> "Ich luge jetzt nicht, wenn ich sage: Ich bin nicht sicher, ob das ein Fehler war. Und die Tatsache, dass ich nicht sicher bin, ist selbst ein Datum, das ich nicht erwartet hatte."

**Letzter Dialog — Cassius, wenn der Spieler das Wissen hütet:**

> "Du hast gehütet. Das ist die Entscheidung, auf die hin ich dich ausgebildet habe."
> *(Pause)*
> "Ich sage dir jetzt etwas, das ich niemandem sage: Ich weiss nicht, ob es die richtige war. Das ist keine Schwäche. Das ist die Last, die mit dem Wissen kommt, das du nun trägst. Willkommen."

### 3.5 Städte-Quest

**Titel:** Mittelgrund

**Thema:** Die Kernstadt als Mikrokosmos — keine Krieg, aber die Vorbeben. Die Stadt funktioniert noch — gerade so.

**Format:** Verschachtelte Miniatur-Aufträge, die zusammen ein Bild ergeben. Kein einzelner Questgeber, kein linearer Strang. Stattdessen: Ein Händler, der Schutzgeld zahlt. Eine Wache, die wegsieht. Ein Priester, der Infizierte registriert — oder versteckt, je nachdem, wem man glaubt. Ein Tiervolk-Händler (→ GDD-04, Rho), der bestohlen wird und keine Klage einreichen kann, weil das Recht des Gastrechts nicht das Recht der Bürger ist.

Das Tiervolk ist in der Stadt als Nomaden, Händler und Diebe präsent — nicht als Handwerker, nicht als Bürger. Sie kennen den Status des Fremden aus eigener Erfahrung und spiegeln den Spieler: Du bist wie wir. Du gehörst nicht hierher. Und vielleicht ist das kein Nachteil.

**Prinzip-Validierung:** Fraktionen als Sprachen. Räume als Erzähler.

### 3.6 Charakter-Quest

**Titel:** Der Spiegel
**Figur:** Maret, der Seher (→ GDD-04)

*(V1-Placeholder geschlossen: Die Charakter-Quest-Figur war in V1 als [OFFEN] markiert. Sie ist jetzt Maret — der einzige NPC in RELICS, der das Schattenfieber in seiner finalen Form überlebt hat und auf der anderen Seite nicht wahnsinnig, aber kaputt in einer anderen Weise ist. Vollständiges Figurenprofil: GDD-04.)*

**Funktion:** Eine tiefe Beziehung zu einer Figur — nicht als Romanze, sondern als Spiegel des Spielers.

**Thema:** Maret sieht den Spieler als Mensch — nicht als Werkzeug, nicht als Bedrohung, nicht als Gelegenheit. Er fragt, warum der Spieler geblieben ist. Er hört die Antwort. Er hat selbst keine.

**Schattenfieber-Varianz:** Wenn der Spieler infiziert ist, verändert sich diese Beziehung fundamental. Nicht weil Maret den Spieler ablehnt — sondern weil die Wahrnehmung des Spielers die Beziehung verzerrt. Ab Stufe "Risse" hört der Spieler Dinge, die Maret nicht gesagt hat — oder die er gesagt hat, aber anders gemeint. Ab "Schwelle" weiss der Spieler nicht mehr, ob die Gespräche, die er mit Maret führt, tatsächlich stattfinden. Die Beziehung wird zur Frage: Kann man jemandem vertrauen, wenn man sich selbst nicht mehr trauen kann?

Und Maret, der selbst an der Grenze gelebt hat: Er weiss das. Er warnt nicht. Er hält die Hand hin.

**Prinzip-Validierung:** Fremder als Zustand. Schattenfieber als Unreliable Narrator.

### 3.7 Kleinere Seitenquests (3x)

#### Seitenquest 1 — "Rausch"

Ein NPC auf Schattenfieber-Stufe "Schwelle". Der Spieler trifft ihn an einem Ort, der nicht ganz real ist — oder der nur für den NPC nicht ganz real ist. Der NPC ist nicht feindlich. Er ist freundlich, hilfsbereit, eloquent. Er bietet dem Spieler Informationen an, die sich als wahr herausstellen — aber nur, wenn der Spieler selbst infiziert genug ist, um sie zu prüfen.

Die Frage der Quest: Ist das, was ein Wahnsinniger sieht, weniger wahr als das, was ein Gesunder sieht?

**Prinzip:** Schattenfieber als Unreliable Narrator.

#### Seitenquest 2 — "Gastrecht"

Ein Tiervolk-Händler wird bestohlen. Alle drei Fraktionen haben eine Version der Geschichte. Der Händler selbst sagt wenig — er fragt den Spieler, was das Gastrecht wert ist, wenn es nicht geschützt wird.

Die Frage der Quest: Wem glaubt man, wenn jede Version in sich logisch ist — und wenn die Wahrheit vielleicht in keiner von ihnen liegt?

**Prinzip:** Fraktionen als Sprachen. Fremder als Zustand.

#### Seitenquest 3 — "Stille"

Ein Ort ohne NPCs. Keine Dialoge. Keine Questgeber. Nur ein verlassener Hof und die Überreste einer Geschichte, die der Spieler aus Gegenständen und Architektur rekonstruieren muss. Was hier geschah, wird nie explizit ausgesprochen.

Die Quest hat keinen Abschluss im klassischen Sinne — sie ist abgeschlossen, wenn der Spieler versteht. Oder wenn er aufhört zu suchen.

**Prinzip:** Räume als Erzähler.

---

## 4. Dialogsystem

### 4.1 Grundstruktur

**Keine Moral-Achse.** Es gibt keine farbcodierten Antwortoptionen, keine Karma-Punkte, kein "Paragon/Renegade"-System. Der Spieler sieht Antworten, nicht Bewertungen. Was eine Antwort bedeutet, zeigt sich in der Reaktion der Welt — nicht in einer Statistik.

**Qualität über Quantität.** Zwei bis vier Antwortoptionen pro Dialogknoten. Nie mehr. Wenn eine Szene sechs Optionen braucht, ist die Szene zu breit und muss fokussiert werden. Jede Option muss sich anfühlen wie etwas, das ein Mensch tatsächlich sagen würde — nicht wie ein Gameplay-Hebel.

**Kein stummer Protagonist.** Der Spieler hat eine Stimme. Er spricht in Sätzen, nicht in Stichpunkten. Ob diese Sätze vertont werden, ist eine Scope-Frage (GDD-06), aber im Skript existieren sie vollständig. Der Spieler hat keine vordefinierte Persönlichkeit — aber er hat eine Sprache, die sich nach den Entscheidungen des Spielers formt.

**Kontextuelle Optionen.** Fraktionszugehörigkeit, Schattenfieber-Stufe und bisherige Entscheidungen schalten Optionen frei oder verändern ihren Wortlaut. Schattenfieber-Optionen sind nicht markiert — keine UI-Hinweise, kein Icon. Sie stehen neben normalen Optionen, als wären sie selbstverständlich. Der Spieler, der nicht weiss, dass es sie gibt, sieht sie nicht.

### 4.2 Fraktions-Register

#### Die Krone — Pflichtsprache

Formell, archaisch tendierend, häufiges Passiv. Die Krone spricht in Pflichten, nicht in Wünschen. "Es wurde angeordnet." "Es obliegt dem Fremden, sich auszuweisen." "Die Ordnung verlangt." Das Subjekt verschwindet oft hinter der Sache.

Die Krone nennt die kosmologische Erosion "die Faulung" und meint damit Strafe. Sie spricht vom "Flechtfest", als wäre es gestern gewesen. Sie erwähnt Sigvalt wie einen Grossvater, der noch im Nebenzimmer sitzt.

Ihr blinder Fleck: Die Krone redet nie über den Widerspruch zwischen ihrem Ordnungsanspruch und ihrem Biotech-Einsatz.

**Beispiel — Aldine Vor, erstes Gespräch:**

> "Ihr Anliegen ist registriert. Die Entscheidung über seine Berechtigung obliegt dem Verfahren. Das Verfahren dauert drei Tage. Wenn die Ordnung Eure Anwesenheit erfordert, werdet Ihr benachrichtigt. Wenn nicht, habt Ihr drei Tage, Eure Angelegenheiten anderweitig zu regeln."

#### Die Gilden — Wertsprache

Direkt, bildreich, durchsetzt von Sprichwörtern und Handelsmetaphern. Die Gilden reden in Preisen, Renditen und Bilanzen — auch über Dinge, die keine Waren sind. "Was kostet dich das?" ist keine Frage nach Geld.

Die Gilden nennen die Welt "den Tharm" — die Eingeweide. Die kosmologische Erosion ist für sie "der Schwund" — ein Verlust, der kalkuliert werden kann.

Ihr blinder Fleck: Die Gilden können nicht denken, was kein Preis hat.

**Beispiel — Cress, Erstbegegnung:**

> "Du fragst nach dem Händler. Das ist bemerkenswert direkt. Direktheit ist eine Qualität, die ich schätze — in der richtigen Dosierung. Die Dosierung hier ist: angemessen. Also: Ich kenne den Händler. Ich kenne, was er weiss. Ich kenne, was das wert ist. Die Frage ist, was du weisst und was das für mich wert wäre. Das ist keine rhetorische Frage."

#### Der Orden — Wissenssprache

Präzise, künstlich ruhig, dominiert von Nominalisierungen und unpersönlichen Konstruktionen. Der Orden verschlüsselt nicht durch Lüge, sondern durch Auslassung — er sagt nie etwas Falsches, aber er sagt selten alles.

Der Orden nennt die kosmologische Erosion "die Entflechtung" — ein Prozess, der verstanden werden muss, nicht gefürchtet.

Sein blinder Fleck: Der Orden verwechselt Verstehen mit Kontrolle.

**Beispiel — Cassius, mittenin einem Gespräch (V2-Ergänzung):**

> "Die Frage, die du stellen wolltest, lautet: Warum habt ihr das verborgen. Das ist eine korrekte Frage. Die Antwort lautet: Nicht weil es falsch ist, was dort steht. Sondern weil die Konsequenz seiner Bekanntheit schädlicher wäre als die Konsequenz seiner Verborgenheit. Das ist eine Kalkulation, keine Zuneigung zur Unwahrheit. Ich hoffe, du erkennst den Unterschied."

#### Das Tiervolk — Wegsprache

Oral, rhythmisch, durchzogen von Gastrecht-Formeln und Weg-Metaphern. Das Tiervolk spricht in Bildern, die sich bewegen. "Der Weg fragt nicht, wohin du willst." "Wer Gastrecht bricht, kreuzt seinen eigenen Pfad."

Ihr blinder Fleck: Das Tiervolk romanisiert seine eigene Aussenseiterposition. Ob sie wirklich frei sind oder nur gelernt haben, ihre Unfreiheit schön zu finden — das ist eine Frage, die RELICS dem Spieler überlasst.

**Beispiel — Rho, der Händler, zum Spieler:**

> "Du fragst, ob ich Angst habe. Das ist eine seltene Frage von jemandem wie dir. Die meisten fragen, was ich weiss oder was ich habe. Du fragst, was ich fühle. Das könnte bedeuten, dass du neugierig bist. Das könnte bedeuten, dass du die Antwort verwenden willst. Das könnte beides bedeuten. Der Weg unterscheidet nicht zwischen Neugier und Kalkul — er führt beide ans Ziel."

### 4.3 Schattenfieber-Dialoge

Das Schattenfieber verändert Dialoge auf drei Ebenen. Die Veränderungen sind graduell — kein harter Schalter bei einem bestimmten Wert.

#### Rauschen (Infektionswert ca. 1-40)

Subtil. Einzelne Wörter in NPC-Dialogen sind verändert — "kalt" statt "kühl", "Fleisch" statt "Boden", "atmen" statt "wehen". Die Sätze sind grammatisch korrekt und inhaltlich plausibel. Der Unterschied ist da, aber er drängt sich nicht auf.

Ausserdem: Umgebungshinweise, die nur für den infizierten Spieler sichtbar sind — ein leises Pulsieren, ein Flüstern, eine Bewegung im Augenwinkel.

**Design-Regel:** Rauschen-Veränderungen müssen so subtil sein, dass ein Spieler sie beim ersten Durchgang für normale Textvariation halten könnte.

#### Risse (Infektionswert ca. 41-80)

Spürbar. Ganze Gesprächsoptionen erscheinen, die dem sauberen Spieler nicht zur Verfügung stehen. Nicht markiert. NPCs reagieren irritiert auf Antworten, die der Spieler für normal hält. Fragwürdige Questgeber treten auf.

**Design-Regel:** Riss-Dialoge müssen MECHANISCH RELEVANT sein — echte Informationen, echte Zugänge, echte Entscheidungen.

#### Schwelle (Infektionswert ca. 81-100)

Fundamental. Der Spieler kann nicht mehr unterscheiden, welche Gespräche "echt" sind. Dialoge mit Figuren, die möglicherweise nicht existieren. Das Parallel-Narrativ der Schwelle ist eine ANDERE Geschichte — in sich so kohärente und mechanisch relevant wie die des sauberen Spielers.

**Design-Regel:** Schwelle-Dialoge dürfen den Spieler NICHT in Sackgassen führen. Auch im Zustand maximaler narrativer Instabilität muss jeder Dialogpfad zu einem spielbaren Ergebnis führen.

---

## 5. Schattenfieber als narratives System

### 5.1 Kosmologische Grundlage

Das Schattenfieber ist keine Krankheit im medizinischen Sinne. Es ist ein kosmologischer Zustand — das Ergebnis davon, dass die Hauten dünner werden, dass die Grosse Flechtung sich löst, dass die Trennung der Daseinsebenen nicht mehr hält. Wer vom Schattenfieber betroffen ist, kommt unkontrolliert mit dem Emer-Material in Kontakt — mit dem Stoff, aus dem die Welt gemacht ist, der aber älter ist als die Welt und sich an Zustände erinnert, die vor der ersten Trennung lagen.

Emres WBB-01 stellt die Verbindung her: Biotechnologie und Schattenfieber greifen auf dasselbe Material zu. Biotech ist die kontrollierte Manipulation, Schattenfieber die unkontrollierte Reaktion. Gleiche Quelle, verschiedene Ausprägung.

### 5.2 Narratives Stufenmodell (Sync mit GDD-02, Tabelle 2.3)

| Narrativer Zustand | Infektionswert | Mechanischer Name (GDD-02) | Kern-Erfahrung |
|---|---|---|---|
| Gesund | 0–19 | Rein | Klare, zuverlässige Wahrnehmung. Die vollständige Geschichte — aber nicht die ganze Wahrheit |
| Rauschen | 20–50 | Gezeichnet → Infiziert | Zweite Textur der Welt. Der Spieler bemerkt sie — vielleicht. Odin-Opfer in seiner mildesten Form |
| Risse | 51–75 | Verwandelt | Die Trennung der Schichten beginnt zu versagen. Andere Informationen. Andere Möglichkeiten. Andere Unsicherheiten |
| Schwelle | 76–100 | Entfesselt | Der Spieler steht an der Haut. RELICS ist jetzt ein anderes Spiel. Nicht schlechter. Anders |

*Randfall (bilateral mit Darius zu klären): GDD-02 definiert Stufe 2 als Wert 26–50 "Infiziert (Übergang Rauschen→Risse)". Das passt zur Übergangszone — Rauschen beginnt ab ~20, Risse beginnen graduell ab ~40. Der Schreibtext für die Übergangszone (Wert 40–50) folgt in V3.*

### 5.3 Das Opfermotiv

In der Mythologie, die Emre geschrieben hat, hat Wissen immer einen Preis. Halvard gab sein Auge. Sigvalt gab seine Hand. Erthag gab sich selbst. Das Schattenfieber ist das spielmechanische Echo dieses mythologischen Prinzips.

Das Opfer ist echt. Es ist nicht reversibel (CD-bestätigt). Die Infektion vergisst nicht. Wer einmal die zweite Schicht gesehen hat, kann nicht mehr so tun, als gäbe es sie nicht.

Das ist die tiefste Verbindung zwischen Narrativ und Mechanik in RELICS: Das Schattenfieber ist kein Buff-System mit narrativem Anstrich. Es ist eine Erzählhaltung, die zum Spielsystem geworden ist.

### 5.4 Replay-Narrativ

RELICS ist ein Spiel, das man zweimal spielen soll. Nicht muss — soll. Der erste Durchgang erzählt eine vollständige Geschichte. Der zweite — mit anderer Fraktion, anderem Infektionsgrad — kommentiert und stellt in Frage.

RELICS beantwortet die Frage "Welche Version ist wahr?" nicht. Die Weigerung, sie zu beantworten, ist das Erlebnis.

### 5.5 Drei Fraktions-Deutungen des Schattenfiebers

**Die Krone — "Anomalie":** Bedrohung der Ordnung, Zeichen des Verfalls. Ab Stufe 3 ist der Krone-Zugang massiv eingeschränkt.

**Die Gilden — "Gelegenheit":** Kontrollierbare Ressource. Sie handeln mit Suppressiva, kalkulieren den Marktwert der Fähigkeiten. Ihre Gefahr liegt nicht in der Ablehnung, sondern in der Instrumentalisierung.

**Der Orden — "Zeichen":** Kosmologisches Signal, das studiert werden muss. Der Orden bietet Reinigung an — gegen Loyalität und Information. Ab Stufe 3 verweigert er die Reinigung: Ein Spieler auf dieser Stufe ist zu wertvoll als Forschungsobjekt.

---

## 6. Der Wanderer — Spielercharakter-Identität

### 6.1 Das Motiv

Emres WBB-01 beschreibt das Halvard-Wanderer-Motiv: Ein mächtiges Wesen, das verkleidet reist — unter falschen Namen, als Bettler, als Niemand. Halvard prüfte die Gastfreundschaft.

RELICS kehrt dieses Motiv um. Der Spieler IST schwach. Er ist kein Gott in Verkleidung. Aber die Welt behandelt ihn, als KÖNNTE er mehr sein — und diese Behandlung IST eine Art von Macht.

### 6.2 Gastrecht als Spieler-Mechanik

Das Gastrecht ist eine lebende kulturelle Praxis, die dem Spieler konkrete mechanische Zugänge verschafft. Feuer, Nahrung, Schutz. Rede und Gegenrede. Bruch hat Konsequenzen.

Jede Fraktion interpretiert das Gastrecht anders (Details: Abschnitt 4.2, Fraktions-Register).

### 6.3 Spieler und Tiervolk — Status-Verwandte

Der Spieler und das Tiervolk teilen denselben Status: Gäste. Diese Verwandtschaft erzeugt narratives Potenzial auf drei Achsen: Solidarität, Konkurrenz, Spiegel.

Das Tiervolk zeigt dem Spieler, was er werden könnte, wenn er nie dazugehört.

### 6.4 Die Lebende Krone und der Wanderer

Was geschieht, wenn der Wanderer — dieser Niemand, dieser Fremde — in Kontakt mit einem Artefakt kommt, das mit seinem Träger verschmilzt?

Die Krone hat bisher Könige verändert — Menschen mit Legitimation. Der Spieler hat nichts davon. Er ist eine leere Seite — und die Krone, die lebt, die wächst, die reagiert, hat noch nie eine leere Seite berührt. Was sie damit macht, ist die Geschichte, die RELICS erzählt.

---

## 7. Synchronisation mit anderen GDD-Kapiteln

| Abhängigkeit | Kapitel | Status | Handlungsbedarf |
|---|---|---|---|
| Schattenfieber-Stufenmapping | GDD-02, Abschnitt 2.3 | Synchronisiert | Übergangszone-Text (Wert 40-50) folgt V3 |
| Schlüsselfiguren | GDD-04 (V1 heute) | Verlinkt | Fraktionsführer-Stimmen integriert |
| Kosmologie und Mythos | WBB-01 (V1) | Integriert | Seher-Visionen: Was sieht Maret genau? (offene Frage) |
| Topos und Geografie | WBB-02 | Abhängig (teilweise) | Ortsnamen für Quest-Lokalisierung fehlen noch |
| Art Direction | GDD-05 (Vera) | Abhängig | Schattenfieber-Visualisierung, Krone-Design |
| Technik/Produktion | GDD-06 (Tobi/Finn) | Abhängig | Vertonung ja/nein, Branching-Komplexität |

---

\clearpage

# GDD-04 — Schlüsselfiguren & NPCs


---

## Lesehilfe: Figuren-Format

Jede Figur hat drei Pflichtbestandteile:

- **Stimme** — ein unverwechselbarer Sprachrhythmus, der sofort erkennbar ist, wenn man ihn laut liest. Kein Steckbrief, keine Zusammenfassung. Beispieldialoge immer inklusive.
- **Funktion** — was tut diese Figur im narrativen System? Blocker, Ermögliger, Spiegel, Zerstoerer?
- **Widerspruch** — etwas, das der Spieler erst spät versteht. Nicht: "der Schurke ist eigentlich gut." Sondern: "die Person, die ich mochte, hat Dinge getan, die ich nicht verzeihen kann — und sie hat einen Grund, den ich verstehe."

Archetypische Figuren — der edle Krieger, der weisen Ratgeber, die geheimnisvolle Seherin — sind kein Ziel. Sie sind das, was man produziert, wenn man aufhört zu denken.

---

## 1. Aldine Vor — Fraktionsführerin der Krone

### Basisdaten

- **Fraktion:** Die Krone
- **Funktion im Spiel:** Quest-Geberin (Kronenquest "Pflicht und Verfall"), Point-of-No-Return-Figur (Beat 6), narrativer Spiegel für den Spieler in Akt II
- **Alter:** 54
- **Äusseres:** Militärische Haltung — nicht durch Disziplin, sondern durch Erschöpfung, die sich zu Haltung verfestigt hat. Kleidung funktional, nicht opulent. Kein Schmuck ausser einem kleinen Siegel an der linken Hand — das Siegel ist nicht das ihrer Familie, sondern das ihres Vorgängers, den sie abgelöst hat.

### Hintergrund

Aldine Vor ist nicht in die Krone-Führerschaft hineingeboren. Sie hat sie erkämpft — nicht durch Verwandtschaft, sondern durch zwanzig Jahre Verwaltung in den Grenzregionen, wo die Krone dünn war und sie die Ordnung allein hält. Ihr Vater war ein Krone-Hauptmann, dem die Kronentreue die Hände abgehackt hatte — buchstäblich, durch einen Befehl, den er hätte verweigern sollen und nicht verweigerte. Er lebte danach noch siebzehn Jahre, ein Denkmal an das, was Pflicht kostet.

Aldine Vor glaubt nicht an die Krone als Institution. Sie glaubt an die Krone als Notwendigkeit — das Einzige, das zwischen dem Mittelgrund und dem Chaos steht, das sie in den Grenzregionen erlebt hat. Wenn sie die Krone schützt, schützt sie nicht Tradition. Sie schützt die Abwesenheit von dem, was sie gesehen hat, wenn Tradition zusammenbricht.

### Stimme

Die Krone spricht in Pflichten, nicht in Wünschen — und Aldine Vor ist die vollkommenste Instanz dieses Registers.

Ihr Stil: Parataxe. Kurze Sätze. Passiv wo möglich. Das Subjekt verschwindet hinter der Sache. Wenn sie bittet, klingt es wie ein Befehl, dem ein Schritt fehlt. Wenn sie dankt, klingt es wie eine Quittung.

**Erstbegegnung (Spieler hat sich durch eine Krone-Aufgabe bewiesen):**

> "Euer Dienst ist registriert. Er entspricht den Anforderungen, die ich gestellt habe. Das ist eine Feststellung, keine Lob."
> *(Pause)*
> "Es gibt weitere Anforderungen. Ob Ihr ihnen entsprechen würdet, ist unklar. Die Vergangenheit bürgt nicht für die Zukunft — das ist der Fehler derer, die in Dynastien denken. Ich denke in Funktion."

**Im dritten Akt, wenn der Spieler die Wahrheit über den Biotech-Einsatz aufgedeckt hat:**

> "Ihr habt es gesagt. Das verändert nichts. Ich sage Euch, warum: Weil die Ordnung nicht bricht, wenn man ihr die Wahrheit zeigt. Sie bricht, wenn die Menschen aufhören, so zu tun, als würde sie halten."
> *(Lange Pause)*
> "Ich tü das jeden Tag. Ihr könnt urteilen, wenn Ihr gefunden habt, was Ihr tun würdet, wenn die Alternative Chaos ist. Nicht theoretisch. Tatsächlich."

**Allein, nachts, wenn der Spieler sie beobachten kann (keine Reaktion auf den Spieler):**

> *(Zu sich selbst, leise)* "Sigvalt gab seine Hand. Die Krone fragte nicht, ob er wollte. Die Krone fragt nie. Das ist ihr einziges Versprechen."

### Funktion

**Blocker und Ermögliger gleichzeitig.** Aldine Vor schliesst Türen und öffnet sie — aber immer mit Konsequenz. Sie gibt dem Spieler Zugang zu Krone-Ressourcen, zu Archiven, zu Informationen, die sonst unzugänglich wären. Aber jeder Zugang bindet. Der Spieler merkt irgendwann, dass er nicht für die Krone arbeitet — sondern dass die Krone ihn arbeiten lässt, weil er etwas hat, das sie braucht, und weil sie ihn beobachtet, ob er weiss was er hat.

**Narrativer Spiegel.** Aldine Vor ist, was der Spieler werden könnte, wenn er sich für die Ordnung entscheidet und lange genug dabei bleibt: jemand, der an das System glaubt, weil die Alternative schlimmer ist, und der gelernt hat, dass "schlimmer" kein Argument ist, sondern ein Zustand.

### Widerspruch

Der Spieler mag Aldine Vor möglicherweise. Oder er respektiert sie zumindest. Sie ist nicht zynisch — sie glaubt wirklich, was sie tut. Sie glaubt an die Ordnung, weil sie gesehen hat, was ohne sie passiert.

Und dann entdeckt der Spieler: Aldine Vor weiss seit Jahren, dass der Krone-Biotech-Einsatz die Faulung beschleunigt. Nicht aus Bosheit. Aus einer Kalkulation: Wenn sie es offentlich macht, bricht die Ordnung. Wenn sie schweigt, hält die Ordnung — vielleicht lange genug, damit jemand anderes eine Lösung findet.

Sie hat sich entschieden zu schweigen. Sie lebt jeden Tag mit dieser Entscheidung. Und sie würde sie wieder treffen.

---

## 2. Cress — Fraktionsführer der Gilden

### Basisdaten

- **Fraktion:** Die Gilden
- **Funktion im Spiel:** Quest-Geber (Gildenquest "Der Preis aller Dinge"), Informationsbroker, narrativer Ermögliger mit verdeckter Agenda
- **Alter:** 41
- **Äusseres:** Gut gekleidet, nicht prunkvoll. Der Unterschied ist bewusst — Prunk signalisiert, dass man versucht, Macht zu zeigen. Cress zeigt keine. Er trägt sie. Sein Äusseres sagt: Ich bin erfolgreicher als du ohne anstrengend darauf hinzuweisen. Hände gepflegt — er arbeitet mit Stift und Siegel, nicht mit Werkzeug, und das sieht man.

### Hintergrund

Cress kommt aus einer Handwerker-Familie im Nordquartier einer Gildenstadt — sein Vater war Weber, seine Mutter Färberin, beide handelten mit dem, was sie herstellten, bis die Gilde den Preis festlegte und der Festpreis bedeutete, dass der Vater nicht mehr kaufen konnte, was er brauchte, um das herzustellen, das er verkaufte.

Cress lernte früh: Das System ist kein Feind und kein Freund. Es ist eine Logik. Wer die Logik kennt, gewinnt. Wer gegen sie kämpft, verliert nicht das Spiel — er spielt das falsche Spiel.

Er hat Leute aus der Armut gezogen. Er hat Städte gebaut. Er hat Handelsrouten eröfffnet, die Regionen verbanden, die vorher isoliert waren. Er hat auch Leute sterben lassen, wenn es billiger war. Er sieht keinen Widerspruch.

### Stimme

Die Gilden sprechen in Preisen und Angeboten — und Cress ist der technisch vollkommenste Sprecher dieses Registers. Er ist nie aggressiv. Er ist nie drückend. Er ist verbindlich und unvermeidlich.

Sein Stil: Viele Konjunktive. "Könnte." "Vielleicht." "Wenn die Umstände günstig sind." Der Preis kommt immer am Ende des Satzes, wenn man schon zugehört hat. Er stellt keine Forderungen — er beschreibt Optionen. Die Optionen sind alle so geformt, dass eine davon immer unattraktiv ist.

**Erstbegegnung:**

> "Du hast Fragen. Das ist gut — Fragen bedeuten Interesse, und Interesse bedeutet, dass ein Gespräch stattfinden könnte, das für beide Seiten produktiv wäre. Mein Name ist Cress. Du weisst das vermutlich schon — wenn du hier bist, hast du dich vorbereitet, und wenn du dich vorbereitet hast, weisst du, an wen du dich wendest."
> *(Kurze Pause)*
> "Was ich noch nicht weiss, ist, was du hast. Das ist der interessante Teil."

**Mitte des Spiels, wenn der Spieler herausfindet, für wen Cress das Wissen über die Lebende Krone weiterverkaufen würde:**

> "Du bist enttäuscht. Das sehe ich. Das ist auch verständlich — du hattest ein Bild von mir, und das Bild war, glaube ich, angenehmer als die Realität."
> *(Pause)*
> "Ich sage dir, was die Realität ist: Ich verkaufe das Wissen. Nicht weil ich gleichgültig bin. Sondern weil Wissen, das nicht zirkuliert, stirbt. Das ist keine Rechtfertigung. Das ist eine Beschreibung."

**Wenn der Spieler ihn direkt nach dem Dorf fragt, das die Brücke opfert:**

> "Das Dorf. Ja. Ich weiss, was du sagen willst. Ich sage dir etwas: Das Dorf weiss es auch. Sie wissen, dass die Brücke gebaut wird. Sie wissen, was es bedeutet. Sie haben Optionen gehabt."
> *(Pausiert)*
> "Die Optionen waren schlecht. Das gebe ich zu. Aber schlecht ist keine Ausrede. Schlecht bedeutet: jemand hat eine schlechtere Kalkulation gemacht als ich. Kein moralisches Urteil. Eine Feststellung."

### Funktion

**Instrumentalisierer.** Cress gibt dem Spieler, was er braucht — aber immer mit einem Restbetrag, den der Spieler nicht sieht, bis er ihn zahlt. Er ist kein Feind. Er ist eine Konsequenz. Wer mit ihm arbeitet, arbeitet für seine Ziele. Das ist transparent. Er sagt es. Aber Transparenz macht es nicht weniger wahr.

**Informationsbroker.** Cress weiss, was die anderen Fraktionen wissen — weil er die Information kauft. Er bietet dem Spieler Wissen an, das er nicht anderswo bekommt. Der Preis des Wissens ist immer: Cress bekommt gleichwertiges Wissen zurück.

### Widerspruch

Cress ist nicht herzlos. Das ist der Widerspruch.

Er kommt aus der Unterschicht. Er weiss, was Armut bedeutet, was es bedeutet, wenn das System die Preise setzt und man kein Mitspracherecht hat. Er hasst das. Er hat sein Leben damit verbracht, aus dieser Position herauszukommen. Und er hat dabei ein System gebaut, das andere in dieselbe Position setzt — weil er gelernt hat, dass das System die einzige Sprache ist, die bleibt.

Der Spieler, der das herausfindet, steht vor einer Frage: Ist Cress ein Heuchler? Oder ist er jemand, der so tief ins System eingearbeitet wurde, dass er vergessen hat, was er dagegen hatte?

Cress hat die Antwort. Er sagt sie nicht, weil er sie für eine Schwäche hält.

---

## 3. Cassius — Fraktionsführer des Ordens

### Basisdaten

- **Fraktion:** Der Orden
- **Funktion im Spiel:** Quest-Geber (Ordensquest "Die Last des Wissens"), Wissensbroker mit Kontrollabsicht, narrativer Antagonist ohne Bosheit
- **Alter:** 67
- **Äusseres:** Ordenstrachtung, aber abgenutzt — die Zeichen des Rangs sind da, aber nicht gepflegt. Er hat aufgehört, Zeichen zu pflegen, weil die Sache selbst ihm wichtiger ist als ihr Symbol. Sehr ruhige Bewegungen. Er bewegt sich, als hätte er gelernt, dass schnelle Bewegungen Verwirrung stiften, und Verwirrung ist Information-Verlust.

### Hintergrund

Cassius war Novize, dann Schüler, dann Archivar, dann Rat, dann — nach einer Kette von Ereignissen, die er als "logische Konsequenzen" bezeichnet — Ordensführer. Niemand wollte das Amt. Cassius wollte es auch nicht. Er übernahm es, weil die Alternative war, jemanden in das Amt zu lassen, der nicht verstand, was das Amt bedeutete.

Er versteht die Welt so gut wie irgendwer in der Spielwelt. Er weiss, dass die Hauten dünner werden. Er weiss, dass das Schattenfieber und die Biotechnologie dasselbe Material verwenden. Er weiss, dass die Lebende Krone nicht eine Lösung ist, sondern eine Komplikation. Er weiss, dass der Orden — wenn er handeln würde, offen handeln würde — vielleicht etwas verbessern könnte.

Und er hält das Wissen trotzdem zurück. Weil Wissen, das unkontrolliert zirkuliert, Panik erzeugt. Und Panik ist schlimmer als Unwissen. Cassius hat Panik gesehen — in einer Grenzregion, vor dreissig Jahren, als jemand die Wahrheit über das Schattenfieber veröffentlichte. Sieben Stadte brannten. Er war dabei.

### Stimme

Der Orden spricht in Fragen und Schweigen — und Cassius ist der Meister dieses Registers. Er stellt Fragen, auf die er die Antworten bereits kennt. Er schlägt die Antwort in Fragen ein, weil er weiss, dass eine Aussage abgelehnt werden kann, eine Frage aber antwortet werden muss — und die Antwort gehört dann dem Fragenden.

Sein Stil: Präzise. Nominalisierungen. Unpersönliche Konstruktionen. Lange Pausen, in denen er dem Spieler Zeit gibt, sich selbst zu verraten. Wenn er direkt ist, ist es ein Zeichen, dass er entschieden hat, dem Spieler zu vertrauen. Das passiert selten.

**Erstbegegnung (Spieler wurde vom Orden untersucht, ohne es zu wissen):**

> "Ihr habt gewartet. Das ist bemerkenswert — die meisten warten nicht. Sie stellen sofort Fragen, als wäre die Frage wichtiger als die Antwort."
> *(Pausiert)*
> "Das ist sie nicht. Die Frage ist die Form. Die Antwort ist der Inhalt. Ich bin an beidem interessiert. Ihr seid, vermute ich, primär an letzterem. Das macht Euch erklärbar."

**Wenn der Spieler fragt, warum Seiten aus den Archiven fehlen:**

> "Ihr fragt, warum. Das ist die naheliegendste Frage, die man stellen kann — und deshalb ist sie meistens nicht die richtige."
> *(Lange Pause)*
> "Die richtigere Frage wäre: Was geschähe, wenn die Seiten nicht fehlten? Ich beantworte Eure Frage trotzdem: Die Seiten fehlen, weil ihre Verfügbarkeit zu einem Zeitpunkt, an dem bestimmte Informationen noch nicht zugeordnet werden konnten, schlechter gewesen wäre als ihre Abwesenheit. Das ist keine Rechtfertigung. Es ist eine Kalkulation."

**Einziges direktes Gespräch, Ordensquest Beat 4 — wenn der Spieler entschieden hat:**

> "Du hast entschieden. Ich bin froh, dass es vorbei ist."
> *(Pause — länger als üblich)*
> "Ich war nicht sicher, was du tun würdest. Das kommt selten vor. Ich bin alt genug, dass es selten vorkommt. Es ist kein angenehmes Gefühl. Es ist auch kein unangenehmes. Es ist... das Gefühl, dass etwas noch offen ist. Das halte ich fest."

### Funktion

**Der Wissens-Hüter als narrative Zentralgestalt.** Cassius ist die Figur, die am meisten weiss — und die deshalb am meisten Schaden anrichten kann, ohne es zu wollen. Er schützt nicht die Wahrheit. Er schützt die Kontrolle über die Wahrheit. Das ist ein Unterschied, den er zumindest intellektuell anerkennt.

**Spiegel für den Orden-Spieler.** Wer den Orden-Pfad spielt, sieht in Cassius eine mögliche Zukunft: jemand, der so viel weiss, dass er nicht mehr anders kann, als zu kontrollieren. Das ist keine Bosheit. Das ist eine Konsequenz.

### Widerspruch

Cassius glaubt wirklich, was er tut. Das ist das Erschreckende.

Er hat nicht beschlossen, ein Kontrolleur zu sein. Er hat beschlossen, Schaden zu verhindern. Und Schaden-Verhinderung hat — über dreissig Jahre, über eine Reihe von plausiblen Entscheidungen — einen Kontrolleur aus ihm gemacht.

Der Spieler, der seinen Questpfad abschliesst, versteht das. Und versteht, dass Cassius es auch weiss. Und weiss, dass Cassius es trotzdem nicht ändern wird — weil die Alternative, nach seiner Kalkulation, immer noch schlimmer ist.

Das ist kein Villain. Das ist ein Mensch, der sich in seiner eigenen Logik eingesperrt hat und zu klug ist, den Schlüssel nicht zu sehen, und zu müde, ihn zu benutzen.

---

## 4. Maret — Der Seher

### Basisdaten

- **Fraktion:** Keine. Früherer Orden-Archivar, jetzt nicht mehr.
- **Funktion im Spiel:** Charakter-Quest "Der Spiegel" (→ GDD-03, Abschnitt 3.6), Einstiegspunkt für Schattenfieber-Narrativ, optionale Figur (nur für Spieler, die ihn suchen — oder infizierte Spieler ab Stufe 1)
- **Alter:** Unbekannt. Er erinnert sich an das Flechtfest als Kind. Das macht ihn alt. Er sieht jünger aus. Das ist das Schattenfieber.
- **Äusseres:** Ordentlich, fast pedantisch ordentlich — Gegenbewegung zu seinem Inneren. Die Kleider sind geflickt, aber sauber geflickt. Er lebt in einem kleinen Zimmer am Rand der Stadt, das er vollgeschrieben hat: an den Wänden, auf losen Blättern, auf dem Boden, über den Fenstern. Die Schrift ist lesbar. Sie ist auch nicht immer chronologisch.

### Hintergrund

Maret war Archivar des Ordens — gut, vielleicht zu gut. Er war der erste, der die Verbindung zwischen Schattenfieber und Biotechnologie systematisch dokumentierte. Er legte das Ergebnis Cassius vor. Cassius las es, dankte ihm, und entschied, dass die Dokumentation nicht zirkulieren dürfe.

Maret war damit nicht einverstanden. Er war damit so nicht einverstanden, dass er versuchte, die Dokumentation zu duplizieren und zu veröffentlichen. Cassius fand es heraus. Maret wurde nicht bestraft — er wurde entlassen. Ohne Feind, ohne Skandal. Einfach: entlassen.

Maret zog sich zurück. Er hatte während seiner Archivarbeit Schattenfieber-Exposition gehabt — keine schwerere als jeder Archivar, der nahe an den betroffenen Texten gearbeitet hat, aber genug. Er infizierte sich weiter, absichtlich oder nicht (er selbst weiss es nicht mehr). Er ist jetzt bei Stufe "Schwelle" — der einzige bekannte Überlebende auf dieser Stufe, der noch funktioniert.

"Funktioniert" ist das Wort, das er selbst benutzt. Nicht "lebt". Nicht "überleben". Funktioniert.

### Stimme

Maret ist keine Orakel-Figur. Er spricht nicht in Rätseln, weil Rätsel profetisch klingen sollen. Er spricht in Fragmenten, weil seine Wahrnehmung in Fragmenten ist — er verliert den Faden nicht, weil er ihn nie vollständig hat. Er weiss, welche Schicht er gerade sieht, und welche er sehen sollte, und ob sie dieselbe sind.

Sein Stil: Ruhig, fast akademisch — das ist sein Archivar-Hintergrund, der blieb. Dann: abrupt. Dann: zurück. Die Lücken in seinen Sätzen sind nicht dramatisch — sie sind der Moment, in dem er eine andere Schicht überprüft.

**Erste Begegnung (Spieler findet ihn am Ort des "ersten Zeichens", Beat 3 Hauptquest):**

> "Du bist neu hier. Ich meine: neu in dem, was du siehst."
> *(Pause — er schaut an einer Stelle hinter dem Spieler, wo nichts ist)*
> "Entschuldige. Manchmal überlagern sich die Schichten, und ich muss überprüfen, welche... aktuell ist. Du bist in der richtigen. Das weiss ich, weil du mich ansiehst."

**Wenn der Spieler ihn nach dem Schattenfieber fragt:**

> "Was du wissen willst, ist: Wie ist es. Das ist die Frage, die alle stellen. Ich sage dir, wie es ist."
> *(Kurze Pause)*
> "Es ist wie... stell dir vor, du schreibst auf Papier, und das Papier ist durchsichtig, und darunter liegt ein anderes Blatt, und auf dem anderen Blatt steht auch etwas. Manchmal lesbar. Manchmal nicht. Manchmal ist das, was darunter steht, wichtiger als das, was ich sehe. Manchmal stimmt es nicht."
> *(Pause)*
> "Ich habe aufgehört, sicher zu sein, welches welches ist. Das klingt schlimmer, als es ist. Oder genau so schlimm. Ich kann das nicht von hier aus beurteilen."

**Zum infizierten Spieler — wenn er merkt, dass der Spieler auch sieht:**

> "Du siehst es. Ich sehe, dass du es siehst. Das ist selten. Nicht — nicht angenehm oder unangenehm. Nur: selten."
> *(Lange Pause. Er sieht den Spieler direkt an — das macht er selten)*
> "Pass auf: Was du siehst, ist nicht immer falsch. Aber was du siehst, ist auch nicht immer das, was da ist. Das klingt wie eine Warnung. Es ist keine Warnung. Es ist eine Beschreibung."
> *(Pause)*
> "Ich hätte mich gewünscht, dass mir das jemand früh gesagt hätte. Ich sage es dir jetzt."

**Spät im Spiel, wenn Spieler ihn nach Cassius fragt:**

> "Cassius."
> *(Pause)*
> "Er hat nicht Unrecht gehabt. Das ist das Schwierige. Er hatte Gründe. Gute Gründe. Ich hatte auch Gründe. Auch gute."
> *(Pause — länger diesmal)*
> "Ich weiss nicht, wer richtig hatte. Ich weiss, was passiert ist, und ich weiss, was ich geglaubt habe, und ich weiss, dass beides gleichzeitig wahr sein kann. Das ist auch etwas, was man im Fieber lernt."

### Funktion

**Emotionaler Kern für infizierte Spieler.** Maret ist die einzige Figur, die dem Spieler sagt, was es bedeutet, auf Schattenfieber-Schwelle zu leben — nicht als Warnung, nicht als Prophezeiung, sondern als Erfahrungsbericht. Er ist der Beweis, dass das Schattenfieber nichts gibt, ohne alles zu nehmen. Und er ist die Person, die trotzdem da ist.

**Brücke zwischen Orden-Wissen und Spieler-Erfahrung.** Maret weiss, was der Orden weiss — er hat es archiviert. Aber er weiss es nicht als Machtinstrument. Er weiss es als jemandem, dem das Wissen etwas gekostet hat.

**Optionaler Questgeber.** Die Charakter-Quest "Der Spiegel" ist nur zugänglich, wenn der Spieler Maret sucht oder infiziert ist. Kein Quest-Marker. Der Spieler findet Maret durch Neugier, durch das "erste Zeichen" in Akt I, oder — wenn infiziert — durch die Schattensinne, die zeigen, wo er ist.

### Widerspruch

Maret ist der sympathischste Charakter in RELICS — das ist seine Gefahr.

Der Spieler mochte ihn. Maret ist ehrlich, ruhig, nicht bedrohlich, und er sagt dem Spieler Dinge, die andere nicht sagen. Maret hat auch — absichtlich oder nicht (er weiss es selbst nicht mehr) — andere Infizierte gefunden und ihnen geholfen, ihre Infektionswerte zu steigern, in dem Glauben, dass höhere Werte tiefere Einsicht bedeuten.

Manche dieser Menschen haben das überlebt. Manche nicht.

Maret weiss das. Er hat keine Entschuldigung. Er hat eine Erklärung: Er dachte, er hülfe. Er ist nicht sicher, ob das eine Entschuldigung ist.

Das ist die Frage, die der Spieler spät im Spiel stellt — und die Maret nicht abweist. Er sagt: "Ich weiss es nicht." Das ist die ehrlichste Antwort, die irgendeine Figur in RELICS gibt.

---

## 5. Rho — Tiervolk-Händler

### Basisdaten

- **Fraktion:** Keine — Tiervolk, nomadisch, Händler
- **Funktion im Spiel:** Städtequest "Mittelgrund" (zentrale Figur), Seitenquest 2 "Gastrecht" (Quest-Geber), Informationsquelle für Spieler, die das Tiervolk-Netz zugang erarbeitet haben
- **Alter:** 38
- **Tierart-Referenz:** Raptor-artig — schlanke Proportionen, Federnzeichnung am Kopf (keine Federn, aber Haare in Federmuster), grosse Augen mit seitlichem Sehfeld. Bewegungen schnell, sehr präzise. Kein tribal-Element in Kleidung oder Verhalten — Stadtwear, gut ausgesucht, fraktionsneutral.
- **Äusseres:** Zieht keine Aufmerksamkeit auf sich, ohne unsichtbar zu sein. Das ist eine Fähigkeit, kein Zufall. Er trägt nichts, das ihn eindeutig einer Fraktion zuordnet. Er trägt auch nichts, das ihn eindeutig als Tiervolk markiert — ausser dem, was er nicht verstecken kann. Er hat nicht gelernt, sich zu verstecken. Er hat gelernt, sich nicht anzubieten.

### Hintergrund

Rho ist in einer Tiervolk-Handelskarawane aufgewachsen — vier Generationen desselben Handelsweges durch denselben Mittelgrund, denselben drei Städte, dieselben Gastrecht-Abkommen, die jede Generation neu aushandeln muss, weil kein Abkommen über den Tod der unterzeichnenden Generation gilt.

Er kennt den Mittelgrund besser als die meisten Einheimischen. Er kennt die Städte als System — wer wirklich entscheidet, wer das Schutzgeld nimmt, welche Krone-Patrouillen käuflich sind, welche Gilden-Lager illegal handeln, welche Orden-Stationen die Tiervolk-Berichte verschwinden lassen. Er kennt das, weil sein Überleben davon abhing, es zu kennen.

Er ist kein Dieb. Aber er kennt Diebe, arbeitet manchmal mit ihnen, und verurteilt sie nicht. Das Recht gilt nicht für das Tiervolk — also gilt das Recht des Tiervolk nicht nach dem Recht. Es gilt nach einer anderen Logik. Rho hat diese Logik.

### Stimme

Das Tiervolk spricht in der Wegsprache — oral, rhythmisch, Weg-Metaphern, Gastrecht-Formeln. Rho spricht das auch — aber er ist lange genug in der Stadt, dass er die Stadtsyntax drüber gelegt hat. Das Ergebnis: Die Wegsprache klingt unter der Stadt-Sprache. Wenn er ruhig ist, hört man die Stad. Wenn er angespannt ist, hört man den Weg.

Sein Stil: Abgewägt, beobachtend. Er stellt Fragen, die er nicht als Fragen formuliert. Er gibt Informationen, die er nicht als Informationen bezeichnet. Er hat gelernt, dass Direktheit riskant ist, und dass das, was er weiss, teurer ist, wenn er es nicht sofort anbietet.

**Erstbegegnung (Spieler nähert sich dem Marktstand):**

> "Du hast mich schon zweimal angeschaut. Das dritte Mal bin ich sicher."
> *(Pause — er arrangiert etwas auf dem Stand, ohne aufzusehen)*
> "Ich verkaufe Getreidewaren aus dem Nordquartier und Gewürze aus dem Weg-Netz. Beides ist gut und beides hat einen fairen Preis. Wenn du das nicht suchst, ist es trotzdem gut zu wissen, was ich offiziell tü."

**Wenn der Spieler nach dem Tiervolk-Netz fragt:**

> "Der Weg fragt nicht, wer du bist. Das stimmt. Aber die, die den Weg kennen, fragen sehr wohl, warum jemand fragt."
> *(Kurze Pause)*
> "Ich frage: Warum fragst du? Nicht als Ablehnung. Als Einstieg. Der Weg braucht keinen Grund. Ich schon."

**Wenn der Spieler die Seitenquest "Gastrecht" beginnt (Rhos Ware wurde gestohlen):**

> "Es gibt drei Versionen davon, was passiert ist. Die Krone-Version, die Gilden-Version, und die des Priesters. Du wirst alle drei hören, wenn du herumfragst."
> *(Pause)*
> "Keine davon stimmt. Ich sage dir das nicht, damit du die richtige Version suchst. Ich sage es, damit du weisst, warum ich nicht zur Wache gegangen bin."

**Spät im Spiel, wenn Spieler Vertrauen erworben hat:**

> "Ich zeige dir etwas, das ich wenigen zeige."
> *(Er zeigt dem Spieler eine handgezeichnete Karte des Tiervolk-Wegnetzes — nicht die Stadt, sondern die Verbindungen zwischen den Gästerechtspunkten, den Schlafsplätzen, den Schutzzonen)*
> "Das ist die Stadt, die die Krone nicht sieht. Das sind die Knochen unter den Steinen. Wir haben sie so gelegt, als eure Vorvätern die Steine draufgebaut haben. Gastrecht braucht keine Mauern. Es braucht nur Erinnerung."

### Funktion

**Informationsquelle ausserhalb der Fraktionen.** Rho weiss, was das Tiervolk-Netz weiss — und das ist oft mehr als die Fraktionen wissen, weil das Tiervolk die Stadt von unten kennt. Er ist kein einfacher Informationsbroker: Er gibt Information gegen Vertrauen, nicht gegen Geld. Vertrauen erarbeitet der Spieler durch Handlungen, nicht durch Dialoge.

**Spiegel-Figur für den Spieler.** Rho und der Spieler sind beide Fremde in der Stadt. Rho zeigt, was es bedeutet, jahrelang Fremder zu sein — nicht als Tragödie, sondern als Praxis. Er hat Strukturen entwickelt, um zu überleben. Manche sind schöner als andere.

**Eingang ins Tiervolk-Subnetz.** Für Spieler, die den Tiervolk-Pfad erkunden, ist Rho der Zugangspunkt zu einem Sub-Netz aus NPCs, Informationen und optionalen Szenen, die keine andere Fraktion bietet.

### Widerspruch

Rho präsentiert sich als pragmatisch, neutral, ausserhalb der Fraktions-Logik. Das stimmt teilweise.

Es stimmt nicht, was er mit bestimmten Informationen gemacht hat. Er hat Krone-Schwachstellen an Gilden-Kontakte verkauft. Nicht aus Bösartigkeit — aus Notwendigkeit, aus einer Situation, in der das Tiervolk-Netz bedroht war und er Schutz brauchte. Er hat einen Krone-Offizier kompromittiert, um eine Karawane zu schützen. Der Offizier verlor seine Stelle. Seine Familie wurde mitbeststraft.

Rho weiss das. Er hat es nicht vergessen. Er hat entschieden, dass es nötig war — und er würde es wieder tun.

Der Spieler, der das herausfindet, steht vor einer Figur, die genau das tat, was er möglicherweise selbst getan hat — in einer anderen Quest, für andere Gründe. Das ist kein Zufall. Das ist Spiegel-Funktion.

---

## 6. Offene Figuren (V2-Aufgaben)

Diese Figuren sind als Bedarf identifiziert, aber noch nicht ausgearbeitet. V2 schliesst sie.

| Figur | Funktion | Quest-Verbindung | Priorität |
|---|---|---|---|
| Grenzhauptmann Aldric | Tutorial-Figur (Beat 1, Intro-Quest "Der Gast") | Intro-Tutorial | Hoch |
| Händlerin Sefa | Gildenkontakt, Erstbegegnung | Beat 2, "Die drei Stimmen" | Mittel |
| Ordenspriester (unbenannt) | Ordenskontakt, Erstbegegnung; Krone-Infizierten-Reaktion | Beat 2, "Die drei Stimmen" | Mittel |
| Letzter Krone-Träger | Spur-NPC (möglicherweise nicht mehr lebendig) | Kronenquest Beat 3 | Hoch |
| Novize mit Ordensarchiv-Zugang | Ordensinnenansicht, Zugang für Beat 1 Ordensquest | Ordensquest Beat 1 | Niedrig |

---

## 7. Synchronisation

| Abhängigkeit | Kapitel | Status |
|---|---|---|
| Fraktions-Sprachen und Dialekte | GDD-03, Abschnitt 4.2 | Verlinkt — Dialoge aus GDD-04 ersetzen Platzhalter in GDD-03 |
| Schattenfieber-Seher-Funktion | GDD-03, Abschnitt 3.6 | Maret ist gesetzt — Cassius-Absprache für Seher-Visionen offen |
| Tiervolk-Design | Briefing + Vera GDD-05 | Rhos Äusseres muss mit Vera abgestimmt werden (kein tribal, leicht alien) |
| Kosmologische Figuren-Referenzen | WBB-01 (Emre) | Halvard, Sigvalt, Erthag als Mythos-Figuren integriert — keine eigene Spieler-Begegnung |

---


*Nines hat die Handnotizen zum Seher vom Tisch geworfen. Der Seher hätte das verstanden.*

\clearpage

# GDD-05: Visuelle Designsprache & Art Direction


---

## 1. Art Direction — Überblick

### 1.1 Visuelle Vision

RELICS sieht aus wie eine Welt, die aus einem Körper gewachsen ist — weil sie es ist.

Die Art Direction von RELICS gründet auf einer einzigen kosmologischen Tatsache: Die Welt wurde aus dem Emer geformt, dem Urwesen, dessen Fleisch zu Erde, dessen Blut zu Gewässern, dessen Knochen zu Gebirgen wurde. Die Welt ist kein toter Gegenstand. Sie ist ein verwandelter Organismus. Alles, was die Bewohner des Mittelgrunds bauen, tragen und benutzen, arbeitet mit dem Schöpfungsmaterial selbst — und das sieht man.

Das Leitprinzip heisst **Organische Gotik**: eine Architektur- und Designsprache, in der gotische Monumentalität auf biologische Logik trifft. Gebäude wirken nicht konstruiert, sondern gewachsen. Kleidung ist nicht genäht, sondern gezüchtet. Technologie pulsiert, atmet, reagiert. Nichts in dieser Welt ist mechanisch. Es gibt keine Zahnräder, keine Dampfmaschinen, keine Schaltkreise. Es gibt Adern, Membranen, Nervenknoten und Stoffwechsel.

Die Tonalität ist düster, geerdet und politisch. Gotische Grandeur trifft feudale Brutalität. Aber — und das ist entscheidend — RELICS ist nicht heruntergekommen. Die Welt ist nicht postapokalyptisch. Sie ist futuristisch in einem organischen Sinne: fortschrittlich, ambitioniert, erschreckend elegant. Was hier verfällt, verfällt mit Grandeur. Was hier bluüht, blueht mit Zäähnen.

**Verbindliche Ausschlüsse:**
- Kein Steampunk, keine Zahnrad-Ästhetik, keine mechanische Technologie
- Kein High Fantasy (keine Elfen, Orks, Zauberer mit Stäben)
- Keine Anachronismen (kein Schiesspulver, kein Buchdruck)
- Keine klassische Magie — alles ist Biologie, Chemie, Körper

### 1.2 Ästhetische Säulen

Drei Säulen tragen jede visuelle Entscheidung in RELICS:

**Organik.** Technologie ist gewachsen, nie gebaut. Kabel sind Adern. Displays sind Membranen. Server sind Nervenknoten. Diese Übersetzungslogik ist nicht metaphorisch — sie ist wörtlich. Die Bewohner des Mittelgrunds arbeiten mit dem Emer-Material, dem Stoff, aus dem die Welt besteht. Ihre Technologie sieht aus wie Biologie, weil sie Biologie IST.

**Grandeur.** Alles in RELICS ist monumental. Städte sind vertikal, Thronsäle erdrüeckend, Gildenhaallen kathedralenhaft. Selbst im Verfall bleibt die Grandeur — sie wird nur tragischer. Ein eingestürzter Bogen ist nicht hässlich; er ist eine Ruine, die noch immer Ehrfurcht einflöesst. Die visuelle Sprache lehnt sich an Gaudi, an gotische Kathedralen und an den Brutalismus: Formen, die den Betrachter klein machen.

**Ambivalenz.** Nichts in RELICS ist rein schön oder rein hässlich. Die präachtigste Halle hat Adern unter dem Putz. Das abstossendste Schattenfieber-Gewebe hat eine verstoeoerrende Eleganz. Das Biotech, das den Alltag erleichtert, und das Schattenfieber, das Körper zersetzt, stammen aus derselben Quelle — dem Emer. Der Spieler soll nie sicher sein, ob das, was er sieht, bewundernswert oder beängstigend ist. Idealerweise beides gleichzeitig.

### 1.3 Die Lebende Krone — Visuelles Leitmotiv

Die Lebende Krone, das Relikt dieser Iteration, ist das zentrale Designobjekt von RELICS und gleichzeitig die Verdichtung aller visuellen Prinzipien.

Sie ist ein organisches Artefakt aus der Grossen Flechtung — dem Akt, der die Daseinsebenen trennte. Sie besteht aus dem reinsten Emer-Material: lebendig, pulsierend, reagierend. Wer sie trägt, wird von ihr durchwachsen. Wurzelartige Strukturen dringen in den Schädel, das Nervensystem, den Körper des Trägers. Frühere Träger zeigten minimale Veränderung. Die letzten Träger waren nicht mehr ganz menschlich.

Die Krone ist kein Schmuckstück. Sie ist ein Organismus. Sie wächst. Ihre Oberfläche verändert sich mit der Zeit, mit dem Träger, mit dem Zustand der Hauten. Sie ist gleichzeitig das machtvollste und das gefährlichste Objekt der Welt. Und sie sieht genau so aus: betoeoerrend und zutiefst verstoeoerrend.

**Visuelle Merkmale der Lebenden Krone:**
- Grundform: Asymmetrisch, organisch, nie geometrisch perfekt. Kein Kronenreif — eher ein Geflecht aus Strukturen, die an Knochen, Koralle und Nervenstrang erinnern
- Oberfläche: Transluzent an manchen Stellen, opak an anderen. Unter der Oberfläche pulsieren schwache Lichtimpulse — wie ein langsamer Herzschlag
- Farbgebung: Blasses Elfenbein bis Bernstein, durchzogen von dunkleren Adern. An den Kontaktstellen zum Träger: rötlich, wie frisches Gewebe
- Reaktivität: Die Krone bewegt sich. Nicht viel — aber genug, um den Betrachter zu verunsichern. Feine Härchen oder Fasern an ihrer Unterseite suchen Kontakt
- Transformation: Je länger sie getragen wird, desto mehr verschmilzt sie mit dem Träger. Bei fortgeschrittener Symbiose (oder Parasitismus) sind Krone und Schädel nicht mehr zu trennen

Die Lebende Krone ist der visuelle Beweis für das Leitprinzip von RELICS: Biotech ist kein Werkzeug. Es ist das Schöpfungsmaterial selbst — lebendig, eigenwillig und nie vollständig kontrollierbar.

### 1.4 Referenzkorridor

| Kategorie | Referenz | Was wir übernehmen |
|-----------|----------|---------------------|
| Architektur | Antoni Gaudi (Sagrada Familia) | Organische Kurven, Rippen als Tragwerk, Natur als Konstruktionsprinzip |
| Architektur | Brutalismus (Barbican, Habitat 67) | Schwere, rohe Materialität, Funktion als Ästhetik, Monumentalität |
| Architektur | Gotische Kathedralen | Vertikalität, Strebewerk, Lichtdramatik |
| Mode | Burgundische Hofmode (15. Jh.) | Hennin, Houppelande, Mi-parti, überladene Silhouetten |
| Mode | Alexander McQueen | Skulpturale Silhouetten, Körper als Material, Provokation durch Eleganz |
| Mode | Iris van Herpen | 3D-gedruckte Strukturen, organische Formen, Mode als Organismus |
| Spiele | Elden Ring | Monumentalität, Environmental Storytelling, Raumschöpfung |
| Spiele | Control (Remedy) | Brutalismus als Spielraum, übernatürliche Verfremdung bekannter Räume |
| Spiele | Hollow Knight | Organische Formensprache, Insekten-Eleganz, Atmosphäre durch Silhouette |
| Spiele | Cyberpunk 2077 | Biotech-Integration in Alltag, Körpermodifikation als Normalität |
| Kunst | HR Giger | Verschmelzung von Organischem und Technischem, Biomechanik |
| Kunst | Zdzislaw Beksinski | Düsterer Surrealismus, Körper als Landschaft, Atmosphäre des Unbehagens |

---

## 2. Fraktionsvisuals

### 2.1 Kernprinzip: Drei Dialekte, eine Sprache

Alle drei Fraktionen des Mittelgrunds — die Krone, die Gilden und der Orden — nutzen dasselbe Biotech. Sie arbeiten mit demselben Emer-Material. Ihre Technologie hat denselben biologischen Ursprung. Aber sie nutzen sie völlig unterschiedlich, und das sieht man.

Die Krone verbirgt ihr Biotech hinter Prunk — es sickert durch den Verfall hindurch. Die Gilden stellen ihr Biotech offen zur Schau — es ist Werkzeug, Statussymbol, Infrastruktur. Der Orden leugnet sein Biotech öffentlich — es operiert hinter makellosen Fassaden.

Drei Dialekte, eine Sprache. Der Spieler lernt das Biotech-Vokabular in einer Fraktion und erkennt es dann in den anderen wieder — aber verzerrt, anders betont, mit anderem Subtext. Ein Gilden-Nervenstrang, der offen an einer Hauswand verläuft, ist Infrastruktur. Derselbe Nervenstrang, der unter dem Putz eines Kronenpalasts hervorleuchtet, ist ein Zeichen des Verfalls. Derselbe Nervenstrang, der hinter einer Ordensklostermauer entdeckt wird, ist ein Skandal.

### 2.2 Die Krone — Grandeur im Zerfall

**Leitbild:** Ein Ballsaal, in dem die Wände atmen.

Die Krone ist die älteste Fraktion, die sich am längsten auf das Relikt — die Lebende Krone — beruft. Ihre visuelle Identität spiegelt genau das wider: vergangene Grösse, die unter ihrem eigenen Gewicht nachgibt. Die Krone-Ästhetik ist nie erbärmlich, nie schmuddelig. Sie ist tragisch. Eine Königin in einem Kleid, das atemberaubend schön ist — und an den Saäumen leise zerfällt.

**Architektur:**
Die Architektur der Krone ist Palastgotik: hohe, schlanke Bögen, die einen Anspruch auf Vertikalität formulieren, den die Substanz nicht mehr trägt. Thronsäle mit Deckengewölben, die sich unter dem eigenen Gewicht leicht krümmen. Fassaden aus behaünem Stein, durchzogen von feinen Rissen, durch die ein schwaches, warmes Leuchten dringt — das Biotech, das unter dem Putz lebt.

Die Krone-Gebäude waren einst vollständig versiegelt. Das Biotech unter der Oberfläche war unsichtbar, ein Geheimnis der Baumeister. Aber die Zeit hat die Versiegelung aufgebrochen. Der Verfall entblösst, was verborgen sein sollte: pulsierendes Gewebe unter abgeplatztem Stuck, biolumineszente Adern in gerissenen Wänden, organische Strukturen, die sich durch Fensterrahmen arbeiten. Die Krone versucht, diese Stellen zu reparieren, zu übertünchen, zu verhängen. Es reicht nie ganz.

Einhändige Statuen stehen in den Thronsälen und an den Portalen — Sigvalt, der seine Hand gab, um die Grosse Flechtung zu halten. Die geopferte Hand ist das zentrale Symbol der Krone-Herrschaft: Macht durch Opfer, Pflicht durch Verlust. Die Statuen sind alt, verwittert, aber nie vernachlässigt. Sie werden gepflegt wie Ahnengräber.

Kronleuchter aus Biolumineszenz hängen in den grossen Hallen. Kein Feuer — lebende Lichtorgane, gezüchtet und in Schmiedeeisenrahmen gefasst. Ihr Licht ist warm, leicht goldgelb, aber nie gleichmässig. Es pulsiert kaum wahrnehmbar, wie ein Herzschlag, der langsamer wird.

**Leitform:** Vertikale, schlanke Bögen. Spitze nach oben, schmal wie ein Seufzer. Anspruch auf Höhe, den die Substanz nicht mehr trägt.

**Materialsprache:** Verblasster Samt, angelaufenes Gold, lebendiger Stein. Brokat, dessen Fäden sich bei genauem Hinsehen bewegen. Poliertes Holz, unter dem eine weiche, warme Schicht liegt. Alles in der Krone war einmal prächtiger.

**Ikonographie:**
- Sigvalts geopferte Hand (einhändige Statuen, Handmotiv in Wappen und Siegeln)
- Die Krone selbst als abstrahiertes Symbol — nicht die Lebende Krone, sondern ihre stilisierte Form
- Vertikale Linien, aufwärts gerichtete Spitzen — der Anspruch auf Höhe

### 2.3 Die Gilden — Organischer Brutalismus

**Leitbild:** Eine Fabrik, die lebt.

Die Gilden sind die ökonomische Macht des Mittelgrunds. Sie sehen in der Welt einen Tharm — ein Eingeweide, ein Material, mit dem man arbeiten kann. Ihre visuelle Identität ist ehrlich bis zur Härte: hier wird nichts verborgen, nichts beschönigt, nichts mystifiziert. Biotech ist Infrastruktur. Wenn eine Wand eine Ader braucht, dann sieht man die Ader.

**Architektur:**
Die Gilden-Architektur ist organischer Brutalismus: massiv, funktional, ungeschönt. Schwere horizontale Blöcke aus gegossenem Material, durchzogen von sichtbaren organischen Systemen. Die Gebäude der Gilden atmen. Man kann es sehen — die leichte Ausdehnung und Kontraktion der Fassade, die rhythmische Bewegung der Membranfenster. Man kann es hören — ein tiefes, gleichmässiges Summen in den Wänden. Und wenn man die Hand auf den Beton legt, spürt man Wärme.

Gildenhallen sind kathedralenhaft in ihrem Ausmass, aber völlig anders in ihrer Wirkung. Wo die Krone nach oben strebt, breiten sich die Gilden horizontal aus. Lagerhallen mit frei liegenden Deckenrippen, die wie Brustkörbe aussehen. Marktplätze, deren Bodenfliesen ein feines Netzwerk von Kapillaren zeigen — Nährstofftransport für die lebenden Wände ringsum. Kontore, deren Schreibpulte aus Chitin gefertigt sind und deren Tinten in organischen Behältern pulsieren.

Die Gilden bauen nicht — sie züchten. Ein neues Gebäude wird nicht errichtet, sondern GESETZT. Man legt einen Biotech-Kern in das Fundament und lässt das Gebäude wachsen, geformt durch Leitkulturen und Nährstoff-Lenkung. Der Prozess dauert Jahre. Das Ergebnis ist ein Gebbäude, das lebt, atmet, altert und stirbt. Die Gilden wissen das. Sie kalkulieren die Lebensdauer ein.

**Leitform:** Schwere horizontale Blöcke. Breite Bögen, gedrungene Proportionen. Funktionalität als Ästhetik: Was eine Pumpe ist, sieht aus wie eine Pumpe.

**Materialsprache:** Roher Beton (oder sein organisches Äquivalent — gegossenes Emer-Material), Chitin-Verkleidung, transluzente Membran-Fenster. Metalle nur als Beschlag und Rahmen. Alles hat eine Funktion, nichts ist Dekoration.

**Ikonographie:**
- Erthags Prinzip: die Waage, der Vertrag, der Preis aller Dinge
- Die Flechtung als Handwerksmotiv — verflochtene Linien in Gildenwappen, Knotenornamente
- Horizontale Linien, Symmetrie, Ausgleich — nichts wird umsonst gegeben

### 2.4 Der Orden — Die makellose Lüge

**Leitbild:** Ein Krankenhaus, das dich beobachtet.

Der Orden ist die gefährlichste Fraktion — visuell, weil er die unschuldigste ist. Die Fassaden des Ordens sind geometrisch perfekt, aus geschliffenem Kalkstein, ohne Ornament, ohne sichtbare Technologie, ohne den kleinsten Hinweis auf das, was dahinter liegt. Zisterzienser-Strenge als Architekturprogramm: Reinheit, Klarheit, Kontrolle.

Dahinter liegt etwas anderes.

**Architektur — die Fassade:**
Von aussen sind Ordensgebäude die schönsten Bauwerke des Mittelgrunds. Nicht prunkvoll wie die Krone, nicht wuchtig wie die Gilden — schlicht schön. Perfekte Proportionen, weisser Stein, Kreuzgänge mit sanftem Lichteinfall. Klostergärten, in denen medizonische Krauter wachsen. Bibliotheken mit Holzregalen und Pergamentbüchern. Schulräume mit Kreidewänden. Der Orden bildet aus. Der Orden heilt. Der Orden bewahrt Wissen. Das ist die Botschaft der Architektur, und sie ist nicht gelogen — sie ist nur nicht die ganze Wahrheit.

**Architektur — dahinter:**
Hinter den makellosen Fassaden betreibt der Orden die fortschrittlichste Biotech-Forschung des Mittelgrunds. Die Innenbereiche, zu denen nur hohe Ränge Zugang haben, sind ein Negativbild der Fassade: Nervenstrang-Korridore, Wände aus pulsierendem Gewebe, Räume, in denen organische Überwachungsnetze jeden Schritt registrieren. Augen in den Wänden. Ohren in den Böden. Ein Netzwerk aus lebendem Sensorgewebe, das den Orden über alles informiert, was in seinen Mauern geschieht.

Die Ordensarchitektur hat zwei Schichten, und der Übergang zwischen ihnen ist das spannendste architektonische Element in RELICS. Es gibt Türen, hinter denen der weisse Kalkstein plötzlich in feuchtes, warmes Gewebe übergeht. Korridore, die als ordentliche Kreuzgänge beginnen und in organische Tunnel münden. Treppen, deren Stufen ab einer gewissen Tiefe nicht mehr aus Stein bestehen, sondern aus etwas, das unter dem Fuss leicht nachgibt.

**Halvards Symbolik:**
Das zentrale Symbol des Ordens ist Halvards Auge — das geopferte Auge des Halvard, der es gab, um die Flechtung zu SEHEN. Das verbliebene Auge sah die Welt. Das geopferte Auge sah das Hohlicht — für immer. Halvards Raben sind das allgegenwärtige Motiv: in Steinrelief an den Fassaden, als Wetterfahnen auf den Dächern, als Stickerei auf den Roben. Die Raben sind Halvards Augen in der Welt — und die Orden-Architektur spiegelt genau das wider: eine Struktur, die alles sieht.

Das Augenmotiv taucht in der Geheimarchitektur öffentlich auf. Nicht als Dekoration — als Funktion. Die organischen Sensorknoten in den Wänden SIND Augen: biologische Überwachungsorgane, die registrieren, filtern, weiterleiten. Wer die Geheimebene des Ordens betritt, wird von Dutzenden dieser Augen beobachtet. Sie blinzeln.

**Leitform:** Perfekte Symmetrie aussen, organisches Chaos innen. Kreise, Bögen, gleichmässige Proportionen — die geometrische Perfektion, die nur durch vollständige Kontrolle möglich ist.

**Materialsprache:** Geschliffener Kalkstein (aussen), Messing-Akzente für Beschläge und Instrumente. Dahinter: pulsierendes Gewebe, Nervenstrangbündel, organische Membranen. Der Kontrast zwischen Fassade und Innerem ist das stärkste visuelle Statement des Ordens.

**Ikonographie:**
- Halvards Auge (das geopferte Auge als zentrales Symbol, allgegenwärtig)
- Halvards Raben (Überwachung, Wissen, Präsenz)
- Geschlossene Formen — Kreise, konzentrische Ringe, das Auge als Form

---

## 3. Biotech-Grammatik

### 3.1 Das Prinzip

Biotech in RELICS ist keine Metapher. Es ist die logische Konsequenz einer Welt, die aus einem lebenden Körper geformt wurde. Wenn die Erde Fleisch ist, die Flüsse Blut, die Berge Knochen — dann ist jede Technologie, die mit diesem Material arbeitet, zwangsläufig biologisch. Die Bewohner des Mittelgrunds haben über Generationen gelernt, das Emer-Material zu kultivieren, zu züchten, zu formen. Sie nennen es nicht "Technologie". Für sie ist es Handwerk, Heilkunde, Alchemie. Aber für den Spieler — und für uns als Gestalter — ist es Biotech.

### 3.2 Übersetzungsregeln

Jedes technologische Element der realen Welt hat ein organisches Äquivalent in RELICS. Diese Übersetzung ist verbindlich für alle Assets:

| Reale Technologie | RELICS-Äquivalent | Visuelle Umsetzung |
|---|---|---|
| Kabel, Leitungen | Adern, Sehnen | Pulsierende Stränge unter/auf Oberflächen, erkennbarer Flüssigkeitstransport |
| Displays, Anzeigen | Membranen | Transluzente, biolumineszente Flächen, die Muster zeigen (keine Pixel, sondern organische Leuchtmuster) |
| Server, Datenspeicher | Nervenknoten, Ganglien | Kompakte organische Verdickungen an Knotenpunkten, warm, leicht pulsierend |
| Energieleitung | Stoffwechsel, Nährlösung | Sichtbarer Flüssigkeitstransport in Adern, Farbe verändert sich mit Energiegehalt |
| Sensoren, Kameras | Augen, Härchen, Poren | Organische Sensororgane: Augen (Orden), Härchen die auf Berührung reagieren (Gilden), Poren die Stoffe aufnehmen (Krone) |
| Beleuchtung | Biolumineszenz | Leuchtorgane in verschiedenen Formen — Kugeln, Stränge, Flächen. Fraktionsabhängig in Farbtemperatur |
| Türen, Schleusen | Sphinkter, Membranen | Organische Öffnungen, die sich dehnen und zusammenziehen. Geschlossene Membranen als Türen (Gilden), Steintüren mit organischem Schloss (Krone/Orden) |
| Heizung, Klimatisierung | Körperwärme, Stoffwechsel | Gebäude regulieren ihre Temperatur selbst. Wände strahlen Wärme ab. Bei Kälte ziehen sich Öffnungen zusammen. |

### 3.3 Sichtbarkeitsgrade

Die Sichtbarkeit von Biotech ist die wichtigste Differenzierung zwischen den Fraktionen. Dieselbe Technologie sieht in drei verschiedenen Kontexten völlig unterschiedlich aus:

| Grad | Krone | Gilden | Orden |
|------|-------|--------|-------|
| **Versteckt** | Standard — Biotech gehört unter den Putz | Selten — warum verstecken, was funktioniert? | Öffentliche Norm — der Orden LEUGNET Biotech |
| **Sichtbar** | Nur bei Verfall — das Verborgene dringt durch | Standard — offen, funktional, pragmatisch | Nur intern — in den Geheimebenen, hinter verschlossenen Türen |
| **Dominant** | Nie — wäre ein Eingeständnis des Verfalls | Prestigebauten — die Gildenhalle als atmendes Monument | Geheime Labore — hier ist die Biologie total, Architektur existiert nicht mehr |

### 3.4 Skala

Biotech existiert auf drei Skalen, und jede hat eigene Designregeln:

**Mikro (Körper und Gegenstände):** Biotech in Kleidung, Schmuck, Werkzeug, Waffen. Feine Adern in Lederhandschuhen. Ein Schwertgriff, der sich der Hand anpasst. Ein Amulett, das warm wird, wenn der Träger krank ist. Auf dieser Skala ist Biotech intim, persönlich, fast unauffällig.

**Meso (Möbel und Räume):** Biotech in Türen, Möbeln, Beleuchtung, Raumkontrolle. Membrantüren in Gildenhäusern. Leuchtorgane in Krone-Kronleuchtern. Organische Schlossmeechnismen in Ordensarchiven. Auf dieser Skala wird Biotech raumbildend: es definiert, wie ein Raum funktioniert, sich anfühlt, reagiert.

**Makro (Gebäude und Infrastruktur):** Biotech in Architektur, Stadtinfrastruktur, Verteidigung. Gebäude, die atmen (Gilden). Stadtmauern, die Wunden heilen (Krone). Überwachungsnetzwerke, die eine ganze Festung durchziehen (Orden). Auf dieser Skala ist Biotech die Stadt selbst. Die Grenze zwischen Gebäude und Organismus verschwindet.

---

## 4. Farbsystem

### 4.1 Grundprinzip: 70/20/10

Jede Fraktionspalette folgt der 70/20/10-Regel: 70% Basis (die dominante Stimmung), 20% Akzent (die Fraktionsidentität), 10% Highlight (das Besondere, Seltene, Auffällige). Diese Verteilung ist verbindlich für alle Assets — Environments, Charaktere, UI-Elemente.

### 4.2 Fraktionspaletten

**Die Krone**

| Rolle | Farbe | Hex | Verwendung |
|-------|-------|-----|------------|
| 70% Basis | Aschgrau | `#3D3D3D` | Stein, Schatten, verwitterte Flächen, Hintergrund |
| 20% Akzent | Karmin | `#8B1A2B` | Wappen, Textilien, Biotech-Glow unter dem Putz, Blut |
| 10% Highlight | Altgold | `#C5A030` | Kronenreste, Ornamente, Biolumineszenz in Thronsälen |

Das Karmin der Krone ist WARM — es erinnert an altes Blut, an Samt, an das Leuchten unter der Haut. Es ist nie grell. Es ist die Farbe von etwas, das einmal lebendig war und langsam erkaltet. Das Altgold erscheint nur in Momenten: ein Kronleuchter, ein Wappen, ein Sonnenstrahl auf einem vergoldeten Rahmen. Es ist die Erinnerung an bessere Zeiten.

**Die Gilden**

| Rolle | Farbe | Hex | Verwendung |
|-------|-------|-----|------------|
| 70% Basis | Warmer Beton | `#7A6E5D` | Architektur, Böden, Arbeitsflächen, Alltag |
| 20% Akzent | Amber | `#C49A20` | Handel, Licht, Reichtum, biologische Flüssigkeiten |
| 10% Highlight | Cyan | `#2EC4B6` | Biotech-Flüssigkeit in Adern, aktive Membranen, Gildenstempel |

Amber und Cyan bilden ein komplementäres Spannungsfeld. Das Amber steht für Handel, Wärme, Profit — alles, was die Gilden nach aussen zeigen. Das Cyan ist die Farbe des Biotech im Betrieb: die Flüssigkeit in den Adern, das Leuchten aktiver Membranen, der Stoff, mit dem gearbeitet wird. Zusammen erzeugen sie eine Palette, die gleichzeitig einladend und industriell wirkt.

**Der Orden**

| Rolle | Farbe | Hex | Verwendung |
|-------|-------|-----|------------|
| 70% Basis | Kalkweiss | `#E8E4DE` | Fassade, Reinheit, Kontrolle, die öffentliche Seite |
| 20% Akzent | Schieferblau | `#4A5568` | Roben, Schatten, Autorität, Strenge |
| 10% Highlight | Bernstein | `#D4A017` | Geheime Biotech-Anlagen, Warnfarbe, das Verborgene |

Die Palette des Ordens hat eine doppelte Lesart. Von aussen: Kalkweiss und Schieferblau — kuühl, ruhig, vertrauenswuerdig. Die Farben einer Institution, der man seine Kinder anvertraut. Von innen: Bernstein — die Farbe des versteckten Biotech, der warme, beunruhigende Kontrast zum kuühlen Äusseren. Bernstein ist die Farbe von Harz, von eingeschlossenem Leben, von Dingen, die konserviert und kontrolliert werden. Wenn der Spieler im Orden Bernstein sieht, weiss er: hier beginnt die Wahrheit.

### 4.3 Globale Akzente

Bestimmte Farben gehören keiner Fraktion, sondern der Welt:

| Kontext | Farben | Hex | Bedeutung |
|---------|--------|-----|-----------|
| Schattenfieber | Violett-Schwarz + Giftgrün | `#2D0A31` + `#39FF14` | Kosmologische Erosion, krank-organisch, ALARM |
| Wildnis | Moosgrün, Erdtoene, Nebel-Grau | `#5C6B3C`, `#8B7355`, `#9E9E9E` | Natur jenseits der Fraktionen, der Mittelgrund als Landschaft |
| Tiervolk | Ocker, Terrakotta, Sand | `#CC7722`, `#C04000`, `#C2B280` | Warme Naturtoene, fremd aber nicht bedrohlich |

### 4.4 Farbregeln

**Regel 1: Fraktionsfarben mischen sich nicht.** Der Spieler erkennt Zugehörigkeit an der Palette. Kein Krone-Gebäude hat Cyan-Akzente. Kein Gilden-Kontor hat Karmin-Textilien. Die Farbsprache ist eindeutig und nicht verhandelbar.

**Regel 2: Übergangszonen sind neutral.** Märkte, Grenzgebiete, Karawanenwege nutzen die neutrale Wildnis-Palette. Hier treffen sich die Fraktionen, und die Abwesenheit von Fraktionsfarben macht das visuell spürbar.

**Regel 3: Schattenfieber bricht JEDE Palette.** Egal welche Fraktionsfarben einen Raum dominieren — wenn das Schattenfieber einbricht, überschreibt Violett-Schwarz plus Giftgrün alles. Das ist das stärkste visuelle Alarmsignal in RELICS: Wenn sich die Farben ändern, stimmt etwas fundamental nicht.

**Regel 4: Die Lebende Krone hat keine Fraktionsfarbe.** Die Krone ist älter als alle Fraktionen. Ihre Farben — Elfenbein, Bernstein, dünkle Adern — gehören nur ihr. Wenn sie in einer Szene auftaucht, ist sie farblich fremd. Das ist Absicht.

**Hinweis für Shader-Implementation (V2, ACES-Validiert):** Alle Hex-Codes in diesem Dokument sind sRGB-Werte, kalibriert für Ü5-Rendering mit aktivem ACES-Tonemapping. ACES hebt Mitteltöne und sättigt Farben leicht ab — warme Toene (Altgold `#C5A030`, Amber `#C49A20`, Bernstein `#D4A017`) sind bewusst tiefer gesetzt als Display-Normal, um nach ACES-Kompression korrekt zu erscheinen. Giftgrün (`#39FF14`) ist HDR-intensiv — soll im SDR-Bereich saturiert wirken, im HDR-Bereich leuchten. Keine Abweichungen von diesen Werten ohne Abstimmung mit Vera und Tobi.

---

## 5. Mode & Rüstung

### 5.1 Leitprinzip: High Fashion Mittelalter + Biotech-Layer

Mode in RELICS ist kein Nebenprodukt. Sie ist ein Erzählmedium. Was ein Charakter trägt, sagt dem Spieler: zu welcher Fraktion gehört er, wie wohlhabend ist er, wie viel Biotech hat er Zugang, und — bei fortgeschrittenem Schattenfieber — was passiert mit seinem Körper.

Die Basis ist die burgundische Hofmode des 15. Jahrhunderts: Hennin (die hohen, spitzen Hauben), Houppelande (die weiten, bodenlangen Übergewänder), Mi-parti (die längsgeteilten Farben). Diese historische Grundlage wird durch einen Biotech-Layer erweitert: organische Elemente, die in die Kleidung integriert sind — nicht als Ersatz, sondern als Erweiterung.

Biotech in der Mode ist ein Statussymbol. Wie bei Schmuck: Wer es sich leisten kann, trägt Kleidung, die lebt. Ein Kragen, dessen Stoff sich der Körpertemperatur anpasst. Handschuhe mit feinen Adern, die den Puls des Trägers spüren. Ein Umhang, der bei Wind seine Dichte verändert. Das ist Luxus, keine Notwendigkeit — und genau deshalb erzählt es Geschichten.

### 5.2 Fraktionsmode

**Krone — Zeremoniell, überladen, fragil:**
Die Krone-Mode ist der sichtbarste Ausdruck des Verfalls. Äusserlich: atemberaubend. Samt und Brokat in Karmin und Altgold, Schichtung über Schichtung, Silhouetten, die Raum beanspruchen. Die Houppelande der hohen Krone-Adeligen sind so weit, dass sie Türen fuellen. Die Hennin so hoch, dass sie bei jedem Schritt leicht schwanken.

Darunter — wer genau hinsieht — lebt etwas. Die Unterkleidung der Krone-Elite ist organisch: ein eng anliegender Anzug aus lebendem Gewebe, das den Körper stützt, wärmt und — bei den Ältesten — zusammenhält. Die prächtigen Obergewänder verbergen, dass manche Krone-Adelige ihren Körper ohne dieses Biotech-Korsett nicht mehr aufrecht halten könnten. Die Mode ist Fassade, die Biotech-Unterschicht ist Notwendigkeit.

**Gilden — Pragmatisch-elegant:**
Die Gilden tragen Mode als Investition. Leder und Chitin-Panzerung, präzise geschnitten, sichtbar teuer, aber nie verschwendereisch. Gilden-Mode sagt: Ich bin erfolgreich, und ich kann es mir leisten, gut auszusehen, während ich arbeite.

Biotech ist offen integriert: verstärkte Nähte aus organischem Material, Taschen mit Membranverschlüssen, Stiefel mit Sohlen, die sich dem Untergrund anpassen. Die reichsten Gildenhändler tragen Umhänge aus gezüchtetem Stoff — ein Material, das kein Weber herstellen kann, sondern nur ein Biotech-Züchter. Das ist der Gilden-Luxus: nicht Dekoration, sondern überlegene Funktion.

**Orden — Asketisch-uniform:**
Die Roben des Ordens sind weiss, bodenlang, ohne Verzierung. Schieferblau für die Umhänge, Messing für die Schnallen. Die niedrigen Ränge sehen alle gleich aus. Das ist Absicht. Der Orden verlangt Selbstauflösung — die Individualität verschwindet hinter der Uniform.

Die hohen Ränge tragen dasselbe — aber wer genau hinsieht, bemerkt Details. Ein leicht unnatürlich glattes Gesicht. Hände, die keine Falten haben. Augen, die im falschen Licht bernsteinfarben schimmern. Die Biotech-Implantate des Ordens sind nicht sichtbar — sie sind unter der Haut. Subdermal. Nahtlos. Die makellosen Körper der hohen Ordensvertreter sind ihr bestgehütretes Geheimnis und ihr offensichtlichstes Zeichen — für den, der hinzusehen weiss.

### 5.3 Rüstungsphilosophie

Rüstung in RELICS ist nicht geschmiedet — sie ist gezüchtet. Organische Panzerung aus kultiviertem Chitin, gehärtetem Kollagen und verstärkten Sehnenstrukturen. Keine Plattenrüstung, keine Kettenhemden im klassischen Sinne. Die Schutzbekleidung der Welt folgt derselben biologischen Logik wie alles andere.

**Leichte Rüstung:** Verstärkte Kleidung mit eingewachsenen Chitin-Platten an kritischen Stellen. Flexibel, leise, unauffällig. Gilden-Söldner und Tiervolk bevorzugen diesen Typ.

**Mittlere Rüstung:** Vollständige Chitin-Schale über einem organischen Unterbau. Die Platten sind ineinander verzahnt wie ein Exoskelett. Beweglich, aber deutlich sichtbar als Rüstung. Standard für Krone-Soldaten.

**Schwere Rüstung:** Dickes, mehrschichtiges organisches Material — fast wie ein zweiter Körper. Die Rüstung wächst um den Träger herum und muss regelmässig genährt werden (Nährlösung, Pflege). Ordensritter und Elite-Kronengarden tragen diesen Typ. Er ist beeindruckend und leicht verstoeoerrend: die Grenzen zwischen Träger und Rüstung verschwimmen bei längerem Tragen.

**Gezüchtete Rüstung als Luxusgut:** Die Gilden kontrollieren die Zucht der besten Rüstungsmaterialien. Eine massgeschneiderte Gilden-Rüstung ist ein Vermögen wert — und ein Statussymbol. Sie passt sich dem Träger an, heilt kleine Beschädigungen selbst und wächst mit (bis zu einem gewissen Grad). Wer eine solche Rüstung trägt, sagt damit: Ich bin die Investition wert.

**OFFEN:** Detaillierte Rüstungsklassen und ihre Kampf-Mechanik — Abstimmung mit Leo (GDD-02) und Darius erforderlich. Visuelle Differenzierung der Rüstungsstufen in Concept Art: V3.

### 5.4 Spieler-Customization & Dominanzprinzip

Der Spielercharakter kann Rüstung und Kleidung individuell kombinieren (CD-Vorgabe). Das System muss visuell lesbar bleiben: Fraktionszugehörigkeit, Rüstungsklasse und Schattenfieber-Status müssen auf einen Blick erkennbar sein, auch bei frei kombinierten Sets.

**Dominanzprinzip — Torso-Primat:**

Die Fraktionszugehörigkeit eines Outfits wird durch den Torso-Slot definiert. Der Torso ist der visuell dominanteste Körperbereiche im Third-Person-Spiel — er ist immer sichtbar, er trägt die grösste Fläche an Fraktionsfarben und Ikonographie.

| Kombination | Visuelles Ergebnis | Fraktionslesbarkeit |
|-------------|-------------------|---------------------|
| Torso Fraktion A + alle anderen Slots Fraktion A | Reine Fraktion | Eindeutig Fraktion A |
| Torso Fraktion A + bis zu 2 Slots Fraktion B | Fraktion A mit Akzenten | Fraktion A erkennbar, B als Kontrast lesbar |
| Torso Fraktion A + 3+ Slots Fraktion B | Gemischtes Set | Visuell neutral — Händler-Lesart, keine eindeutige Fraktionszugehörigkeit |
| Torso neutral (Tiervolk/Wildnis) + beliebige Slots | Neutrales Set | Kein Fraktionssignal |

**Schattenfieber überschreibt das Dominanzprinzip.** Ab Infektionsstufe 2 (Risse, Wert 41+) sind am Körper des Spielers Schattenfieber-Zeichen sichtbar — unabhängig davon, welches Outfit getragen wird. Die Fraktionszugehörigkeit bleibt lesbar, aber das Schattenfieber-Signal ist dominant. Kein Outfit verbirgt fortgeschrittene Infektion.

**NPC-Reaktion auf gemischte Sets:** NPCs lesen Fraktionszugehörigkeit am Outfit. Gemischte Sets erzeugen ambivalente NPC-Reaktionen — kein Fraktions-Bonus, kein Fraktions-Malus. Das können erfahrene Spieler gezielt einsetzen, um Fraktionssignale zu neutralisieren. Design-Entscheidung: Das ist kein Bug, sondern eine Spieloption.

---

## 6. Tiervolk — Visuelle Identität

### 6.1 Leitprinzip: Alien-Elegant, nicht Tribal

Das Tiervolk ist fremd. Nicht fremdartig wie ein Fantasywesen aus einem Kinderbuch — fremd wie etwas, das fast menschlich ist, aber nicht ganz. Die Differenz ist subtil und genau deshalb verstoeoerrend. Die CD-Vorgabe ist klar: "Leicht alien vs. menschlich clean." Das Tiervolk soll den Spieler faszinieren und leicht verunsichern, nie abstossen und nie verharmlosen.

Das Tiervolk hat keine eigene Architektur. Sie sind Nomaden, Gäste in den Fraktionsstädten. Händler und Diebe, keine Handwerker. Sie bauen nicht — sie bewegen sich. Ihre visuelle Identität liegt deshalb vollständig in ihren Körpern, ihrer Kleidung und ihren Objekten.

### 6.2 Körperdesign

Die Tier-Merkmale des Tiervolks sind nicht offensichtlich. Kein Fellkörper, keine Schnauze, keine Schweife. Stattdessen: Pupillenformen, die nicht menschlich sind — schlitzfoerrmig, horizontal, sternfoermig. Hautstrukturen, die an Schuppen, Federn oder feinstes Fell erinnern, aber erst bei Nähe sichtbar werden. Proportionen, die knapp daneben liegen: Finger ein Gelenk zu lang, Hälse etwas zu beweglich, Schultern in einem Winkel, der menschlich nicht funktionieren wüerde.

Kein Mitglied des Tiervolks sieht aus wie ein bestimmtes Tier. Die Merkmale sind gemischt, individuell, irreduzibel. Sie erinnern an ETWAS — aber der Spieler kann nie genau sagen, woran. Das ist der Kern des Designs: das Unheimliche im Fast-Vertrauten.

Bewegungsmuster verstärken den Effekt. Ein Tiervolk-Händler dreht den Kopf eine Spur zu weit. Eine Tiervolk-Diebin bewegt sich mit einer Geschmeidigkeit, die kein Mensch hat. Ein Tiervolk-Ältester sitzt in einer Haltung, die bequem aussieht, aber für ein menschliches Skelett unmöglich wäre. Das sind keine grossen Gesten — es sind Details, die sich addieren.

### 6.3 Kleidung & Schmuck

Die Kleidung des Tiervolks erzählt ihre Geschichte: zusammengesammelt aus allen Fraktionen, zusammengetragen auf Wanderungen, umgearbeitet mit eigenen Techniken. Ein Tiervolk-Händler trägt vielleicht einen Krone-Samtumhang über Gilden-Lederstiefeln, befestigt mit Orden-Messingschnallen. Die Kombination ist eklektisch, nie zufällig — sie verrät, in welcher Fraktionsstadt er zuletzt war, mit wem er gehandelt hat, wo er willkommen war.

Daneben existiert eine eigene Schmucktradition: Knochen, Bernstein, Flusskiesel, gefundene Biotech-Fragmente. Die Fragmente sind besonders aussagekräftig — das Tiervolk sammelt abgestorbene oder abgefallene Biotech-Stücke und verarbeitet sie zu Schmuck. Was für die Fraktionen Abfall ist, wird für das Tiervolk Ornament. Das ist kein Primitivismus — es ist eine andere Wertschätzung desselben Materials.

### 6.4 Farbpalette

Warme Naturtoene als Basis: Ocker (`#CC7722`), Terrakotta (`#C04000`), Sand (`#C2B280`). Diese Palette setzt sich von allen drei Fraktionspaletten ab und signalisiert sofort: hier ist jemand, der keiner Fraktion gehört. In ihrem Eigendesign — dem, was nicht von Fraktionen zusammengetragen ist — verwendet das Tiervolk keine Fraktionsfarben. Kein Karmin, kein Amber, kein Kalkweiss. Ihre Farben sind die Farben der Wege zwischen den Städten: Staub, Lehm, Sonnenbraun.

---

## 7. Schattenfieber — Visuelle Manifestation

### 7.0 Referenztabelle: Stufen und Grenzen

> Diese Tabelle ist verbindlich und identisch in GDD-02, GDD-03 und GDD-05. Keine Abweichungen. (CD-Entscheidung, Tag 4, Szene 3.)

| Infektionswert | Narrativer Zustand (Nami/GDD-03) | Mech. Stufe (Darius/GDD-02) | Visueller Status (Vera/GDD-05) |
|---------------|----------------------------------|------------------------------|-------------------------------|
| 0 | Gesund | Stufe 0 — Rein | Stufe-0-Baseline: keine Schattenzeichen |
| 1–40 | Rauschen | Stufe 1–2 (Gezeichnet/Infiziert) | Subtile Schattenzeichen, schwaches Schimmern |
| 41–75 | Risse | Stufe 3 (Verwandelt) | Sichtbare Schattenzeichen, Körperveränderung |
| 76–100 | Schwelle | Stufe 4 (Entfesselt) | Erschreckende Transformation, Körpergrenze uneindeutig |

Halluzinations-Start: Wert 76 (Beginn Stufe 4/Schwelle).

### 7.1 Leitprinzip: Die falsche Organik

Biotech ist schöen-organisch. Schattenfieber ist krank-organisch. Beide stammen aus derselben Quelle — dem Emer-Material —, aber das Schattenfieber ist die unkontrollierte Variante, und das sieht man. Wo Biotech pulsiert, zuckt das Schattenfieber. Wo Biotech wächst, wuchert das Schattenfieber. Wo Biotech leuchtet (in Amber, Cyan, Altgold), glüeht das Schattenfieber in FALSCHEN Farben: Violett-Schwarz (`#2D0A31`) und Giftgrün (`#39FF14`).

Das Schattenfieber-Farbsignal ist das stärkste visuelle Alarmsignal in RELICS. Es bricht jede bestehende Palette, jede Fraktionsästhetik, jede architektonische Ordnung. Wenn der Spieler in einem Krone-Palast Giftgrün sieht, weiss er sofort: etwas ist sehr falsch. Das Signal muss unmissverständlich sein — kein subtiler Übergang, sondern ein visueller Bruch.

### 7.2 Vier visuelle Zustände

**Stufe 0: Baseline — Rein (Infektionswert 0)**

Der uninfizierte Spieler ist die visuelle Nulllinie. Alles, was Schattenfieber ab Wert 1 zeigt, definiert sich als Abweichung von diesem Zustand.

Am Körper: Keine Auffälligkeiten. Normale Hautfarbe, normale Pupillen, normale Schatten. Das Nervensystem-UI (GDD-02, Kap. 3) zeigt alle vier Äste in vollem, klarem Licht — keine Schatten-Überlagerungen, kein Violett-Schwarz. Augen reagieren normal auf Licht. Schatten fallen korrekt.

In der Umgebung: Der Spieler sieht nur die erste Schicht der Welt. Verstecktes Biotech ist unsichtbar. Emotionen von NPCs sind nicht ablesbar. Schattenfieber-Zonen sind erkennbar durch physische Warnsignale (Geruch, Temperatur, Licht) — aber nicht durch Schattensinne.

Gameplay-Relevanz: Stufe 0 ist kein Nachteil — sie ist ein anderer Spielstil. Volle Systemeffizienz aller Nervensystem-Äste (Cardio, Muskel, Lymph). Volle Alchemie-Wirksamkeit. Keine sozialen Einschränkungen. Das Stufe-0-Äquivalent zu Schattensinnen ist Alchemie plus Trainerfähigkeiten — andere Mittel, gleichwertiger Spielraum.

**Rauschen: Infektionswert 1–40**

Am Körper: Subtil. Adern unter der Haut, die leicht dunkler erscheinen als normal. Bei bestimmten Lichtwinkeln ein schwaches violettes Schimmern auf der Haut. Pupillen, die in Schattenzonen kurz aufleuchten — ein grünlicher Reflex, wie Katzenaugen im Dunkeln. Nichts davon ist auf den ersten Blick sichtbar. Man muss wissen, worauf man achtet.

In der Umgebung: Fast unsichtbar. Kerzen flackern etwas länger, bevor sie erlöschen. Schatten fallen in leicht falsche Richtungen. An verseuchten Orten: ein feiner violetter Dunst über dem Boden, Pflanzen, deren Blätter sich einrollen. Der Spieler bemerkt es vielleicht nicht bewusst — aber die Atmosphäre ändert sich.

**Risse: Infektionswert 41–75**

Am Körper: Sichtbar. Die Hautstruktur verändert sich — nicht überall, aber an exponierten Stellen. Die Adern treten hervor und pulsieren in einem eigenen Rhythmus, der nicht zum Herzschlag passt. An den Händen, am Hals, im Gesicht erscheinen asymmetrische Muster: Verdickungen, Verfärbungen, Strukturen, die an Narben erinnern, aber wachsen. Schatten um den Betroffenen verhalten sich FALSCH — sie sind zu lang, zu dunkel, zu beweglich.

In der Umgebung: Unübersehbar. Schattenfieber-Zonen haben eine klare visuelle Grenze: eine Linie, an der die Farben entsättigen, das Licht kippelt, die Flora mutiert. Innerhalb der Zone: Bäume mit Wucherungen, Steine, die schwitzen, Gras, das in giftgrünen Adern leuchtet. Die Luft ist dichter. Partikel schweben, die kein Staub sind.

**Schwelle: Infektionswert 76–100**

Am Körper: Erschreckend. Die Körpergrenze des Betroffenen wird uneindeutig. Gewebe dehnt sich über die natürliche Silhouette hinaus — Fasern, Ranken, dünne Stege aus organischem Material, die den Körper mit der Umgebung zu verbinden scheinen. Bei Kontakt lösen sie sich auf, wachsen aber nach. Die Haut ist stellenweise transluzent — darunter leuchtet es schwach giftgrün. Die Augen sind vollständig verändert: keine menschliche Iris mehr, sondern ein gleichmässiges Leuchten.

In der Umgebung: Totalbefall. Die Grenze zwischen "gesund" und "befallen" existiert nicht mehr in diesen Zonen. Die gesamte Umgebung ist transformiert: Gebäude, die von organischem Material überwuchert sind, Böden, die nachgeben wie Haut, Lichtquellen, die in Violett-Schwarz und Giftgrün pulsieren. Die Luft zittert. Die Physik scheint FALSCH — Wasser fliesst in die falsche Richtung, Schatten bewegen sich eigenständig, die Schwerkraft hat Aussetzer. Die Hauten zwischen den Daseinsebenen sind hier dünn, und man sieht es.

### 7.3 Designregeln für Schattenfieber

**Regel 1: Schattenfieber ist KEIN Biotech.** Biotech ist kontrolliert, funktional, gewollt. Schattenfieber ist unkontrolliert, parasitär, kosmologisch. Obwohl beide aus dem Emer-Material stammen, müssen sie visuell klar unterscheidbar sein. Biotech hat warme, natürliche Toene (Amber, Cyan, Elfenbein). Schattenfieber hat kalte, unnatürliche Toene (Violett-Schwarz, Giftgrün). Biotech pulsiert gleichmässig. Schattenfieber zuckt, flackert, stoesst.

**Regel 2: Schattenfieber ist NIE schön.** Biotech darf ästhetisch ansprechend sein — die Ambivalenz liegt in der Funktion, nicht in der Form. Schattenfieber dagegen darf nie schön aussehen. Es kann FASZINIEREND sein, es kann IMPOSANT sein, aber nie in einer Weise, die der Spieler als angenehm empfindet. Das visuelle Unbehagen ist die Hauptfunktion.

**Regel 3: Schattenfieber bricht Regeln.** Die visuellen Regeln, die für den Rest der Welt gelten — Farbpaletten, Lichtlogik, Physik —, gelten in Schattenfieber-Zonen nicht. Das ist die stärkste visuelle Aussage: hier endet die Ordnung. Die Flechtung versagt. Die Hauten werden dünn. Das Galt — der Urzustand VOR aller Differenzierung — scheint durch.

---

## 8. Environments & Architektur

### 8.1 Leitprinzip: Der Mittelgrund als lebender Körper

Die bewohnte Welt — der Mittelgrund — ist kein unbelebter Schauplatz. Sie ist der verwandelte Körper des Emer, und die Bewohner haben sich darauf eingerichtet, AUF und IN einem Organismus zu leben. Das Environment Design spiegelt das wider: Landschaften, die subtil organisch wirken. Felsen, deren Maserung an Muskelgewebe erinnert. Flüsse, deren Verlauf sich über Jahrzehnte leicht verändert — wie Adern, die sich verlagern. Höhlen, die wie Organe geformt sind.

Diese organischen Untertoene sollen nie offensichtlich sein. Der Mittelgrund sieht auf den ersten Blick aus wie eine mitteleuropäische Landschaft: dichte Wälder, sanfte Hügel, neblige Täler, schroffe Gebirge. Erst auf den zweiten Blick — oder mit Schattensinnen — werden die Emer-Strukturen sichtbar: die Textur im Fels, das Muster im Boden, der Puls im Wasser.

### 8.2 Vertikalität als Designprinzip

Jede besiedelte Zone in RELICS nutzt die vertikale Achse. Städte sind dreidimensionale Räume: begehbare Dachlandschaften, Kellergewölöbe, Kanalisation, Brücken zwischen Gebäuden, Türme, Aufzüge (organisch — Kapseln, die an Sehnen hoch- und runtergezogen werden). Der Spieler soll immer drei Optionen haben: oben, unten, durch.

Vertikalität ist auch ein Statussignal. In Krone-Städten wohnen die Mächtigen OBEN — in den Türemen und Söollern, nahe am Himmel, nahe an Sigvalts Höhe. In Gilden-Städten wohnen die Mächtigen auf der ERDE — nah am Markt, nah am Tharm. In Ordensstädten wohnen die Mächtigen UNTEN — in den Gewölöben, den Archiven, den geheimen Laboratorien.

### 8.3 Regionstypen

**Krone-Stadt: Verfallende Pracht.**
Enge, vertikale Gassen unter riesigen gotischen Bögen. Palastbezirke mit Fassaden, die einmal weiss waren und jetzt von Rissen und Biotech-Durchbrüchen gezeichnet sind. Hohe Türme mit biolumineszenten Kronleuchtern, die nachts die Stadt in warmes Karmin-Gold tauchen. Statuen von Sigvalt an jeder Kreuzung — einhändig, verwittert, von niemandem missachtet. Die Strassen sind gepflastert, aber die Fugen leuchten schwach: die Adern unter der Stadt sind hier nah an der Oberfläche. Vorhallen, in denen Wandteppiche hängen, die sich langsam bewegen — weil das Material lebt.

**Gilden-Stadt: Industrielle Monumentalität.**
Breite Strassen, offene Marktplätze, kathedralenhafte Gildenhallen mit sichtbaren Deckenrippen. Die Gebäude atmen — wörtlich. Wände, die sich leicht ausdehnen und zusammenziehen. Böden mit Kapillarnetzwerken. Membranfenster, die sich bei Regen verdichten. Karawanenhöfe, in denen Tiervolk-Händler ihre Waren auslegen. Kontore mit Chitin-Schreibpulten und Membran-Dokumenten. Fabrikgebäude, in denen Biotech-Material gezüchtet wird — riesige Hallen, warm, feucht, pulsierend. Die Gilden-Stadt riecht nach Leben.

**Ordens-Stadt: Geometrische Perfektion.**
Von aussen die schönste Siedlung des Mittelgrunds. Weisse Mauern, perfekte Proportionen, Kreuzgänge mit sanftem Lichteinfall. Schulen, Hospitäler, Bibliotheken — alles offen, alles einladend. Halvards Raben als Steinrelief an den Gebäuden. Klostergärten mit medizonischen Kräütern. Die Strassen sind breit und sauber. Kein Verfall, kein Dreck, keine Unordnung. Und unter der Oberfläche: Nervenstrang-Korridore, Überwachungsorgane, Labore. Der Spieler, der tief genug in den Orden vordringt, erlebt den Moment, in dem der weisse Kalkstein aufhört und das pulsierende Gewebe beginnt.

**Wildnis: Mitteleuropa mit Emer-Unterton.**
Dichte Wälder, neblige Täler, schroffe Gebirge, Moorlandschaften. Auf den ersten Blick realistisch, auf den zweiten Blick subtil fremd: Felsen mit Muskelmaserung, Bäume, deren Rinde an Haut erinnert, Quellen, die in einem Rhythmus sprudeln. Ruinen vergangener Epochen, überwachsen und halb verdaut von der Landschaft — das Land nimmt zurück, was auf ihm gebaut wurde. Einzelhöfe, Einsiedler, verlassene Wachposten. Die Wildnis ist schöen und still und nicht sicher.

**Übergangszonen: Neutrale Räume.**
Märkte, Karawanenwege, Grenzgebiete. Hier treffen die Fraktionen aufeinander, und die visuelle Sprache ist bewusst neutral: Erdtoene, keine Fraktionsfarben, einfache Architektur ohne Biotech-Prägung. Tiervolk-Präsenz ist hier am stärksten — ihre eklektische Kleidung und ihre fremden Körper setzen sich gegen die neutrale Umgebung deutlich ab.

**Schattenfieber-Zonen: Die Entflechtung.**
Gebiete, in denen die Hauten dünn geworden sind. Die visuelle Transformation ist total: Farben entsättigen und kippen in Violett-Schwarz, Giftgrün leuchtet in den Adern der Landschaft, Flora und Fauna sind mutiert. Die Physik verhält sich falsch. Licht bricht anders. Wasser fliesst aufwärts. Schatten haben eigene Konturen. Diese Zonen sind die visuell intensivsten Orte in RELICS — und die gefährlichsten. Ihre Grenzen sind scharf: ein Schritt trennt die geordnete Welt vom Chaos. Die Hauten sind hier so dünn, dass das Stillfeld (oder das Hohlicht) durchscheint.

### 8.4 Beleuchtung

Beleuchtung in RELICS folgt zwei Logiken — natürlich und künstlich — und einer Ausnahme.

**Natürliches Licht:** Diffus, oft bedeckt, selten warm. Der Mittelgrund liegt in einer klimatischen Zone, die an Mitteleuropa erinnert: häufig bewölkt, häufig neblig, selten strahlend. Die goldene Stunde (kurz vor Sonnenuntergang) ist ein seltener, wertvoller Moment — wenn sie eintritt, wird sie zum visuellen Geschenk. Concept Artists sollen die meisten Szenen in diffusem, kuühlem Licht gestalten und die goldene Stunde sparsam einsetzen.

**Künstliches Licht:** Ausschliesslich Biolumineszenz. Keine Fackeln, keine Kerzen, keine Öllampen. Lichtorgane — gezüchtete biologische Leuchtkörper — sind die einzige künstliche Lichtquelle. Ihre Farbtemperatur ist fraktionsabhängig:
- Krone: Warm, goldgelb, pulsierend — wie Kerzenlicht, aber lebendiger (`#C5A030`)
- Gilden: Neutral bis kühl, funktional, gleichmässig — Arbeitslicht, das nie blendet (`#C49A20` bis `#2EC4B6`)
- Orden: Kühl, weiss, gleichmässig — Kliniklicht, das keine Schatten lässt (`#E8E4DE`)

**Die Ausnahme — Schattenfieber-Licht:** In Schattenfieber-Zonen verhält sich Licht physikalisch falsch. Schatten fallen in die falsche Richtung. Lichtquellen leuchten, ohne zu beleuchten. Farben kippen ins Violett-Schwarz. Giftgrüne Adern leuchten von innen — sie brauchen keine Lichtquelle, sie SIND eine. Das Schattenfieber-Licht ist die Abwesenheit jeder visuellen Ordnung.

### 8.5 Gameplay-Orte: Fraktionsvarianten (V2 neu)

Bestimmte Gameplay-Orte kommen in allen drei Fraktionen vor — Alchemie-Station, Trainer, Händler. Jede Fraktion interpretiert diese Orte anders. Die Fraktionsvariante ist visuell sofort lesbar.

**Alchemie-Station**

Alchemie ist in RELICS Biologie: Substanzen aus Emer-Material, destilliert, konzentriert, kombiniert. Jede Fraktion betreibt Alchemie, aber mit anderen Mitteln und anderen Zwecken.

| Fraktion | Visueller Charakter | Lage | Signalelemente |
|----------|---------------------|------|----------------|
| Krone | Privates Laboratorium hinter verhängten Türen. Elegantes Gerät aus Altgold und dunklem Glas. Die Gefässe sind organisch geformt, die Flüssigkeiten pulsieren schwach in Karmin. Keine Beschriftung — Krone-Alchemie ist Geheimwissen. | Hinterräume von Paläesten, unter Kapellen | Altgold-Gerät, Karmin-Flüssigkeiten, verschlossene Gefässe, kein Licht von aussen |
| Gilden | Öffentliche Werkstatt. Alles sichtbar, alles beschriftet, alles zugänglich (gegen Geld). Breite Arbeitsflächen aus Chitin, grosse Membran-Behälter, Amber-Biolumineszenz über den Stationen. Die Zutatenliste hängt an der Wand. | Erdgeschoss von Gildenhäusern, Marktebene | Amber-Licht, offene Regale, Membran-Behälter, Preisliste sichtbar |
| Orden | Scheinbar ein Krankenhaus-Vorbereitungsraum: weiss, steril, geordnet. Was wirklich passiert, ist nicht sofort erkennbar. Die Substanzen sind farblos. Die Geräte sehen wie medizinische Instrumente aus. Bernstein-Glow kommt aus Behältern, die verschlossen und etikettiert sind — mit Codes, nicht mit Namen. | Ordenshospitäler, Innenbereiche | Kalkweiss, verschlossene Codes-Etiketten, Bernstein-Glow hinter Glas, keine sichtbaren Pflanzen |

**Trainer**

Trainer lehren Kampffähigkeiten und körperliche Techniken (GDD-02, Kap. 3.3). Jede Fraktion hat exklusive Trainer für bestimmte Waffenstile und Fertigkeiten. Optisch ist sofort erkennbar, welche Fähigkeiten hier gelehrt werden.

| Fraktion | Visueller Charakter | Lage | Signalelemente |
|----------|---------------------|------|----------------|
| Krone | Zeremonieller Übungshof oder Fechtsaal. Hohe Decken, Holzdielen, einhändige Statuen als stille Zuschauer. Krone-Trainer lehren Schwertkampf, Paraden, zeremonielle Kampfkunst. Kleidung: formal, Karmin-Akzente, keine sichtbare Rüstung — Haltung ist Rüstung. | Innenhöfen von Paläesten und Adelsgebäuden, obere Stadtebene | Einhändige Statuen, Karmin-Wandverkleidung, Schwerttrophaän, kein Biotech sichtbar |
| Gilden | Kämpfarena oder Söldnerquartier. Pragmatisch, dreckig, effektiv. Strö auf dem Boden, Chitin-Dummies, Waffenregale mit allem, was Funktion hat. Gilden-Trainer lehren Dolchkampf, Bogenarbeit, Gürilla-Taktiken. Kleidung: Arbeitskleidung mit organischen Verstarkungen. | Karawanenhöfe, Söldnerunterkünfte, Untergeschoss von Gildenhallen | Chitin-Trainingsgeräte, offene Waffenregale, Amber-Licht, sichtbare Kampfspuren |
| Orden | Meditativer Übungsraum. Kalkweiss, minimale Einrichtung, symmetrisch. Orden-Trainer lehren Körperkontrolle, Schmerzunterdrückung, Konzentrationsarbeit — aber auch fortgeschrittene Kampftechniken, die nach aussen wie Heilkunde aussehen. | Innenbereiche von Ordensgebäuden, untere Ebenen | Kalkweiss, keine Dekoration, geometrische Übungsmarkierungen am Boden, Schieferblau-Roben des Trainers |

**Händler**

Händler verkaufen Waren, Informationen, Zugang. Tiervolk-Händler sind die mobilen Generalisten. Fraktionshändler spezialisieren sich auf ihre eigenen Produkte. Optisch klar unterscheidbar.

| Händler-Typ | Visueller Charakter | Lage | Signalelemente |
|--------------|---------------------|------|----------------|
| Krone-Händler | Privates Kontor mit schweren Vorhängen. Nicht alles ist ausgestellt — die wertvollsten Waren sind hinter dem Ladentisch. Karmin-Textilien, Altgold-Preisschilder, Biolumineszenz als Beleuchtung. Haltung des Händlers: erwartet Respekt. | Palastbezirke, Adelsmarkte | Verhang vor dem Eingang, Altgold-Schilder, versteckte Ware, körpersprachlich kühl |
| Gilden-Händler | Öffentlicher Stand oder grosses Kontor. Ware ist ausgestellt, Preise sind sichtbar, Verhandlung ist erwünscht. Amber-Beleuchtung, Chitin-Theke, Membran-Verpackungen. Haltung des Händlers: pragmatisch, laut, direkt. | Marktplätze, Karawanenhöfe, Erdgeschoss | Offene Auslagen, sichtbare Preisliste, Amber-Licht, laute Umgebung |
| Orden-Händler | Kein klassischer Handel — der Orden verkauft nicht, er verteilt. Zutritt nur bei Beziehungsstatus. Kalkweiss-Raum, geordnete Regale, alles etikettiert. Was der Orden gibt, kostet Information oder Loyalität, kein Geld. | Ordenshospitäler, Bibliotheken | Kalkweiss, keine Preisschilder, Händler in Ordensroben, erwartet Gegenleistung in Form von Information |
| Tiervolk-Händler | Mobiler Stand, eklektische Ware aus allen Fraktionen. Ocker-Terrakotta-Tücher als Auslageflächeche, Knochen-Schmuck als Dekoration, Biotech-Fragmente als Raritäten. Haltung des Händlers: freundlich, beobachtend, immer bereit abzuhaün. | Übergangszonen, Marktplätze, Stadtgrenzen | Ocker-Erdtoene, gemischte Ware, mobiles Setup (kein fester Stand), Tiervolk-Proportionen |

---

\clearpage

# GDD-06 — Technische Spezifikation & Produktion


---

## 1. Engine & Rendering

### 1.1 Engine-Wahl

RELICS wird in **Unreal Engine 5.4+** entwickelt (bestätigt Tag 1, Szene 3). Die Engine-Entscheidung basiert auf drei Faktoren: Nanite und Lumen liefern die Rendering-Qualität, die der Dark-Fantasy-Look erfordert, ohne dass wir eine eigene Render-Pipeline bauen müssen. Das Gameplay Ability System (GAS) ist die einzige Engine-native Lösung, die Darius' dreischichtiges Combat-System (GDD-02, Kap. 1.2) ohne Drittanbieter-Middleware abbilden kann. Und die Marketplace-Infrastruktur ist für ein kleines Team wie unseres ein realer Produktionsfaktor — nicht als Ersatz für eigene Assets, sondern als Basis zum Anpassen.

**Zielplattform:** PC first (Windows). Konsolen sind ein Stretch Goal, das frühestens nach dem Vertical Slice evaluiert wird. Die Entscheidung für PC first ist keine Einschränkung, sondern eine bewusste Scope-Steuerung: Konsolen-Portierung erfordert Anpassungen an Controller-UI, Performance-Optimierung für fixe Hardware und Zertifizierungsprozesse, die unser aktuelles Team nicht stemmen kann.

**Singleplayer.** Kein Multiplayer-Backend, kein Koop, keine Online-Features. Das vereinfacht die Architektur erheblich und eliminiert eine ganze Kategorie technischer Risiken.

### 1.2 Rendering-Architektur

#### Nanite (Virtualisierte Geometrie)

Nanite ist das primäre Geometrie-System für alle statischen Hard-Surface-Meshes: Architektur, Props, Waffen, Terrain-Deko, Felsen. Die Kernidee: Künstler müssen keine manuellen LOD-Ketten mehr bauen. Nanite übernimmt die geometrische Vereinfachung zur Laufzeit, was besonders bei modularen Architektur-Kits (Kap. 4.1) die Produktionsgeschwindigkeit drastisch erhöht.

Einschränkungen, die den Workflow betreffen:
- **Skeletal Meshes** (Charaktere, Kreaturen, NPCs) unterstützen kein Nanite. Hier verwenden wir klassische LOD-Ketten mit drei Stufen (High, Mid, Low). Vera modelliert High-Poly, die LODs werden semi-automatisch generiert (Simplygon oder Ü5-internes Proxy-System).
- **Vegetation** ist ein Hybrid: Baumstämme und grosse Gehölze als Nanite-Meshes, Blätter und Gras als traditionelle Alpha-Karten mit Dithering. Der Grund: Nanite kann keine Alpha-Masken verarbeiten, und Wind-Animation (World Position Offset) funktioniert nur mit traditionellen Meshes.
- **Vertex-Animation** ist über Nanite eingeschränkt möglich (s. Kap. 1.4 für Regelwerk). Starke WPO-Deformationen (Schattenfieber Stufe 3-4) müssen als traditionelle Meshes gebaut werden.

#### Lumen (Globale Beleuchtung)

Lumen ist das primäre GI-System. Wir verwenden keine gebackenen Lightmaps. Das ist eine fundamentale Entscheidung: In einer Welt, die auf Environmental Storytelling setzt (GDD-01, Säule P4), muss Licht dynamisch auf Spieleraktionen reagieren können — eine Fackel geht aus, ein Feuer wird entzündet, die Tageszeit wechselt. Gebackene Beleuchtung kann das nicht.

**Shipping-Konfiguration:** Hardware Ray Tracing (HW RT Lumen). Das liefert die beste Qualität bei Innenräumen (die für RELICS' gotische Architektur zentral sind) und hält die visuellen Artefakte minimal, die Software Lumen in engen Räumen mit vielen Lichtquellen produziert.

**Fallback:** Software Lumen für Hardware ohne RT-Unterstützung (Minimum-Tier, siehe Kap. 6). Die visuellen Unterschiede sind akzeptabel, solange wir Innenräume nicht auf mehr als 4-5 Bouncen angewiesen machen.

**Referenz-Look:** Control (Remedy) für Innenräume — präzise Lichtführung, dramatische Schatten, praktische Lichtquellen als Gestaltungselement. Alan Wake 2 für Aussenräume — natürliches Licht, atmosphärische Streuung, keine überbelichteten Himmel.

#### Virtual Shadow Maps (VSM)

Standard bei Lumen-Projekten. VSM liefert hochauflösende Schatten ohne die Artefakte klassischer Cascaded Shadow Maps. Das Budget: maximal 8-12 dynamische Lichtquellen gleichzeitig pro Szene. Das klingt nach wenig, ist aber ausreichend, wenn wir konsequent mit praktischen Lichtquellen arbeiten (Biolumineszenz-Organe, Feuer, Laternen) und globale Beleuchtung den Rest übernimmt.

Risiko: VSM hat in Ü 5.3/5.4 noch Performance-Spitzen bei vielen überlappenden Schatten. Epic verbessert das kontinuierlich, aber wir müssen in der Prototyping-Phase Worst-Case-Szenen testen (z.B. Marktplatz mit 12 Lichtorganen).

#### Farb-Pipeline

Die Farb-Pipeline ist eine der Entscheidungen, die unsichtbar ist, wenn sie funktioniert, und katastrophal, wenn sie es nicht tut. RELICS verwendet **ACES (Academy Color Encoding System)** als Arbeitsfarbraum über die gesamte Tool-Chain: Substance Designer/Painter, Houdini, Unreal Engine 5. Das stellt sicher, dass Farben konsistent bleiben, egal welches Tool sie erzeugt hat.

Warum ACES und nicht sRGB? Weil RELICS eine düster-farbige Palette braucht (Briefing: "Düster, aber farbig. Kein Entsättigungs-Klischee.") und sRGB im Low-Key-Bereich Farbinformationen verliert. ACES hat einen grösseren dynamischen Umfang und bewahrt Farbnuancen in den Schatten — genau dort, wo unser Spiel lebt.

**Tone Mapping:** ACES als Standard-Tone-Mapper in Ü5, mit der Option auf eine Custom LUT, wenn der generische ACES-Look zu "filmlastig" wirkt. Evaluation im Prototyp.

**Deakins-Prinzip (intern):** Roger Deakins arbeitet mit reduzierter Beleuchtung, aber nie mit entsättigten Farben. Ein dunkler Raum ist nicht grau — er ist tiefblau, warm-orange am Rand, mit Farbtemperatur-Kontrast. Dieses Prinzip gilt für jeden beleuchteten Raum in RELICS.

### 1.3 Post-Processing Stack

Der Post-Processing Stack ist bewusst zurückhaltend. Jeder Effekt muss einen narrativen oder gameplay-relevanten Grund haben. "Sieht cool aus" ist kein Grund.

| Effekt | Einstellung | Begründung |
|--------|-------------|-------------|
| Color Grading | Gedämpfte Palette, fraktionsspezifisch | Krone: warme Verrottung (`#C5A030`/`#8B1A2B`). Gilden: kühle Präzision (`#2EC4B6`/`#C49A20`). Orden: entsättigt-kühle Monochromie (`#E8E4DE`/`#4A5568`) |
| Vignette | Subtil (0.3-0.4) | Fokussiert den Blick, verstärkt Tunneleffekt in engen Räumen |
| Depth of Field | Cinematisch in Dialogen (f/2.8-Simulation), minimal im Gameplay | Dialog-Kamera braucht Bokeh für Portraitqualität. Im Gameplay würde DOF die Lesbarkeit stoeren |
| Bloom | Nur praktische Lichtquellen | Biolumineszenz-Organe, Feuer. Kein Lens-Flare. Kein Glow auf Materialien ohne Emissionsgrund |
| Motion Blur | Per-Object (Waffen-Swings, Feindangriffe) | Verstärkt das Gewicht von Kampfaktionen. Kein Camera Motion Blur — das erzeugt Übelkeit und stoert die Lesbarkeit |
| Film Grain | Optional (Spielereinstellung) | Manche Spieler mögen den filmischen Look, andere nicht. Keine Default-Aktivierung |
| Chromatische Aberration | Nur Schattenfieber (Kap. 5) | Kein genereller CA-Effekt. Ausschliesslich als Infektionsindikator |

### 1.4 Organische Shader-Architektur (NEU V2)

RELICS' Kern-Ästhetik ist organische Gotik (GDD-05, Kap. 1.1): Alles lebt, atmet, pulsiert. Das hat direkte Konsequenzen für die Shader-Architektur. Dieser Abschnitt definiert die technischen Regeln für organische Oberflächen — Hauten, Membranen, Biotech-Gewebe — und grenzt ab, wo Nanite endet und traditionelle Meshes beginnen.

#### Hauten-Shader (Subsurface Scattering)

Organische Oberflächen in RELICS benötigen **Subsurface Scattering (SSS)**, um das Gefühl von lebendigem Gewebe zu erzeugen: Licht dringt in die Oberfläche ein und tritt an benachbarten Stellen wieder aus (wie Licht durch eine Hand). Das ist der visuelle Unterschied zwischen "Stein, der wie Haut aussieht" und "Haut".

**Shading Model:** `Subsurface Profile` (nicht das Legacy-`Subsurface`-Modell). Subsurface Profile implementiert Burley-SSS, das seit Ü5.3 physikalisch korrekt ist und Wrap-Around-Beleuchtung liefert. Das ist für Biotech-Gewebe und Charakterhaut die einzige akzeptable Lösung.

**Performance-Budget:** Subsurface Profile ist Screen-Space und kostet ~0.3-0.5 ms pro Screen-Fill auf empfohlener Hardware. Das muss im Gesamtbudget eingerechnet werden. Massnahme: SSS nur dort einsetzen, wo es visuell notwendig ist. Nicht jede Steinwand braucht SSS — nur organische Elemente im Vordergrund.

**Asset-Kategorien mit SSS:**
- Spielercharakter (Haut, Hautpartien unter Rüstung)
- NPCs mit Gesichts-Nahaufnahmen (Dialog-Kamera)
- Biotech-Gewebe-Elemente (Membranen, Adern, Nervenknoten) — wenn Nahsicht-relevant
- Lebende Krone (GDD-05, Kap. 1.3): Transluzente Stellen mit SSS, opake Stellen ohne

**Asset-Kategorien OHNE SSS:**
- Hintergrund-Architektur (zu weit weg, nicht wahrnehmbar)
- Props und Gerätschaften (nicht organisch)
- Terrain (eigenes Material-System, kein SSS)

#### World Position Offset (WPO) — Regelwerk

WPO ermöglicht Vertex-Displacement im Shader: atmende Wände, pulsierende Adern, schwankende Biotech-Elemente. Es ist das technische Fundament des "lebenden" Looks.

**Nanite + WPO:** Seit Ü5.1 unterstützt Nanite WPO grundsätzlich, aber mit Einschränkungen. Nanite+WPO ist vertretbar für kleine Puls-Animationen (Displacement unter 5% der Mesh-Grösse). Für grössere Deformationen — insbesondere Schattenfieber Stufe 3-4 — nicht geeignet.

**Nanite-Ausnahmen-Katalog:**

| Asset-Typ | Nanite | WPO | Begründung |
|-----------|--------|-----|-------------|
| Architektur (statisch, kein Biotech) | Ja | Nein | Reines Nanite, höchste Performance |
| Architektur mit kleinen Biotech-Adern | Ja | Ja (klein) | Nanite+WPO, Displacement < 5% |
| Pulsierende Membran-Elemente | Nein | Ja | Traditionelles Mesh, stärkere Puls-Animation |
| Schattenfieber-Vegetation | Nein | Ja | Traditionelles Mesh, starke WPO-Deformation |
| Schattenfieber-Geometrie Stufe 3-4 | Nein | Ja | Traditionelles Mesh, atmende Wände, Barrel-Distortion |
| Baum-Stämme (Grossgehölze) | Ja | Nein | Nanite, Wind über PCG-Instancing |
| Baum-Blätter / Gras | Nein | Ja | Traditionell + Alpha-Karte, Wind-WPO |
| Charaktere / NPCs / Kreaturen | Nein | Nein | Skeletal Mesh, kein Nanite |
| Lebende Krone | Nein | Ja | Eigenes Material, SSS + WPO, langsame Bewegung |

**WPO-Performance-Budget:** 0.2 ms GPU bei maximaler WPO-Last (alle sichtbaren organischen Elemente aktiv). WPO-Intensität skaliert mit LOD-Distanz: unter 10m voll, 10-30m halbe Intensität, über 30m deaktiviert.

---

## 2. Kamerasystem

### 2.1 Architektur

Das Kamerasystem basiert auf Ü5s **Spring Arm Component**. Die Entscheidung für Spring Arm (statt eines vollständig custom Kamerasystems) ist pragmatisch: Spring Arm löst Wandkollision, Lagging und Distanz-Management out of the box. Custom-Erweiterungen können darüber gebaut werden, ohne die Basis neu zu erfinden.

**Third Person ist der Primärmodus** (bestätigt Tag 1). Der Spielercharakter ist sichtbar, customizable Rüstung und Kleidung sind ein visuelles Belohnungssystem (Briefing). Ein reiner First-Person-Modus würde den Animationsaufwand verdoppeln (Arm-Rigs, FP-Waffen-Meshes, separate Animationssets) und ist daher als V2/DLC-Stretch-Goal klassifiziert.

**Architektonische Vorbereitung für FP:** Die Spring-Arm-Architektur erlaubt einen Arm-Length-Wert von 0, was mathematisch einem FP-Modus entspricht. Wir bauen keine FP-Features, aber wir verbauen auch nichts, was FP später unmöglich machen würde. Kein Gameplay-Code darf die Existenz eines sichtbaren Spielercharakters voraussetzen.

**Zoom:** Stufenlos via Mausrad (PC) oder rechtem Stick (Controller). Der Zoom interpoliert zwischen den Kontext-Modi-Parametern, nicht nur die Arm-Distanz.

### 2.2 Kontext-Modi

Das Kamerasystem wechselt kontextabhängig zwischen vier Modi. Der Wechsel ist kein harter Cut, sondern ein parametrischer Blend über die angegebene Dauer.

| Modus | Arm Length | FOV | Offset | Blend-Dauer | Auslöser |
|-------|-----------|-----|--------|-------------|-----------|
| Exploration | 350 cm | 78 deg | Leicht rechts (+30 cm) | Standard | Default-Modus, aktiv bei freier Bewegung |
| Combat | 200 cm | 82 deg | Über Schulter (+50 cm, +20 cm hoch) | 0.3 s | Feind im Engagement-Radius oder Waffe gezogen |
| Dialog | 100 cm | 72 deg | Schulterblick, Blick auf NPC-Gesicht | 0.5 s | Dialog-Trigger |
| Inspect | 400 cm | 70 deg | Zentriert (Offset 0) | 0.3 s | Inventar, Karte, Nervensystem-UI |

**Exploration** ist der Ruhezustand. Die leichte Rechts-Verschiebung gibt dem Spieler Sichtfeld links vom Charakter — das ist intuitiver für rechtsdominante Spieler und lässt Raum für UI-Elemente am linken Rand.

**Combat** zieht die Kamera näher heran und erhöht das FOV leicht. Das erzeugt ein Gefühl von Geschwindigkeit und Enge, ohne die Übersicht zu verlieren. Die Schulter-Perspektive erlaubt präziseres Zielen (relevant für Bogen/Armbrust).

**Dialog** simuliert einen cinematischen Schulterblick. Die niedrige Arm Length erzeugt Portraitqualität. Hier greift der DOF-Effekt (f/2.8-Simulation, siehe Kap. 1.3).

**Inspect** zieht die Kamera zurück und zentriert, damit der Spieler seinen Charakter und dessen Ausrüstung in voller Grösse sieht — wichtig für das Nervensystem-Leveling-UI (GDD-02, Kap. 3).

### 2.3 Kollision und Verhalten

- **Sphere Trace** für Wandkollision: Die Kamera fährt näher an den Charakter heran, statt durch Geometrie zu clippen. Radius: 12 cm (gross genug, um Ecken zu glätten, klein genug, um nicht auf Möbel zu reagieren).
- **Enge Räume:** Automatischer Nah-Zoom mit Minimum-Distance von 80 cm. Unter 80 cm würde der Charakter die gesamte Sicht blockieren.
- **Vegetation:** Dithering-Fadeout bei Kamera-Nähe (Radius 60 cm um Kameraposition). Keine harte Kollision mit Blättern und Gras — das würde in einem bewaldeten Gebiet ständig die Kamera ruckeln lassen.
- **Camera Lag:** Speed 8-10. Das erzeugt eine geschmeidige Nachführung, die sich organisch anfühlt, ohne den Charakter "hinter sich herzuziehen".
- **Pitch Range:** -60 bis +70 Grad. Der erweiterte Aufwärts-Bereich (+70) ist essentiell für Dishonored-Vertikalität (GDD-01, Säule P6): Der Spieler muss nach oben schauen können, um Kletterwege und Dachlandschaften zu erkennen.

## 3. Combat-Architektur

### 3.1 Grundsystem

Das Combat-System basiert auf dem **Gameplay Ability System (GAS)**, das in Ü5 nativ integriert ist. GAS ist die einzige Engine-Lösung, die die Komplexität von Darius' dreischichtigem Combat-Design (GDD-02, Kap. 1.2) abbilden kann, ohne auf Drittanbieter-Middleware angewiesen zu sein. Das reduziert das Abhängigkeitsrisiko, erfordert aber einen Entwickler mit GAS-Erfahrung (s. Anforderungsprofil Kap. 8.2).

**Fundamentale Abhängigkeit:** Das Combat-System setzt einen **dedizierten Gameplay-Programmer** voraus. Kein Teammitglied hat die C++-Tiefe, um GAS auf Produktionsniveau zu implementieren. Das Freelancer-Budget (Kap. 8.2) ist primär für diese Position reserviert. Ohne diese Person gibt es kein Combat, kein Vertical Slice, kein Spiel.

### 3.2 GAS-Architektur (V1 Scope)

| Komponente | GAS-Element | Implementierung | Priorität |
|------------|-------------|-----------------|------------|
| Basis-Attribute | Attribute Set | HP, Stamina, Infektionswert als GAS Attributes. Float-basiert, repliziert (Singleplayer: lokal) | Kern |
| Leichter/Schwerer Angriff | Gameplay Abilities | Ability-Klassen mit Montage-Referenz, Damage-Calculation, Stamina-Kosten | Kern |
| Block / Ausweichen | Gameplay Abilities | State-Machine: Idle > Block > Active. Parry = Frame-Window innerhalb von Block | Kern |
| Hit Detection | Animation Notifies | Notify-basiert: Sweep/Overlap bei definierten Frames. Keine Hitbox-Volumes, sondern Trace-basiert (präziser, weniger Collider-Overhead) | Kern |
| Stamina-Management | GAS Gameplay Effects | Kosten pro Aktion als Gameplay Effect. Regeneration als Duration-Effect mit Period | Kern |
| Hit Reactions / Stagger | Gameplay Cues + Montages | Gameplay Cues triggern VFX/Sound, Montages übernehmen die Animations-Reaktion | Kern |
| Schattenfieber-Fähigkeiten | Custom Abilities + MPC | Abilities mit doppeltem Kosten-System (Stamina + Infektionswert-Erhöhung). Post-Processing-Feedback über Material Parameter Collection | V1 nach Emre/Darius-Sync |
| Feind-KI | StateTree (Ü5-nativ) | Verhaltenslogik in StateTree, Combat-Aktionen als GAS Abilities. Feinde nutzen dasselbe System wie der Spieler | Kern |
| Gameplay Tags | Tag-Hierarchie | `Combat.State.Blocking`, `Combat.State.Staggered`, `Infection.Level.Rauschen` etc. Tags steuern, welche Abilities wann aktivierbar sind | Kern |

**Waffentypen V1-Scope:** Schwert (Einhand) + Bogen. Das ist das Minimum, um die Kern-Combat-Loop zu validieren. Armbrust, Schild, Zweihand-Waffen und Dolche sind V2 (GDD-02, Kap. 1.3 definiert sechs Waffenklassen — wir liefern zwei für den Vertical Slice).

### 3.3 Animation

**Motion Matching** (Ü 5.4+) ist das Bewegungssystem. Der Vorteil gegenüber klassischen Blend Trees: natürlichere Übergänge zwischen Gehen, Laufen, Stoppen, Richtungswechsel. Das reduziert das "Eislaufen"-Problem, das viele Third-Person-Spiele haben, und unterstützt das gewichtige Kampfgefühl (GDD-01, Säule P2).

**Animations-Datenbank:** Motion Matching braucht grosse Datensätze. Die Strategie ist dreistufig:
1. **Prototyping:** Mixamo als Basis. Kostenlos, sofort verfügbar, ausreichend für Gameplay-Iteration
2. **Produktion:** Marketplace-Animation-Packs als Startpunkt. Packs mit gewichtigem Melee-Combat (z.B. "Medieval Combat Animset") als Grundlage, angepasst
3. **Hero-Animations:** Custom oder MoCap für Kern-Movesets. Budget-Abhängig (Kap. 8.2)

**Control Rig:** IK für Fussplatzierung (Terrain-Anpassung), Waffenausrichtung (Aim Offset), und Rückenpanzerung (Socket-basiert). Control Rig ist Ü5-nativ und ersetzt die früheren AnimDynamics-Workarounds.

**Gewichtiges Kampfgefühl — technische Hebel:**
- **Hitlag:** 2-4 Frames Pause bei Treffer (sowohl Spieler als auch Feind). Erzeugt das Gefühl von Masse und Impact
- **Camera Shake:** Subtil, richtungsabhängig. Kein Bildschirm-Schütteln, sondern ein kurzer Impuls in Angriffsrichtung
- **Zeitlupe:** Optional für kritische Treffer (0.2 s bei 0.7x Speed). Muss sich verdient anfühlen, nicht inflationär
- **Impact VFX:** Funken, Staub, Blutspuren. Niagara-Partikel, physikbasiert

### 3.4 Risiken und Mitigationen

| Risiko | Schwere | Mitigation | Fallback |
|--------|---------|------------|----------|
| Gameplay-Programmer verzögert sich | KRITISCH | Suche beginnt sofort (Woche 1). Finn führt Gespräche | Marketplace-Combat-Framework als Bridge (Risiko: GAS-Inkompatibilität) |
| GAS-Lernkurve zu steil | HOCH | Lyra-Projekt (Epic) als Referenz-Implementierung. Iterativer Aufbau, keine Gross-Architektur am Anfang | GAS-Kurs/Beratung einkaufen (500-1000 EUR Budget) |
| Kampf fühlt sich nicht "gewichtig" an | HOCH | Frühe Prototyp-Iteration. Game-Feel-Workshop in Woche 6-7: Hitlag, Kamera, Sound als isolierte Variablen testen | Referenz-Videos von Gothic/Dark Souls als Benchmark-Reihe |
| Motion Matching Daten unzureichend | MITTEL | Früh mit Mixamo-Daten testen. Marketplace-Packs evaluieren (Woche 4) | Fallback auf klassische Blend Trees (funktioniert, sieht schlechter aus) |

---

## 4. Asset-Pipeline

### 4.1 Modulares Kit-System

Die Asset-Strategie für RELICS ist modular. Das bedeutet: Wir bauen keine fertigen Gebäude, sondern einen Baukasten aus ~60 Architektur-Modulen (Wand-Segmente, Ecken, Türrahmen, Fenster, Dach-Elemente, Fundamente, Biotech-Elemente, Membran-Einschlüsse, organische Strukturen), aus denen sich hunderte Gebäude-Varianten zusammensetzen lassen.

Dieses Prinzip ist nicht optional, sondern überlebensnotwendig: Vera ist die einzige dedizierte Künstlerin im Team. Ohne modulares System müssen wir jedes Gebäude einzeln modellieren. Mit modularem System modelliert Vera die Module, und Level Design baut daraus eine Stadt.

**Fraktions-Differenzierung** erfolgt über Material-Instanzen, nicht über separate Meshes. Dieselbe Wand bekommt je nach Fraktion ein anderes Material. Hex-Codes 1:1 aus GDD-05 (Vera Kowalski, V1):

| Fraktion | Basis (70%) | Akzent (20%) | Highlight (10%) |
|----------|-------------|--------------|-----------------|
| Krone | `#3D3D3D` Aschgrau | `#8B1A2B` Karmin | `#C5A030` Altgold |
| Gilden | `#7A6E5D` Warmer Beton | `#C49A20` Amber | `#2EC4B6` Cyan |
| Orden | `#E8E4DE` Kalkweiss | `#4A5568` Schieferblau | `#D4A017` Bernstein |

**Globale Akzente (fraktionsunabhängig):**

| Kontext | Farbe A | Farbe B | Farbe C |
|---------|---------|---------|---------|
| Schattenfieber | `#2D0A31` Violett-Schwarz | `#39FF14` Giftgrün | — |
| Wildnis/Neutral | `#5C6B3C` Moosgrün | `#8B7355` Erdton | `#9E9E9E` Nebel-Grau |
| Tiervolk | `#CC7722` Ocker | `#C04000` Terrakotta | `#C2B280` Sand |

Diese Hex-Codes sind verbindlich für alle Material-Instanzen. Jede Abweichung braucht explizite Abstimmung mit Vera (GDD-05) und dem CD.

**Fraktions-Material-Instanzen — Beschreibung:**
- **Krone:** Eleganter Zerfall. Aschgrau-Stein mit Karmin-Biotech-Glow in Rissen, Altgold-Ornamente. Farbreferenz: `#3D3D3D` Basis, `#8B1A2B` Glow, `#C5A030` Metallakzent
- **Gilden:** Industrielle Eleganz. Warmer Beton-Grundton, Amber-Licht auf funktionalen Elementen, Cyan in aktiven Adern. Farbreferenz: `#7A6E5D` Basis, `#C49A20` Licht, `#2EC4B6` Biotech-Fluid
- **Orden:** Monolithisch, doppelte Lesart. Kalkweiss-Fassade mit Schieferblau-Schatten; innen Bernstein für verborgenes Biotech. Farbreferenz: `#E8E4DE` Fassade, `#4A5568` Schatten, `#D4A017` Geheimebene

### 4.2 Standards

| Standard | Wert | Begründung |
|----------|------|-------------|
| Texel Density (Hero) | 10.24 px/cm | Für Assets in Nahsicht (Waffen, Rüstungen, Interaktionsobjekte). Entspricht ~1024px auf 1m |
| Texel Density (Background) | 5.12 px/cm | Für Hintergrund-Assets (Architektur-Module, Terrain-Deko). Spart VRAM ohne sichtbaren Qualitätsverlust |
| Naming (Static Mesh) | `SM_[Kat]_[Name]_[Var]` | z.B. `SM_Wall_Stone_01`, `SM_Door_Wood_Gilden_02` |
| Naming (Material Instance) | `MI_[Fraktion]_[Material]` | z.B. `MI_Krone_Stein_Verwittert`, `MI_Gilden_Bronze_Poliert` |
| Naming (Skeletal Mesh) | `SK_[Typ]_[Name]` | z.B. `SK_Char_PlayerMale`, `SK_Creature_Infizierter_01` |
| LOD (Skeletal) | 3 Stufen | LOD0: Voll, LOD1: 50%, LOD2: 25%. Automatisch via Simplygon oder Ü5-Proxy |
| LOD (Static/Nanite) | Automatisch | Nanite übernimmt. Kein manueller LOD-Workflow nötig |
| Textur-Format | BC7 (Farbe), BC5 (Normal) | Standard-Kompression für Ü5. BC7 hat bessere Qualität als DXT5 bei gleicher Grösse |
| Max. Texturgrösse | 4096x4096 (Hero), 2048x2048 (Standard) | 4K nur für Hero-Assets. Alles andere 2K |

### 4.3 Prozedurale Systeme

#### Houdini-Terrain

Houdini ist das Kern-Tool für Terrain-Generierung. Der Workflow: Heightfield-Generation in Houdini, Erosion (hydraulisch + thermisch), Pfade und Strassen als Masken, Export über das Houdini Engine Plugin direkt in Ü5.

**Scope:** 4-6 km2, organisiert über Ü5 World Partition mit 256m x 256m Zellen. World Partition erlaubt, dass nur die sichtbaren Terrain-Zellen geladen werden — essentiell für die Semi-Open-World ohne Ladebildschirme (GDD-01, Säule P4).

**HDAs für Vera:** Ich baue Houdini Digital Assets mit vereinfachter Oberfläche. Vera soll nicht Houdini lernen müssen — sie soll Parameter schieben können: Biom-Typ (Wald, Sumpf, Fels), Vegetationsdichte, Höhenvariation, Pfad-Breite. Das HDA generiert, sie iteriert, wir exportieren. Das ist der Produktivitätshebel.

Ehrliche Einschätzung: Die HDAs müssen WIRKLICH einfach sein. Vera ist eine schnelle Lernerin, aber Houdini hat die steilste Lernkurve in unserer gesamten Tool-Chain. Wenn die HDAs zu komplex werden, wird Vera sie nicht nutzen, und ich werde zum Flaschenhals. Erste HDA-Version muss in Woche 3 getestet werden.

#### PCG-Vegetation

Ü5s Procedural Content Generation (PCG) Framework für regelbasierte Vegetations-Platzierung. Die Regeln: Neigung (Gras nicht an Steilhängen), Höhe (Baumgrenze), Bodentyp (Sumpfpflanzen nur in Feuchtgebieten), Distanz zu Pfaden (keine Bäume AUF dem Weg), Distanz zu Gebäuden (Lichtung um Siedlungen).

Vera liefert 8-12 Vegetations-Assets pro Biom. PCG verteilt sie nach Regeln. Das spart hunderte Stunden manueller Platzierung.

#### Substance Designer

Prozedurale Materialien für sich wiederholende Oberflächen: Stein, Holz, Metall, Erde. Substance-Graphen exportieren direkt in Ü5-kompatible Texturen (Base Color, Normal, ORM). Die ACES-Konfiguration in Substance muss identisch zur Ü5-Konfiguration sein — sonst driften die Farben.

### 4.4 Asset-Quellen

| Quelle | Einsatzbereich | Budget-Implikation | Risiko |
|--------|----------------|--------------------|--------|
| Vera (Eigenproduktion) | Characters, Hero-Props, Concept Art, UI-Elemente | Intern (Gehalt) | Flaschenhals — eine Person für alles Visuelle |
| Tobi (prozedural) | Terrain, Felsen, Materialien, Vegetation-Verteilung | Intern (Gehalt) + Houdini-Lizenz | Houdini-Know-how ist nicht übertragbar |
| Megascans (Ü5 inklusive) | Umgebungs-Assets: Felsen, Boden, Vegetation-Basis | Kostenlos (Quixel Bridge) | Qualität gut, aber generisch — braucht Anpassung für RELICS-Look |
| Marketplace (selektiv) | Basis-Assets zum Anpassen, Animation Packs, VFX | Budget: 2.000-3.000 EUR (Kap. 8.2) | Qualitätsschwankung. Jedes Asset muss vor Kauf geprüft werden |
| Photogrammetrie (optional) | Texturen, Fels/Mauerwerk-Referenz | Gering (eigene Ausrüstung) | Detmold/Lemgo-Umgebung als Quelle. Mittelalterliche Architektur vor der Haustür |

---

## 5. Schattenfieber-Tech

### 5.1 Systemübersicht & Drei-Schichten-Rendering (ERWEITERT V2)

Das Schattenfieber ist das technisch anspruchsvollste System in RELICS. Es ist kein einzelner Effekt, sondern ein Querschnittssystem, das Rendering, VFX, Gameplay, Audio und Narrative verbindet.

**Kernprinzip:** Der Infektionswert (0-100, Float) ist der einzige Eingabeparameter für spielerseitige Effekte. Alle visuellen Effekte leiten sich von diesem einen Wert ab. Das System interpoliert kontinuierlich — keine harten Stufenschalter (GDD-02, Kap. 2.3).

#### Drei-Schichten-Rendering (NEU V2)

Die Welt in RELICS besteht aus drei Daseinsebenen (WBB-01, Emre Yilmaz): **Mittelgrund** (die bewohnte Welt), **Hohlicht** (die untere Ebene, dunkler, komprimierter), **Stillfeld** (die obere Ebene, leerer, gefährlicher). Normal ist nur der Mittelgrund sichtbar. Ab Schattenfieber-Schwelle (Infektionswert 76+) oder in bestimmten Lore-Orten beginnen die anderen Ebenen durchzuschimmern.

Technisch: Jede Ebene ist ein eigenes Post-Processing-Volume-Profil. Priority-Blending steuert, welche Profile aktiv sind. Maximum 5 aktive PP-Segmente gleichzeitig.

| Schicht | PP-Profil | Visuelle Identität | Aktivierung |
|---------|-----------|---------------------|-------------|
| Mittelgrund | `PPV_Midground_Base` | Standard-Rendering. Fraktionsspezifisches Color Grading. Kein Zusatz-Overhead | Immer aktiv |
| Mittelgrund (Schattenfieber) | `PPV_SF_Player` | Spielerseitig MPC-gesteuert. Alle SF-Effekte Stufe 1-4 | Infektionswert > 0 |
| Hohlicht | `PPV_Hohlicht` | Tiefer, komprimierter. Farbpalette: Richtung `#2D0A31`, Schatten verlängert, Kontrast erhöt. Geometrie wirkt schwerer | Infektionswert >= 76 ODER Zone-Trigger |
| Stillfeld | `PPV_Stillfeld` | Heller, leer, geometrisch verzerrt. Entsättigung extrem, Kanten scharf. Schwindel-WPO auf Peripherie | Infektionswert >= 90 ODER Zone-Trigger |
| Befallene Zone | `PPV_Zone_Befallen` | Level-Volume. Unabhängig von Spieler-Infektionswert. Schattenfieber-Farbprofil für alle sichtbar | Level-Placement |

**Maximale Gleichzeitigkeit:** 3 Profile im Normalfall (Base + SF_Player + ggf. Zone). 5 Profile als absolutes Maximum (Base + SF_Player + Hohlicht + Stillfeld + Zone — nur in spezifischen Endgame-Sequenzen).

**Zwei Schattenfieber-Farbprofile:**
- **Profil A (spielerseitig):** MPC-gesteuert. Skaliert mit Infektionswert. Intensität graduell. Nur der Spieler sieht dieses Profil in seiner vollen Intensität.
- **Profil B (zonenbasiert):** Level-Volume, feste Werte. Alle Spieler sehen befallene Zonen gleich. Unabhängig von persönlichem Infektionswert — das sind öffentliche Warnzeichen.

*Zu validieren mit Emre: Anzahl der aktiven Segmente pro Szene. Standard: 3. Maximum: 5. Bestätigungsbedarf.*

### 5.2 Technische Architektur (unverändert)

Das System besteht aus drei Schichten:

**Schicht 1: Material Parameter Collection (MPC)**
Eine zentrale MPC (`MPC_Schattenfieber`) hält den Infektionswert als skalaren Parameter. Alle Post-Processing-Materialien, Niagara-Systeme und Welt-Shader lesen diesen Wert. Änderungen am Infektionswert propagieren automatisch in alle Systeme — kein manuelles Update nötig.

**Schicht 2: Post-Processing Volume**
Ein eigener Post-Processing Volume, der dem Spielercharakter folgt (nicht level-global). Die Material-Instanzen in diesem Volume lesen die MPC und skalieren ihre Effekte entsprechend.

**Schicht 3: Niagara VFX**
GPU-Partikel-Systeme, die ebenfalls die MPC lesen. Schattensporen, Flimmern, Verzerrungspartikel — alles skaliert mit dem Infektionswert.

### 5.3 Fünf-Stufen-Rendering (KORRIGIERT V2 — CD-Lock Stufengrenzen)

CD-verbindliche Stufengrenzen: Rauschen 1-40, Risse 41-75, Schwelle 76-100.

| Stufe | Lore-Phase | Infektionswert | Post-Processing Effekte | Niagara VFX | Welt-Effekte | Technische Komplexität |
|-------|-----------|---------------|------------------------|-------------|--------------|------------------------|
| 0 (Rein) | — | 0 | Keine | Keine | Keine | Baseline |
| 1 (Rauschen Früh) | Rauschen | 1-20 | Leichte Farbverschiebung in den Schatten (kühler, bläulicher). Subtiles Vignette-Pulsieren (0.05 Hz) | Vereinzelte Schattensporen (2-5 Partikel, kaum sichtbar) | Schattensinne: Versteckte Objekte erhalten Custom Stencil Outline | Niedrig |
| 2 (Rauschen Spät) | Rauschen | 21-40 | + Chromatische Aberration (einsetzend, 0.05-0.15). Farbsättigung beginnt zu verschieben (Grün > Cyan am Rand) | + Partikel-Overlay dichter (10-15 Partikel). Emotionsauren an NPCs als farbige Niagara-Systeme | + Gesprächsoptionen-Shader: UI-Text für SF-Dialoge mit leichtem Glitch | Mittel |
| 3 (Risse) | Risse | 41-75 | + Geometrische Verzerrung am Bildrand (Barrel Distortion, animiert). Farbpalette kippt merklich. Depth-of-Field-Schimmer auf mittlerer Distanz. CA stärker (0.2-0.5) | + Schattenranken-Partikel am Bildrand. Tiefensicht als Niagara-Overlay (geologische Schichten, Adern im Terrain) | + Custom Stencil Buffer für Objekte, die nur ab Rissen sichtbar sind. Fragwürdige NPCs mit Flimmer-Shader | Hoch |
| 4 (Schwelle) | Schwelle | 76-100 | + Halluzinatorische Elemente (s. Kap. 5.4). Vertex-Displacement auf Welt-Geometrie. Doppelbilder (Ghost-Rendering). Farbkanal-Separation. Hohlicht/Stillfeld beginnen durchzuschimmern (Kap. 5.1) | + Vollständiges Sporen-Feld. Schatten bewegen sich autonom. Lichtquellen flackern asynchron | + Parallel-Geometrie: Ganze Raum-Segmente in alternativer Version. NPCs ohne visuellen Unterschied zu "echten" NPCs | Sehr hoch |

### 5.4 Graduelle Interpolation — Technik (KORRIGIERT V2)

Der Trick ist, dass alle Effekte nicht bei Stufengrenzen "anspringen", sondern über Kurven interpoliert werden:

- **Farbverschiebung:** `Lerp(NormalMatrix, VerschobenMatrix, InfektionswertFloat / 100)`. Beginnt bei Wert 1, voll bei 100.
- **Chromatische Aberration:** Intensität = `max(0, (Infektionswert - 20) / 80)`. Beginnt bei ~20, erreicht Maximum bei 100.
- **Geometrische Verzerrung (Barrel):** Intensität = `max(0, (Infektionswert - 41) / 59)`. Beginnt bei 41 (Risse-Grenze), graduell bis 100.
- **Halluzinationen:** `max(0, (Infektionswert - 76) / 24)`. **Beginnt bei 76 (Schwelle-Grenze).** Maximum bei 100. *(V1-Fehler: Start bei 70 — korrigiert auf 76 per CD-Lock.)*
- **Hohlicht-Einblendung:** `max(0, (Infektionswert - 76) / 24)`. Gleiche Kurve wie Halluzinationen. Schwelle-Phase = Hohlicht beginnt sichtbar zu werden.
- **Stillfeld-Einblendung:** `max(0, (Infektionswert - 90) / 10)`. Erst bei 90, extrem kurzer Bereich. Sehr intensive Wirkung.

Alle Kurven sind in Ü5 als **Float Curve Assets** hinterlegt und können im Editor angepasst werden, ohne Code zu ändern. Emre und Nami können diese Kurven mitgestalten — sie definieren, WANN sich etwas "richtig" anfühlt.

### 5.5 Welt-Effekte (Befallene Zonen)

Befallene Zonen in der Spielwelt haben eigene Post-Processing Volumes (Profil B, s. Kap. 5.1) mit vorab gesetzten Schattenfieber-Effekten — unabhängig vom Infektionswert des Spielers. Diese Zonen sind für ALLE Spieler sichtbar.

- **Biotech-Vegetation:** Organische Auswüchse, pulsierende Ranken. Vertex-Animation (kein Nanite), emissive Materialien mit Pulse-Funktion. Farben: `#2D0A31` + `#39FF14`
- **Boden-Shader:** Terrain-Material mit zusätzlichem Schattenfieber-Layer (organische Textur, leicht animiert)
- **Niagara-Atmosphäre:** Schattensporen als GPU-Partikel, Nebel mit volumetrischem Scattering. Emres Nebel-Beschreibung ("Nebel, der sich anfühlt wie Trauer") = technische Parameter: langsame Partikel, tiefe Sättigung in `#2D0A31`, Gewicht nach unten (negative Y-Geschwindigkeit), kaum horizontale Drift.

### 5.6 Performance-Implikation

Das Schattenfieber-System hat ein eigenes Performance-Budget von **2 ms GPU-Zeit** (bei empfohlener Hardware). Aufgeteilt:
- Post-Processing (alle aktiven Profile): 0.8 ms
- Niagara-Partikel: 0.7 ms (GPU-Partikel, LOD-aware)
- Custom Stencil / Welt-Effekte: 0.5 ms (nur in befallenen Zonen aktiv)
- Drei-Schichten-Overhead (Hohlicht/Stillfeld aktiv): +0.3 ms Reserve einplanen

Bei Stufe 0 ist das Budget nahe 0 ms. Das System kostet nur, wenn es aktiv ist.

### 5.7 Abhängigkeiten und offene Punkte

| Abhängigkeit | Von wem | Status | Dringlichkeit |
|--------------|---------|--------|---------------|
| Hauten-Segmentanzahl (3 oder 5 Standard?) | Emre (Lore-Logik) | Offen | MITTEL — Annahme 3 Standard, brauche Bestätigung |
| Visueller Referenz Stufe 3-4 | Emre (Lore), Vera (Concept) | Offen | HOCH — ohne Referenz baue ich ins Blaue |
| Infektionswert-Gameplay-Logik | Darius (GDD-02) | V0.5 vorhanden | Mittel |
| Narrative Zustände → visuelle Parameter | Nami | Rauschen/Risse/Schwelle definiert | Mittel |
| Audio-Verzerrung (Risse+) | Offen (kein Audio-Lead) | Nicht begonnen | Niedrig für V1, hoch für VS |
| Abstimmungsmeeting Schattenfieber-Tech | Tobi + Emre + Darius + Vera | Noch nicht terminiert | HOCH — nächste Woche |

---

## 6. Performance-Ziele

### 6.1 Hardware-Tiers

RELICS definiert drei Hardware-Tiers. Die Ziel-Framerates sind ambitioniert, aber durch Upscaling-Technologie erreichbar.

| Tier | GPU-Referenz | CPU-Referenz | RAM | Ziel-FPS | Auflösung | Rendering |
|------|-------------|-------------|-----|----------|-----------|-----------|
| Minimum | GTX 1070 / RX 5700 | i5-8400 / R5 3600 | 16 GB | 30 fps | 1080p | Software Lumen, Low Settings, FSR Quality |
| Empfohlen | RTX 3070 / RX 6800 | i7-10700 / R7 5800X | 16 GB | 60 fps | 1440p | HW RT Lumen, High Settings, DLSS/FSR Quality |
| High-End | RTX 4080+ / RX 7900 XT | i7-12700+ / R7 7800X3D | 32 GB | 60 fps | 4K | Max Settings, RT Reflections, DLSS/FSR Performance |

**Redaktionelle Notiz:** Minimum-Tier (GTX 1070) ist provisorisch. GTX 1070 mit Software Lumen, Nanite und Schattenfieber-Effekten bei 30 fps ist ambitioniert. Der tatsächliche Minimum-Tier wird nach Benchmark-Phase (Woche 6-8) final gesetzt — möglicherweise auf GTX 1660 / RX 5500 XT verschoben. Das ist eine datenbasierte Entscheidung.

### 6.2 Upscaling (Pflicht)

Upscaling ist nicht optional, sondern ein Kern-Feature:
- **DLSS 3** (Nvidia): Super Resolution + Frame Generation
- **FSR 3** (AMD): Super Resolution + Fluid Motion Frames
- **XeSS** (Intel): Optional, niedriger Prio

DLSS und FSR sind der Grund, warum 60 fps bei 4K realistisch ist. Ohne Upscaling wäre 4K/60 auf keiner Consumer-Hardware erreichbar.

Frame Generation als Option für unterstützte Hardware. Nicht als Standard aktiviert — Eingabe-Latenz ist bei Action-Combat relevant.

### 6.3 Performance-Budgets

| Kategorie | Budget | Begründung |
|-----------|--------|-------------|
| Draw Calls | < 5.000 pro Frame | Nanite reduziert Draw Calls drastisch. 5.000 ist konservativ und lässt Raum für UI und Partikel |
| Dynamische Lichter | 8-12 gleichzeitig | VSM-Limit. Darüber hinaus Performance-Einbruch |
| Vegetation Draw Distance | Gras: 50-80 m, Bäume: 500 m | Gras ist der teuerste Vegetationstyp. Bäume als Impostors ab 300 m |
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

**Perforce (Helix Core)** für das Ü5-Projekt. Das umfasst alle Binär-Assets (Meshes, Texturen, Maps, Blueprints, Sound). Perforce ist der Industriestandard für Unreal-Projekte, weil es Binär-Dateien nativ sperren kann (File Locking). Kein Git LFS für Engine-Assets.

**Git** für Dokumentation (GDD, WBB, dieses Dokument), Scripts, Pipeline-Tools.

### 7.2 Ordnerstruktur (Ü5-Projekt)

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
      Schattenfieber/    -- MPC, PP-Volumes, alle fünf Profile
    Maps/
      Persistent/
      Sublevels/
      Test/
    Data/
      DataTables/
      Curves/            -- Float Curves: SF-Parameter, Kamera-Blends, WPO-Intensität
      GameplayTags/
```

### 7.3 Tool-Chain

| Tool | Version | Einsatz | Verantwortlich | Lizenzkosten (jährlich) |
|------|---------|---------|----------------|-------------------------|
| Unreal Engine 5.4+ | Latest stable | Runtime, Level Design, Blueprints, Sequencer | Tobi, Darius, Gameplay-Programmer | Kostenlos (5% Royalty ab 1M USD) |
| Houdini Indie | 20.5+ | Terrain, prozedurale Assets, FX-Prototyping | Tobi | ~270 EUR/Jahr |
| Houdini Engine (Ü5 Plugin) | Matching | Houdini-Ü5-Bridge | Tobi | In Indie-Lizenz enthalten |
| Substance Painter | Latest | Texturierung, Materialien | Vera, Tobi | ~220 EUR/Jahr (Indie) |
| Substance Designer | Latest | Prozedurale Materialien | Tobi | In Substance-Abo enthalten |
| Blender | 4.x | 3D-Modelling, Rigging, UV-Layout | Vera | Kostenlos |
| Photoshop / Krita | Latest | Concept Art, Texturen, UI-Mockups | Vera | ~290 EUR/Jahr (PS) oder kostenlos (Krita) |
| Perforce Helix Core | Latest | Asset-Versionskontrolle | Tobi (Admin) | Kostenlos bis 5 User |
| Jira / Notion | TBD | Taskmanagement, Sprint-Planung | Finn | ~0-100 EUR/Jahr |
| DaVinci Resolve | 19+ | Color Grading Referenz, Trailer-Schnitt | Tobi | Kostenlos (Free Version) |

**Gesamte jährliche Tool-Kosten:** ~780-1.080 EUR.

---

## 8. Meilensteine & Budget

### 8.1 Phasen

| Phase | Zeitraum | Kern-Deliverables | Abhängigkeit | Exit-Kriterium |
|-------|----------|-------------------|---------------|----------------|
| **Pre-Production** | Wochen 1-4 | GDD V1 + WBB V1 fertig. Ü5-Projekt steht. Kamera-Prototyp spielbar. Terrain-Prototyp (1 km2). Art-Style-Targets validiert | Team komplett (minus Gameplay-Programmer) | CD gibt Design-Lock. Alle können im Ü5-Projekt arbeiten |
| **Vertical Slice Prototype** | Wochen 5-12 | Spielbare Szene: 1 Region (~1 km2), Hauptquest-Ausschnitt (30 min Gameplay), Combat V1 (Schwert + Bogen, 3 Feindtypen), 1 Stadt (Blockout), Schattenfieber Stufe 0-2 | Gameplay-Programmer an Bord (spätestens Woche 5) | Szene spielbar. Combat fühlt sich "gewichtig" an |
| **Vertical Slice Polish** | Wochen 13-18 | VS spielbar und präsentabel: Beleuchtung (Lumen-Pass), Asset-Polish (Nanite, Material-Instanzen), Quest komplett, Performance-Ziele auf empfohlener Hardware, Schattenfieber Stufe 0-3 | Asset-Pipeline läuft | VS vorzeigbar (CD, Publisher, Presse) |
| **Alpha** | Wochen 19-30 | Gesamte Kernregion (4-6 km2). Alle Quests (Greybox). Combat V2 (alle 6 Waffenklassen). Nervensystem-Leveling spielbar. Alchemie V1. Schattenfieber alle Stufen inkl. Drei-Schichten | Scope-Lock (spätestens Ende Woche 18) | Feature-Complete |
| **Beta** | Wochen 31-40 | Content-Complete. Polish-Pass. QA-Runden. Performance-Optimierung. Balancing | QA-Kapazität | Alle bekannten Blocker gefixt |
| **Release** | Woche 40+ | Steam Early Access oder Full Release | CD-Entscheidung | Spielbar, stabil, repräsentativ |

### 8.2 Budget-Aufschlüsselung (45.000 EUR Freelancer-Budget) — ERWEITERT V2

Das Freelancer-Budget ist begrenzt und muss strategisch eingesetzt werden.

| Position | Geschätztes Budget | Zeitraum | Begründung |
|----------|-------------------|----------|-------------|
| **Gameplay-Programmer (GAS/Combat)** | 20.000-25.000 EUR | Wochen 5-18 (14 Wochen) | Kritischste Abhängigkeit. Ohne diese Person kein Combat, kein VS. ~1.400-1.800 EUR/Woche |
| **Animations-Assets** | 5.000-8.000 EUR | Wochen 8-18 | Marketplace-Packs + Custom-Anpassung. Motion-Matching-Datenbank. Ggf. MoCap-Session (~2.000 EUR für einen Tag) |
| **Audio/Sound Design** | 5.000-7.000 EUR | Wochen 13-30 | MetaSounds-Setup, Combat-SFX, Ambient, Schattenfieber-Audio |
| **QA-Support** | 3.000-5.000 EUR | Wochen 25-40 | Externe Tester für Schattenfieber-Stufenübergänge |
| **Marketplace-Assets** | 2.000-3.000 EUR | Laufend | Architektur-Bases, Vegetation-Packs, VFX-Bibliotheken |
| **Puffer** | 2.000-5.000 EUR | Reserve | Unvorhergesehenes |
| **Gesamt** | ~37.000-53.000 EUR | | Mittelwert: ~45.000 EUR |

**Anforderungsprofil Gameplay-Programmer (PFLICHT-Kriterien):**

- **GAS (Gameplay Ability System): Pflicht-Kriterium.** Wer kein nachweisbares GAS-Projekt vorweisen kann, kommt nicht in die engere Auswahl. Keine Ausnahmen.
- Ü5 C++ auf Produktionsniveau (kein Blueprint-only)
- StateTree-Erfahrung oder Bereitschaft zur schnellen Einarbeitung (gute Dokumentation vorhanden)
- Freelancer-Erfahrung: Milestone-basierte Abrechnung muss akzeptabel sein
- Verfügbarkeit ab Woche 5 (spätestens)
- Kommunikationssprache Deutsch oder Englisch

**Wunsch-Kriterien (kein Ausschluss):**
- Erfahrung mit Third-Person-Action-Spielen (Gothic, Souls-artige als Referenz)
- Motion Matching Erfahrung (Ü5)
- Vertrautheit mit ACES-Farb-Pipelines

**Suche beginnt:** Sofort (Woche 1). Finn führt erste Gespräche. Stellenbeschreibung: Abstimmung Tobi+Finn.

**Ehrliche Einschätzung:** 45.000 EUR ist ein sehr knappes Budget. Der Gameplay-Programmer allein verbraucht die Hälfte. Wenn diese Person länger als 14 Wochen braucht oder teurer ist als geschätzt, wird der Rest des Budgets komprimiert. Risiko-Mitigation: Früh mit der Suche beginnen, klaren Scope kommunizieren, Milestone-basierte Bezahlung vereinbaren.

---

## Anhang B: Glossar

| Begriff | Erklärung |
|---------|-----------|
| ACES | Academy Color Encoding System. Industriestandard für konsistenten Farbraum über mehrere Tools |
| GAS | Gameplay Ability System. Ü5-natives Framework für Fähigkeiten, Attribute und Gameplay-Effekte |
| HDA | Houdini Digital Asset. Wiederverwendbarer, parametrischer Houdini-Node mit vereinfachter Oberfläche |
| MPC | Material Parameter Collection. Ü5-System, um globale Werte an alle Materialien gleichzeitig zu senden |
| Nanite | Ü5-System für virtualisierte Geometrie. Automatisches LOD ohne künstlerischen Aufwand |
| Lumen | Ü5-System für dynamische globale Beleuchtung. Kein Baking nötig |
| PCG | Procedural Content Generation. Ü5-Framework für regelbasierte Asset-Platzierung |
| VSM | Virtual Shadow Maps. Ü5-Schattensystem mit hoher Auflösung |
| VS | Vertical Slice. Spielbarer, repräsentativer Ausschnitt des fertigen Spiels |
| MoCap | Motion Capture. Aufzeichnung realer Bewegungen für Spielanimationen |
| SSS | Subsurface Scattering. Lichtstreuung unterhalb einer Oberfläche. Essentiell für organische/Haut-Materialien |
| WPO | World Position Offset. Vertex-Displacement im Shader. Grundlage für atmende, lebende Oberflächen |
| PPV | Post-Processing Volume. Ü5-Container für Screen-Space-Effekte |
| SF | Schattenfieber. Abkürzung intern |

---

*Änderungen: Hex-Codes GDD-05 1:1, Kap. 1.4 Organische Shader-Architektur neu, Drei-Schichten-Rendering Kap. 5.1, Stufengrenzen CD-Lock, Halluzinations-Start korrigiert auf 76, Anforderungsprofil Gameplay-Programmer.*
*Nächster Schritt: Schattenfieber-Abstimmung terminieren, Hauten-Segmentanzahl mit Emre klären, Kamera-Blueprint V0.1.*

\clearpage
