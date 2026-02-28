---
title: "RELICS"
subtitle: "Game Design Document — Dark Fantasy CRPG"
author: "GenSoftworks"
date: "v0.3"
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
  - \fancyhead[L]{RELICS — GDD v0.3}
  - \fancyhead[R]{GenSoftworks}
  - \fancyfoot[C]{\thepage}
---

# RELICS — Game Design Document

**Dark Fantasy CRPG**

Version: v0.3
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

## Kapitel-Übersicht

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

\newpage

# Kapitel 01 — Kernvision & Core Loop

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

Freie Bewegung durch eine offene, handgefertigte Welt. Kein prozeduraler Füllstoff. Jeder Ort existiert, weil er eine Geschichte erzählt oder ein Gameplay-Ziel hat.

**Designregeln**:
- **Keine Fragezeichen auf der Karte.** Der Spieler erkundet, weil die Welt ihn einlädt — nicht, weil ein Icon blinkt.
- **Sichtlinien als Leitsystem.** Knochentürme sind von überall sichtbar — Orientierung, Lore und Gameplay-Ziel zugleich.
- **Vertikale Exploration.** Klettern ist Kernbewegung. Tiefe (Titanenadern, unterirdische Labore) und Höhe (Knochenturmspitzen, Klippenöden).
- **Dichteprüfung**: Max. 90 Sekunden ohne interessanten Kontaktpunkt.

### 1.3.2 BEGEGNEN

Kontaktpunkte zwischen Spieler und Welt. Nicht nur Kampf — Begegnungen sind NPCs, Umwelträtsel, Fraktions-Checkpoints, Entdeckungen, Gerüchte, Fallen.

**Designregeln**:
- **NPCs haben Tagesabläufe.** Der Schmied arbeitet tagsüber und trinkt abends. Der Händler des Höhlenvolks ist nur bei Neumond da. Wer die Rhythmen kennt, hat Vorteile.
- **Begegnungen eskalieren basierend auf Ruf.** Nicht "Freund/Feind", sondern ein Spektrum.
- **Zufallsbegegnungen mit Logik.** Kein Bandit im Vakuum. Banditen operieren an Handelsrouten, Wölfe jagen nahe Wasserquellen. Die Welt folgt ökologischen und ökonomischen Regeln.
- **Stille als Begegnung.** Ein leeres Dorf. Ein frisch ausgehobenes Grab. Stille erzählt Geschichten.

### 1.3.3 HANDELN

Jede Begegnung hat mindestens zwei Handlungsoptionen. Keine davon ist "die richtige."

**Designregeln**:
- **Drei Säulen des Handelns**: Gewalt, Verhandlung, Subversion. Jede Begegnung muss mindestens zwei der drei unterstützen.
- **Keine moralische Bewertung durch das Spiel.** Kein Karma-System. Die Welt reagiert — das Spiel urteilt nicht.
- **Wissen als Handlungsoption.** Wer die Lore kennt, hat Dialogoptionen, die andere nicht haben.
- **Unterlassung ist eine Handlung.** Ein NPC bittet um Hilfe. Der Spieler geht weiter. Der NPC stirbt — oder überlebt allein und erinnert sich.

### 1.3.4 KONSEQUENZ

Die Welt reagiert auf Spielerhandlungen. Nicht sofort, nicht immer sichtbar, aber immer real.

**Designregeln**:
- **Sofortige + verzögerte Konsequenzen.** Ein Mord hat sofortige Folgen (Wachen, Ruf-Verlust) UND verzögerte (die Familie des Opfers drei Stunden später, die Quest-Linie, die sich schließt).
- **Konsequenzen sind nicht binär.** Einem Händler des Höhlenvolks zu helfen verbessert den Ruf bei Händlern, verschlechtert ihn beim Siedlervolk, und ist dem Küstenvolk egal.
- **Konsequenz-Kaskaden.** Große Entscheidungen haben Fernwirkungen. "Ich habe den Schmied nicht gerettet. Jetzt hat das Dorf keine Waffen. Jetzt gibt es kein Dorf mehr."
- **Erinnerung ist Konsequenz.** NPCs vergessen nicht. Das Gedächtnis der Welt ist lang.
- **Physische Konsequenz.** Ein niedergebranntes Dorf bleibt niedergebrannt. Die Welt akkumuliert die Spuren des Spielers.

