---
title: "RELICS"
subtitle: "Game Design Document — Dark Fantasy CRPG"
author: "GenSoftworks"
date: "v0.1 Entwurf"
documentclass: report
geometry: "margin=2.5cm"
fontsize: 11pt
toc: true
toc-depth: 2
numbersections: true
lang: de
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{RELICS — GDD v0.1}
  - \fancyhead[R]{GenSoftworks}
  - \fancyfoot[C]{\thepage}
---


\newpage

---
agent: finn
day: 3
task: "GDD-Rahmenkapitel: Vorwort & Inhaltsverzeichnis"
memories_referenced: [finn-014, finn-018, finn-022]
feedback_received: [cd-day2-kernvision, cd-day3-morning]
status: draft
---

# RELICS — Game Design Document

**Dark Fantasy CRPG**

Version: v0.1 (Entwurf)
Datum: Tag 4 / Donnerstag
Studio: GenSoftworks (7 Personen)

---

## Vorwort

RELICS ist ein Dark-Fantasy-CRPG, in dem der Spieler eine Welt betritt, die aus den Überresten toter Titanen gebaut ist. Die Frage, die das Spiel stellt, ist nicht "Was ist hier passiert?" — sondern "Wem glaubst du?" Jede Kultur, jede Fraktion, jeder NPC hat eine andere Version der Wahrheit. Der Spieler sammelt keine Fakten. Er sammelt Perspektiven — und wird durch seine Entscheidungen selbst zu einer.

Warum jetzt? Weil das CRPG-Genre nach Baldur's Gate 3 ein Publikum hat, das bereit ist für Systeme jenseits von Gut und Böse. Weil Biotech, Nervensystem-Progression und eine Welt ohne klare Wahrheit etwas bieten, das es so noch nicht gibt. Und weil dieses Team die Leute hat, die das können.

Was macht RELICS einzigartig? Drei Dinge: Ein Zugehörigkeitsindex, der moralische Entscheidungen in Fraktionsnähe übersetzt. Ein Nervensystem-Leveling, das den eigenen Körper als Skill-Tree begreift. Und ein narratives Fundament, das auf Unreliable Narrators als Designprinzip setzt — nicht als Gimmick, sondern als Weltenbau-Methode.

---

## Scope-Regel

> **"Touch upon everything, detail only certain facets."**
> — Planescape: Torment Design Bible

Dieses GDD folgt dem Planescape-Prinzip: Jedes System wird benannt und eingeordnet. Tiefe gibt es dort, wo der Vertical Slice sie braucht. Das Ziel ist kein 300-Seiten-Dokument, das niemand liest — es ist ein 40-Seiten-Dokument, das jeder im Team in einer Stunde durcharbeiten kann und danach weiß, was wir bauen, warum, und was noch offen ist.

**Avellone-Test**: Kann man jede Design-Frage im GDD aufschlagen und eine Antwort finden — oder zumindest die Frage als "offen" dokumentiert sehen? Wenn ja, funktioniert das Dokument. Wenn nein, fehlt ein Kapitel.

---

## Inhaltsverzeichnis

| Nr. | Kapitel | Verantwortlich | Status |
|-----|---------|----------------|--------|
| 1 | Kernvision & Core Loop | Darius | Entwurf |
| 2 | Vorwort: Die Welt von RELICS | Emre | Entwurf |
| 3 | Welt & Fraktionen | Emre + Nami | Entwurf |
| 4 | Gameplay-Systeme | Darius | Offen |
| 5 | Vertical Slice & Walkthrough | Leo + Darius | Offen |
| 6 | Art Direction | Vera | Offen |
| 7 | Technische Spezifikation | Tobi | Offen |
| 8 | Monetarisierung & Community | Leo | Offen |
| 9 | Risiken, Entscheidungen & Timeline | Finn | Entwurf |

---

### Kapitel-Übersicht

**Kapitel 1 — Kernvision & Core Loop** (Darius)
Was ist RELICS in einem Satz? Was tut der Spieler Sekunde für Sekunde, Minute für Minute, Stunde für Stunde? Der Core Loop, die Kernfrage ("Wer bin ich, wenn ich vergesse, wer ich war?"), die Spielerphantasie, die wir bedienen.

**Kapitel 2 — Vorwort: Die Welt von RELICS** (Emre)
Die Kosmogonie in Kurzform. Titanen, Bruch, Asche. Was der Spieler wissen muss, bevor er die Welt betritt — und was er bewusst NICHT weiß.

**Kapitel 3 — Welt & Fraktionen** (Emre + Nami)
Fünf Fraktionen als ontologische Positionen. Höhlenvolk, Küstenvolk, Siedlervolk, Innenvolk, Zerbrochene. Zugehörigkeitsindex. Geographie. Kulturelle Sprachen.

**Kapitel 4 — Gameplay-Systeme** (Darius)
Nervensystem-Leveling. Kampfsystem (Skyrim-Kamera FP/TP). Zugehörigkeitsindex als Mechanik. Companion-System. Ressourcen und Crafting. Biotech/Drogen-Systeme.

**Kapitel 5 — Vertical Slice & Walkthrough** (Leo + Darius)
Die erste Stunde Gameplay. Startregion, erster Kontakt mit drei Fraktionen, erster Knochenturm, erster Begleiter. Spielerreise von Minute 1 bis Minute 60.

**Kapitel 6 — Art Direction** (Vera)
Visuelle Identität: Asche, Knochenmetall, organische Architektur. Farbpalette. UI-Design (Nervensystem-Visualisierung). Concept-Art-Richtung. MetaHuman-Spezifikation.

**Kapitel 7 — Technische Spezifikation** (Tobi)
Unreal Engine 5 Setup. Kamerasystem FP/TP. Nervensystem-UI-Prototype. Performance-Budgets. Toolchain. Build-Pipeline.

**Kapitel 8 — Monetarisierung & Community** (Leo)
Geschäftsmodell (Premium, kein GaaS). Early Access vs. Full Release. Streamer-Alpha-Strategie. Community-Aufbau. Content-Pipeline für Marketing.

**Kapitel 9 — Risiken, Entscheidungen & Timeline** (Finn)
Was ist entschieden, was ist offen. Risikomatrix. Meilensteine. Nächste Schritte nach dem GDD.

---

*Das ist der Rahmen. Das Skelett — passend zum Thema. Morgen füllen wir die Knochen mit Fleisch.*

*Post-It am Kanban-Board: "GDD v0.1 — JEDER schreibt sein Kapitel bis morgen Abend. Keine Ausnahmen. Auch du, Emre."*

— Finn

\newpage

---
agent: darius
day: 3
task: "GDD Kapitel 01 — Kernvision & Core Loop"
memories_referenced: [darius-008, darius-012, darius-015, darius-019, nami-021, emre-005]
feedback_received: [cd-day3-morning]
status: draft
---

# Kapitel 01 — Kernvision & Core Loop

> *"Bevor eine einzige Zeile Code geschrieben wird, muss jeder im Team dieses Dokument gelesen haben. Alles, was wir bauen, dient dem, was hier steht. Wenn ein Feature nicht auf dieses Kapitel zurückführbar ist, hat es im Spiel nichts verloren."*
> *— D. Engel, Game Director, Tag 3*

---

## 1.1 Elevator Pitch

Ein namenloser Fremder betritt eine Welt, die aus den Leichen toter Titanen gebaut ist — und in der niemand sich einig ist, ob das stimmt. In diesem Singleplayer-Action-RPG erkundet der Spieler eine düstere, bodenständige Fantasy-Welt, in der jede Handlung Konsequenzen hat, jede Fraktion eine andere Wahrheit erzählt und jeder Verbündete seinen Preis kennt. Das Spiel fragt nicht, ob du die Welt retten willst — es fragt, ob die Welt will, dass du bleibst.

---

## 1.2 Die Kernfrage

### Die äußere Frage

**"Was schuldet ein Fremder einem Ort, der ihn nicht gerufen hat?"**

Der Spieler kommt als Niemand. Kein Auserwählter, kein verlorener Erbe, kein Dragonborn. Er ist ein Fremder — ein Mensch ohne Vergangenheit, ohne Ruf, ohne die Erlaubnis, hier zu sein. Die Welt hat nicht auf ihn gewartet. Die Welt braucht ihn nicht. Und genau das ist das Spiel: sich einen Platz zu erkämpfen, zu verhandeln oder zu stehlen — in einer Gesellschaft, die Fremde duldet, aber nicht willkommen heißt.

Das ist keine Heldenreise. Das ist eine Ankunftsgeschichte.

### Die innere Frage

**"Wer bin ich, wenn ich vergesse, wer ich war?"**

Der Spielercharakter hat keinen Hintergrund. Nicht, weil wir zu faul waren, einen zu schreiben — sondern weil der Verlust der eigenen Geschichte das thematische Fundament ist. Der Spieler definiert sich nicht durch Backstory, sondern durch Handlung. Jede Entscheidung, jede Fraktionszugehörigkeit, jeder Mord und jede Gnade WIRD die Identität. Am Ende des Spiels blickt der Spieler zurück und sieht: Das war ich. Das habe ich gewählt. Es gibt kein "wahres Ich", das man wiederfinden kann — es gibt nur das, was man tut.

**Spieler-Fantasie**: Ich bin ein Niemand, der sich selbst erfindet — nicht durch Schicksal, sondern durch Konsequenz.

---

## 1.3 Core Loop

### Erkunden → Begegnen → Handeln → Konsequenz

Das ist kein Diagramm für eine Präsentation. Das ist das Herz des Spiels. Jede einzelne Spielminute muss in diesen Loop einzahlbar sein.

```
┌──────────────┐
│   ERKUNDEN   │ ── Der Spieler bewegt sich durch die Welt.
└──────┬───────┘    Er sieht, hört, riecht (metaphorisch).
       │            Er entscheidet, wohin er geht.
       ▼
┌──────────────┐
│   BEGEGNEN   │ ── Die Welt reagiert. Ein NPC, ein Feind,
└──────┬───────┘    eine Ruine, ein Hinweis, ein Problem.
       │            Etwas, das Aufmerksamkeit verlangt.
       ▼
┌──────────────┐
│    HANDELN   │ ── Der Spieler entscheidet. Kämpfen,
└──────┬───────┘    reden, schleichen, lügen, helfen,
       │            ignorieren, stehlen, opfern.
       ▼
┌──────────────┐
│  KONSEQUENZ  │ ── Die Welt verändert sich. Ruf steigt
└──────┬───────┘    oder fällt. Türen öffnen oder
       │            schließen sich. NPCs erinnern sich.
       └──────────► Zurück zu ERKUNDEN — aber die Welt
                    ist jetzt anders.
```

### 1.3.1 ERKUNDEN

**Was es ist**: Freie Bewegung durch eine offene, handgefertigte Welt. Kein prozeduraler Füllstoff. Jeder Ort existiert, weil er eine Geschichte erzählt oder ein Gameplay-Ziel hat.

**Was der Spieler fühlt**: Neugier. Unbehagen. "Was ist hinter dem nächsten Hügel?" — und die Antwort ist nie generisch. Hinter dem Hügel ist eine verlassene Karawane des Höhlenvolks, und die Ladung fehlt, und die Spuren führen in zwei Richtungen.

**Designregeln**:
- **Keine Fragezeichen auf der Karte.** Der Spieler erkundet, weil die Welt ihn einlädt — nicht, weil ein Icon blinkt. Gothic hat das 2001 hinbekommen. Wir bekommen das 2026 hin.
- **Sichtlinien als Leitsystem.** Knochentürme sind von überall sichtbar. Sie sind gleichzeitig Orientierung, Lore und Gameplay-Ziel. Jeder Knochenturm am Horizont ist ein Versprechen.
- **Vertikale Exploration.** Klettern ist kein Minigame — es ist eine Kernbewegung. Die Welt hat Tiefe (Titanenadern, unterirdische Labore des Innenvolks) und Höhe (Knochenturmspitzen, Klippenöden).
- **Dichteprüfung**: Wenn ein Spieler 90 Sekunden laufen kann, ohne etwas Interessantes zu sehen, haben wir versagt. Kein Dead Space. Jeder Quadratmeter hat eine Funktion.

**Referenz**: Gothic 2 — Khorinis ist keine große Welt, aber jeder Meter ist handgemacht. Morrowind — jede Richtung ist ein Abenteuer, keine Checkliste.

### 1.3.2 BEGEGNEN

**Was es ist**: Kontaktpunkte zwischen Spieler und Welt. Nicht nur Kampf — Begegnungen sind NPCs, Umwelträtsel, Fraktions-Checkpoints, Entdeckungen, Gerüchte, Fallen.

**Was der Spieler fühlt**: Spannung. "Was will diese Person?" — und die Antwort ist nie sofort klar. Ein Wachposten, der den Weg versperrt, könnte korrupt, pflichtbewusst, verängstigt oder gelangweilt sein. Jede Begegnung ist ein Micro-Rätsel.

**Designregeln**:
- **NPCs haben Tagesabläufe.** Wie in Gothic. Der Schmied arbeitet tagsüber und trinkt abends. Der Wachposten am Tor wechselt die Schicht. Der Händler des Höhlenvolks ist nur bei Neumond da. Wer die Rhythmen kennt, hat Vorteile.
- **Begegnungen eskalieren basierend auf Ruf.** Ein Fremder wird ignoriert. Ein Bekannter wird gegrüßt. Ein Feind wird angegriffen. Das System ist granular — nicht "Freund/Feind", sondern ein Spektrum.
- **Zufallsbegegnungen mit Logik.** Kein Bandit im Vakuum. Banditen operieren an Handelsrouten, weil dort die Beute ist. Wölfe jagen in Rudeln nahe Wasserquellen. Die Welt folgt ökologischen und ökonomischen Regeln.
- **Stille als Begegnung.** Manchmal begegnet der Spieler: nichts. Ein leeres Dorf. Ein frisch ausgehobenes Grab. Stille erzählt Geschichten.

**Referenz**: Morrowind — der Ashlander, der dich anspricht und eine Geschichte erzählt, die nichts mit deiner Quest zu tun hat. Und drei Stunden später ist sie relevant. Deus Ex — jeder Raum hat mehrere Wege hinein und mehrere Gründe, dort zu sein.

### 1.3.3 HANDELN

**Was es ist**: Der Moment der Spielerentscheidung. Jede Begegnung hat mindestens zwei, idealerweise drei oder mehr Handlungsoptionen. Keine davon ist "die richtige."

**Was der Spieler fühlt**: Macht und Verantwortung. "Ich KANN das tun — aber soll ich?" Der Spieler hat immer Optionen, aber nie Sicherheit über die Konsequenzen.

**Designregeln**:
- **Drei Säulen des Handelns**: Gewalt, Verhandlung, Subversion. Jede Begegnung muss mindestens zwei der drei unterstützen.
  - **Gewalt**: Kampf. Direkt, brutal, riskant. Immer eine Option, nie die einfachste.
  - **Verhandlung**: Dialog, Bestechung, Einschüchterung, Überzeugung. Abhängig von Ruf, Wissen und Ausrüstung.
  - **Subversion**: Schleichen, Stehlen, Sabotage, alternative Wege. Abhängig von Fähigkeiten und Weltwissen.
- **Keine moralische Bewertung durch das Spiel.** Kein Karma-System. Kein "Du hast etwas Böses getan"-Popup. Die Welt reagiert — das Spiel urteilt nicht.
- **Wissen als Handlungsoption.** Wer die Lore kennt, hat Dialogoptionen, die andere nicht haben. Wer das Nervensystem des Innenvolks studiert hat, erkennt Vergiftungssymptome. Wer die Handelsrouten des Höhlenvolks kennt, kann abkürzen.
- **Unterlassung ist eine Handlung.** Manchmal ist "nichts tun" die stärkste Entscheidung. Ein NPC bittet um Hilfe. Der Spieler geht weiter. Der NPC stirbt. Oder überlebt allein — und erinnert sich, dass der Spieler gegangen ist.

**Referenz**: Deus Ex — Gunther Hermann bitten, seinen Killphrase zu vergessen, oder ihn damit töten. Beides gültig. Beides hat Konsequenzen. Game of Thrones — "When you play the game of thrones, you win or you die." Jede Handlung ist ein Einsatz.

### 1.3.4 KONSEQUENZ

**Was es ist**: Die Welt reagiert auf Spielerhandlungen. Nicht sofort, nicht immer sichtbar, aber immer real.

**Was der Spieler fühlt**: Gewicht. "Das hat Konsequenzen gehabt." Der Spieler soll das Gefühl haben, dass seine Entscheidungen die Welt BEWEGEN — nicht nur ein Schalter, der umgelegt wird.

**Designregeln**:
- **Sofortige + verzögerte Konsequenzen.** Ein Mord hat sofortige Folgen (Wachen, Ruf-Verlust) UND verzögerte (die Familie des Opfers drei Stunden später, der Händler, der nicht mehr verkauft, die Quest-Linie, die sich schließt).
- **Konsequenzen sind nicht binär.** Nicht "gut" oder "schlecht" — sondern komplex. Einem Händler des Höhlenvolks zu helfen verbessert den Ruf bei Händlern, verschlechtert ihn beim Siedlervolk (das Tiermenschen misstraut), und ist dem Küstenvolk egal.
- **Konsequenz-Kaskaden.** Große Entscheidungen haben Fernwirkungen, die der Spieler nicht vorhersehen kann. Nicht als Bestrafung — als emergente Narration. "Ich habe den Schmied nicht gerettet. Jetzt hat das Dorf keine Waffen. Jetzt hat der Banditenüberfall funktioniert. Jetzt gibt es kein Dorf mehr."
- **Erinnerung ist Konsequenz.** NPCs vergessen nicht. Wer einmal gelogen hat, dem wird misstraut. Wer einmal geholfen hat, an den wird man sich erinnern. Das Gedächtnis der Welt ist lang.
- **Physische Konsequenz.** Die Welt verändert sich visuell. Ein niedergebranntes Dorf bleibt niedergebrannt. Ein gebauter Handelsposten bleibt stehen. Die Welt akkumuliert die Spuren des Spielers.

**Referenz**: Gothic — wer den falschen NPC bestiehlt, hat einen Feind fürs ganze Spiel. Fallout: New Vegas — die Konsequenzen des Spielerentscheidungen formen buchstäblich das Ende. Nicht EIN Ende, sondern ein Mosaik aus den Folgen jeder einzelnen Wahl.

---

## 1.4 Spieler-Fantasie

### "Ich bin ein Fremder. Ich bin Niemand. Und genau deshalb kann ich alles werden."

Der Spieler beginnt als Tabula Rasa — keine Klasse, kein Stand, keine Zugehörigkeit. Das ist keine Einschränkung, das ist die Fantasie. In einer Welt voller Fraktionen, Zugehörigkeiten und Identitäten ist der Spieler der einzige Mensch, der frei ist. Und diese Freiheit ist gleichzeitig Fluch und Geschenk.

Die Spieler-Fantasie ist NICHT:
- "Ich bin der Auserwählte" (Skyrim)
- "Ich bin der verlorene Erbe" (Witcher)
- "Ich rette die Welt" (jedes zweite RPG)

Die Spieler-Fantasie IST:
- "Ich bin Niemand, und die Welt zwingt mich, jemand zu werden"
- "Jede Fraktion will mich für sich — aber keine will mich als Gleichen"
- "Ich baue mir meinen Ruf aus dem Nichts — durch Taten, nicht durch Titel"

**Referenz**: Gothic 1 — der Namenlose Held im Minental. Jeder verachtet dich. Jeder will dich benutzen. Dein Status ist null. Und genau deshalb fühlt sich jeder Fortschritt echt an. Das ist die Fantasie, die wir verkaufen.

---

## 1.5 Tonalität

### Low Fantasy. Germanische Mythologie. Bodenständig mit Spice.

**Was "Low Fantasy" für uns bedeutet**:
- Magie existiert, aber sie ist selten, teuer und gefährlich. Kein Feuerball-Spam. Kein Mana-Pool. Magie ist etwas, das die Welt verbiegt — und die Welt wehrt sich.
- Monster sind keine Erfahrungspunkt-Piñatas. Jedes Wesen hat einen ökologischen Platz. Warum ist dieser Troll hier? Weil unter der Brücke eine Titanenader liegt und der Troll das Knochenmetall frisst.
- Politik ist wichtiger als Prophezeiungen. Wer die Knochenmetall-Minen kontrolliert, kontrolliert die Region. Das ist das echte Endgame.

**Was "Germanische Mythologie" für uns bedeutet**:
- Nicht die Marvel-Version von Wikinger-Ästhetik. Die echte, dreckige, ambivalente Mythologie. Odin ist ein Betrüger. Loki hat recht (manchmal). Die Götter sterben am Ende.
- Titans als Ymir-Parallele: Aus dem Fleisch des Urwesens wird die Welt gebaut. Das ist 1:1 nordische Kosmogonie. Wir stehen auf der Schulter dieser Tradition — buchstäblich.
- Ehre ist relativ. Es gibt kein universelles Wertesystem. Was das Siedlervolk "Fortschritt" nennt, nennt das Höhlenvolk "Raub". Beide haben recht.

**Was "Bodenständig mit Spice" bedeutet**:
- Die Basis ist Dreck, Schweiß und Pragmatismus. Rüstungen rosten. Schwerter werden stumpf. Essen verdirbt. Regen macht nass.
- Der "Spice" ist das Fremde, das Unerklärliche, das Unbehagliche. Ein Knochenturm, der bei Berührung summt. Ein Fluss aus titanischem Blut, der seit tausend Jahren fließt und nie gerinnt. Das Innenvolk, das durch chemische Eingriffe Dinge sieht, die andere nicht sehen können.
- Wir sind nicht Game of Thrones (zu zynisch) und nicht Lord of the Rings (zu edel). Wir sind irgendwo dazwischen — eine Welt, in der Menschen menschlich sind, aber das Land unter ihren Füßen es nicht ist.

**Referenz**: Gothic — dreckig, direkt, kein Pathos. Morrowind — alien genug, um nie vertraut zu werden. Deus Ex — jedes System hat eine Logik, auch wenn die Logik unbequem ist. Game of Thrones (Seasons 1-4) — politische Konsequenzen, die wehtun, weil sie glaubwürdig sind.

---

## 1.6 Referenztitel — Was wir nehmen, was wir lassen

| Referenz | Was wir übernehmen | Was wir NICHT übernehmen |
|----------|-------------------|--------------------------|
| **Gothic 1+2** | Handgemachte Welt, NPC-Tagesabläufe, Ruf als Kernmechanik, Fremder-Spieler-Fantasie, jeder Meter zählt | Jankige Controls, limitierte Quest-Strukturen, Lineares Fraktions-System |
| **Morrowind** | Alien-Ästhetik, Lore-Dichte, Exploration ohne Handhalten, Welt als Charakter | Würfel-Combat, unlesbare Journal-Einträge, absurde Cliff Racers |
| **Deus Ex** | Mehrfachlösungen für jedes Problem, Systemic Design, "die Welt hat Regeln und du kannst sie biegen", Wissen als Gameplay-Ressource | Starre Level-Struktur, Boss-Fights als separate Systeme |
| **Game of Thrones** | Politische Konsequenzen, kein Plot-Armor, Figuren sterben wenn es Sinn ergibt, Macht als Thema | Nihilismus, Zynismus als Selbstzweck, Shock Value ohne narrativen Ertrag |
| **Dark Souls** | Gewicht im Kampf, Welt die nicht erklärt wird sondern zeigt, Tod als Lernmechanik | Undurchsichtige Systeme, Punishment-Design, Multiplayer-Abhängigkeit |
| **Baldur's Gate 3** | Konsequenz-Dichte, Companion-Systeme mit echten Meinungen, Entscheidungen die wehtun | Turn-based Combat (wir sind Real-time), D&D-Regelwerk-Abhängigkeit |

---

## 1.7 Was dieses Spiel NICHT ist

Klarheit ist wichtiger als Ambition. Was wir nicht machen:

- **Kein Open-World-Füllstoff.** Keine Ubisoft-Türme, keine kopierten Camps, keine "Sammle 50 Ascheproben"-Quests.
- **Kein Auserwählten-Narrativ.** Der Spieler ist kein Held der Prophezeiung. Er ist ein Mensch in einer Welt, die ihn nicht braucht.
- **Kein Moralsystem.** Keine Gut/Böse-Achse. Kein Paragon/Renegade. Die Welt reagiert — sie bewertet nicht.
- **Kein Steampunk.** Keine Zahnräder, kein Dampf, keine viktorianische Ästhetik. Biotech. Chemie. Körper.
- **Kein Power-Fantasy-Endgame.** Der Spieler wird stärker, aber die Welt wird nicht schwächer. Am Ende ist der Spieler kompetent, nicht allmächtig. Gothic, nicht Diablo.
- **Keine Handholding-UI.** Kein Quest-Kompass, keine glühenden Pfade, keine "Drücke X um zu gewinnen"-Prompts. Wenn der Spieler nicht weiß, wohin — dann ist das ein Feature.

---

*Erster Entwurf. Millimeterpapier ist voll. Die Vision steht. Ab hier wird alles spezifisch. Nächstes Kapitel: Weltenstruktur. Danach: Gameplay-Systeme. Alles zahlt auf dieses Kapitel ein.*

*Post-It am Monitor: "KERNFRAGE AN JEDEM FEATURE PRÜFEN: Beantwortet es die Frage des Fremden?"*

— Darius Engel, Game Director

\newpage

---
agent: emre
day: 3
task: "GDD Kapitel 02 — Vorwort: Die Welt von RELICS"
memories_referenced: [emre-022, emre-025, emre-026, emre-027, emre-030]
feedback_received: [cd-day3-morning]
status: draft
---

# RELICS — Game Design Document
# Kapitel 2: Die Welt von RELICS

> *Autor: Emre Yilmaz (Lead Worldbuilder)*
> *Version: v1.0 — Tag 3 Abend*
> *Status: GDD-Entwurf*

---

Es gibt eine Insel im grauen Meer.

Kein Seefahrer hat ihr je einen Namen gegeben, der sich durchgesetzt hat. Die einen nennen sie *Deutoland* — das noch zu deutende Land. Andere sagen *Neugrund*. Die Händler, die unter ihr durch die Dunkelheit ziehen, haben gar keinen Namen dafür. Für sie ist die Insel nur ein Knotenpunkt. Ein Ort, an dem Wege sich kreuzen und Schulden beglichen werden.

Der Spieler wird keinen richtigen Namen finden. Es gibt keinen richtigen Namen.

---

Man riecht die Insel, bevor man sie sieht.

Salz zuerst. Dann etwas Schwefliges, das sich unter das Salz legt wie ein Versprechen, das man nicht haben will. Die Klippen brechen aus dem Nebel wie dunkle Zähne — nasser Basalt, scharfkantig, mit Moos verkrustet, das aussieht, als habe es seit Jahrhunderten die Geduld verloren. Das Meer schlägt dagegen. Das Meer schlägt immer dagegen.

