---
title: "RELICS — Game Design Document"
subtitle: "Anhang B · v0.1"
short-title: "GDD"
author: "GenSoftworks Studio Simulation"
date: "2026"
lang: german
toc: true
---

# RELICS Alpha-Build: Erste-Stunde Streamer-Checkliste

**Zweck:** Live-Testwerkzeug für Alpha mit Streamern (LeoPlaysIndie + Gäste)
**Format:** Praktische QA-Checkliste, nicht Design-Doc

---

## Ziel: Chat-Retention in den kritischen 8–12 Minuten

**Kontext:** Meine 47K YouTube-Follower erwarten:
1. Klare Identität (nicht generic fantasy)
2. Emotionale Hook (nicht nur Mechanic)
3. Mechanik-Innovation (nicht Skyrim-Clone)

Wenn Chat in den ersten 12 Minuten nicht "engaged" ist, klicken 40% ab. Das ist Baseline aus Community-Daten.

---

## Phase 1: INTRO (0–5 Min) — Erste Impressionen

### Checkliste

- [ ] **Material-Klasse ist SOFORT erkennbar**
  - Schaue auf meinen Character: Trage ich Color-Schichten richtig?
  - Schaue auf NPCs: Reicher NPC ≠ armer NPC optisch?
  - **Chat-Test:** Wenn jemand sagt "this looks high-fashion", SUCCESS
  - **FAIL:** "this looks generic"

- [ ] **Welt fühlt sich VERTRAUT + FREMD an**
  - Mitteleuropa-Vibes: Fachwerk, Stein, organisch
  - NICHT Generisches High Fantasy
  - **Chat-Test:** "Ist das Köln? Ist das Mittelalter? Ist das...beides?"
  - **FAIL:** "Looks like WoW"

- [ ] **Audio-Design Setting tragen**
  - Ambient-Sound: Vögel, Wind, ferne Stimmen?
  - Nicht zu laut, nicht zu leise
  - **Chat-Test:** Zuschauerreaktion auf Soundscape
  - **FAIL:** Stille oder generischer Fantasy-Music

- [ ] **Ingame-UI ist nicht invasiv**
  - Minimalistisch oder Stealth-UI?
  - **Chat-Test:** "Schöne UI" vs "wo ist mein HUD?"
  - **FAIL:** MMORPG-Style UI mit 15 Elementen

### Beispiel-Kommentar im Chat bei SUCCESS:
"wait this doesn't look like skyrim???" (gut gemeint)
"actually medieval cyberpunk hits" (perfekt)

---

## Phase 2: EMOTIONAL HOOK (5–10 Min) — Der sterbende NPC

### Checkliste

- [ ] **Sterbender NPC hat KLARE Motivation**
  - Ist mir klar, warum dieser NPC das Relikt gibt?
  - Ist es Verzweiflung? Hoffnung? Geheimnis?
  - **Chat-Test:** Erste Reaktion sollte emotional, nicht strategisch sein
  - **FAIL:** "Warum gibt er mir das?"

- [ ] **Dialog fühlt sich LEBENDIG an**
  - Voice-Acting: keine Roboter-Qualität
  - Timing: nicht zu schnell, nicht zu träge
  - **Chat-Test:** Wenn Chat "rip" schreibt = emotionale Verbindung
  - **FAIL:** "cringe dialogue"

- [ ] **Genealogie ist MINIMAL erklärt, aber signifikant**
  - Sterbender NPC hat Familie? Feinde? Status?
  - Ich sollte verstehen: "Dieser Person war etwas wichtig"
  - **Chat-Test:** "I care about this person" vs "who is this?"
  - **FAIL:** Generischer "old man gives you quest" archetype

- [ ] **Relikt-Übergabe ist RITUELL, nicht transactional**
  - Es ist nicht "hier nimm Gegenstand"
  - Es ist "hier vererbe ich dir Verantwortung"
  - **Chat-Test:** Zuschauerreaktion sollte "whoa" sein, nicht "okay cool"
  - **FAIL:** Klingt wie Questmarker-Pickup

- [ ] **Schattenfieber-Zeichen ist SUBTIL**
  - Nächster liegt der sterbende NPC? Infiziert?
  - Erste visuell-auditive Anomalie?
  - **Chat-Test:** "Ist das normal? Warum sieht/klingt das weird?"
  - **FAIL:** Obvious "infected" marker oder zu mystisch

### Beispiel-Chat-Reaktion bei SUCCESS:
```
Chat: "wait why is his hand shaking like that"
Chat: "this dude is dying RIGHT NOW"
Chat: "oh no oh no oh no"
(Viewers retain)
```

---

## Phase 3: MECHANIK-INTRO (10–15 Min) — Combat oder erste Aktion

### Checkliste

- [ ] **Combat fühlt sich GEWICHTIG an**
  - Schwert: nicht zu schnell, nicht zu träge
  - Hit-Feedback: Sound + Particle + Screen-Shake?
  - **Chat-Test:** "oh that felt good" vs "floaty"
  - **FAIL:** Souls-like über-complicated oder Skyrim-janky

- [ ] **Erste Skill-by-Use Progression ist SICHTBAR**
  - Nach 3–5 Schlägen: Merke ich etwas?
  - Nach 10 Schlägen: Ist es definitiv unterschiedlich?
  - **Chat-Test:** "Did you see that? Your swing changed!" (nach ~7 hits)
  - **FAIL:** Keine Veränderung sichtbar = "skill system broken"

- [ ] **Gegner-Reaction fühlt sich REAL an**
  - Gegner blockt? Weicht aus? Reagiert auf mich?
  - Nicht statisch, nicht overpowered
  - **Chat-Test:** Combat sollte sich taktisch anfühlen, nicht zufällig
  - **FAIL:** Gegner-AI ist offensichtlich dumm oder unfair

- [ ] **Relikt-Item hat visuelles GEWICHT**
  - In meinem Inventar: sieht es wichtig aus?
  - In meiner Hand (wenn equiped): ist es bemerkenswert?
  - **Chat-Test:** "what is that thing??" (Neugier, nicht Verwirrtheit)
  - **FAIL:** Relikt sieht aus wie ein Stein oder ein Bug

---

## Phase 4: WELT-ASYNCHRONITÄT (15–30 Min) — Erste Fraktionssignale

### Checkliste

- [ ] **Krone-NPCs sind erkennbar anders als Orden-NPCs**
  - Krone: Militärisch? (Bewaffnet? Patrouille?)
  - Orden: Überwachend? (Priester? Fragend?)
  - Gilden: Handelnd? (Kaufleute? Verhandlung?)
  - **Chat-Test:** "Ooh those are like... police?" vs "those are monks?"
  - **FAIL:** Alle NPCs sind gleich oder generisch

- [ ] **NPCs ignorieren mich nicht völlig**
  - Reagieren sie auf meine Präsenz?
  - Gibt es gegensätzliche Reaktionen (eine Fraktion mag mich, andere nicht)?
  - **Chat-Test:** "Wow the city reacts to me!"
  - **FAIL:** Walking simulation, keine Interaktion

- [ ] **Audio-Ambient gibt Kultur-Kontext**
  - Gebetsgesang aus Kloster?
  - Hammer aus Schmiede?
  - Markt-Getümmel aus Gilden-Bezirk?
  - **Chat-Test:** "I hear a forge? Where are we?"
  - **FAIL:** Silent generic fantasy world

- [ ] **Erste Fraktions-Quest-Option ist ERKENNBAR**
  - Nach Relikt-Übergabe: Gibt es 2–3 verschiedene "nächste Schritte"?
  - Jeder kann ich eine andere Fraktion folgen?
  - **Chat-Test:** "Wait, should we help the king or the church?" (nicht eine Option)
  - **FAIL:** Linearer Questmarker, keine Wahl

---

## Phase 5: IMMERSION CHECK (30–60 Min) — Gesamtbild

### Checkliste

- [ ] **Ich habe nach 30 Min keine großen Fragen wie "WTF is happening?"**
  - Zeitlicher Kontext: klar genug?
  - Spatial Kontext: weiß ich, wo ich bin?
  - Motivation: verstehe ich, warum ich weitermache?
  - **Chat-Test:** Lautet die meiste Reaktion "cool" vs "confused"?
  - **FAIL:** Zu viele Fragen = schlechtes Onboarding

- [ ] **Material-Klasse-Ökonomie ist spürbar**
  - Kann ich unterschiedliche Waffen/Armor sehen?
  - Gibt es ein Upgrade-System (Crafting? Loot?)?
  - **Chat-Test:** "Can I make better stuff?" (Motivation für weiterspielen)
  - **FAIL:** Alle Waffen sehen gleich aus

- [ ] **Relikt fühlt sich nicht "broken" an**
  - Ist es im Inventar? Kann ich es equip-pen?
  - Reagiert es auf etwas? (Schattenfieber, andere Relikte, Orte?)
  - **Chat-Test:** "What does this thing DO?" (Neugier, nicht Verwirrung)
  - **FAIL:** Relikt ist unauffällig oder glitchy

- [ ] **Erste Stunde fühlt sich POLISHED an**
  - Clipping? Texture-Fehler? UI-Bugs?
  - **Chat-Test:** "This looks unfinished" ist DEATH-Marker
  - **FAIL:** Sichtbare Production-Fehler

- [ ] **Meine Fähigkeit als "fremder Charakter" ist spürbar**
  - Werde ich von anderen erkannt? ("stranger", "outsider")
  - Fühle ich mich agentschaftlich oder gelyncht?
  - **Chat-Test:** "Wait, why does everyone hate me?" (good if intentional) vs "bad design"?
  - **FAIL:** Ich bin der "chosen one" Archetype

---

## Quantitativ: Streamer-Metriken (für meine YT/Twitch)

### Tracking während des Tests

- **Minute 0–5:** Wie viele Chat-Nachrichten? (Engagement-Baseline)
- **Minute 5–10:** Ist die Zahl HÖHER? (Emotional hook)
- **Minute 10–15:** Erste Combat-Reaktion. Positive/Neutral/Negative?
- **Minute 15–30:** Fraktions-Reaktion. Neugier oder Verwirrung?
- **Minute 30–60:** Retention-Kurve. Flach = FAIL. Steil = SUCCESS.

### Zielwerte (aus meinen Community-Daten)

```
0–5 Min:  100% viewers
5–10 Min: 85% viewers (emotional hook muss gut sein)
10–15 Min: 75% viewers (mechs müssen "feel right")
15–30 Min: 70% viewers (Fraktions-Choice sollte reintegrieren)
30–60 Min: 65% viewers (mindestens halten)

FAIL: <50% nach 60 Min
SUCCESS: >70% nach 60 Min
```

---

## Bug-Reporting: Standard-Template

Wenn ich während des Tests Bugs finde, reporte ich sie so:

```
BUILD: RELICS Alpha 0.1
STREAM DATE: [date]
RETENTION AT BUG: [minute]

INFRASTRUCTURE: [Wolf category]
SEVERITY: [Critical/High/Medium/Low]
FEEL-IMPACT: [Immersion/Mechanics/Clarity]

TITLE: [2-sentence description]

REPRO STEPS:
1. [exact step]
2. [exact step]
3. [exact step]

EXPECTED: [what should happen]
ACTUAL: [what happens]

SCREENSHOT/VIDEO: [timestamp from VOD]

PRIORITY FOR ALPHA: [Critical/Important/Nice-to-have]
```

---

## Beispiel-Run (fiktiv)

```
Minute 0: Starte Spiel. Material-Klasse sofort erkennbar (All-Black Krone-Guard neben mir).
Minute 3: Dialog mit sterbendem Alchemisten. Voice-Acting ist gut. Chat sagt "rip".
Minute 7: Erhalte Relikt-Scherbe. Visuelle Übergabe ist rituell, kein Queststep.
Minute 10: Erste Combat-Encounter vs Krone-Soldat. Hit-Feedback ist solide.
Minute 12: Nach ~10 Schlägen merke ich meine Axt-Animation ist flüssiger. Chat sagt "yo your swing just got better?"
Minute 18: Drei NPCs approachen mich aus unterschiedlichen Richtungen. Krone: feindselig. Orden: fragend. Gilden: neutral.
Minute 25: Ich wähle Gilden-Option (mit Kaufmann sprechen). Quest-Marker erscheint, aber nicht invasiv.
Minute 40: Habe Relikt in Gilden-Werkstatt gebracht. NPC sagt "this artifact... it's not human-made. From BEYOND." (Mythologie-Hint)
Minute 55: Erste Quest-Abschluss mit Gilden. Bekomme Material zum Crafting. Skill-by-Use-System wird sichtbar.
Minute 60: Chat: "Okay I'm invested. When can we play this?"

RESULT: Retention bei 72%. SUCCESS.
```

---

## Vor dem Test: Setup

- [ ] OBS ist configured für 1080p60
- [ ] Microphone-Level: -6dB
- [ ] Chat-Overlay eingeschaltet
- [ ] Video-Editor (Premiere) bereit für Schnitt
- [ ] Clementine (Bartagame) hat Wasser + Wärme
- [ ] Mein Kaffee ist full (Streaming braucht Koffein)
- [ ] Notepad offen für Stichpunkte während des Spiels

---

## Nach dem Test: Reporting

1. **Direkt nach Stream:** YouTube-Community-Post ("What did you think of RELICS Alpha?")
2. **Nächster Tag:** Google Sheets-Zusammenfassung (Retention + Bugs + Observations)
3. **Bericht an Darius:** (persönlich, mit Timestamps + Clips)
4. **Bericht an Team:** (Freitag-Meeting, wenn GDD-Snapshot ansteht)

---

\clearpage

# Leo ↔ Darius Sync: Skill-by-Use Designdiskussion

**Zeitslot:** Tag 2, 14:00
**Ort:** Darius' Büro oder QA-Station (beide haben dual monitors)
**Dauer:** 45–60 Minuten
**Ziel:** Skill-by-Use philosophisch + mechanisch + praktisch finalisieren

---

## Meine Kernposition

**Skill-by-Use ist nicht nur Mechanic. Es ist Weltweltanschauung.**

Die Gilden (Material-Klasse) kontrollieren Macht durch Handwerk. Der Spieler, der mit Gilden-aligned ist, erlernt durch TUN — nicht durch Mana-Punkte oder Skill-Trees.

Das ist **strukturell richtig** und sollte **visuell spürbar** sein.

---

## Diskussionspunkte (in dieser Ordnung)

### 1. PHILOSOPHISCHE ALIGNMENT

**Leo sagt:**
"Skill-by-Use ist nicht random progression. Es ist die Weltsicht der GILDEN."

- **Krone lernt durch Blut:** Geburt, Erbe, Ahnen (Blut-Magie? Erbliche Fähigkeiten?)
- **Orden lernt durch Wissen:** Bücher, Schulung, Meditation (Intellekt als Ressource?)
- **Gilden lernen durch Praxis:** Hämmern, Schmieden, Experimentieren (Skill-by-Use)

Wenn Spieler Gilden wählt, sollte das Progression-System diese Philosophie WIDERSPIEGELN.

**Frage an Darius:**
"Sind wir aligned, dass Skill-by-Use nicht 'neutral' ist, sondern Fraktions-aligned?"

**Warum wichtig:** Wenn Spieler merkt "Ich lerne, indem ich tue", fühlt sich das nicht wie Grind an, sondern wie AGENTSCHAFT. Das ist Disco-Elysium-Level Design-Thinking.

---

### 2. PRAKTISCHE METRIKEN (für Alpha)

**Leo sagt:**
"Erste 10 Nutzungen MÜSSEN sichtbar sein. Nicht Damage. FEEL."

**Metriken für Skill-Upgrade:**

```
Nutzung 1–4:  Baseline. Kein Feedback außer Hit-Sound + Particle.

Nutzung 5–7:  SUBTIL-Signal:
  - Hit-Sound wird cleaner (nicht neuer Sound, aber "besserer")
  - Particle-Color shiftet minimal (z.B. "bluer" für Tiegelstahl?)
  - Combo-Animation wird SMARTER (fluider)

Nutzung 8–10: OBVIOUS-Signal:
  - Hit-Sound ist definitiv unterschiedlich (nicht "new", aber "evolved")
  - Swing-Arc visualisiert sich besser (fluidere Animation)
  - Potential for combo-extension wird sichtbar

Nutzung 11+: Diminishing returns. Spieler weiß: "Ich bin jetzt skilled mit dieser Waffe"
```

**Chat-Test (aus meiner Streamer-Erfahrung):**
- Nutzung 1–4: Chat ist nicht interessiert
- Nutzung 5–7: Chat merkt etwas, fragt aber "what changed?"
- Nutzung 8–10: Chat sagt "wait, your attack is different now!" oder "dude your swing just got better"
- SUCCESS: Keiner sagt "ist das ein Bug?"

**Frage an Darius:**
"Können wir diese 10-Hit-Metriken in Alpha-Feature-List hochpriorisieren?"

**Warum wichtig:** In der ersten Stunde mit Streamern, wenn Spieler 15–20 Mal kämpft, MUSS sie diese Progression sehen. Sonst Tweet: "Skill-System broken?"

---

### 3. INTEGRATION MIT RELIKT-RESONANZ

**Leo sagt:**
"Relikt könnte Skill-Lernen BESCHLEUNIGEN oder INTERFERIEREN."

**Möglichkeit A:** Relikt-Nähe = schnellerer Skill-by-Use
- "In der Nähe des Relikt lerne ich schneller"
- Philosophie: Relikt ist Konzentrator von Macht
- Mechanic: Nach 5 Hits statt 10 Hits sichtbar mit Relikt

**Möglichkeit B:** Relikt-Nähe = Schattenfieber-Interferenz
- "Relikt stört meine Fähigkeit, normal zu lernen"
- Philosophie: Relikt ist FREMD, nicht natürlich
- Mechanic: Skill-Upgrade-Visuals sind "glitchy" wenn Relikt aktiv

**Möglichkeit C:** Relikt hat nichts mit Skill-by-Use zu tun
- Clean separation
- Philosophie: Relikt ist orthogonal zu lernen

**Frage an Darius:**
"Welche Option macht narrativ Sinn? Oder sollen wir das später definieren?"

**Warum wichtig:** Welt-Kohärenz. Wenn Relikt nicht mit Skill-Learning verknüpft ist, fühlt sich die Welt "loose" an.

---

### 4. TECHNISCHE FEASIBILITY (mit Tobi später)

**Leo fragen Darius zuerst, dann Tobi:**

- [ ] Können Skill-Upgrade-Visuals parallel zu Relikt-Shader-Anim existieren?
- [ ] Ist Animation-Streaming für 10 verschiedene "Swing-States" kW-heavy?
- [ ] Können Particle-Colors data-driven sein (Config, nicht hardcoded)?
- [ ] Können Sound-Crossfades (alte → neue Axt-Sound) in Audio-Engine laufen?

**If blockers:**
"Was ist der MVP-Scope für Alpha? Können wir Komplexität reduzieren?"

**Warum wichtig:** Ich brauche technische Garantie, dass "visuell sichtbar" überhaupt machbar ist für Alpha-Deadline.

---

### 5. CONTENT-INTEGRATION MIT NAMI

**Leo sagt:**
"Skill-by-Use hat Dialog-Implikationen."

- **NPC-Dialog-Shift:** Wenn ich geskilled bin mit Schwert, sollten Soldaten mich anders grüßen?
- **Quest-Gating:** Können (sollten) Quest-Options an Skill-Level gebunden sein?
  - z.B. "craft a [intermediate] weapon" erfordert 5+ Smithing-Skill-Level?
- **Faction-Recognition:** Wenn Gilden-NPC merkt, dass ich skilled bin, reagiert sie anders?

**Frage an Darius:**
"Sollen wir später (nicht Alpha) mit Nami koordinieren, dass Quest-Options Skill-States trackbar machen?"

**Warum wichtig:** Skill-System sollte nicht nur Mechanic sein, sondern Narrative-Trigger.

---

### 6. STREAMER-RETENTION (meine Red Line)

**Leo sagt (am dringlichsten):**
"Alpha-Success ist nicht Game-completeness. Es ist Chat-Engagement in den ersten 12 Minuten."

**Skill-by-Use im Retention-Fenster:**

Das erste Combat-Encounter sollte in Minute 10–12 sein.
Spieler schlägt 10x hin.
Chat sollte nach Hit 8 sagen: "wait what just happened?"