---

## 1.4 Spieler-Fantasie

### "Ich bin ein Fremder. Ich bin Niemand. Und genau deshalb kann ich alles werden."

Der Spieler beginnt als Tabula Rasa — keine Klasse, kein Stand, keine Zugehörigkeit. In einer Welt voller Fraktionen und Identitäten ist der Spieler der einzige Mensch, der frei ist. Freiheit als Fluch und Geschenk.

- "Ich bin Niemand, und die Welt zwingt mich, jemand zu werden"
- "Jede Fraktion will mich für sich — aber keine will mich als Gleichen"
- "Ich baue mir meinen Ruf aus dem Nichts — durch Taten, nicht durch Titel"

---

## 1.5 Tonalität

### Low Fantasy. Germanische Mythologie. Bodenständig mit Spice.

**Low Fantasy**: Magie ist selten, teuer und gefährlich. Monster haben einen ökologischen Platz. Politik ist wichtiger als Prophezeiungen.

**Germanische Mythologie**: Nicht Marvel-Wikinger. Echte, ambivalente Mythologie. Titanen als Ymir-Parallele — aus dem Fleisch des Urwesens wird die Welt gebaut. Ehre ist relativ: Was das Siedlervolk "Fortschritt" nennt, nennt das Höhlenvolk "Raub".

**Bodenständig mit Spice**: Die Basis ist Dreck, Schweiß und Pragmatismus. Der Spice ist das Unerklärliche — ein Knochenturm, der bei Berührung summt, ein Fluss aus titanischem Blut, der nie gerinnt. Nicht Game of Thrones (zu zynisch), nicht Lord of the Rings (zu edel).

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

- **Kein Open-World-Füllstoff.** Keine Ubisoft-Türme, keine kopierten Camps.
- **Kein Auserwählten-Narrativ.** Der Spieler ist ein Mensch in einer Welt, die ihn nicht braucht.
- **Kein Moralsystem.** Keine Gut/Böse-Achse. Die Welt reagiert — sie bewertet nicht.
- **Kein Steampunk.** Biotech. Chemie. Körper.
- **Kein Power-Fantasy-Endgame.** Kompetent, nicht allmächtig. Gothic, nicht Diablo.
- **Keine Handholding-UI.** Kein Quest-Kompass, keine glühenden Pfade.

\newpage

# Kapitel 2: Die Welt von RELICS

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

\newpage

# Kapitel 3: Welt & Fraktionen

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

**Rasse**: Tiermenschen — humanoid mit tierischen Merkmalen (Fell, Ohren, Nachtsicht). Varianten: fuchsartig, dachsartig, fledermausartig.

**Weltsicht**: Die Welt ist ein Marktplatz. Alles hat einen Preis. Wert wird verhandelt, nicht zugewiesen.

**Zone**: Die Unterwelt (Zone 5), mit Knotenpunkten unter jeder Oberflächenzone.

**Identität**: Distribution. Das Höhlenvolk produziert fast nichts — es BEWEGT alles. Erz, Kräuter, Information. Währung ist Vertrauen und Schulden. Monopol: Tunnelnetz-Wissen. Karawanen-Clans statt Dörfer. Seidenstraßen-Ästhetik unter der Erde.

**Konfliktlinie**: Kontrolle vs. Freiheit. Die Festung will regulieren, das Höhlenvolk will handeln. Handel/Schmuggel-Grenze ist fließend.

**Spieler-Relevanz**: Zugang zu seltenen Waren, Schwarzmarkt, Informationsnetzwerk. Tauschhandel und Gefälligkeiten statt Gold. Langfristiger Handel verbessert Angebote.

**Mythologische Wurzel**: Edda-Zwerge — dekonstruiert als Händler statt Schmiede.

---

### II. DAS KÜSTENVOLK — *"Die Welt wartet auf Deutung."*

**Rasse**: Elfisch-inspiriert — hochgewachsen, blass, langlebig (150+ Jahre). Lichtempfindliche Augen. Akademisch, leicht entrückt.

**Weltsicht**: Die Welt ist ein Text. Jedes Relikt, jede Gesteinsschicht ist ein Zeichen. Die Vergangenheit ist realer als die Gegenwart.