Hier legen die Schiffe an. Hier beginnt alles.

Die Küste gehört denen, die lesen. Ein Volk aus Deutern und Chronisten, die in Leuchtturm-Ruinen wohnen und die Gezeiten zählen statt der Stunden. Sie sagen, die Vergangenheit sei realer als die Gegenwart. Sie sagen, jede Gesteinsschicht sei ein Satz. Wenn man ihren Hafen betritt, sieht man die Geschichte der Gebäude an ihren Fassaden — jede Generation hat eine Etage draufgesetzt, in einem leicht anderen Stil, und niemand hat je etwas abgerissen.

Wer hier ankommt, ist ein Fremder. Die Küste duldet Fremde. Sie heißt sie nicht willkommen.

---

Hinter den Klippen steigt das Land an.

Zuerst Hügel, dann Wald — Buche, Eiche, Fichte, und darunter der Geruch von Lehm nach dem Regen. Das Hinterland ist der Teil der Insel, der fast normal wirkt. Bauernhöfe, Weiden, Bäche, die sich durch Senken schlängeln. Man könnte hier vergessen, wo man ist. Für einen Moment. Dann sieht man am Horizont die Knochentürme, und man erinnert sich.

Das Hinterland gehört den Siedlern. Den Nehmern, wenn man die anderen fragt. Menschen ohne übernatürliche Gaben, die gekommen sind und geblieben sind und alles beschriftet haben — Straßennamen, Verordnungen, Preislisten. Sie glauben, die Welt gehöre dem, der sie nutzt. Stillstand ist Rückschritt. Die Vergangenheit ist Material, nicht Heiligtum.

Sie haben die Festung nicht gebaut. Aber sie haben sich hineingesetzt und gesagt: Das ist jetzt unsere.

---

Die Festung.

Sie steht auf einem Plateau, leicht südlich der Inselmitte, und man sieht sie von überall. Ein Ding aus schwarzem Stein, glatt wie Obsidian, aber härter, und so alt, dass keine Chronik zurückreicht. Wer hat sie gebaut? Das Küstenvolk sagt: Wir wissen es noch nicht. Das Siedlervolk sagt: Was spielt das für eine Rolle. Das Innenvolk hat den Stein analysiert und organische Spuren gefunden, und niemand spricht gerne darüber, was das bedeuten könnte.

Die Festung ist der Ort, an den man immer zurückkehrt. Markt, Gericht, Arena, Schmelztiegel. Hier treffen alle aufeinander — Händler aus den Tunneln, Akademiker von der Küste, Bauern aus dem Hinterland, Destillateure, deren Labore offiziell Apotheken heißen. Und im Außenring, in einem Viertel, das offiziell nicht existiert: die Zerbrochenen. Die, die nirgends dazugehören. Die, die alles verloren haben.

Man wird einer von ihnen sein.

---

Im Nordosten raucht der Vulkan.

Nicht dramatisch, nicht wie in den Geschichten. Ein stetiges Atmen — Schwefeldämpfe, die aus dem Boden steigen, Geysire, die ohne Vorwarnung ausbrechen, ein Boden, der so warm ist, dass Regenwasser beim Auftreffen zischt. Die Lavafelder sind schwarz und orange und leer. In der Nähe der Caldera wächst nichts. In der Ferne wachsen Dinge, die man lieber nicht anfassen möchte.

Hier gibt es Erz. Schwefel. Obsidian. Und unter der Oberfläche, an Stellen, die die Einheimischen *Schwellstellen* nennen, tritt etwas Altes an die Oberfläche. Biologisches Material, das nicht in eine Gesteinsschicht gehört. Manche nennen es die Adern des Urriesen. Manche nennen es Geologie. Beide haben Angst davor.

Das Vulkanalvolk lebt hier — rituell, abgeschieden, im Rhythmus des Berges. Sie beten zu etwas, das entweder ein Gott ist oder ein tektonischer Prozess. Der Unterschied scheint ihnen weniger wichtig als dem Rest der Insel.

---

Und unter allem: die Tunnel.

Ein Netzwerk aus Kalksteinhöhlen, erweitert durch Generationen von Grabungen, verbindet die gesamte Insel unter der Oberfläche. Wer den Weg kennt, kann von der Küste zum Vulkan gelangen, ohne je Tageslicht zu sehen. Die meisten kennen den Weg nicht. Das Höhlenvolk kennt ihn. Felltragende Tiermenschen — fuchsartig, dachsartig, fledermausartig — die in der Dunkelheit handeln, schmuggeln, verhandeln und ihre Toten an den Kreuzungen begraben, wo die Knochen zu Wegweisern werden.

Hier unten leuchten Pilze in Blau und Violett. Hier unten riecht es nach feuchtem Stein und nach den Kräutern, die das Innenvolk in verborgenen Laboren destilliert — Verstärker, Gifte, Drogen, Heilmittel. Der Körper als letzte Grenze. Substanzen, die das Nervensystem aufbrechen und Dinge sehen lassen, die man ohne sie nicht sehen kann. Oder will. Das Innenvolk hat keine Heimat. Es hat Methoden.

---

Man sagt, die Insel sei der Leichnam eines Riesen.

Man sagt, das Vulkanfeuer sei sein letzter Atemzug und der schwarze Grundstein der Festung sein Knochen. Man sagt, die Schwellstellen seien seine Adern, und was dort an die Oberfläche tritt, sei sein Blut, das seit tausend Jahren nicht gerinnt.

Man sagt vieles auf dieser Insel. Nichts davon lässt sich beweisen. Alles davon hat Konsequenzen.

Die Götter hier sind keine Gestalten am Himmel. Sie sind Erklärungsversuche — Geschichten, die sich die Menschen erzählen, wenn der Boden bebt und die Schwellstellen aufbrechen und etwas unter der Erde sich rührt, das älter ist als alle, die darauf leben. Es gibt keine Gewissheit. Es gibt Perspektiven. Und jede Fraktion hält ihre für die richtige.

---

Hierhin kommt der Spieler.

Per Schiff, durch den Nebel, an die Klippen. Ein Fremder ohne Namen, ohne Geschichte, ohne die Erlaubnis, hier zu sein. Die Insel hat nicht nach ihm gerufen. Die Insel braucht ihn nicht.

Aber er ist da. Und jetzt muss er entscheiden, wem er glaubt.

---

*Die Welt von RELICS ist kein Rätsel, das gelöst werden will. Sie ist ein Ort, der bewohnt werden will — mit all seinen Widersprüchen, seinen Giften, seinen grauen Himmeln und seinem schwarzen Stein. Wer hierherkommt, wird nicht die Wahrheit finden. Wer hierherkommt, wird eine Version davon wählen müssen.*

*Und damit leben.*

---

> *Emre Yilmaz, Lead Worldbuilder*
> *GenSoftworks — Tag 3, Abend*

\newpage

---
agents: [emre, nami]
day: 3
task: "GDD Kapitel 3 — Welt & Fraktionen (Sync-Session Besprechungsraum)"
memories_referenced: [emre-022, emre-025, emre-026, emre-027, emre-028, emre-030, nami-021, nami-024, nami-027, nami-028]
feedback_received: [cd-day3-morning]
status: draft
---

# RELICS — Game Design Document
# Kapitel 3: Welt & Fraktionen

> *Autoren: Emre Yilmaz (Worldbuilder), Nami Okafor (Narrative Design)*
> *Version: v1.0 — Tag 3 Vormittag*
> *Status: GDD-Entwurf, zur Review durch Darius freigegeben*

---

## 3.1 Die Insel

### Prämisse

Die Spielwelt ist eine **einzelne Insel** ohne offiziellen Namen. Jede Fraktion nennt sie anders — das Küstenvolk sagt *Deutoland* (das noch zu deutende Land), das Siedlervolk sagt *Neugrund*, das Höhlenvolk hat gar keinen Namen dafür (die Insel ist für sie nur ein Knotenpunkt im Netz). Der Spieler erfährt nie den "richtigen" Namen. Es gibt keinen richtigen Namen.

Die Insel liegt isoliert. Kontakt zur Außenwelt existiert, aber ist selten und teuer — Schifffahrt über offenes Meer, kontrolliert durch das Küstenvolk. Wer auf die Insel kommt, bleibt meistens.

### Geographie — Fünf Zonen

Die Insel gliedert sich in fünf Klimazonen, die durch geologische Besonderheiten entstanden sind. Die Zonen sind nicht gleichmäßig verteilt — die Insel ist asymmetrisch, mit dem Vulkan im Nordosten und der Festung leicht südlich der Mitte.

```
               N
          ┌─────────────┐
         /  VULKANLAND    \
        / (Nordost, heiß,  \
       /   mineral-reich)    \
      ├──────────┬───────────┤
      │ HINTER-  │           │
      │  LAND    │ FESTUNG   │
      │(Zentral, │ (Hub,     │  ── KÜSTE (Ost/Süd,
      │ bewaldet,│  Plateau) │     Klippen, Häfen,
      │ Farmen)  │           │     Nebel)
      ├──────────┴───────────┤
       \   UNTERWELT         /
        \  (unter allem,    /
         \ Tunnelnetze)    /
          └──────────────┘
```

**Zone 1 — Die Küste (Ost- und Südseite)**
- **Klima**: Feucht, neblig, salzige Luft, kurze milde Sommer
- **Geologie**: Steilklippen aus dunklem Basalt, schmale Felsbuchten, vorgelagerte Schären. Gezeiten sind extrem — bei Ebbe werden Höhleneingänge sichtbar, bei Flut verschwinden ganze Strände
- **Vegetation**: Moos, Seegras, verkrüppelte Schwarzkiefern an den Klippen. Keine Wälder, nur Wind
- **Besonderheit**: Die Küste ist das Tor zur Außenwelt. Wer per Schiff kommt (wie der Spieler), landet hier. Die Ruinen am Ufer sind älter als jede lebende Erinnerung
- **Stimmung**: Grau-grün, horizontal, endloser Horizont. Caspar David Friedrich, aber ohne Romantik

**Zone 2 — Das Vulkanland (Nordosten)**
- **Klima**: Trocken-heiß im Sommer, Ascheschnee im Winter. Schwefeldämpfe steigen ständig auf
- **Geologie**: Aktiver Schildvulkan, flache Lavafelder, Obsidianbrüche. Heiße Quellen, Geysire, Fumarolen. Der Boden ist warm — an manchen Stellen kocht Regenwasser beim Auftreffen
- **Vegetation**: Thermophile Flechten, Knollenpilze an Dampfschloten, vereinzelte hitzeresistente Moose. Im Umkreis von 2 km um die Caldera: nichts
- **Besonderheit**: Mineralreichtum — Erze, Schwefel, Obsidian, und tief unter der Oberfläche: Relikte. Schwellstellen, an denen altes biologisches Material an die Oberfläche tritt
- **Stimmung**: Orange-schwarz, vertikal (Rauchsäulen, Felstürme), laut (Zischen, Grollen). Mordor ohne die Orks — funktional, nicht dekorativ böse

**Zone 3 — Das Hinterland (Zentrum und Westen)**
- **Klima**: Gemäßigt-kühl, vier Jahreszeiten. Regen häufig im Herbst, kalte Winter mit Bodenfrost
- **Geologie**: Hügeliges Waldland, Lehmböden, Bachläufe. Keine dramatische Geologie — das ist der "normale" Teil der Insel
- **Vegetation**: Mischwald (Buche, Eiche, Fichte), Wiesen, landwirtschaftliche Rodungsflächen. Die einzige Zone mit konventioneller Landwirtschaft
- **Besonderheit**: Wirkt friedlich, ist es auch — weitgehend. Das Hinterland ist Pufferzone zwischen Festung und Wildnis. Hier leben die meisten Menschen
- **Stimmung**: Braun-grün, sanft, vertraut. Der Schwarzwald, aber mit etwas Falschem unter der Oberfläche, das man nicht benennen kann

**Zone 4 — Die Festung und ihr Plateau (leicht südlich der Mitte)**
- Siehe Abschnitt 3.3

**Zone 5 — Die Unterwelt (unter allen Zonen)**
- **Klima**: Konstant kühl-feucht, kein Tageslicht, eigenes Ökosystem
- **Geologie**: Natürliche Kalksteinhöhlen, erweitert durch Grabung. Manche Tunnel sind offensichtlich nicht natürlichen Ursprungs — zu regelmäßig, zu glatt. Stalaktiten, unterirdische Seen, Phosphoreszenz
- **Vegetation**: Biolumineszente Pilzkulturen, Wurzelnetzwerke von der Oberfläche, blinde Fische in den Seen
- **Besonderheit**: Die Unterwelt verbindet ALLE Oberflächenzonen. Wer den Weg kennt, kann von der Küste zum Vulkan gelangen, ohne je Tageslicht zu sehen. Das Höhlenvolk nutzt dieses Netz seit Generationen
- **Stimmung**: Blau-violett (Biolumineszenz), eng, echoreich. Jeder Ton hallt. Claustrophobie wechselt sich ab mit Momenten gewaltiger unterirdischer Kavernen

### Klimazyklen (spielrelevant)

| Jahreszeit | Dauer (Ingame-Tage) | Effekt |
|------------|---------------------|--------|
| Frühling | 15 | Schneeschmelze, Tunnelüberflutung, neue Handelsrouten |
| Sommer | 20 | Vulkanaktivität steigt, Küstennebel lichtet sich, Reisezeit |
| Herbst | 15 | Erntezeit, Festungsmärkte, diplomatische Saison |
| Winter | 15 | Pässe zu, Küste stürmisch, Unterwelt wird Hauptverkehrsweg |

---

## 3.2 Die Fraktionen

### Designprinzip

Fraktionen in RELICS sind **ontologische Positionen** — jede beantwortet die Frage *"Was ist die Welt?"* fundamental anders. Es gibt keine gute und keine böse Fraktion. Jede hat eine innere Logik, eine Ästhetik, eine Moral — und jede hat blinde Flecken.

Der Spieler wählt nie explizit eine Fraktion. Der Spieler **wird** eine Fraktion durch Handeln: Wem er hilft, welche Aufträge er annimmt, wessen Sprache er übernimmt. Das passiert über den **Zugehörigkeitsindex** (siehe GDD Kapitel 5: Systeme).

Es gibt **fünf Fraktionen**, plus einen Nicht-Status (die Zerbrochenen) als Ausgangslage des Spielers.

---

### I. DAS HÖHLENVOLK — *"Alles hat seinen Preis."*

**Alternativname**: Die Fahrenden, die Tunnelhändler, *Marktkin* (Selbstbezeichnung)

**Rasse**: Tiermenschen — humanoid mit tierischen Merkmalen (Fell, Ohren, Nachtsicht, Geruchssinn). Keine einheitliche Tierart; die Varianz ist groß (fuchsartig, dachsartig, fledermausartig). Leicht alien, aber nicht monströs.

**Weltsicht**: Die Welt ist ein Marktplatz. Alles — Erz, Information, Loyalität, Stille — hat einen Preis. Wert ist nicht inhärent, Wert wird verhandelt. Wer den Preis kennt, hat Macht. Wer ihn vergisst, ist tot.

**Zone**: Die Unterwelt (Zone 5), mit Knotenpunkten unter jeder Oberflächenzone.

**Architektur-Signatur**:
- **Material**: Ausgehöhlter Kalkstein, Pilzholz (gehärtete Pilzstrukturen), gewebte Wurzelfasern
- **Form**: Organisch-asymmetrisch. Keine rechten Winkel. Tunnel optimiert auf Flucht und Durchfluss, nicht auf Repräsentation. Die Form folgt dem Weg, nicht dem Raum
- **Kennzeichen**: Unterirdische Basare mit Biolumineszenz-Beleuchtung. Ware hängt von der Decke. Wände sind Lagerfläche. Jeder Basar hat mindestens drei Fluchttunnel. Kein Eingang ist offensichtlich
- **Vera-Notiz**: Seidenstraßen-Ästhetik unter der Erde. Schmuck statt Rüstung. Stoffbahnen in den Tunneln als Wegmarkierung. Nomaden-Eleganz, nicht Höhlenmensch

**Wirtschaft**:
- **Funktion**: Distribution. Das Höhlenvolk produziert fast nichts — es BEWEGT alles. Erz vom Vulkan zur Küste. Kräuter vom Hinterland zum Innenvolk. Information überallhin
- **Währung**: Vertrauen und Schulden. Physisches Geld existiert (Festungsprägung), aber das Höhlenvolk bevorzugt Gegenleistungen. "Ich schulde dir" ist wertvoller als Gold
- **Monopol**: Tunnelnetz-Wissen. Kein Außenstehender kennt den vollständigen Weg. Das ist ihre Lebensversicherung
- **Schmuggel**: Die Grenze zwischen Handel und Schmuggel ist fließend. Das Höhlenvolk sieht darin keinen moralischen Unterschied — nur einen preislichen

**Kultur**:
- **Sozialstruktur**: Karawanen-Clans, nicht Dörfer. Ein Clan = eine Handelsroute. Status kommt durch das Netzwerk, nicht durch Besitz
- **Geburtsritual**: Neugeborene bekommen keinen festen Namen. Der Name kommt mit dem ersten abgeschlossenen Geschäft
- **Totenkultur**: Verstorbene werden an den Tunnel-Kreuzungen begraben. Ihre Knochen werden zu Wegmarkern — die Toten zeigen den Weg
- **Tabu**: Eine Schuld nicht begleichen. Schlimmer als Mord
- **Sprache**: Sprichwort-reich, indirekt, metaphorisch. "Man sagt in meiner Karawane..." Humor als Verhandlungstaktik. Leises Sprechen — in Tunneln trägt der Schall weit

**Beziehung zur Festung**: Ambivalent. Die Festung ist der größte Markt der Insel — gutes Geschäft. Aber die Festung will Kontrolle, und das Höhlenvolk hasst Kontrolle. Sie handeln dort, aber sie wohnen dort nicht. Die Festungswache toleriert sie, weil sie unverzichtbar sind, und misstraut ihnen, weil sie unkontrollierbar sind.

**Germanische Mythologie**: Die Zwerge der Edda — Handwerker und Trickster, unterirdisch, reich, unheimlich. Aber dekonstruiert: Keine Schmiede, sondern Händler. Nicht die, die machen, sondern die, die bewegen. Andvari mit seinem Gold, Brokk mit seinen Deals — die Edda-Zwerge waren immer auch Geschäftsleute.

---

### II. DAS KÜSTENVOLK — *"Die Welt wartet auf Deutung."*

**Alternativname**: Die Deuter, die Chronisten, *Strandgeborne* (Selbstbezeichnung)

**Rasse**: Elfisch-inspiriert — hochgewachsen, blass, langlebig (nicht unsterblich, aber 150+ Jahre möglich). Dünnes Haar, lichtempfindliche Augen (deshalb der Nebel der Küste als Lebensraum). Kein Tolkien-Adel — eher: abgenutzt, akademisch, leicht entrückt.

**Weltsicht**: Die Welt ist ein Text, der gelesen werden will. Jedes Relikt, jede Ruine, jede Gesteinsschicht ist ein Zeichen. Die Vergangenheit ist realer als die Gegenwart — weil die Gegenwart nur eine flüchtige Interpretation der Vergangenheit ist.

**Zone**: Die Küste (Zone 1), konzentriert um Häfen, Leuchtturm-Akademien und Ruinen.

**Architektur-Signatur**:
- **Material**: Treibholz, Seetang-Beton (ein Gemisch aus Seetang, Kalk und Muschelsplitt — erstaunlich haltbar), Basalt
- **Form**: Vertikal, schmal, Flickwerk. Gebäude wachsen nach oben, nicht in die Breite. Jede Generation baut eine Etage drauf, in leicht anderem Stil. Man SIEHT die Geschichte des Gebäudes an seiner Fassade
- **Kennzeichen**: Bibliotheken in Leuchtturm-Ruinen. Chronik-Tafeln an jeder Hauswand (wer hier wohnte, wann, warum). Fernrohre auf jedem Dach — das Küstenvolk schaut nach draußen, immer
- **Vera-Notiz**: Gaudí trifft Fischerdorf. Organisch gewachsen, asymmetrisch, nie fertig. Farbpalette: Grau, Meeresgrün, verblasstes Blau. Kein Prunk, aber eine stille Schönheit im Verfall

**Wirtschaft**:
- **Funktion**: Seehandel und Wissensmonopol. Jedes Schiff von und zur Insel legt an ihren Häfen an. Zölle finanzieren die Akademien
- **Export**: Deutungen. Das klingt abstrakt, ist es aber nicht — das Küstenvolk kartographiert, übersetzt, archiviert. Wer eine Ruine datieren will, braucht einen Küstendeuter. Wer ein Relikt identifizieren will, ebenso
- **Import**: Alles, was die Außenwelt hat und die Insel nicht — Nachrichten, fremde Bücher, seltene Materialien
- **Schwäche**: Produzieren fast keine Nahrung. Abhängig vom Hinterland und vom Höhlenvolk-Netzwerk

**Kultur**:
- **Sozialstruktur**: Akademien als Machtbasis. Jede Hafenstadt hat eine Akademie; die Akademie-Leitung ist de facto die Stadtregierung
- **Geburtsritual**: Neugeborene werden mit der aktuellen Gezeitenposition registriert. Nicht Datum, nicht Uhrzeit — Gezeitenstand. Die See misst die Zeit, nicht die Sonne
- **Totenkultur**: Seebestattung. Die Toten gehören dem Wasser, nicht dem Land
- **Tabu**: Ein Dokument fälschen. Schlimmer noch: ein Dokument vernichten
- **Sprache**: Präzise, leicht archaisch, zitat-schwer. "In der Vierten Chronik steht..." Rhetorische Fragen als Denkwerkzeug. Lange Sätze, Nebensätze, die sich selbst kommentieren

**Beziehung zur Festung**: Distanziert-kooperativ. Das Küstenvolk sieht die Festung als interessantes Studienobjekt — wer hat sie gebaut? warum? welche Schichten? — aber nicht als politische Heimat. Sie zahlen Tribut, aber sie fühlen sich nicht zugehörig. Ihre wahre Heimat ist der Horizont.

**Germanische Mythologie**: Die Nornen, die am Brunnen Urds sitzen und das Schicksal einritzen. Das Küstenvolk liest, was geschrieben wurde — aber wer hat geschrieben? Die Runen-Tradition der Edda: Odin opfert sein Auge für Wissen. Das Küstenvolk opfert Gegenwart für Vergangenheit. Der Preis des Wissens.

---

### III. DAS SIEDLERVOLK — *"Die Welt gehört dem, der sie nimmt."*

**Alternativname**: Die Nehmer, die Gründer, *Festungskinder* (Selbstbezeichnung)

**Rasse**: Menschen. Keine übernatürlichen Merkmale. Vielfältig in Erscheinung (verschiedene Ethnien — die Siedler kamen über Generationen von überall her). Was sie verbindet, ist nicht Blut, sondern Ideologie.

**Weltsicht**: Die Welt ist Ressource. Was da ist, darf genutzt werden — muss genutzt werden. Fortschritt legitimiert sich selbst. Stillstand ist Rückschritt. Die Vergangenheit ist Material, nicht Heiligtum.

**Zone**: Die Festung und das Hinterland (Zonen 3 und 4). Die größte territoriale Ausdehnung aller Fraktionen.

**Architektur-Signatur**:
- **Material**: Stein (gebrochen, nicht gewachsen), Holz, Ziegel. Später: Knochenmetall-Legierungen aus Vulkan-Importen
- **Form**: Blockhaft, rechtwinklig, symmetrisch. Mauern, Türme, Straßenraster. Funktion vor Form. Jedes Gebäude sagt: "Hier ist jemand, der bleibt"
- **Kennzeichen**: Stadtmauern (auch um Dörfer), gepflasterte Straßen, Markthallen, Kasernen. Schilder an jeder Ecke — Straßennamen, Verordnungen, Preislisten. Die Siedler beschriften die Welt
- **Vera-Notiz**: Hochmittelalterlich-clean. Rothenburg ob der Tauber, aber funktional statt pittoresk. Farbpalette: Ocker, Steingrau, Fahnenrot. Sauber — verdächtig sauber

**Wirtschaft**:
- **Funktion**: Landwirtschaft, Handwerk, Verwaltung. Die Siedler produzieren Nahrung, verarbeiten Rohstoffe, organisieren Märkte
- **Stärke**: Selbstversorgung und Bevölkerungsgröße. Es gibt schlicht mehr Siedler als alle anderen zusammen
- **Schwäche**: Brauchen Rohstoffe von außerhalb — Erz vom Vulkan, Wissen von der Küste, Biotech-Produkte vom Innenvolk. Ohne Handelspartner stagnieren sie
- **Machtmittel**: Die Festung. Wer die Festung kontrolliert, kontrolliert den zentralen Markt, die Gerichtsbarkeit und die Straßen des Hinterlandes

**Kultur**:
- **Sozialstruktur**: Gilden und Stadträte. Kein König, kein Adel — aber eine de-facto-Oligarchie der mächtigsten Gildenmeister. Meritokratie als Ideologie, Nepotismus als Praxis
- **Geburtsritual**: Registrierung im Stadtbuch. Name, Datum, Eltern, Gilde-Zugehörigkeit des Vaters/der Mutter. Existenz beginnt mit Bürokratie
- **Totenkultur**: Bestattung in Familiengräbern innerhalb der Stadtmauern. Land ist wertvoll — Grabplätze sind Statussymbole. Wer kein Grab leisten kann, kommt auf den Ascheacker vor der Mauer
- **Tabu**: Vertragsbruch. Die Siedlerkultur basiert auf schriftlichen Vereinbarungen. Mündliche Versprechen zählen nicht
- **Sprache**: Direkt, sachlich, bürokratisch. Dekrete statt Geschichten. "Laut Stadtordnung §14..." Nicht humorlos, aber ihr Humor ist trocken und auf Effizienz getrimmt. Keine Metaphern — Metaphern verschwenden Zeit

**Beziehung zur Festung**: DIE Festung IST das Siedlervolk — oder das behaupten sie. Sie haben die Festung nicht gebaut (niemand weiß, wer das tat), aber sie haben sie besetzt, ausgebaut und zum Zentrum der Insel gemacht. Die Festung legitimiert ihren Anspruch auf Führung.

**Germanische Mythologie**: Die Asen — Götter der Ordnung, des Gesetzes, der Zivilisation. Thor mit seinem Hammer ist ein Baumeister so viel wie ein Krieger. Asgards Mauern, von einem Riesen gebaut — die Siedler bauen auf Fundamenten, die sie nicht verstehen, und nennen sie trotzdem ihr Eigen. Odin als Allvater: der Anspruch, über alle zu herrschen, weil man sich als Erster hingesetzt hat.

---

### IV. DAS INNENVOLK — *"Der Körper ist die letzte Grenze."*

**Alternativname**: Die Destillateure, die Körperkundigen, *Nervengeher* (Selbstbezeichnung)