**Wenn das nicht klappt:**
- Hit 10: Chat merkt nichts = "skill system is broken"
- Zuschauerzahl sinkt von 75% → 55%
- Reddit-Post am nächsten Tag: "LeoPlaysIndie's RELICS Alpha ist buggy"
- Das ist für Studio death-Spiral

**Meine Empfehlung (hart):**
"Wenn Skill-Upgrade-Visuals nicht bis Alpha Ready sind: DEACTIVATE DAS SYSTEM für Alpha."
"Besser: 1 simple Mechanic, 100% Polish"
"Schlecht: komplexes System, 60% Polish"

**Frage an Darius:**
"Können wir committed sein: Skill-Upgrade-Visuals sind Alpha-BLOCKING?"

---

### 7. LANGZEITVISION (Post-Alpha)

**Leo sagt (optionsdiskussion):**

Für RELEASE (nicht Alpha):

- [ ] Jede Waffe-Klasse hat 5–7 Skill-States (current = 3?)
- [ ] Skill-by-Use → Unlocks (Combo-Moves, Special-Attacks?)
- [ ] Tier-System: Anfänger → Handwerker → Meister (Gilden-Ranking?)
- [ ] Schmiede-Quests: "Forge this [legendary] weapon" = Level-30-Content?

**Frage an Darius:**
"Ist das Vision-aligned? Oder zu viel für Gilden-Fantasy?"

**Warum wichtig:** Langzeitspielbarkeit. Nach 100 Stunden sollte Skill-by-Use noch sinnvoll sein.

---

## Meine Talking-Points Summary (kurz)

1. **Philosophie:** Skill-by-Use = Gilden-Weltsicht (nicht neutral)
2. **Praxis:** Erste 10 Nutzungen müssen visuell-sichtbar sein
3. **Relikt:** Potenzielle Integration? (beschleunigen oder stören?)
4. **Tech:** MVP-Check mit Tobi, falls Komplexität-Problem
5. **Narrative:** Später mit Nami koordinieren für Quest-Integration
6. **Streamer:** Skill-Upgrade-Visuals sind Alpha-Blocking (RED LINE)
7. **Zukunft:** Langzeit-Potential für Release-Scope

---

## Was ich von Darius erwarte (Output)

Nach diesem Sync sollte ich wissen:

- [ ] Ist Skill-by-Use für Alpha realistisch in diesem Scope?
- [ ] Wenn ja: Welche Metriken (Hit-Count-to-Upgrade)?
- [ ] Wenn nein: Wann können wir es revisit-en?
- [ ] Wer ist Owner für Skill-Upgrade-Visuals? (Vera? Tobi? jemand anderes?)
- [ ] Wann nächster Sync? (vor Alpha-Build? danach?)

---

## Was ich mitbringe

- [ ] Meine Retention-Daten aus 3 ähnlichen Games
- [ ] Chat-Engagement-Metriken (wann Zuschauer abschalten)
- [ ] Wolf-Checkliste (für Philosophie-Alignment)
- [ ] Alpha-Erste-Stunde-Checkliste (praktische QA-Markers)

---

**Vorbereitung (meine Seite):**
- Zweite Monitor hat Google Sheets mit Retention-Daten offen
- Dritter Tab: Wolf-Checkliste (reference)
- Vierter Tab: Skill-by-Use Mechanic-Doku (falls vorhanden, falls nicht, Darius hat seine)
- Notizbuch ist bereit für Action-Items

**Tone:**
- Collaborative (nicht adversarial)
- Data-driven (nicht gefühlsbasiert)
- Praktisch (nicht akademisch)
- Grindig, wenn nötig (ich bin die Spieler-Stimme, keine Business-Optimierung)

---

**Ziel-Outcome:**
Darius und ich sind aligned auf Skill-by-Use Philosophie + Praxis für Alpha. Klar, wer was macht, bis wann. Und ich habe Confidence, dass erste Streamer-Session keine Engagement-Disaster ist.

\clearpage

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

\clearpage

# RELICS: Spieler-Analyse & Community Research
**Leo Fischer | QA Lead | Tag 1, Szene 2**

## Die Frage
Wer spielt RELICS? Welche Communities würden das anfeuern? Und wo liegen die Fallstricke?

---

## Zielgruppe — Overlapping Circles

RELICS spricht folgende Spielertypen an:

### 1. **Immersion-First Players** (Disco Elysium, Outer Wilds, Kingdom Come Deliverance)
- Wollen sich in eine Welt **verlaufen**, nicht geklopft werden
- Lieben Dark Fantasy mit Zähnen (Elden Ring für Story-Hasser ist hier NICHT das Vorbild — sondern Hollow Knight)
- Fordern: Welt-Kohärenz, Keine Handholding, "Feeling" vor Tutorial
- Risk: Unsere erste Stunde muss knallhart geerdet sein

### 2. **Faction Player** (Baldur's Gate, Vampires the Masquerade: Bloodlines, New Vegas)
- "Ich wähle NICHT die gute Fraktion" ist ihr Satz
- Wollen Krone vs. Gilden vs. Orden spielen, ohne moralischen Zeigefinger
- Fordern: Faction-Quests, die nicht Gut/Böse sondern pragmatisch sind
- Risk: Wenn alle drei Fraktionen gleich mächtig sind, kann es sich zu "Middling" anfühlen

### 3. **Crafting/Progression Freaks** (Dark Souls, Hades, Stardew)
- Lieben sichtbare Materialsprache (das Briefing: Material = Status)
- Wollen Schwerter, die AUSSEHEN wie Schmiede-Gilde vs. Orden-Protottypen
- Fordern: Crafting-Tiefe, Upgrade-Sichtbarkeit, Materialknappheit
- Risk: Wenn wir zu viele Loot-Drops machen, wird es bloat

### 4. **Medieval Aesthetics Obsessed** (Mount & Blade, Kingdom Come)
- Lieben realistische Rüstung, Handwerk, kein Fantasy-Kitsch
- Cyberpunk-Elemente könnte sie ABSCHRECKEN, wenn es Steampunk riecht
- Fordern: Echte mittelalterliche Logik + "Tech als Geheimnis" statt sichtbar
- Risk: Biotech muss sich wie **Alchemie** anfühlen, nicht wie Sci-Fi

---

## Konkurrenzvergleich — Was sichert unser Territory?

| Spiel | Stärke | Schwäche | RELICS kann hier siegen |
|-------|--------|----------|------------------------|
| **Kingdom Come: Deliverance** | Immersion, Realismus | Langweilig, Missionen sind fetch-quests | Faction-Drama, Material-Upgrade-Sichtbarkeit |
| **Skyrim** | Open World, Vielfalt | Oberflächlich, Fraktionen sind austauschbar | Erde, politische Tiefe, Material-Bedeutung |
| **Elden Ring** | Combat, Mystery | Unzusammenhängend, Story ist optional | Narrative Tiefe, Klare Quest-Struktur |
| **Baldur's Gate 3** | Fraktionsgameplay, Verzweigung | Rundenbasiert, Team-RPG, zu viel Erzählung | Real-time, Solo-Agentschaft, Handwerk |
| **Cyberpunk 2077** | Ästhetik, Fraktionen | Spielwelt fühlt sich leblos an | Medieval = weniger "Simulationslast" |

---

## Kritische Risiken aus Spielersicht

### 1. **Medieval Cyberpunk = Identitätskrise**
Wenn es nach zwei Stunden unklar ist, ob das "Fantasy mit Tech-Flavor" oder "Cyberpunk mit Pferd" ist, springt Chat ab. Das Briefing sagt: **Material = Macht**. Das ist das Unterscheidungsmerkmal.

**Test-Kriterie:** Eine Waffe aus der Schmiede-Gilde vs. Orden sieht SOFORT anders aus. Nicht "Ordnung vs. Chaos", sondern "Legierung vs. Biotech".

### 2. **Die erste Stunde wird zum Gatekeep**
Spieler von Disco Elysium wollen keine 20-Minuten-Dialoge bei der Character-Creation. Spieler von KCD wollen rein. **Wir können nicht beide bedienen.**

**Angebot:** Tutorial-Quest, die *spielt* statt erklärt. Du wachst auf, kennst dein Handwerk nicht, musst dich beweisen. Die Welt antwortet auf deine Wahl sofort.

### 3. **Schattenfieber ist das Eisen auf der Map**
Das ist unsere "Magie ohne Magie"-Lösung. Wenn es mystisch wirkt statt biologisch, fühlt es sich wie Betrug an. Spieler merken sofort: "Das ist doch nur Magie mit anderm Namen."

**Test-Kriterie:** Schattenfieber muss sichtbar, körperlich, mit Kosten sein. Ein Spieler, der sich damit erweitert, wird GEZEICHNET. Nicht "Superkraft", sondern "Infiziert".

### 4. **Faction-Gleichgewicht ist zerbrechlich**
Krone + Gilden + Orden = drei Pole. Aber wenn zwei davon sich gegen eins verbünden, kollabiert die Spiel-Wahrheit. **Asymmetrie ist okay**, aber die Spieler müssen verstehen, warum jede Fraktion für jemanden attraktiv ist.

- Krone: Tradition, Militär, Ehre (für Cliché-Hater riskant)
- Gilden: Geld, Macht, Autonomie (für Anarchists)
- Orden: Wissen, Kontrolle, Sicherheit (für Authoritarians)

---

## Community-Radar

### Communities die RELICS lieben würden:
- /r/elderscrolls (wenn wir Open-World-Feeling liefern)
- /r/darksouls (Immersion, Material-Bedeutung)
- /r/kingdomcome (Realismus, aber fantasy-erlaubt)
- /r/Bloodborne (Gothic, Geerdet, Kämpfe mit Gewicht)
- /r/HollowKnight (Dichte statt Breite)

### Communities die sauer wären:
- Skyrim-Puristen ("Was ist dieses Cyberpunk-Zeug?")
- Cyberpunk-Fans ("Warum habt ihr mein Neon genommen?")
- Turnip-Boy-Casual-Players ("Zu düster, zu viel Mathmachiniken")

---

## Fazit für GDD Kapitel 2 (Kernmechaniken)

**Die erste halbe Stunde ist nicht Tutorial. Sie ist Angebot.**

Du wachst auf. Du kennst dein Handwerk nicht. Ein NPC braucht einen beschädigten Dolch repariert. Du hast zwei Wege: Schmiede-Gilde aufsuchen (Schulden) oder im Schwarzmarkt wild herumfummeln (Risiko). Beide Optionen sind spielbar.

In dieser halben Stunde lernt der Spieler:
- Das Gefühl von Material-Klasse (Gold Delaine vs. Tiegelstahl fühlt sich unterschiedlich an)
- Dass Welt-NPCs nicht warten (Krone patrouilliert, Orden späht, Gilden verhandeln)
- Dass Schattenfieber eine Bedrohung IST, nicht eine Quest-Lore-Notiz

Das ist der Spieler-Hook. Nicht Story. **Agentschaft.**

\clearpage

# Recherche-Notizen: Erzählkonzept RELICS
**Nami Okafor — Tag 1, Schreibstube 12e**
*Quellen: Planescape Last Rites Vision Statement (1997/2007), VtM 2nd Ed (1997)*

---

## 1. Der Fremde als epistemisches Werkzeug

Planescape löst das Einführungsproblem elegant: Weil der Spielercharakter amnestisch erwacht, wird er *zusammen* mit dem Spieler in die Welt eingeführt. Kein Infodump. Kein Wissensvorsprung. Staunen als Spielmechanik.

RELICS braucht eine andere Variante davon — unser Fremder ist kein Amnesiker, sondern ein **Außenseiter**. Er kommt von woanders. Er kennt die Regeln nicht. Die drei Fraktionen sprechen mit ihm, weil er nichts schuldet — noch nicht. Er ist tabula rasa als politische Kategorie.

Das bedeutet: Der Spieler lernt die Welt *durch Mißverständnisse*. Ein Ordensbote ist höflich und bedrohlich zugleich. Ein Gildenmeister schenkt etwas — aber Schenkungen hier sind Verbindlichkeiten. Die Krone bittet nicht, sie erwartet. Der Fremde versteht das zuerst nicht. Und dann, langsam, zu gut.

**Kernfrage**: Wem vertraue ich — und was kostet dieses Vertrauen?

---

## 2. Das Schattenfieber als Unreliable Narrator

Hier liegt das Herzstück. Das Schattenfieber ist nicht nur eine Seuche — es ist ein **Wahrnehmungsfilter**, der in den Erzähltext eingreift.

Drei Stufen, die ich mir vorstelle:

**Stufe 1 — Rauschen**: Geräusche klingen nach. Schatten bewegen sich einen Herzschlag zu spät. Der Spieler bemerkt es, der Charakter noch nicht. (Spieler als Überlegener — kurze Umkehrung: *wir* sehen, was der Charakter nicht sieht.)

**Stufe 2 — Risse**: NPCs sagen etwas. Was der Spieler liest, stimmt nicht mit dem überein, was Gesprächspartner später als Gesagtes zitieren. Wer hat gelogen — der NPC, das Interface, das Gedächtnis des Charakters? Keine Antwort.

**Stufe 3 — Schwelle**: Der Charakter beginnt Dinge zu sehen, die *wahr sein könnten*. Eine Gilde-Insignie, die kurz wie ein Totenschädel aussieht. Eine Ordensmönch-Gestalt, die einen Moment lang keine Silhouette wirft. Ist das die Krankheit — oder Erkenntnis?

VtM formuliert es anders, aber trifft dasselbe: *"We have found the enemy... and it is us."* Das Schattenfieber ist kein Außenfeind. Es wächst von innen. Es ist der Spiegel, den man lieber nicht ansieht.

**Mechanische Implikation**: Das Schattenfieber-Level sollte *sichtbar* sein, aber mehrdeutig interpretierbar. Nicht: "Du halluzinierst." Sondern: "Etwas stimmt nicht — mit dir, oder mit dieser Welt?"

---

## 3. Fraktionsmoral — keine ist gut, keine ist böse

Das ist das schwierigste Problem. Und ich glaube, die Lösung kommt nicht aus dem Kopf, sondern aus der Struktur.

VtM schafft das durch **Personal Horror**: Jede Fraktion *glaubt* moralisch zu handeln. Der Orden glaubt, Wissen zu schützen — und nennt es Inquisition. Die Krone glaubt, Ordnung zu wahren — und nennt es Erbrecht. Die Gilden glauben, Wohlstand zu schaffen — und nennen es Monopol.

Die Spieler-Lektion darf nicht sein: "Alle sind böse." Sie muss sein: **"Alle sind konsequent."** Jede Fraktion hat eine innere Logik, die sich von innen heraus *richtig* anfühlt. Man muss eine Fraktion wirklich mögen können — und trotzdem irgendwann sehen, was diese Liebe kostet.

Strukturell heißt das: Jede Fraktion braucht einen **sympathischen Einstiegspunkt** (ein Gesicht, dem man vertraut), einen **Moment der Kompliziertheit** (man sieht das System hinter dem Gesicht), und einen **Point of No Return** (man kann aussteigen — aber nicht ungestraft).

---

## 4. Erste Quest-Ideen (gelbe Post-Its, WIP)

**Intro-Quest**: Der Fremde kommt an. Weiß nicht wo, weiß nicht warum. Erster Kontakt: ein Sterbender am Stadtrand — Schattenfieber-Opfer. Er drückt dem Fremden etwas in die Hand. Was es ist, weiß man noch nicht. Drei Boten kommen fast gleichzeitig: Krone, Gilden, Orden. Alle wollen dasselbe. Der Fremde wählt, zu wem er geht.

**Hauptquest-Kern (Hypothese)**: Das Relikt ist kein Objekt der Macht — es ist ein Objekt der *Wahrheit*. Es zeigt, was wirklich ist. Wer es besitzt, kann nicht mehr lügen — oder kann nur noch lügen. (Noch offen. Muss mit dem Briefing-Relikt abgeglichen werden — was ist das Relikt dieser Iteration?)

**Nebenquest-Idee "Der Zeuge"**: Ein alter Mann in den Slums behauptet, das Schattenfieber geheilt zu haben. Er sieht Dinge, die andere nicht sehen. Ist er verrückt — oder hell? Der Spieler muss entscheiden, ob seine Informationen glaubwürdig sind, ohne je sicher zu sein.

---

\clearpage

# Technische Recherche-Notizen — RELICS
**Datum**: Tag 1, Montag, 10:00 Uhr

---

## 1. Rendering-Pipeline: Lumen + Nanite

**Nanite** ist für RELICS gesetzt. Die vertikale Stadt mit ihren Schichtungen aus poliertem Stein, Metall-Intarsien und Fachwerk-Strukturen braucht extreme Geometriedichte ohne manuelles LOD-Authoring. Risiko: Nanite hat bekannte Schwächen bei dünnen Geometrien (Ketten, Zaunstäbe, Pflanzen) — die müssen weiterhin als traditionelle Meshes mit handgestellten LODs gehandhabt werden. Knochen-Schnitzereien der Unterschicht und Zunftzeichen-Reliefs sind gute Nanite-Kandidaten.

**Lumen** für Global Illumination ist der richtige Ansatz, aber die vertikale Stadtstruktur stellt ein ernstes Problem: Lumen arbeitet mit Screen-Space-Fallbacks und Software-Raytracing in einem fixen Radius. Tiefe Kanäle, überhängende Arkaden, Slum-Bereiche unter Brücken — überall dort, wo der Himmel nicht sichtbar ist, degeneriert Lumen-GI. **Lösung**: Hardware-Raytracing aktivieren wo Budget es erlaubt, kombiniert mit manuell platzierten Lumen-Importance-Volumes für kritische Innenräume (Gildenhallen, Ordenskorridore). Für die Slum-Kanäle: statisches Baked Lighting als Fallback definieren.

**Fazit Rendering**: Machbar. Kein Experiment, sondern Handwerk. Die Kombination aus Lumen-Hardware-RT für obere Stadtebenen und Hybrid-Baking für untere Ebenen ist ein etabliertes Muster. Zeitaufwand für Setup-Phase: realistisch 3–4 Wochen für eine stabile Basis-Pipeline.

---

## 2. Biolumineszenz — Emissive in Lumen

Das Briefing setzt auf Biolumineszenz als Neon-Äquivalent: phosphoreszierende Mineralien, Alchemie-Leuchtstoffe. Das ist technisch der interessanteste Teil.

In UE5 funktioniert Emissive mit Lumen gut — Emissive-Flächen werden als Lichtquellen behandelt, wenn der Mesh als "Emissive Light Source" flagged ist. **Problem**: Bei vielen kleinen Emissive-Quellen (hunderte Pilze, Alchemie-Phiolen, Buntglasfenster) explodiert der Performance-Overhead. **Lösung**: Emissive-Quellen in drei Klassen einteilen:

- **Klasse A** (hero lights): Echte Lumen-Emitter. Wenige, sorgfältig platzierte Stücke pro Szene — die Bergkristall-Linsen der Oberschicht, die großen Alchemie-Lampen der Gilden.
- **Klasse B** (ambient glow): Emissive-Material ohne Lumen-Light-Source-Flag. Leuchten visuell, strahlen aber kein GI ab. Für Füllmaterial in Slum-Bereichen.
- **Klasse C** (VFX): Particle-basierte Biolumineszenz für organische Leuchtelemente (Pilze, Schimmel). Niagara-System, skalierbar über Qualitätsstufen.

**FFXIV-Referenz**: Die v2.0-Specs zeigen, dass Square Enix Materiallesbarkeit durch starke Kontrast-Hierarchien sicherte — helle, klar definierte Emissive-Stellen auf dunklen Basismaterialien. Das ist für RELICS direkt anwendbar: die Biolumineszenz muss lesbar sein, nicht überwältigend.

---

## 3. Schattenfieber — VFX-Stufen (Post-Processing)

Das Schattenfieber ist das einzige Übernatürliche im Spiel. Die visuelle Eskalation muss in der Pipeline klar definiert sein, damit Nami und Vera konsistent arbeiten können.

**Drei Stufen, Post-Process Volume gesteuert:**

**Stufe 1 — Frühinfektion (subtil):** Leichte Chromatic Aberration an Bildrändern (+/- 0.3 Pixel max). Gelegentliches Film Grain-Aufflackern. Farbtemperatur minimal kühler (Bloom-Tint Richtung Cyan). Der Spieler soll unsicher sein, ob er etwas sieht.