**Zone**: Die Küste (Zone 1) — Häfen, Leuchtturm-Akademien, Ruinen.

**Identität**: Seehandel und Wissensmonopol. Kartographie, Übersetzung, Archivierung. Akademien als Machtbasis. Vertikale Flickwerk-Architektur — jede Generation baut eine Etage drauf. Gaudí trifft Fischerdorf.

**Konfliktlinie**: Vergangenheit vs. Fortschritt (gegen Siedlervolk). Produzieren keine Nahrung — abhängig vom Hinterland.

**Spieler-Relevanz**: Lore-Zugang, Relikt-Identifikation, Seehandel. Wissen als Währung. Drei Schlüssel-NPCs (Nornen-Echo) führen in die Weltgeschichte ein — und widersprechen sich.

**Mythologische Wurzel**: Die Nornen am Brunnen Urds. Odin opfert sein Auge für Wissen.

---

### III. DAS SIEDLERVOLK — *"Die Welt gehört dem, der sie nimmt."*

**Rasse**: Menschen. Keine übernatürlichen Merkmale. Ethnisch vielfältig — verbunden durch Ideologie, nicht Blut.

**Weltsicht**: Die Welt ist Ressource. Fortschritt legitimiert sich selbst. Stillstand ist Rückschritt.

**Zone**: Die Festung und das Hinterland (Zonen 3 und 4). Größte territoriale Ausdehnung.

**Identität**: Landwirtschaft, Handwerk, Verwaltung. Größte Bevölkerung. Gilden-Oligarchie. Blockhaft-rechtwinklige Architektur — Rothenburg ob der Tauber, funktional statt pittoresk. Beschriften die Welt: Straßennamen, Verordnungen, Preislisten.

**Konfliktlinie**: Anspruch auf Führung durch Besatzung der Festung (die sie nicht gebaut haben). Abhängig von Rohstoff-Importen. Meritokratie als Ideologie, Nepotismus als Praxis.

**Spieler-Relevanz**: Dominante politische Macht, Questgeber-Hub, regulierter Markt. Vertragsbasierte Kultur — Vertragsbruch ist das größte Tabu.

**Mythologische Wurzel**: Die Asen — Götter der Ordnung. Bauen auf Fundamenten, die sie nicht verstehen.

---

### IV. DAS INNENVOLK — *"Der Körper ist die letzte Grenze."*

**Rasse**: Rassenübergreifend. Keine biologische Gruppe, sondern eine ideologische. Verbunden durch Praxis: Selbstexperiment.

**Weltsicht**: Die Wahrheit liegt im Körper, nicht in der Welt. Der Körper erinnert sich an Dinge, die der Geist vergessen hat.

**Zone**: Kein festes Territorium — loses Netzwerk über alle Zonen. Schwerpunkte: Vulkanland (Rohstoffe), Unterwelt (Labore), Festung (Absatzmarkt).

**Identität**: Produktion von Biotech-Substanzen: Verstärker (*Sporen*), Gifte (*Tinkturen*), Drogen (*Tiefstoffe*), Heilmittel (*Balsame*). Meister-Schüler-Struktur. Initiation durch Selbstversuch. Giger trifft mittelalterliche Apotheke. "Destillateure" ist die Berufsbezeichnung innerhalb der Fraktion.

**Konfliktlinie**: Parasitär-symbiotisch mit der Festung — offiziell verboten, inoffiziell Hauptkunde. Labore tarnen sich als "Apotheken."

**Spieler-Relevanz**: Quelle des Nervensystem-Levelings. Substanzen als mächtiges aber riskantes Werkzeug. Sucht als Gameplay-Konsequenz. Zugang zu verstecktem Wissen.

**Mythologische Wurzel**: Die Völva (Seherin durch Trance). Odins Selbstopfer am Weltenbaum — Wissen durch Selbstverletzung.

---

### V. DIE ZERBROCHENEN — *"Ich bin, was übrig bleibt."*

**Rasse**: Alle. Keine Ethnie, keine Organisation. Ein **Zustand**. Exilierte, Überläufer, Entwurzelte, Fremde.

**Zone**: Überall und nirgends. Armenviertel *die Scherben* in der Festung (offiziell nicht existent).

