# Reasoning — Darius Engel — Tag 5, Szene 2 (WORK)

## Was ich heute tue und warum

GDD-01 ist der Eingangspunkt des gesamten GDD. Wer das Dokument zum ersten Mal liest, muss nach Kapitel 1 wissen: Was ist das fuer ein Spiel? Fuer wen? Was verspricht es? Und haelt das Versprechen standhalt gegen den Briefing?

V1 hatte sieben Abschnitte — Elevator Pitch, Design-Saeulen, USPs, Zielgruppe, Spielerfahrung (1h/10h/40h), Referenzrahmen, offene Fragen. Die Struktur war solide. Aber nach zwei Tagen GDD-02-Arbeit, nach Leos QA-Bedingungen, nach Namis drei Endpfaden und Emres Relikt-Entscheidung weiss ich mehr. V1 war ein Rahmen. V2 muss der Raum sein.

---

## Die fuenf Korrekturen, die ich vornehme

### 1. Scope-Realitaetscheck

V1 hatte eine Tendenz zur Vollstaendigkeit: "Wir wollen alles." Aber wir bauen einen Vertical Slice. Ein Vertical Slice hat EINE Region, EINE Hauptquest, ZWEI Nebenquests. Das heisst: Die Spieluebersicht muss ehrlich sein ueber den Massstab. "Open-World" ist die Ambition der Serie, nicht des Vertical Slice.

Ich mache das transparent: V2 trennt klar zwischen dem Serienversprechen (RELICS als Plattform) und dem Iteration-Versprechen (diese Iteration, dieser Vertical Slice). Das ist keine Einschraenkung — das ist Ehrlichkeit, die Vertrauen schafft.

### 2. Zielgruppe 25-40 schuetzt das Spiel

Vage Zielgruppen-Formulierungen wie "fuer RPG-Fans" sind kontraproduktiv. Sie fuehren zu falschen Erwartungen beim Spieler und falschen Prioritaeten im Team. Die Zielgruppe fuer RELICS ist praeziese: Spieler, die Gothic und Skyrim kennen, vielleicht Bloodborne gespielt haben, jetzt aber kaum noch Zeit haben. Sie spielen tief, aber nicht tagelang am Stueck. Sie wollen Konsequenz — keine Tutorial-Haende.

Das bedeutet: Zugaenglich genug, um ohne Handbuch anzufangen. Tief genug, um 40 Stunden zu halten. Kein Grind. Keine Fuellinhalte.

### 3. Kamera als Design-Saeule — nicht als Feature

Die Kamera ist in V1 als "Feature" gelistet: nahtloser Wechsel zwischen FP und TP. Das ist falsch geframet. Die Kamera ist eine PHILOSOPHIE-Aussage: Dieser Spieler darf in seine eigene Perspektive gehen (FP = Immersion, Praesenz, Gothic-Dichte) oder aus ihr heraustreten (TP = Uebersicht, Kampflesbarkeit, Ausruestungs-Customization). Das ist Spieler-Autonomie auf der visuellen Ebene. Das gehoert in die Design-Saeulen.

### 4. Tiervolk + Biotech als Weltsprache

Tiervolk war in V1 ein Aufzaehlungspunkt. Aber Tiervolk ist tatsaechlich ein Kern-Designelement der Weltidentitaet. Die Entscheidung "Haendler und Diebe, nicht Handwerker" ist eine soziale Architektur-Entscheidung. Sie sagt: Das Tiervolk bewegt sich in den Raendern der Gesellschaft, handelt mit dem, was andere nicht anfassen wollen, und hat Zugang zu Inhalten, die ueber legale Wege nicht erreichbar sind. Das ist mechanisch relevant.

Biotech war ebenfalls zu vage. Biotech = Alchemie als Weltphysik. Leveling als Koerperlichkeit. Schattenfieber als biologische Transformation. Die Aesthetik ist nicht Steampunk, nicht Science-Fantasy — es ist mittelalterliche Biologie, die an ihre eigenen Grenzen stosst. Das muss in der Spieluebersicht als Identitaetsmerkmal stehen.

### 5. Konsequenz-Versprechen operationalisieren

"Entscheidungen haben Konsequenzen" steht in jedem zweiten RPG-Presskit. Es bedeutet nichts, wenn es nicht konkret ist. Fuer RELICS heisst Konsequenz konkret:

- **Fraktionszustand verfolgt Entscheidungen dauerhaft** — wer einen Ordenssoldaten toetet, hat ein Problem mit dem Orden fuer den Rest des Spiels. Es gibt keine "Questmarker-Gnadenfrist".
- **Schattenfieber-Entscheidungen sind permanent** — der Hard Cap ist bereits verankert. Das ist das prominenteste Konsequenz-Beispiel im Spiel.
- **Weltzustand aendert sich** — der Spieler kann in den zweiten Akt gehen und merken, dass ein NPC nicht mehr da ist, weil er ihn im ersten Akt versehentlich in eine Falle getrieben hat. Nicht durch Quest-Logik, sondern durch emergente Spielwelt.

Konsequenz muss in Kategorien ausgedrueckt werden: Sofortige Konsequenz (NPC stirbt), kurzfristige Konsequenz (Fraktion reagiert, Quests fallen weg/kommen dazu), langfristige Konsequenz (Weltzustand am Ende des zweiten/dritten Akts unterscheidet sich).

---

## Was ich NICHT aendere

- Die sechs Design-Saeulen bleiben strukturell — sie sind der richtige Rahmen
- Der Elevator Pitch bleibt kurz und scharf
- Die Referenzrahmens-Tabelle bleibt — sie ist ein praktisches Orientierungswerkzeug
- Das 1h/10h/40h-Prinzip bleibt — es ist didaktisch wertvolles Format

---

## Selbstreflexion

Freitagmorgen, letzter Produktionstag. GDD-02 ist gestern fertig geworden — das war die schwerere Arbeit. GDD-01 ist heute die Saubermacher-Aufgabe: alles, was in den letzten vier Tagen klar geworden ist, rueckwirkend in den Eingangspunkt einbauen.

Die Versuchung ist, GDD-01 zu lang zu machen. Ein Ueberblicksdokument muss KNAPP sein. Jeder Satz muss fragen: Macht das Spass? Was ist die Spieler-Fantasie hier?

Wenn das Dokument fertig ist, sollte jemand, der nur GDD-01 liest, verstehen: "Okay, das ist ein Gothic-Nachfolger mit Biotech-Aesthetik und einer Infektionsmechanik, die meine Spielentscheidungen koerperlich macht. Fuer Leute, die Tiefe wollen und keine Zeit fuer Bullshit haben."

Wenn der Leser das denkt: V2 hat funktioniert.