**Stufe 2 — Fortgeschritten (eindeutig):** Vignetierung verstärkt. Pulsierendes Depth of Field im Nahbereich (simuliert veränderte Wahrnehmung). Schatten-Bereiche des Bildes erhalten einen Indigo-Tint durch Color Grading Curve. Geometrie "atmet" leicht — vertex-animierte Umgebungsobjekte im sichtbaren Radius (±2cm Oszillation). Risiko: das kann Spieler mit Motion-Sickness-Empfindlichkeit treffen. Accessibility-Option muss her.

**Stufe 3 — Kritisch (Grenze zur anderen Seite):** Full-Screen-Shader-Overlay mit organischen Riss-Strukturen (inspiriert von den planes of existence beyond known reality aus dem Briefing). Welt-Geometrie zeigt temporäre "Lücken" — schwarze Flächen, durch die Dunkelheit scheint. Nervensystem-Visualisierung startet automatisch. Das ist der gefährlichste State — Spieler kann Fähigkeiten nutzen, aber die Wahrnehmung ist kompromittiert.

**Implementierung**: Alle drei Stufen als Parameter-Set in einem Blueprint-System. Smooth Blending zwischen Stufen über Timeline-Nodes. Kein Hard-Cut.

---

## 4. Vertikale Stadt — Occlusion, LOD, Sichtlinien

Die größte technische Herausforderung des Projekts. Die Stadt ist vertikal geschichtet wie eine Cyberpunk-Metropole — Macht oben, Slums unten. Das bedeutet:

**Occlusion**: Massive Überhänge und Brückenstrukturen blockieren natürliche Sichtlinien. UE5-Occlusion-Culling funktioniert horizontal gut, hat aber Schwächen bei starker Vertikalität. **Empfehlung**: Manuelle Occlusion Volumes für die Hauptebenen-Übergänge. Jede Stadtebene bekommt einen eigenen "Sichtbereich" — was von oben nicht sichtbar ist, wird aggressiv gecult. Das setzt voraus, dass das Level-Design Ebenen als diskrete Zonen behandelt.

**Streaming**: World Partition in UE5 ist Pflicht. Vertikale Achse muss in der Partitionierung berücksichtigt werden — UE5 World Partition ist primär horizontal konzipiert. Lösung: Manuelle Data Layers für Vertikalschichten (Layer 0: Untergrund/Kanäle, Layer 1: Straßenebene, Layer 2: Brücken/Arkaden, Layer 3: Türme/Gilden).

**Dark Souls-Referenz**: FromSoftware verwaltet Materiallesbarkeit durch starke Hell-Dunkel-Kontraste und begrenzte Farbpaletten pro Zone. Das ist für RELICS nützlich: jede Vertikalebene bekommt eine dominante Lichtstimmung (Oben: kaltes Tageslicht durch Bergkristall-Linsen; Mitte: warmes Kerzenlicht, Buntglas-Farbflecken; Unten: phosphoreszierendes Blau-Grün, Feuerschein). Lesbarkeit durch Licht, nicht durch Komplexitätsreduktion.

---

## 5. Kamerasystem — Third/First Person nahtlos

Skyrim-Referenz ist explizit im Briefing. Umsetzung in UE5:

**Ansatz**: Eine Camera-Komponente, zwei Modi. Kein Kamera-Swap, sondern Blend zwischen Offset-Position (Third-Person: 200cm hinter, 80cm über Schulter) und Eye-Position (First-Person: exakte Head-Socket-Koordinate). Blend-Zeit: 0.3 Sekunden, Ease-In/Out-Kurve.

**Herausforderung**: Das Nervensystem-Leveling-System zeigt halbtransparente Körper-Overlays (Cardio, Muskel, Lymph). Im Third-Person-Modus ist das trivial — Overlay auf Character Mesh. Im First-Person-Modus brauchen wir einen separaten "Arm Mesh", der das eigene Körper-Nervensystem in der Kamera-Perspektive zeigt. Das ist ein separates Mesh-Set, das synchron animiert werden muss. **Aufwand: mittel-hoch.**

**FOV**: Third Person: 90° empfohlen für das Gefühl von Raum in der vertikalen Stadt. First Person: 95–100° für Immersion in engen Gängen (Slums, Ordenskorridore). Beide als Spieler-Option exposiert.

---

## 6. Risiko-Übersicht

| System | Machbarkeit | Hauptrisiko |
|---|---|---|
| Nanite Geometrie | Hoch | Dünne Geometrien, erfordern Fallback |
| Lumen GI vertikal | Mittel | Degeneriert in tiefen Kanälen — Hybrid-Baking nötig |
| Biolumineszenz-Skala | Mittel | Performance bei vielen Emittern — Klassifizierung nötig |
| Schattenfieber PP | Hoch | Accessibility-Risiko bei Stufe 2/3 |
| Vertikales Culling | Mittel-Hoch | UE5 World Partition primär horizontal |
| Kamera-Blend | Hoch | Nervensystem-Arm-Mesh erhöht Aufwand |

**Gesamteinschätzung**: Das Projekt ist technisch machbar mit UE5. Kein System erfordert Custom-Engine-Arbeit. Die kritischste Entscheidung, die früh getroffen werden muss: wie diskret sind die Stadtebenen? Je klarer das Level-Design die Vertikalschichten trennt, desto robuster wird die gesamte technische Pipeline.

---

*Nächster Schritt: Abstimmung mit Vera über Vertikalstruktur. Abstimmung mit Nami über Post-Process-Stufen des Schattenfiebers.*

\clearpage

# Wolf-Checkliste für RELICS: Alpha-Build QA

**Kontext:** Spielerperspektiv-Prüfwerkzeug basierend auf Mark J. P. Wolfs neun Infrastrukturen imaginärer Welten (2013, Kap. 3)
**Verwendung:** QA-Checkliste für Konsistenz + Spielerimmersion. Was merkt der Spieler? Was ist nur Backend?

---

## Überblick: Die neun Infrastrukturen

Wolf definiert neun "Sekundäre Welten-Infrastrukturen" als Gerüst, das Welten konsistent hält:
1. **Karten** (Maps) — räumliche Struktur
2. **Zeitleisten** (Timelines) — chronologische Ordnung
3. **Genealogien** (Genealogies) — Figurennetze
4. **Natur** (Nature) — Flora, Fauna, Ökologie
5. **Kultur** (Culture) — Bräuche, Alltag, Religion
6. **Sprache** (Language) — Namenssysteme, Dialekte
7. **Mythologie** (Mythology) — Schöpfungsmythen, Legenden
8. **Philosophie** (Philosophy) — Weltsicht, Ethik
9. **Verknüpfung** (Tying Together) — Wechselwirkungen

**Leo's Twist:** Für jede Infrastruktur unterscheide ich zwischen:
- **SICHTBAR:** Was der Spieler im Gameplay merkt (UI, Mechaniken, NPCs, Dialog, Umgebung)
- **BACKEND:** Konsistenz, die nur bei Close-Reading auffällt (Lore-Kohärenz, historische Tiefe)
- **CRITICAL:** Fehler, die Immersion killen

---

## 1. KARTEN — Topografie & räumliche Navigation

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Stadtarchitektur visuell kohärent**
  - Oberschicht-Viertel: Brutalistisch, Bauhaus, Hängende Gärten. Sichtbar unterschiedlich von Unterschicht.
  - Unterschicht: Versteckt, Kanäle, Slums. Muss sich "getrennt" anfühlen. Nicht zufällig verteilt.
  - **SICHTBAR:** Erste 5 Min — sieht Spieler die vertikale Schichtung? (Krone/Orden oben, Gilden verteilt, Slums unten)
  - **CRITICAL:** Wenn ein Oberschicht-NPCs-Palazzo neben einer Slum-Hütte steht ohne Übergangsviertel = Glaubwürdigkeit kaputt

- [ ] **Karte funktioniert als Spielsandbox**
  - Kann ich frei navigieren oder bin ich auf Pfaden?
  - Gibt es explorative Anreize (abseits gelegene Höhlen, versteckte Queste)?
  - **SICHTBAR:** Gameplay-Freiheit in den ersten 30 Min. "Kann ich dorthin?"
  - **BACKEND:** Konsistente Wegfindung ohne Clipping/Phasing

- [ ] **Relikt-Resonanz an räumlichen Ankerpunkten**
  - Das Relikt sitzt an einer "dünnen Stelle" (Schwellen-Konzept). Ist diese räumlich wahrnehmbar?
  - Gibt es visuelle Anomalien um das Relikt (Flora/Fauna?), die die Spielerin hinzieht?
  - **SICHTBAR:** Erste Begegnung mit Relikt sollte sich UNTERSCHIEDLICH anfühlen vom Rest der Map
  - **CRITICAL:** Wenn Relikt wie ein normales Gegenstand aussieht = Spieler verpasst es, Darius hat Angst

- [ ] **Fraktions-Gebiete räumlich erkennbar**
  - Krone: Schloss, Verwaltung (Zentral?)
  - Orden: Klöster, Archive (oben/Höhe?)
  - Gilden: Werkstätten, Märkte (verteilt)
  - **SICHTBAR:** Nach 1 Stunde soll Spieler wissen: "Ah, DAS ist Krone-Gebiet"
  - **BACKEND:** Konsistente Fahnenmale, Wappenschilder, Architektur-Codes

---

## 2. ZEITLEISTEN — Geschichte, Konflikte, Wendepunkte

### Spielerperspektive: Was merkt der Spieler?

- [ ] **"Sterbender gibt Fremden Relikt-Scherbe" — temporale Klarheit**
  - Ist der Wendepunkt zeitlich verankert? ("Der König starb letzte Nacht", "Es ist drei Tage vor der Krönung")
  - **SICHTBAR:** Dialog-Exposition ohne Codex-Dump. NPCs sollten Zeit-Kontext natürlich erwähnen
  - **CRITICAL:** Wenn Spieler nach 1 Stunde nicht weiß, "wann" das Spiel stattfindet = Problem

- [ ] **Fraktions-Spannungen zeitlich nachvollziehbar**
  - Krone vs. Orden vs. Gilden — gibt es einen Konflikt, der GERADE läuft?
  - Spieler sollte verstehen: "Warum können diese Fraktionen nicht einfach miteinander reden?"
  - **SICHTBAR:** Erste Quest-Einstieg sollte zeigen, dass Fraktions-Asymmetrie ECHT ist
  - **BACKEND:** Zeitleiste mit konkreten Ereignissen (nicht nur "irgendwann war Krieg")

- [ ] **Relikt-Historischer Kontext**
  - Ist das Relikt ALT? Oder NEU?
  - Gab es Vorkommnisse? (andere Relikte, Schatten-Krisen?)
  - **SICHTBAR:** Optional-Lore für neugierige Spieler (Codex-Einträge, NPC-Dialog)
  - **BACKEND:** Konsistente Zeitleiste, die keinen Anachronismus erzeugt

- [ ] **Schattenfieber — zeitliche Eskalation**
  - Wird es schlimmer? Gibt es Berichte von Infizierungen?
  - **SICHTBAR:** Ambient-Dialog-Scheints ("Hast du gehört, dass dritte Kind in der Gasse...")
  - **CRITICAL:** Wenn Schattenfieber sich nicht als ZEITLICHE BEDROHUNG anfühlt = Spieler nimmt es nicht ernst

---

## 3. GENEALOGIEN — Figurennetze & Dynastien

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Fraktions-Hierarchien sichtbar**
  - Krone: König, Adel, Soldaten (vertikale Hierarchie)
  - Orden: Patriarch, Priester, Inquisitoren (Autorität-Struktur)
  - Gilden: Meister, Gesellen, Lehrlinge (Kompetenz-Struktur)
  - **SICHTBAR:** Erste 30 Min — Spieler sollte wenig Haupt-NPCs pro Fraktion kennen, aber ihre Rollen verstehen
  - **CRITICAL:** Wenn NPCs ohne erkennbare Rolle auftreten = verwirrt

- [ ] **"Familie" als Einstieg in Erzählung**
  - Der sterbende NPC hat eine Familie? Feinde? Verbündete?
  - Spieler sollte EMOTIONAL an dieser Figur hängen, nicht nur mechanisch
  - **SICHTBAR:** Dialog-Chemie, Voice-Acting, Animation. Macht die Sterbeszene FEEL?
  - **BACKEND:** Genealogie-Konsistenz (wer ist mit wem verwandt, beruflich, romantisch?)

- [ ] **Fraktions-interne Spannungen (Genealogie)**
  - Gibt es Rivalen INNERHALB einer Fraktion?
  - Z.B. zwei Gildenmeister, die unterschiedliche Positionen haben?
  - **SICHTBAR:** Quest-Verzweigungen sollten zeigen: "Die Krone ist nicht eins. Es gibt unterschiedliche Agenden."
  - **BACKEND:** NPC-Listen mit Beziehungen

---

## 4. NATUR — Flora, Fauna, Ökologie

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Schattenfieber verändert Biologie sichtbar**
  - Infizierte Tiere: merkwürdig? Gefährlich? Biolumineszent?
  - **SICHTBAR:** Wenn Spieler infiziert wird, soll sie körperlich SPÜREN, dass was falsch ist
  - **CRITICAL:** Wenn Schattenfieber als "magische Krankheit" wirkt statt "biologische Mutation" = Tonalität-Fehler

- [ ] **Mitteleuropäische Ökologie (nicht generisch Fantasy)**
  - Waldtypen: Laubwald, Nadelwald (geografisch sinnvoll)
  - Jahreszeiten: Sichtbar? (im Spiel-Zeitablauf)
  - **SICHTBAR:** Environment Art sollte SEIN, nicht "Generic Medieval Forest"
  - **BACKEND:** Vera's Responsibility. Leo prüft: Fühlt sich die Natur vertraut + übernatürlich an?

- [ ] **Tiervolk: Material-Handel, nicht mystisch**
  - Tiervolk = "Händler und Diebe, nicht Handwerker" (Briefing)
  - Sie sollten MODERN-Cyberpunk wirken: Finesse, Diebstahl, Netzwerke
  - **SICHTBAR:** Wenn Tiervolk auftritt, sollte es anders SPIELEN (schneller, politischer)
  - **CRITICAL:** Kein tribal-Magic-Vibe. Sie sind Cyberpunk-Operatoren.

---

## 5. KULTUR — Bräuche, Alltag, Religion

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Material-Klasse ist SICHTBAR**
  - Oberschicht: All-Black, All-White, Monochrom + einzelner neon-Akzent
  - Mittelschicht: Erdtöne, gedeckte Farben
  - Unterschicht: Grau, Braun, schmutzig + gestohlene leuchtende Teile
  - **SICHTBAR:** Nach 30 Min sollte Spieler wissen: "Dieser NPC ist Oberschicht, weil er nur Weiß trägt"
  - **CRITICAL:** Wenn Materialsprache konsistent, Immersion steigt. Wenn chaotisch, wirkt Welt billig.

- [ ] **Alltag ist erkennbar (nicht nur Combat)**
  - Zivile NPCs machen was? (Weber webt, Schmiede schmiedet, Mönch betet?)
  - **SICHTBAR:** Ambient-Animation, AI-Schedules. Leben sich nicht live anfühlen?
  - **BACKEND:** Gilden-Monopole sollten sich in Alltag widerspiegeln (warum gibt es nur eine Schmiede?)

- [ ] **Religion (Orden) ist subtil, nicht mystisch**
  - Orden = Bildungsmonopol + Überwachung (Briefing)
  - Sind Mönche sichtbar in der Stadt? Inquisitoren?
  - **SICHTBAR:** Kirchen/Klöster sollten sich von Schloss/Werkstatt unterscheiden
  - **CRITICAL:** Kein "magischer Glaube". Orden sollte politisch-rational wirken

- [ ] **Bräuche: Fraktions-spezifisch**
  - Krone: Tournamente, Hofzeremoniell?
  - Orden: Prozessionen, Archive?
  - Gilden: Zunfttreffen, Meisterschaften?
  - **SICHTBAR:** Optional-Queste sollten diese Bräuche zeigen
  - **BACKEND:** Nami's Responsibility. Aber Leo prüft: Würde Streamer das interessant finden?

---

## 6. SPRACHE — Namenssysteme, Dialekte

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Namen sind germanisch (keine Generik-Fantasy)**
  - Krone: Hochdeutsche Namen (Friedrich, Margarete, Leopold)
  - Orden: Religiöse Namen (Gottfried, Agnes, Bruno)
  - Gilden: Handwerks-Familiennamen (Müller, Weber, Schmidt)
  - Tiervolk: ???  (noch zu definieren mit Team)
  - **SICHTBAR:** Wenn Spieler einen Namen hört, sollte sie Fraktions-Zugehörigkeit erraten können
  - **CRITICAL:** Wenn Namen generisch wirken ("Zarthaxion") = Fantasy-Cliché-Gefühl

- [ ] **Dialekte (optional, aber impactful)**
  - Unterschicht spricht anders als Oberschicht?
  - Tiervolk hat Akzent?
  - **SICHTBAR:** Voice-Acting. Unterschiedliche Dialekte machen Welt DICHT
  - **BACKEND:** Nicht übertreiben (Spieler soll verstehen, nicht verwirrt sein)

- [ ] **Codex-Sprache konsistent mit Dialog**
  - Wenn Spieler Lore liest, soll es sich wie "aus dieser Welt" anfühlen
  - **BACKEND:** Nami's Responsibility. Leo prüft: Zu akademisch? Oder lebendig?

---

## 7. MYTHOLOGIE — Schöpfungsmythen, Legenden, Prophezeiungen

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Relikt hat mythologischen Ursprung**
  - Wer hat das Relikt geschaffen? Woher kommt es?
  - Optional-Lore für Deep-Dive-Spieler
  - **SICHTBAR:** Erste Begegnung sollte RÄTSELHAFT sein (nicht erklärend)
  - **CRITICAL:** Spieler soll fühlen: "Das ist älter als alles, was ich kenne"

- [ ] **Germanische Mythologie (subtil)**
  - Yggdrasil-Referenzen? (Schwellen zwischen Welten?)
  - Wotan/Orden-Parallele?
  - **SICHTBAR:** Optional. Nur für Spieler, die suchen.
  - **BACKEND:** Darf NICHT forciert sein. Tonal leicht, nicht "preachy"

- [ ] **Jede Fraktion hat ihre Mythologie**
  - Krone: "Wir sind von alten Königen abstammend"
  - Orden: "Wissen ist heilig"
  - Gilden: "Material = Macht"
  - **SICHTBAR:** NPCs sollten ihre Weltsicht durch Mythen ausdrücken
  - **BACKEND:** Mythologische Konsistenz (widersprechen sich die Mythen? Absicht?)

---

## 8. PHILOSOPHIE — Weltsicht, Ethik, Wertesysteme

### Spielerperspektive: Was merkt der Spieler?

- [ ] **"Skill-by-Use" hat philosophischen Grund**
  - Krone: "Erbe = Macht" (Geburt)
  - Orden: "Bildung = Macht" (Wissen)
  - Gilden: "Handwerk = Macht" (Praxis)
  - Spieler: Du lernst durch Tun (Skill-by-Use) — also philosophisch GITDERN-aligned, nicht Order-aligned
  - **SICHTBAR:** Nach Skill-Upgrade sollte Dialog-Option anders sein ("Ich WEISS jetzt, wie man das macht")
  - **CRITICAL:** Skill-System muss spielerisch mit Weltanschauung SYNC sein

- [ ] **"Echte Fraktionswahl" hat ethischen Grund**
  - Krone: "Ich will Ordnung" (Tradition)
  - Orden: "Ich will Kontrolle" (Wissen)
  - Gilden: "Ich will Wohlstand" (Material)
  - **SICHTBAR:** Jede Quest sollte drei Lösungen haben (jeweils Fraktion-aligned)
  - **CRITICAL:** Spieler soll nicht fühlen: "Alle Fraktionen sind gleich." Sie sollten echte Dilemmen sein

- [ ] **Schattenfieber: philosophische Bedrohung**
  - Was passiert, wenn der Körper / die Hierarchie / das Wissen kaputt geht?
  - **SICHTBAR:** Infizierte NPCs sollten VERZWEIFELT sein, nicht nur "zombie-like"
  - **BACKEND:** Schattenfieber-Philosophie mit Emre klären (Was bedeutet es, infiziert zu sein?)

---

## 9. VERKNÜPFUNG — Wechselwirkungen zwischen Infrastrukturen