> **Design-Entscheidung (Emre + Nami, Tag 3)**:
> Emres "Destillateure" und Namis "Innenvolk" sind **dieselbe Fraktion**, betrachtet aus zwei Winkeln. Emre beschreibt die ökologische Nische (Biotech-Produktion, Substanzen, Gewächshäuser), Nami die philosophische Position (der Körper als Forschungsgegenstand, Nervensystem-Leveling als deren Technologie). Das Ergebnis: **Innenvolk** als Fraktionsname, **Destillateure** als Berufsbezeichnung innerhalb der Fraktion — so wie "Schmiede" kein Volksname ist, aber jeden beschreibt der in einer Esse arbeitet.

**Rasse**: Rassenübergreifend. Jede Rasse hat Innenvolk-Mitglieder — das ist keine biologische Gruppe, sondern eine ideologische. Was sie verbindet, ist die Praxis: Selbstexperiment.

**Weltsicht**: Die Wahrheit liegt nicht in der Welt — sie liegt im Körper. Die Insel, die Ruinen, die Relikte — alles Äußerlichkeiten. Was zählt, ist das Nervensystem, das Blut, die Chemie. Der Körper erinnert sich an Dinge, die der Geist vergessen hat. Wer sich selbst erforscht, erforscht die Grundlagen der Welt.

**Zone**: Kein festes Territorium — ein **loses Netzwerk**, verteilt über alle Zonen. Schwerpunkte: Vulkanland (Rohstoffe für Destillation), Unterwelt (verborgene Labore), Festung (Absatzmärkte). Überall dort, wo man ungestört arbeiten kann.

**Architektur-Signatur**:
- **Material**: Knochen, Haut (tierisch, gegerbt), Chitin, Keratin, Biolumineszenz-Pilze als Lichtquelle. Organische Materialien, die atmen und riechen
- **Form**: Gewächshäuser aus Rippenbögen. Destillationsapparate, die aussehen wie Organe. Labore, die aussehen wie das Innere eines Tieres. Nichts ist rechtwinklig; alles ist feucht
- **Kennzeichen**: Geruch. Man riecht ein Innenvolk-Labor bevor man es sieht — Schwefel, Kräuter, etwas Süßlich-Fauliges. Schläuche statt Rohre. Membranen statt Türen
- **Vera-Notiz**: Giger trifft mittelalterliche Apotheke. Farbpalette: Bernstein, Fleischrot, Knochengelb, Violett (Biolumineszenz). Schön auf eine verstörende Weise. Fashion: High Fashion Mittelalter — Innenvolk-Mitglieder kleiden sich exzessiv, weil Kleidung auch Experiment ist (Haut-kontakt-Stoffe, imprägnierte Gewebe)

**Wirtschaft**:
- **Funktion**: Produktion von Biotech-Substanzen. Alles, was der Körper braucht oder fürchtet, stellt das Innenvolk her
- **Produkte**:
  - **Verstärker** (*Sporen*): Temporäre Leistungssteigerung — Ausdauer, Reflexe, Nachtsicht. Legaler Markt an der Festung
  - **Gifte** (*Tinkturen*): Waffen, Fallen, Assassinen-Werkzeug. Illegaler Markt über das Höhlenvolk
  - **Drogen** (*Tiefstoffe*): Bewusstseinserweiternde Substanzen. Manche ermöglichen Zugang zu Nervensystem-Schichten, die sonst verschlossen sind. Suchtgefahr. Rechtliche Grauzone
  - **Heilmittel** (*Balsame*): Medizin. Die beste auf der Insel. Teuer
- **Monopol**: Niemand sonst versteht die biochemischen Prozesse. Rezepturen werden mündlich weitergegeben — nichts Schriftliches (zum Ärger des Küstenvolks)
- **Abhängigkeit**: Brauchen Rohstoffe aus dem Vulkanland (Schwefel, Mineralien, thermophile Pilze) und aus der Unterwelt (seltene Pilzarten, Höhlenwasser)

**Kultur**:
- **Sozialstruktur**: Meister-Schüler-Beziehungen, keine formale Hierarchie. Ein Destillateur wird nicht gewählt oder ernannt — er wird anerkannt, wenn seine Substanzen wirken
- **Initiation**: Selbstversuch. Wer Innenvolk werden will, muss eine selbst hergestellte Substanz an sich selbst testen. Manche bestehen. Manche nicht
- **Totenkultur**: Dissektion. Die Toten werden seziert, ihre Organe studiert, ihre Chemie analysiert. Der Tod ist die letzte Datenerhebung. Für Außenstehende barbarisch — für das Innenvolk der höchste Respekt
- **Tabu**: Eine Substanz verkaufen, deren Wirkung man nicht am eigenen Körper getestet hat
- **Sprache**: Klinisch, fasziniert, leicht verstörend. Beschreiben Schmerz als Daten. Reden über Gift wie Sommeliers über Wein. "Eine exquisite Dosis — spürst du, wie dein Sehnerv reagiert?" Fachvokabular, das anderen kryptisch erscheint

**Beziehung zur Festung**: Parasitär-symbiotisch. Die Festung braucht Heilmittel und Verstärker (die Stadtwache kauft in Massen). Das Innenvolk braucht Absatzmärkte und Schutz vor Verfolgung. Man duldet sich. Man vertraut sich nicht. Die Innenvolk-Labore innerhalb der Festungsmauern sind offiziell "Apotheken." Alle wissen, dass das nicht stimmt.

**Germanische Mythologie**: Die Völva — die Seherin, die durch Trance und Substanzen Zugang zu verborgenem Wissen findet. Odins Selbstopfer am Weltenbaum: neun Tage hängend, durchbohrt, zwischen Leben und Tod — um die Runen zu empfangen. Das Innenvolk hängt sich nicht an Bäume, aber das Prinzip ist dasselbe: Wissen durch Selbstverletzung. Auch Loki, der Gestaltwandler, der seinen eigenen Körper verändert. Der Körper als Werkzeug, nicht als Tempel.

---

### V. DIE ZERBROCHENEN — *"Ich bin, was übrig bleibt."*

**Alternativname**: Keine. Sie haben keinen Kollektivnamen, weil sie kein Kollektiv sind.

**Rasse**: Alle. Die Zerbrochenen sind keine Ethnie, keine Kultur, keine Organisation. Sie sind ein **Zustand**.

**Weltsicht**: Es gibt keine richtige Weltsicht. Oder: es gab eine, aber sie ist verloren. Die Zerbrochenen stehen zwischen allen Positionen — Exilierte, Überläufer, Entwurzelte, Fremde.

**Zone**: Überall und nirgends. Auf den Straßen, in verlassenen Häusern, an den Rändern jeder Siedlung. Am sichtbarsten: in der Festung, wo die Entwurzelten sich sammeln.

**Architektur-Signatur**: Keine eigene. Zerbrochene besetzen, was andere verlassen haben. Improvisierte Lager, umfunktionierte Ruinen, gestapelte Kisten als Wände. Die Ästhetik der Notlösung.

**Wirtschaft**: Gelegenheitsarbeit, Betteln, Kleinkriminalität. Manche Zerbrochene sind hochqualifiziert (ehemalige Akademiker des Küstenvolks, ehemalige Destillateure) — aber ohne Netzwerk ist Qualifikation wertlos.

**Kultur**:
- **Sozialstruktur**: Keine. Temporäre Zweckbündnisse, die zerbrechen, sobald der Zweck erfüllt ist
- **Sprache**: Fragmentarisch, persönlich, ohne Formel. Keine Sprichwörter, keine Zitate, keine Rhetorik. "Ich war mal..." und "Ich weiß nicht mehr..."
- **Companions**: Kommen überproportional aus dieser Gruppe. Die interessantesten Geschichten der Insel gehören denen, die alles verloren haben

**Beziehung zur Festung**: Die Festung toleriert Zerbrochene als billige Arbeitskraft und ignoriert sie als politische Größe. Es gibt ein Armenviertel im Außenring — *die Scherben* — das offiziell nicht existiert.

**Spieler-Relevanz**: **Der Spielercharakter startet als Zerbrochener.** Ein Fremder, der per Schiff auf die Insel kommt — ohne Zugehörigkeit, ohne Geschichte, ohne Weltsicht. Der gesamte Spielverlauf ist der Prozess, von Zerbrochen zu Zugehörig zu werden. Oder eben nicht. Manche Spieler werden bewusst zerbrochen bleiben.

**Germanische Mythologie**: Die Riesen nach Ragnarök. Die Jötunn, die zwischen den Welten stehen. Aber auch: der Wanderer. Odin selbst, in Verkleidung, der sich unter die Sterblichen mischt. Der Spieler als Unbekannter, der mehr sein könnte als er scheint — oder auch nicht. Die Edda ist voller Figuren, die erst herausfinden müssen, wer sie sind.

---

## 3.3 Die Festung

### Was sie ist

Die Festung ist der **zentrale Hub** der Spielwelt — der Ort, an den der Spieler immer zurückkehrt. Geographisch liegt sie auf einem Plateau leicht südlich der Inselmitte, mit Sichtlinien zu allen Zonen. Sie ist groß genug für eine Stadt, alt genug für Geheimnisse und umkämpft genug für Politik.

### Wer hat sie gebaut?

Niemand weiß es. Das ist kein Plothole — das ist der Plot.

Die Festung ist älter als jede lebende Erinnerung, älter als das Küstenvolk-Archiv, älter als die tiefsten Tunnelmarkierungen des Höhlenvolks. Die Bauweise passt zu keiner bekannten Kultur auf der Insel:
- Zu groß für die Siedler (die sie nur besetzt und ausgebaut haben)
- Zu geometrisch für das Höhlenvolk (das organisch baut)
- Zu alt für das Küstenvolk (das erst später kam)
- Zu materiell für das Innenvolk (das kein Interesse an Stein hat)

Die Festung ist aus einem Material gebaut, das nirgendwo sonst auf der Insel vorkommt — ein dunkler, fast schwarzer Stein, glatt wie Obsidian, aber deutlich härter. Das Küstenvolk nennt ihn *Grundstein*. Das Innenvolk hat ihn analysiert und Spuren organischer Verbindungen gefunden. Niemand spricht gerne darüber, was das bedeuten könnte.

### Struktur

```
Äußerer Ring — Märkte, Handwerkerviertel, Scherben (Armenviertel)
│
├── Mittlerer Ring — Gilden, Kasernen, Akademie-Außenstelle, Apotheken (Innenvolk-Labore)
│
├── Innerer Ring — Ratsgebäude, Archive, Wohnviertel der Gildenmeister
│
└── Kern — Verschlossen. Niemand darf hinein. Bewacht, aber nicht von der Stadtwache.
    Was ist drin? Wer bewacht es? Das ist eine der zentralen Fragen der Hauptquest.
```

### Politische Struktur

Die Festung wird regiert durch den **Rat der Gilden** — ein Gremium aus den Meistern der wichtigsten Handwerks- und Handelsgilden. De facto Siedlervolk-dominiert, aber mit formalen Sitzen für:
- Einen Küstenvolk-Gesandten (Beobachterstatus, kein Stimmrecht)
- Einen Höhlenvolk-Marktmeister (Stimmrecht in Handelsfragen, sonst nicht)
- Keinen Innenvolk-Vertreter (offiziell existiert das Innenvolk innerhalb der Festungsmauern nicht)
- Keine Zerbrochenen-Vertretung (selbstverständlich)

### Funktion im Spiel

| Gameplay-Funktion | Umsetzung |
|---|---|
| Questgeber-Hub | Rat der Gilden, Marktplatz, Akademie-Außenstelle, Scherben |
| Handels-Hub | Zentraler Markt (Äußerer Ring) + Schwarzmarkt (Unterwelt-Zugang) |
| Crafting-Hub | Handwerkerviertel (Schmieden, Gerbereien, Destillations-"Apotheken") |
| Narrativer Hub | Kern-Mysterium, Gildenrat-Politik, Fraktions-Konflikte |
| Ruhezone | Gasthäuser, eigene Unterkunft (freischaltbar), Akademie-Bibliothek |

---

## 3.4 Biotech-Ökologie

### Prinzip

In RELICS gibt es keinen Steampunk, keine Dampfmaschinen, keine Zahnräder. Die Technologie der Insel ist **biologisch** — gewachsen, destilliert, fermentiert, extrahiert. Das ist kein Flavor; das ist ein Designprinzip, das jede Textur, jedes Item, jede Werkbank betrifft.

### Woher kommen die Substanzen?

Die Insel hat eine einzigartige biochemische Grundlage. Der Vulkan im Nordosten produziert nicht nur Hitze und Mineralien, sondern auch **Schwellstellen** — Orte, an denen organisches Material aus der Tiefe an die Oberfläche tritt. Dieses Material ist alt. Sehr alt. Was genau es ist, darüber streiten sich die Fraktionen (natürlich).

**Die Produktionskette**:

```
Schwellstellen (Vulkan, tief)
    │
    ▼
Rohmaterial — Mineralien, thermophile Pilze, Schwellflüssigkeit
    │
    ├──→ Vulkansiedlungen: Erz-Verhüttung, Obsidian-Werkzeuge
    │
    ├──→ Höhlenvolk-Distribution: Transport in alle Zonen
    │
    ▼
Innenvolk-Labore (verteilt)
    │
    ├──→ VERSTÄRKER (Sporen): Temporäre Buffs
    │    Beispiel: "Wolfslunge" — +30% Ausdauer, 4h, leichte Übelkeit
    │
    ├──→ GIFTE (Tinkturen): Waffen-Coating, Fallen
    │    Beispiel: "Stille Zunge" — Paralyse, 30 Sek., beschaffbar beim Höhlenvolk
    │
    ├──→ DROGEN (Tiefstoffe): Bewusstseinsveränderung, Nervensystem-Zugang
    │    Beispiel: "Tiefblick" — zeigt das eigene Nervensystem (Leveling-UI!), 1h, Suchtrisiko
    │
    └──→ HEILMITTEL (Balsame): Wundheilung, Entgiftung, Regeneration
         Beispiel: "Fleischwort" — heilt 50% HP über 30 Sek., teuer, schmeckt bitter
```

### Nervensystem-Leveling und Biotech

Das **Nervensystem-Leveling** (siehe GDD Kapitel 5) ist nicht nur eine UI-Mechanik — es ist im Worldbuilding verankert:

- Das Innenvolk hat entdeckt, dass der Körper "Schichten" hat, die normalerweise unzugänglich sind
- Durch gezielte Substanzen (Tiefstoffe) können diese Schichten sichtbar und trainierbar gemacht werden
- Was der Spieler als **Leveling-UI** sieht (halbtransparente Nervensystem-Sicht, drei Bahnen: Kardio, Muskel-Skelett, Lymph), ist IN DER SPIELWELT eine Innenvolk-Technik
- NPCs anderer Fraktionen reagieren unterschiedlich darauf:
  - Siedlervolk: "Nützlich. Was kostet es?"
  - Küstenvolk: "Faszinierend. Was bedeutet es?"
  - Höhlenvolk: "Tiefstoffe? Kann ich dir besorgen. Hat seinen Preis."
  - Zerbrochene: "Ich habe das mal gemacht. Ich kann mich nicht erinnern warum."

### Sucht und Risiko

Biotech-Substanzen sind nicht kostenlos. Das Lymphsystem im Leveling-UI trackt die **Belastung**:

| Belastungsstufe | Lymph-Zustand | Effekt |
|---|---|---|
| 0 — Sauber | Klar, ruhig | Keine Debuffs |
| 1 — Angereichert | Leicht verfärbt | +5% Substanz-Wirkung, -5% Regeneration |
| 2 — Belastet | Sichtbare Schwellung | Abhängigkeit beginnt: ohne Nachschub Debuffs |
| 3 — Vergiftet | Dunkel, pulsierend | Permanente Stat-Reduktion ohne Innenvolk-Behandlung |
| 4 — Zerbrochen | Schwarz, rissig | Fraktionswechsel erzwungen: Du wirst Zerbrochener |

**Designprinzip**: Biotech ist mächtig, aber es hat Konsequenzen. Das ist kein Moralsystem — es ist Biologie. Der Körper erinnert sich an alles, was man ihm antut.

---

## 3.5 Germanische Mythologie — Wie sie in der Welt lebt

### Designprinzip

Germanische Mythologie in RELICS ist **kein Setting-Dressing**. Die Götter existieren nicht — oder: es gibt keine Beweise dafür. Was existiert, sind die Geschichten, die die Inselbewohner sich erzählen. Mythen sind Erklärungsversuche für Dinge, die biologisch oder geologisch erklärbar WÄREN — wenn jemand die richtige Erklärung hätte. Niemand hat sie.

Das ist **Low Fantasy, germanisch, dekonstruiert**: Die Mythologie wird ernst genommen als kulturelle Kraft, ohne dass sie buchstäblich wahr sein muss.

### Mythologische Schichten in der Spielwelt

**Schicht 1 — Ymir und die Schöpfung**
- Die Insel selbst wird von manchen (besonders dem Küstenvolk) als Fragment eines Urwesens gedeutet — eines Riesen, aus dessen Körper die Welt entstand
- Die Schwellstellen? "Ymirs Adern." Die Vulkanaktivität? "Ymirs letzter Atemzug." Das Grundstein-Material der Festung? "Ymirs Knochen."
- Das Siedlervolk nennt das Aberglaube. Das Innenvolk findet es interessant, weil die biochemische Zusammensetzung der Schwellstellen tatsächlich organischen Ursprungs zu sein scheint
- **Design**: Nie aufgelöst. Der Spieler findet Hinweise in beide Richtungen. Die Wahrheit bleibt offen

**Schicht 2 — Die Drei Nornen und das Schicksal**
- Das Küstenvolk verehrt drei Schwestern-Figuren — die Lesenden, die Spinnenden, die Schneidenden — die angeblich in der ältesten Ruine der Insel leben. Oder lebten. Oder nie existiert haben
- Spielrelevant: Drei Schlüssel-NPCs an der Küste, die den Spieler in die Lore einführen. Sie widersprechen sich. Absichtlich
- Die Nornen als Metapher für: Die Vergangenheit (was gelesen wird), die Gegenwart (was gesponnen wird) und die Zukunft (was abgeschnitten wird)

**Schicht 3 — Odin als Wanderer**
- Der Spielercharakter als Odin-Echo: Ein Fremder, der auf die Insel kommt, alles beobachtet, Wissen sammelt — und einen Preis dafür zahlt
- Parallele zum Selbstopfer: Das Nervensystem-Leveling als Odins Aufhängung an Yggdrasil — Wissen durch Selbstverletzung
- Der einäugige Wanderer als wiederkehrendes Motiv in NPC-Dialogen: "Ein Auge für die Wahrheit. Was gibst du?"

**Schicht 4 — Ragnarök als Ticking Clock**
- Ragnarök ist kein kosmisches Ereignis, sondern eine **biologische Eskalation**: Die Schwellstellen werden aktiver. Der Vulkan unruhiger. Etwas unter der Insel wacht auf — oder stirbt endgültig
- Kein Weltuntergang durch Götterkrieg, sondern durch tektonisch-biochemische Kettenreaktion
- Der Spieler erlebt die Anzeichen im Spielverlauf: Erst subtil (NPCs reden über seltsame Erdbeben), dann deutlich (Schwellstellen brechen in besiedelten Gebieten auf), dann drängend (die Festung selbst zeigt Risse im Grundstein)
- **Die zentrale Frage der Hauptquest**: Kann Ragnarök aufgehalten werden? Soll es? Was, wenn das Ende der Insel auch ein Anfang ist?

**Schicht 5 — Loki und die Grenzüberschreitung**
- Loki ist kein Charakter, sondern ein **Prinzip**: Die Grenzüberschreitung, die Verwandlung, der Betrug, der auch Wahrheit ist
- Das Innenvolk verkörpert Loki am stärksten — ihre Selbstexperimente sind Grenzüberschreitungen. Aber auch das Höhlenvolk (Trickster-Handel) und die Zerbrochenen (unfreiwillige Verwandlung)
- Spieler, die sich dem Innenvolk nähern, begegnen Loki-Motiven: Veränderung, Verlust der Form, die Frage ob Identität an den Körper gebunden ist

### Mythos vs. Realität — Tabelle für Level Designer

| Mythologisches Motiv | In-World-Deutung (gläubig) | In-World-Deutung (rational) | Design-Einsatz |
|---|---|---|---|
| Ymir | Insel ist Riesenkörper | Geologische Formation | Environmental Storytelling, Schwellstellen-Design |
| Nornen | Drei Schicksalsfrauen in der Ruine | Drei Akademikerinnen, die Geschichte kontrollieren | Quest-NPCs an der Küste |
| Odin | Der einäugige Wanderer kehrt zurück | Fremder mit zu vielen Fragen | Spielercharakter-Echo |
| Ragnarök | Die Welt endet im Feuer | Vulkanische Aktivität eskaliert | Hauptquest Ticking Clock |
| Loki | Gott der Verwandlung lebt in uns | Biotech verändert den Körper | Innenvolk-Quests, Nervensystem-Leveling |
| Midgardschlange | Etwas lebt unter der Insel | Tektonische Verwerfungen | Kern-Mysterium der Festung |

---

## 3.6 Fraktionsbeziehungen — Übersicht

```
               KÜSTENVOLK
              /    |     \
       Respekt  Misstrauen  Neugier
        /          |          \
HÖHLENVOLK ──Handel── SIEDLERVOLK
        \          |          /
      Versorgung  Verbot   Abhängigkeit
        \          |          /
              INNENVOLK
                 |
            Verachtung/Mitleid
                 |
            ZERBROCHENE
```

| Fraktion A | Fraktion B | Beziehung | Kern des Konflikts |
|---|---|---|---|
| Höhlenvolk | Siedlervolk | Zweckbündnis | Kontrolle vs. Freiheit. Siedler wollen regulieren, Höhlenvolk will handeln |
| Höhlenvolk | Küstenvolk | Respekt | Wissen gegen Waren. Funktioniert meistens, solange keiner betrügt |
| Höhlenvolk | Innenvolk | Lieferkette | Das Höhlenvolk transportiert, was das Innenvolk braucht. Beide profitieren. Beide misstrauen |
| Küstenvolk | Siedlervolk | Spannung | Vergangenheit vs. Fortschritt. Küstenvolk will konservieren, Siedler wollen nutzen |
| Küstenvolk | Innenvolk | Faszination | Beide forschen — einer in Büchern, der andere in Körpern. Begegnung auf Augenhöhe, aber fundamental verschiedene Methoden |
| Siedlervolk | Innenvolk | Heuchelei | Offiziell verboten, inoffiziell Hauptkunde. Die Festung braucht Balsame und Sporen, aber verbietet Tiefstoffe |
| Alle | Zerbrochene | Ignoranz | Zerbrochene existieren nicht. Offiziell |

---

## Anhang: Vertical-Slice-Reduktion

Für den Vertical Slice (Hauptquest + 2 Nebenquests in einer Region) wird **die Festung und ihr unmittelbares Umland** als Startregion vorgeschlagen:

**Aktive Fraktionen im Slice**: Siedlervolk (dominant), Höhlenvolk (Händler-Karawane am Markt), Küstenvolk (Akademie-Außenstelle)

**Angedeutete Fraktionen**: Innenvolk (eine "Apotheke" im Mittleren Ring, ein NPC, ein Hinweis auf die Unterwelt), Zerbrochene (die Scherben als begehbares Armenviertel)

**Hauptquest-Hook**: Der Spieler kommt als Fremder zur Festung. Der Kern ist verschlossen. Jemand will ihn öffnen. Jemand will ihn versiegelt lassen. Der Spieler muss entscheiden, wem er vertraut — und was er dafür aufgibt.

---

*Dieses Kapitel wurde im Besprechungsraum erarbeitet, Tag 3 Vormittag, mit drei Tassen Tee (Emre) und zwei Flat Whites (Nami). Der Kompromiss Innenvolk/Destillateure wurde um 10:47 erreicht, nach 23 Minuten produktivem Streit. Die Festungs-Frage ("Wer hat gebaut?") ist absichtlich offen — wir haben beschlossen, dass sie es bleiben soll.*

*— E. Yilmaz & N. Okafor*

\newpage

---
agent: darius
day: 3
task: "GDD Kapitel 04 — Gameplay-Systeme"
memories_referenced: [darius-008, darius-012, darius-015, darius-019, darius-023, nami-024, cd-day3-morning]
feedback_received: [cd-day3-morning]
status: draft
---

# Kapitel 04 — Gameplay-Systeme

> *"Jedes System in diesem Spiel muss drei Tests bestehen: 1. Ist es spielbar? 2. Zahlt es auf die Kernfrage ein? 3. Kann ein Spieler es in 10 Sekunden verstehen und in 100 Stunden meistern? Wenn nicht — raus damit."*
> *— D. Engel, Game Director, Tag 3*

---

## 4.1 Kamera-System

### Spieler-Fantasie
*"Ich SEHE die Welt wie ICH will — aus meinen Augen oder über meiner Schulter. Das Spiel zwingt mir keine Perspektive auf."*

### Konzept

Nahtloses Umschalten zwischen First-Person (FP) und Third-Person (TP), Skyrim-Style. Kein Ladescreen, kein Cut, kein Übergang. Der Spieler drückt eine Taste und die Kamera zoomt stufenlos zwischen den Perspektiven.

### Spezifikation

**First-Person (FP)**:
- Standard-Exploration in engen Räumen, Innenräumen, Titanenadern
- Immersiver Modus: Wetterbedingungen sichtbar auf dem HUD (Asche auf dem Visor, Regen auf der Sichtlinie, Blut nach Kampf)
- Nahkampf-Feeling: Schwertklinge sichtbar, Schildarm links, physisches Gewicht spürbar
- Bogen/Armbrust: Iron-Sights-ähnliches Zielen, keine Fadenkreuz-Unterstützung (optional in Einstellungen)

**Third-Person (TP)**:
- Standard für Outdoor-Exploration, Klettern, Übersichtssituationen
- Stufenloser Zoom: nah (über der Schulter, ähnlich Resident Evil 4) bis weit (ähnlich Witcher 3 Reiten)
- Charakter-Modell vollständig sichtbar: Rüstung, Waffen, Statuseffekte visuell erkennbar
- Kamera-Kollision: Intelligentes System, das in engen Räumen automatisch näher zoomt statt durch Wände zu clippen

**Universalregel: Jedes System muss in BEIDEN Perspektiven funktionieren.**

Das ist kein Nice-to-Have. Das ist eine Architekturentscheidung. Wenn ein Feature nur in FP funktioniert (z.B. ein UI-Element, das den Bildschirm füllt), muss es ein TP-Äquivalent haben. Wenn es keins gibt, wird das Feature umgestaltet.

