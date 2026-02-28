# RELICS — Recherche-Notizen: GDD-Struktur & erste Mechanik-Ideen
**Darius Engel / Tag 1 / Szene 2 — Einzelarbeit**

---

## Was ich heute gelesen habe

- Deus Ex "Shooter: Majestic Revelations" — Warren Spector, Ion Storm, v5.3e, 11/08/1997
- Diablo Pitch Document — Condor, Inc., Copyright 1994

---

## 1. Was diese alten Dokumente über GDD-Struktur lehren

**Deus Ex macht etwas Entscheidendes richtig:** Das Dokument beginnt nicht mit Mechaniken, sondern mit einer Frage. "Is it better to live free in a world of chaos or live safely in an ordered world of someone else's design?" Das ist kein Tagline — das ist das Designprinzip, aus dem jede Systementscheidung folgt. Spector nennt das "High Concept", und der Satz ist so präzise, dass man das gesamte Spiel daraus ableiten kann.

Das will ich für RELICS übernehmen. Unser High Concept: **"Ich betrete als Fremder eine Welt, die ohne mich funktioniert hat — und durch mein Handeln werde ich Teil des Systems, das ich vielleicht zerstöre."**

**Diablo zeigt die andere Schule:** Kein Philosophieunterricht. Condor 1994 erklärt ihr Spiel in einem Satz: "hack and slash, feel good gaming audience." Dann kommt sofort das Gameplay-Walkthrough. Dieser Pragmatismus hat mir imponiert — die wussten genau, was der Spieler fühlen soll, und haben alles andere rausgestrichen.

**Was ich für unser GDD daraus nehme:** Kapitel 1 muss beides liefern. Ein klares High Concept (philosophische Ebene) UND ein präzises "Game Feel"-Statement (Körperempfindung beim Spielen). Nicht eines oder das andere.

---

## 2. Medieval Cyberpunk — was das systemisch bedeutet

Das Briefing sagt: "Technologischer Fortschritt erzeugt Ungleichheit." Das ist kein Flavor, das ist eine Mechanik-Prämisse.

Was Spector mit "World Simulation" meint — Objekte haben physikalische Eigenschaften, Probleme haben mehrere Lösungen, NPCs reagieren auf Kontext — das lässt sich direkt übersetzen:

**Materialklasse als Gameplay-Variable.** Im Briefing: Titan-Legierungen für die Oberschicht, Eisen für die Unterschicht. Das darf keine reine Kosmetik sein. Die Werkstoff-Qualität muss echte Spielrelevanz haben: bessere Rüstung hält länger, bessere Waffe macht mehr Schaden, aber bessere Materialien sind hinter Gildenschranken gesperrt. Der Spieler als Fremder startet mit Eisengerät — und das fühlt sich so an.

**Die drei Fraktionen als Zugangskontrollen.** Deus Ex hat Majestic-12, den TLC, den Illuminatenorden. Drei Kräfte, keine ist gut. RELICS hat Krone, Gilden, Orden. Dasselbe Prinzip. Jede Fraktion kontrolliert andere Ressourcen: die Krone kontrolliert Territorium und Militärpassagen, die Gilden kontrollieren Materialzugang und Handwerksrezepturen, der Orden kontrolliert Wissen und Bildung (= Fertigkeitsbücher, Upgrade-Pfade). Fraktionsruf ist kein abstrakter Zähler — er ist der Schlüssel zu konkreten Spielsystemen.

---

## 3. Das Nervensystem-Leveling — erster Gedanke

Kein Attribut-Grid. Kein Erfahrungspunkte-Balken. Die halbtransparente Nervensystem-Ansicht ist unsere visuelle Metapher und soll auch funktional anders sein.

**Spieler-Fantasie:** "Mein Körper ist mein Fortschrittsanzeiger. Ich sehe, was ich trainiert habe."

Erste Idee: Drei Subsysteme (Cardio, Muskel, Lymph) trainieren durch Nutzung. Wer viel läuft, verbessert Ausdauer (Cardio). Wer viel kämpft, verbessert Stärke (Muskel). Wer Alchemika einnimmt oder Schattenfieber-Einfluss übersteht, verändert das Lymphsystem — mit Risiken. Das ist das Deus Ex-Skill-by-Use-Prinzip (nicht granular-numerisch, sondern qualitativ in Stufen), kombiniert mit dem Gothic-Meistersystem: Wer Schwertkampf auf Meister bringen will, braucht einen Lehrer.

**Problem, das ich Leo fragen muss:** Sind Spieler bereit, für Trainingsfortschritt Zeit zu investieren, oder fühlt sich das wie Grind an? Deus Ex hat das bewusst auf vier Qualitätsstufen gedeckelt (Untrained / Skilled / Advanced / Master) — das könnte unser Modell sein.

---

## 4. Design-Säulen (erster Entwurf — wird mit dem Team kalibriert)

1. **Immersive Simulation** — jedes Problem hat mehrere Lösungen, die Welt reagiert konsequent
2. **Fraktionspolitik als Kernspannung** — kein "Gut vs. Böse", sondern konkurrierende Interessen
3. **Körperlicher Fortschritt** — das Nervensystem ist der Charakter, nicht eine Zahl auf einem Screen
4. **Dichte vor Breite** — Gothic statt Skyrim-Karte; handgemacht, jeder NPC hat eine Funktion

---

## 5. Was noch fehlt — Fragen an das Team

- **An Emre:** Welche Rolle spielt das Relikt mechanisch? Muss ich eine Spieler-Fantasie definieren, bevor wir den Relikt-Typen kennen?
- **An Nami:** Wie sieht der Questbeginn aus? Spector hat einen klaren Act-1-Aufhänger (verschwundener Bruder). Wir brauchen eine persönliche Eintrittsfrage, die den Spieler zieht.
- **An Leo:** Deus Ex argumentiert bewusst gegen granulare Skill-Zahlen (1-100). Hat aktuelle Forschung/Community-Feedback dazu etwas Aktuelles?

---

## GDD-Struktur für RELICS (Vorschlag an Team)

Basierend auf Spector: erst Vision, dann Systeme, dann Welt. Nicht umgekehrt.

| Kap. | Titel | Verantwortlich |
|------|-------|----------------|
| 1 | Spielübersicht & Design-Säulen | Darius |
| 2 | Kernmechaniken (Combat, Crafting, Progression, Nervensystem) | Darius |
| 3 | Erzählkonzept & Quests | Darius + Nami |
| 4 | Schlüsselfiguren & NPCs | Nami |
| 5 | Visuelle Designsprache & Art Direction | Vera |
| 6 | Technische Spezifikation & Produktion | Tobi + Finn |

---

*Notizbuch-Stand 10:00 Uhr — Entwurf, keine finale Entscheidung*