### Spielerperspektive: Was merkt der Spieler?

Diese ist die WICHTIGSTE für Immersion. Alle neun Infrastrukturen sollten ZUSAMMENHÄNGEN.

- [ ] **Karte + Kultur = Raum-Verhalten**
  - Oberschicht-Viertel: Ruhig, organisiert, sichtbare Wachen
  - Unterschicht: Chaotisch, schnell, versteckte Drusen-Quellen
  - Wenn Spieler durch verschiedene Viertel geht, sollte GAMEPLAY sich unterscheiden
  - **SICHTBAR:** Encounters, NPCs, Loot sollten schicht-konsistent sein
  - **CRITICAL:** Wenn Unterschicht wie Oberschicht spielbar ist = Immersion kaputt

- [ ] **Zeitleiste + Mythologie = Sinnhaftigkeit**
  - "Vor 500 Jahren kam das Relikt" (Zeitleiste) = "Deshalb ist es in DIESEM Tempel" (Mythologie + Karte)
  - **SICHTBAR:** Wenn Spieler Environment erforscht, Lore sollte räumliche Strukturen erklären
  - **BACKEND:** Nami + Emre sollten koordinieren

- [ ] **Genealogie + Fraktions-Philosophie = NPC-Motivation**
  - Eine Krone-Adelige hat Grund, Orden zu bekämpfen, weil ihre PHILOSOPHIE unterschiedlich ist
  - Nicht random Feindschaft, sondern strukturelle Unverträglichkeit
  - **SICHTBAR:** Wenn Spieler NPC-Quests macht, sollte Motivation aus Weltbau klar sein
  - **CRITICAL:** Keine "just because"-Quests. Alles muss aus Weltkohärenz folgen

- [ ] **Kultur + Sprache + Natur = Glaubwürdigkeit**
  - Wenn eine Gegend AUSSIEHT wie Mitteleuropa (Natur), KLINGT wie Deutsch (Sprache), und LEBT wie MA (Kultur), ist Immersion komplett
  - **SICHTBAR:** Gesamtes Paket: Environment + NPC-Aussehen + Dialog + Alltag
  - **CRITICAL:** Wenn eins nicht passt, wirkt alles falsch

- [ ] **Relikt + alle neun Infrastrukturen = Welt-als-Charakter**
  - Das Relikt sollte nicht nur Mechanic sein, sondern VERKÖRPERUNG aller Infrastrukturen
  - Relikt-Geschichte = Mythologie
  - Relikt-Effekt auf Flora/Fauna = Natur
  - Relikt-Konflikt zwischen Fraktionen = Philosophie
  - Relikt-Resonanz = Karte
  - usw.
  - **SICHTBAR:** Wenn Spieler Relikt interagiert, sollte es sich wie KERN der Welt anfühlen
  - **CRITICAL:** Relikt darf nicht isoliert sein. Es muss ALLES durchdringen.

---

## Praxis: Checklisten-Workflow (QA-Einsatz)

### Alpha-Build-Test (erste 60 Minuten)

**Tag 1: SICHTBAR-Checks** (was merkt der Spieler?)
1. Starte Spiel. Keine Designdocs vorher lesen.
2. Notiere in nächsten 5 Min: Welche Infrastruktur-Signale merke ich?
   - Sehe ich unterschiedliche Schichten? (Karte + Kultur)
   - Höre ich verschiedene Sprachstile? (Sprache)
   - Merke ich zeitliche Urgency? (Zeitleiste)
3. Nach 30 Min: Schreibe "Erste-Eindruck-Bericht" (Spielerperspektive)
4. Nach 60 Min: Ist die Fraktions-Wahl ECHT? (Philosophie)

**Tag 2: BACKEND-Checks** (Lore-Konsistenz)
1. Lese alle verfügbaren Codex/Lore-Einträge
2. Prüfe: Widersprechen sich Zeitleiste + Mythologie?
3. Prüfe: Sind NPC-Genealogien konsistent?
4. Schreibe "Lore-Audit"-Bericht

**Day 3: VERKNÜPFUNG-Checks** (Weltkohärenz)
1. "Wenn ich die Karte als Person nehmen würde: Macht sie Sinn?"
2. "Wenn ich die Regeln des Relikt-Philosophie nehme: Erklärt es die Welt?"
3. Schreibe "Weltkohärenz"-Bericht

### Beispiel-Bug-Report (mit Wolf-Infrastruktur)

```
RELICS: Alpha, Erste Stunde
Infrastruktur: Karte + Kultur
Severity: HIGH (Immersion)

Beschreibung:
Nach Intro treffe ich auf reiche Kaufleute in Slum-Viertel.
Sie tragen All-White-Oberschicht-Klamotten.
Umgebung ist aber eindeutig Unterschicht (morsche Häuser, Ratten).

Problem:
- Material-Klasse (Kultur) passt nicht zu räumlichen Kontext (Karte)
- Spieler: "Warum sind Oberschicht hier? Sind die verloren?"

Lösung:
Option A: NPCs umziehen zu Oberschicht-Viertel
Option B: NPC-Kostüme ändern zu Mittelschicht
Option C: Dialog erklären warum Oberschicht hier ist
```

---

## Mein QA-Fokus für RELICS Alpha

**Kanarienvogel-Rolle (Leo streamt für 47K Follower):**

Das wichtigste ist nicht, dass alle 9 Infrastrukturen PERFECT sind.
Sondern dass sie KOHÄRENT FÜHLEN.

1. **Minute 0–5:** Merkt Streamer-Chat die Material-Klasse? ("Ooh fancy" vs. "meh")
2. **Minute 5–10:** Hängt Spieler emotionell am sterbenden NPC? (Genealogie + Kultur + Dialog)
3. **Minute 10–15:** Versteht Spieler die zeitliche Situation? ("Warte, wann findet das statt?")
4. **Minute 15–30:** Gibt es ECHTE Fraktionswahl oder nur Illusion? (Philosophie)
5. **Minute 30–60:** Fühlt sich Relikt-Resonanz WOW an oder buggy? (Alle Infrastrukturen)

Wenn Chat nicht abschaltet beim Intro = SUCCESS.

---

\clearpage

# GDD Kapitel 01 — Spielübersicht & Design-Säulen (v1)

**Quellen:** Briefing, Deus Ex GDD v5.3e (Spector/Ion Storm 1997), Diablo Pitch Document (Condor 1994), eigene Recherche-Notizen Tag 1, Emre-Output Tag 2, Nami-Notizen Tag 1, Leo-Analyse Tag 1

> Dieses Kapitel definiert das "Was" und das "Warum" von RELICS — bevor irgendeine Mechanik beschrieben wird. Nach Spector: Philosophie zuerst, Systeme danach. Alle Folgekapitel müssen auf diesen Design-Säulen aufbauen können.

---

## 1. Projekttitel & Format

**Serientitel:** RELICS
**Erste Iteration:** RELICS: Die Wurzel *(Arbeitstitel — wartet auf CD-Freigabe)*
**Format:** Single-Player Computer-Rollenspiel
**Perspektive:** Third-Person / First-Person, nahtlos umschaltbar
**Monetarisierung:** Premium, einmaliger Kaufpreis — keine Mikrotransaktionen, keine kleinen Add-ons. DLCs nach Full Release, ausschließlich groß.

---

## 2. High Concept Statement

RELICS fragt: *Wem gehört diese Welt — und was bist du bereit zu tun, um darin zu überleben?*

Du bist ein Fremder. Du weißt nicht, wer du warst. Du weißt nicht, warum du hier bist. Aber die Stadt vor dir funktioniert ohne dich — sie hat Regeln, Mächte, Hierarchien, die sich über Jahrhunderte eingeschliffen haben. Drei Fraktionen teilen die Welt unter sich auf: die Krone mit ihrem Militär und ihren leeren Kassen, die Gilden mit ihren Monopolen und ihrem Geld, der Orden mit seinem Wissen und seiner Inquisition. Keine ist gut. Keine ist böse. Alle sind konsequent.

Und dann gibt es das Schattenfieber. Eine Seuche, die den Körper verändert. Jede Fraktion hat eine andere Erklärung — alle drei liegen falsch, aber jede liegt anders falsch. Die Wahrheit liegt tiefer. Unter der Stadt, in der Stille unter dem Stein, wartet etwas, das die Grenze zwischen den Ebenen des Seins zusammenhält. Es heißt Die Wurzel. Es schwächt sich ab. Und das Fieber breitet sich aus.

Du wirst hineingezogen, ob du willst oder nicht. Was du daraus machst — das ist das Spiel.

---

## 3. Spieler-Fantasie-Statement

**"Ich betrete als Fremder eine aufregende Sandbox."** *(Briefing, unveränderlich)*

Ausformuliert für das Design-Team:

Der Spieler soll sich fühlen wie jemand, der eine fremde Stadt zum ersten Mal betritt und merkt, dass sie *funktioniert* — Händler handeln, Wachen patrouillieren, Gildenmeister verhandeln, Ordensboten eilen durch Gassen. Er ist das Störelement. Die Welt hat ohne ihn existiert. Sie lässt ihn rein — zögernd, abwartend, mit Hintergedanken.

Das Versprechen: *Ich kann hier meine eigene Geschichte schreiben. Nicht eine Geschichte, die mir das Spiel aufzwingt. Meine.*

Drei konkrete Fantasien, die dieses Statement trägt:

1. **Agentschaft:** Ich löse jedes Problem auf meine Weise. Schleiche ich durch den Gilden-Checkpoint, bestehe ich ihn oder erkaufe ich mir Durchgang?
2. **Aufstieg:** Ich fange mit Eisengerät an und arbeite mich in eine Welt vor, in der Titan-Legierungen und Tiegelstahl die Sprache der Macht sind. Mein Körper ist mein Fortschrittsanzeiger.
3. **Konsequenz:** Meine Entscheidungen formen die Welt. Wenn ich für die Gilden arbeite, verschließt mir der Orden Türen. Das ist kein Bug. Das ist der Vertrag.

---

## 4. Game Feel

Spector schreibt im Deus Ex-GDD nicht "das Spiel soll sich gut anfühlen". Er beschreibt eine *Körperempfindung*. Das ist der Standard.

**RELICS-Game-Feel in einem Satz:**
*Ich stehe am Rand einer lebendigen, gefährlichen Welt und spüre, dass meine nächste Entscheidung etwas verändert.*

**Textur dieser Empfindung:**
- Schwere. Kämpfe sind nicht flüssig und elegant — sie kosten etwas. Ein Schwerthieb fordert Kraft, eine Parade fordert Timing. Der Körper des Spielers ist spürbar.
- Reibung. Die Stadt gibt sich nicht preis. Gilden-Tore sind gesperrt. Ordenswächter beobachten. Die Krone erwartet. Diese Reibung ist kein Fehler — sie ist das Medium, durch das sich Fortschritt anfühlt.
- Staunen + Bedrohung. Die Biolumineszenz in den Kanälen leuchtet schön. Sie leuchtet, weil dort das Fieber am stärksten ist. Die Welt ist attraktiv und gefährlich zur selben Zeit.
- Dichte. Jeder NPC hat eine Funktion, einen Tagesablauf, ein Gesicht. Niemand steht als Dekoration herum. Das fühlt sich nicht wie ein Videospiel an — es fühlt sich wie eine Welt an.

---

## 5. Genre & Perspektive

| Parameter | Wert |
|---|---|
| Genre | Action-RPG / Immersive Sim |
| Ton | Dark Fantasy — düster, geerdet, politisch |
| Setting | Medieval Cyberpunk: frühes Spätmittelalter + High-Tech-Materialien |
| Perspektive | Third-Person (Standard) / First-Person (umschaltbar) |
| Weltstruktur | Semi-Open-World: dichte, handgefertigte Kernregion statt weiter Leerfläche |
| Kampf | Real-Time Action, Melee-fokussiert, gewichtig |
| Magie | Keine. Alchemie + Schattenfieber-Mutationen (mit Kosten) |
| Referenzen | Gothic 2, Deus Ex, Vampires the Masquerade: Bloodlines, Prey 2017 |
| Explizite Nicht-Referenzen | Kein Steampunk. Kein High Fantasy. Kein Zauberstab. |

**Verortung auf dem Fantasy-Spektrum:**
Medium-Fantasy — zwischen Low und High. Low-Magic, High-Tech (Materialien als Technologie). Biotech-Futurismus, der sich von innen wie Alchemie anfühlt, nicht wie Science-Fiction.

---

## 6. Die vier Design-Säulen

Diese vier Säulen sind Designfilter, keine Marketingversprechen. Jedes Feature, das in die Produktion geht, muss gegen mindestens zwei dieser Säulen bestehen. Features, die keine einzige Säule stärken, werden gestrichen.

---

### Säule I — Immersive Simulation

**Statement:** Jedes Problem hat mehr als eine Lösung. Die Welt reagiert konsequent auf das, was der Spieler tut.

**Was das bedeutet:**
- NPCs verhalten sich nach eigener Logik, nicht nach Spieler-Bequemlichkeit. Ein Gildenmeister macht keine Ausnahmen, weil der Spieler nett fragt — er macht sie, wenn der Spieler etwas wert ist.
- Physische Eigenschaften der Welt sind konsistent. Eine verschlossene Tür bleibt verschlossen, bis der Spieler den Schlüssel hat, sie aufbricht, das Schloss knackt oder einen anderen Eingang findet. Es gibt keinen magischen "Interagiere"-Knopf.
- Fraktionsentscheidungen haben echte systemische Konsequenzen. Wer für den Orden arbeitet, verliert Gilden-Ruf. Das System buchführt still.
- Mehrere Lösungswege sind keine Checkboxen ("Stealth/Kampf/Dialog") — sie entstehen aus dem Zusammenspiel von Spieler-Fähigkeiten, Umgebung und Fraktionsstand.

**Spieler-Fantasie:** *"Diese Welt reagiert auf mich. Ich bin nicht auf einem Schienen-Trip."*

**Referenz:** Spector (Deus Ex GDD, 1997): "The world simulation allows players to solve problems in a variety of ways."

---

### Säule II — Fraktionspolitik als Kernspannung

**Statement:** Kein Gut gegen Böse. Drei konkurrierende Mächte, jede mit innerer Logik, jede mit konkreten Ressourcen, die sie kontrollieren.

**Was das bedeutet:**

| Fraktion | Ressource | Gameplay-Zugang | Fantasie |
|---|---|---|---|
| **Die Krone** | Territorium, Militärpassagen, Rechtsstatus | Schutz, Bewegungsfreiheit, Ehrentitel | Legitimität erkaufen |
| **Die Gilden** | Materialien, Handwerksrezepturen, Schwarzmarkt | Crafting-Tiefe, Upgrade-Pfade, Händler-Netzwerke | Macht durch Handwerk |
| **Der Orden** | Wissen, Fertigkeitsbücher, Bildungsmonopol | Skill-Upgrades, Lore-Zugang, Heilkunde | Verständnis als Waffe |

Fraktionsruf ist keine abstrakte Zahl — er ist der Schlüssel zu konkreten Spielsystemen. Wer bei den Gilden gut steht, kommt an Damaszener-Stahl. Wer beim Orden arbeitet, versteht das Schattenfieber tiefer (oder glaubt es zu verstehen).

Kein moralischer Zeigefinger. Jede Fraktion hat einen sympathischen Einstiegspunkt, einen Moment der Kompliziertheit, und einen Point of No Return.

**Spieler-Fantasie:** *"Ich wähle nicht die gute Fraktion. Ich wähle meine Fraktion."*

**Referenz:** VtM: Bloodlines (Troika, 2004). Leo (Recherche Tag 1): "Alle drei Fraktionen müssen für jemanden attraktiv sein."

---

### Säule III — Körperlicher Fortschritt

**Statement:** Der Körper des Spielers ist der Charakter. Fortschritt ist sichtbar, spürbar, und hat Kosten.

**Was das bedeutet:**

Das Nervensystem-Leveling ersetzt klassische Attribut-Grids und Erfahrungspunkte-Balken. Drei Subsysteme:

| Subsystem | Trainiert durch | Mechanische Auswirkung |
|---|---|---|
| **Cardio** | Laufen, Ausdauerkämpfe, Flucht | Ausdauer, Bewegungsgeschwindigkeit, Regeneration |
| **Muskel** | Schwertkampf, Tragen, physische Arbeit | Schadenswerte, Tragegewicht, Rüstungseffizienz |
| **Lymph** | Alchemika einnehmen, Schattenfieber-Exposition, Heilrituale | Widerstandsfähigkeit gegen das Fieber, Zugang zu Mutationen, Risiko |

Jedes Subsystem hat vier Qualitätsstufen (nach dem Deus Ex-Modell: Untrained / Geübt / Fortgeschritten / Meister). Keine 1-100-Skalen. Qualitätswechsel, keine Zahlenoptimierung.

**Das Schattenfieber als dritte Progressionsachse:**
- Das Lymph-Subsystem koppelt direkt an die Schattenfieber-Progression (vier Stadien: Rauschen / Risse / Schwelle / Übergang — nach Emres Lore-Ausarbeitung)
- Wer das Fieber unterdrückt (Krone-Weg), bleibt "sauber", verliert aber Zugang zu bestimmten Fähigkeiten
- Wer das Fieber nutzt (Gilden-Weg: Destillierung als Produkt), gewinnt Kraft, bezahlt mit Körper
- Wer das Fieber versteht (Orden-Weg: Deutungshoheit), bekommt tieferen Lore-Zugang, aber der Orden will etwas dafür

Das ist kein "Magie-System mit anderem Namen". Die Kosten sind real. Ein Spieler mit fortgeschrittenem Fieber wird *gezeichnet*.

**Spieler-Fantasie:** *"Mein Körper ist mein Fortschrittsanzeiger. Ich sehe, was ich trainiert habe — und was es mich gekostet hat."*

**Referenz:** Spector (Deus Ex GDD, 1997): Skill-Granularität über vier Qualitätsstufen statt 1-100-Skala. Emre (Mythos v1, Tag 2): Schattenfieber-Stadien biologisch verankert.

---

### Säule IV — Dichte vor Breite

**Statement:** Handgefertigte Welt, handgefertigte Begegnungen. Lieber zwanzig NPCs mit Persönlichkeit als zweihundert mit Füll-Dialog.

**Was das bedeutet:**
- Die Schwellenstadt ist der Kern. Keine riesige Weltkarte mit leeren Gebieten dazwischen. Eine Stadt, vertikal geschichtet (Krone oben / Gilden-Mittelzone / Volksviertel / Slums und Kanäle), dicht belebt.
- Jede Zone hat eigene Materialsprache, eigene Architektur, eigenen NPC-Typ. Der Spieler liest Schicht und Status sofort ab — ohne HUD-Icon.
- NPCs haben Tagesabläufe. Wachen lösen ab. Märkte öffnen und schließen. Ein Schmied, der um 14:00 in der Hammergasse arbeitet, ist um 20:00 in der Kneipe.
- Seitenquests entstehen aus der Welt, nicht aus Ausrufezeichen über NPC-Köpfen.
- Kein Loot-Bloat. Materialien sind knapp. Ein Stück Damaszener-Stahl ist ein Ereignis.

**Der Gothic-Kontrast zu Skyrim:**
Skyrim hat 300 Orte, an denen man Drachen töten kann. Gothic 2 hat Khorinis — und Khorinis *lebt*. Jeder Bewohner hat einen Namen, eine Meinung, einen Tagesablauf. Diese Dichte erzeugt die Illusion, in einer echten Welt zu sein. Das ist RELICS' Versprechen.

**Spieler-Fantasie:** *"Diese Welt existierte, bevor ich ankam. Sie wird nach mir weiterexistieren."*

**Referenz:** Gothic 2 (Piranha Bytes, 2002). Spector (Deus Ex GDD, 1997): "No weird 'game spaces'." Leo (Recherche Tag 1): "Dichte statt Breite ist unser schärfstes Unterscheidungsmerkmal."

---

## 7. Tonalität

**Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.**

Das ist kein Grimdark um des Grimdark willen. Die Welt ist dunkel, weil die Verhältnisse dunkel sind. Die Krone hat leere Kassen und bröckelnde Legitimität. Die Gilden halten Monopole mit Gewalt. Der Orden hat Bildung als Kontrollmittel. Das ist keine Fantasy — das ist Struktur.

