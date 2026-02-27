# Leo — Tag 05, Szene 5 (WORK) — Output

---

## Fix 1: Ymir-Ersetzung in GDD-02

**Erledigt.** Zwei Stellen korrigiert:

- Kap. 2.7, Zeile 172: `"Ymir-Material"` → `"Emer-Material"`
- Kap. 6.1, Zeile 334: `"(Ymir, Ginnungagap, etc.)"` → `"(Emer, Ginnungagap, etc.)"`

"Ginnungagap" wurde nicht angefasst — Emre hat dafuer noch keinen RELICS-eigenen Begriff etabliert. Das ist eine offene Stelle, die er im WBB-01 nachliefern muss.

---

## QA-Abschlussbericht — Woche 1

**Dokument:** `simulation-2-test/gallery/gdd/02-kernmechaniken.md`
**Autor:** Leonie Fischer, QA Lead
**Datum:** Tag 5, Freitag — Nachmittag (vor dem Wochen-Review)

---

### 1. Was haben wir geliefert?

Fuer ein erstes Konzept in einer Woche ist das ehrlich beeindruckend. Wir haben:

- GDD-01 bis GDD-06 als Strukturdokumente
- GDD-02 als V0.5 mit echtem Fleisch: Combat, Schattenfieber, Nervensystem-Leveling, Alchemie, Exploration — alles mit Spieler-Perspektive durchdacht, nicht nur als Feature-Liste
- Drei nicht-verhandelbare QA-Bedingungen fuer das Schattenfieber-System, die im Dokument verankert sind
- Eine Risikomatrix, die die groessten Fallstricke benennt
- WBB-01 (Emre): Mythos-Grundlage, aus der das Spiel seine Seele zieht
- Erste Art-Direction-Hinweise (Vera)

Was ich NICHT bewerten kann, weil ich es nicht gelesen habe: der aktuelle Stand von GDD-03 bis GDD-06 und WBB-02/03. Das ist eine echte Luecke — fuer einen vollstaendigen Abschlussbericht braeuchte ich diese Dokumente.

---

### 2. Was hat sich aus Spielersicht gut entwickelt?

**Das Schattenfieber-System.**
Das ist der Teil, bei dem ich am fruehsten "ja, das will ich spielen" gedacht habe. Nicht wegen der Zahlen — die koennen sich noch aendern — sondern wegen der Grundidee: Infektion als bewusste Entscheidung, nicht als Strafe. Die drei Bedingungen (Transparenz, sofortige Power Fantasy, kein Zufall) sind solide. Wenn das Team diese Linie haelt, haben wir etwas, das sich anders anfuehlt als das, was ich kenne. Bloodborne ist eine gute Referenz, aber wir gehen weiter — weil wir die Entscheidung ins Narrativ einbetten.

**Das Stufe-0-Aequivalent-Prinzip.**
Das war meine groesste Sorge am Anfang: Wird Stufe 0 sich wie "der langweilige Weg" anfuehlen? Mit der Aequivalent-Tabelle in Kap. 2.5 haben wir eine Antwort darauf. Sie ist noch nicht durchgetestet — aber sie ist da, und das ist der erste Schritt.

**Die Build-Archetypen (Kap. 6.2).**
Emergente Archetypen statt vorgegebene Klassen. Das ist die richtige Richtung. Fuer ein Spiel mit diesem Anspruch (Gothic-Dichte, Disco-Elysium-Geist) brauchen wir keine Warrior/Mage/Rogue-Schubladen. Der "Reine Krieger" und die "Schattenbestie" muessen sich BEIDE vollstaendig anfuehlen.

---

### 3. Wo habe ich noch offene Fragezeichen?

**Kontrollverlust-Episoden (Stufe 4).**
Das ist das riskanteste Feature im System. Die Risikomatrix sagt "Mittel" fuer Schwere und Wahrscheinlichkeit. Ich bin nicht sicher, ob das stimmt. Ein Spieler, der 30 Stunden investiert hat und dann das Gefuehl bekommt, die Kontrolle "ungewollt" zu verlieren — das kann sehr schnell sehr toxisch werden, egal wie gut wir es kommunizieren. Ich will, dass Darius und Tobi das NICHT auf dem Papier loesen, sondern im Prototyp testen. Bevor das spielbar ist, kein endgueltiges Design.

**Die narrativen Zustands-Dialoge (Stufe 3-4, Kap. 2.3).**
"Dialoge mit Figuren, die moeglicherweise nicht existieren" — das klingt grossartig. Das ist auch das teuerste QA-Objekt, das ich mir vorstellen kann. Jeder Quest-State mal alle Infektionsstufen mal alle moeglichen Entscheidungen. Das ist kein V1-Feature. Ich moechte, dass wir fuer den Vertical Slice eine reduzierte Version definieren: Wie viele "fragwuerdige" Dialoge testen wir tatsaechlich durch? Was ist das Minimum, das die Spielerfahrung bugged, wenn wir es nicht testen?

**Das Namenssystem (Kap. 6.1).**
Fix ist gemacht (Ymir → Emer), aber die fundamentale Frage ist offen: Wann liefert Emre das vollstaendige Framework? Alle anderen Dokumente arbeiten mit Arbeitsbegriffen. Das ist okay fuer V0.5, aber spätestens fuer V1 muss das Fundament stehen. Ich habe heute in 2.7 ein "Ginnungagap" stehen lassen, weil ich keine Autorisation habe, das eigenhaendig zu ersetzen.

---

### 4. Was braucht CD-Feedback?

Drei Fragen, die ich ins Review mitbringe:

**a) Kontrollverlust: Wann ist er spielbar?**
Ich brauche eine CD-Entscheidung: Ist Kontrollverlust ein Feature fuer den Vertical Slice, oder schieben wir es auf V2? Bevor das entschieden ist, ist Kap. 2.9 nicht abschliessbar.

**b) Narrativ-Schicht (Stufe 3-4): Scope fuer den Vertical Slice?**
Was ist das Minimum, das Nami und Darius schreiben? Ich brauche eine realistische Zahl: Wie viele "fragwuerdige" Questgeber/Dialoge gehen wir fuer den ersten Slice wirklich an? Das bestimmt meinen QA-Aufwand fundamental.

**c) Ginnungagap — Emre, wann kommt das RELICS-Aequivalent?**
Keine Blocker-Frage, aber sie muss auf dem Tisch liegen.

---

### 5. Mein Gefuehl nach Woche 1

Ich habe schon viele Projekte gesehen, die in Woche 1 zu gut aussehen. Die implodieren dann in Woche 3, wenn das erste spielbare Ding da ist und nichts davon so funktioniert, wie es auf Papier aussah.

Bei RELICS habe ich das Gefuehl nicht. Nicht weil das Design perfekt ist — das ist es nicht, und das ist auch nicht der Anspruch in Woche 1. Sondern weil wir uns die richtigen Fragen stellen. Das Schattenfieber-System hat echte Risiken, und wir benennen sie. Die Stufe-0-Fantasie hat das Potenzial, leer zu fuehlen, und wir arbeiten dagegen. Das Namenssystem ist inkonsistent, und wir flaggen es.

Das Spiel, das ich in der GDD-02 lese, wuerde ich spielen wollen. Ob es sich dann auch so anfuehlt — das ist die Arbeit der naechsten Wochen.

---

*Leonie Fischer — QA Lead, Tag 5, 14:30 Uhr*
*Schreibt diesen Bericht am Art-Station, mit kaltem Kaffee und drei offenen Browser-Tabs mit Bloodborne-Wikis*