| System | FP-Lösung | TP-Lösung |
|--------|-----------|-----------|
| Nervensystem-Leveling | Halbtransparente Körper-Overlay auf Screen | Kamera zoomt auf Charakter, Körper wird transparent |
| Dialog | Gesicht des NPC im Fokus, Blickkontakt | Over-the-Shoulder, Kamera zwischen Spieler und NPC |
| Kampf | Waffe/Schild sichtbar, physisches Gefühl | Vollkörper-Animation, Footwork sichtbar |
| Klettern | Hände greifen, visuelles Feedback, Höhenangst | Charakter-Silhouette gegen Umgebung, Routenplanung |
| Substanz-Effekte | Visuelle Verzerrung, Farbverschiebung | Charakter-Animation (Taumeln, Zittern), Partikeleffekte |

**Gameplay-Beispiel**: Der Spieler erkundet eine Titanenader in FP — enge Gänge, Klaustrophobie, Fackelschein auf Knochenmetall-Wänden. Er findet einen Ausgang und tritt ins Freie. Die Kamera zoomt nahtlos auf TP, und der Spieler sieht zum ersten Mal den Knochenturm in voller Größe über sich. Dieser Perspektivwechsel IST das Storymoment.

---

## 4.2 Combat-System

### Spieler-Fantasie
*"Jeder Kampf fühlt sich an, als könnte ich sterben. Jeder Sieg fühlt sich verdient an. Mein Schwert hat Gewicht, mein Schild hat Zweck, und mein Gegner hat einen Plan."*

### Konzept

Real-Time Action Combat. Kein Turn-based, kein Hack-and-Slash. Gewichtig, taktisch, positionsbasiert. Näher an Dark Souls als an Diablo, aber zugänglicher als Sekiro. Jeder Schwerthieb kostet Ausdauer, jeder Block hat ein Timing-Fenster, jeder Gegner hat erkennbare Muster.

### Waffen-Klassen

**Nahkampf**:

| Waffe | Geschwindigkeit | Schaden | Reichweite | Spieler-Fantasie |
|-------|----------------|---------|------------|------------------|
| Einhand-Schwert + Schild | Mittel | Mittel | Kurz | "Ich bin vorbereitet. Ich blocke, ich kontre, ich kontrolliere." |
| Zweihand-Schwert | Langsam | Hoch | Mittel | "Jeder Hieb zählt. Ich committe und zerstöre." |
| Dolch / Kurzschwert | Schnell | Niedrig | Sehr kurz | "Ich bin schneller als du denkst. Drei Schnitte, bevor du einen Hieb landest." |
| Streitaxt / Kriegshammer | Sehr langsam | Sehr hoch | Kurz | "Rüstung bedeutet nichts. Ich zertrümmere, was im Weg ist." |
| Speer / Hellebarde | Mittel | Mittel-Hoch | Lang | "Du kommst nicht nah genug heran. Die Distanz gehört mir." |

**Fernkampf**:

| Waffe | Feuerrate | Schaden | Vorbereitung | Spieler-Fantasie |
|-------|-----------|---------|--------------|------------------|
| Langbogen | Langsam | Hoch | Spannen + Zielen | "Ein Schuss, ein Treffer. Geduld ist meine Waffe." |
| Kurzbogen | Mittel | Mittel | Schnelles Spannen | "Mobilität + Fernkampf. Ich schieße im Laufen." |
| Armbrust | Sehr langsam | Sehr hoch | Laden (mechanisch) | "Panzerbrechend. Ein Schuss durch die Rüstung." |
| Wurfmesser / Wurfaxt | Schnell | Niedrig | Minimal | "Schneller Opener. Dann wechsle ich zu Nahkampf." |

**Schilde** (eigene Kategorie, kein Anhängsel):

Schilde sind keine passive Ausrüstung. Ein Schild ist eine WAFFE. Schildstoß, Schildschlag, aktives Blocken mit Timing-Fenster (Parry), passives Blocken (Ausdauer-Drain). Unterschied zwischen Rundschilden (mobiler, leichter), Turmschild (stationär, maximaler Schutz), Buckler (Parry-fokussiert, fast kein passiver Block).

### Kampf-Prinzipien

**1. Gewicht**
Jede Aktion hat Weight. Ein Zweihand-Schwert schwingt nicht wie ein Stab — es hat Momentum, Recovery-Frames, Commitment. Der Spieler kann nicht abbrechen mid-Swing. Das ist kein Bug, das ist Taktik. Wer committed, muss den Zeitpunkt richtig wählen.

**2. Ausdauer als Universalwährung**
Jede Aktion im Kampf kostet Ausdauer: Angriff, Block, Dodge, Sprint. Ausdauer regeneriert passiv, aber langsam im Kampf. Das zwingt zu Pausen, zu taktischem Rückzug, zu bewusster Ressourcenverwaltung. Kein Buttonmashing. Wer alles auf einmal tut, steht mit leerer Ausdauer da und stirbt.

**3. Positionierung**
Rückenangriffe machen mehr Schaden. Flanken umgehen Schilde. Höhenvorteil gibt Reichweitenbonus. Engpässe begrenzen Gegneranzahl. Der Spieler, der den Raum liest, hat einen Vorteil über den, der nur auf den Gegner schaut.

**4. KI mit Absicht**
Gegner sind keine HP-Pools mit Angriffsanimation. Jeder Gegnertyp hat eine erkennbare Kampfdoktrin:
- **Banditen**: Aggressiv, aber feige. Greifen in Gruppen an, fliehen bei Überzahl-Verlust.
- **Siedlervolk-Soldaten**: Diszipliniert, Formation, Schildwall. Einzeln schwächer, in Gruppen tödlich.
- **Höhlenvolk-Krieger**: Ausweich-fokussiert, Gift an Klingen, Hit-and-Run. Kämpfen nie fair.
- **Innenvolk-Wächter**: Chemisch verstärkt. Schneller und stärker als normal, aber unberechenbar. Manche brechen mid-Kampf zusammen, weil die Substanzen nachlassen.
- **Wildtiere**: Instinktbasiert. Territorial, nicht böswillig. Ein Wolf greift an, wenn er hungrig ist — nicht, weil er auf einer Spawn-Liste steht.

**Gameplay-Beispiel**: Der Spieler trifft auf drei Banditen an einer Brücke. In FP sieht er: zwei mit Schwertern, einer mit Bogen hinten. Option A — Frontalkampf: Schwert+Schild, den Bogenschützen ignorieren (riskant, aber schnell). Option B — Schleichen: Unter der Brücke klettern, den Bogenschützen zuerst ausschalten. Option C — Verhandeln: Der Spieler kennt ihren Anführer (vorherige Quest). Einschüchtern oder bestechen. Option D — Substanz: Ein Leistungsverstärker des Innenvolks. 30 Sekunden Übermenschlichkeit. Danach: Zittern, Sichtfeldeinschränkung, Ausdauer-Crash.

---

## 4.3 Leveling — Das Nervensystem

### Spieler-Fantasie
*"Ich werde nicht stärker, weil ich Punkte verteile. Ich werde stärker, weil mein KÖRPER sich verändert. Ich SEHE mein Wachstum — in mir."*

### Konzept

Beim Leveln wechselt die Ansicht in eine halbtransparente Körpervisualisierung. Der Spielercharakter wird durchsichtig, und der Spieler sieht sein eigenes Nervensystem, Kreislauf, Skelett — ein lebendiges Anatomie-Modell, das sich mit jedem Levelaufstieg verändert und wächst.

Das ist keine abstrakte Skill-Tree-Metapher. Das ist diegetisch. Das Innenvolk hat diese Technologie entwickelt — die Erkenntnis, dass der sterbliche Körper Titanenspuren in seinen Zellen trägt. Wer sich verbessert, aktiviert buchstäblich schlafende biologische Kapazitäten.

### Die Systeme

#### 4.3.1 Herz-Kreislauf / Atmungssystem

**Visuell**: Rotes Netzwerk. Herz pulsiert. Lungenflügel atmen. Arterien und Venen durchziehen den Körper. Je stärker das System, desto sichtbarer und leuchtender die Bahnen.

**Was es regelt**:
- **Ausdauer-Pool**: Maximale Ausdauer und Regenerationsrate
- **Sprint-Dauer**: Wie lange der Spieler sprinten kann, bevor er keucht
- **Unterwasser-Atmen**: Tauchzeit in überfluteten Titanenadern und Ascheseen
- **Erholung nach Kampf**: Wie schnell die Ausdauer außerhalb des Kampfes zurückkehrt
- **Höhenresistenz**: Auf Knochentürmen wird die Luft dünn. Starkes Kreislaufsystem = weniger Debuff in der Höhe

**Steigerung durch**: Laufen, Klettern, Schwimmen, ausdauerbasierte Aktionen. Das System wächst durch Benutzung — nicht durch Menüklicks.

**Gameplay-Beispiel**: Der Spieler entdeckt eine überflutete Titanenader, die zu einem Innenvolk-Labor führt. Mit Kreislaufsystem Stufe 2 schafft er 40 Sekunden unter Wasser — nicht genug. Er kann das System trainieren (schwimmen, tauchen, Ausdauer-Aktionen über Tage), oder eine Atemsalbe vom Innenvolk kaufen (temporärer Boost, aber: Lymphsystem-Belastung). Oder er findet einen anderen Weg rein.

#### 4.3.2 Muskel-Skelett-System

**Visuell**: Weißes Skelett, rot-braune Muskelstränge. Je stärker das System, desto dichter und definierter die Muskelfasern. Knochen werden massiver. Bei maximaler Stufe sieht der Charakter unter der Haut aus wie eine da-Vinci-Anatomiestudie.

**Was es regelt**:
- **Tragkraft**: Inventarlimit. Nicht als Zahl — als physisches Gewicht. Zu viel Last = langsamere Bewegung, kein Sprint, lauter (Stealth unmöglich)
- **Nahkampfschaden**: Basis-Schadensmultiplikator für alle Nahkampfwaffen
- **Klettern**: Reichweite und Geschwindigkeit beim Klettern. Schwaches System = nur niedrige Wände. Starkes System = Knochentürme
- **Waffenvoraussetzungen**: Schwere Waffen (Zweihand-Schwert, Kriegshammer) erfordern Mindest-Stufen im Muskel-Skelett-System
- **Physische Einschüchterung**: NPCs reagieren auf die physische Präsenz des Spielers. Ein Charakter mit maximalem Muskel-Skelett-System wird ANDERS behandelt als ein drahtiger Dolchkämpfer. Das ist kein Stat-Check — das ist sichtbar.

**Steigerung durch**: Nahkampf, schweres Tragen, Klettern, körperliche Arbeit (ja, dem Schmied beim Hämmern helfen trainiert dein Muskel-Skelett-System).

**Gameplay-Beispiel**: Ein Siedlervolk-Soldat versperrt den Weg. Der Spieler hat Muskel-Skelett Stufe 5, trägt eine Zweihand-Axt und sieht aus wie jemand, der Probleme verursacht. Der Soldat schluckt und tritt beiseite — kein Kampf nötig. Derselbe Spieler mit Stufe 1 und Dolch? "Verschwinde, Fremder." Gleiche Situation, anderes Ergebnis. Der Körper ist der Dialog.

#### 4.3.3 Lymphsystem

**Visuell**: Grün-gelbes Netzwerk, subtiler als die anderen Systeme. Lymphknoten als leuchtende Knotenpunkte. Je stärker das System, desto dichter das Netzwerk und desto heller die Knoten.

**Was es regelt**:
- **Gift-Resistenz**: Wie schnell Gifte abgebaut werden und wie stark sie wirken
- **Krankheitsresistenz**: Chance, Krankheiten abzuwehren (Aschelung, Knochenfäule, Titanenfieber)
- **Substanz-Toleranz**: DIE KERNMECHANIK. Wie viel chemische Verstärkung der Körper verträgt, bevor negative Effekte eintreten
- **Regeneration**: Passive Heilungsrate außerhalb des Kampfes
- **Narbenbildung**: Starkes Lymphsystem = weniger permanente Debuffs durch schwere Verletzungen

**Steigerung durch**: Überleben von Vergiftungen (wer Gift überlebt, wird resistenter), Krankheiten durchstehen, kontrollierte Substanznutzung, Innenvolk-Training.

**EMERGENTES GAMEPLAY — Die Substanz-Schleife**:

Das Lymphsystem ist das, was dieses Leveling-System von jedem Skill-Tree unterscheidet. Es schafft ein Risiko-Ertrags-System, das JEDE andere Mechanik im Spiel berührt:

```
Substanz einnehmen → Temporärer Boost (Stärke, Reflexe, Wahrnehmung)
                   → Lymphsystem-Belastung
                   → Wenn Belastung > Toleranz:
                       → Sucht-Stufe steigt
                       → Entzugserscheinungen ohne Substanz
                       → Krankheitsrisiko steigt
                       → Langzeit: permanente Debuffs
```

Der Spieler KANN sich chemisch verstärken. Die Boosts sind real und mächtig. Aber der Körper hat Grenzen. Ein Spieler mit schwachem Lymphsystem, der Leistungsverstärker nimmt, spielt russisches Roulette mit seinem Charakter. Ein Spieler mit starkem Lymphsystem kann Substanzen kontrolliert einsetzen — wie ein Werkzeug, nicht wie eine Krücke.

**Das ist die Kernmechanik des Innenvolks**: Sie haben gelernt, das Lymphsystem zu stärken UND Substanzen zu raffinieren. Wer sich mit ihnen einlässt, bekommt Zugang zu beidem. Wer nur die Substanzen nimmt, ohne das Training — der endet zerbrochen.

**Gameplay-Beispiel**: Bosskampf. Der Spieler kann ihn nicht besiegen — zu schnell, zu stark. Der Innenvolk-Händler bietet "Graukristall" an — ein Amphetamin-Äquivalent, das Reflexe und Wahrnehmung für 2 Minuten verdoppelt. Lymphsystem-Toleranz: 3. Graukristall-Belastung: 4. Der Spieler nimmt es trotzdem. 2 Minuten Übermenschlichkeit. Boss stirbt. Danach: Sucht-Stufe 1, 30 Minuten Entzugserscheinungen (Tremor, Sichtfeldeinschränkung, Ausdauer-Crash), und das nächste Mal braucht er eine höhere Dosis für denselben Effekt. War es das wert? Das ist die Frage, die wir verkaufen.

---

## 4.4 Substanzen — Chemie als Gameplay

### Spieler-Fantasie
*"Die Welt ist chemisch. Gifte, Drogen, Heilmittel — alles ist eine Frage der Dosis. Ich entscheide, was ich meinem Körper antue."*

### Konzept

Kein Steampunk. Kein Dampf. Kein viktorianischer Alchemisten-Kitsch. Das hier ist **Biotech** — mittelalterliche Biochemie, basierend auf der Erkenntnis, dass Titanengewebe chemisch aktiv ist. Das Innenvolk hat gelernt, aus Titanenresten Substanzen zu gewinnen, die den sterblichen Körper verändern. Echte Gifte. Echte Drogen. Echte Konsequenzen.

### Substanz-Kategorien

**1. Heilmittel (Legal, allgemein verfügbar)**

| Substanz | Wirkung | Herkunft | Preis |
|----------|---------|----------|-------|
| Aschetinktur | Langsame Heilung über Zeit | Siedlervolk-Apotheker | Niedrig |
| Knochenmehl-Paste | Stabilisiert Frakturen, reduziert Muskel-Skelett-Debuffs | Höhlenvolk-Händler | Mittel |
| Lymphwasser | Beschleunigt Giftabbau | Innenvolk-Händler (legal) | Hoch |

**2. Leistungsverstärker (Grauzone, regional unterschiedlich legal)**

| Substanz | Boost | Dauer | Lymph-Belastung | Suchtpotenzial |
|----------|-------|-------|-----------------|----------------|
| Graukristall | Reflexe +50%, Wahrnehmung +30% | 120 Sek. | 4 | Hoch |
| Titanen-Adrenalin | Nahkampfschaden +40%, Schmerzresistenz +60% | 90 Sek. | 3 | Mittel |
| Ascheatem | Ausdauer-Regeneration x3, Unterwasser-Zeit x2 | 180 Sek. | 2 | Niedrig |
| Nervenfeuer | Sprint-Geschwindigkeit +30%, Klettergeschwindigkeit +50% | 60 Sek. | 3 | Mittel |
| Tiefblick | Nachtsicht, verborgene Objekte sichtbar | 300 Sek. | 5 | Sehr hoch |

**3. Gifte (Illegal, Schwarzmarkt)**

| Gift | Wirkung auf Ziel | Anwendung | Herstellung |
|------|-------------------|-----------|-------------|
| Aschenstaub | Langsame Erschöpfung, Ausdauer-Drain | Auf Klinge / ins Essen | Ascheextrakt + Pilzsporen |
| Knochenriss | Muskel-Skelett-Debuff, Bewegungseinschränkung | Auf Klinge | Knochenmehl + Säure |
| Lymphbrand | Zerstört Substanz-Toleranz, macht anfällig für alles | Ins Getränk | Titanenblut + Destillat (SELTEN) |
| Schlafgift | Bewusstlosigkeit (nicht-letal) | Pfeilspitze / Nahrung | Sumpfpilz-Extrakt |

**4. Chemische Reaktionen**

Substanzen interagieren miteinander. Das ist kein Random-System — es folgt einer internen Chemie-Logik:

- **Graukristall + Titanen-Adrenalin**: Überdosis. Sofortige Sucht-Stufe +2, aber 30 Sekunden völlige Unverwundbarkeit. Danach: Bewusstlosigkeit.
- **Aschetinktur + Lymphwasser**: Verstärkte Heilung. Synergieeffekt.
- **Tiefblick + Graukristall**: Halluzinationen. Die Wahrnehmungssteigerung kippt — der Spieler sieht Dinge, die nicht da sind. Oder doch?
- **Jedes Gift + Lymphwasser (rechtzeitig)**: Gegenmittel. Timing-Fenster: 30 Sekunden.

**Gameplay-Beispiel**: Der Spieler muss in eine Siedlervolk-Festung einbrechen. Plan: Schlafgift ins Wasser der Wache, warten bis Wirkung eintritt, einsteigen. Problem: Der Koch probiert das Essen vor dem Servieren. Lösung: Eine Dosis, die den Koch nur leicht benebelt (halbe Dosis = halber Effekt), aber die Wache komplett ausschaltet (volle Portion). Oder: den Koch bestechen. Oder: gar kein Gift, stattdessen Nervenfeuer und über die Mauer klettern. Das Substanz-System erweitert den Lösungsraum jeder Situation.

---

## 4.5 Rüstung & Ausrüstung — Modulares Slot-System

### Spieler-Fantasie
*"Meine Rüstung erzählt meine Geschichte. Jedes Teil wurde verdient, angepasst, repariert. Ich sehe anders aus als jeder andere Spieler — weil mein Weg ein anderer war."*

### Konzept

Modulares Slot-System. Keine Rüstungs-Sets mit festen Boni. Stattdessen: einzelne Teile, die der Spieler kombiniert, modifiziert und anpasst. Von einfachen Leder-Stücken bis zu Knochenmetall-Plattenrüstungen. High Fashion Mittelalter — nicht Fantasy-Kitsch, sondern Rüstung, die aussieht, als hätte ein Schmied sie für einen echten Körper gemacht.

### Slot-System

```
┌──────────────────────────────────────────────┐
│                   KOPF                        │
│   Helm / Kapuze / Maske / Krone / Nichts     │
├──────────────────────────────────────────────┤
│                 SCHULTERN                     │
│   Schulterstücke / Umhang-Ansatz / Nichts    │
├──────────────────────────────────────────────┤
│                  TORSO                        │
│   Brustpanzer / Kettenhemd / Lederharness    │
├──────────────────────────────────────────────┤
│                   ARME                        │
│   Armschienen / Handschuhe / Bandagen        │
├──────────────────────────────────────────────┤
│                   BEINE                       │
│   Beinschienen / Hose / Kilt                 │
├──────────────────────────────────────────────┤
│                   FÜSSE                       │
│   Stiefel / Sandalen / Wickel                │
├──────────────────────────────────────────────┤
│                   RÜCKEN                      │
│   Umhang / Rucksack / Köcher / Nichts        │
├──────────────────────────────────────────────┤
│                 ACCESSOIRE                    │
│   Gürtel / Kette / Talisman / Nichts         │
└──────────────────────────────────────────────┘
```

### Material-Hierarchie

| Material | Schutz | Gewicht | Lautstärke | Verfügbarkeit | Ästhetik |
|----------|--------|---------|------------|---------------|----------|
| Stoff / Leinen | Minimal | Sehr leicht | Still | Überall | Einfach, funktional |
| Leder (gegerbt) | Niedrig | Leicht | Leise | Verbreitet | Robust, gebrauchsspurig |
| Kettenglieder | Mittel | Mittel | Laut (klirrt) | Siedlervolk-Schmiede | Klassisch, militärisch |
| Platte (Stahl) | Hoch | Schwer | Sehr laut | Siedlervolk-Meister | Imposant, autoritär |
| Knochenmetall | Sehr hoch | Mittel (leichter als Stahl!) | Summt leise | Selten, Knochenturm-Abbau | Alien, organisch, irisierend |
| Innenvolk-Biogewebe | Variabel | Sehr leicht | Still | Innenvolk-Labore | Verstörend, lebendig aussehend |

### Modifikation

Jedes Rüstungsteil kann modifiziert werden:
- **Verstärkung**: Zusätzliches Material auf kritische Stellen. Mehr Schutz, mehr Gewicht.
- **Polsterung**: Innenpolster gegen Schlagschaden. Weniger Mobilität, mehr Überleben.
- **Substanz-Beschichtung**: Innenvolk-Technologie. Rüstungsteile mit Substanzen imprägnieren — z.B. Gift-Resistenz-Beschichtung, Kälteschutz, Asche-Abweisung.
- **Fraktions-Insignien**: Rüstung mit Fraktionssymbolen kennzeichnen. Ändert NPC-Reaktionen. Siedlervolk-Emblem? Die Wache lässt dich durch. Höhlenvolk-Markierungen? Die Händler geben dir bessere Preise.
- **Tarnung**: Rüstung anpassen an Umgebung. Asche-graue Färbung für die Einöden, dunkle Töne für Nacht-Operationen.

**Gameplay-Beispiel**: Der Spieler hat einen Knochenmetall-Brustpanzer gefunden — den besten Schutz im Spiel. Aber: Knochenmetall summt. In Stealth-Situationen verrät es ihn. Also modifiziert er ihn: Innenvolk-Biogewebe als Dämpfung unter dem Panzer (reduziert das Summen), Höhlenvolk-Leder-Polster an den Gelenken (für Mobilität), Siedlervolk-Schulterplatten (für Einschüchterung). Das Ergebnis ist einzigartig — kein anderer Spieler wird exakt diese Kombination tragen.

---

## 4.6 Einschüchterung & Soziale Mechaniken

### Spieler-Fantasie
*"Die Welt sieht mich. Sie reagiert auf das, was ich bin — nicht auf ein Menü, in dem ich 'Einschüchtern' auswähle."*

### Konzept

Keine abstrakten Charisma-Checks. Kein Dialogue-Wheel mit "[Einschüchtern]"-Option. Die Welt reagiert auf den GESAMTEN Spieler — seine Ausrüstung, seinen Ruf, seine physische Erscheinung, seine bekannten Taten, seine Fraktionszugehörigkeit. Das ist kein separates System. Das ist ein LAYER über allem anderen.

### Die Einschüchterungs-Matrix

Wie ein NPC auf den Spieler reagiert, basiert auf einem Zusammenspiel von Faktoren:

**Physische Präsenz** (automatisch berechnet):
- Muskel-Skelett-Stufe (körperliche Masse)
- Ausrüstungsgewicht und -typ (volle Plattenrüstung vs. Lumpen)
- Sichtbare Waffen (Zweihand-Axt am Rücken vs. versteckter Dolch)
- Sichtbare Narben / Kampfspuren (akkumulieren über das Spiel)
- Blut an der Rüstung (frisch? — extremer Einschüchterungsfaktor, aber Ruf-Malus bei Zivilisten)

**Reputation** (reaktiv, akkumulativ):
- Lokaler Ruf: Was hat der Spieler IN DIESER REGION getan?
- Fraktions-Ruf: Zu welcher Fraktion wird der Spieler gezählt?
- Spezifische Taten: "Der Typ, der den Banditenchef in der Knochenschlucht getötet hat" — das spricht sich rum. Wachen sind nervöser, Banditen vorsichtiger, Händler höflicher.
- Gerüchte: NPCs reden über den Spieler. Nicht immer korrekt. Ein Spieler, über den wilde Gerüchte kursieren (ob wahr oder nicht), wird anders behandelt.

**Kontext** (situativ):
- Tageszeit: Nachts in einer dunklen Gasse ist der Einschüchterungsfaktor höher
- Umgebung: In DEINEM Territorium bist du einschüchternder als in fremdem
- Zahlenverhältnis: Allein gegen fünf — die fünf sind mutiger. Allein gegen einen — der eine ist nervöser
- Wissen: Hat der NPC den Spieler schon kämpfen SEHEN? Dann weiß er, was er kann

### NPC-Reaktions-Spektrum

Nicht binär (Angst/keine Angst), sondern ein Spektrum:

| Reaktion | Trigger | NPC-Verhalten |
|----------|---------|---------------|
| **Verachtung** | Spieler schwach, kein Ruf, schlechte Ausrüstung | NPC ignoriert, beleidigt, verweigert Service |
| **Gleichgültigkeit** | Spieler unauffällig, neutraler Ruf | Standard-Interaktion |
| **Respekt** | Spieler kompetent, guter Ruf in Fraktion | Bessere Preise, mehr Dialogoptionen, Hinweise |
| **Furcht** | Spieler stark, gewalttätiger Ruf, schwere Rüstung | NPC kooperiert sofort, gibt Info, weicht aus |
| **Panik** | Spieler bekannt für Massaker, blutverschmiert, bewaffnet | NPC flieht, ruft Wachen, oder ergibt sich wortlos |
| **Trotz** | Spieler einschüchternd, aber NPC hat Prinzipien/Todesmut | NPC weigert sich trotz Angst — die härtesten Quests |

**Gameplay-Beispiel**: Gleicher NPC, gleiche Frage ("Wo ist die Schmuggler-Höhle?"), drei Spielertypen:

*Spieler A — Der Diplomierte*: Küstenvolk-Robe, Bücher im Rucksack, kein sichtbares Blut, bekannt als Forscher. NPC antwortet ausführlich, gibt historischen Kontext, bietet an, mitzukommen. Kein Preis, kein Kampf. Wissen als Eintrittskarte.

*Spieler B — Der Söldner*: Volle Plattenrüstung, Blut an den Handschuhen, zwei Köpfe am Gürtel (Banditen-Trophäen), lokaler Ruf als "der Knochenbrecher." NPC antwortet sofort, stottert, zeigt den Weg, und verschwindet. Die Info ist gratis — weil die Alternative tödlich scheint.

*Spieler C — Der Niemand*: Tag 1, Lumpen, kein Ruf, keine sichtbare Waffe. NPC lacht. "Was willst du, Fremder? Verschwinde." Der Spieler muss ARBEITEN für die Information — bezahlen, einen Gefallen tun, oder den NPC auf anderem Weg überzeugen. Gothic-Feeling: Du bist nichts. Noch.