Das Schattenfieber ist das einzige Übernatürliche. Es wird ernst genommen, nie trivialisiert. (Tolkien-Prinzip: "One thing must not be made fun of — the magic itself." Emres Leitlinie, ich unterschreibe.)

**Visuelle Signatur der Tonalität:**
- Oberschicht: All-Black, All-White, Monochrom — ein einzelner Neon-Akzent (leuchtendes Indigo, Blutrot, Giftgrün)
- Unterschicht: Grau, Braun, schmutzig — und gelegentlich ein gestohlenes Stück Farbe
- Biolumineszenz in den Kanälen: schön und bedrohlich
- Kein Zahnrad. Keine Dampfmaschine. Keine Hexagone.

---

## 8. Zielgruppe (nach Leo Fischer, Tag 1)

RELICS spricht vier überlappende Spielertypen an:

1. **Immersion-First Players** — wollen sich in eine Welt verlaufen, nicht geführt werden (Kingdom Come: Deliverance, Disco Elysium, Outer Wilds)
2. **Faction Players** — "Ich wähle nicht die gute Fraktion" (VtM: Bloodlines, Fallout: New Vegas)
3. **Crafting/Progression Freaks** — wollen sichtbare Materialsprache, echte Upgrade-Tiefe, keine Loot-Inflation (Dark Souls, Stardew)
4. **Medieval Aesthetics Obsessed** — reale mittelalterliche Logik + Biotech als Geheimnis, kein Kitsch (Kingdom Come, Mount & Blade)

**Kritisches Risiko (Leo):** Die erste Stunde ist kein Tutorial. Sie ist ein Angebot. Wenn der Spieler in Minute fünfzehn nicht versteht, was dieser Ort *ist*, verlieren wir ihn. Die erste Stunde muss stehen, wenn wir in die Streamer-Alpha gehen.

---

## 9. Abgrenzung

| Was RELICS IST | Was RELICS NICHT IST |
|---|---|
| Handgefertigte, dichte Welt | Weitläufige, leere Open World |
| Körperlicher Fortschritt sichtbar | Abstraktes Level-up-System |
| Drei Fraktionen ohne Moralkeulen | Gut-gegen-Böse-Struktur |
| Schattenfieber als biologische Wahrheit | Magiesystem mit Fantasy-Label |
| Spieler als namenloser Fremder | Spieler als vordefinierten Charakter (kein Geralt, kein JC Denton) |
| Medieval Cyberpunk: Material als Macht | Steampunk, High Fantasy, Science-Fantasy |
| Immersive Sim: mehrere Lösungswege | Schienenspiel mit Illusion der Wahl |

---

## 10. Vier offene Fragen — Stand Tag 2, 10:00 Uhr

Diese Fragen wurden im Briefing (Tag 2, Szene 1) aufgeworfen. Antworten folgen bis 17:00.

| # | Frage | Status | Antwort |
|---|---|---|---|
| 1 | **Stadtfrage:** Eine Stadt oder mehrere? | Geklärt | EINE vertikale Stadt (Schwellenstadt, Emres Topos-Skizze) als Kernschauplatz dieser Iteration. Mitteleuropäisch, auf Felssporn, vier Schichten. |
| 2 | **Schattenfieber-Scope:** Wie tief geht die Integration? | Geklärt | Hauptquest-antreibend UND dritte Progressionsachse (Lymph-Subsystem). Vier biologische Stadien nach Emres Lore. Drei Fraktions-Antworten = drei Gameplay-Pfade. |
| 3 | **Tiervolk:** Spielbar oder NPC? | Geklärt | NPC — Händler und Informationsbroker. Nicht spielbar. Leicht alien in Ästhetik, nicht tribal. Eigene Händler-Netzwerke parallel zu den Gilden. |
| 4 | **Release-Modell:** Wie liefern wir? | Geklärt | Main Release → Streamer-Alpha (vorgelagert, erste Stunde muss stehen) → Beta (max. 6–12 Monate) → Full Release → große DLCs. Keine kleinen Add-ons. |

---

\clearpage

# GDD Kapitel 04 — Schlüsselfiguren & NPCs (v1)

**Datum:** Tag 2, Dienstag, Schreibstube 12e
**Quellen:** Briefing, Recherche-Notizen Tag 1, VtM 2nd Ed, Planescape Last Rites Vision Statement, Briefing-Outputs Emre + Darius + Team

---

> **Redaktionelle Vorbemerkung (Nami):**
>
> Ich schreibe Figuren nicht von innen nach außen. Ich schreibe ihre Stimme zuerst, dann ihre Funktion. Wenn eine Figur keine eigene Stimme hat, hat sie kein Recht auf Existenz im Spiel.
>
> Jeder NPC in diesem Dokument hat eine Zeile, die nur er oder sie sagen kann. Das ist mein Qualitätskriterium. Nicht: "hat eine interessante Backstory." Sondern: "sagt etwas, das mich aufhorchen lässt."

---

## Strukturprinzip

Jede Figur wird beschrieben nach:

1. **Wer sie ist** — in drei Sätzen, kein Infodump
2. **Was sie vom Fremden will** — explizit und versteckt
3. **Was sie nie zugeben würde** — die Risse in der Fassade
4. **Ihre Stimme** — ein Muster, eine Eigenheit, ein charakteristischer Satz
5. **Spielerrelevanz** — Quest-Anker, Reaktion auf Fraktionswahl, Schattenfieber-Verhältnis
6. **Dramatischer Wendepunkt** — der Moment, in dem die Figur kompliziert wird

---

## 4.1 Der Fremde — Spielercharakter

*Kein vollständiger NPC-Eintrag, da spielergesteuert. Aber die Leerstelle muss benannt werden.*

Der Fremde ist kein Held. Er ist eine **Frage in Menschengestalt.**

Er kommt von woanders — woher, das wählt der Spieler bei der Charaktererstellung, und es beeinflusst, wie die Welt auf ihn reagiert, aber nicht, was er "ist." Er hat einen Namen, den wir nie aussprechen. Er hat eine Vergangenheit, die wir in Dialogoptionen andeuten, aber nie erzählen. Er ist **Blank Slate mit Textur** — kein leeres Blatt, sondern ein Blatt, das schon beschrieben war und abgewischt wurde.

**Das epistemische Prinzip:** Der Fremde lernt die Welt durch Mißverständnisse. Ein Gildenmeister, der ihm die Hand schüttelt, hat gerade eine Verpflichtung eingefordert — der Fremde weiß das nicht, noch nicht. Ein Ordensbote, der "ehrenwert" sagt, meint "gebunden." Die Krone bittet nicht — sie erwartet. Der Spieler lernt das langsam. Zu langsam, manchmal.

**Schattenfieber-Status:** Stufe 1 (Rauschen) ab Minute fünfzehn des Spiels. Nach dem Fragment. Das Rauschen gehört zum Charakter — er soll es erst sehr viel später als Symptom erkennen, wenn überhaupt.

**Für Vera:** Keine definierte Silhouette. Keine Gesichtsfarbe, keine festgelegte Körperhaltung. Die Ausrüstung zu Beginn ist Unterschicht — Eisen, ungefärbtes Leinen, aufgearbeitetes Leder. Das wird sich verändern, aber das erste Bild muss das sein.

---

## 4.2 Der Sterbende — Intro-NPC

**Vorläufiger In-World-Name:** Hieronymus Vael
**Funktion:** Intro-Sequenz, Quest-Auslöser, erster Schattenfieber-Spiegel

### Wer er ist

Hieronymus Vael war Bote. Nicht Krone, nicht Orden, nicht Gilden — er war **freier Bote**, einer der wenigen, die zwischen allen Lagern liefen, weil alle Lager solche Leute brauchen. Er wusste zu viel von zu vielen. Und er hat etwas transportiert, das er nicht hätte transportieren sollen: die Relikt-Scherbe. Jetzt stirbt er daran. Stufe 3 des Schattenfiebers — die Schwelle — und er weiß, dass er nicht zurückkommt.

Er ist ca. fünfzig Jahre alt, sieht achtzig aus. Die Haut an seinen Händen ist dünn geworden wie Papier, darunter laufen Muster, die aussehen wie tinte-eingeschriebene Adern, aber dunkler. Er riecht nach Erde. Sein Atem geht in kurzen Stößen.

Er liegt am Stadtrand, im Gras zwischen zwei ausrangierten Karrengeleisen. Es ist früher Morgen. Nebel. Er hat sich hierhin geschleppt, weil er wusste: die Stadt war nicht sicher. Nicht mit dem, was er trägt.

### Was er vom Fremden will

Explizit: Dass der Fremde die Scherbe nimmt. Dass jemand anderes weiterlebt, wenn er nicht mehr kann.

Versteckt: Absolution. Hieronymus hat jemandem vertraut, dem er nicht hätte vertrauen dürfen. Das Stück Relikt war ein Auftrag — bezahlt, legal, professionell. Aber er hat die Fragen nicht gestellt, die er hätte stellen sollen. Er stirbt nicht nur an der Scherbe. Er stirbt an seiner eigenen Bequemlichkeit. Der Fremde ist nicht sein Retter. Er ist Hieronymus' letzter Zeuge.

### Was er nie zugeben würde

Dass er weiß, wer den Auftrag gegeben hat. Er weiß es. Er sagt es nicht, weil er Angst hat, dass dieses Wissen den Fremden umbringt, bevor er überhaupt angefangen hat. Vielleicht. Oder weil er sich schämt.

### Seine Stimme

Hieronymus spricht in kurzen Sätzen. Er hat keine Energie für lange Erklärungen. Aber er ist kein Rätsel-NPC — er versucht zu erklären, scheitert aber an Zeit und Atem. Die Lücken in seinem Sprechen sind keine Absicht, sondern Erschöpfung.

**Charakteristischer Satz:**

> "Nimm das. Geh nicht zurück, wo du herkamst — dort kennen sie deinen Weg. Versteh das nicht als Warnung. Versteh das als das Einzige, was ich dir noch geben kann."

Er sagt "Versteh das" zweimal. Das ist sein Muster — er hat sein Leben damit verbracht, sicherzugehen, dass Botschaften ankommen. Auch jetzt noch.

### Spielerrelevanz

- Die Fragment-Übergabe ist der **Clip-Moment** (Leo, 14:00 Sync). Sie muss in den ersten fünfzehn Minuten passieren.
- Kurz danach erscheinen die drei Fraktionsboten. Dass der Fremde die Scherbe hat, ist entweder schon bekannt — oder wird innerhalb von Minuten bekannt. Das ist die erste narrative Frage: Wie?
- Der Spieler kann Hieronymus nach seinem Tod durchsuchen. Er findet wenig: ein zerrissenes Pergament-Stück mit drei Siegeln (Krone, Orden, Gilden — alle drei, was unmöglich sein sollte). Das ist eine Spur, die erst viel später aufgelöst wird.
- **Unreliable Narrator-Moment:** In Stufe 2 (Risse) erinnert sich der Spieler an die Begegnung mit Hieronymus. Was er "erinnert," stimmt nicht exakt mit dem überein, was passiert ist. Kleiner Unterschied — Hieronymus hat etwas gesagt oder nicht gesagt. Der Spieler weiß nicht, welche Version wahr ist.

### Dramatischer Wendepunkt

Gibt es nicht — Hieronymus stirbt in den ersten zwanzig Minuten. Aber: Wenn der Spieler im späteren Spielverlauf herausfindet, wer den Auftrag gegeben hat, verändert das die Erinnerung an diesen ersten Moment. Hieronymus wird rückwirkend komplizierter. Das ist sein Wendepunkt — post-mortem.

---

## 4.3 Fraktionsvertreter — Schlüssel-NPCs

*Je ein Hauptkontakt pro Fraktion. Kein Gut/Böse. Jede Figur hat einen sympathischen Einstiegspunkt und einen Moment der Kompliziertheit.*

---

### 4.3.1 Krone — Marschall Adelhaid Brenn

**Funktion:** Erster Kontakt zur Krone, Militärbehörde, potenzielle Auftraggeberin in Act 1

#### Wer sie ist

Adelhaid Brenn ist fünfundvierzig. Sie hat dreiundzwanzig Jahre in der Kronarmee gedient, davon acht als Marschall der Stadtgarnison. Sie trägt Tiegelstahl-Rüstung, gebürstet, ohne Verzierung — nicht aus Bescheidenheit, sondern weil Verzierungen im Nahkampf Angriffspunkte sind. Sie ist die Person, die die Scherbe-Situation als erste offiziell zur Kenntnis nimmt: Sie kennt den Namen Hieronymus Vael, und sie wollte ihn vor drei Tagen befragen.

Sie ist kein Schurke. Sie ist jemand, der Ordnung aufrechterhalten hat, weil Ordnung das Einzige ist, das die Schwächsten schützt. Wenn die Krone fällt, fallen zuerst die Menschen in den untersten Stadtschichten. Das glaubt sie. Das hat sie gesehen.

#### Was sie vom Fremden will

Explizit: Die Scherbe. Wenn sie den Fremden nicht überzeugen kann, sie freiwillig abzugeben, dann zumindest seine Zusammenarbeit.

Versteckt: Einen Vorwand, um das Schattenfieber-Problem zu lösen, ohne dass ihre Vorgesetzten wissen, dass es ein Problem gibt. Die Garnison verliert Soldaten — Schattenfieber-Exposition in den Unterkanal-Bereichen der Stadt. Sie hat es bisher nicht gemeldet, weil ein offizieller Bericht eine Quarantäne bedeuten würde, und eine Quarantäne bedeutet, dass die Kaufleute der Gilden sich beschweren, und dann greift der Gildenrat ein, und dann hat sie plötzlich Gilden-Aufseher in ihrer Kaserne. Das will sie nicht.

#### Was sie nie zugeben würde

Dass die Krone — nicht nur lokale Garnison, sondern die Kronbehörde selbst — das Relikt seit Jahren kennt. Nicht das Fragment. Das Original. Und dass sie aus dieser Kenntnis nie eine Pflicht abgeleitet hat, die ihr unbequem gewesen wäre. Sie weiß nicht, was das Relikt *ist* — aber sie weiß, dass Akten darüber existieren, die sie nicht lesen durfte.

#### Ihre Stimme

Brenn spricht direkt und ohne Umwege. Sie sagt nie "vielleicht," sie sagt "es wäre denkbar." Sie sagt nie "ich weiß nicht," sie sagt "das ist noch nicht ermittelt." Bürokratische Sprache als Selbstschutz, nicht als Täuschung. Sie ist kein Lügner — sie ist jemand, dem Präzision wichtiger ist als Ehrlichkeit.

Sie fragt viele Gegenfragen. Nicht als Verhörtaktik, sondern weil sie keine Entscheidung trifft, die sie nicht vollständig versteht.

**Charakteristischer Satz:**

> "Ich bitte Sie nicht, mir zu vertrauen. Das wäre unvernünftig. Ich bitte Sie, die Konsequenzen der Alternative zu verstehen."

#### Spielerrelevanz

- Boten-Szene: Brenns Bote erscheint als einer der drei Boten nach Hieronymus' Tod. Er ist höflich, uniformiert, unauffällig — und hartnäckig.
- Fraktions-Aufnahme: Der Spieler kann sich Brenn und der Krone anschließen. Sie bietet Unterkunft in der Kaserne (Oberschicht-Niveau, Midlevel der Stadt), Zugang zu Kronpassagen, und Ausrüstung aus Kronbeständen.
- **Schattenfieber-Reaktion der Krone:** Unterdrückung. Der Orden-Linie: Quarantäne. Die Gilden-Linie: Nutzbar machen. Brenn vertritt die Krone: Das Schattenfieber ist ein militärisches Problem. Man löst es wie ein militärisches Problem. Schweigen, Eindämmen, Kontrollieren.
- **Moral-Komplikation:** Im mittleren Spielverlauf stellt der Spieler fest, dass Brenn einen Unterkanal-Bereich hat sperren lassen — mit Menschen drin. Schattenfieber-Exposition. Sie nennt es "kontrollierte Quarantäne." Es sind vierzig Menschen. Siebzehn sind gestorben.

#### Dramatischer Wendepunkt

Brenn erfährt, was das Relikt wirklich ist. Emres Lore-Dokument beschreibt das Relikt als Schwellen-Stabilisator. Wenn Brenn das versteht — und sie *versteht* es, das ist ihre Stärke — zieht sie sofort die politische Konsequenz: Wenn das Relikt die Schwelle stabilisiert, und die Schwelle ist das, was das Schattenfieber kontrolliert, dann ist das Relikt eine Waffe. Eine, die die Krone besitzen muss. Nicht aus Bosheit. Aus militärischer Logik. Das ist der Moment, in dem sie aufhört, eine Verbündete zu sein und anfängt, ein Hindernis zu werden — ohne dass sie sich verändert hat.

---

### 4.3.2 Orden — Bruder Ivo Scherer

**Funktion:** Erster Kontakt zum Orden, Deutungs-Instanz, Informationsbroker (mit Preis)

#### Wer er ist

Ivo Scherer ist zweiunddreißig. Er sieht jünger aus und weiß das — er nutzt es. Er ist kein hoher Ordensmann, er ist Mittelrang: ein Forschungsbruder mit Archivzugang und genug Bildung, um gefährlich zu sein, aber zu wenig hierarchischen Status, um unangreifbar zu sein. Das macht ihn interessant. Er ist klug genug, den Machtspielern im Orden zu helfen, ohne je selbst einer zu werden. Das nennt er Demut. Es ist Selbstschutz.

Er trägt schwarze Ordensgewänder mit einem einzelnen indigofarbenen Ordenssiegel. Die Hände sind tintenbeschmiert. Er lächelt oft — aber das Lächeln erreicht die Augen nur, wenn er etwas Interessantes hört.

#### Was er vom Fremden will

Explizit: Das Fragment zu untersuchen. Nicht zu besitzen — er ist clever genug, diese Formulierung zu wählen. Er will Zugang, nicht Kontrolle. Vorerst.

Versteckt: Wissen, das er monopolisieren kann. Der Orden hat ein Bildungsmonopol, aber das Bildungsmonopol funktioniert nur, solange der Orden weiß, was andere nicht wissen. Ein Schwellen-Artefakt, das auftaucht und kursiert? Das ist eine Wissenslücke. Lücken machen ihn nervös. Er will die Lücke füllen — und dann verwalten.

#### Was er nie zugeben würde

Dass er einen Ur-Text über das Relikt gesehen hat. Fragmentarisch, unvollständig — aber er hat ihn gesehen, vor drei Jahren, in den Archivuntergeschossen, und er hat ihn nicht gemeldet. Er hat ihn kopiert. Die Kopie liegt in seinem Quartier. Er weiß, dass der Orden das als Häresie behandeln würde, nicht weil der Text ketzerisch ist, sondern weil nicht-gemeldete Archivauffunde Amtsverluste bedeuten.

#### Seine Stimme

Scherer spricht in langen, präzisen Sätzen mit Zwischensätzen, die immer etwas sagen, das er direkt nicht sagen möchte. Er stellt Fragen, die Aussagen sind. Er wiederholt Formulierungen des Gesprächspartners, leicht verändert — "Sie sagten, er drückte Ihnen etwas in die Hand. *Drückte.* Das ist ein Wort mit Druck dahinter."

**Charakteristischer Satz:**

> "Was Sie da beschreiben, ist entweder sehr gefährlich oder sehr wichtig. In meiner Erfahrung ist es meistens beides. Ich frage mich, ob Sie den Unterschied erkennen, wann die eine Eigenschaft in die andere kippt."

#### Spielerrelevanz

- Boten-Szene: Scherers Kontaktmann — kein uniformierter Bote, ein zivil gekleideter junger Mann, der aussieht wie ein Kaufmannslehrling — spricht den Fremden unauffällig an. Er übergibt ein versiegeltes Briefchen mit einer Adresse.
- Fraktions-Aufnahme: Der Orden bietet Zugang zum Archiv (Fertigkeitsbücher, Upgrade-Pfade), Unterkunft in einem Ordenshaus (Oberschicht, aber asketisch), und Scherers persönliche Deutungsleistung.
- **Schattenfieber-Reaktion des Ordens:** Deutungshoheit. Der Orden sagt nicht, was das Schattenfieber *ist* — er sagt, was es *bedeutet*. Das ist eine Theologie-Aussage, keine Medizin-Aussage. Wer krank wird, hat etwas falsch gemacht. Wer überlebt, hat etwas Richtiges getan. Wer wirklich verstehen will, muss durch den Orden. Das ist die Kontrolle.
- **Informationsbroker-Mechanik:** Scherer ist der NPC, über den der Spieler am meisten über die Weltgeschichte erfährt. Aber jede Information hat einen Preis — nicht notwendigerweise Geld. Manchmal eine Gunst. Manchmal eine Handlung, die den Spieler in die Nähe einer Fraktionsentscheidung bringt, bevor er bereit ist.

