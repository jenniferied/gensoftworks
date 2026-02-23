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