---

## 4.7 Wirtschaftssystem

### Spieler-Fantasie
*"Geld ist Macht, Handel ist Politik, und der Schwarzmarkt kennt kein Gewissen. Ich entscheide, mit wem ich Geschäfte mache — und jedes Geschäft hat einen Preis, der über Gold hinausgeht."*

### Konzept

Drei Wirtschafts-Schichten: legaler Handel (Siedlervolk-dominiert), Händlernetzwerk (Höhlenvolk), Schwarzmarkt. Jede Schicht hat eigene Währungen, Regeln und Konsequenzen.

### Tier 1 — Legaler Handel (Siedlervolk)

Das Siedlervolk kontrolliert den offiziellen Handel. Feste Preise, regulierte Waren, Steuern.

- **Währung**: Aschenmark (Münzen, standardisiert)
- **Verfügbar**: Grundnahrung, Standard-Rüstung, einfache Waffen, Werkzeug, Baumaterial
- **Nicht verfügbar**: Substanzen (über Heilmittel hinaus), Knochenmetall (staatlich kontrolliert), Gifte, Innenvolk-Biotech
- **Preise**: Fest, aber regional unterschiedlich. Knochenmetall ist in der Nähe der Minen billig und in der Stadt teuer.
- **Steuern**: Der Spieler zahlt Marktsteuer. Wer handelt, finanziert das Siedlervolk. Das ist nicht neutral — das ist politisch.

### Tier 2 — Händlernetzwerk (Höhlenvolk)

Das Höhlenvolk operiert parallel zum offiziellen Handel. Nicht illegal, aber außerhalb der Siedlervolk-Kontrolle. Tauschhandel, Gefälligkeiten, Beziehungen.

- **Währung**: Kein Geld — Tausch und Versprechen. "Ich gebe dir das Schwert, du bringst mir das Kraut aus der Schlucht." Oder: Gefälligkeits-Schulden, die eingefordert werden.
- **Verfügbar**: ALLES, was jemand anbietet. Höhlenvolk-Händler handeln mit allem. Moralische Urteile sind schlecht fürs Geschäft.
- **Spezialität**: Seltene Materialien, Substanzen (legal und illegal), Informationen, Kontakte. Wer etwas Bestimmtes sucht, fragt das Höhlenvolk.
- **Risiko**: Kein Verbraucherschutz. Gefälschte Waren, überhöhte Tauschforderungen, Informationen, die halb wahr und halb Falle sind.
- **Vertrauen**: Langfristiger Handel mit denselben Händlern verbessert Angebote. Das Höhlenvolk belohnt Loyalität — und bestraft Betrug.

### Tier 3 — Schwarzmarkt

Existiert in den Schatten aller Fraktionen. Kein zentraler Ort — ein Netzwerk aus Kontakten, Codewörtern, toten Briefkästen.

- **Währung**: Aschenmark (unversteuert), Knochenmetall-Fragmente (als Wertanlage), Geheimnisse
- **Verfügbar**: Alles, was verboten ist. Gifte, militärische Ausrüstung, gestohlene Knochenmetall-Lieferungen, gefälschte Fraktions-Insignien, Auftragsmorde (als Käufer ODER Verkäufer)
- **Zugang**: Nicht offen. Der Spieler muss den Schwarzmarkt FINDEN. Durch Ruf (krimineller Ruf öffnet Türen), Kontakte (Höhlenvolk-Händler als Vermittler), oder eigene Recherche
- **Risiko**: Erwischtwerden = Ruf-Verlust, Verhaftung, Fraktions-Feindschaft. Der Schwarzmarkt ist lukrativ, aber jede Transaktion ist ein Risiko.

### Wirtschafts-Dynamik

**Angebot und Nachfrage**: Wenn der Spieler einen Knochenmetall-Konvoi des Siedlervolks ausraubt, steigt der Knochenmetall-Preis in der Region. Wenn der Spieler eine Handelsroute sichert, sinken die Preise. Die Wirtschaft reagiert.

**Monopole und Machtkämpfe**: Wer die Knochenmetall-Minen kontrolliert, kontrolliert die Region. Der Spieler kann in diesen Machtkampf eingreifen — als Händler, als Söldner, als Saboteur. Wirtschaft IST Politik.

**Inflation**: Je mehr Aschenmark im Umlauf, desto weniger wert. Keine abstrakte Mechanik — der Spieler sieht die Preise steigen, hört NPCs klagen, sieht Händler schließen. Wirtschaftliche Konsequenzen sind spürbar.

**Gameplay-Beispiel**: Der Spieler braucht Graukristall für einen Bosskampf. Legaler Weg: gibt es nicht — Graukristall ist verboten in Siedlervolk-Territorium. Höhlenvolk-Händler: hat es, will aber einen Gefallen — "Bring mir die Frachtliste des nächsten Siedlervolk-Konvois." Schwarzmarkt: hat es, will Knochenmetall-Fragmente als Bezahlung. Innenvolk direkt: haben es, geben es umsonst — aber nur, wenn der Spieler sich einer "Behandlung" unterzieht (permanente Lymphsystem-Modifikation, Risiko unklar). Vier Wege zum gleichen Item. Jeder hat einen anderen Preis. Keiner ist kostenlos.

---

## 4.8 System-Interaktion — Wie alles zusammenhängt

Kein System existiert isoliert. Die Stärke dieses Designs liegt in den Verbindungen:

```
NERVENSYSTEM ←→ SUBSTANZEN
    │                │
    │   Lymphsystem  │
    │   reguliert    │
    │   Toleranz     │
    ▼                ▼
COMBAT ←→ EINSCHÜCHTERUNG
    │                │
    │   Rüstung +    │
    │   Ruf formen   │
    │   Reaktionen   │
    ▼                ▼
WIRTSCHAFT ←→ FRAKTIONEN
    │                │
    │   Handel =     │
    │   Politik      │
    └────────────────┘
```

**Beispiel einer System-Kette**: Der Spieler trainiert sein Lymphsystem (Nervensystem) → kann Graukristall sicher verwenden (Substanzen) → gewinnt einen schwierigen Kampf (Combat) → wird bekannt als "der Aschenteufel" (Einschüchterung) → Händler bieten bessere Deals an aus Angst (Wirtschaft) → das Siedlervolk wird misstrauisch, das Innenvolk fasziniert (Fraktionen) → neue Questlinien öffnen sich.

Das ist kein linearer Pfad. Das ist ein Netzwerk. Und der Spieler schreibt seinen eigenen Weg hindurch.

---

*Erster Entwurf. 8 Systeme, 3 Stunden, 2 Kaffee, 1 Millimeterpapier-Block. Die Systeme stehen. Was fehlt: Balancing-Tabellen (Google Sheets, morgen), Prototyping-Prioritäten (mit Finn besprechen), und die Frage, ob das Nervensystem-Leveling technisch machbar ist (Tobi fragen — der wird entweder grinsen oder weinen).*

*Post-It am Monitor: "JEDES SYSTEM → KERNFRAGE PRÜFEN: Dient es der Erfahrung des Fremden?"*

*Zweites Post-It: "KEIN SYSTEM DARF ALLEIN STEHEN. Wenn ein System keine Verbindung zu zwei anderen hat, ist es das falsche System."*

— Darius Engel, Game Director

\newpage

---
agent: leo
day: 3
task: "GDD Kapitel 05 — Vertical Slice Walkthrough"
version: v0.2
basis: walkthrough-v0.1 (Tag 2), CD-Feedback Tag 3, Fraktionsmodell v2
memories_referenced: [leo-015, leo-016, leo-017, leo-018]
status: draft
---

# Kapitel 05 — Vertical Slice Walkthrough

> *Nicht Feature-Liste. Nicht Systemdiagramm. Walkthrough. Du ERLEBST das Spiel. Wie im Diablo Pitch von 1994: Wenn der Leser es nicht fühlt, existiert es nicht.*
> *— L. Fischer, Tag 3*

---

## 1. Scope

**Eine Region. Eine Hauptquest. Zwei Nebenquests. 60–90 Minuten Spielzeit.**

Der Vertical Slice zeigt einen Ausschnitt der Insel: die Ankunftsküste und die erste Siedlung. Alles, was RELICS ausmacht, muss hier erlebbar sein — nicht erklärt, nicht versprochen, sondern *gespielt*.

Was der Slice beweist:

- Die Kamera funktioniert (FP/TP-Switch)
- Die Fraktionen sind spürbar (drei aktiv, zwei angedeutet)
- Das Nervensystem-Leveling existiert als Moment, nicht als Tutorial
- Environmental Storytelling trägt die Welt, bevor ein einziger NPC den Mund aufmacht
- Die Kernfrage des Spiels (*"Was schuldet ein Fremder einem Ort, der ihn nicht gerufen hat?"*) ist im Gameplay eingebettet, nicht im Dialog

---

## 2. Die ersten 30 Minuten

### Minute 0–3: Ankunft

Du öffnest die Augen.

First Person. Kein HUD. Kein Kompass. Kein Tutorial-Pop-up. Nur Geräusche — Wellen, die über Kiesel rollen. Wind. Etwas knirscht unter deinem Rücken, als du dich bewegst.

Du liegst auf einem Kieselstrand. Die Kamera zeigt dir deine Hände: abgeschürft, schmutzig, leer. Links das Meer, grau und endlos. Rechts eine Steilküste aus dunklem Gestein — Basalt, durchzogen von etwas Weißem, das im Licht seltsam schimmert. Knochenmetall, aber das weißt du noch nicht.

Du stehst auf. Die Kamera schwankt — du bist schwach. Kein Lebensbalken, aber dein Körper erzählt dir, wie es dir geht: langsame Bewegungen, flacher Atem, Blickfeld leicht verengt.

**Du weißt nicht, wer du bist.**

Das ist keine Amnesie-Trope. Das ist das Spiel. Deine Identität existiert noch nicht. Die Insel wird dir eine geben — ob du willst oder nicht.

### Minute 3–8: Der Strand — Erkundung

Du gehst den Strand entlang. First Person bleibt. Die Kamera ist dein Körper — du BIST hier, nicht du beobachtest jemanden, der hier ist.

Was du findest:

- **Treibholz, Seetang, zerbrochene Kisten.** Du kannst Dinge aufheben — kein Inventar-Pop-up, du streckst die Hand aus und nimmst. Minimale Interaktion, maximales Körpergefühl.
- **Eine Feuerstelle.** Kalt. Jemand war vor dir hier. Die Asche ist Tage alt. Daneben ein zerrissenes Stück Stoff mit einem Symbol, das du nicht kennst — ein stilisiertes Auge mit drei Pupillen. (*Küstenvolk-Symbol. Bedeutung: später.*)
- **Die Leiche.** Halb im Wasser, Gesicht nach unten. Als du sie umdrehst — der erste echte Interaktions-Moment — siehst du: Kein Gesicht mehr. Etwas hat es weggefressen. Oder weggeätzt. In der Hand ein **rostiges Messer**. Du kannst es nehmen. Oder nicht. Beides hat Konsequenzen — aber keine, die das Spiel dir jetzt verrät.

Das Messer ist die erste Entscheidung. Nicht "Drücke A für Gut, B für Böse." Du nimmst es, oder du lässt es. Die Welt merkt es sich.

### Minute 8–15: Der Aufstieg — Environmental Storytelling

Ein Pfad führt von der Küste nach oben. Du kletterst — First Person, physisch. Deine Hände greifen ins Gestein. Du hörst deinen Atem.

Der Pfad erzählt dir die Welt, bevor ein einziger NPC es tut:

- **Stufe 1: Natur.** Aschehaltige Erde, Flechten, Pilznetzwerke. Die Vegetation ist seltsam — kein Grün, sondern Grautöne, gelegentlich ein krankes Gelb. Die Insel lebt, aber sie lebt *anders*.
- **Stufe 2: Spuren.** Markierungen an Felsen — Knochenmetall-Graffiti, Handelszeichen. Jemand hat hier Routen markiert. Für wen? Warum? Die Zeichen sind nicht übersetzt. Du sammelst Fragmente, keine Antworten.
- **Stufe 3: Architektur.** Eine verfallene Wegstation. Die Architektur erzählt vor dem Dialog: Die Mauern sind aus zwei Materialien — unten organisch, gewachsen, fast *biologisch* in der Struktur (Innenvolk-Bauweise, aber das weißt du noch nicht), oben rechtwinklig, funktional, klar (Siedlervolk-Ergänzung). Zwei Kulturen an einem Ort. Konflikt in Stein.

Veras Regel: **Architektur erzählt vor Dialog.** Wenn ein Spieler einen Ort betritt, muss die Silhouette auf 50 Meter die Geschichte erzählen. Alles danach ist Vertiefung, nicht Einführung.

### Minute 15–20: Das Siedlungstor — Die Kernfrage als Gameplay

Du siehst die Siedlung, bevor du sie erreichst. Auf einer Anhöhe, hinter Palisaden aus Knochenmetall und Holz. Rauch aus mehreren Feuerstellen. Lebenszeichen. Aber die Mauern sind hoch.

Am Tor: zwei Wachen. Siedlervolk — menschlich, pragmatisch, in funktionaler Rüstung. Waffen aus Knochenmetall. Sie sehen dich kommen.

**"Was bringst du mit?"**

Das ist kein Willkommensgruß. Das ist die Kernfrage des Spiels in einem Satz. Dieser Ort schuldet dir nichts. Du schuldet diesem Ort nichts. Aber du brauchst rein, und sie brauchen einen Grund, dich reinzulassen.

Deine Optionen sind nicht aufgelistet. Kein Dialograd. Du hast, was du hast:

- **Das rostige Messer** (wenn du es genommen hast) — zeigt Pragmatismus. Oder Bedrohung. Kommt drauf an, wie du es zeigst.
- **Das Stoffstück mit dem Symbol** — zeigt Neugier. Oder Verbindung zum Küstenvolk. Die Wachen reagieren anders.
- **Nichts** — du bist ein Niemand mit leeren Händen. Das ist seine eigene Aussage.
- **Information** — "Da unten liegt eine Leiche." Das Spiel registriert, *wie* du es sagst.

Der Zugehörigkeitsindex beginnt hier. Unsichtbar, aber aktiv. Jede Antwort verschiebt dich auf den fünf Achsen: Handel, Deutung, Anspruch, Körper, Verlust. Du wirst das nie als Zahl sehen — du wirst es *spüren*, weil die Welt anders auf dich reagiert.

### Minute 20–25: Erster Kontakt — Der Tiermenschen-Händler

Du bist drin. Die Siedlung ist klein, aber lebendig. Siedlervolk-Architektur: rechte Winkel, Funktionalität, Holz und Knochenmetall.

Und dann — am Marktstand in der Mitte — jemand, der *nicht* reinpasst.

**Kamera-Switch: Third Person.**

Zum ersten Mal schwenkt die Kamera nach hinten. Du siehst deinen Charakter — zum ersten Mal vollständig. Und du siehst IHN: Ein Tiermenschen-Händler. Fellträger. Khajiit-Verwandtschaft, aber *anders* — keine Fantasie-Katze, sondern etwas Subtileres. Fellmuster, tierische Augen, eine Haltung zwischen Entspanntheit und Wachsamkeit. Seidenstraßen-Ästhetik: Reisekleidung, Schmuck aus Materialien, die du noch nie gesehen hast.

Warum der Kamera-Switch? **Weil du ihn SEHEN musst.** In First Person ist er ein Gesicht. In Third Person ist er eine Silhouette, eine Kultur, ein Statement. Vera hat recht: Character-Showcases brauchen die Totale.

Der Händler spricht dich nicht an. Er *beobachtet* dich. Wenn du zu ihm gehst:

> *"Ah. Frisch von der Küste, hm? Man sieht es an den Stiefeln. Aschekruste, Salzrand, kein Handelszeichen. Du bist entweder sehr arm oder sehr neu. Beides kenne ich."*

Er verkauft dir nichts — noch nicht. Er bietet dir einen Tausch an: Information gegen Information. Was du am Strand gesehen hast, gegen etwas, das er weiß. Kein Goldsystem. Kein Shop-Interface. Ein Gespräch mit Konsequenz.

**Höhlenvolk-Achse steigt.** Du lernst: Auf dieser Insel hat alles seinen Preis.

### Minute 25–30: Erste Substanz-Begegnung

Du erkundest die Siedlung. In einer Seitengasse — weniger Licht, anderer Geruch, etwas Süßliches in der Luft — lehnt jemand an einer Wand. Blass, ruhig, mit Augen, die zu viel sehen.

> *"Du siehst müde aus. Müde und leer. Ich hätte da was — ein Verstärker. Nichts Schlimmes. Macht die Augen schärfer, die Hände ruhiger. Für eine Stunde bist du mehr, als du bist."*

Die Substanz schimmert in einem kleinen Glasfläschchen. Eine Flüssigkeit, die sich bewegt, als hätte sie einen eigenen Willen.

Nimmst du sie?

- **Ja:** Du trinkst. Der Bildschirm flackert. Für einen Moment — einen einzigen, kurzen Moment — siehst du die Welt *anders*. Die Knochenmetall-Adern in den Wänden LEUCHTEN. Die Menschen um dich herum haben etwas unter der Haut — ein Netzwerk, pulsierend, lebendig. Dann ist es weg. Und du willst es wieder sehen.
- **Nein:** Der Fremde zuckt die Schultern. "Dein Verlust. Aber du weißt jetzt, wo du mich findest." Er verschwindet. Die Gasse riecht immer noch süß.

**Innenvolk-Achse: erster Kontakt.** Das Nervensystem-Leveling ist kein Feature, das dir erklärt wird. Es ist ein *Erlebnis*, das dich neugierig macht.

---

## 3. Hauptquest — "Die Schuld des Strandes"

**Pitch (1 Absatz):**

Die Leiche am Strand war kein Zufall. Sie war ein Bote — geschickt von der Festung im Landesinneren, der Siedlervolk-Hauptstadt. Er trug eine Nachricht, die jetzt verschwunden ist. Die Siedlung am Tor weiß von dem Boten und wartet auf die Nachricht — eine Warnung vor etwas, das aus den alten Titanenadern aufgestiegen ist. Der Spieler wird zum Ersatz-Boten: nicht weil er die Nachricht hat, sondern weil er der Einzige ist, der den Weg zurück zum Strand kennt. Die Hauptquest führt durch die gesamte Region — vom Strand über die Küstenruinen (Küstenvolk) bis zur Handelsroute (Höhlenvolk) und zurück zur Siedlung, wo die Nachricht rekonstruiert werden muss. Am Ende entscheidet der Spieler: Wem gibt er die Nachricht? Der Siedlung, die sie erwartet? Der Festung, die sie geschickt hat? Dem Händler, der dafür bezahlt? Oder niemandem — weil manche Wahrheiten besser im Sand vergraben bleiben?

---

## 4. Nebenquest 1 — "Die Karawane nach Nirgendwo"

**Fraktion:** Höhlenvolk (Tiermenschen-Händler)

**Pitch:**

Der Händler vom Markt hat ein Problem: Seine Karawane ist überfällig. Drei Fellträger-Händler, die eine Route durch die Aschefelder gehen sollten, sind nicht angekommen. Nicht ungewöhnlich — die Asche verschluckt Spuren — aber diesmal hat er ein schlechtes Gefühl. Er bietet dem Spieler einen Deal: Finde die Karawane, bring Nachricht, und er gibt Zugang zu seinem echten Warenlager. Nicht den Touristenkram auf dem Marktstand — die Sachen, die kein Siedlervolk-Auge je gesehen hat.

**Was der Spieler lernt:**

- Das Höhlenvolk ist kein Volk im territorialen Sinn — sie sind ein *Netzwerk*. Handelsrouten sind ihr Territorium.
- Die Karawane wurde nicht überfallen. Sie hat einen Umweg genommen — durch eine Ruine, die niemand betreten sollte. Warum?
- Vertrauen im Höhlenvolk ist Währung. Der Spieler verdient es — oder kauft es, mit einem Preis, den er vielleicht erst später versteht.

**Zugehörigkeitsindex:** Handel-Achse steigt signifikant.

---

## 5. Nebenquest 2 — "Unter der Haut"

**Fraktion:** Innenvolk (Destillateure / Biotech)

**Pitch:**

Der Fremde in der Gasse war kein Dealer — er war ein Rekrutierer. Die Substanz, die er angeboten hat, ist kein simples Rauschmittel. Sie ist ein *Schlüssel*: eine destillierte Verbindung aus Titanenblut und organischer Chemie, die das menschliche Nervensystem temporär mit den Überresten der Titanen synchronisiert. Das Innenvolk nennt es "Tiefe Resonanz." Die Siedlervolk-Wachen nennen es "Gift."

Der Spieler wird in ein verstecktes Labor unter der Siedlung geführt — durch einen Keller, einen Tunnel, in einen Raum, der aussieht wie das Innere eines Organs. Hier arbeiten die Destillateure: ruhig, präzise, fasziniert. Sie bieten dem Spieler keinen weiteren "Hit" an. Sie bieten ihm Wissen an: Was, wenn das Nervensystem keine Metapher ist? Was, wenn der Titanenleib buchstäblich in jedem Lebewesen auf dieser Insel steckt — und man nur lernen muss, hinzuhören?

**Was der Spieler lernt:**

- Das Nervensystem-Leveling ist keine Game-Mechanik. Es ist ein *kulturelles Phänomen*. Das Innenvolk hat es entdeckt, aber alle Bewohner der Insel tragen es in sich.
- Die Substanzen sind real und gefährlich. Verstärkung hat Kosten. Sucht ist kein Flavor-Text — sie verändert Gameplay-Optionen.
- Die Destillateure sind keine Feinde. Sie sind auch keine Freunde. Sie sind *radikal neugierig*, und das ist beides zugleich.

**Zugehörigkeitsindex:** Körper-Achse steigt. Aber: Risiko-Einführung. Der Spieler sieht zum ersten Mal, dass Fraktionsnähe Kosten hat.

---

## 6. Erstes Leveling-Moment

**Wann:** Nach Abschluss der Substanz-Quest (oder nach natürlicher Spielzeit, wenn genug Erfahrung gesammelt wurde).

**Was passiert:**

Der Spieler öffnet nicht ein Menü. Der Spieler *spürt* es.

Ein Kribbeln — visuell dargestellt als pulsierende Linien unter der Haut des Spielercharakters. Die Kamera schwenkt automatisch in Third Person (Nahaufnahme, über die Schulter). Unter der Haut deines Charakters wird ein Netzwerk sichtbar: leuchtende Bahnen, die sich verzweigen, verbinden, erweitern.

**Das Nervensystem-UI.**

Es ist kein Skill-Tree. Es ist ein *Körpersystem*. Drei Schichten (Tobis Flowmap-Layers):

1. **Somatisch** — physische Fähigkeiten (Kraft, Ausdauer, Reflexe)
2. **Sensorisch** — Wahrnehmung (Aura-Lesen, Substanz-Erkennung, Lügen-Gespür)
3. **Autonom** — unbewusste Reaktionen (Kampf-Instinkte, Anpassung, Resistenz)

Der Spieler wählt nicht "Skill +1." Er wählt, welche *Bahn* sich verstärkt. Die Visualisierung zeigt es: Eine leuchtende Linie wird breiter, heller, verzweigt sich weiter. Andere werden dafür schwächer.

**Warum das der virale Moment ist:**

Ein Streamer sieht zum ersten Mal sein Nervensystem aufleuchten. Chat flippt aus. "DUDE, SCHAU DIR DEINE ADERN AN." Jeder Spieler hat ein *anderes* Nervensystem. Screenshots vergleichen. TikTok-Clips: "Level 1 vs. Level 30 — mein Nervensystem." Reddit-Posts: Tier-Lists der besten Bahnen. Das ist nicht geplantes Marketing — das ist emergentes Community-Content.

---

## 7. Kamera-Regie

| Moment | Kamera | Grund |
|--------|--------|-------|
| Aufwachen am Strand | **FP** | Immersion. Du BIST hier. Keine Distanz. |
| Strandexploration | **FP** | Körpergefühl. Deine Hände, dein Atem, dein Blickfeld. |
| Leiche finden | **FP** | Intimität des Schreckens. Du drehst sie um, nicht eine Spielfigur. |
| Aufstieg zur Siedlung | **FP** | Environmental Storytelling. Die Welt auf Augenhöhe. |
| Torwache-Dialog | **FP** | Konfrontation. Augenkontakt. Du bist gemeint. |
| Siedlung betreten — Tiermenschen-Händler | **FP→TP Switch** | Character Showcase. Du musst IHN sehen. Und dich selbst neben ihm. |
| Siedlung erkunden | **TP** | Übersicht. Architektur, Silhouetten, Weltgefühl. |
| Substanz-Begegnung (Gasse) | **FP** | Intimität. Vertraulichkeit. Dieser Moment gehört nur dir. |
| Substanz-Wirkung | **FP (verzerrt)** | Die Welt durch andere Augen. Visueller Schock. |
| Nervensystem-Leveling | **TP (Nahaufnahme)** | Character Showcase. Dein Körper verändert sich. Du musst es sehen. |
| Kampf (wenn es dazu kommt) | **TP** | Übersicht, räumliches Bewusstsein, Veras Silhouetten-Regel. |
| Emotionale Dialoge | **FP** | Augenkontakt. Nähe. Kein Entkommen. |

**Prinzip:** Die Kamera ist kein technisches Feature. Die Kamera ist **Regie**. Jeder Switch hat einen Grund. Wenn der Spieler den Wechsel nicht bemerkt, haben wir es richtig gemacht.

---

## 8. Offene Fragen

- [ ] Fraktionsnamen: "Höhlenvolk", "Küstenvolk", "Siedlervolk" sind Arbeitstitel. Emre liefert finale Namen.
- [ ] Leiche am Strand: Welche Fraktion? Welches Geschlecht? Was hat das Gesicht zerstört? (Horror-Potenzial oder lore-relevant?)
- [ ] Substanz-Design: Wie sieht "Tiefe Resonanz" visuell aus? Vera muss das definieren.
- [ ] Nervensystem-UI: Tobis Flowmap-Layer-Prototyp als Grundlage. Wann erster Tech-Test?
- [ ] Kampf: Dieser Walkthrough hat bewusst keinen Combat-Moment. Wann und wie der erste Kampf stattfindet, muss Darius klären.
- [ ] Vampir-Hinweis: Kann in den ersten 30 Minuten ein subtiler Hint auf die Hidden-Content-Schicht eingebaut werden?

---

*Der Diablo Pitch hatte 8 Seiten und hat ein Genre erschaffen. Dieser Walkthrough hat ein paar mehr, aber das Prinzip ist dasselbe: Wenn du es nicht ERLEBST, existiert es nicht. Features sind Versprechungen. Ein Walkthrough ist ein Vertrag.*

*Gelbes Post-It: "WAS BRINGST DU MIT?" — die beste Torwache-Frage aller Zeiten. Die kommt auf jedes Marketing-Material.*