**Identität**: Keine eigene Architektur, keine Sozialstruktur. Improvisierte Lager, umfunktionierte Ruinen. Manche hochqualifiziert, aber ohne Netzwerk wertlos.

**Spieler-Relevanz**: **Der Spielercharakter startet als Zerbrochener.** Ohne Zugehörigkeit, ohne Geschichte. Der gesamte Spielverlauf ist der Prozess, von Zerbrochen zu Zugehörig zu werden — oder bewusst zerbrochen zu bleiben. Companions kommen überproportional aus dieser Gruppe.

**Mythologische Wurzel**: Der Wanderer Odin in Verkleidung. Figuren, die erst herausfinden müssen, wer sie sind.

---

## 3.3 Die Festung

Zentraler Hub der Spielwelt. Plateau leicht südlich der Inselmitte, Sichtlinien zu allen Zonen. Groß genug für eine Stadt, alt genug für Geheimnisse.

**Herkunft**: Unbekannt. Das ist kein Plothole — das ist der Plot. Älter als jedes Archiv, passt zu keiner bekannten Kultur. Gebaut aus *Grundstein* — schwarzer Stein, glatter als Obsidian, härter, mit Spuren organischer Verbindungen.

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

Keine Dampfmaschinen, keine Zahnräder. Technologie ist **biologisch** — gewachsen, destilliert, fermentiert. Das ist ein Designprinzip, das jede Textur, jedes Item, jede Werkbank betrifft.

**Produktionskette**: Schwellstellen (Vulkan) → Rohmaterial → Höhlenvolk-Distribution → Innenvolk-Labore → Vier Kategorien: Verstärker (Sporen), Gifte (Tinkturen), Drogen (Tiefstoffe), Heilmittel (Balsame).

**Nervensystem-Leveling**: Im Worldbuilding verankert, nicht nur UI-Mechanik. Das Innenvolk hat entdeckt, dass der Körper "Schichten" hat, die durch Tiefstoffe sichtbar und trainierbar werden. Die Leveling-UI ist IN DER SPIELWELT eine Innenvolk-Technik.

**Sucht-Mechanik**: Lymphsystem trackt Belastung in 5 Stufen (Sauber → Zerbrochen). Stufe 4 erzwingt Fraktionswechsel zu den Zerbrochenen. Details in Kapitel 4.

---

## 3.5 Germanische Mythologie — Wie sie in der Welt lebt

Germanische Mythologie ist **kein Setting-Dressing**. Götter existieren nicht (oder es gibt keine Beweise). Mythen sind Erklärungsversuche — Low Fantasy, germanisch, dekonstruiert. Nie aufgelöst: Der Spieler findet Hinweise in beide Richtungen.

**Fünf mythologische Schichten**:
1. **Ymir**: Insel als Riesenkörper. Schwellstellen = Adern. Vulkan = letzter Atemzug. Hauptquest-Treiber.
2. **Nornen**: Drei Schlüssel-NPCs an der Küste (Lesende, Spinnende, Schneidende). Widersprechen sich absichtlich.
3. **Odin**: Spielercharakter als Wanderer-Echo. Nervensystem-Leveling als Selbstopfer-Parallele.
4. **Ragnarök**: Biologische Eskalation als Ticking Clock — Schwellstellen werden aktiver, Festung zeigt Risse.
5. **Loki**: Grenzüberschreitung als Prinzip. Innenvolk verkörpert dies am stärksten.

| Motiv | Gläubige Deutung | Rationale Deutung | Design-Einsatz |
|---|---|---|---|
| Ymir | Insel ist Riesenkörper | Geologische Formation | Environmental Storytelling |
| Nornen | Schicksalsfrauen | Akademikerinnen | Quest-NPCs |
| Odin | Wanderer kehrt zurück | Fremder mit Fragen | Spielercharakter-Echo |
| Ragnarök | Welt endet im Feuer | Vulkan eskaliert | Hauptquest Ticking Clock |
| Loki | Verwandlungsgott | Biotech verändert Körper | Innenvolk-Quests |
| Midgardschlange | Etwas lebt unter der Insel | Tektonische Verwerfungen | Festungs-Mysterium |

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

Für den Vertical Slice: **die Festung und ihr unmittelbares Umland** als Startregion.