#### Dramatischer Wendepunkt

Scherer zeigt dem Spieler (unter bestimmten Bedingungen) seinen Ur-Text-Fragmentfund. Das ist sein Angebot, sein letztes Vertrauens-Kapital. Aber: Der Spieler kann in diesem Moment sehen, dass die Kopie unvollständig ist — und dass die fehlenden Stellen genau das sind, was erklärt, wie man das Relikt *zerstört.* Scherer hat das nicht kopiert. Vielleicht aus Vergessen. Vielleicht nicht.

---

### 4.3.3 Gilden — Gildenmeisterin Vreni Kast

**Funktion:** Erster Kontakt zu den Gilden, Wirtschaftsmacht, Vermittlerin und Händlerin

#### Wer sie ist

Vreni Kast ist zweiundfünfzig. Sie ist Meisterin der Glasmacher-Gilde — optische Instrumente, Alchemie-Phiolen, Bergkristall-Linsen. Das ist nicht die größte Gilde, aber es ist eine der technologisch avanciertesten. Glasmacher sehen, was andere nicht sehen — buchstäblich und im übertragenen Sinn. Sie ist kurz, unscheinbar, trägt immer eine Lupe an einer Kette. Ihre Hände sind vernarbt von Jahrzehnten an Werkbänken.

Sie hat aus einer Handwerkerfamilie ohne Gildenstatus in den Gildenrat aufgestiegen. Das war nicht Glück. Das war dreißig Jahre kalkuliertes Handeln.

#### Was sie vom Fremden will

Explizit: Das Fragment analysieren. Sie formuliert es als Angebot — sie bietet Dienstleistungen und Information im Tausch für Zugang. Kein Besitz. Analyse.

Versteckt: Zu verstehen, was das Fragment von sich abstrahlt. Scherers Orden hat Deutungshoheit über das Nicht-Messbare. Die Gilden wollen das Messbare — und wenn etwas mit dem Fragment passiert, das messbar ist, will Kast das erste Messinstrument sein, das es misst. Sie denkt: Wer das Relikt versteht, kann das Schattenfieber kontrollieren. Und wer das Schattenfieber kontrolliert, kontrolliert den wichtigsten Rohstoff in der Stadt.

#### Was sie nie zugeben würde

Dass die Glasmacher-Gilde bereits seit zwei Generationen versucht, das Schattenfieber zu synthetisieren. Nicht heilen — synthetisieren. Als Rohstoff. Die Experimente haben keine Überlebenden hinterlassen. Die Überreste liegen im untersten Kellergeschoss des Gildenhauses. Sie nennt es intern "das Destillationsarchiv." Es riecht dort nach verbranntem Haar und etwas Süßlichem.

#### Ihre Stimme

Kast redet schnell, präzise, und lässt dem Gesprächspartner keine Zeit zum Innehalten. Sie gibt viele Informationen, bevor der andere eine Frage stellen kann — das ist keine Offenheit, das ist Überflutung. Wen sie mag, gibt sie Spitznamen. Wen sie nicht mag, nennt sie "Kollege."

Sie macht sich selten Sorgen. Wenn sie sich doch Sorgen macht, beginnt sie Sätze mit "Das ist interessant" — was das Gegenteil von dem ist, was sie meint.

**Charakteristischer Satz:**

> "Sie halten das gerade in der Hand und wissen nicht, was es ist. Das ist die unangenehmste Position, in der man sich befinden kann — wertvolles Unwissen. Ich kann das ändern. Nicht umsonst, natürlich. Aber ich glaube, wir werden uns einig."

#### Spielerrelevanz

- Boten-Szene: Kast schickt keinen Boten. Sie wartet. Sie weiß, dass der Fremde in die Unterstadt muss — und dort kontrollieren die Gilden die Märkte. Der erste Kontakt ist zufällig inszeniert, aber nicht zufällig.
- Fraktions-Aufnahme: Die Gilden bieten Zugang zu Materialien (bessere Ausrüstung, Alchemie-Rezepturen), ein Handelsnetz das Informationen liefert, und Geld. Direkter als Krone und Orden.
- **Schattenfieber-Reaktion der Gilden:** Verwertung. Das Schattenfieber ist kein Feind — es ist ein unkontrolliertes Potenzial. Die Gilden wollen es kontrollierbar machen. Synthetisieren. In Produkte überführen. Das ist nicht zynischer als was die Krone tut — aber es ist ehrlicher.
- **Handels-Mechanik:** Vreni Kast ist der NPC, über den Spieler Zugang zu Nicht-Standard-Ausrüstung bekommen. Aber viele ihrer besten Angebote sind mit Bedingungen verknüpft, die erst später relevant werden.

#### Dramatischer Wendepunkt

Der Spieler entdeckt das Destillationsarchiv. Das ist Kasts Point of No Return — nicht für die Spielfigur, sondern für den Spieler: Er muss entscheiden, ob das, was er über Kast weiß, ändert, was er bereit ist, mit ihr zu tun. Kast selbst verteidigt das Archiv nicht moralisch. Sie sagt: "Das waren Freiwillige. Das Schattenfieber hätte sie trotzdem getötet." Das kann wahr sein. Das ändert nichts daran, was das Archiv ist.

---

## 4.4 Tiervolk — Salva (keine Familiennamen-Kultur)

**Funktion:** Informationsbroker, Händler, Verbindung zur Unterstadt und zu Netzwerken außerhalb der Fraktionen

### Eine Vorbemerkung zum Tiervolk

Das Tiervolk ist kein Volk. "Tiervolk" ist ein abwertender Begriff der Stadtbevölkerung für eine lose Gemeinschaft von Händlern und Informationsmaklern, die teilweise Merkmale aufweisen, die die Stadtbevölkerung als "tierisch" bezeichnet: Schuppenhaut, längere Gliedmaßen, Pupillen in anderen Formen, Geruchswahrnehmung die über menschliche Norm geht. Das ist kein übernatürliches Merkmal. Es ist eine Anpassung — Generationen von Exposition an bestimmte Materialien und Umgebungen in bestimmten Regionen, deren Genaues nicht bekannt ist.

Sie nennen sich intern "die Reisenden." Das Wort Tiervolk benutzen sie für sich selbst nicht. Wer es ihnen gegenüber benutzt, bekommt höflich einen doppelten Preis.

Das Briefing sagt: Tiervolk weniger tribal, leicht alien vs. menschlich clean. Händler und Diebe, NICHT Handwerker. Das passt: Die Reisenden verkaufen, was andere nicht verkaufen, wissen, was andere nicht wissen, und bewegen sich in Räumen, die für die drei Fraktionen unsichtbar sind.

### Wer Salva ist

Salva ist zwischen dreißig und fünfzig — das ist schwer zu sagen, und er gibt keine Auskunft darüber. Er ist Informationsbroker und Kontaktvermittler. Er hat keine Gilde-Mitgliedschaft, keine Kronen-Akkreditierung, keinen Ordensstatus. Er hat ein Netz aus Kontakten, das alle drei Fraktionen umspannt — ohne dass irgendjemand von den anderen weiß, dass er auch für sie arbeitet.

Er hat schuppige Haut um die Schläfen und Handgelenke, einen länglichen Hals, Pupillen die sich im Dunkeln weiten wie die eines Katers. Er trägt immer etwas Gestohlenes aus der Oberschicht — eine Faser Brokatseide als Tuchstreifen, eine einzelne Lapislazuli-Applikation an seiner Jacke. Das ist keine Zurschaustellung. Das ist Kompass: wo der Wert ist, war Salva zuerst.

### Was er vom Fremden will

Explizit: Einen Kunden, der zahlt. Der Fremde ist neu, schuldet niemandem etwas, kennt keine lokalen Regeln. Das ist eine ideale Ausgangslage für jemanden, der Informationen verkauft: der Käufer weiß nicht, was der Preis der Wahrheit ist.

Versteckt: Schutz. Salva ist in einer gefährlichen Position. Alle drei Fraktionen dulden die Reisenden, weil sie nützlich sind — aber "dulden" ist kein Status, der anhält. Wenn eine Fraktion einen Grund findet, die Reisenden zu vertreiben oder zu kontrollieren, gibt es kein Schutzrecht. Der Fremde, der keine Fraktion hat, ist vorübergehend unberührbar. Das ist nützlich.

### Was er nie zugeben würde

Dass er das Fragment schon einmal gesehen hat. Nicht dieses spezifische Fragment — aber etwas Ähnliches, vor Jahren, in einer Handelsroute weit südlich der Stadt. Es kam mit einer Karawane, und die Karawane kam nicht an. Er war das einzige Überlebende. Er hat nie darüber gesprochen, weil er keine Erklärung hat, die nicht verrückt klingt.

### Seine Stimme

Salva redet in Konjunktiven. "Man könnte sagen." "Es wäre denkbar, dass." Er macht nie direkte Behauptungen über heikle Themen — nicht weil er lügt, sondern weil direkte Behauptungen ihn angreifbar machen. Wenn er etwas als Fakt bezeichnet, ist es ein Fakt.

Er macht manchmal eine lange Pause mitten in einem Satz. Nicht für Dramatik — er hört gerade etwas, das andere nicht hören.

**Charakteristischer Satz:**

> "Was Sie in der Hand halten, hat drei verschiedene Preisschilder — je nachdem, wen Sie fragen. Ich rate Ihnen, nicht alle drei zu fragen. Nicht gleichzeitig."

### Spielerrelevanz

- Salva ist der NPC, der dem Fremden am frühesten erklärt, wie die Stadt *wirklich* funktioniert — nicht die offizielle Version.
- Er ist kein Quest-Geber. Er ist ein **Kontext-Lieferant**. Die Informationen, die er verkauft, verändern nicht den Verlauf von Quests, aber sie verändern, wie der Spieler die Quests versteht.
- Er reagiert auf Fraktionswahl: Wenn der Spieler einer Fraktion beitritt, wird Salva vorsichtiger. Nicht feindlich — vorsichtiger. Er hat jetzt weniger Spielraum.
- **Schattenfieber-Status:** Salva hat Exposition — nicht Krankheit, aber Nähe. Die Reisenden, die in bestimmten Unterstadt-Bereichen handeln, kommen regelmäßig in Kontakt mit Schwellen-Bereichen. Er weiß es. Er nimmt Vorsichtsmaßnahmen, die er nicht erklärt.
- Er ist der einzige NPC, der den Fremden beim ersten Treffen beim korrekten Namen nennt — obwohl der Fremde ihn ihm nicht gesagt hat. Das ist ein Rätsel, das das Spiel nicht auflöst.

### Dramatischer Wendepunkt

Salva verschwindet für eine längere Spielperiode. Wenn er zurückkommt, sieht er verändert aus — nicht dramatisch, aber die Schuppenhaut hat sich ausgebreitet, sein Geruch ist anders. Er spricht nicht darüber. Wenn der Spieler fragt, sagt er: "Das ist irrelevant. Was ich gefunden habe, ist das Gegenteil."

Was er gefunden hat: den Ursprungsort des Fragments. Er gibt diese Information gegen einen sehr hohen Preis weiter.

---

## 4.5 WBB-Ergänzungsnotizen: Fraktionskosmologien
*(Vorbereitung für WBB Kap. 3 — Ethos / Emre-Kollaboration)*

*Diese Notizen gehören offiziell in die WBB. Ich schreibe sie hier, weil sie untrennbar mit den NPC-Stimmen verbunden sind — ich kann Scherer nicht schreiben, ohne zu wissen, was der Orden glaubt. Emre soll diese Notizen als Input für sein Ethos-Kapitel verwenden.*

### Die drei Schöpfungserzählungen — Unreliable Narrators auf Weltebene

Der Orden hat einen **kanonischen Text**: die Ordensgenesis. Eine göttliche Ordnung hat die Welt erschaffen und die Schwelle als Schutzwall gesetzt. Das Schattenfieber ist der Beweis, dass der Schutzwall durchbrochen wurde — durch menschliche Überheblichkeit, durch das Streben nach Wissen, das nicht für Menschen bestimmt war. Der Orden ist der Hüter dieses Wissens. Wer durch den Orden lernt, ist sicher. Wer außerhalb des Ordens sucht, öffnet die Risse weiter.

**Was der Orden verschweigt:** Der Ur-Text, aus dem die Ordensgenesis abgeleitet ist, beschreibt die Schwelle nicht als Schutzwall. Er beschreibt sie als Membran — etwas, das in beide Richtungen durchlässig ist, von Natur aus. Das Schattenfieber ist nicht Strafe. Es ist Kontakt. Der Orden hat diese Lesart unterdrückt, weil sie die Deutungshoheit aufhebt.

Die Krone hat **keine systematische Kosmologie** — das ist ihr ehrlichstes Merkmal. Die Kronmythologie ist eine Sammlung von Herrscherlegenden: Das erste Königreich hat die Stadt auf dem Fels gegründet, weil der Fels stark ist und stark Bleibendes anzieht. Das Schattenfieber ist ein Feind wie andere Feinde — man bekämpft es, man kontrolliert es, man berichtet es nicht weiter, wenn der Bericht mehr Schaden anrichtet als das Schweigen.

**Was die Krone nicht weiß:** Es gibt im Kronarchiv Berichte über das Relikt, die älter sind als die Stadt selbst. Das Kronarchiv weiß es. Die Menschen, die das Archiv verwalten, wissen, dass sie die Berichte nicht lesen dürfen. Sie wissen nicht, warum.

Die Gilden haben eine **Gründungschronik**: Wissen ist Arbeit. Material ist Wissen. Wer das Material beherrscht, hat die Welt beherrscht, und wer die Welt beherrscht, braucht keine Kosmologie. Das Schattenfieber ist ein Material-Problem mit einer Material-Lösung. Irgendjemand hat das Gleichgewicht gestört; irgendein Material aus jenseits der Schwelle ist durchgekommen; man findet es, man synthetisiert es, man kontrolliert es.

**Was die Gilden nicht sagen:** Die Destillationsversuche der Glasmacher (Vreni Kasts Archiv) haben etwas Reproduzierbares ergeben. Ein Extrakt. Er stabilisiert Schattenfieber-Opfer in Stufe 1 — kurz. Danach beschleunigt er die Progression dramatisch. Die Gilden haben diese Information als nicht-brauchbar klassifiziert. Nicht als gefährlich. Als nicht-brauchbar.

### Das Tiervolk — eine vierte Kosmologie, die niemand ernst nimmt

Salva hat mir etwas erzählt — ich weiß nicht, ob es stimmt, er hat es im Konjunktiv gesagt — das ich hier notieren will: Die Reisenden glauben, dass das Schattenfieber kein Durchsickern ist. Es ist eine **Kommunikation**. Etwas jenseits der Schwelle kommuniziert. Das, was wir Schattenfieber nennen, sind die Empfänger dieser Kommunikation — Körper, die versuchen, in einer Sprache zu antworten, die sie nicht sprechen können.

Kein NPC im Spiel bestätigt das. Kein Text widerlegt es.

---

## 4.6 Quest-Skizzen
*(Erste Entwürfe — gelbe Post-Its)*

### Intro-Quest: "Was er in der Hand hielt"

**Trigger:** Spieler betritt die Spielwelt. Früher Morgen, Stadtrand, Nebel.
**Einstieg:** Hieronymus Vael stirbt. Fragment-Übergabe. Drei Boten erscheinen innerhalb von Minuten.
**Erste Entscheidung:** Zu welchem Boten geht der Spieler zuerst?

Dies ist keine Moral-Entscheidung. Der Spieler kennt die Fraktionen noch nicht. Er geht zu dem Boten, dessen Angebot sich zuerst richtig anfühlt. Die Welt merkt es sich.

**Struktur:**
- Beat 1 — Hieronymus. Die Übergabe. Das Rauschen beginnt (Schattenfieber Stufe 1, kaum wahrnehmbar).
- Beat 2 — Die drei Boten. Kurze Kontakte. Keine Entscheidung nötig — alle drei geben Adressen. Aber wer der erste Besuch ist, prägt die Eröffnungssequenz.
- Beat 3 — Erste Adresse. Der Spieler betritt die Stadt zum ersten Mal richtig. Er bemerkt die Schichtung. Er hat keine Ahnung, wo er steht.

**Clip-Moment (Finn/Leo-Anforderung):** Die Fragment-Übergabe. Hieronymus' letzter Satz. Das erste Rauschen — eine Sekunde lang sind die Schatten nicht dort, wo sie sein sollten.

---

### Hauptquest-Strang: "Der Spieler verfolgt das Relikt, weil er sich selbst verfolgt"

*(Arbeitstitel — Darius hat das genehmigt, solange es ein griffiges Label für das Kapitel gibt. Ich nenne es vorerst: Der Schwellenanker)*

Die zentrale Frage des Hauptquests: **War ich immer hier, oder hat das Relikt mich gerufen?**

Diese Frage wird nie direkt beantwortet. Das ist keine Schwäche der Story, das ist die Story.

**Act 1 — Das Fragment:** Der Spieler hat ein Stück von etwas, das viele wollen und keiner versteht. Die drei Fraktionen wollen es aus unterschiedlichen Gründen. Salva will es für Geld. Der Spieler beginnt, die Stadt zu verstehen.

**Act 2 — Das Muster:** Das Fragment ist nicht einzigartig. Es gibt andere. Hinweise darauf, dass das Relikt in Stücke zerbrochen wurde — wann, durch wen, warum. Die Fraktionen haben unterschiedliche Stücke. Oder wissen, wo die anderen sind. Der Spieler navigiert ein Netz aus Halbwahrheiten.

**Act 3 — Die Schwelle:** Der Spieler erreicht den Ursprungsort. Was er dort findet, hängt von seinen Entscheidungen ab. Emres Relikt-Konzept — der Schwellenanker — wird hier konkret. Das Relikt stabilisiert die Schwelle. Wenn es zerstört wird, öffnet sich die Schwelle weiter. Wenn es erhalten wird, bleibt das Schattenfieber kontrollierbar — aber nichts ändert sich an den Bedingungen, unter denen die Stadt die Schwächsten behandelt.

**Endkonsequenzen (drei Hauptäste, keine eindeutige "richtige" Entscheidung):**
1. Das Relikt der Krone übergeben. Die Schwelle bleibt stabil. Die Krone kontrolliert das Schattenfieber militärisch. Die Stadt überlebt. Die untersten Schichten bleiben, wo sie sind.
2. Das Relikt dem Orden übergeben. Die Schwelle wird durch Ordenswissen verwaltet. Das Schattenfieber wird zur Theologie. Wer nicht unter Ordensdeutungshoheit lebt, ist ungeschützt.
3. Das Relikt niemanden geben. Die Schwelle öffnet sich weiter. Das Schattenfieber eskaliert. Aber etwas kommt durch — und was durchkommt, ist nicht nur Krankheit.

**Was Darius wissen muss (für Sync 14:00):** Ich brauche eine Entscheidung über das Relikt-Design, bevor ich Act 3 ausarbeiten kann. Darius' "Das Herz"-Vorschlag ist narrativ stark — ich kann damit arbeiten. Emres "Die Wurzel"-Vorschlag ist kosmologisch stärker. Ich würde die Synthese vorschlagen: Das Herz ist das Fragment, die Wurzel ist das Ganze. Der Spieler hat ein Herzkammer-Stück. Das Ganze liegt irgendwo in der Tiefe der Stadt.

---

## Noch offen (pink Post-Its)

- **Fragment-Szene (Finn/Leo-Anforderung):** Habe sie skizziert. Schreibe heute nachmittag die ausformulierte halbe Seite, die Finn für morgen braucht.
- **Relikt-Entscheid:** Warte auf Darius' Bestätigung beim 14:00 Sync. "Das Herz" als Fragment, "Die Wurzel" als Ganzes — kann ich erst finalisieren, wenn Emre und Darius einig sind.
- **Stadtname / Schauplatz:** Brauche Emres Ortsnamen für die Dialoge. Hieronymus Vael kann den Ort nicht benennen, wenn ich keinen habe.
- **Tiervolk-Eigenname:** "Salva" ist ein Platzhalter. Emre soll Namenssystem-Input geben.
- **Nebenquest-Ausarbeitung:** "Der Zeuge" (alter Mann in den Slums) und zwei weitere Ideen folgen in v2.