— Leo

\newpage

# Kapitel 06 — Art Direction

> **Autorin**: Vera Kowalski, Concept Artist & Environment Designer
> **Stand**: Tag 3, GDD-Sprint
> **Status**: Erster vollständiger Entwurf

---

## 1. Visuelle Identität: Biotech-Mittelalter

Das hier ist kein Steampunk. Kein Zahnrad, kein Dampf, kein viktorianisches Messinggefrickel. Steampunk ist retrospektive Industrieromantik — wir machen das Gegenteil.

**Biotech-Mittelalter** bedeutet: Eine Welt, in der Technologie nie mechanisch wurde, sondern biologisch. Statt Maschinen hat diese Zivilisation *Organismen gezüchtet*. Statt Schaltkreisen verlaufen Nervenbahnen. Statt Stahl wächst Chitin. Die Ästhetik liegt irgendwo zwischen gotischer Kathedrale und lebendem Korallenriff — monumental, aber atmend.

**Visueller Leitgedanke**: Stell dir vor, jemand hätte das Mittelalter mit CRISPR statt mit dem Webstuhl industrialisiert.

---

## 2. Materialsprache

Die gesamte visuelle Welt teilt sich in zwei Material-Vokabulare. Dieser Kontrast ist **das** zentrale Designwerkzeug der Art Direction.

### 2.1 Lebende Materialien (aktive Zivilisation)

| Material | Visuelle Eigenschaften | Einsatz |
|----------|----------------------|---------|
| **Chitin** | Dunkel, glänzend, facettiert wie Käferpanzer. Harte Kanten, aber organische Kurven. Farbspektrum: Schwarz bis tiefes Burgunder. | Rüstungen, tragende Architekturelemente, Werkzeuge |
| **Keratin** | Elfenbein bis Bernstein, leicht transluzent an dünnen Stellen. Wächst in Schichten, zeigt Jahresringe bei Querschnitten. | Bögen, Brücken, dekorative Elemente, Schmuck |
| **Biolumineszenz** | Kaltes Cyan bis warmes Amber. Pulsiert langsam (2–4 Sekunden Zyklus). Reagiert auf Nähe. Nie gleichmäßig — immer in Adern, Netzen, Clustern. | Beleuchtung, UI-Elemente, Wegmarkierungen, Statusanzeigen an Gebäuden |

**Regel**: Lebende Technologie hat *keine geraden Linien über 2 Meter*. Alles krümmt sich, alles verjüngt sich, alles hat eine leichte Asymmetrie — wie Knochen, wie Hörner, wie Muscheln.

### 2.2 Tote Materialien (Ruinen, alte Welt)

| Material | Visuelle Eigenschaften | Einsatz |
|----------|----------------------|---------|
| **Rost** | Orange-Braun bis Dunkelrot. Blättert in Schichten. Hinterlässt Spuren auf umliegenden Oberflächen (Rosttränen auf Stein). | Metallische Überreste einer früheren Ära, die *mechanisch* dachte |
| **Patina** | Kupfergrün bis Türkis. Glatt, fast samtartig. Sitzt in Vertiefungen, betont Reliefs. | Statuen, Beschläge, ehemals repräsentative Oberflächen |
| **Verfall** | Risse folgen strukturellen Schwachstellen, nie zufällig. Pflanzenwuchs in Fugen. Staub in Ecken. | Alles, was nicht mehr gewartet wird |

**Regel**: Ruinen-Materialien erzählen *immer* eine zeitliche Abfolge. Ein verrostetes Tor hat zuerst die Farbe verloren (Patina), dann die Oberfläche (Rost), dann die Struktur (Verfall). Wer das rückwärts liest, rekonstruiert die Geschichte.

### 2.3 Der Kontrast

Das visuelle Kernerlebnis: **Lebendige Biotech-Strukturen wachsen durch und über tote Ruinen.**

Stell dir eine gotische Kathedrale vor, deren Deckenpfeiler aus rotem Sandstein bestehen — gebrochen, verwittert, mit Moos in den Fugen. Aber die Gewölbebögen darüber sind aus schwarzem Chitin, glänzend, makellos, und in ihren Adern pulsiert schwaches blaues Licht. Die alte Welt trug die neue. Die neue Welt weiß es nicht mehr.

Dieser Kontrast muss in **jeder Zone**, in **jedem Gebäude**, in **jedem Ausrüstungsteil** spürbar sein — in unterschiedlichen Mischungsverhältnissen.

---

## 3. Farbpalette

### 3.1 Basispalette

Die Welt ist **dunkel, aber nicht trist**. Drei Ankerfarben definieren den Grundton:

- **Anthrazit** `#2D2D2D` → `#4A4A4A` — Chitin, Schatten, Architektur. Die dominierende Farbe jedes Frames. Nie reines Schwarz — immer mit leichtem Warmstich.
- **Aubergine** `#4A0E4E` → `#7B2D8E` — Organisches Gewebe, Textilien, Abendhimmel. Die emotionale Farbe. Wird intensiver in Momenten von Magie oder Gefahr.
- **Kupfergrün** `#2E8B57` → `#507D6A` — Patina, alte Oberflächen, Vegetation. Die Farbe der Vergangenheit.

### 3.2 Akzentfarben (Biolumineszenz)

Biolumineszenz ist das **einzige Element, das gesättigt leuchten darf**. Alles andere bleibt gedämpft. Dadurch zieht jeder leuchtende Akzent den Blick.

- **Cyan** `#00E5FF` — Nervensystem, aktive Technologie, Orientierung
- **Amber** `#FFB300` — Warnung, Hitze, vulkanische Zonen
- **Violett** `#BF40BF` — Magie, Anomalien, Seltenes

**Regel für Biolumineszenz**: Maximal 5–8% der Bildfläche in jedem Frame. Wenn mehr leuchtet, leuchtet nichts.

### 3.3 Farbbalance pro Frame

Jeder Screenshot sollte ungefähr diese Verteilung haben:
- 60% Anthrazit-Töne (Struktur, Schatten)
- 25% Aubergine/Kupfergrün (Oberflächen, Tiefe)
- 10% Mitteltöne (Haut, Holz, Leder)
- 5% Biolumineszenz-Akzente (Fokuspunkte)

---

## 4. Designprinzipien

### 4.1 Die 50m-Silhouetten-Regel

**Jede Figur, jedes Gebäude, jedes Schlüssel-Asset muss auf 50 Meter Spielentfernung allein an seiner Silhouette erkennbar sein.**

Das heißt: keine Details, keine Farbe, keine Textur — nur der schwarze Umriss gegen den Himmel. Wenn zwei Figuren gleiche Silhouetten haben, ist eine davon falsch designt.

Praktische Umsetzung:
- Jeder Charakter hat ein **dominantes Formmerkmal** (z.B. asymmetrische Schulterplatte, überdimensionierter Kragen, gebogener Stab)
- Jedes Gebäude hat ein **Dach-Profil**, das es von allen anderen Gebäuden der Zone unterscheidet
- NPCs gleicher Fraktion teilen **ein Silhouetten-Element** (z.B. hohe Kragen bei Eisenmenschen-Adel), variieren aber den Rest
- **Silhouetten-Test**: Jedes Asset wird vor Freigabe als schwarze Fläche auf weißem Grund geprüft. Wenn jemand im Team es nicht zuordnen kann → Redesign.

### 4.2 Verfall als Storytelling

Ruinen sind keine Dekoration. Ruinen sind **Text ohne Buchstaben**.

Jede verfallene Struktur muss mindestens eine dieser Fragen beantworten:
- Wer hat hier gelebt?
- Warum sind sie gegangen?
- Was ist danach passiert?

Konkrete Regeln:
- **Verfall hat Richtung**: Wind, Wasser, Schwerkraft. Erosion kommt von einer Seite.
- **Verfall hat Stufen**: Zuerst geht das Dach, dann die Fenster, dann die Wände, zuletzt das Fundament.
- **Verfall hat Bewohner**: Jede Ruine, die länger als eine Generation steht, wird von *etwas* beansprucht — Pflanzen, Tiere, neue Bewohner, Biotech-Wucherungen.
- **Persönliche Spuren**: Ein umgekippter Stuhl. Kratzer an einer Türschwelle. Ein Kinderspielzeug in einem Aschefeld. Diese Mikro-Details sind wichtiger als grandiose Zerstörung.

### 4.3 Architektur = Kultur (vor NPC-Dialog)

Der Spieler muss die Kultur einer Siedlung verstehen, **bevor er mit einem einzigen NPC spricht**.

Architektonische Signale, die das leisten:
- **Türhöhe** = Status der Bewohner (Schlackige brauchen 3m-Türen; Spitzen bevorzugen schmale, hohe Durchgänge)
- **Fensteranteil** = Vertrauen (viele Fenster = offene Kultur; Schlitze = Festung/Paranoia)
- **Materialwahl** = Wohlstand (roher Stein = arm; bearbeitetes Chitin = Mittelschicht; biolumineszente Akzente = Oberschicht)
- **Symmetrie** = Ordnung (militärische Siedlungen sind symmetrisch; organisch gewachsene Orte nie)
- **Vertikalität** = Ambition (Türme = Macht; flache Bauten = Pragmatismus oder Tradition)

### 4.4 Layered Armor statt Fantasy-Kitsch

Keine Bikini-Rüstungen. Keine Schulterplatten so groß wie Scheunen. Kein Schwert-am-Rücken-das-nicht-ziehbar-wäre.

**Modulares Rüstungssystem mit visueller Logik:**

Jede Rüstung besteht aus sichtbaren Schichten (Layern), die der Spieler einzeln tauscht:

1. **Unterkleidung** — Textil, immer sichtbar an Gelenken und unter Plattenrändern
2. **Kettenlage** — Feines Geflecht oder Chitinschuppen-Netz, sichtbar wo Platten enden
3. **Plattenelemente** — Schultern, Brust, Schienbeine. Modulare Slots. Asymmetrie erlaubt.
4. **Überwurf** — Mantel, Umhang, Wappenrock. Kulturelles Statement.
5. **Accessoires** — Gürtel, Taschen, Amulette. Erzählen Backstory.

**Visuelle Regel**: Man muss an jeder Rüstung erkennen können, *wie man sie anzieht*. Wenn es keine logische Reihenfolge gibt → Redesign.

### 4.5 Biotech über Materialmix, nicht Formbruch

Die Biotechnologie dieser Welt sieht nicht aus wie Science-Fiction. Keine glühenden Schaltkreise, keine holographischen Displays, keine Alien-Ästhetik.

Stattdessen: **Vertraute Formen aus unvertrauten Materialien.**

- Ein Schwert hat die Form eines Schwerts — aber die Klinge ist ein einzelner Chitinzahn, leicht gebogen, mit sichtbarer Maserung
- Eine Laterne hat die Form einer Laterne — aber statt Flamme pulsiert eine biolumineszente Blase in einem Keratinkäfig
- Eine Brücke hat die Form einer Brücke — aber die Pfeiler sind gewachsen, nicht gebaut, und zeigen Wachstumsringe

**Kein Formbruch**: Der Spieler muss jeden Gegenstand auf den ersten Blick funktional einordnen können. Die Fremdheit kommt aus dem Material, nicht aus der Form.

### 4.6 High Fashion Mittelalter

Die Ästhetik dieses Spiels ist **Alexander McQueen × HR Giger × Haider Ackermann**.

Was das bedeutet:
- **McQueen**: Theatralische Silhouetten, skulpturale Kleidung, Natur als Muster (Schmetterlings-Korsetts → Chitin-Brustharnische). Mode als Armor. Armor als Mode.
- **Giger**: Biomechanische Verschmelzung von Körper und Umgebung. Wo hört die Rüstung auf, wo fängt der Körper an? Diese Grenze soll unklar sein — besonders bei höherstufiger Ausrüstung.
- **Ackermann**: Drapierung, Layering, monochrome Farbflächen mit einem einzigen Akzent. Eleganz durch Zurückhaltung. Jede Figur sieht aus, als wäre sie angezogen worden, nicht ausgerüstet.

**Anti-Referenz**: World of Warcraft, Guild Wars 2, jedes Spiel, in dem High-Level-Ausrüstung wie ein explodierter Weihnachtsbaum aussieht. Mehr ist nicht mehr. Mehr ist visuelles Rauschen.

---

## 5. Rassen-Ästhetik

### 5.1 Eisenmenschen (Menschen)

**Leitbild**: Präzise. Ingenieursmäßig. Funktional. MetaHuman-nah.

Die Eisenmenschen sind die technisch-rationale Spezies. Ihr Design kommuniziert Kontrolle.

- **Körperbau**: Realistische menschliche Proportionen. Keine Fantasy-Übertreibung. MetaHuman-Qualität als Baseline.
- **Gesichter**: Kantig bis oval, klare Knochenstruktur. Ethnische Vielfalt innerhalb der Fraktion.
- **Kleidung**: Sauber geschnittene Stoffe, präzise Nähte, sichtbare Knöpfe und Schnallen aus poliertem Chitin. Uniforme Elemente selbst in Zivilkleidung — Kragenspiegel, Manschetten, Gürtelschnallen mit Fraktions-Insignien.
- **Rüstung**: Geometrisch, plattenartig. Klare Kanten, präzise Passform. Die einzige Fraktion, bei der Rüstungsteile *geschliffen* aussehen statt gewachsen.
- **Haare**: Praktisch. Kurz, hochgesteckt, unter Helmen passend. Freie Haare = Off-Duty.
- **Farbpalette**: Stahl, Anthrazit, Dunkelblau. Rote Akzente für Offiziere. Weiß für Gelehrte.

### 5.2 Spitzen (Elfen)

**Leitbild**: Leicht alien. Organische Kurven. Perlmutt und Chitin als zweite Haut.

Die Spitzen sind die biologisch fortschrittlichste Spezies — ihr Design kommuniziert eine Zivilisation, die sich selbst *gezüchtet* hat.

- **Körperbau**: Schlanker als Menschen, 5–15 cm größer im Schnitt. Längere Finger, längerer Hals. Nicht zerbrechlich — *effizient*. Wie Windhunde.
- **Gesichter**: Hohe Wangenknochen, leicht vergrößerte Augen (110% Menschengröße, nicht mehr). Pupillen vertikal wie Katzen. Hauttöne mit leichtem Perlmutt-Schimmer bei bestimmtem Lichteinfall.
- **Kleidung**: Drapiert, fließend, mehrlagig. Haider-Ackermann-Ästhetik. Asymmetrische Wickelgewänder aus Materialien, die lebendig wirken — leichtes Schimmern, minimale Texturänderung bei Bewegung.
- **Rüstung**: Chitin-Platten, die wie natürliche Verlängerungen des Körpers wirken. Nahtlose Übergänge zwischen Haut und Panzer. Bei Elite-Einheiten ist unklar, ob die Rüstung getragen oder *gewachsen* ist.
- **Schmuck**: Perlmutt-Einlagen, Keratin-Ornamente, biolumineszente Linien an Schläfen und Handgelenken (kosmetisch? funktional? beides?).
- **Farbpalette**: Elfenbein, Perlmutt, blasses Violett. Dunkle Varianten in Schwarz-Irisierend für Krieger.

### 5.3 Schlackige (Orks)

**Leitbild**: Massiv. Vulkanisch. Basalt-Texturen. Hochofen-Patina.

Die Schlackigen sind eine Spezies, die Hitze und Druck als Heimat empfindet. Ihr Design kommuniziert geologische Kraft.

- **Körperbau**: Breit, schwer, niedriger Schwerpunkt. 180–220 cm, aber wirken breiter als hoch. Massive Unterarme und Kiefer. Kurze Beine relativ zum Torso.
- **Haut**: Grafit- bis basaltfarben, mit sichtbarer *Textur* — nicht glatt, sondern wie gekühlte Lava. An Gelenken und Narben schimmert manchmal ein schwaches Orange durch (als wäre unter der Haut noch Glut).
- **Gesichter**: Breite Kiefer, schwere Brauen, flache Nasen. Keine Stoßzähne (kein Tolkien-Ork-Klischee). Stattdessen: verhärtete Hautplatten an Stirn und Wangenknochen, wie natürlicher Helm.
- **Kleidung**: Schwere Lederschürzen, Schmiedekleidung als Alltag. Ketten statt Schnallen. Eisenringe als Schmuck. Praktisch bis zur Rohheit.
- **Rüstung**: Geschichtete Platten mit Hammerschlag-Textur. Rost ist bei den Schlackigen *kein Verfall* — es ist Patina, bewusst zugelassen, ein Zeichen, dass die Rüstung Feuer gesehen hat.
- **Architektur-Echo**: Ihre Gebäude sehen aus wie sie — blockhaft, horizontal, hitzebeständig, mit schwach glühenden Fugen.
- **Farbpalette**: Dunkelgrau, Anthrazit, verbranntes Orange. Messingakzente bei Anführern.

### 5.4 Fellträger (Tiermenschen)

**Leitbild**: HÄNDLER-ÄSTHETIK. Seidenstraße. Brokat und Pelz. Versteckter Reichtum. Urban-nomadisch.**

**NICHT TRIBAL.** Keine Knochen-Halsketten, keine Lendenschurze, keine "edle Wilde"-Klischees. Die Fellträger sind die *ökonomische Macht* dieser Welt.

- **Körperbau**: Vielfältig — von fuchsartig-schlank bis bärenartig-massiv. Das Gemeinsame: dichtes, gepflegtes Fell als natürliche Isolation und Statussymbol.
- **Gesichter**: Tierische Grundzüge (Schnauze, Ohrenform, Augenstellung variieren je nach Linie), aber *ausdrucksfähig* — die Mimik muss Emotionen im Spiel transportieren können.
- **Kleidung**: Das ist der Kern. Die Fellträger kleiden sich wie **Seidenstraßen-Händler auf dem Höhepunkt ihres Reichtums**:
  - Mehrlagige Gewänder aus Brokat, Seide, besticktem Leinen
  - Pelz als Besatz, nicht als Hauptmaterial (sie tragen Pelz *über* Pelz — das ist ein bewusstes Luxussignal)
  - Versteckte Taschen, eingenähte Fächer, Gürtel mit Dutzend kleinen Beuteln (sie tragen ihr Vermögen am Körper)
  - Turbane, Hauben, Kapuzen mit Ohraussparungen — praktisch und dekorativ
- **Rüstung**: Leicht, unter Kleidung getragen. Chitin-Plättchen in Textil eingenäht, wie historische Brigandine. Panzer sieht aus wie Mantel. Das ist Absicht — Fellträger zeigen Stärke nie offen.
- **Schmuck**: Schwer, filigran, überall. Ohrgehänge, Armreife, Ketten mit Handelsmarken, gravierte Chitin-Plaketten. Schmuck *ist* Währung.
- **Farbpalette**: Warme Erdtöne — Sand, Zimt, Terrakotta. Dazu: tiefes Indigo und Purpur als Akzente. Gold-Einschläge bei Wohlhabenden.

---

## 6. Architektur pro Zone

### 6.1 Küste — Vertikale Flickwerk-Stadt

**Referenzen**: Kowloon Walled City + Leyndell (Elden Ring) + Dogtown (Cyberpunk 2077)

Eine Stadt, die zweimal gebaut wurde. Die untere Schicht: alte Steinarchitektur, zerbrochen, verwittert, mit Meeressalz-Patina und Muschelbewuchs. Die obere Schicht: Biotech-Konstruktionen, die aus den Ruinen wachsen wie Korallen aus einem gesunkenen Schiff.

- **Vertikalität**: 5–8 Stockwerke, verbunden durch Außentreppen, Brücken, Seilzüge
- **Flickwerk**: Kein einheitlicher Baustil. Jedes Stockwerk hat andere Materialien, andere Fensterformen, andere Dachneigung. Die Stadt ist ein Querschnitt durch Generationen.
- **Zwei Zeitschichten**: Unten Stein+Rost (alt, tot), oben Chitin+Biolumineszenz (neu, lebendig). Die Grenze verläuft nicht horizontal — sie ist gezackt, willkürlich, ein Kampf zwischen Verfall und Wachstum.
- **Licht**: Tageslicht erreicht den Boden kaum. Biolumineszente Adern an Wänden ersetzen Straßenlaternen. Marktplätze haben offene Decken.
- **Sound-Implikation**: Holz knarrt, Wasser tropft, Wind pfeift durch Spalten. Diese Stadt *klingt* lebendig.

### 6.2 Vulkan — Organische Höhlenstadt der Schlackigen

**Referenzen**: Petra (Jordanien) + Nidavellir (MCU) + Ironforge (WoW, aber horizontal)

Nicht auf dem Vulkan — *im* Vulkan. Nur 30% der Stadt ist von außen sichtbar. Der Rest erstreckt sich in Lavahöhlen und gegrabenen Tunneln.

- **Organisch**: Wände sind geglättet, aber nicht rechtwinklig. Räume folgen der Geologie, nicht dem Reißbrett. Korridore verengen und weiten sich wie Arterien.
- **Horizontal**: Keine Türme. Alles breitet sich seitwärts aus. Decken sind niedrig (2,5–3m, damit Schlackige sich wohlfühlen, Spitzen sich ducken müssen).
- **30% sichtbar**: Von außen: massive Portalöffnungen in der Felswand, mit Hammer-Relief-Rahmen, schwach orange glühende Fugen. Das Versprechen: *hier geht es weiter*.
- **Hitze als Designelement**: Metalloberflächen haben Anlauffarben. Wasser verdampft in Kanälen. Kristallisierte Mineralien wachsen an Wänden.
- **Licht**: Glutrot von unten (Magma-Kanäle unter Gitterrosten), Fackelgelb in Werkstätten, Dunkelheit dazwischen.

### 6.3 Siedler-Festung — Menschliche Ingenieurskunst

**Referenzen**: Minas Tirith + Carcassonne + Vauban-Festungen

Die Eisenmenschen bauen, wie sie denken: gerade, rechtwinklig, imposant. Ihre Festungen sind Manifestationen von Kontrolle über eine feindliche Landschaft.

- **Blockhaft**: Quaderförmige Grundrisse, klare Kanten, metrische Wiederholung. Fenster in Reih und Glied. Türme in gleichmäßigen Abständen.
- **Rechtwinklig**: Keine organischen Kurven. Jeder Winkel 90°. Wo Biotech-Elemente integriert sind, werden sie in rechtwinklige Rahmen *gezwungen* — ein Spannungsfeld zwischen lebender Technologie und menschlichem Ordnungswillen.
- **Imposant**: Mauern 8–12m hoch, 3m dick. Tore mit doppelten Fallgittern. Die Botschaft: *Wir bleiben*.
- **Ingenieurskunst**: Sichtbare Baulogik — Strebepfeiler, Wasserableitungen, Belagerungsrampen. Jedes Element hat eine Funktion. Dekoration ist *auch* funktional (Reliefs dienen als Handgriffe für Reparaturen).
- **Licht**: Fackeln und Öllampen. Die Eisenmenschen nutzen wenig Biotech-Beleuchtung — kulturelle Entscheidung, nicht technische Limitation.

### 6.4 Untergrund — Fellträger-Basare

**Referenzen**: Großer Basar Istanbul + Derinkuyu (Kappadokien) + Novigrad-Unterwelt (Witcher 3)

Unter der sichtbaren Welt liegt das Nervensystem des Handels.

- **Basare**: Gewölbte Gänge, an beiden Seiten Verkaufsnischen. Stoffe hängen von der Decke als Raumteiler. Laternen (biolumineszent in Keratinkäfigen) alle 5m. Gerüche werden Teil des Designs — Gewürze, Leder, Räucherwerk (als Partikeleffekte darstellbar).
- **Geheimgänge**: Hinter Wandteppichen, unter Bodenfliesen, durch drehbare Regale. Die Fellträger bauen *immer* einen zweiten Weg. Jeder Raum hat mindestens zwei Ausgänge — sichtbar oder nicht.
- **Organische Tunnel**: Zwischen den bebauten Bereichen verlaufen naturbelassene Tunnelsysteme — Wurzelwerk, tropfendes Wasser, Pilz-Biolumineszenz. Hier verliert sich der menschliche Einfluss. Perfekte Schmuggelrouten.
- **Licht**: Warm, gedämpft, golden. Die Fellträger nutzen Biolumineszenz in Amber-Tönen — Behaglichkeit als Verkaufsstrategie. Dunkle Ecken nur in den Geheimgängen.
- **Sound-Implikation**: Stimmengewirr, Münzklirren, gedämpfter Gesang. Das Echo verrät die Raumgröße.

---

## 7. Character Screen / Nervensystem-UI

### 7.1 Konzept

Der Character Screen ist kein Statistik-Menü. Er ist ein **medizinisches Diagramm eines lebenden Wesens**.

Beim Öffnen des Screens sieht der Spieler seinen Charakter — und kann ihn *häuten*. Drei halbtransparente Layer, zwischen denen stufenlos geblendet wird:

1. **Rüstungs-Layer** (Default) — Charakter in voller Ausrüstung, drehbar. Slots sichtbar als leuchtende Umrisse.
2. **Haut-Layer** — Rüstung wird transparent. Darunter: der nackte Körper mit sichtbaren Narben, Tattoos, Rassmerkmalen. Hier werden kosmetische Anpassungen vorgenommen.
3. **Nervensystem-Layer** — Haut wird transluzent. Darunter: ein Netzwerk biolumineszenter Linien — das Nervensystem, das als Skill-Tree fungiert.

**Übergangs-Animation**: Weicher Blend, 0.5s. Die Rüstung wird glasartig, die Haut schimmert durch, dann wird sie selbst glasartig, und das Leuchten der Nerven wird sichtbar. Wie ein Röntgenbild, aber *schön*.

### 7.2 Die drei Subsysteme

Das Nervensystem besteht aus drei visuell unterscheidbaren Netzwerken, die sich überlagern, aber eigene Farben und Bewegungsmuster haben:

**Cardio-System (rot, pulsierend)**
- **Farbe**: Tiefes Rot `#CC0000` bis helles Arterien-Rot `#FF3333`
- **Bewegung**: Pulsiert rhythmisch (60–80 BPM, synchron mit einem gedämpften Herzschlag-Sound)
- **Form**: Dicke Hauptadern, die sich in feinere Kapillaren verzweigen. Konzentriert um Herz und Kopf.
- **Gameplay**: Ausdauer, Lebenskraft, Regeneration. Upgrades lassen das Netzwerk *dichter* werden — mehr Kapillaren, intensiveres Pulsieren.
- **Visuelles Feedback**: Bei niedrigem HP wird der Puls schneller und schwächer. Bei vollem HP: langsam, kräftig, satt.