**Aktive Fraktionen**: Siedlervolk (dominant), Höhlenvolk (Händler-Karawane), Küstenvolk (Akademie-Außenstelle)

**Angedeutete Fraktionen**: Innenvolk (eine "Apotheke", ein NPC), Zerbrochene (die Scherben als begehbares Armenviertel)

**Hauptquest-Hook**: Der Spieler kommt als Fremder zur Festung. Der Kern ist verschlossen. Jemand will ihn öffnen. Jemand will ihn versiegelt lassen.

\newpage

# Kapitel 04 — Gameplay-Systeme

---

## 4.1 Kamera-System

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

**Universalregel: Jedes System muss in BEIDEN Perspektiven funktionieren.** Kein Feature ohne FP- und TP-Äquivalent.

| System | FP-Lösung | TP-Lösung |
|--------|-----------|-----------|
| Nervensystem-Leveling | Halbtransparente Körper-Overlay auf Screen | Kamera zoomt auf Charakter, Körper wird transparent |
| Dialog | Gesicht des NPC im Fokus, Blickkontakt | Over-the-Shoulder, Kamera zwischen Spieler und NPC |
| Kampf | Waffe/Schild sichtbar, physisches Gefühl | Vollkörper-Animation, Footwork sichtbar |
| Klettern | Hände greifen, visuelles Feedback, Höhenangst | Charakter-Silhouette gegen Umgebung, Routenplanung |
| Substanz-Effekte | Visuelle Verzerrung, Farbverschiebung | Charakter-Animation (Taumeln, Zittern), Partikeleffekte |

---

## 4.2 Combat-System

Real-Time Action Combat. Gewichtig, taktisch, positionsbasiert. Näher an Dark Souls als an Diablo, zugänglicher als Sekiro. Jeder Schwerthieb kostet Ausdauer, jeder Block hat ein Timing-Fenster, jeder Gegner hat erkennbare Muster.

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

**Schilde**: Aktive Waffe, nicht passive Ausrüstung. Schildstoß, Schildschlag, aktives Blocken (Parry), passives Blocken (Ausdauer-Drain). Varianten: Rundschild (mobil), Turmschild (stationär), Buckler (Parry-fokussiert).

### Kampf-Prinzipien

1. **Gewicht**: Jede Aktion hat Momentum und Recovery-Frames. Kein Abbrechen mid-Swing.
2. **Ausdauer als Universalwährung**: Angriff, Block, Dodge, Sprint kosten Ausdauer. Kein Buttonmashing.
3. **Positionierung**: Rückenangriffe, Flanken, Höhenvorteil, Engpässe als taktische Elemente.
4. **KI mit Absicht**: Jeder Gegnertyp hat eine erkennbare Kampfdoktrin:
   - **Banditen**: Aggressiv in Gruppen, fliehen bei Überzahl-Verlust
   - **Siedlervolk-Soldaten**: Formation, Schildwall
   - **Höhlenvolk-Krieger**: Gift an Klingen, Hit-and-Run
   - **Innenvolk-Wächter**: Chemisch verstärkt, unberechenbar
   - **Wildtiere**: Instinktbasiert, territorial

---

## 4.3 Leveling — Das Nervensystem

Halbtransparente Körpervisualisierung als Skill-System. Diegetisch: Das Innenvolk hat entdeckt, dass der sterbliche Körper Titanenspuren in seinen Zellen trägt. Wer sich verbessert, aktiviert schlafende biologische Kapazitäten.

### Die drei Systeme

#### 4.3.1 Herz-Kreislauf / Atmungssystem

**Visuell**: Rotes Netzwerk, pulsierend. **Regelt**: Ausdauer-Pool, Sprint-Dauer, Unterwasser-Atmen, Erholung, Höhenresistenz. **Steigerung durch**: Laufen, Klettern, Schwimmen — das System wächst durch Benutzung.

#### 4.3.2 Muskel-Skelett-System

**Visuell**: Weißes Skelett, rot-braune Muskelstränge. **Regelt**: Tragkraft (physisches Gewicht), Nahkampfschaden, Kletterreichweite, Waffenvoraussetzungen, physische Einschüchterung (NPCs reagieren auf sichtbare Masse). **Steigerung durch**: Nahkampf, schweres Tragen, Klettern, körperliche Arbeit.