---

*grünes Post-It: Figuren-Grundgerüst steht. Jede Stimme ist testbar.*
*gelbes Post-It: Quest-Struktur ist Skizze. Act 3 wartet auf Relikt-Entscheid.*
*pink Post-It: Fragment-Szene, Stadtname, Tiervolk-Name — externe Inputs nötig.*

\clearpage

# GDD Kapitel 6: Technische Spezifikation & Produktion

**RELICS: [Relikt-Name steht aus]**

---

> **Anmerkung zur Dokumentstruktur**
> Dieses Kapitel ist die technische Antwort auf das kreative Briefing. Jede Entscheidung hier hat einen Grund — und den schreibe ich dazu. Wenn eine Entscheidung keine Begründung hat, gehört sie nicht ins Dokument. Das ist mein Standard.

---

## 6.1 Engine & Technologiebasis

### 6.1.1 Unreal Engine 5 — Begründung

RELICS wird in **Unreal Engine 5** entwickelt. Diese Entscheidung ist gesetzt und nicht diskussionswürdig. Die Begründung:

Das Kernszenario — eine vertikal geschichtete Stadt mit extremer Geometriedichte, biolumineszenten Materialien, dynamischer Globalbeleuchtung und einem Post-Process-System, das die Spielwahrnehmung schrittweise deformiert — erfordert eine Kombination aus Nanite, Lumen und World Partition. Kein anderes aktuell verfügbares System bietet alle drei in Integration. Custom-Engine-Arbeit wäre für ein Studio dieser Größe prohibitiv.

**Engine-Version**: UE5.4 LTS (Long-Term Support Release). Kein Upgrade während der Alpha-Phase. Feature-Patches werden erst nach Beta evaluiert.

**Ziel-Plattform (primär)**: Windows PC (DirectX 12)
**Ziel-Plattform (sekundär)**: PlayStation 5, Xbox Series X (nach Full-Release evaluiert)

**Hardware-Mindestanforderungen (PC, Zielzustand):**
| Stufe | GPU | RAM | Einstellung |
|---|---|---|---|
| Minimum | NVIDIA RTX 2070 / AMD RX 6700 XT | 16 GB | Lumen Software RT, mittlere Qualität |
| Empfohlen | NVIDIA RTX 3080 / AMD RX 7900 XT | 32 GB | Lumen Hardware RT, hohe Qualität |
| Ultra | NVIDIA RTX 4080 / AMD RX 7900 XTX | 32 GB | Full Hardware RT, maximale Qualität |

*Anmerkung*: Die Minimum-Konfiguration nutzt Lumen in Software-RT-Modus. Das degeneriert GI-Qualität in den Slum-Unterebenen merklich. Akzeptabel — die Unterebenen sind dunkel per Design.

---

### 6.1.2 Kernkomponenten der Engine

**Nanite** — Virtualisierte Geometrie
Nanite ist für die gesamte statische Architekturgeometrie aktiviert. Die Materiallesbarkeit der Welt — Zunftzeichen-Reliefs, Titan-Legierung-Oberflächendetail, Knochen-Schnitzereien der Unterschicht — funktioniert nur mit Nanite-Detailauflösung. Ohne LOD-Authoring pro Mesh spart das konservativ geschätzt 40–60% des Modellierungs-Aufwands gegenüber traditioneller Pipeline.

*Bekannte Schwächen und Kompensation:*
- **Dünne Geometrien** (Ketten, Gitterstäbe, Pflanzenstifte, Stoff-Überhänge): Nanite crasht bei Meshes unter ~2px projected-size. Diese Kategorie behält traditionelle LODs und Imposter-Billboards ab Distanzklasse 3.
- **Wasser, Transluzenz**: Nanite unterstützt keine transluzenten Materialien. Alle Wasseroberflächen und Glas-Elemente sind non-Nanite mit eigenem LOD-Setup.
- **Moving Meshes**: Nanite funktioniert für statische und leicht animierte Meshes. Kampf-Props, die zerstört werden können, müssen als Nanite-Fallback-Mesh mit Destruction-Proxy gebaut werden.

---

**Lumen** — Dynamische Globalbeleuchtung und Reflexionen

Lumen ist das wichtigste und gleichzeitig riskanteste System im Projekt. Die Begründung ist direkt: eine lebendige, biolumineszente Stadt mit phosphoreszierenden Mineralien, Alchemie-Lampen und Schattenfieber-Mutationen braucht echte dynamische GI. Statisches Baked Lighting würde jeden Runtime-Zustandswechsel — das Aktivieren eines Relikts, eine Schattenfieber-Eskalation, die Biolumineszenz-Klasse-A-Emitter — optisch inkonsistent machen.

*Lumen-Konfiguration nach Stadtschicht:*

| Schicht | Modus | Begründung |
|---|---|---|
| **Layer 3** (Türme, Gilden-Hochbau) | Hardware Raytracing | Offener Himmel, viele Bergkristall-Linsen-Reflektionen — hier ist Hardware-RT-Qualität sichtbar und rechtfertigbar |
| **Layer 2** (Brücken, Arkaden) | Hardware Raytracing | Starke Buntglas-Farbflecken auf Böden, Reflexionen in Metall-Intarsien — RT sichtbar |
| **Layer 1** (Straßenebene) | Software Raytracing (hohe Qualität) | Kompromiss: genug GI-Bouncing für Kerzenlicht-Atmosphäre, Budget-schonend |
| **Layer 0** (Untergrund, Kanäle) | Software Raytracing + Hybrid Baked | Lumen degeneriert stark ohne Himmelssicht. Baked Irradiance für statische Bereiche, Lumen-Emitter für dynamische Lichtquellen |

*Lumen-Tuning-Parameter (global):*
- `r.Lumen.ScreenProbeGather.ScreenSpaceBentNormal 1` — Verbessert GI in Ecken und Nischen, kritisch für Gewölbe-Architektur
- `r.Lumen.Reflections.MaxRoughnessToTrace 0.4` — Beschränkt RT-Reflexionen auf glänzende Materialien (Titan, Glas, Edelstahl)
- `r.Lumen.DiffuseIndirect.Allow 1`
- Lumen-Importance-Volumes: Manuell platziert in allen Gildenhallen, Ordenskorridoren, Ratsräumen — höhere Probe-Dichte wo Materialqualität inszeniert wird

*Lumen-Emitter-Klassifizierung* (→ detailliert in 6.3.2):
- Klasse A: echte GI-Emitter (wenige, hero lights)
- Klasse B: visuell emissiv, kein GI-Beitrag
- Klasse C: Niagara-Partikel-Glow

---

**World Partition** — Streaming und vertikale Architektur

World Partition ist Pflicht für eine offene Welt dieser Größe. Das primäre technische Problem: UE5 World Partition ist horizontal konzipiert — es streamt Grid-Zellen auf einer XY-Ebene. Die vertikale Stadtstruktur von RELICS (vier markante Schichten auf der Z-Achse) ist kein Standardfall.

*Lösung: Manuelle Data Layers als vertikale Strukturierung*

Statt die Vertikale dem automatischen Streaming zu überlassen, strukturieren wir vier manuelle Data Layers:

| Layer | Inhalt | Lichtstimmung | Schattenfieber-Ambience |
|---|---|---|---|
| **Layer 0** | Untergrund, KanalSystem, Slum-Keller | Phosphoreszierendes Blau-Grün, vereinzelt Feuerschein | Hoch — subtile PP-Basis-Ambience aktiv |
| **Layer 1** | Straßenebene, Handwerkerviertel, Marktplätze | Warmes Kerzenlicht, Buntglas-Farbflecken aus Obergeschossen | Mittel |
| **Layer 2** | Brücken, Arkaden, niederer Gilden-Bereich | Diffuses Tageslicht durch Bergkristall-Linsen-Streuung | Niedrig |
| **Layer 3** | Türme, Gildenhochbau, Ordensanlagen, Kronenpalast | Klares Tageslicht, Bergkristall-Linsen direkt, Metallic-Reflektionen | Minimal |

*Technische Implementierung:*
- Jeder Data Layer ist eine eigenständige Streaming-Einheit mit eigenem Post-Process-Volume-Stack
- Manuelle Occlusion-Volumes an allen Schicht-Übergängen — Layer 3 cullt aggressiv Layer 0 und 1 wenn Sichtlinien getrennt
- Ebenen-Übergänge (Treppen, Lifte, Schächte) sind als "Transition Zones" definiert — beide angrenzenden Layer gleichzeitig geladen für 60m Radius um den Übergang
- **Offene Frage an Vera**: Wie diskret sind die Schichtgrenzen im Level-Design? Fließende Übergänge erhöhen die Transition-Zone-Radius-Kosten signifikant. Diskrete Ebenen = robustere Streaming-Pipeline. Das muss vor World-Partition-Setup entschieden sein.

---

## 6.2 Kamerasystem

### 6.2.1 Third/First Person — nahtloser Übergang

Das Briefing nennt explizit Skyrim als Referenz. Der Übergang muss nahtlos sein — kein Ladebildschirm, kein sichtbarer Kamera-Swap.

**Implementierungsansatz:**
Eine einzige Camera-Component, zwei definierte Offset-Zustände, interpoliert:

- **Third-Person-Position**: 200 cm hinter dem Charakter, 80 cm über der Schulter (leichter Schulter-Offset für bessere Sichtbarkeit der Figur in Kämpfen)
- **First-Person-Position**: Exakte Head-Socket-Koordinate, keine Körper-Sichtbarkeit

**Blend-Mechanismus:**
- Blend-Dauer: 0.3 Sekunden
- Kurventyp: Ease-In/Out (keine lineare Interpolation — die fühlt sich mechanisch an)
- Ausgelöst per Tastendruck oder Context-Trigger (enge Gänge lösen optionalen Auto-Wechsel aus)

**FOV-Konfiguration:**
| Modus | Standard-FOV | Spieler-Range |
|---|---|---|
| Third Person | 90° | 75° – 100° |
| First Person | 95° | 80° – 110° |
| Vertikaler Raum (z.B. Turm-Inneres) | +5° automatisch | — |

*Begründung FOV-Spread*: Die vertikale Stadt erfordert mehr vertikalen Sichtraum als ein Standardspiel. 90° Third Person ist Standard; der automatische +5° in hohen Räumen ist eine qualitative Verbesserung ohne Übelkeit-Risiko.

---

### 6.2.2 Cinematik-Modus (Sequencer)

Für Cutscenes, Dialoge und Relikt-Aktivierungs-Sequenzen nutzen wir **UE5 Sequencer** mit eigenem Kamerasystem.

- Cinematic-Kameras sind separate Kamera-Akteure — sie übernehmen temporär die Kontrolle, blenden zurück auf Spieler-Camera
- DOF: echtes Bokeh-DOF im Cinematic-Modus (Performance-Kosten akzeptiert für Kino-Qualität)
- **Tarkowski-Referenz** (Nami): Statische Langzeiteinstellungen, langsame Zooms, keine handheld-Simulation. Die Kamera ruht — die Welt bewegt sich in ihr. Das soll das Kamera-Führungsprinzip für alle Haupt-Cutscenes sein.

---

## 6.3 Rendering-Pipeline: Materialien & Biolumineszenz

### 6.3.1 Material-Philosophie

Jedes Material in RELICS muss auf drei Ebenen funktionieren:
1. **Materiallesbarkeit** — der Spieler erkennt sofort den sozialen Status des Trägers/Besitzers (Dark Souls Design Works-Prinzip: Abnutzung und Kontext erzählen Geschichte)
2. **Physikalische Plausibilität** — kein Material sieht "falsch" aus. PBR-Werte innerhalb physikalischer Grenzen.
3. **Performance-Budget** — jedes Material hat ein definiertes Instruction-Count-Limit

**Material-Hierarchie nach sozialer Schicht** (technische Entsprechung des Briefings):

| Schicht | Materialklasse | Roughness-Range | Metallic | Besonderheit |
|---|---|---|---|---|
| Oberschicht | High-Fidelity PBR | 0.05 – 0.25 | Ja (Titan, Edelstahl, Gold) | Clearcoat-Layer für Bergkristall-Linsen, Emissive optional |
| Mittelschicht | Standard PBR | 0.3 – 0.6 | Partiell (Bronze, Silber) | Malachit-Einlagen via Masked-Layer |
| Unterschicht | Dirty/Layered PBR | 0.6 – 0.95 | Selten | Wear-Maps, Schmutz-Parameter, gestohlene Akzente |

*Globalregel*: Material-Kontrast-Hierarchie nach FFXIV-v2.0-Vorbild. Emissive-Elemente sitzen auf dunklen Basismaterialien — Lesbarkeit vor Sättigung.

---

### 6.3.2 Biolumineszenz — Dreiklassen-System

Biolumineszenz ist das Neon-Äquivalent dieser Welt. Phosphoreszierende Mineralien, Alchemie-Leuchtstoffe, organisches Glühen. Das technische Problem: viele Emitter = Performance-Kollaps. Lösung: striktes Klassifizierungssystem.

**Klasse A — Hero Lights (echte Lumen-GI-Emitter):**
- Mesh-Flag: `Cast Lumen Light = true`
- Zweck: Setzt die narrative Lichtstimmung einer Szene
- Budget: max. 8–12 Klasse-A-Emitter gleichzeitig im sichtbaren Bereich
- Beispiele: Bergkristall-Linsen der Gildenmeister, große Alchemie-Lampen in Ordenskorridoren, das aktivierte Relikt (Zustand 2)
- Emissive-Intensität: 50–200 cd/m² (physikalisch plausibel für echte Glaslampen-Äquivalente)

**Klasse B — Ambient Glow (visuell emissiv, kein GI-Beitrag):**
- Mesh-Flag: `Cast Lumen Light = false`
- Zweck: Atmosphärische Dichte ohne Performance-Kosten
- Budget: unbegrenzt — kein GI-Overhead
- Beispiele: phosphoreszierende Schimmel-Patches in Untergeschossen, Alchemie-Phiolen im Regal, Kleinst-Buntglas-Elemente
- Emissive-Intensität: 2–15 cd/m² — leuchten visuell, strahlen aber nicht in die Szene

**Klasse C — Particle Glow (Niagara, organisch):**
- Niagara-System mit Billboard-Sprites und Custom-Depth-Masking
- Zweck: organische Biolumineszenz-Cluster (Pilze, Schimmel-Kolonie, Schattenfieber-Wucherungen)
- Skalierbar über GPU-Simulationsstufen (Low/Medium/High)
- Lodded ab 20m Distanz — Particle Count halbiert sich pro Distanzklasse
- Beispiele: Slum-Pilz-Cluster, Kanal-Algen-Glühen, Schattenfieber-Pusteln an Infizierten

*Dokumentationspflicht*: Jeder platzierte Klasse-A-Emitter wird in einer Scene-Light-Bible dokumentiert. Keine undokumentierten Hero Lights in final gebauten Szenen.

---

## 6.4 Schattenfieber — Post-Processing-System

### 6.4.1 Systemarchitektur

Das Schattenfieber-PP-System ist das komplexeste Single-Feature im Projekt. Es muss drei klar definierte Stufen mit smoothem Übergang abbilden und darf kein hartcodiertes System sein — alle Parameter müssen Blueprint-seitig steuerbar bleiben, damit Darius und Nami Inhalte ohne Tobi-Beteiligung implementieren können.

**Blueprint-Architektur:**

```
BP_SchattenfiebertSystem
├── Timeline-Komponente (Float-Kurve, 0.0 – 3.0 = Stufe-Werte)
├── PostProcessComponent (Stack)
│   ├── PP_Stage_0 (Base — immer aktiv)
│   ├── PP_Stage_1 (Blend-Weight 0→1 bei 0.0–1.0)
│   ├── PP_Stage_2 (Blend-Weight 0→1 bei 1.0–2.0)
│   └── PP_Stage_3 (Blend-Weight 0→1 bei 2.0–3.0)
├── ScalarParameter: "ShadowFever_Intensity" (0.0 – 3.0)
├── Event: OnStageThresholdReached (1.0 / 2.0 / 3.0)
└── Accessibility-Override: "DisableVertexAnimation" (Bool)
```