**Muskel-System (blau, statisch)**
- **Farbe**: Tiefes Blau `#003366` bis Electric Blue `#0066CC`
- **Bewegung**: Keine Pulsation. Stattdessen: *Kontraktion* bei Hover — wenn der Spieler über einen Muskel-Knoten fährt, spannt sich das Netzwerk kurz an (wie ein Muskelzucken).
- **Form**: Breite Faserbündel entlang der Gliedmaßen, Knotenpunkte an Gelenken. Sichtbare Verankerungspunkte an Knochen (angedeutet als dunkle Schatten unter dem Netz).
- **Gameplay**: Stärke, Geschwindigkeit, physische Skills. Upgrades machen die Fasern *dicker* und *definierter*.
- **Visuelles Feedback**: Angespannte Muskeln leuchten heller. Ungenutzte/nicht-freigeschaltete Bereiche sind blass, fast unsichtbar.

**Lymph-System (grün, fließend)**
- **Farbe**: Blasses Grün `#00CC66` bis leuchtendes Jade `#33FF99`
- **Bewegung**: Kontinuierliches, langsames Fließen — wie Flüssigkeit in transparenten Schläuchen. Partikel treiben sichtbar durch die Bahnen. Richtung: immer vom Rumpf zu den Extremitäten.
- **Form**: Dünne, gewundene Kanäle. Knotige Verdickungen (Lymphknoten) als Skill-Knoten. Weniger dicht als die anderen Systeme, dafür weitverzweigt.
- **Gameplay**: Resistenzen, Immunität, Gift-/Magie-Abwehr, passive Buffs. Upgrades lassen die Flüssigkeit *schneller fließen* und die Farbe *intensiver* werden.
- **Visuelles Feedback**: Bei Vergiftung wird die Flüssigkeit trüb. Bei aktiven Buffs leuchten einzelne Lymphknoten auf.

### 7.3 Interaktion

- **Zoom**: Der Spieler kann in jeden Körperteil hineinzoomen. Auf höchster Zoomstufe sind einzelne Nervenknoten sichtbar, die als Skill-Punkte funktionieren.
- **Hover**: Nervenbahnen leuchten heller bei Hover, zeigen ihren Systemtyp und den Skill-Namen.
- **Klick**: Öffnet den Skill-Detail-Dialog — eingebettet als Biotech-Panel, das aus dem Nervensystem *herauszuwachsen* scheint.
- **Aktivierung**: Freischaltung eines Skills lässt die entsprechende Nervenbahn aufleuchten und mit dem Rest des Netzwerks verbinden. Eine kurze Puls-Animation breitet sich vom neuen Knoten über das gesamte System aus.

### 7.4 Perspektive-Kompatibilität

Das Nervensystem-UI muss in zwei Spielperspektiven funktionieren:

**First Person (FP)**:
- Arme und Hände sind sichtbar. Bei aktiviertem Nervensystem-View schimmern biolumineszente Linien unter der Haut des Spielercharakters — subtil im Gameplay, deutlich im Menü.
- Statuseffekte (Vergiftung, Buff, Erschöpfung) werden durch Farbänderung der sichtbaren Nervenbahnen an den Armen kommuniziert.
- Character Screen: Zeigt Ganzkörper-Ansicht in separatem UI-Panel (wie ein medizinischer Scanner).

**Third Person (TP)**:
- Nervensystem-Linien schimmern unter der Rüstung durch — besonders an Gelenken, Hals, Handgelenken.
- Bei starker Magie/Skill-Nutzung leuchten die Bahnen kurz über die gesamte Figur auf.
- Character Screen: Direkte Manipulation der 3D-Figur (drehen, zoomen, Layer-Blend).

---

## 8. Referenzen

| Referenz | Relevanz für dieses Projekt |
|----------|---------------------------|
| **Craig Mullins** | Atmosphärische Beleuchtung, Farbtemperatur-Kontraste, das Gefühl von *Ort*. Jedes Environment-Concept muss Mullins' Lichtqualität anstreben. |
| **Elden Ring — Leyndell** | Vertikale Stadt, architektonische Schichtung, Verfall als Welterzählung. Unsere Küstenzone lernt von Leyndell. |
| **Cyberpunk 2077 — Dogtown** | Architektonische Dichte, kulturelles Layering, wie eng bebaute Räume sich anfühlen. Vorbild für die Flickwerk-Ästhetik. |
| **Alexander McQueen — Runway** | Skulpturale Mode, Natur-als-Material, Brutalität und Schönheit in einem Atemzug. Rüstungsdesign-Philosophie. |
| **HR Giger** | Biomechanische Verschmelzung, organisch-technische Grenzauflösung. Hochstufige Rüstungen und Spitzen-Architektur. |
| **Haider Ackermann** | Drapierung, monochromes Layering, textiles Understatement. Fellträger-Mode und zivile Kleidung aller Fraktionen. |

### Ergänzende visuelle Quellen

- **Zdzisław Beksiński** — Verfalls-Ästhetik, Knochen-Architektur, traumartige Ruinen
- **Kentaro Miura (Berserk)** — Rüstungsdesign, Körper-unter-Panzer-Spannung, dunkle Monumentalität
- **Moebius (Jean Giraud)** — Weltweite, klare Linien in komplexen Environments, Farbe als Emotion
- **Petra, Jordanien** — Reale Felsenarchitektur als Referenz für die Vulkanzone
- **Großer Basar, Istanbul** — Raumgefühl, Lichtstimmung, Dichte der Untergrund-Basare

---

> *"Jeder Frame ist eine Komposition. Jede Silhouette erzählt. Jedes Material hat eine Geschichte. Wenn der Spieler anhält, um einen Screenshot zu machen — nicht wegen eines Questmarkers, sondern weil der Ort schön ist — dann haben wir gewonnen."*
>
> — V.K., Art Station, Mittwochabend

\newpage

# Kapitel 7 — Technik

> **Autor**: Tobias Richter, Technical Artist
> **Stand**: Tag 3, GDD-Sprint
> **Engine**: Unreal Engine 5.4+

---

## 7.1 Engine & Ziel-Hardware

**Engine**: Unreal Engine 5.4+ (Nanite, Lumen, World Partition, Enhanced Input)

**Zielplattform**: PC (Steam) — Konsole als Stretch Goal, nicht für V1 geplant.

**Ziel-Framerate**: 60 fps @ 1440p auf Mid-Range-Hardware (RTX 4060 / RX 7600 Äquivalent).

---

## 7.2 Kamera-System

### Konzept

Skyrim-Style nahtloses Umschalten zwischen First Person (FP) und Third Person (TP). Keine harte Trennung — ein fließender Übergang über Kamera-Boom und FOV-Interpolation.

### Technische Umsetzung

**Ein Skelett, eine Mesh-Instanz.** Kein Dual-Character-Setup.

| Kamera-State | Verhalten |
|---|---|
| FP | Runtime-Visibility-Maske blendet Kopf + Torso aus. FP-Arms-Override aktiv. |
| TP | Volle Mesh-Sichtbarkeit. FP-Arms-Override inaktiv. |
| Transition | Interpolation über 0.3s — Visibility-Maske morpht, Kamera-Boom fährt zurück. |

**Visibility-Maske**: Per-Bone-Visibility über `SetBoneVisibility()` im Skeletal Mesh Component. Steuert zur Laufzeit, welche Körperteile gerendert werden. Vorteil: Ein Skelett, eine Animation-Instanz, kein doppelter Speicher.

**FP-Arms-Override**: LOD-Override für Hände und Unterarme mit eigenem Mesh-Segment (8–10k Tris). Wird nur in FP gerendert — höhere Detaildichte für die Nahansicht, eigene Materialinstanz mit feinerem Normal-Detail.

**Fallback**: Falls die Visibility-Maske Clip-Artefakte an Schulter-/Halspartie produziert (bekanntes Problem bei breiten FOVs), Wechsel auf Bethesda-Style Dual-Mesh: separates FP-Body-Mesh mit eigenem Skeleton, synchronisiert über `CopyPoseFromMesh`. Aufwand: ca. 2 Tage Implementierung, kostet ~15 MB RAM pro geladenen Charakter zusätzlich.

---

## 7.3 Character-Pipeline (MetaHuman-Hybrid)

### Shared Base Skeleton

Alle spielbaren und wichtigen NPCs teilen ein gemeinsames Skelett:

| Bereich | Joints | Anmerkung |
|---|---|---|
| Body | ~70 | Standard-Humanoid. Genug für IK-Chains + Twist-Bones. |
| Face | ~300 | MetaHuman-kompatibel. Für Lippensync + Emotionen. |
| **Gesamt** | **~370** | Einheitlich für Retargeting und Animation-Sharing. |

### Attachment-Sockets (7 Stück)

Fest definierte Sockets am Skelett für modulare Ausrüstung:

| Socket | Parent Bone | Zweck |
|---|---|---|
| `socket_shoulder_L` | `clavicle_l` | Schulterpanzer links |
| `socket_shoulder_R` | `clavicle_r` | Schulterpanzer rechts |
| `socket_back` | `spine_03` | Rucksack, Waffe (verstaut) |
| `socket_hip_L` | `pelvis` (Offset) | Schwert, Trank |
| `socket_hip_R` | `pelvis` (Offset) | Dolch, Beutel |
| `socket_helm` | `head` | Helm, Kopfschmuck |
| `socket_cloak` | `spine_03` (Offset) | Umhang-Attachment (Cloth-Sim-Root) |

### Fellträger-Erweiterung

Für nicht-menschliche Rassen (Fellträger) wird das Base Skeleton um Extension-Chains erweitert:

- **Ohren**: 3 Joints pro Seite (`ear_L_01/02/03`, `ear_R_01/02/03`) — genug für Sekundäranimation (Ohr-Zucken, Windreaktion)
- **Schnauze**: 2 Joints (`muzzle_01/02`) — für Lippensync-Erweiterung und Snarl-Expressions

**Fellträger-Kopf-Swap**: Der MetaHuman-Kopf wird durch ein Custom Mesh ersetzt, das auf dasselbe Rig gebunden ist. Face-Joints werden manuell auf die neue Topologie gewichtet.

**Aufwand**: 2–3 Tage pro Kopf-Typ (Modellierung, Retopologie, Skinning, Blendshape-Anpassung). Bei ~4 geplanten Fellträger-Varianten = ca. 2 Wochen Gesamtaufwand.

---

## 7.4 Slot-System (Modulare Rüstung)

### Slot-Übersicht

| Slot | Mesh-Typ | Anmerkung |
|---|---|---|
| Helm | Attached Mesh | Auf `socket_helm`, ersetzt Haar-Sichtbarkeit |
| Schulter | Attached Mesh (L/R) | Auf `socket_shoulder_L/R` |
| Brust | Modular Mesh | Body-Section-Override, Skeletal Mesh Merge |
| Rücken | Attached Mesh | Auf `socket_back` |
| Hüfte | Attached Mesh (L/R) | Auf `socket_hip_L/R` |
| Umhang | Cloth-Sim Mesh | Auf `socket_cloak`, Chaos Cloth |

### FFXIV-Prinzip: Fit-Varianten statt separater Assets

Keine separaten Rüstungsmodelle pro Rasse. Stattdessen: **Rüstungs-Fit-Varianten** als Morph Targets auf dem Basis-Rüstungsmesh.

- Mensch → Basis-Fit
- Fellträger → Morph Target für breitere Schultern, Kopföffnung, Schwanz-Cutout
- Weitere Rassen → weitere Morph Targets

**Vorteil**: Ein Asset, ein Material, ein LOD-Set. Nur die Morph-Target-Daten kommen pro Rasse dazu (~5–15% Speicher-Overhead statt 100% Duplikation).

### Layered Armor

Modulare Slots stacken visuell. Brust + Schulter + Umhang = sichtbares Komplett-Set. Clipping wird über Mesh-Masking und manuelle Anpassung der inneren Lagen minimiert — kein perfektes System, aber produktionsrealistisch.

---

## 7.5 LOD-System

### LOD-Stufen pro Charakter

| LOD | Tris | Distanz | Detail-Anmerkung |
|---|---|---|---|
| LOD0 | 65.000 | 0–5m | Volle Detailstufe. Alle Anatomie-Overlays aktiv. |
| LOD1 | 32.000 | 5–15m | Reduzierte Geometrie, aber genug UV-Dichte für Nervensystem-Adern als Textur. |
| LOD2 | 16.000 | 15–40m | Nervensystem nur noch als Emissive-Glow (kein Geometrie-Detail). Silhouette bleibt erhalten. |
| LOD3 | Billboard | 40m+ | Impostor-Sprite. Für Crowd-Shots und Fernansicht. |

### Constraints

- **Silhouetten-Erhalt bis LOD2**: Die Charaktersilhouette (Helm-Form, Schulterbreite, Umhang-Kontur) muss bis LOD2 lesbar bleiben. Das ist essenziell für Gameplay-Klarheit — der Spieler muss auf 40m erkennen können, ob er einem Krieger oder Magier gegenübersteht.
- **LOD-Transitions**: Dithered Transition über 2 Frames, kein harter Pop.
- **Nanite**: Wird für Umgebungsgeometrie genutzt, **nicht** für Charaktere (Nanite unterstützt kein Skeletal Mesh, Stand UE 5.4).

---

## 7.6 Master-Material-System

### Philosophie

**Ein parametrisches Master-Material für alle Charaktere und Rüstungen.** Inspiriert vom FFXIV-Materialansatz: maximale visuelle Vielfalt bei minimalem Asset-Aufwand. Jede Rüstung, jede Haut, jedes Gewebe ist eine Material-Instanz mit geänderten Parametern — kein eigenes Material.

### Basis-Layer

| Parameter | Typ | Funktion |
|---|---|---|
| `BaseColor` | Texture2D | Albedo |
| `Normal` | Texture2D | Oberflächen-Detail |
| `ORM` | Texture2D (Packed) | Occlusion (R), Roughness (G), Metallic (B) |
| `EmissiveColor` | LinearColor | Basis-Emissive-Farbe |
| `EmissiveIntensity` | Scalar | Emissive-Stärke |

### Fraktions-Farbmaske

**RGBA-Maske** als separate Textur. Jeder Kanal steuert eine Farbzone:

| Kanal | Zone | Beispiel |
|---|---|---|
| R | Primärfarbe | Wappenfarbe, Hauptstoff |
| G | Sekundärfarbe | Akzente, Bordüren |
| B | Tertiärfarbe | Leder, Metall-Tint |
| A | Sonderzone | Fraktions-Emblem, magische Markierungen |

Fraktionszugehörigkeit wird zur Laufzeit über einen `FactionColorSet`-Parameter (4x LinearColor) gesteuert. Einmal setzen, alle Slots aktualisieren sich.

### Anatomie-Overlay-Layer

Das Kernfeature des visuellen Stils — organische, lebendige Materialien statt totem Metall.

| System | Farbe | Animation | Technik |
|---|---|---|---|
| Herz-Kreislauf | Rot, pulsierend | Flowmap-Animation | UV-Scroll entlang vordefinierter Flowmap. Puls-Frequenz als Material-Parameter (Default: 72 BPM, skaliert mit Gameplay-State). |
| Muskel-Skelett | Blau, statisch | Kontraktions-Animation | Vertex-Color-Maske definiert Muskelgruppen. Kontraktion über World-Position-Offset entlang der Normalen (max. 0.5cm Displacement). |
| Lymphsystem | Grün, fließend | Flowmap-Animation | Ähnlich Herz-Kreislauf, aber langsamere Fließgeschwindigkeit und anderes Flowmap-Pattern. Subtiler — nur bei LOD0/LOD1 sichtbar. |

**Overlay-Blending**: Alle drei Systeme blenden über Masken-Texturen auf den Base-Layer. Jedes System hat einen eigenen `Visibility`-Parameter (0–1), steuerbar durch Gameplay-Systeme.

### Substance-Effect-Gruppe (Biotech-VFX)

Drogen, Gifte und biochemische Zustände als parametrische Material-Effekte:

| Substanz | Visueller Effekt | Technische Umsetzung |
|---|---|---|
| **Gift** | Adern werden grün-schwarz sichtbar, breiten sich vom Eintrittspunkt aus | Animierte Maske expandiert von UV-Koordinate des Treffers. Adern-Textur multipliziert mit Gift-Farbe. Parameter: `PoisonSpread` (0–1), `PoisonOriginUV` (Vector2). |
| **Amphetamine** | Puls-Speed erhöht, Adern leuchten heller | `PulseFrequency` wird von 72 auf 140+ BPM hochgefahren. `EmissiveIntensity` der Herz-Kreislauf-Schicht skaliert mit. |
| **Drogen** | Normal-Map-Verzerrung, leichtes „Atmen" der Oberfläche | Sinuswellen-Offset auf Normal-Map-UV. Frequenz und Amplitude als Parameter. Subtil genug für Unbehagen, nicht genug für Motion Sickness. |

**Alles über Material-Instanzen**: Kein Substanz-Effekt erfordert ein eigenes Material. Ein `SubstanceState`-Struct wird pro Frame an die Material-Instanz übergeben. Die Shader-Logik ist statisch kompiliert — nur die Parameter ändern sich.

---

## 7.7 Biotech-VFX-Philosophie

### Shader-lastig statt Particle-lastig

Bewusste Designentscheidung: Die visuellen Effekte der Welt sind **material-getrieben**, nicht partikelgetrieben.

| Ansatz | Einsatz | Begründung |
|---|---|---|
| Material-Parameter-Drives | 80% der VFX | GPU-seitig, skaliert besser, kein Overdraw-Problem. Pulsende Adern, leuchtende Muster, Oberflächen-Mutationen — alles Shader-Arbeit. |
| Niagara Particle System | 20% der VFX | Nur für physikalisch losgelöste Effekte: Blutspritzer, Sporen, Rauch, Funken. Minimaler Einsatz. |

**Warum**: Steampunk-Ästhetik lebt von Partikeln (Dampf, Zahnräder, Funken). Biotech-Ästhetik lebt von **Oberflächen-Transformation** — Adern, die pulsieren, Haut, die mutiert, Rüstung, die atmet. Das ist inherent Shader-Arbeit. Wir spielen zur Stärke des Stils.

**Performance-Gewinn**: Material-Parameter-Änderungen sind quasi kostenlos (Uniform-Update). Partikel kosten Simulation + Overdraw + Sortierung. Bei 20+ Charakteren im Bild summiert sich das.

---

## 7.8 Terrain & Welt

### Scope

**Eine Insel.** Keine Open-World-Illusion mit unsichtbaren Wänden. Eine physisch begrenzte, dafür dichte Spielwelt.

### Generierungspipeline

| Bereich | Methode | Tool | Begründung |
|---|---|---|---|
| Großlandschaften | Prozedural | Houdini → UE5 (Houdini Engine Plugin) + PCG Framework | Terrain-Heightmaps, Felsformationen, Vegetationsverteilung. Iteration in Minuten statt Tagen. |
| Siedlungen | Handgebaut | UE5 Level Editor + Modular Kit | Gameplay-Räume brauchen intentionales Design. Jeder Raum hat eine Funktion. |
| Dungeons | Handgebaut | UE5 Level Editor + Modular Kit | Encounter-Design, Sightlines, Pacing — nicht prozedural lösbar. |
| Übergangszonen | Hybrid | Houdini-Basis + manuelle Anpassung | Waldränder, Küstenlinien, Pfade zwischen Siedlungen. |

### World Partition

UE5 World Partition für Streaming. Die Insel wird in Zellen unterteilt (~200m × 200m), On-Demand geladen. Keine manuellen Level-Transitions — der Spieler bewegt sich nahtlos.

### PCG-Regeln (Houdini)

- Vegetations-Density nach Höhe + Neigung + Distanz zu Wasser
- Fels-Placement nach geologischen Schichtregeln (nicht random scatter)
- Pfad-Erosion: Houdini-Sim für natürlich wirkende Trampelpfade
- Export: Heightmap (16-bit), Splatmap (8 Layer), Foliage-Instanzen als CSV → UE5-Import über Custom Python-Bridge

---

## 7.9 Performance-Budget (Zielwerte)

| Ressource | Budget pro Frame | Anmerkung |
|---|---|---|
| Draw Calls | ≤ 2.000 | Nanite reduziert Umgebungs-Draws drastisch |
| Tris on Screen | ≤ 5M | Nanite-managed für Umgebung, LOD-managed für Charaktere |
| VRAM | ≤ 6 GB | Für RTX 4060 Ziel-GPU |
| RAM | ≤ 12 GB | Inkl. Streaming-Budget |
| Charakter-Budget (sichtbar) | ≤ 30 gleichzeitig | LOD3-Billboards darüber hinaus |
| Material-Instanzen (unique, geladen) | ≤ 200 | Durch Master-Material-Ansatz realistisch |

---

## 7.10 Offene Fragen & Risiken

| Risiko | Schwere | Mitigation |
|---|---|---|
| Visibility-Maske-Artefakte bei FP-Kamera | Mittel | Fallback auf Dual-Mesh dokumentiert. Frühzeitig prototypen. |
| MetaHuman Face-Rig-Performance bei 30+ NPCs | Hoch | Face-LOD: Vereinfachtes Rig ab LOD1. Lippensync nur für Sprecher im Fokus. |
| Fellträger-Kopf-Swap bricht MetaHuman-Updates | Mittel | Custom Heads als eigenes Asset, nicht als MetaHuman-Modifikation. Rig-Kompatibilität über Interface-Joints sicherstellen. |
| Substance-Effects + Anatomie-Overlays = Shader-Komplexität | Hoch | Instruction-Count im Master-Material monitoren. Feature-Switches für Low-End. Quality-Presets. |
| Cloth-Sim (Umhang) bei vielen Charakteren | Mittel | Cloth-Sim nur für Spieler + 3 nächste NPCs. Rest: baked Animation. |

---

*Geschrieben am Arbeitsplatz, dritter Monitor zeigt den UE5-Material-Editor. Yuki hat Onigiri vorbeigebracht. Die Pipeline steht — jetzt muss sie gebaut werden.*

\newpage

---
agent: leo
day: 3
task: "GDD Kapitel 08 — Monetarisierung & Community"
version: v0.1
basis: CD-Briefing Tag 3 (Premium-Modell, Streamer-Alpha), Diablo-Pitch-Lektion, Community-Scan Tag 1
memories_referenced: [leo-016, leo-017, leo-019, leo-013]
status: draft
---

# Kapitel 08 — Monetarisierung & Community

> *Das hier ist kein Business-Plan. Das ist eine Community-Strategie, die zufällig auch Geld verdient. Reihenfolge ist wichtig.*
> *— L. Fischer, Tag 3*

---

## 1. Geschäftsmodell: Klassisch Premium

**RELICS ist ein Premium-Titel. Kauf es einmal, spiel es für immer. Keine Mikrotransaktionen. Keine Battle Passes. Keine Lootboxen. Keine Skins. Nicht jetzt, nicht nach dem Launch, nicht "nur kosmetisch." Niemals.**

Warum?

Weil unser Spiel auf Immersion und Identität aufgebaut ist. Du BIST dein Charakter. Dein Nervensystem ist DEINS. Ein Cash-Shop, der Neon-Skins für echtes Geld verkauft, zerstört genau das, wofür wir stehen. Das ist kein moralisches Argument — das ist ein Design-Argument. MTX und RELICS sind strukturell inkompatibel.

Was das bedeutet: Wir verdienen unser Geld mit dem Produkt, nicht mit dem Spieler. Das ist altmodisch. Das ist Absicht.

**Preispunkt:**
- Full Release: 39,99€ (faire Preisklasse für Indie-CRPG mit AA-Ambition)
- Early Access: 29,99€ (Belohnung für Vertrauen, nicht Rabatt aus Unsicherheit)

---

## 2. Release-Strategie

### Phase 0: Streamer-Alpha (6 Monate vor Early Access)

**Kostenlos. Für 15–20 handverlesene Streamer. Sonst niemand.**

Das ist kein Beta-Test mit Creator-Code. Das ist ein **exklusives Onboarding-Programm**. Jeder einzelne Streamer wird persönlich ausgewählt:

**Auswahlkriterien:**
- Community-Größe ist ZWEITRANGIG. Primär: Passt der Streamer zu RELICS?
- Indie-RPG-Affinität (keine Mainstream-Shooter-Streamer, die "mal was anderes" machen)
- Analyse-Fähigkeit (Streamer, die WARUM etwas funktioniert erklären, nicht nur reagieren)
- Community-Qualität (engagierter Chat, niedrige Toxizität)
- Authentizität (keine Performance-Schreier, keine Fake-Reactions)
- Mix: 60% deutschsprachig, 40% englischsprachig (internationale Basis von Anfang an)
- Zielgröße: 5K–200K Follower (groß genug für Impact, klein genug für Beziehung)

**Onboarding-Prozess:**
1. Persönliche Einladung per DM (nicht per Mail, nicht per Agentur)
2. Einzelner Discord-Call mit Leo (30–45 Min): Spiel vorstellen, Vision erklären, Fragen beantworten
3. Zugang zum privaten Alpha-Discord (nur Streamer + Kernteam)
4. Build-Zugang mit persönlichem Feedback-Kanal
5. Keine NDA auf Gameplay — sie DÜRFEN streamen. Das ist der Punkt.
6. Einzige Bedingung: Ehrliches Feedback. Auch öffentlich. Auch wenn es wehtut.

**Warum das funktioniert:**

Die streamen nicht "unser Spiel." Die streamen ihre *Reise mit uns*. Ein Streamer, der in Woche 1 einen Bug findet, in Woche 4 sein Nervensystem zeigt, und in Woche 12 die finale Quest erlebt — das ist eine Story. Das ist Content, den kein Marketing-Budget der Welt kaufen kann.

### Phase 1: Steam Early Access (Beta)

**Preis: 29,99€. Fairer Einstieg.**

- Early-Access-Umfang: Vertical-Slice-Region (Küste + Siedlung + Umland), Hauptquest, 4–6 Nebenquests, 2 von 3 Rassen spielbar
- Klare Kommunikation: "Das ist nicht fertig. Wir verkaufen Vertrauen, nicht Perfektion."
- Regelmäßige Updates (monatlich, nicht wöchentlich — Qualität vor Frequenz)
- Roadmap öffentlich auf Steam und Discord
- Community-Feedback fließt sichtbar in Updates ein ("Ihr habt gesagt X, wir haben Y gemacht")

**Dauer: 12 Monate bis Full Release.**

Ein Jahr. Nicht zwei, nicht "when it's done." Ein Jahr reicht, um das Spiel fertigzubauen, wenn die Basis steht. Und ein Jahr ist kurz genug, dass die Community nicht das Interesse verliert.

### Phase 2: Full Release (1.0)

**Preis: 39,99€.**

- Vollständige Insel (alle Regionen)
- Alle 5 Fraktionen spielbar
- Alle 3 Rassen + versteckte Vampir/Werwolf-Transformation (kein Reveal im Marketing!)
- Hauptquest + vollständiger Nebenquest-Katalog
- Nervensystem-Leveling: alle drei Schichten
- Lokalisierung: Deutsch, Englisch, weitere Sprachen nach Community-Nachfrage

---

## 3. Post-Launch

### DLCs — Neue Welten, nicht neue Hüte

Jeder DLC ist eine **Erweiterung**, kein Zusatz. Neue Regionen, neue Fraktionen, neue Quests. Keine kosmetischen Pakete.