#### 4.3.3 Lymphsystem

**Visuell**: Grün-gelbes Netzwerk, fließend. **Regelt**: Gift-/Krankheitsresistenz, **Substanz-Toleranz** (Kernmechanik), passive Regeneration, Narbenbildung. **Steigerung durch**: Vergiftungen überleben, Krankheiten durchstehen, kontrollierte Substanznutzung.

**Die Substanz-Schleife** (emergentes Gameplay):

```
Substanz einnehmen → Temporärer Boost
                   → Lymphsystem-Belastung
                   → Wenn Belastung > Toleranz:
                       → Sucht-Stufe steigt
                       → Entzugserscheinungen
                       → Langzeit: permanente Debuffs
```

Starkes Lymphsystem = kontrollierter Substanzeinsatz. Schwaches Lymphsystem + Substanzen = russisches Roulette. Wer nur die Substanzen nimmt ohne Innenvolk-Training, endet zerbrochen.

---

## 4.4 Substanzen — Chemie als Gameplay

Mittelalterliche Biochemie statt Steampunk. Titanengewebe ist chemisch aktiv. Das Innenvolk hat gelernt, daraus Substanzen zu gewinnen, die den Körper verändern.

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

**Chemische Reaktionen**: Substanzen interagieren nach interner Logik. Kombinationen erzeugen Synergien (Aschetinktur + Lymphwasser = verstärkte Heilung), Überdosen (Graukristall + Titanen-Adrenalin = Unverwundbarkeit + Bewusstlosigkeit), oder Halluzinationen. Lymphwasser dient als universelles Gegenmittel (30-Sekunden-Fenster).

---

## 4.5 Rüstung & Ausrüstung — Modulares Slot-System

Modulares Slot-System. Keine Rüstungs-Sets mit festen Boni. Einzelne Teile zum Kombinieren und Modifizieren. High Fashion Mittelalter.

### Slots

8 Slots: Kopf, Schultern, Torso, Arme, Beine, Füße, Rücken (Umhang/Rucksack/Köcher), Accessoire (Gürtel/Kette/Talisman).

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

Jedes Rüstungsteil modifizierbar: Verstärkung (Schutz/Gewicht), Polsterung, Substanz-Beschichtung (Gift-Resistenz, Kälteschutz), Fraktions-Insignien (ändert NPC-Reaktionen), Tarnung.

---

## 4.6 Einschüchterung & Soziale Mechaniken

Keine abstrakten Charisma-Checks. Die Welt reagiert auf den GESAMTEN Spieler — Ausrüstung, Ruf, physische Erscheinung, Taten, Fraktionszugehörigkeit. Kein separates System, sondern ein Layer über allem.

**Drei Eingabefaktoren**: Physische Präsenz (Muskel-Skelett-Stufe, Rüstung, sichtbare Waffen, Narben), Reputation (lokal, Fraktions-Ruf, spezifische Taten, Gerüchte), Kontext (Tageszeit, Territorium, Zahlenverhältnis).

**NPC-Reaktions-Spektrum** (nicht binär):

| Reaktion | Trigger | NPC-Verhalten |
|----------|---------|---------------|
| Verachtung | Schwach, kein Ruf | Ignoriert, beleidigt |
| Gleichgültigkeit | Unauffällig | Standard-Interaktion |
| Respekt | Kompetent, guter Ruf | Bessere Preise, Hinweise |
| Furcht | Stark, gewalttätiger Ruf | Kooperiert sofort |
| Panik | Massaker-Ruf, blutverschmiert | Flieht oder ergibt sich |
| Trotz | Einschüchternd, aber NPC hat Prinzipien | Weigert sich trotz Angst |

---

## 4.7 Wirtschaftssystem

Drei Wirtschafts-Schichten mit eigenen Währungen, Regeln und Konsequenzen:

**Tier 1 — Legaler Handel (Siedlervolk)**: Aschenmark als Währung. Feste, regional unterschiedliche Preise. Standard-Waren verfügbar, Substanzen/Knochenmetall/Gifte nicht. Marktsteuer finanziert das Siedlervolk — Handel ist politisch.