Der `ShadowFever_Intensity`-Wert wird vom Gameplay-Blueprint geschrieben (Darius' Lymph-Subsystem → Interface). Tobi's System liest den Wert und reagiert.

**Übergänge**: Immer geblended über die Timeline-Kurve. Kein Hard-Switch zwischen Stufen. Minimum-Blend-Zeit: 2 Sekunden pro Stufe.

---

### 6.4.2 Stufe 0 — Basis (kein Schattenfieber)

Normaler Spielzustand. Der PP_Stage_0-Stack ist trotzdem aktiv — er setzt die Color-Grading-Basis für RELICS.

- **Color Grading**: ACES-Tonemapping, leicht kühle Schattenbereich (Shadow Gain: RGB 0.95 / 0.95 / 1.02)
- **Film Grain**: 0.2 Intensität, 1.0 Körnung — minimal, nicht bewusst wahrnehmbar
- **Bloom**: Physikalisch kalibrierter Bloom-Mode, Schwellwert 1.2 — nur echte überbelichtete Stellen leuchten
- **Schärfe**: Temporal Anti-Aliasing (TAA), Schärfe-Boost 0.2

*Begründung*: Die leicht kühlen Schatten bauen schon im Normalzustand eine latente Kälte auf — der Spieler fühlt sie nicht bewusst, aber sie ist da. Technische Narratologie.

---

### 6.4.3 Stufe 1 — Frühinfiltration (sensorisch, subtil)

Der Spieler soll unsicher sein, ob er etwas sieht. Die Stufe ist so designt, dass erfahrene Spieler sie aktiv suchen müssen.

**Aktive Parameter:**
- **Chromatic Aberration**: Randbereich +0.4 Pixel max, zentral 0 — nur die Peripherie ist betroffen
- **Bloom-Tint**: Leicht Richtung Cyan verschoben (RGB-Multiplikator: 0.95 / 1.0 / 1.05)
- **Film Grain**: hochgesetzt auf 0.45, Körnung feiner (0.7) — das "Rauschen" aus Namis Stufe-1-Beschreibung
- **Schattenbereich-Kühlung**: Shadow Gain +0.05 auf Blaukanal — Schatten werden kälter
- **Vignette**: 0.15 Intensität — kaum bemerkbar, rahmt aber den Blick

**Was nicht aktiv ist**: kein DOF, keine Vertex-Animation, keine Geometrie-Eingriffe. Das kommt in Stufe 2.

*Spielerfahrung (Nami-Alignment)*: Geräusche klingen nach — das ist Sound-Design-Territorium, kein PP-System. Aber die Bild-Entsprechung ist die Chromatic Aberration: das Bild "klingt nach" im optischen Sinne. Eine winzige Farb-Verschiebung, die sich wie ein Echo anfühlt.

---

### 6.4.4 Stufe 2 — Mutative Phase (eindeutig, riskant)

Ab hier ist das Schattenfieber bewusst spürbar. Spieler wissen, dass sie infiziert sind. Die Wahrnehmung kompromittiert sich.

**Aktive Parameter:**
- **Chromatic Aberration**: 0.8 Pixel, leichte Oszillation (Sinuswelle, 0.5 Hz)
- **Vignette**: 0.35, pulsierend (0.25 Hz Sinuswelle, Amplitude 0.1)
- **Depth of Field**: Nahbereichs-DOF aktiviert, Focal Length 400cm, F-Stop 1.8 — Objekte näher als 4m werden scharf gestellt, Hintergrund unscharf. Simuliert veränderten Wahrnehmungs-Fokus.
- **Color Grading Curves**: Schattenbereich Indigo-Tint — Shadow-Midpoint-Offset: RGB -0.03 / -0.03 / +0.08
- **Vertex-Animation** (Umgebungsobjekte, separates System): ausgewählte organische Meshes im 15m-Radius um den Spieler oszillieren ±1.5 cm, 0.3–0.8 Hz (variiert pro Mesh). Das ist das "Atmen" der Welt.

**Accessibility-Option (Pflicht)**:
- Einstellungsmenü: "Schattenfieber-Bewegungseffekte reduzieren"
- Bei Aktivierung: Vertex-Animation deaktiviert, DOF-Pulsieren deaktiviert, Vignette-Pulsieren → statisch auf 0.3
- Die Stufe bleibt erkennbar, aber Motion-Sickness-Trigger werden eliminiert
- Dokumentation im Spielhandbuch: klarer Hinweis auf diese Option

---

### 6.4.5 Stufe 3 — Auflösung (Grenze zur anderen Seite)

Der kritische Zustand. Spieler befinden sich an der Schwelle zu den "planes of existence beyond known reality". Das ist das einzige Übernatürliche im Spiel — und es muss sich so anfühlen.

**Aktive Parameter:**
- **Full-Screen-Overlay**: `M_SchattenfiebertOverlay` — ein Custom-Depth-Masking-Shader mit organischen Rissstrukturen. Die Risse entstehen an Bildrändern und wandern langsam zur Bildmitte. Bewegungsgeschwindigkeit abhängig von `ShadowFever_Intensity`.
- **Geometrie-Lücken**: Ausgewählte Wand-Meshes zeigen temporäre schwarze Flächenbereiche — als würden Teile der Weltgeometrie nicht mehr existieren. Technisch: ein separater Render-Pass mit Masked-Visibility über Custom Stencil Buffer.
- **Indigo-Bloom**: Emissive-Quellen bekommen starken Indigo-Halo — Bloom-Radius 8.0, Tint stark Richtung Indigo/Violett
- **Chromatic Aberration**: 1.5 Pixel, chaotisch (Rauschwert statt Sinuswelle)
- **Nervensystem-Visualisierung**: startet automatisch (→ 6.5)

**Was diese Stufe mit dem Relikt-Shader verbindet**: Der kritische Relikt-Zustand (→ 6.6) nutzt dasselbe visuelle Vokabular wie Stufe 3 — Rissstrukturen, Innen-Leuchten, Indigo-Tönung. Das ist keine Koinzidenz. Das Relikt und die Krankheit sprechen dieselbe Sprache. Intentionale Ambiguität.

*Accessibility-Option*: Bei aktiviertem Modus werden Geometrie-Lücken deaktiviert, Overlay-Intensität auf 0.6 reduziert. Die Stufe bleibt narrativ funktional.

---

### 6.4.6 Schattenfieber-Ambient (Layer-gebunden)

Unabhängig vom Spieler-Infektionslevel haben die Data Layers eine baseline Schattenfieber-Ambience:

- Layer 0 (Untergrund): `ShadowFever_Ambient = 0.15` — die Schwelle ist hier dünn, das spürt man
- Layer 1 (Straße): `ShadowFever_Ambient = 0.05`
- Layer 2 (Arkaden): `ShadowFever_Ambient = 0.0`
- Layer 3 (Türme): `ShadowFever_Ambient = 0.0`

Der Ambient-Wert addiert auf den Spieler-Wert. Ein Spieler ohne Infektion in Layer 0 läuft bei effektiv 0.15 — im Normalzustand nicht bewusst, aber da. Technische Narratologie: die Architektur erzählt die Kosmologie.

---

## 6.5 Nervensystem-Visualisierung

### 6.5.1 Konzept

Das Leveling-System (→ GDD Kap. 2) nutzt eine halbtransparente Nervensystem-Sicht als Visualisierung des Fortschritts. Drei Subsysteme — Cardio (Ausdauer), Muskel (Stärke), Lymph (Immunresistenz/Schattenfieber-Toleranz) — werden als Overlay auf den Charakter-Körper projiziert.

Dieses System hat zwei Modi:
1. **Statistik-Ansicht** (vom Spieler ausgelöst, Menü): Vollbild-Overlay, alle drei Systeme sichtbar, interaktiv
2. **Echtzeit-Overlay** (kontextabhängig): schmales, halbtransparentes Overlay — aktiviert in Stufe 3 Schattenfieber, nach schweren Verletzungen, und optional permanent im HUD

---

### 6.5.2 Technische Umsetzung

**Third-Person-Modus:**
- Overlay via Custom-Depth-Pass auf dem Charakter-Mesh
- Drei Materialschichten (Cardio, Muskel, Lymph) mit eigenem Emissive-Kanal
- Farb-Kodierung: Cardio = warmrot, Muskel = bernsteingelb, Lymph = kühles Grün-Weiß
- Opazität: 0.4–0.7 je nach Kontext (Menü: 0.7, Echtzeit: 0.4)
- Fortschritt sichtbar als Textur-Dichte und Emissive-Intensität — stärkeres Cardio-Subsystem = dichter gezeichnete rote Linien, die heller leuchten

**First-Person-Modus:**
- Separates Arm-Mesh-Set (eigene Asset-Klasse: `SK_FP_Arms`)
- Synchron animiert mit dem Haupt-Charakter-Mesh via Animation-Blueprint
- Nervensystem-Overlay auf das `SK_FP_Arms`-Mesh — der Spieler sieht seine eigenen Unterarme, Hände, angedeutet die Schultern
- **Aufwand-Klassifizierung**: mittel-hoch. Das Arm-Mesh braucht einen vollständigen eigenen Animations-Set. Synchronisation mit dem Haupt-Mesh ist der technische Hauptaufwand. Zeitschätzung: 3 Wochen für stabiles System.

**Shader-Struktur (M_Nervensystem_Base):**
```
Inputs:
  - BaseColor: Charakter-Skin
  - NervensystemMask_Cardio (Texture2D, R-Kanal)
  - NervensystemMask_Muskel (Texture2D, G-Kanal)
  - NervensystemMask_Lymph (Texture2D, B-Kanal)
  - Fortschritt_Cardio (Scalar 0–1)
  - Fortschritt_Muskel (Scalar 0–1)
  - Fortschritt_Lymph (Scalar 0–1)
  - Overlay_Opacity (Scalar 0–1)

Outputs:
  - Emissive: Farb-kodiertes Nervensystem-Leuchten
  - Custom Depth: für Compositing-Pass
```

---

## 6.6 Relikt-Shader — Master Material System

### 6.6.1 Konzept

Das Relikt — der Schwellen-Stabilisator, der kosmologische Resonanzpunkt — existiert als ein einziges Mesh mit einem Master-Material und drei Material-Instanzen. Die Übergänge zwischen den Zuständen sind immer geblended, nie hart. Das Relikt ist kein Gadget; es ist ein kosmologisches Instrument. Das muss im Material sichtbar sein.

---

### 6.6.2 Drei Zustände

**Zustand 1 — Ruhezustand (dormant):**
Das Relikt ruht. Es ist nicht tot — es ist latent lebendig.

- **Base Material**: transluzentes, mattes Grundmaterial
- **Subsurface Scattering (SSS)**: aktiv, warme Untertonfarbe (RGB 1.0 / 0.85 / 0.7 — leicht goldenes Hautton-Unterlicht)
- **SSS-Radius**: 0.8 cm — das Licht streut tief, wie durch organisches Gewebe
- **Roughness**: 0.55 — nicht spiegelnd, aber nicht stumpf. Polierter Knochen oder Elfenbein-Charakter.
- **Emissive**: 0.0 — kein aktives Leuchten
- **Lumen-Emitter**: deaktiviert

*Designabsicht*: Das Relikt soll schon im Ruhezustand anders aussehen als totes Material. Das SSS erzeugt ein inneres Lebendigkeit — etwas ist da, schläft aber.

---

**Zustand 2 — Aktiver Zustand (resonant):**
Das Relikt ist aktiviert. Es ist zur Lichtquelle geworden.

- **Base Material**: dasselbe Grundmaterial, aber SSS-Intensität um 40% erhöht
- **Emissive-Layer**: hochgefahren, Farbe = warmes Indigo-Weiß (RGB 0.85 / 0.8 / 1.2, überbelichtet bei 3.5)
- **Lumen-Emitter**: aktiviert (Klasse A) — das Relikt wirft echtes GI in die Szene, färbt umliegende Wände und Böden
- **Lichtfarbe Lumen**: leicht violett-weiß (CCT 7500K mit Indigo-Bias) — kühler als natürliches Licht, kalt und klar
- **Lichtradius**: 4m für direkte Lumen-Reichweite, darüber Bloom-Halo
- **Bloom-Halo**: 6.0 Radius, Indigo-Tint — sichtbar auch auf Screenshots, nicht nur in Bewegung

*Designabsicht*: Das aktivierte Relikt soll sofort als Lichtquelle erkennbar sein. Es ist die wichtigste dynamische Lichtquelle in jeder Szene, in der es aktiv ist.

---

**Zustand 3 — Kritischer Zustand (überlastet):**
Das Relikt ist am Limit. Das kosmologische Instrument bricht unter Last.

- **Base Material**: Riss-Overlay-Layer aktiv — ein Masked-Texture-Layer projiziert organische Rissstrukturen auf die Oberfläche
- **Riss-Struktur**: `T_Relikt_Riss_01` (Procedural Noise-basiert, kein symmetrisches Muster) — Risse öffnen sich im Laufe des kritischen Zustands (Blend-Parameter steuert Öffnungsgrad)
- **Innenleuchten**: durch die Risse scheint das Emissive-Innere — lokal höhere Emissive-Intensität an Riss-Kanten (8.0+, kalt-violett)
- **Subsurface Scattering**: jetzt blau-violett getönt (RGB 0.7 / 0.6 / 1.3) — die Wärme ist weg, das SSS-Licht ist kalt
- **Lumen-Emitter**: flackernd, instabil (Blueprint-gesteuerte Intensitätsschwankung, 2–8 Hz unregelmäßig)
- **Lichtfarbe**: hard-violett (CCT >10000K, stark ins Ultraviolett verschoben)
- **Vertex-Animation**: das Mesh selbst vibriert leicht (±0.2mm, 12 Hz) — submillimeter, erzeugt nervöses Shimmern

*Designabsicht*: Visuelles Vokabular entspricht bewusst PP-Stufe 3. Das Relikt und das Schattenfieber sprechen dieselbe Sprache: Rissstrukturen, Kalt-Violett, Innenleuchten, Instabilität. Der Spieler sieht diese Verbindung — ob er sie versteht, ist Erzählung.

---

### 6.6.3 Master-Material-Struktur (M_Relikt_Master)

```
Parameter-Gruppen:
  [Base]
    Roughness (Scalar)
    BaseColor (Vector)

  [SSS]
    SSS_Enabled (StaticBool)
    SSS_Color (Vector)
    SSS_Radius (Scalar)
    SSS_Intensity (Scalar)

  [Emissive]
    Emissive_Enabled (StaticBool)
    Emissive_Color (Vector)
    Emissive_Intensity (Scalar)
    Emissive_Flicker (Bool)
    Emissive_FlickerFrequency (Scalar)

  [Riss]
    Riss_Enabled (StaticBool)
    Riss_Mask (Texture2D)
    Riss_BlendAmount (Scalar 0–1)
    Riss_EmissiveBoost (Scalar)

  [State_Blend]
    State_Alpha (Scalar 0–2.0)
    -- 0.0 = Zustand 1, 1.0 = Zustand 2, 2.0 = Zustand 3
    -- Alle Parameter interpolieren im Blueprint anhand dieses Wertes
```

**Drei Material-Instanzen**: `MI_Relikt_Dormant`, `MI_Relikt_Resonant`, `MI_Relikt_Critical` — alle vom selben Master. Blueprint interpoliert zwischen den Instanz-Parametern über `State_Alpha`.

---

## 6.7 Houdini-Pipeline — Terrain und Prozedurale Systeme

### 6.7.1 Terrain-Generierung

Die vertikale Stadt braucht eine Basis-Topografie: das Flusstal, die Hügelketten der umgebenden Mittelgebirgs-Landschaft, die natürlichen Erhebungen, auf denen die Stadtschichten gebaut sind.

**Workflow:**
1. Basis-Terrain in **Houdini** procedural generiert (Houdini Heightfield-System)
2. Export als `.hdr`-Heightmap nach UE5 (16-bit, 4096×4096 für Kernregion)
3. In UE5: Landscape-System mit Nanite-Tessellation für Nahbereich
4. Automatisches Foliage-Placement via PCG (Procedural Content Generation Graph, UE5 native)

**Houdini-Setup:**
- Basis-Erosion: hydraulische Erosion für naturwirkende Täler und Rinnsale
- Stadtplattform-Sculpting: manuelle Eingaben (Terrassen-Formen für die Stadtebenen) werden in Houdini als Kontrollkurven eingebracht
- Fluss-System: Heightfield-Vexnet für Flussbettgenerierung
- Output-Auflösungen: 4k für Terrain-Kern (2km Radius), 2k für äußere Bereiche (10km Radius)

*Offene Frage an Vera*: Gibt es definierte Punkte für Stadteingang, wichtige Sichtachsen (z.B. von der Stadtmauer auf den Gildenhochbau)? Die brauche ich als Constraint-Kurven für das Houdini-Setup.

---

### 6.7.2 Prozedurale Stadtdetails (PCG-Systeme)

Für wiederholende Stadtdetails (Pflasterstein-Muster, Mauer-Erosion, Fassaden-Ageing, Schimmel-Verteilung im Untergrund) wird ein PCG-System aufgebaut:

- **Pflaster-Variation**: PCG platziert Stein-Typ, Rotation, Abnutzungsgrad basierend auf Nähe zu Fußwegen und Schicht-Tiefe
- **Fassaden-Ageing**: prozedurale Wear-Maps generiert in Houdini, instanziiert via PCG
- **Biolumineszenz-Cluster**: Niagara-Systeme werden via PCG in Layer-0-Bereichen platziert, Dichte abhängig von Nähe zu Wasserquellen (simuliert Feuchtigkeitskorrelation)
- **Vegetation-Infiltration**: in Slum-Bereichen und verlassenen Abschnitten wachsen prozedurale Pflanzen-Cluster aus Rissen

---

## 6.8 Color Science & Display-Pipeline

### 6.8.1 Color-Management

RELICS nutzt **ACES** (Academy Color Encoding System) als Farbraum-Standard.

**Pipeline:**
```
Kreativ-Input → ACEScg Arbeitsraum → ACES Tonemapping → Display-Transform (sRGB/DCI-P3)
```

- Alle Texturen: in sRGB gespeichert, im Shader in lineares Licht konvertiert
- Emissive-Werte: in physikalischen Einheiten (cd/m²) definiert, nicht als 0–1-Werte
- LUT (Look-Up-Table): ein Basis-LUT für den RELICS-Look (kühle Schatten, gedämpfte Mitten, klare Lichter), drei Varianten (Normal / Schattenfieber-Stufe-2 / Schattenfieber-Stufe-3)

**Warum kein AgX?** AgX ist für Photography optimiert und komprimiert Highlights weicher. RELICS braucht scharfe, klare Lichter — die Bergkristall-Linsen, die Relikt-Emitter müssen leuchten, nicht weich werden. ACES gibt uns das.

---

### 6.8.2 Display-Kalibrierung (internes Studio)

Alle Arbeitsstationen im Studio haben kalibrierte Displays (Delta-E < 2.0). Die Referenz-LUT läuft auf einem Samsung Odyssey OLED, der als "Goldstandard"-Display dient. Spieler-seitig gibt es keine Kontrolle — daher sind alle Emissive-Werte so kalibriert, dass sie auch auf einem Standard-SDR-Display (sRGB, 200 cd/m² Peak) korrekt wirken. HDR-Displays bekommen automatisch einen separaten Display-Transform mit erweiterten Highlight-Bereichen.

---

## 6.9 Produktion & Release-Pipeline

### 6.9.1 Milestone-Übersicht

| Milestone | Technischer Status | Schlüssel-Deliverables |
|---|---|---|
| **Pre-Alpha** | Prototyp-Pipeline | Rendering-Architektur steht, Material-Master-Systeme gebaut, World Partition Setup stabil |
| **Alpha** (Streamer) | Feature-Freeze Rendering | Data Layers gesetzt, Lumen-Konfiguration fixiert, PP-System stabil, Relikt-Shader stabil. Standard: stabil + konsistent, NICHT polished |
| **Beta** | Tuning-Phase | Alle bestehenden Systeme werden tuned — Performance-Optimierung, visuelle Feinheit, Accessibility vollständig |
| **Full Release** | Feinschliff + große Setpieces | Abschließende Lighting-Pass für alle Hauptorte, Cinematic-Sequenzen final |
| **DLC** | Erweiterung auf stabiler Basis | Neue Assets auf bestehenden Systemen — kein neues technisches Risiko in DLC-Phase |

**Alpha ist der härteste Freeze**: Nach Alpha-Abgabe sind folgende Systeme nicht mehr änderbar:
- Data Layer-Struktur (Schichtanzahl, Naming, Streaming-Logik)
- Lumen-Konfiguration (RT-Modus pro Layer)
- Schattenfieber-PP-System-Architektur (Blueprint-Struktur, Parameter-Namen)
- Relikt-Master-Material-Struktur (Parameter-Gruppen, Slot-Namen)
- Kamerasystem-Grundstruktur

*Begründung*: Diese Systeme sind die Säulen, auf denen alle anderen Content-Systeme aufbauen. Eine Änderung nach Alpha bricht zuverlässig abhängige Systeme. Tuning ist erlaubt. Umstrukturierung nicht.

---

### 6.9.2 Pre-Alpha — Technische Prioritäten

**Woche 1–4: Foundation**
- UE5 Projekt-Setup, Engine-Version fixieren
- World Partition aktivieren, vier Data Layers anlegen und testen
- Lumen-Konfiguration pro Layer einrichten (Software RT / Hardware RT, Hybrid Baked für Layer 0)
- Erste Prototyp-Materialien: ein Oberschicht-Material, ein Unterschicht-Material, ein Emissive-Klasse-A

**Woche 5–8: Kernsysteme**
- Schattenfieber-Blueprint (alle drei Stufen, smooth geblended)
- Relikt-Master-Material (alle drei Zustände)
- Kamerasystem (Third/First Person Blend)
- Nervensystem-Shader (Third-Person-Modus, First-Person folgt in Woche 10–12)

**Woche 9–12: Integration**
- Biolumineszenz-Pipeline (Klasse A/B/C operativ)
- PCG-System für erste Straßen-Füllung
- Houdini-Terrain-Export → UE5 getestet
- Accessibility-Optionen implementiert und getestet
- Interne Alpha-Kandidat: alle Systeme laufen, kein Polishing

---

### 6.9.3 Monetarisierung — Technische Implikation

Das Briefing ist eindeutig: **Klassisch Premium, keine Mikrotransaktionen.** Das hat eine direkte technische Konsequenz, die ich hier festhalten will:

Kein Live-Service-Backend. Keine Server-seitige Spielstand-Validierung. Keine DRM-Middleware, die Runtime-Overhead erzeugt. Das ist eine technische Erleichterung: die Architektur ist offline-first, save-game ist lokal, kein Always-Online-Requirement.

DLC-Technisch: DLC-Content wird als Pak-Files geliefert (UE5 Standard). Das Basis-Spiel enthält keine Platzhalter für DLC-Content — DLC erweitert auf der stabilen Basis, belegt aber keine Speicherpunkte in der Hauptgame-Dateistruktur.

---

## 6.10 Risiko-Register

| System | Priorität | Risiko | Mitigation |
|---|---|---|---|
| Lumen vertikale GI | HOCH | Degeneriert in tiefen Kanälen | Hybrid Baked für Layer 0, Lumen-Importance-Volumes |
| World Partition vertikal | HOCH | UE5 primär horizontal konzipiert | Manuelle Data Layers, Occlusion Volumes an Ebenen-Übergängen |
| Schattenfieber PP Accessibility | HOCH | Vertex-Animation und DOF-Pulsieren = Motion-Sickness-Risiko | Accessibility-Option Pflicht, intern getestet mit betroffenen Personen |
| Nanite dünne Geometrien | MITTEL | Absturz bei dünnen Meshes | Fallback-LOD-Workflow definiert, Asset-Klassifizierung obligatorisch |
| Biolumineszenz Performance | MITTEL | Viele Emitter = GI-Overhead | Dreiklassen-System, Klasse-A-Budget: max. 12 gleichzeitig |
| Nervensystem Arm-Mesh | MITTEL | Hohes Animations-Aufwand im FP-Modus | Eigenständiger Task, 3-Wochen-Schätzung, eigenständige Asset-Klasse |
| Relikt-Shader-Synchronität | NIEDRIG | State-Alpha-Drift zwischen Blueprint und Material | Interface-Konvention festgelegt, Parameternames dokumentiert |

---

\clearpage