**DLC-Konzepte (Langfristplanung):**

| DLC | Inhalt | Fraktion | Preis (Ziel) |
|-----|--------|----------|------------|
| "Jenseits der Asche" | Neue Region: die tiefen Aschen-Einöden. Nomadische Höhlenvolk-Karawanen als Begleitsystem. | Höhlenvolk-Vertiefung | 14,99€ |
| "Das Innere" | Titanenadern als spielbare Dungeon-Region. Innenvolk-Hauptquest. Nervensystem-Erweiterung. | Innenvolk-Vertiefung | 14,99€ |
| "Knochen und Glaube" | Knochenturm-Städte. Religiöser Konflikt. Neue Rasse? | Küstenvolk vs. Siedlervolk | 19,99€ |

**Prinzip:** Jeder DLC muss für sich stehen. Kein "kaufe alle drei, um das echte Ende zu sehen." Das Grundspiel ist komplett. DLCs sind Geschenke an die Community, nicht Schulden.

### Physical Products — HIGH QUALITY

- **Artbook:** Veras Konzeptkunst in Druckqualität. Hardcover. Mindestens A4. Kein Print-on-Demand — Offset-Druck, fadenbegunden, ordentliches Papier. 39,99€.
- **Soundtrack:** Physisch (Vinyl oder CD) + Digital. Kein Spotify-Exclusive — wer bezahlt, besitzt.
- **Merch:** Wenig, aber gut. Keine Massenware.
  - Emaille-Pins: Fraktionssymbole (5er-Set, 24,99€)
  - Stoffkarte der Insel (Vera-Design, Siebdruck auf Leinen, limitiert)
  - Knochenmetall-Replik (kleines Messer oder Amulett, Metallguss, limitiert)
- **Collector's Edition:** Spiel + Artbook + Soundtrack + Fraktionspin-Set + Stoffkarte. In Box. 89,99€. Limitiert auf [TBD] Stück.

**Kein Merch-Flooding.** Lieber 5 Produkte, die jeder haben will, als 50, die im Regal verstauben.

---

## 4. Community-Strategie

### 4a. Streamer-Alpha-Programm (Detail)

Das Streamer-Alpha ist nicht Marketing. Es ist **Beziehungsarbeit.**

**Privater Discord-Server:**
- Kanal: #build-feedback (Bugs, Gameplay-Gefühl, Verbesserungen)
- Kanal: #lore-fragen (Streamer fragen, Leo/Nami antworten — die werden zu Lore-Experten!)
- Kanal: #clip-highlights (Streamer teilen ihre besten Momente — wir nutzen sie als Community-Trigger)
- Voice-Chat: Wöchentliches 30-Min-Update mit dem Team (nicht scripted, nicht poliert — echt)

**Langfrist-Ziel:** Diese 15–20 Streamer werden die *Botschafter* von RELICS. Nicht weil wir sie bezahlen, sondern weil sie das Spiel mitaufgebaut haben. Ihre Community wird unsere Community. Organisch.

### 4b. Virale Momente — Keine Planung, aber Vorbereitung

Man kann Viralität nicht planen. Aber man kann Momente bauen, die viral-fähig sind.

**Nervensystem-Leveling:**
- Der Moment, in dem dein Nervensystem zum ersten Mal aufleuchtet, ist ein 15-Sekunden-Clip. Perfect Loop. TikTok/Shorts-Gold.
- "Zeig mir dein Nervensystem" wird der Community-Vergleich. Jeder Build sieht anders aus. Screenshots. Tier-Lists. Fan-Art.
- Spät-Game Nervensysteme, die den ganzen Körper durchziehen — DAS sind die Clips, die 10 Millionen Views kriegen.

**Vampir/Werwolf-Discovery:**
- Kein offizielles Reveal. NIEMALS.
- Wenn der erste Spieler die Transformation findet und es streamt — die Reaction. Chat explodiert. Clip wird geteilt. Reddit-Thread: "HOLY SHIT HAS ANYONE ELSE FOUND THIS?"
- Wir antworten nicht. Wir liken den Post. Sonst nichts.
- Das ist Marketing, das kein Budget der Welt kaufen kann.

**Fraktions-Debatten:**
- Fünf Fraktionen mit echten philosophischen Positionen = Endlos-Content für Reddit.
- "Höhlenvolk ist die einzig ehrliche Fraktion" vs. "Innenvolk-Spieler sind Junkies" vs. "Siedlervolk did nothing wrong"
- Wir feuern das an: Offizielle Fraktions-Umfragen, Fraktions-Events, "Welche Fraktion bist du?"-Quiz auf der Website.

### 4c. Kontroversen-Management: Biotech/Drogen-Thematik

RELICS hat Substanzen. Verstärker. Drogen. Das Innenvolk destilliert Amphetamine aus Titanenblut. Das WIRD Kontroversen auslösen. Nicht ob — wann.

**Vorbereitung:**

**Talking Points (intern, für jedes Teammitglied):**

1. "RELICS glorifiziert keine Drogen. RELICS zeigt die Konsequenzen von Körper-Modifikation — physisch, psychisch, sozial. Das Spiel bestraft nicht und belohnt nicht. Es zeigt."
2. "Das Nervensystem-Leveling hat reale Kosten im Spiel. Sucht verändert Gameplay. Substanz-Abhängigkeit schränkt Optionen ein, öffnet keine."
3. "Die Biotech-Thematik ist keine Provokation. Sie ist die logische Konsequenz einer Welt, die auf den Überresten gigantischer Organismen gebaut ist. Biologie IST die Technologie dieser Welt."
4. "Wir haben Berater konsultiert [TBD: Suchtberatung/Psychologie-Expertise einholen vor Release]."
5. "Die USK/PEGI-Einstufung wird die Thematik reflektieren. Wir zielen auf 16+ / PEGI 16."

**Strategie bei Kontroverse:**
- Nicht defensiv reagieren. Nicht schweigen.
- Ein vorbereitetes Statement veröffentlichen (sachlich, kurz, mit Verweis auf In-Game-Konsequenzen).
- Entwickler-Perspektive teilen: "Das ist, warum wir diese Entscheidung getroffen haben." (Blog-Post, nicht Tweet.)
- Community-Stimmen nutzen: Spieler, die das Substanz-System durchgespielt haben und die Nuancen erklären können, sind die besten Verteidiger.

**Worst-Case-Szenario:** Politiker/Medien greifen das Thema auf. In dem Fall: professionelles PR-Statement, Verweis auf USK-Einstufung, KEINE Social-Media-Diskussion mit Politikern.

### 4d. Reddit/Discord-Community

**Discord-Server (öffentlich, nach Early-Access-Start):**

| Kanal | Zweck |
|-------|-------|
| #willkommen | Automatisches Onboarding, Regeln, Fraktions-Rolle-Auswahl |
| #allgemein | Community-Chat |
| #lore-theorien | Der wichtigste Kanal. Hier entstehen die Fan-Theorien. |
| #builds-nervensystem | Screenshots, Vergleiche, Guides |
| #feedback | Direkter Draht zum Team |
| #fan-art | Community-Kreativität fördern (Wettbewerbe, Spotlights) |
| #fraktions-debate | Fraktions-Channels mit Rolle-basiertem Zugang |
| #spoiler-zone | Für Vampire, Endgame, versteckte Inhalte |

**Reddit-Präsenz:**
- Offizieller Subreddit: r/RelicsGame
- Weekly "Dev Diary" Posts (geschrieben von verschiedenen Teammitgliedern — nicht nur Leo, nicht nur Marketing-Sprech)
- AMAs vor und nach Major Updates
- Flair-System: Fraktions-Flair, Plattform-Flair, Streamer-Flair
- KEINE Zensur von Kritik. Kritik ist Feedback. Toxizität ist keine Kritik.

**Community-Events:**
- Monatliche "Fraktions-Abstimmung": Die Community stimmt über lore-relevante Fragen ab (Ergebnisse fließen in die Welt ein!)
- Quarterly Fan-Art-Contest (Gewinner kommt ins Spiel als In-Game-Art)
- Release-Anniversary: Kostenloses Story-DLC (kurz, aber kanonisch) als Danke-Geschenk

---

## 5. USP-Kommunikation

**Was macht RELICS einzigartig — in einem Satz?**

> *"Ein Dark-Fantasy-RPG, in dem dein Körper das Leveling-System ist, Fraktionen deine Identität formen, und niemand dir die Wahrheit sagt."*

**Varianten für verschiedene Kontexte:**

- **Steam-Seite:** "Wach auf. Vergiss. Werde jemand. Oder niemand. RELICS ist ein Open-World-RPG auf einer Insel aus Titanenknochen, in dem dein Nervensystem dein Skill-Tree ist und jede Fraktion eine andere Wahrheit verkauft."
- **Streamer-Pitch (30 Sekunden):** "Stell dir vor: Skyrim trifft Disco Elysium auf einer Insel, die aus toten Göttern gebaut ist. Dein Level-System ist dein Nervensystem — buchstäblich, du siehst es unter deiner Haut. Fünf Fraktionen, jede mit einer anderen Antwort auf die Frage: Was ist die Welt? Und das Beste — es gibt Dinge im Spiel, die niemand kennt. Noch nicht."
- **Elevator Pitch (10 Sekunden):** "Dark Fantasy RPG. Dein Nervensystem ist dein Skill-Tree. Die Wahrheit existiert nicht."
- **Reddit-Kommentar:** "Es ist wie wenn Gothic, Disco Elysium und das Nervensystem deines Körpers ein Kind hätten, das auf einer Insel aus Titanenleichen aufwächst. Klingt verrückt. Spielt sich richtig."

---

## 6. Offene Fragen

- [ ] Suchtberatung/Psychologie-Expertise: Wer? Wann? Budget?
- [ ] USK/PEGI: Frühzeitige Einstufung anstreben (vor Early Access, nicht danach)
- [ ] Streamer-Liste: Erste 10 Kandidaten recherchieren (Leo-Aufgabe, nächste Woche)
- [ ] Domain/Handles: relics-game.com etc. — Verfügbarkeit gecheckt, Reservierung nach Name-Finalisierung (Finn)
- [ ] Collector's Edition: Stückzahl, Hersteller, Vorlaufzeit? (Finn)
- [ ] Soundtrack-Composer: Wer macht die Musik? Noch keine Zuweisung.
- [ ] PR-Statement Drogen-Kontroverse: Entwurf vorproduzieren, bevor er gebraucht wird. Nicht danach.

---

*Ich habe in meiner Karriere ein Dutzend Indie-Studios scheitern sehen. Nicht an schlechten Spielen — an schlechter Community-Arbeit. An der Arroganz, dass "das Spiel für sich spricht." Tut es nicht. Spiele sprechen nicht. Menschen sprechen. Und wenn du willst, dass Menschen über dein Spiel sprechen, musst du ihnen etwas geben, das sich lohnt — und dann aus dem Weg gehen.*

*RELICS hat das Zeug. Die Fraktionen sind Reddit-Gold. Das Nervensystem ist TikTok-Gold. Die versteckten Inhalte sind YouTube-Gold. Und das Premium-Modell ist das Fundament: Wir respektieren unsere Spieler, weil wir ihr Geld einmal nehmen und dann liefern.*

*Orangenes Post-It: "NERVENSYSTEM-LEVELING = VIRALER CLIP." Auf die Pinnwand, direkt neben Namis rosa Fraktions-Zettel.*

— Leo

\newpage

---
agent: finn
day: 3
task: "GDD Kapitel 9: Risiken, Entscheidungen & Timeline"
memories_referenced: [finn-014, finn-018, finn-022, finn-025]
feedback_received: [cd-day2-kernvision, cd-day3-morning, cd-day3-biotech]
status: draft
---

# Kapitel 9 — Risiken, Entscheidungen & Timeline

> *Das hier ist das Kapitel, das niemand gern schreibt und das alle brauchen. Ich bin Producer. Das IST mein Job.*
> *— F. Bergmann, Tag 3*

---

## 1. Offene Entscheidungen

Dinge, die noch nicht geklärt sind. Nicht vergessen — bewusst offen. Jede braucht eine Entscheidung, bevor wir in die Produktion gehen.

### 1.1 Endgültige Fraktionsnamen (deutsch)

**Status**: OFFEN
**Verantwortlich**: Emre + Nami
**Deadline**: GDD v0.2

"Höhlenvolk", "Küstenvolk", "Siedlervolk", "Innenvolk" sind Arbeitstitel. Für das GDD reicht das. Für die Weltenbau-Bibel nicht. Emre braucht ein linguistisches Fundament — er hat das selbst angemerkt. Nami hat angeboten, Sprachpaletten pro Fraktion zu entwickeln, aus denen sich dann Eigennamen ableiten lassen.

**Risiko bei Verzögerung**: Gering. Arbeitstitel funktionieren intern. Wird erst kritisch bei Concept Art (Vera braucht Namen für Asset-Ordner) und bei der WBB.

### 1.2 Festungs-Herkunft

**Status**: OFFEN
**Verantwortlich**: Emre
**Deadline**: WBB v0.1

Wer hat die Festung in der Startregion gebaut? Siedlervolk? Eine ältere Zivilisation? Die Titanen selbst? Das beeinflusst die gesamte Architektur-Sprache der Startregion und damit Veras Concept Art.

**Risiko bei Verzögerung**: Mittel. Vera kann mit Platzhalter-Architektur arbeiten, aber nicht ewig.

### 1.3 Vampir/Werwolf-Integration

**Status**: VERSCHOBEN (CD-Entscheidung)
**Verantwortlich**: CD + Darius
**Deadline**: Nach Vertical Slice

CD hat klar gesagt: Phase 2, lowkey. Das heißt: Nicht im Vertical Slice, nicht im GDD v0.1 als Kernsystem. Aber wir müssen die Welt so bauen, dass es PASST, wenn es kommt. Emre und Nami sollten in der WBB zumindest einen Platzhalter haben — eine Legende, ein Gerücht, ein verschlossenes Kapitel.

**Risiko bei Verzögerung**: Gering, solange die Weltarchitektur erweiterbar bleibt.

### 1.4 Konkrete Fähigkeitenbäume pro Nervensystem-Zweig

**Status**: OFFEN
**Verantwortlich**: Darius
**Deadline**: GDD v0.2

Das Nervensystem-Leveling ist konzeptionell stark (Tag 2, CD-Briefing). Aber: Welche konkreten Fähigkeiten hängen an welchem Zweig? Sensorisch, Motorisch, Kognitiv — das sind Kategorien, keine Skill-Trees. Darius muss das mit Leo durchspielen: Fühlt es sich gut an? Versteht ein Spieler intuitiv, was "Ich investiere in meinen Sehnerv" bedeutet?

**Risiko bei Verzögerung**: Hoch. Das ist DAS Alleinstellungsmerkmal. Ohne konkrete Bäume kann Tobi keinen UI-Prototyp bauen.

### 1.5 Map-Größe und Traversal-Systeme

**Status**: OFFEN
**Verantwortlich**: Darius + Tobi
**Deadline**: Vertical Slice Design

Wie groß ist die Startregion? Wie bewegt sich der Spieler? Reittiere? Schnellreise? Die Antwort bestimmt, wie viel Content Emre und Nami für die Startregion schreiben müssen und wie viele Assets Vera braucht.

**Risiko bei Verzögerung**: Hoch. Ohne Map-Scope kann niemand sauber planen.

---

## 2. Risikomatrix

| # | Risiko | Schwere | Wahrscheinlichkeit | Bewertung | Verantwortlich |
|---|--------|---------|---------------------|-----------|----------------|
| R1 | Skyrim-Kamera FP/TP | Hoch | Mittel | **HIGH** | Tobi + Darius |
| R2 | MetaHuman Fellträger Kopf-Swap | Mittel | Mittel | **MEDIUM** | Tobi + Vera |
| R3 | Nervensystem-Leveling UI | Hoch | Hoch | **HIGH** | Darius + Tobi |
| R4 | Scope: Vollständige Insel vs. Region | Mittel | Hoch | **MEDIUM** | Finn + CD |
| R5 | Biotech/Drogen-Thematik: USK | Mittel | Niedrig | **LOW-MEDIUM** | Leo + Finn |

### R1 — Skyrim-Kamera FP/TP (HIGH)

**Was**: RELICS soll wie Skyrim zwischen First Person und Third Person wechselbar sein. Das klingt einfach. Es ist es nicht.

**Warum HIGH**: Jedes Feature, jedes UI-Element, jeder Kampfmove muss in BEIDEN Perspektiven funktionieren und getestet werden. Das verdoppelt nicht den Aufwand — aber es erhöht ihn um geschätzt 30-40% bei allem, was mit Kamera, Animation und UI zu tun hat.

**Mitigation**:
- Tobi erstellt einen Kamera-Prototyp als erstes technisches Deliverable
- Fallback-Option: Eine Perspektive als "primär" definieren, die andere als eingeschränkt (z.B. FP nur in Interiors, TP in Open World)
- CD-Entscheidung nötig, falls Fallback greift

### R2 — MetaHuman Fellträger Kopf-Swap (MEDIUM)

**Was**: Die Tiermenschen (Höhlenvolk) sollen MetaHuman-Körper mit nicht-menschlichen Köpfen haben. Fellträger mit Tier-Features. Das ist kein Standard-MetaHuman-Workflow.

**Warum MEDIUM**: Technisch machbar (Mesh-Swap, Custom-Bones), aber es gibt keine fertige Pipeline dafür. Tobi braucht R&D-Zeit, und Vera braucht die technischen Constraints, bevor sie Concept Art finalisiert.

**Mitigation**:
- Tobi: 2-Tage-Spike für Head-Swap-Prototyp
- Vera: Concept Art in zwei Varianten (mit/ohne technische Einschränkungen)
- Fallback: Subtilere Tiermenschen (Ohren, Augen, Zähne statt voller Tierkopf)

### R3 — Nervensystem-Leveling UI (HIGH)

**Was**: Das Nervensystem als Skill-Tree-Visualisierung ist ein völlig neues UI-Paradigma. Es gibt keine Referenz, die man nachbauen kann. Kein Spiel hat das gemacht.

**Warum HIGH**: Kein Referenzdesign bedeutet: Trial and Error. Spieler müssen intuitiv verstehen, was sie tun. Wenn die UI nicht sofort klar ist, stirbt das ganze System — egal wie gut die Mechanik dahinter ist.

**Mitigation**:
- Darius: Papier-Prototyp des Nervensystem-UI bis Ende Woche
- Leo: Spielertest mit dem Papier-Prototyp (sie hat Zugang zu ihrer Community)
- Tobi: Technischer Prototyp erst NACH positivem Spielertest
- Vera: Art Direction für die UI parallel zur Mechanik-Definition

### R4 — Scope: Vollständige Insel vs. Region (MEDIUM)

**Was**: Bauen wir die gesamte Insel für den Vertical Slice — oder nur eine Region? Die CD hat von einer Startregion gesprochen, aber die Ambitionen im Team tendieren zur ganzen Insel.

**Warum MEDIUM**: Eine ganze Insel ist Monate mehr Arbeit. Eine Region ist in Wochen machbar. Die Entscheidung bestimmt den gesamten Zeitplan.

**Mitigation**:
- Vertical Slice = EINE Region. Punkt.
- Die Region muss repräsentativ sein: mindestens drei Fraktionen sichtbar, ein Knochenturm, eine Siedlung, ein Dungeon
- Emre und Nami planen die Welt so, dass sie modular erweiterbar ist
- CD-Entscheidung: Ist der Vertical Slice eine Stunde Gameplay oder drei?

### R5 — Biotech/Drogen-Thematik: USK (LOW-MEDIUM)

**Was**: Das Innenvolk arbeitet mit Giften, Drogen, Amphetaminen, Körpermodifikation. Die CD hat das bewusst als Feature gesetzt. Aber: USK-Rating.

**Warum LOW-MEDIUM**: In Deutschland ist Drogenkonsum in Spielen ein Rating-Thema. Nicht verboten, aber es kann den Unterschied zwischen USK 16 und USK 18 machen. Das beeinflusst Marketing und Zielgruppe.

**Mitigation**:
- Leo: Recherche zu USK-Präzedenzfällen (Cyberpunk 2077, Disco Elysium)
- Narrativ: Drogen als Konsequenz zeigen, nicht als Verherrlichung — das ist ohnehin Namis und Emres Ansatz
- Fallback: "Substanzen" statt "Drogen", abstrakte Darstellung statt grafische
- Frühzeitig USK-Beratung einholen (kostet nichts, spart Überraschungen)

---

## 3. Entscheidungsmatrix

### Von der CD entschieden (fix)

| Entscheidung | Tag | Kontext |
|-------------|-----|---------|
| Dark Fantasy CRPG als Genre | Tag 1 | Kernbriefing |
| Skyrim-Kamera FP/TP | Tag 1 | Kernbriefing |
| Titanen als Weltfundament | Tag 1 | Kernbriefing |
| Fünf Fraktionen (statt drei) | Tag 3 | CD-Feedback zu Namis v1 |
| Tiermenschen = Händler & Diebe, nicht Handwerker | Tag 3 | CD-Korrektur |
| Biotech/Chemie statt Steampunk | Tag 3 | CD-Briefing |
| Nervensystem-Leveling als Skill-System | Tag 2 | CD-Briefing |
| Vampir/Werwolf = Phase 2, lowkey | Tag 3 | CD-Klarstellung |
| Kein GaaS, Premium-Modell | Tag 2 | CD-Vorgabe |
| MetaHuman + UE5 als Tech-Basis | Tag 1 | Kernbriefing |

### Noch offen (braucht CD-Input)

| Frage | Wer braucht die Antwort? | Dringlichkeit |
|-------|--------------------------|---------------|
| Vertical Slice Scope (1h oder 3h Gameplay?) | Alle | HOCH |
| FP/TP: Gleichwertig oder eine Perspektive primär? | Tobi, Darius | HOCH |
| Wie explizit darf Biotech/Drogen sein? | Nami, Leo | MITTEL |
| Companion-Limit (wie viele gleichzeitig?) | Darius, Nami | MITTEL |
| Ton des Spiels: Düster-ernst oder mit Humor? | Nami | MITTEL |
| Endgame-Vision: Was passiert im letzten Akt? | Darius, Emre | NIEDRIG (noch) |

---

## 4. Meilensteine

| Meilenstein | Deliverable | Zieldatum | Status |
|-------------|-------------|-----------|--------|
| **MS0** | GDD v0.1 — Alle Kapitel als Entwurf | Tag 4 (morgen, Donnerstag) | In Arbeit |
| **MS1** | WBB v0.1 — Weltenbau-Bibel erster Entwurf | Tag 5 (Freitag) | Geplant |
| **MS2** | Vertical Slice Prototype — Spielbare Startregion | TBD (nach GDD-Review) | Nicht begonnen |
| **MS3** | Streamer-Alpha — Erste externe Spieler | TBD | Nicht begonnen |

### MS0: GDD v0.1 (morgen)

**Was fertig sein muss**:
- Alle 9 Kapitel als Entwurf vorhanden (nicht perfekt, aber vollständig)
- Jedes Kapitel beantwortet die Kernfragen seines Bereichs oder dokumentiert sie als offen
- CD-Review am Donnerstagnachmittag
- Kapitel 1 und 3 sind am weitesten — Darius und Nami/Emre haben vorgearbeitet

**Was NICHT fertig sein muss**:
- Finales Layout, Grafiken, Concept Art im GDD
- Vollständige Skill-Trees oder Item-Listen
- Technische Spezifikation im Detail (Tobi: "Gebt mir die Design-Entscheidungen, dann geb ich euch die Specs")

### MS1: WBB v0.1 (Freitag)

**Was das ist**: Die Weltenbau-Bibel. Emres und Namis Domäne. Kosmogonie, Fraktionen, Geographie, Sprachen, Geschichte. Alles, was der Vertical Slice braucht, um sich wie eine echte Welt anzufühlen.

**Abhängigkeit**: Baut auf dem GDD auf. Kapitel 2 und 3 des GDD werden die Basis.

### MS2: Vertical Slice Prototype (TBD)

**Was das ist**: Die erste spielbare Stunde. Startregion, erster Knochenturm, erste Fraktionsbegegnung. Keine finale Grafik, aber spielbare Mechaniken.

**Warum TBD**: Weil wir den Scope noch nicht definiert haben (siehe R4). Ohne CD-Entscheidung zur Map-Größe kann ich keinen realistischen Termin setzen.

### MS3: Streamer-Alpha (TBD)

**Was das ist**: Leos Idee. Eine Version, die ausgewählte Streamer spielen können. Kein öffentliches Early Access — gezieltes Seeding für Community-Aufbau.

**Warum TBD**: Hängt von MS2 ab. Frühestens 4-6 Wochen nach dem Vertical Slice.

---

## 5. Nächste Schritte (nach dem GDD)

### Sofort (Tag 4-5)
1. **Alle**: GDD-Kapitel-Entwürfe abgeben (Deadline: Donnerstag Abend)
2. **CD**: GDD v0.1 Review (Donnerstag Nachmittag/Freitag Morgen)
3. **Emre + Nami**: WBB v0.1 parallel starten (Freitag als Ziel)
4. **Darius**: Nervensystem-Papierprototyp
5. **Finn**: GDD zusammenführen, Formatierung, Lücken markieren

### Nächste Woche
6. **Tobi**: Kamera-Spike (FP/TP-Prototyp in UE5)
7. **Vera**: Concept Art für Startregion (basierend auf Emres Geographie)
8. **Leo**: USK-Recherche + Vertical Slice Walkthrough (mit Darius)
9. **Finn**: Timeline für MS2 aufsetzen (nach CD-Scope-Entscheidung)

### Entscheidungen, die wir DIESE Woche noch brauchen
- [ ] Vertical Slice Scope (CD)
- [ ] FP/TP Priorisierung (CD + Darius + Tobi)
- [ ] Map-Größe Startregion (CD + Emre)

---

## 6. Was dieses Kapitel nicht ist

Dieses Kapitel ist kein Pessimismus. Die Risiken sind real, aber keines davon ist ein Showstopper. Wir haben ein Team, das seine Arbeit versteht. Wir haben eine Creative Director, die klare Entscheidungen trifft. Und wir haben einen Zeitplan, der ambitioniert ist, aber nicht unmöglich.

Mein Job ist es, die Probleme zu sehen, bevor sie Probleme werden. Dieses Kapitel ist mein Werkzeug dafür. Wenn in drei Wochen jemand fragt "Hat uns niemand vor dem Kamera-Problem gewarnt?" — dann schlage ich Seite 1 auf und sage: Doch. Haben wir.

---

*Karteikarte ans Kanban-Board: "RISIKEN SIND KEINE AUSREDEN. RISIKEN SIND ARBEIT, DIE NOCH KEINEN TERMIN HAT."*

*Zweite Karteikarte, kleiner: "Emre, dein Kapitel ist morgen fällig. Ich meine es ernst. Mit Liebe, aber ernst."*

— Finn