**Tier 2 — Händlernetzwerk (Höhlenvolk)**: Tausch und Versprechen statt Geld. Handelt mit ALLEM. Seltene Materialien, Substanzen, Informationen. Kein Verbraucherschutz. Loyalität wird belohnt, Betrug bestraft.

**Tier 3 — Schwarzmarkt**: Netzwerk aus Kontakten und Codewörtern. Gifte, militärische Ausrüstung, Auftragsmorde. Zugang durch kriminellen Ruf oder Höhlenvolk-Kontakte. Erwischtwerden = Ruf-Verlust, Verhaftung.

**Dynamik**: Angebot und Nachfrage reagieren auf Spieleraktionen. Wirtschaft IST Politik.

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

\newpage

# Kapitel 05 — Vertical Slice Walkthrough

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

\newpage

# Kapitel 06 — Art Direction

---

## 1. Visuelle Identität: Biotech-Mittelalter

Technologie wurde nie mechanisch, sondern biologisch. Statt Maschinen: gezüchtete Organismen. Statt Schaltkreisen: Nervenbahnen. Statt Stahl: Chitin. Ästhetik zwischen gotischer Kathedrale und lebendem Korallenriff.

**Leitgedanke**: Das Mittelalter, industrialisiert mit CRISPR statt mit dem Webstuhl.

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

| Rasse | Leitbild | Körperbau | Farbpalette | Rüstungs-Stil |
|-------|----------|-----------|-------------|---------------|
| **Eisenmenschen** (Menschen) | Präzise, funktional, MetaHuman-nah | Realistische Proportionen, ethnisch vielfältig | Stahl, Anthrazit, Dunkelblau | Geometrisch, plattenartig, geschliffen |
| **Spitzen** (Elfen) | Alien, organisch, Perlmutt | Schlank, 5–15cm größer, vertikale Pupillen | Elfenbein, Perlmutt, blasses Violett | Chitin-Platten als Körperverlängerung, Haider-Ackermann-Drapierung |
| **Schlackige** (Orks) | Massiv, vulkanisch, Basalt | Breit, 180–220cm, Haut wie gekühlte Lava | Dunkelgrau, verbranntes Orange | Hammerschlag-Platten, Rost als Patina |
| **Fellträger** (Tiermenschen) | Seidenstraßen-Händler, NICHT tribal | Vielfältig (fuchsartig bis bärenartig) | Sand, Zimt, Terrakotta, Indigo | Leichte Chitin-Brigandine unter Brokat, Schmuck ist Währung |

---

## 6. Architektur pro Zone

| Zone | Referenzen | Kernmerkmale | Licht |
|------|-----------|--------------|-------|
| **Küste** | Kowloon + Leyndell + Dogtown | Vertikales Flickwerk, 5–8 Stockwerke. Unten Stein+Rost, oben Chitin+Biolumineszenz. Generationen-Schichtung. | Biolumineszente Adern statt Laternen |
| **Vulkan** | Petra + Nidavellir | *Im* Vulkan. 30% sichtbar. Horizontal, niedrige Decken. Wände folgen Geologie. Hitze als Designelement. | Glutrot von unten, Fackelgelb in Werkstätten |
| **Festung** | Minas Tirith + Vauban | Blockhaft, rechtwinklig, imposant. Mauern 8–12m, 3m dick. Biotech in rechtwinklige Rahmen gezwungen. | Fackeln und Öllampen (kulturelle Entscheidung) |
| **Untergrund** | Großer Basar Istanbul + Derinkuyu | Gewölbte Basare, Amber-Biolumineszenz. Jeder Raum hat mindestens zwei Ausgänge. Organische Tunnel als Schmuggelrouten. | Warm, gedämpft, golden |

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

| Referenz | Relevanz |
|----------|----------|
| Craig Mullins | Atmosphärische Beleuchtung, Farbtemperatur-Kontraste |
| Elden Ring — Leyndell | Vertikale Stadt, Verfall als Welterzählung |
| Alexander McQueen | Skulpturale Mode, Natur-als-Material |
| HR Giger | Biomechanische Verschmelzung, organisch-technische Grenzauflösung |
| Haider Ackermann | Drapierung, monochromes Layering |
| Beksiński | Verfalls-Ästhetik, Knochen-Architektur |
| Kentaro Miura (Berserk) | Rüstungsdesign, dunkle Monumentalität |

