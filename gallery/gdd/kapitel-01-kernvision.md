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
