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