\newpage

# Kapitel 7 — Technik

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

\newpage

# Kapitel 08 — Monetarisierung & Community

---

## 1. Geschäftsmodell: Klassisch Premium

Premium-Titel. Keine Mikrotransaktionen, keine Battle Passes, keine Lootboxen. MTX und RELICS sind strukturell inkompatibel — das Spiel baut auf Immersion und Identität.

**Preispunkt:**
- Full Release: 69,99€
- Early Access: 29,99€

---

## 2. Release-Strategie

### Phase 0: Streamer-Alpha (6 Monate vor Early Access)

15–20 handverlesene Streamer. Persönliche Einladung, privater Discord, Build-Zugang. Keine NDA auf Gameplay. Einzige Bedingung: ehrliches Feedback.

**Auswahlkriterien**: Indie-RPG-Affinität, Analyse-Fähigkeit, Community-Qualität. 60% deutsch, 40% englisch. 5K–200K Follower.

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

**Preis: 69,99€ (AAA-Standard 2026).**

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
| "Jenseits der Asche" | Neue Region: die tiefen Aschen-Einöden. Nomadische Höhlenvolk-Karawanen als Begleitsystem. | Höhlenvolk-Vertiefung | 29,99€ |
| "Das Innere" | Titanenadern als spielbare Dungeon-Region. Innenvolk-Hauptquest. Nervensystem-Erweiterung. | Innenvolk-Vertiefung | 29,99€ |
| "Knochen und Glaube" | Knochenturm-Städte. Religiöser Konflikt. Neue Rasse? | Küstenvolk vs. Siedlervolk | 29,99€ |

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

## 4. Community-Strategie (Zusammenfassung)

**Virale Momente**: Nervensystem-Leveling als 15-Sekunden-Clip (TikTok/Shorts). Vampir/Werwolf-Discovery ohne offizielles Reveal. Fraktions-Debatten als Reddit-Content.

**Kontroversen-Management (Biotech/Drogen)**: Vorbereitetes Statement. Kernaussage: RELICS zeigt Konsequenzen, glorifiziert nicht. Sucht verändert Gameplay negativ. USK-Ziel: 16+. Suchtberatung vor Release einholen.

**Community-Plattformen**: Discord (öffentlich nach EA-Start) mit Lore-, Builds- und Feedback-Kanälen. Reddit-Subreddit mit wöchentlichen Dev Diaries und AMAs.

---

## 5. USP-Kommunikation

**Elevator Pitch**: "Dark Fantasy RPG. Dein Nervensystem ist dein Skill-Tree. Die Wahrheit existiert nicht."

**Steam-Seite**: "RELICS ist ein Open-World-RPG auf einer Insel aus Titanenknochen, in dem dein Nervensystem dein Skill-Tree ist und jede Fraktion eine andere Wahrheit verkauft."

\newpage

# Kapitel 9 — Risiken, Entscheidungen & Timeline

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
Jedes Feature muss in beiden Perspektiven funktionieren (+30-40% Aufwand).
**Mitigation**: Kamera-Prototyp als erstes Deliverable. Fallback: eine Perspektive primär.

### R2 — MetaHuman Fellträger Kopf-Swap (MEDIUM)
Keine fertige Pipeline für nicht-menschliche Köpfe auf MetaHuman-Körpern.
**Mitigation**: 2-Tage-Spike. Fallback: subtilere Tiermenschen (Ohren/Augen statt voller Tierkopf).

### R3 — Nervensystem-Leveling UI (HIGH)
Neues UI-Paradigma ohne Referenzdesign. Muss intuitiv sein.
**Mitigation**: Papier-Prototyp → Spielertest → Tech-Prototyp.

### R4 — Scope: Insel vs. Region (MEDIUM)
Ganze Insel = Monate. Eine Region = Wochen. Vertical Slice = EINE Region.
**Mitigation**: Modulare Weltplanung. CD-Entscheidung zum Slice-Scope nötig.

### R5 — Biotech/Drogen-Thematik: USK (LOW-MEDIUM)
Kann USK 16 vs. 18 beeinflussen.
**Mitigation**: Frühzeitige USK-Beratung. Drogen als Konsequenz, nicht Verherrlichung.

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
