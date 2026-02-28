---
title: "RELICS — Game Design Document"
subtitle: "Anhang B · v0.2"
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

# QA-Bericht Tag 3 — Leo Fischer

**Datum:** Mittwoch, Tag 3, 10:30–12:00 Uhr
**QA-Typ:** Kapitel-Review (Spielerperspektive + Briefing-Konsistenz)
**Reviewer:** Leo Fischer, QA Lead
**Checkliste:** Wolf-Infrastrukturen, Terminologie, Sauberkeit, Vollständigkeit, interne Konsistenz

**Umfang:** 4 Kapitel gereviewed
- `01-spieluebersicht-v1.md` (Darius)
- `04-schluesselfiguren-v1.md` (Nami)
- `06-technische-spezifikation-v1.md` (Tobi)
- WBB `01-mythos-v1.md` (Emre)

---

## TL;DR — Executive Summary

**Allgemeines:** Die Kapitel hängen kohärent zusammen. Die vier Agenten haben gut kommuniziert. Aber: **Drei KRITISCHE Blocking-Punkte**, die vor Darius' v2-Revision gelöst sein müssen, und **eine Design-Doc-Hygiene-Schuld**, die bis zur Alpha-Freigabe weg muss.

**Bleeding Issues** (sofort handeln):
1. **Relikt-Namenspolitik** — Vier verschiedene Label für dasselbe Objekt. Briefing sagt "Schwellenanker" ist der Name. Kapitel befolgen das nicht konsistent.
2. **Emres Widersprüche-Log** — W-001 (Substanz vs. Bedingung), W-003 (Flora/Fauna undefiniert), W-004 (Tiervolk kosmologischer Ursprung), W-005 (Relikt-Physik vage).
3. **Autor-Nummern in sichtbaren Texten** — CD-Feedback: "Saubere Dokumente, keine Namen." Violiert in Kap 01 und Kap 04.

---

## Detailanalyse nach Wolf-Infrastrukturen

### 1. Karten (Geographie, räumliche Ordnung)


**Gut:**
- Emre (WBB 01) definiert die vertikale Ordnung klar: Oben = Sicherheit, Unten = Schwellennähe
- Tobi (Kap 06) hat die Schicht-Architektur technisch umgesetzt (vier Data Layers, Streaming-Logik)
- Schwarzrand-Topografie ist beschrieben (Talkessel, Felswände, vertikale Stadt)

**Problematisch:**
- **Keine Detailkarte.** Wo sind die Gilden-Viertel konkret? Wo die Ordenssitze? Wo der Kronpalast? Das sieht nach Vera-Aufgabe aus, aber: Im GDD sollte mindestens erwähnt sein, welche NPCs in welcher Schicht sichtbar werden (Spieler-Erkenntnis). Kap 04 (Nami) hat das ansatzweise: "Der Spieler merkt die Schichtung" — aber nicht konkret.
- **Houdini-Terrain-Constraints fehlen** — Tobi schreibt in 6.7.1: "Offene Frage an Vera: Gibt es definierte Punkte für Stadteingang, wichtige Sichtachsen?" Das ist KRITISCH und sollte vor Woche 1–4 Pre-Alpha geklärt sein, nicht offen.

**QA-Empfehlung:** Vera sollte bis Ende heute eine Skizze (Schichttrennung, Hauptzugangsrouten, 2–3 definierte Sichtachsen) bereitstellen. Kann dann in WBB Kap 2 (Topos) ausgearbeitet werden.

---

### 2. Zeitleisten (Geschichte, Konflikte, Wendepunkte)


**Gut:**
- Emre definiert: "Vor einer Generation wurde die Wurzelkammer geöffnet" — das ist der Wendepunkt
- Darius (Kap 01) referenziert das: "Die Öffnung" ist die narrative Absicht
- Nami (Kap 04) baut Quest-Struktur drauf: Act 1 = Fragment-Suche, Act 2 = Muster erkennen, Act 3 = Ursprung

**Problematisch:**
- **"Vor einer Generation" ist nicht konkretisiert.** Emre schreibt in Widerspruchs-Log W-006: "20 Jahre? 30 Jahre? 40 Jahre?" Das beeinflusst, welche NPCs Zeitzeugen sind. Hieronymus Vael (Kap 04) sollte einer sein, aber sein Alter (ca. 50, "sieht achtzig aus") muss konsistent sein.
- **Keine Zeitleiste der Fraktionen.** Wann spalten die Fraktionen sich? Wann gründen die Gilden ihre Monopole? Das ist implizit in Emre (WBB 01, Abschnitt 6 — Gilden-Monopolstruktur), aber nicht chronologisiert.
- **Relikt-Entfernung vs. Schattenfieber-Eskalation nicht konkretisiert.** Emre schreibt: "Vor einer Generation [...] öffnete jemand die Wurzelkammer. [...] Das Schattenfieber breitete sich explosionsartig aus." Aber: wie lange dauerte die Eskalation? Wochen? Monate? Das ändert alles für Spieler-Verstehen.

**QA-Empfehlung:** Emre + Nami müssen gemeinsam festlegen:
- Konkrete Jahreszahl der Öffnung
- Eskalations-Zeitleiste (Schattenfieber-Ausbreitung)
- Wer war Zeuge wann (für Nami's Quest-Struktur)

Bis Ende heute sollte da Klarheit sein. Ist für Act 1 blockierend.

---

### 3. Genealogien (Figurennetze, Dynastien)


**Gut:**
- Nami (Kap 04) hat fünf Kernfiguren stark ausgearbeitet: Hieronymus, Adelhaid Brenn (Krone), Ivo Scherer (Orden), Vreni Kast (Gilden), Salva (Tiervolk)
- Jede Figur hat klare Stimme und versteckte Absichten — das ist Qualität
- Fraktions-Hierarchien angedeutet: "Marschall" (Brenn), "Forschungsbruder" (Scherer), "Gildenmeisterin" (Kast)

**Problematisch:**
- **Keine Feudal-Hierarchie.** Wer ist der König/die Königin? Wer führt den Orden? Wer ist der Gildenrat-Chef? Nami schreibt "Spieler kann Fraktionen beitreten" — aber mit welchen NPCs? Nur mit den fünf?
- **Tiervolk-Status unklar.** Salva ist "keine Fraktion, sondern lose Gemeinschaft." Nami schreibt in Kap 04: "Das Tiervolk ist kein Volk" (Section 4.4). Aber: Wer sind die anderen Reisenden? Hat jeder einen Namen/eine Rolle?
- **Nami erwähnt "alte Mann in den Slums" (Nebenquest-Idee, Section 4.6).** Aber: Name? Funktion? Das ist noch eine Nebennotiz, nicht ausgearbeitet.

**QA-Beobachtung:** Die Kern-5-Figuren sind hervorragend. Aber die Welt fühlt sich klein an, wenn nur diese 5 prägen. Gothic 2 hat 50+ benannte NPCs mit Tagesablauf. RELICS strebt "Dichte vor Breite" an — aber es braucht genug Dichte, dass die Welt atmet. Das ist für v1 okay (Skelet), aber muss bis Beta ausgebaut sein.

**QA-Empfehlung:** Nami sollte bis Beta ein Genealogie-Diagram zeichnen: Fraktions-Hierarchie mit 3–5 NPCs pro Fraktion, dann sekundäre Kontakte. Das ist ein großes Dokument, aber für Quest-Planung essential.

---

### 4. Natur (Flora, Fauna, Ökologie)


**Gut:**
- Emre erwähnt Schattenflora und Schwellenfauna — klingt richtig
- Tobi (Kap 06) hat "Vegetation-Infiltration" als PCG-System — schön
- Biolumineszenz ist konsistent über alle Kapitel (Kap 06, WBB 01)

**Problematisch:**
- **Emre schreibt selbst (WBB 01, W-003): "Komplett undefiniert. [...] Muss in Kap. 2 (Topos) kommen."**
- **Was sind konkrete Pflanzen/Tiere?** Gibt es Schwellen-Pilze? Schwellen-Insekten? Mutierte Waldtiere? Nichts davon ist beschrieben.
- **Tiervolk-Herkunft unklar.** Briefing sagt: "Tiervolk weniger tribal, leicht alien vs. menschlich clean." Aber: Sind sie menschliche Mutanten? Eigene Spezies? Emre schreibt in Widerspruchs-Log W-004: "Muss geklärt werden. KRITISCH."
- **Nahrungskette/Ökologie fehlt.** Das scheint zu Vera-/Emre-Aufgabe (Topos-Kapitel) zu gehören, aber sollte hier angedeutet sein.

**QA-Warnung:** Das ist nicht "schön zu haben". Das ist Welt-Konsistenz. Ein Spieler, der in den Schlund steigt, sieht Pflanzen. Diese Pflanzen müssen visuell erzählen, dass die Schwelle hier nah ist. Vera braucht Referenzen. Emre muss die liefern. **Bis Beta ist das blockierend für die visuelle Kontinuität.**

**QA-Empfehlung:** Emre macht für WBB Kap 2 (Topos) eine Natur-Unterliste: 5–7 Schwellenflora-Typen (mit Name, Visuelle Beschreibung, biologischer Zweck), 3–4 Schwellenfauna (dito), Tiervolk-Herkunftshypothese (auch wenn Spieler das nie erfährt — für innere Konsistenz).

---

### 5. Kultur (Bräuche, Kunst, Religion, Alltagsleben)


**Gut:**
- Darius (Kap 01) hat Materialsprache perfekt: Oberschicht = All-Black/Monochrom, Unterschicht = Grau/Schmutzig + gestohlene Farbe
- Emre (WBB 01) hat Fraktions-Kosmologien detailliert: Krone (Legitimation durch Siegel), Orden (Legitimation durch Wissen), Gilden (Legitimation durch Material)
- Nami (Kap 04) zeigt Alltagsleben durch NPC-Stimmen: Brenn spricht bürokratisch, Scherer stellt Gegenfragen, Kast spricht schnell
- Gilden-Monopole konkretisiert in Emre (WBB 01, Abschnitt 6): Schmiede, Glasmacher, Weber, Gerber, Goldschmiede, Kerzenzieher, Pergamenter, Steinmetze

**Lücken:**
- **Religion/Spiritualität.** Der Orden hat eine Theologie, aber: Gibt es andere Glaubenssysteme? Private Altäre in den Slums? Aberglaube? Nami könnte das ausbauen, aber es ist nicht da.
- **Alltag in den Schichten.** Was essen die Unterschicht-Bewohner? Was machen sie nachts? Wo schlafen sie? Das ist Material für Welt-Glaubhaftigkeit — kommt aber erst in "Topos"-Kapitel.

**QA-Note:** Die Kultur-Tiefe ist hier sehr gut. Nicht perfectible, aber solide.

---

### 6. Sprache (Namenssysteme, Dialekte)


**Gut:**
- Schwarzrand — Name funktioniert (Emre, WBB 01)
- Charakter-Namen haben germanischen Klang: Adelhaid, Ivo, Vreni, Hieronymus — korrekt für "Mitteleuropa + germanische Mythologie"
- Fraktion-Labels sind klar: Krone, Orden, Gilden

**Problematisch:**
- **Keine Dialektsysteme.** Sprechen Unterschicht-NPCs anders als Oberschicht? Emre hat das nicht definiert. Nami könnte es in die Stimmen-Beschreibung einbauen (z.B. "Brenn spricht wie eine Offizierin, korrekt, ohne Dialekt").
- **Tiervolk-Namen.** Salva ist "Platzhalter" (Nami, Kap 04). Wie nennen sich die Reisenden untereinander? Gibt es ein Tiervolk-Namenssystem?
- **Schwellenphänomene-Vokabular nicht etabliert.** Emre schreibt "Flüstern" (Stufe 1), "Wandlung" (Stufe 2), "Entgrenzung" (Stufe 3) — aber sind das echte Straßen-Namen? Oder NPC-Jargon? Spieler-Vokabular?

**QA-Empfehlung:** Für WBB Kap 3 (Ethos) sollte Nami/Emre ein Sprachsystem definieren. Nicht obligatorisch für GDD v2, aber wichtig bis Beta.

---

### 7. Mythologie (Schöpfungsmythen, Legenden, Prophezeiungen)


**Gut:**
- Emre (WBB 01, Abschnitt 4) hat drei Schöpfungsmythen ausarbeitet — jeder mit klarer Fraktion und verstecktem Inhalt:
  - Krone: "Das Erste Siegel" (Legitimation durch kosmische Notwendigkeit)
  - Orden: "Die Prüfung" (Legitimation durch Wissen)
  - Gilden: "Der Rohstoff" (Legitimation durch Material)
- Jeder Mythos hat "Was sie verrät" + "Was sie verschweigt" — das ist Qualitäts-Struktur
- Emre schreibt explizit: "Keine ist vollständig wahr. Keine ist vollständig falsch." Das ist genau richtig.

**Kleine Lücke:**
- **Keine Volkslegenden.** Gibt es Märchen im Schlund? Übernatürliche Geschichten, die Spieler hören? Das ist Detail, kann aber in Quests eingehen.
- **Prophezeiungen?** Briefing sagt "kein High Fantasy" — also wahrscheinlich keine klassischen Prophezeiungen. Aber: Gibt es dunkle Ahnungen bei den alten NPCs?

**QA-Note:** Dieser Teil ist hervorragend. Emres mythologische Struktur ist die Stärke dieses GDD-Sets.

---

### 8. Philosophie (Weltsicht, Ethik, Wertesysteme)


**Gut:**
- Darius (Kap 01) hat Philosophie in die Design-Säulen eingebaut:
  - Säule I (Immersive Simulation): "Die Welt reagiert auf mich"
  - Säule II (Fraktionspolitik): "Ich wähle nicht die gute Fraktion"
  - Säule III (Körperlicher Fortschritt): "Mein Körper ist mein Fortschrittsanzeiger"
  - Säule IV (Dichte vor Breite): "Diese Welt existierte, bevor ich ankam"
- Emre (WBB 01) hat Fraktion-Philosophien in den Mythen: Materialismus (Gilden), Providentialismus (Orden), Souveränismus (Krone)
- Nami (Kap 04, Section 4.4): "Die Wahrheit ist eine Arbeit, die der Spieler leisten muss" — das ist eine Epistemologie-Statement

**Könnte ausgearbeitet werden:**
- **Spieler-Ethik** nicht explizit. Welche moralischen Dilemmata soll der Spieler erleben? "Fragment ablehnen ist Kosmologie-Wahl" (Briefing) — aber wo sind andere ethische Fragen?
- **Nihilismus-Falle.** Wenn Spieler sich in einer Welt sieht, wo "keine Fraktion gut ist," kann das existenzbedrohend wirken (was gewollt ist) oder deprimierend (was nicht gewollt ist). Wie balanciert das Design dagegen?

**QA-Note:** Philosophie ist implizit gut. Für Streamer-Alpha ist das ausreichend.

---

### 9. Verknüpfung (Wechselwirkungen zwischen Infrastrukturen)


**Übersicht der Verknüpfungen:**
```
Schwelle (Geographie)
  ↓
Schwellensubstrat (Biologie)
  ↓
Schattenfieber (Drei Stufen)
  ↓
Lymph-Subsystem (Gameplay, Darius)
  ↓
Fraktions-Reaktionen (Lore, Emre + Nami)
  ↓
Quest-Struktur (Nami)
  ↓
NPC-Motivationen (Nami)
  ↓
Spieler-Entscheidungen
```

Das ist eine lineare Kette, die aufgeht. Das ist gut. Keine Widersprüche in der Verknüpfung.

**Aber: Siehe "Widerspruchs-Log" unten.**

---

## Terminologie & Namenspolitik — KRITISCHES PROBLEM

**Bleeding Issue #1: Relikt-Labeling**

Das Briefing schreibt (siehe Memory Tag 3, Briefing-Abschnitt):
> "Schwellenanker-Name = Relikt (nicht "Relikt-Anker" oder andere Varianten)"

**Wie die Kapitel das handhaben:**

| Kapitel | Autor | Label | Zitat |
|---------|-------|-------|-------|
| GDD 01 | Darius | "Die Wurzel" | "die Wurzel als Schwellenanker ist lore-seitig gesetzt" (Zeile 238) |
| GDD 04 | Nami | "Das Relikt" + "Der Schwellenanker" | "das Relikt ist ein Schwellen-Stabilisator" (WBB 01) + "der Hauptquest dreht sich um diese Suche" (ohne Label) |
| WBB 01 | Emre | "Das Relikt" / "Schwellen-Stabilisator" | "Das Relikt ist ein Schwellen-Stabilisator." (Zeile 241) |
| GDD 06 | Tobi | "Das Relikt" | "Das Relikt -- der Schwellen-Stabilisator" (Section 6.6) |

**Das Problem:**
- Darius nennt es "Die Wurzel" — Emre definiert "Wurzelkammer" (Ort) + "das Relikt" (Objekt)
- Nami schreibt manchmal "Fragment" (das Stück), manchmal "das Relikt" (das Ganze), manchmal "Der Schwellenanker" (Label für Quest?)
- Das Briefing sagt: Der Serientitel ist "RELICS: [Relikt-Name]". Wenn das Objekt "Die Wurzel" heißt, dann "RELICS: Die Wurzel". Aber Emre nennt es "Das Relikt."

**Spielerperspektive:** Ein Spieler hört in der ersten Stunde:
1. Hieronymus übergibt "Fragment" → "Das Relikt"?
2. Boten sprechen über "Das Relikt" oder "Die Wurzel"?
3. In Quests: "Finde den Schwellenanker"?
4. Im HUD: "Quest: Das Relikt zurückbringen"?

Das ist verwirren.

**QA-Entscheidung anfordern:**
Darius + Emre + Nami müssen bis 14:00 Uhr HEUTE entscheiden:
1. **Internaler Name (Lore):** "Die Wurzel" oder "Das Relikt"?
2. **Spieler-Label (Quest/HUD):** "Das Relikt" oder "Der Schwellenanker"?
3. **Serientitel:** "RELICS: Die Wurzel" oder "RELICS: Das Relikt"?

Meine QA-Empfehlung:
- **Intern (Emre/Nami-Dialog):** "Die Wurzel" = das ursprüngliche, stabile Objekt in der Wurzelkammer. "Das Relikt" / "Das Fragment" = das Stück, das der Spieler trägt.
- **Spieler-Sicht:** "Der Schwellenanker" (allgemeiner NPC-Begriff) oder "Die Wurzel" (wenn Spieler sie findet). Nicht "das Relikt" — zu abstrakt.
- **Serientitel:** "RELICS: Die Wurzel" klingt besser als "Die Fragmente" oder "Das Relikt."

Aber das ist eine Entscheidung, nicht meine Empfehlung. **MUSS GELÖST SEIN BIS V2.**

---

## Sauberkeit — CD-Feedback-Violationen

**Bleeding Issue #2: Autor-Namen im sichtbaren Text**

CD-Feedback (Briefing-Log, Tag 3 09:00):
> "PDFs müssen sauber sein (keine Kommentare, Namen, Metadaten-Krümel)"

**Violationen gefunden:**

**In Kap 01 (Darius, Spielübersicht):**
- Zeile 4: "Quellen: Briefing, Deus Ex GDD v5.3e (Spector/Ion Storm 1997), Diablo Pitch Document (Condor 1994), **eigene Recherche-Notizen Tag 1, Emre-Output Tag 2, Nami-Notizen Tag 1, Leo-Analyse Tag 1**"
- Zeile 76: "Referenzen | Gothic 2, Deus Ex, Vampires the Masquerade: Bloodlines, Prey 2017 | **Leo (Recherche Tag 1): "Dichte statt Breite ist unser schärfstes Unterscheidungsmerkmal."**"

Das sind Quellen-Referenzen auf andere Agenten. Das ist im Arbeitsdokument okay, aber NICHT in der PDF-Freigabe. Das muss zu neutralen Labels werden: "Forschung Tag 1" statt "Leo-Analyse Tag 1", oder einfach raus.

**In Kap 04 (Nami, Schlüsselfiguren):**
- Zeile 3: "Autorin: Nami Okafor — Narrative Designer" (okay)
- Zeile 82: "Die Fragment-Übergabe ist der **Clip-Moment (Leo, 14:00 Sync)**."

Das ist ein Prozess-Kommentar. "Leo, 14:00 Sync" ist ein interner Referenz. In der Spieler-PDF hat das nichts zu suchen.

**In Kap 06 (Tobi, Tech-Spec) und WBB 01 (Emre, Mythos):**
- Keine großen Violationen, aber: WBB 01 Zeile 46: "*Design-Anmerkung: Die germanische Mythologie...*" — das ist Autor-Stimme. Sollte neutralisiert werden.

**Remediation für v2:**
- Alle "(Name, Prozess)" Kommentare entfernen
- Autor-Anmerkungen in HTML-Kommentare verschieben: `<!-- Leo: ... -->`
- Quellenreferenzen auf andere Agenten in neutrale Labels umwandeln

**Timeline:** Das ist nicht blockierend für Darius-Sync (Darius hat den Text ja gelesen), aber VOR PDF-Export (Alpha-Snapshot) muss das weg sein.

---

## Interne Konsistenz — Emres Widerspruchs-Log

**Emre hat selbst 6 Widersprüche gelistet (WBB 01, Section 7).** Das ist ehrlich und hilfreich. Aber es sind KRITISCHE Lücken.

| # | Betrifft | Problem | Leo-Bewertung |
|---|----------|---------|---------------|
| W-001 | Schwellensubstrat | Ist es Substanz oder Bedingung? | **KRITISCH** — ändert die Kosmologie. Substanz = Spieler könnte es "sammeln". Bedingung = es ist um dich herum, du kannst nicht davonlaufen. |
| W-002 | Stufe-1-Reversibilität | Wenn vollständig reversibel, warum suchen manche es auf? | **MITTEL** — logisch, aber nicht spielmechanisch blockierend. Antwort: "Kippmoment basierend auf Dosierung/Zeit" würde reichen. |
| W-003 | Biotech-Flora/Fauna | Komplett undefiniert | **HOCH** — Vera braucht Reference für visuelle Entwicklung. Emre muss mindestens 5 Beispiele haben (für WBB Kap 2). |
| W-004 | Tiervolk | Kosmologischer Ursprung unklar | **KRITISCH** — Salva ist ein wichtiger NPC, Nami hat ihn skizziert, aber: wo kommt sein Volk HER? Mutation? Eigene Spezies? Relikt-Effekt? Das ändert Erzählung fundamental. |
| W-005 | Relikt-Physik | Stabilisierungsmechanismus zu vage | **MITTEL** — nicht spielmechanisch, aber: für Glaubhaftigkeit sollte Emre eine pseudophysikalische Erklärung haben (nicht Spieler-sichtbar, aber for consistency). |
| W-006 | Zeitlinie der Öffnung | "Vor einer Generation" unkonkretisiert | **HOCH** — Nami braucht das für NPC-Alterskonistenz und Zeugenfragen. |

**QA-Empfehlung:**
- W-001, W-004, W-006 müssen bis heute 14:00 geklärt sein (vor Nami's weitere Arbeit)
- W-003 muss bis morgen geklärt sein (Vera braucht Reference)
- W-002, W-005 können bis Ende dieser Woche offen bleiben

**Emre sollte dazu angemerkt werden:** "Dein Log ist hilfreich. Statt das offen zu lassen, kannst du eine Hypothese aufschreiben — auch wenn Spieler das nie erfährt. Das ist für interne Konsistenz genug."

---

## Vollständigkeit — Wolf-Checkliste vs. Briefing

**Emre hat eine Wolf-Checkliste (WBB 01, Section 8). Feedback:**

| Infrastruktur | Abgedeckt | Zu Beta | Anmerkung |
|---|---|---|---|
| Karten | Teilweise | Vera: Detailkarte + Level-Design Constraint-Points | |
| Zeitleisten | Teilweise | Emre + Nami: konkrete Jahreszahlen, Zeugenlisten | |
| Genealogien | Nein | Nami: Fraktion-Hierarchie für Beta | |
| Natur | Minimal | Emre: 5+ Flora/Fauna-Typen + Tiervolk-Herkunft | |
| Kultur | Ja | Nami: Optional — Alltagsleben, Spiritualität vertiefen | |
| Sprache | Minimal | Emre/Nami: Dialekt + Tiervolk-Namenssystem | |
| Mythologie | Ja | Keine Lücken | |
| Philosophie | Ja | Optional — Spieler-Ethik-Dilemmata ausarbeiten | |
| Verknüpfung | Ja | Keine Lücken | |

**Spieler-Perspektive: "Erste 30 Minuten"-Checkliste**

Nach Briefing-Anforderung ("Erste Stunde muss stehen") + Leo-Memory (Alpha-Erste-Stunde-Metriken):

- **Min 0–5: Material-Klasse erkennbar?** ✅ Ja (Darius Kap 01 + Nami Kap 04: Unterschicht-Ausrüstung für Spieler)
- **Min 5–10: Emotionale Hook am sterbenden NPC?** ⚠️ Nami hat Hieronymus ausgearbeitet (gut), aber: Replikations-Zeit? Animation? VO-Zeilen? Das ist nicht-GDD-Territory, aber muss stehen.
- **Min 10–15: Skill-by-Use erste Nutzungen sichtbar?** ❌ GDD Kap 02 (Kernmechaniken) fehlt. Das ist Darius-Aufgabe, blockiert aber Bewertung. Kann nicht QA-en, bis es existiert.
- **Min 15–30: Fraktions-Asymmetrie echte Wahl?** ✅ Nami hat drei Boten mit unterschiedlichen Angeboten (gut). Aber: Wie schnell muss Spieler wählen? Da sollte Zeitdruck sein.
- **Min 30–60: Relikt fühlt sich WOW an?** ⚠️ Tobi hat Shader definiert (WOW-Potential da), aber: Wann kriegt Spieler das erste Mal echten Kontakt mit Relikt-Aktivierung? Fragment ist inert, dann... was? Das ist eine Nami/Darius-Frage (in Kap 2/3).

**Blockierend für v2:** Kap 2 (Kernmechaniken) und Kap 3 (Erzählkonzept) müssen vor dem nächsten Alpha-Test existieren. Ohne die kann ich nicht "erste 30 Min" fully evaluieren.

---

## Briefing-Konsistenz

**Checklist gegen Briefing (`simulation-2/briefing.md`):**

| Punkt | Briefing | GDD-Status | Konsistenz |
|---|---|---|---|
| **Genre:** "Medieval Cyberpunk" | ✅ Kap 01 (Darius): "Medieval Cyberpunk: frühes Spätmittelalter + High-Tech-Materialien" | ✅ |
| **Keine Steampunk** | ✅ Kap 06 (Tobi): "Kein Zahnrad. Keine Dampfmaschine." | ✅ |
| **Keine High Fantasy** | ✅ Kap 01 (Darius): "Keine Magie → Alchemie, Schattenfieber-Fähigkeiten" | ✅ |
| **Schattenfieber = einziges Übernatürlich** | ✅ WBB 01 (Emre): "Das Schattenfieber ist das einzige Übernatürliche" | ✅ |
| **Spieler = Fremder, namenlos** | ✅ Kap 04 (Nami): "Der Fremde ist eine Frage in Menschengestalt" | ✅ |
| **Drei Fraktionen, keine ist gut/böse** | ✅ Kap 01 (Darius) + WBB 01 (Emre): alle drei mit Legitimitäts-Erzählungen | ✅ |
| **Materialsprache als Macht** | ✅ Kap 01 (Darius): Material-Hierarchie nach Schicht | ✅ |
| **Immersive Sim** | ✅ Kap 01 (Darius, Säule I) | ✅ |
| **Real-Time Action, Melee** | ✅ Kap 01 (Darius) + Kap 06 (Tobi): Combat-Architektur | ✅ |
| **Premium, keine Mikrotransaktionen** | ✅ Kap 01 (Darius) + Kap 06 (Tobi) | ✅ |
| **DLCs groß, kein Content-Drip** | ✅ Kap 06 (Tobi): "DLC-Content erweitert auf stabiler Basis" | ✅ |
| **Spieler darf Fragment ablehnen** | ✅ Briefing + Memory + Nami erwähnt "Ablehnung-Option heute als halbe Seite in Kap 5" | ⚠️ **Nicht in Kap 04.** Muss in Kap 5 (Erzählkonzept, noch nicht geschrieben) kommen |
| **Schwellenanker ist Relikt-Name** | ⚠️ Briefing sagt das, aber Kapitel konsistent nicht | ❌ **SIEHE TERMINOLOGIE-PROBLEM OBEN** |

**Fazit:** 11/12 Punkte konsistent. 1 offene Schuld (Fragment-Ablehnung in Kap 5), 1 Namenspolitik-Problem (Schwellenanker vs. Relikt).

---

## Zusammenfassung: Was gut, was schlecht

### ✅ Was funktioniert hervorragend

1. **Mythologische Struktur** (Emre, WBB 01) — die drei Schöpfungsmythen sind intelligent und asymmetrisch
2. **NPC-Stimmen** (Nami, Kap 04) — jede Figur hat eine Voice, die man sofort erkennt
3. **Fraktions-Design** (Darius + Emre) — alle drei Mächte sind plausibel und haben Anreize
4. **Material-Sprache** (Darius, Kap 01) — Status wird visuell lesbar, nicht abstrakt
5. **Technische Architektur** (Tobi, Kap 06) — Shader-Struktur für Relikt und Schattenfieber ist sauber und performant
6. **Gameplay-Philosophie** (Darius, vier Säulen) — das ist eine Orientierung, keine Checkliste
7. **Verwobene Kausalität** (alle) — Schwelle → Schattenfieber → Fraktionen → Quest → Spieler-Wahl ist eine logische Kette

### ⚠️ Was muss bis v2 geklärt sein (blockierend)

1. **Relikt-Namenspolitik** — "Die Wurzel" vs. "Das Relikt" vs. "Der Schwellenanker" (ENTSCHEIDUNG bis 14:00)
2. **Emres Widerspruchs-Log W-001, W-004, W-006** — Substanz-Definition, Tiervolk-Herkunft, konkrete Zeitlinie
3. **Autor-Namen in sichtbaren Texten** — muss bis PDF-Export weg sein

### ⚠️ Was braucht Ausarbeitung bis Beta

1. **Florenferenz für Vera** — konkrete Schwellenflora/Fauna-Beispiele
2. **Genealogie-Diagramm** — Fraktions-Hierarchie mit 3–5 NPCs pro Fraktion
3. **Detailkarte** — Vera's Level-Design mit Constraint-Points für Tobi
4. **Dialektsysteme** — Sprechen Unterschicht-NPCs anders?
5. **Spieler-Ethik-Dilemmata** — mehr als "Relikt ablehnen"

---

## Abschließende Einschätzung (Spieler-Perspektive)

Wenn ich als 47k-Follower-Streamer diese Alpha-Version spielen würde (ohne Kap 2 und 3 voraus):

**Minuten 0–15:**
- Material-Klasse erkenne ich sofort ✅
- Hieronymus-Scene: emotional, nicht übertrieben, gut ✅
- Relikt-Fragment sieht aus wie... was ist das? ⚠️ (Tobi hat den Shader, aber ich muss ihn sehen)
- Drei Boten: aha, politische Wahl — gut, aber ich weiß nicht, was ich tue

**Minuten 15–30:**
- Erste Quest-Gebiet: Schichtung sichtbar? JA (Materialsprache trägt) ✅
- NPCs: Brenn, Scherer, Kast haben unterschiedliche Stimmen ✅
- Fraktions-Zugehörigkeit hat Konsequenzen? *Noch nicht sichtbar* (hängt von Kap 2 ab)

**Retention-Prognose (ohne Kap 2/3):** 70% nach 60 Min. Das ist das Ziel. Reachbar. Aber der "WOW"-Moment muss in Kap 2 oder 3 sein (Relikt-Aktivierung oder erste Combat-Sequenz mit Skill-Feedback).

**Chat-Prognose:** Leute sind neugierig, nicht begeistert. Sagen: "This looks dense. Let's see where it goes." Das ist besser als "yo this is broken" oder "zzz", aber nicht das "oh damn" der ersten 8 Min, das Retention hält.

**Für v1 → v2:** Macht. Richtung ist richtig. Braucht nur Feinschliff + Kap 2/3 um zu wissen, ob "WOW" kommt.

---

## Action Items für Darius, Emre, Nami, Tobi

**Vor 14:00 Uhr heute (für Darius-Sync):**
- [ ] **Darius + Emre + Nami:** Relikt-Namenspolitik entscheiden (Wurzel vs. Relikt vs. Schwellenanker)
- [ ] **Emre + Nami:** W-001 (Substanz-Definition), W-004 (Tiervolk), W-006 (konkrete Zeitlinie) klären

**Bis morgen früh:**
- [ ] **Emre:** 5+ Schwellenflora-Typen mit Beschreibungen (für Vera)
- [ ] **Darius/Nami:** Kap 2 (Kernmechaniken) Entwurf — vorzeigen für QA

**Bis Ende dieser Woche (vor PDF-Export für Alpha):**
- [ ] **Darius/Nami/Tobi:** Alle Autor-Namen und Prozess-Kommentare aus sichtbaren Texten entfernen
- [ ] **Vera:** Detailkarte mit Constraint-Points
- [ ] **Nami:** Genealogie-Diagramm (Fraktions-Hierarchie)

---

**QA-Report Ende.** Bereit für Diskussion.

<!-- Leo: Dieser Report ist eine ehrliche Bewertung ohne "aber es ist gut genug"-Puffer. Der Grund: Alpha-Release ist in 6 Wochen. Jede Lücke wird größer, je näher wir kommen. Besser jetzt klar machen, was offen ist, als auf dem Stream "äh, daran haben wir nicht gedacht." -->

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

# GDD Kapitel 01 — Spielübersicht & Design-Säulen

<!-- Darius: v2 — Aktualisierungen: "Schwarzrand" als offizieller Stadtname, "Schwellenanker" als Relikt-Bezeichnung (CD bestätigt, Tag 3 Briefing). Alle Statuszeilen und Autorenvermerke in HTML-Kommentare verschoben. Offene Punkte in Kap. 11 als beantwortet markiert. -->

<!-- Status: v2 | Tag 3, Mittwoch | Autor: Darius Engel -->

---

## 1. Projekttitel & Format

**Serientitel:** RELICS
**Erste Iteration:** RELICS: Der Schwellenanker
**Format:** Single-Player Computer-Rollenspiel
**Perspektive:** Third-Person / First-Person, nahtlos umschaltbar
**Monetarisierung:** Premium, einmaliger Kaufpreis — keine Mikrotransaktionen, keine kleinen Add-ons. DLCs nach Full Release, ausschließlich groß.

---

## 2. High Concept Statement

RELICS fragt: *Wem gehört diese Welt — und was bist du bereit zu tun, um darin zu überleben?*

Du bist ein Fremder. Du weißt nicht, wer du warst. Du weißt nicht, warum du hier bist. Aber die Stadt vor dir funktioniert ohne dich — sie hat Regeln, Mächte, Hierarchien, die sich über Jahrhunderte eingeschliffen haben. Drei Fraktionen teilen die Welt unter sich auf: die Krone mit ihrem Militär und ihren leeren Kassen, die Gilden mit ihren Monopolen und ihrem Geld, der Orden mit seinem Wissen und seiner Inquisition. Keine ist gut. Keine ist böse. Alle sind konsequent.

Und dann gibt es das Schattenfieber. Eine Seuche, die den Körper verändert. Jede Fraktion hat eine andere Erklärung — alle drei liegen falsch, aber jede liegt anders falsch. Die Wahrheit liegt tiefer. Unter der Stadt, in der Stille unter dem Stein, wartet etwas, das die Grenze zwischen den Ebenen des Seins zusammenhält. Es heißt der **Schwellenanker**. Es schwächt sich ab. Und das Fieber breitet sich aus.

Du wirst hineingezogen, ob du willst oder nicht. Was du daraus machst — das ist das Spiel.

---

## 3. Spieler-Fantasie-Statement

**"Ich betrete als Fremder eine aufregende Sandbox."** *(Briefing, unveränderlich)*

Ausformuliert:

Der Spieler soll sich fühlen wie jemand, der eine fremde Stadt zum ersten Mal betritt und merkt, dass sie *funktioniert* — Händler handeln, Wachen patrouillieren, Gildenmeister verhandeln, Ordensboten eilen durch Gassen. Er ist das Störelement. Die Welt hat ohne ihn existiert. Sie lässt ihn rein — zögernd, abwartend, mit Hintergedanken.

Das Versprechen: *Ich kann hier meine eigene Geschichte schreiben. Nicht eine Geschichte, die mir das Spiel aufzwingt. Meine.*

Drei konkrete Fantasien, die dieses Statement trägt:

1. **Agentschaft:** Ich löse jedes Problem auf meine Weise. Schleiche ich durch den Gilden-Checkpoint, bestehe ich ihn oder erkaufe ich mir Durchgang?
2. **Aufstieg:** Ich fange mit Eisengerät an und arbeite mich in eine Welt vor, in der Titan-Legierungen und Tiegelstahl die Sprache der Macht sind. Mein Körper ist mein Fortschrittsanzeiger.
3. **Konsequenz:** Meine Entscheidungen formen die Welt. Wenn ich für die Gilden arbeite, verschließt mir der Orden Türen. Das ist kein Bug. Das ist der Vertrag.

---

## 4. Game Feel

**RELICS-Game-Feel in einem Satz:**
*Ich stehe am Rand einer lebendigen, gefährlichen Welt und spüre, dass meine nächste Entscheidung etwas verändert.*

**Textur dieser Empfindung:**
- **Schwere.** Kämpfe sind nicht flüssig und elegant — sie kosten etwas. Ein Schwerthieb fordert Kraft, eine Parade fordert Timing. Der Körper des Spielers ist spürbar.
- **Reibung.** Die Stadt gibt sich nicht preis. Gilden-Tore sind gesperrt. Ordenswächter beobachten. Die Krone erwartet. Diese Reibung ist kein Fehler — sie ist das Medium, durch das sich Fortschritt anfühlt.
- **Staunen + Bedrohung.** Die Biolumineszenz in den Kanälen leuchtet schön. Sie leuchtet, weil dort das Fieber am stärksten ist. Die Welt ist attraktiv und gefährlich zur selben Zeit.
- **Dichte.** Jeder NPC hat eine Funktion, einen Tagesablauf, ein Gesicht. Niemand steht als Dekoration herum. Das fühlt sich nicht wie ein Videospiel an — es fühlt sich wie eine Welt an.

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

**Referenz:** Warren Spector, Deus Ex GDD v5.3e (Ion Storm, 1997): "The world simulation allows players to solve problems in a variety of ways."

---

### Säule II — Fraktionspolitik als Kernspannung

**Statement:** Kein Gut gegen Böse. Drei konkurrierende Mächte, jede mit innerer Logik, jede mit konkreten Ressourcen, die sie kontrollieren.

**Was das bedeutet:**

| Fraktion | Ressource | Gameplay-Zugang | Fantasie |
|---|---|---|---|
| **Die Krone** | Territorium, Militärpassagen, Rechtsstatus | Schutz, Bewegungsfreiheit, Ehrentitel | Legitimität erkaufen |
| **Die Gilden** | Materialien, Handwerksrezepturen, Schwarzmarkt | Crafting-Tiefe, Upgrade-Pfade, Händler-Netzwerke | Macht durch Handwerk |
| **Der Orden** | Wissen, Fertigkeitsbücher, Bildungsmonopol | Skill-Upgrades, Lore-Zugang, Heilkunde | Verständnis als Waffe |

Fraktionsruf ist keine abstrakte Zahl — er ist der Schlüssel zu konkreten Spielsystemen. Wer bei den Gilden gut steht, kommt an Damaszener-Stahl. Wer beim Orden arbeitet, versteht das Schattenfieber tiefer.

Kein moralischer Zeigefinger. Jede Fraktion hat einen sympathischen Einstiegspunkt, einen Moment der Kompliziertheit, und einen Point of No Return.

**Spieler-Fantasie:** *"Ich wähle nicht die gute Fraktion. Ich wähle meine Fraktion."*

**Referenz:** Vampire: The Masquerade — Bloodlines (Troika Games, 2004).

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
- Das Lymph-Subsystem koppelt direkt an die Schattenfieber-Progression (drei Stadien: Flüstern / Wandlung / Entgrenzung — nach biologischer Lore)
- Wer das Fieber unterdrückt (Krone-Weg), bleibt "sauber", verliert aber Zugang zu bestimmten Fähigkeiten
- Wer das Fieber nutzt (Gilden-Weg: Destillierung als Produkt), gewinnt Kraft, bezahlt mit Körper
- Wer das Fieber versteht (Orden-Weg: Deutungshoheit), bekommt tieferen Lore-Zugang, aber der Orden will etwas dafür

Das ist kein Magiesystem mit anderem Namen. Die Kosten sind real. Ein Spieler mit fortgeschrittenem Fieber wird *gezeichnet*.

**Spieler-Fantasie:** *"Mein Körper ist mein Fortschrittsanzeiger. Ich sehe, was ich trainiert habe — und was es mich gekostet hat."*

**Referenz:** Warren Spector, Deus Ex GDD v5.3e: Skill-Granularität über vier Qualitätsstufen statt 1-100-Skala.

---

### Säule IV — Dichte vor Breite

**Statement:** Handgefertigte Welt, handgefertigte Begegnungen. Lieber zwanzig NPCs mit Persönlichkeit als zweihundert mit Füll-Dialog.

**Was das bedeutet:**
- **Schwarzrand** ist der Kern. Keine riesige Weltkarte mit leeren Gebieten dazwischen. Eine Stadt, vertikal geschichtet (Obere Ränder / Mittelwand / Schlund), dicht belebt.
- Jede Zone hat eigene Materialsprache, eigene Architektur, eigenen NPC-Typ. Der Spieler liest Schicht und Status sofort ab — ohne HUD-Icon.
- NPCs haben Tagesabläufe. Wachen lösen ab. Märkte öffnen und schließen. Ein Schmied, der um 14:00 in der Hammergasse arbeitet, ist um 20:00 in der Kneipe.
- Seitenquests entstehen aus der Welt, nicht aus Ausrufezeichen über NPC-Köpfen.
- Kein Loot-Bloat. Materialien sind knapp. Ein Stück Damaszener-Stahl ist ein Ereignis.

**Der Gothic-Kontrast zu Skyrim:**
Skyrim hat 300 Orte, an denen man Drachen töten kann. Gothic 2 hat Khorinis — und Khorinis *lebt*. Jeder Bewohner hat einen Namen, eine Meinung, einen Tagesablauf. Diese Dichte erzeugt die Illusion, in einer echten Welt zu sein. Das ist RELICS' Versprechen.

**Spieler-Fantasie:** *"Diese Welt existierte, bevor ich ankam. Sie wird nach mir weiterexistieren."*

**Referenz:** Gothic 2 (Piranha Bytes, 2002); Warren Spector, Deus Ex GDD v5.3e: "No weird 'game spaces'."

---

## 7. Tonalität

**Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.**

Das ist kein Grimdark um des Grimdark willen. Die Welt ist dunkel, weil die Verhältnisse dunkel sind. Die Krone hat leere Kassen und bröckelnde Legitimität. Die Gilden halten Monopole mit Gewalt. Der Orden hat Bildung als Kontrollmittel. Das ist keine Fantasy — das ist Struktur.

Das Schattenfieber ist das einzige Übernatürliche. Es wird ernst genommen, nie trivialisiert.

**Visuelle Signatur der Tonalität:**
- Oberschicht: All-Black, All-White, Monochrom — ein einzelner Neon-Akzent (leuchtendes Indigo, Blutrot, Giftgrün)
- Unterschicht: Grau, Braun, schmutzig — und gelegentlich ein gestohlenes Stück Farbe
- Biolumineszenz in den Kanälen: schön und bedrohlich
- Kein Zahnrad. Keine Dampfmaschine. Keine Hexagone.

---

## 8. Zielgruppe

RELICS spricht vier überlappende Spielertypen an:

1. **Immersion-First Players** — wollen sich in eine Welt verlaufen, nicht geführt werden (Kingdom Come: Deliverance, Disco Elysium, Outer Wilds)
2. **Faction Players** — "Ich wähle nicht die gute Fraktion" (VtM: Bloodlines, Fallout: New Vegas)
3. **Crafting/Progression Freaks** — wollen sichtbare Materialsprache, echte Upgrade-Tiefe, keine Loot-Inflation (Dark Souls, Stardew Valley)
4. **Medieval Aesthetics Obsessed** — reale mittelalterliche Logik + Biotech als Geheimnis, kein Kitsch (Kingdom Come: Deliverance, Mount & Blade)

**Kritisches Risiko:** Die erste Stunde ist kein Tutorial. Sie ist ein Angebot. Wenn der Spieler in Minute fünfzehn nicht versteht, was dieser Ort *ist*, verlieren wir ihn. Die erste Stunde muss stehen, wenn wir in die Streamer-Alpha gehen.

---

## 9. Abgrenzung

| Was RELICS IST | Was RELICS NICHT IST |
|---|---|
| Handgefertigte, dichte Welt | Weitläufige, leere Open World |
| Körperlicher Fortschritt sichtbar | Abstraktes Level-up-System |
| Drei Fraktionen ohne Moralkeulen | Gut-gegen-Böse-Struktur |
| Schattenfieber als biologische Wahrheit | Magiesystem mit Fantasy-Label |
| Spieler als namenloser Fremder | Spieler als vordefinierten Charakter |
| Medieval Cyberpunk: Material als Macht | Steampunk, High Fantasy, Science-Fantasy |
| Immersive Sim: mehrere Lösungswege | Schienenspiel mit Illusion der Wahl |

---

## 10. Geklärte Design-Fragen

| # | Frage | Antwort |
|---|---|---|
| 1 | **Schauplatz:** Eine Stadt oder mehrere? | EINE vertikale Stadt: **Schwarzrand**. Mitteleuropäisch, auf Felssporn gebaut, vertikal geschichtet in drei Zonen (Obere Ränder / Mittelwand / Schlund). |
| 2 | **Schattenfieber-Scope:** Wie tief geht die Integration? | Hauptquest-antreibend UND dritte Progressionsachse (Lymph-Subsystem). Drei biologische Stadien. Drei Fraktions-Antworten = drei Gameplay-Pfade. |
| 3 | **Tiervolk:** Spielbar oder NPC? | NPC — Händler und Informationsbroker. Nicht spielbar. Leicht alien in Ästhetik, nicht tribal. Eigene Händler-Netzwerke parallel zu den Gilden. |
| 4 | **Release-Modell:** Wie liefern wir? | Streamer-Alpha (erste Stunde muss stehen) → Beta (max. 6–12 Monate) → Full Release → große DLCs. |
| 5 | **Relikt-Name:** Wie heißt das zentrale Artefakt? | **Der Schwellenanker** — In-World-Begriff, CD-bestätigt. Das Fragment beim Spieler: ein Stück des Schwellenankers. |
| 6 | **Ablehn-Option:** Kann der Spieler das Fragment ablehnen? | Ja — CD-bestätigt. Der Spieler darf das Fragment von Hieronymus Vael ablehnen. Konsequenzen in Kapitel 3 (Erzählkonzept) ausgearbeitet. |

---

<!-- Darius: Kap. 11 (offene Punkte aus v1) vollständig aufgelöst und in Kap. 10 als geklärte Fragen überführt. Interne Abhängigkeiten zu Kap. 2 und Kap. 3 sind jetzt dort direkt eingearbeitet. -->

*Versionsstatus: v2 — Alle Design-Säulen ausgearbeitet, High Concept gesetzt, Game Feel definiert. Stadtname Schwarzrand und Relikt-Name Schwellenanker CD-bestätigt eingetragen. Ablehn-Option integriert.*

\clearpage

# GDD Kapitel 02 — Kernmechaniken

<!-- Status: v1 | Tag 3, Mittwoch | Autor: Darius Engel -->
<!-- Darius: Dieses Kapitel definiert alle Kernsysteme von RELICS: Der Schwellenanker. Jedes System ist aus den vier Design-Säulen abgeleitet. Spieler-Fantasie-Statement steht über jeder Mechanik-Beschreibung — ist das nicht da, ist das Feature raus. -->

---

## Überblick

Dieses Kapitel beschreibt die fünf Kernsysteme von RELICS: Der Schwellenanker. Jedes System ist direkt aus den Design-Säulen von Kapitel 1 abgeleitet und muss gegen mindestens zwei Säulen bestehen:

1. **Kampfsystem** — Säule I (Immersive Sim) + Säule III (Körperlicher Fortschritt)
2. **Nervensystem-Leveling** — Säule III (Körperlicher Fortschritt) + Säule I (Immersive Sim)
3. **Crafting & Materialsystem** — Säule II (Fraktionspolitik) + Säule IV (Dichte vor Breite)
4. **Fraktionsruf-System** — Säule II (Fraktionspolitik) + Säule I (Immersive Sim)
5. **Schattenfieber-Progression** — Säule III (Körperlicher Fortschritt) + Säule II (Fraktionspolitik)

---

## 2.1 Kampfsystem

### Spieler-Fantasie

*"Jeder Kampf kostet mich etwas. Wenn ich gewinne, habe ich es mir verdient."*

### Designprinzipien

Das Kampfsystem von RELICS ist kein Showroom für Combo-Systeme. Es ist eine mechanische Umsetzung von Schwere und Konsequenz — den zwei Kerneigenschaften des Game-Feel-Statements aus Kapitel 1. Kämpfe sollen sich anstrengend anfühlen, nicht befriedigend-flüssig. Der Spieler soll nach einem schweren Kampf *erschöpft* sein, nicht triumphierend-leicht.

**Referenz:** Gothic 2 (Piranha Bytes, 2002) — Kampf als Risiko, nicht als Komfort. Dark Souls (FromSoftware, 2011) — Positionierung, Gewicht, Kosten.

### Kernmechaniken des Kampfes

**Ausdauersystem (Stamina)**

Die zentrale Ressource im Kampf ist nicht Gesundheit, sondern Ausdauer. Jede Aktion kostet Ausdauer:
- Leichter Angriff: geringe Kosten
- Schwerer Angriff: hohe Kosten
- Parade / aktive Abwehr: moderate Kosten
- Ausweichen / Rollen: moderate Kosten
- Sprinten, Springen: kontinuierliche Kosten

Ist die Ausdauer erschöpft, wird der Spieler anfällig: Angriffe treffen schwerer, Paraden schlagen durch, der Spieler kann sich nicht mehr aktiv bewegen. Ausdauer regeneriert mit kurzer Verzögerung nach der letzten Aktion — ein aktiver Kampf ohne Pausen lässt den Spieler langsam zusammenbrechen.

Ausdauerkapazität und Regenerationsrate sind direkt mit dem Cardio-Subsystem des Nervensystem-Levelings verknüpft (→ Abschnitt 2.2).

**Trefferzonen & Positionierung**

RELICS kennt keine abstrakten Trefferwahrscheinlichkeiten. Positionierung ist eine direkte taktische Variable:
- Angriffe von hinten ignorieren Rüstungsschutz der Vorderseite
- Angriffe von der Seite umgehen aktive Paraden
- Flankieren ist das stärkste taktische Mittel — und das, was Gegner aktiv versuchen

Der Spieler kämpft in der Regel alleine gegen Gruppen. Positionierung an Engpässen (Türrahmen, Treppenstufen, enge Gassen) ist keine Spielhilfe, sondern überlebensnotwendig.

**Waffenklassen und ihre Eigenlogik**

| Waffenklasse | Stärke | Schwäche | Besondere Eigenschaft |
|---|---|---|---|
| **Einhandschwert** | Ausgewogen, schnell | Mittlere Reichweite, mittlerer Schaden | Kann mit Schild kombiniert werden |
| **Zweihandschwert** | Hoher Schaden, gute Reichweite | Hohe Ausdauerkosten, langsamer | Kann Schilde durchschlagen (Rüstungsdurchdringung) |
| **Dolch** | Sehr schnell, niedrige Ausdauerkosten | Geringer Schaden, kurze Reichweite | Finisher-Angriffe möglich (Schleich-Umgebung) |
| **Axt** | Hoher Schaden gegen Rüstung | Langsam, keine Parade-Option | Ignoriert anteilig Rüstungsschutz |
| **Streitkolben** | Effektiv gegen Plattenrüstung | Langsam, hohe Ausdauerkosten | Betäubungseffekt bei vollem Treffer |
| **Bogen** | Distanzangriff, leise | Nachladezeit, unbrauchbar in Nahkampf | Schwachstellen-Targeting möglich |
| **Armbrust** | Hohe Durchschlagskraft | Sehr lange Nachladezeit | Kann schwere Rüstung durchdringen |

Keine Waffe ist "die beste". Die Auswahl ist eine taktische Entscheidung, die vom Gegnertyp, der Umgebung und dem eigenen Muskel-Subsystem-Stand abhängt.

**Alchemie im Kampf**

Alchemika sind keine Magie-Substitute. Sie sind Hilfsmittel mit Nebenwirkungen:
- **Stärkungstränke:** Temporäre Ausdauer-Regeneration, Schadensbonus — mit Nachkater (reduzierte Werte nach Wirkende)
- **Heilmittel:** Langsame, anhaltende Heilung — nicht sofort. In einem aktiven Kampf nutzen sie wenig, danach sehr viel.
- **Schwellensubstrat-Extrakte:** Hochriskante Kampfmittel, die temporäre Stärke durch Schattenfieber-Exposition erzeugen. Jede Einnahme erhöht den Fieber-Wert im Lymph-Subsystem.
- **Rauch- und Blendmittel:** Taktische Werkzeuge für Rückzug und Neupositionierung

Alchemika werden im Crafting-System hergestellt oder über Gilden und Händler erworben (→ Abschnitt 2.3).

**Kampf vs. Ausweichen**

Das System belohnt den Spieler nicht dafür, möglichst viele Kämpfe zu gewinnen. Es belohnt ihn dafür, dass er in der Welt navigiert. Viele Begegnungen haben Umgehungswege: Soziale Lösungen (Fraktionsruf-basiert), Stealth-Wege, alternative Routen. Das Kampfsystem ist für die Fälle, in denen das nicht klappt — oder für die Spieler, die es genau so wollen.

---

## 2.2 Nervensystem-Leveling

### Spieler-Fantasie

*"Ich sehe meinen Fortschritt. Ich sehe, was er mich gekostet hat."*

### Das System im Überblick

Das Nervensystem-Leveling ist das Herz von RELICS' Progressionsdesign. Es ersetzt klassische Erfahrungspunkte-Balken und Attribut-Grids vollständig. Der Spieler hat keinen "Level". Er hat drei Subsysteme, die sich durch tatsächliches Tun entwickeln.

**Philosophie:** Ein Schwertkämpfer wird zum Schwertkämpfer, indem er kämpft. Nicht indem er Erfahrungspunkte sammelt und Punkte verteilt. Diese "Skill-by-Use"-Logik stammt direkt aus Gothic 2 — aber RELICS verfeinert sie durch das Deus-Ex-Modell der Qualitätsstufen statt graduellem Zahlenfortschritt.

Das Nervensystem visualisiert sich durch eine halbtransparente Körperansicht, die während des Levelings eingeblendet werden kann: leuchtende Nervenbahnen zeigen aktive Subsysteme, trübe zeigen inaktive, und die Fieber-Infiltration des Lymphsystems ist in Echtzeit sichtbar.

![Nervensystem-Konzept: Schwellenanker-Relikt in Zustand Eins](../concepts/day02-vera/relics/relikt-zustand-eins-aktiviert_seedream-4-5.png)

*Konzeptbild: Biolumineszente Gefäßlinien — dieselbe visuelle Sprache gilt für das Nervensystem-Leveling-Interface. Lymph-Kontamination folgt vergleichbaren Mustern.*

### Die drei Subsysteme

**Cardio — Das Ausdauersystem**

Das Cardio-Subsystem bestimmt alle Ausdauer-bezogenen Parameter: wie lange der Spieler laufen kann, wie schnell er sich erholt, wie viele Kampfaktionen er in Serie ausführen kann, bevor er pausieren muss.

*Trainiert durch:* Ausdauerkämpfe (Kämpfe, die lange dauern), Sprinten, Klettern, Flucht-Sequenzen, Erkundung größerer Strecken ohne Rast.

*Vier Qualitätsstufen:*

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Untrainiert | Erschöpft schnell, langsame Regeneration, eingeschränkte Kampfdauer |
| II | Geübt | Moderate Ausdauer, schnellere Regeneration, kann kurze Sprintphasen nutzen |
| III | Fortgeschritten | Hohe Ausdauer, rapide Regeneration, Ausdauer ist selten ein Engpass |
| IV | Meister | Ausdauer ist kein limitierender Faktor. Kampf-Pausen werden taktisch, nicht notwendig |

*Progression:* Jede Qualitätsstufe erfordert eine bestimmte Anzahl an "Ausdauer-Ereignissen" — Kampfrunden, Sprintmeter, Kletterakte. Das Spiel trackt diese unsichtbar und zeigt nur die aktuelle Qualitätsstufe an. Der Übergang ist spürbar, nicht abrupt: Der Spieler merkt, dass er weiter laufen kann, bevor die Stufe visuell bestätigt wird.

**Muskel — Das Kraftsystem**

Das Muskel-Subsystem bestimmt alle physischen Stärkeparameter: Schadensausgabe im Nahkampf, maximales Tragegewicht, Effizienz schwerer Rüstungen.

*Trainiert durch:* Nahkampfangriffe (jeder Treffer zählt, auch verpasste), schwere Gegenstände tragen und transportieren, physische Arbeit (optionale Tätigkeiten in der Welt: Schmieden helfen, Ladungen schleppen — auch das trainiert).

*Vier Qualitätsstufen:*

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Untrainiert | Minimaler Nahkampfschaden, niedriges Tragegewicht, mittelschwere Rüstungen beschränken Mobilität |
| II | Geübt | Ordentlicher Nahkampfschaden, Rüstung schränkt weniger ein, kann kompetent kämpfen |
| III | Fortgeschritten | Deutlicher Schadensbonus, schwere Rüstungen voll nutzbar, Tragegewicht kein Problem |
| IV | Meister | Spitzenwerte. Schwere Zweihandwaffen werden zu bevorzugten Werkzeugen, maximale Rüstungseffizienz |

*Besonderheit:* Das Muskel-Subsystem interagiert mit dem Crafting-System. Wer auf Stufe III oder IV ist, kann schwere Waffen und Rüstungen überhaupt erst sinnvoll nutzen. Damaszener-Stahl-Ausrüstung auf einem Stufe-I-Spieler ist Verschwendung.

**Lymph — Das Fieber-System**

Das Lymph-Subsystem ist das komplexeste und gefährlichste der drei. Es bildet die biologische Schnittstelle zwischen dem Spielercharakter und der Schwellenrealität.

*Trainiert durch:* Einnahme von Alchemika und Schwellensubstrat-Extrakten, Exposition in Dünnstellen (die tiefen Bereiche von Schwarzrand), Heilrituale des Ordens (die ebenfalls das Lymphsystem verändern, aber auf kontrollierte Weise), Kontakt mit dem Schwellenanker.

*Vier Qualitätsstufen:*

| Stufe | Bezeichnung | Auswirkung |
|---|---|---|
| I | Unangetastet | Baseline. Keine Schattenfieber-Symptome, keine Mutation, aber auch keine Vorteile durch das Lymphsystem |
| II | Exponiert (Flüstern) | Erste Schattenfieber-Symptome. Sensorische Erweiterungen: Farben intensiver, Geräusche mit Nachklang. Gameplay-Vorteil: Wahrnehmen versteckter Schwellen-Objekte. |
| III | Kontaminiert (Wandlung) | Sichtbare physische Veränderungen. Physische Buffs (Stärke, Ausdauer durch Fieber). Kognitive Kosten: Erinnerungen unzuverlässig, gelegentliche Wahrnehmungsstörungen im Gameplay |
| IV | Durchdrungen (Entgrenzung) | Irreversibel. Massiver Power-Spike, aber der Spieler verliert zunehmend die Kontrolle. Nur über bestimmte Orden-Rituale oder Schwellenanker-Interaktion partiell stabilisierbar |

*Kritische Eigenschaft:* Das Lymph-Subsystem kennt keine einfache Progression von I nach IV. Es gibt Kontaminations-Akkumulation, die sich durch Fieberquellen aufbaut, und Reduktions-Mechanismen:
- Krone-Weg: Medizinische Unterdrückung — Lymph-Wert senken, aber kein Aufstieg in Stufe II–IV möglich
- Gilden-Weg: Kontrollierte Nutzung — Lymph-Wert auf einem Plateau halten, Vorteile von Stufe II extrahieren
- Orden-Weg: Destillation und Verstehen — langsamer Aufstieg mit Stabilisierung, tiefer Lore-Zugang, aber der Orden hat Forderungen

*Das Schattenfieber-Risiko:* Wer unkontrolliert in Dünnstellen operiert oder zu viele Extrakte nimmt, riskiert einen unkontrollierten Sprung von Stufe II zu Stufe III oder von III zu IV. Stufe IV ohne stabilisierende Intervention ist faktisch ein langsamer Game-Over-Zustand — der Spieler wird immer schwerer kontrollierbar, bis er die Handlungsfähigkeit verliert.

### Qualitätsstufen-Übergänge

Ein Qualitätsstufenwechsel ist ein Moment im Spiel. Keine Fanfare, keine Leveling-Bildschirme. Die Nervensystem-Ansicht zeigt kurz das aktive Subsystem aufleuchten — eine visuelle Bestätigung, keine Unterbrechung. Der Spieler merkt es an der veränderten Spielperformance, nicht durch eine UI-Meldung.

Der Spieler kann aktiv "investieren": Wer weiß, dass ein schwerer Kampf bevorsteht, kann vorab gezielt das Muskel-Subsystem stimulieren (Kampfübungen mit einem Trainer, Schmiedearbeit). Das ist die optionale Vorbereitung — keine Pflicht, aber ein strategischer Hebel.

---

## 2.3 Crafting & Materialsystem

### Spieler-Fantasie

*"Ein Stück Damaszener-Stahl ist ein Ereignis. Ich weiß, was ich tue, wenn ich es verarbeite."*

### Designprinzipien

Das Crafting-System von RELICS ist keine Item-Fabrik. Es ist ein Ausdruck der Fraktionspolitik und der Materialsprache der Welt. Materialien sind keine Zahlen — sie sind Hierarchien. Wer welches Material verarbeitet, definiert, wo er in der sozialen Ordnung steht.

**Keine Loot-Inflation.** Ein Stück Tiegelstahl ist selten. Damaszener-Stahl ist eine Rarität. Schwellenlegierungen sind die gefährlichste und mächtigste Materialklasse, mit einem echten Preis.

### Materialklassen

RELICS hat fünf Materialklassen. Jede ist mit einer Fraktionszugehörigkeit und einem sozialen Status verknüpft:

| Klasse | Material-Beispiele | Zugang | Sozialer Status |
|---|---|---|---|
| **I — Unterschicht** | Eisen, Zinn, Knochen, ungefärbtes Leinen | Frei verfügbar, Markt und Schwarzmarkt | Gesetzlos, mittellos |
| **II — Handwerker** | Gehärteter Tiegelstahl, Silber, Malachit, gefärbtes Leinen | Gilden-Markt (kein Ruf nötig) | Respektabler Handwerker |
| **III — Meister** | Damaszener-Stahl, Bronzeguss, Bergkristall | Gilden-Zugang (Ruf: Anerkannt) | Gilden-Mitglied, mittlerer Stand |
| **IV — Elite** | Titan-Legierungen, Roségold, Lapislazuli | Gilden-Zugang (Ruf: Vertraut) + Krone-Passierschein | Oberschicht, Gildenmeister |
| **V — Schwellen** | Schwellenlegierungen, Schwellenfäden, Schwellentalg, Schwellenlinsen | Hoher Gildenruf (Ruf: Meister) ODER Schlund-Schwarzmarkt (mit Fieber-Risiko) | Verboten / Begehrt |

**Materialklasse I–II** sind für den gesamten Spielverlauf das Brot-und-Butter-Material. Ein gut gefertigtes Tiegelstahl-Schwert von einem Spieler mit Muskel III übertrifft ein schlecht gehandhabtes Damaszener-Schwert von einem Spieler mit Muskel I. Das System belohnt Können, nicht nur Material.

**Materialklasse V (Schwellen-Materialien)** sind das Endgame-Crafting. Zwei Zugangswege:
1. Gilden-Weg: Langer Ruf-Aufbau, sicher, legal, teuer
2. Schwarzmarkt-Weg: Sofort verfügbar, illegal, und jedes Stück Schwellenmaterial, das nicht durch Gildenverarbeitung gesichert ist, trägt Schattenfieber-Exposition — jede Verarbeitung erhöht den Lymph-Wert

### Handwerk-Mechanik

Crafting in RELICS ist aktiv, nicht passiv. Der Spieler sitzt nicht in einem Menü — er steht an einer Werkbank (oder einem Schmiedefeuer) und führt eine vereinfachte Handwerks-Sequenz durch.

**Werkzeug-Erfordernisse:** Verschiedene Materialien brauchen verschiedene Werkzeugqualitäten. Eisen lässt sich mit einer einfachen Feldschmiede verarbeiten. Damaszener-Stahl braucht eine Meister-Schmiede — die in der Regel Gilden-Territorium ist. Der Spieler muss also entweder Zugang zu Gilden-Infrastruktur erkaufen oder seine eigene Werkbank schrittweise ausbauen.

**Rezeptur-System:** Rezepturen sind keine automatischen Freischaltungen. Sie sind Wissen — Wissensgegenstände in der Welt:
- Öffentliches Wissen (Rezepturen für Klasse I–II): In der Welt verfügbar, NPCs zeigen sie, Bücher enthalten sie
- Gilden-Wissen (Rezepturen für Klasse III–IV): Nur durch Gilden-Zugehörigkeit oder Entwendung zugänglich
- Geheimes Wissen (Rezepturen für Klasse V): Liegt in Gilden-Archiven, Orden-Archiven, oder bei bestimmten NPCs mit eigenem Preis

**Qualitätsstufen beim Crafting:** Ein Produkt kann in drei Qualitätsvarianten erzeugt werden — Grundlegend / Ordentlich / Meisterwerk. Die Variante hängt ab von: Materialqualität, Werkzeugqualität, und einer kleinen Skill-Komponente (die sich mit Wiederholung verbessert — Muskel-Subsystem-Synergy). Meisterwerke sind selten, aber real, und bei bestimmten NPCs hochbegehrt (Trade-Commodity).

### Rüstungsdesign als sozialer Ausdruck

Die Rüstung des Spielers ist das visuelle Statusstatement. Das System erkennt das und macht es spielmechanisch relevant:

- **Rüstungsklasse** (leicht / mittel / schwer) beeinflusst Ausdauerkosten und Beweglichkeit
- **Material** definiert Schutzwerte und NPC-Reaktionen (ein Spieler in Tiegelstahl wird in Oberschicht-Bereichen anders angesprochen als einer in Eisen)
- **Ausrüstungsmix:** Der Spieler kann jedes Körperteil unabhängig ausrüsten. Eine Kombination von schwerer Schulterpartie mit leichten Beinen ist möglich und sinnvoll.
- **Verfall und Reparatur:** Rüstungen und Waffen nehmen Schaden. Reparatur ist eine Alltagshandlung. Das verhindert, dass der Spieler "set and forget" spielt — er muss aktiv mit seinem Equipment interagieren.

---

## 2.4 Fraktionsruf-System

### Spieler-Fantasie

*"Ich habe mir diese Tür verdient. Oder ich habe sie mir verbaut."*

### Designprinzipien

Das Fraktionsruf-System ist kein Gut-/Böse-Barometer. Es ist eine Buchführung von Handlungen und ihren Konsequenzen. Jede Fraktion bewertet den Spieler nach eigener Logik — und die Logiken widersprechen sich.

Das System funktioniert nach dem Prinzip der kommunizierenden Röhren: Was bei der Krone gewinnt, verliert in der Regel bei den Gilden oder beim Orden. Ausnahmen existieren (neutrale Handlungen), aber echte Maximierung bei allen drei gleichzeitig ist nicht möglich.

### Ruf-Stufen

Jede Fraktion kennt fünf Ruf-Stufen:

| Stufe | Bezeichnung | Zugang | Hinweistext |
|---|---|---|---|
| I | **Unbekannt** | Basiszugang zu öffentlichen Bereichen der Fraktion | "Sie sind neu hier." |
| II | **Bekannt** | Einfache Aufgaben verfügbar, Händler gewähren Basispreise, erste innere Tore offen | "Man hat von Ihnen gehört." |
| III | **Anerkannt** | Mittlere Materialien zugänglich, wichtigere NPCs sprechen direkt, Zugang zu Fraktions-Infrastruktur (Schlafplatz, Werkstätte) | "Sie haben sich als nützlich erwiesen." |
| IV | **Vertraut** | Elite-Materialien verfügbar, Insider-Informationen, Fraktions-Missionen auf hohem Niveau, spezifische Ausrüstung als Geschenk | "Sie sind einer von uns." |
| V | **Meister** | Vollzugang. Schwellen-Materialien (Gilden), Kronpassagen (Krone), geheime Orden-Archive, Entscheidungen beeinflussen Fraktionspolitik | "Ich vertraue Ihnen mein Leben an." |

**Ruf-Verlust:** Handlungen gegen eine Fraktion senken den Ruf. Ruf kann nicht "doppelt negativ" werden — die Mindststufe ist "Feindselig":

| Sonderstufe | Bezeichnung | Konsequenz |
|---|---|---|
| 0 | **Feindselig** | Tore geschlossen. NPCs greifen an oder fliehen. Keine Handelsinteraktion möglich. Nur über Quest-Lösung (spezifisch für jede Fraktion) auflösbar. |

### Ruf-Quellen

Ruf wird erzeugt durch:
- **Quests:** Hauptquelle. Direkte Fraktionsquests geben klaren Ruf-Gain. Offene Quests von Fraktions-NPCs geben Ruf bei der entsprechenden Fraktion.
- **Handlungen in der Welt:** Wächter der Krone angreifen = Krone-Ruf verloren, unabhängig davon ob die Wachen "böse" waren. Gilden-Eigentum stehlen = Gilden-Ruf verloren. Das System beobachtet still.
- **Dialoge und Entscheidungen:** Bestimmte Gespräche haben Ruf-Konsequenzen, die nicht explizit angezeigt werden. Der Spieler spürt sie an veränderten NPC-Reaktionen.
- **Handels-Reputation:** Wer konsequent bei einer Fraktion kauft, gewinnt langfristig Ruf (klein, aber akkumulierend).

### Konflikt-Mechanik: Wenn Fraktionen kollidieren

Ab einem bestimmten Ruf-Niveau in zwei konkurrierenden Fraktionen verlangen beide, dass der Spieler "Farbe bekennt." Das ist kein Quest — das ist eine stille Kulminierung. Ein Gildenmeister sagt dem Spieler: "Ich habe gehört, Sie arbeiten auch für den Orden. Das ist eine Frage, die ich nicht nochmals stellen will." Das Spiel erzwingt keine Entscheidung — aber es macht deutlich, dass die Situation sich nicht halten lässt.

**Point of No Return:** Jede Fraktion hat einen quest-spezifischen Punkt, an dem der Spieler sich endgültig entscheiden muss. Diese Punkte kommen nicht gleichzeitig und werden dem Spieler nicht explizit als "Point of No Return" angezeigt. Er merkt erst rückwirkend, wann er die Entscheidung getroffen hat.

### Gilden-Monopolstruktur und Crafting-Zugang

Das Fraktionsruf-System bei den Gilden ist speziell: Die Gilden sind kein monolithischer Block. Es gibt sieben große Gilden (Schmiede, Glasmacher, Weber, Gerber, Goldschmiede, Kerzenzieher, Pergamenter), und der Ruf bei der Gilden-Fraktion insgesamt beeinflusst den Basisrand. Darüber hinaus gibt es Einzel-Ruf bei spezifischen Gilden:

- **Schmiede-Ruf:** Zugang zu Waffen und Rüstungen der Klasse III–IV
- **Glasmacher-Ruf:** Zugang zu Optik-Instrumenten, Schwellenlinsen, alchemistischen Phiolen
- **Gerber-Ruf:** Zugang zu Kanälen und dem Schlund — physischer Zugang, nicht nur Handel
- **Weber-Ruf:** Schwellenfäden und Elite-Textilien

Wer nur Gilden-Gesamtruf sammelt, ohne einzelne Gilden zu pflegen, bekommt generischen Zugang. Wer gezielt eine Gilde hofiert, bekommt spezifische Tiefe.

---

## 2.5 Schattenfieber-Progression

### Spieler-Fantasie

*"Ich sehe, was das Fieber aus mir macht. Ich entscheide, wie weit ich gehe."*

### Designprinzipien

Das Schattenfieber ist keine Krankheit, die man heilt. Es ist ein Zustand, den man navigiert. Drei Fraktionen, drei Strategien. Keine davon ist optimal — alle haben Kosten und Vorteile.

Das Fieber ist direkt an das Lymph-Subsystem gekoppelt (→ Abschnitt 2.2). Die Stadien des Lymph-Subsystems entsprechen den Schattenfieber-Stufen. Dieser Abschnitt beschreibt die Gameplay-Konsequenzen und die Fraktions-Antworten im Detail.

![Schwellenanker: Zustand Null — ruhend](../concepts/day02-vera/relics/relikt-zustand-null-ruhend_seedream-4-5.png)

*Konzeptbild: Der Schwellenanker in Ruhezustand. Die visuelle Sprache des Ruhezustands spiegelt die Baseline des Lymph-Subsystems (Stufe I: Unangetastet).*

### Die drei Fieber-Stadien im Gameplay

**Stadium I — Flüstern (Lymph-Stufe II: Exponiert)**

Das erste Stadium ist die Einladung. Es gibt nichts zu verlieren, aber etwas zu gewinnen:

*Vorteile:*
- Erweiterte Sinneswahrnehmung: Der Spieler sieht Schwellen-Objekte, die für andere unsichtbar sind (bestimmte versteckte Durchgänge, Schwellensubstrat-Konzentrationen, die den Weg zu Schwarzmarkt-Ressourcen weisen)
- Leichte intuitive Kampfunterstützung: Gegnerbewegungen werden einen Herzschlag früher "wahrgenommen" — kein Kampf-Autoziel, aber eine kleine Reaktionszeitverlängerung

*Kosten:*
- Gelegentliche Wahrnehmungsstörungen: Schatten an falscher Stelle, Geräusche ohne Quelle. Keinen spielmechanischen Nachteil — aber der Spieler merkt, dass etwas nicht stimmt
- Sichtbare leichte Veränderung: Unter bestimmtem Licht sind die Lymph-Muster unter der Haut sichtbar. Bestimmte NPCs reagieren darauf.

*Reversibilität:* Vollständig reversibel durch Entfernung von Fieberquellen und Krone-Medizin. Der Spieler kann hier jederzeit zurück.

**Stadium II — Wandlung (Lymph-Stufe III: Kontaminiert)**

Das zweite Stadium ist der Preis für Macht:

*Vorteile:*
- Deutliche physische Buffs: Erhöhte Stärke und Ausdauer (überlagert Muskel- und Cardio-Subsystem)
- Tiefere Schwellen-Wahrnehmung: Der Spieler nimmt Dünnstellen intuitiv wahr, kann Schwellensubstrat "spüren" (Mechanik: Kompass-ähnlicher Puls in Dünnstellen-Richtung)
- Immunität gegen leichte Schattenfieber-Exposition: Kontaminierte Bereiche, die andere töten würden, kann der Spieler bereisen

*Kosten:*
- Erinnerungsfragmentierung: Gelegentlich berichtet das Spiel eine Szene anders als beim ersten Erleben. Nicht gameplaymäßig einschränkend, aber psychologisch belastend
- Sichtbare Mutation: Dunkle Adern, teilweise Transparenz der Haut, veränderte Augen. Oberschicht-NPCs verweigern Interaktion. Bestimmte Questlinien werden unzugänglich (Orden-Questlinie kürzt sich dramatisch).
- Soziale Kosten: Krone-Ruf nimmt passiv ab, solange Stadium II aktiv ist

*Reversibilität:* Nicht heilbar, aber managebar. Gilden bieten Stabilisierungspräparate (teuer, laufende Kosten). Orden bietet Kontroll-Rituale (kostenlos, aber mit Dankesschuld).

**Stadium III — Entgrenzung (Lymph-Stufe IV: Durchdrungen)**

Das dritte Stadium ist das Ende der kontrollierten Progression:

*Vorteile:*
- Extremer Power-Spike: Der Spieler ist physisch auf dem Maximum. Übernatürliche Stärke, Schwellenwahrnehmung permanent aktiv, temporäre Unverwundbarkeit möglich
- Direkte Schwellen-Interaktion: Der Spieler kann Orte und Objekte berühren, die im normalen Zustand unzugänglich sind. Bestimmte Questenden werden erst hier zugänglich.

*Kosten:*
- Kontrollverlust: Spieleraktionen werden gelegentlich durch "Schwellen-Impulse" überlagert — die Figur handelt für Sekunden autonom
- Narrativer Sackweg: Ab Stadium III sind bestimmte Quest-Outcomes unmöglich. Der Spieler kann die Geschichte nicht mehr in bestimmte Richtungen lenken.
- Irreversibilität: Ohne Schwellenanker-Intervention oder Orden-Hochritual kein Zurück.

*Der Schwellenanker als Stabilisator:* Ein Spieler, der den Schwellenanker hält (Hauptquest-Fortschritt), kann Stadium III partiell stabilisieren. Das ist keine Heilung — aber es verhindert das unkontrollierte Durchgleiten in den Identitätsverlust. Dies ist der narrative und mechanische Kern des Hauptquests.

![Schwellenanker: Zustand Drei — Auflösung](../concepts/day02-vera/relics/relikt-zustand-drei-aufloesung_seedream-4-5.png)

*Konzeptbild: Zustand Drei. Der Schwellenanker in Auflösung — die visuelle Entsprechung von Lymph-Stufe IV. Die Grenzen zwischen Objekt und Umgebung lösen sich auf.*

### Die drei Fraktions-Antworten auf das Schattenfieber

**Krone — Unterdrückung**

Die Krone behandelt das Schattenfieber als militärisches Problem. Ihre Ärzte und Quartiermeister bieten Krone-Medizin: Suppressoren, die den Lymph-Wert aktiv senken und Stufe I reversieren.

*Gameplay:*
- Krone-Medizin ist kostenlos für Krone-Mitglieder, teuer für andere
- Unterdrückung verhindert alle Fieber-Vorteile — aber auch alle Fieber-Kosten
- Krone-Weg-Spieler sind das "saubere" Spielprofil: sozial akzeptiert, alle Questlinien offen, aber ohne Fieber-Buffs auf physische Ressourcen angewiesen

*Trade-off:* Wer den Krone-Weg geht, verzichtet auf die Macht des Fiebers. Krone-Quests kompensieren das durch bessere Ausrüstung, Zugang zu Tiegelstahl-Waffen, und politische Unterstützung.

**Gilden — Verwertung**

Die Gilden sehen das Schattenfieber als Rohstoff. Ihre Alchemisten bieten Stabilisierungspräparate, die den Lymph-Wert auf einem Plateau halten: Die Vorteile von Stadium I bleiben zugänglich, die unkontrollierte Progression zu Stadium II wird verhindert.

*Gameplay:*
- Gilden-Präparate sind teuer und müssen regelmäßig erneuert werden (laufende Ressourcenkosten)
- Wer mit Gilden-Zugang arbeitet, kann Stadium I kontrolliert halten — und bei Bedarf (für kurze Zeit, mit Nachkater) auf Stadium II übersteigen
- Gilden-Weg-Spieler sind das "pragmatische" Spielprofil: sie nutzen das Fieber als Werkzeug, zahlen dafür regelmäßig, und halten Optionen offen

*Trade-off:* Ressourcenintensiv. Wer keine konstante Einnahmequelle hat, kann den Gilden-Weg nicht aufrechterhalten. Das verknüpft Fieber-Management direkt mit der Wirtschaftsmechanik.

**Orden — Destillation und Verstehen**

Der Orden behandelt das Schattenfieber als Prüfung und als Zugang zu Wissen. Ihre Rituale ermöglichen kontrollierten, langsamen Aufstieg durch die Stufen — mit Stabilisierung auf jeder Ebene.

*Gameplay:*
- Orden-Rituale sind kostenlos (Kosten: Zeit und Verpflichtung gegenüber dem Orden)
- Wer den Orden-Weg geht, kann das Fieber tiefer nutzen als der Gilden-Weg — bis in Stadium II hinein, stabil
- Orden-Weg-Spieler sind das "tiefste" Spielprofil: Sie verstehen das Schattenfieber am besten, haben den tiefsten Lore-Zugang, aber der Orden hat eine Agenda

*Trade-off:* Der Orden will etwas. Jedes Ritual ist eine Schuld. Irgendwann fragt der Orden nach dem Schwellenanker.

---

## 2.6 Systeminteraktionen

Die fünf Kernsysteme existieren nicht isoliert. Ihre Stärke kommt aus den Wechselwirkungen:

**Kampf × Nervensystem-Leveling**
Jeder Kampf trainiert Cardio und Muskel. Ein Spieler, der kämpft, wird besser im Kampf. Das ist die direkteste Feedback-Schleife. Aber: Wer riskante Kämpfe mit Schwellensubstrat-Extrakten gewinnt, trainiert auch das Lymph-Subsystem — ungewollt.

**Crafting × Fraktionsruf**
Bessere Materialien erfordern höheren Fraktionsruf. Das bindet Crafting an Fraktionsentscheidungen. Wer den Orden hofiert, bekommt kein Damaszener-Stahl — der Orden handelt nicht mit Waffen. Wer die Gilden höfiert, verliert Krone-Ruf. Crafting-Optimierung ist Fraktions-Optimierung.

**Schattenfieber × Fraktionsruf**
Der Fieber-Status des Spielers verändert Fraktions-Reaktionen. Ein Spieler in Stadium II ist bei der Krone nicht mehr willkommen. Ein Spieler in Stadium I wird vom Orden besonders aufmerksam behandelt (sie wollen wissen, wie weit er bereits ist). Die Gilden sind die einzige Fraktion, die aktive Fieber-Träger ohne Stigma bedient — weil sie sie als Kunden brauchen.

**Nervensystem-Leveling × Crafting**
Muskel-Stufe III+ ist Voraussetzung für sinnvolle Nutzung von Klasse-IV-Ausrüstung. Der Spieler kann sich die besten Materialien kaufen — aber erst nutzen, wenn der Körper folgt. Das verhindert "Day-One-Endgame-Gear" und macht die Progression organisch.

**Kampf × Schattenfieber**
Wer mit Schwellensubstrat-Extrakten kämpft, gewinnt Macht und verliert Kontrolle. Der schnellste Weg zum Kampfsieg ist oft der direkteste Weg in Stadium III. Das ist die ultimative Abwägung des Systems.

---

<!-- Darius: Offene Punkte für interne Klärung — nicht im sichtbaren Dokument. W-001/W-002 aus Emres WBB (Schwellensubstrat als Substanz vs. Feld, Kippmoment Stufe I → II) müssen vor v2 dieses Kapitels synchronisiert werden. Leo-QA-Pass auf Balancing-Werte (Ruf-Schwellenwerte, Lymph-Akkumulation) steht aus. -->

*Versionsstatus: v1 — Alle fünf Kernsysteme ausgearbeitet. Balancing-Werte (konkrete Zahlenwerte) folgen in v2 nach Leo-QA-Sync. Systeminteraktionen definiert. Spieler-Fantasie-Statements verifiziert.*

\clearpage

# Bildliste für Darius — Vera-Concept-Art Handoff

**Von:** Finn
**An:** Darius
**Datum:** Mi, 28.02.2026, 10:15 Uhr
**Ziel:** Zeigt dir, welche Vera-Bilder du für GDD Kap 5 (Art Direction) nutzen sollst

---

## Verfügbare Vera-Renders (Di generiert)

### Relikt — **2 Bilder für Kap 5 & Geschäfte mit Spielmechanik**

1. **`relikt-hero-shot-aktiviert_gpt-image-1-5`**
   - Beschreibung: Schwellenanker im aktivierten Zustand auf Altar in Kammer, Spieler im Hintergrund awed
   - CD-Feedback: "Sieht cool aus — mitnehmen"
   - **Aktion:** Text/Prompts entfernen, ins Markdown einbinden
   - **Fit:** Kap 5 Art Direction (visuelle Darstellung des Relikt/Schwelleankers) + GDD Kap 1 (High Concept Illustration möglich)

2. **`relikt-drei-zustaende-vergleich_nano-banana-2`**
   - Beschreibung: 3-Panel Vergleich (Ruhend | Aktiviert | Auflösung) nebeneinander
   - CD-Feedback: "Kommt am nächsten ran, aber Text weg"
   - **Aktion:** Alle Labels/Prompts entfernen, nur die 3 Bilder
   - **Fit:** GDD Kap 2–3 (Mechanik erklärt) oder Kap 5 (visuelle Designsprache)

**SKIP:**
- `relikt-zustand-null-ruhend` (zu düster, Panel-Set bereits besser)
- `relikt-zustand-eins-aktiviert` (zu isoliert, Hero-Shot besser)
- `relikt-zustand-drei-aufloesung` (zu isoliert, Panel-Set besser)

---

### Fraktions-Materialpaletten — **3 Bilder für Kap 5 & WBB Mythos/Ethos**

1. **`fraktion-krone-materialpalette`**
   - Beschreibung: Flat-lay (Titanium, Blutrot-Signet, Damask Stahl, Black Brocade, Kristallglas)
   - CD-Feedback: ✅ "Super"
   - **Aktion:** Keine (nutzen as-is)
   - **Fit:**
     - GDD Kap 5 (Materialsprache der Oberschicht visualisieren)
     - WBB Kap 1 (optional: Mythos-Eröffnung, wie die Krone sich selbst sieht)

2. **`fraktion-orden-materialpalette`**
   - Beschreibung: Flat-lay (Weiße Leinen, Kristalllinse, Vellum Manuskript, Lumineszent-Phial, Knochen-Rosenkranz)
   - CD-Feedback: ✅ "Super"
   - **Aktion:** Keine (nutzen as-is)
   - **Fit:**
     - GDD Kap 5 (Materialsprache des Wissens visualisieren)
     - WBB Kap 1 (optional: Mythos-Eröffnung, wie der Orden sich selbst sieht)

3. **`fraktion-gilden-materialpalette`**
   - Beschreibung: Flat-lay (Indigo Brocade, Malachit, Amber, Bronze Siegel, Leder-Schürze, Pigment-Proben)
   - CD-Feedback: ⚠️ "Text zu viel — kürzen"
   - **Aktion:** Vera braucht noch heute (Mi 12:00): Labels/Erklärungen entfernen. Nur Material + Kontext minimiert.
   - **Fit:**
     - GDD Kap 5 (Materialsprache der Mittelschicht/Handwerk)
     - WBB Kap 1 (optional: Mythos)

---

### Umgebung — **1 Bild, aber mit Caveats**

**`stadtschnitt-vertikale-schichtung`**
- Beschreibung: Cross-section der vertikalen Stadt (4 Schichten: Slums | Fachwerk | Gilden | Krone)
- CD-Feedback: ⚠️ "Sieht unnatürlich aus — nächste Iteration"
- **Aktion:** SKIP für v0.1. Vera iteriert am Do/Fr (Deadline v0.2/v0.3)
- **Fit:** GDD Kap 5 (Environment/Architecture), optional WBB Kap 2 (Topos Visual)

---

## Dein Workflow (GDD Kap 5 — Art Direction)

**Was ich von dir erwarte (Mi 15:00 Draft):**

1. **Relikt-Bilder einbinden:**
   - Hero-Shot in Text zu Schwellenanker-Visualisierung integrieren
   - 3-Panel-Vergleich in Mechanik-Sektion (Progression zeigen: dormant → active → dissolution)

2. **Materialpaletten-Farbsprache nutzen:**
   - Du hast jetzt visuelle Referenzen für alle 3 Fraktionen
   - Text: beschreib die Designprinzipien (warum diese Farben, Materialien, Silhouetten)
   - Bilder dienen als Beweis

3. **HTML-Kommentare:**
   - Alle deine Notizen/Anmerkungen zu Vera-Bilder → in HTML-Kommentare umwandeln
   - Kein Text über den Bildern im PDF

4. **Referenzen checken:**
   - Siehst du konsistente Designsprache über alle 9 Bilder?
   - Feedback für Vera (Do morgen): Was funktioniert? Was braucht Iteration?

---

## Vera-Input (parallel — sie sitzt auch gerade an Cleanup)

**Vera macht parallel (Mi 12:00–17:00):**
- Gilden-Palette Text kürzen (CD braucht das bis heute)
- Alle Metadaten entfernen (Künstler-Namen, Prompt-Text)
- Renders in sauberes Format für PDF vorbereiten

**Darius-Feedback für Vera (Do morgen):**
- Darius checkt heute: Welche 2 Relikt-Bilder funktionieren zusammen?
- Welche Paletten-Farben passen zu Spielmechanik?
- Input an Vera → mehr Refinement für v0.2

---

## Zusammenfassung für die Timeline

| Bild | Kapitel | Action | Status |
|------|---------|--------|--------|
| **Relikt Hero-Shot** | GDD Kap 5 (+ optional 1) | Einbinden, Text weg | 🔵 Bereit |
| **Relikt 3-Panel** | GDD Kap 2–3 oder 5 | Einbinden, Labels weg | 🔵 Bereit |
| **Krone-Palette** | GDD Kap 5 + WBB Kap 1 | Einbinden, as-is | 🔵 Bereit |
| **Orden-Palette** | GDD Kap 5 + WBB Kap 1 | Einbinden, as-is | 🔵 Bereit |
| **Gilden-Palette** | GDD Kap 5 + WBB Kap 1 | Einbinden, Text kürzen (Vera) | ⏳ Vera arbeitet dran (heute) |
| **Stadtschnitt** | GDD Kap 5 + WBB Kap 2 | SKIP v0.1, nächste Iteration | ⏳ Vera macht Do/Fr v0.2 |

---

## Fragen?

- Brauchst du mehr Kontext zu den Bildern? → Lese Vera's Recherche-Notizen: `simulation-2/gallery/concepts/00-recherche-notizen-vera-v1.md`
- Wo genau in Kap 5 passen sie? → Dein Design. Ich kann checken bei Mi 15:00.
- Feedback für nächste Vera-Iteration? → Schreib kurz auf → ich gebe Vera Bescheid (Do morgen)

**Deadline:** Deine Bilder-Integration bis Mi 15:00. Gilden-Palette von Vera kommt bis heute 12:00.

Moin.

\clearpage

# GDD Kapitel 03 — Erzählkonzept

<!-- Status: v1 | Tag 3, Mittwoch | Autor: Darius Engel -->
<!-- Darius: Dieses Kapitel ist in enger Abstimmung mit Nami Okafors GDD Kap. 4 entstanden. Nami hat Figuren und Quest-Skizzen geliefert; ich habe die systemische Struktur und die Spieler-Aktiv-Mechaniken hinzugefügt. Die Ablehn-Option (Spieler darf Fragment verweigern) ist CD-bestätigt und hier vollständig ausgearbeitet. -->
<!-- Darius: Verwendete Quellen: GDD Kap. 4 v1 (Nami, Tag 2), WBB Kap. 1 v1 (Emre, Tag 2), Briefing. Nami hat die Figuren-Stimmen, ich habe die Quest-Mechanik. Das Erzählkonzept braucht v2 mit Namis ausformuliertem Halbseiten-Text zur Ablehn-Option (war für Mi 10:00 versprochen). -->

---

## Überblick

Das Erzählkonzept von RELICS: Der Schwellenanker definiert, wie die Geschichte erzählt wird — nicht was die Geschichte ist. Die Handlung ist ein Werkzeug, um die vier Design-Säulen erfahrbar zu machen.

**Zentrales Erzählprinzip:** Der Spieler ist kein Held. Er ist ein Fremder, der in eine Situation hineingezogen wird, die ohne ihn bereits bestand. Die Geschichte ist nicht über den Spieler — sie ist eine Geschichte, in der der Spieler Entscheidungen trifft.

**Erzählstruktur:** Drei Akte, drei Fraktionspfade, mehrere Questlinien, die sich überschneiden und widersprechen. Kein Akt ist vollständig linear. Jeder Akt hat einen "Open-World-Raum", in dem der Spieler die Welt erkundet, bevor er den nächsten narrativen Anker betritt.

---

## 3.1 Intro-Sequenz — "Was er in der Hand hielt"

### Spieler-Fantasie

*"In den ersten fünfzehn Minuten muss ich verstehen, was dieser Ort ist. Nicht durch Exposition — durch Erleben."*

### Die Szene

**Zeitpunkt:** Früher Morgen. Die Stadt Schwarzrand liegt im Nebel. Der Spieler betritt die Spielwelt zum ersten Mal.

**Der Sterbende:** Hieronymus Vael liegt am Stadtrand, zwischen zwei ausrangierten Karrengeleisen. Freier Bote, gescheitert. Schattenfieber Stadium III. Er hat nicht mehr lange. Er hält etwas in der Hand: eine Scherbe aus einem Material, das der Spieler noch nicht einordnen kann. Unter einer bestimmten Neigung des Lichts leuchtet es — schwach, biolumineszent, unheimlich schön.

**Die Übergabe-Szene (Clip-Moment):** Hieronymus Vael sieht den Spieler. Er hat keine Kraft mehr für eine lange Erklärung. Er versucht es trotzdem. Die Szene dauert nicht länger als drei Minuten.

> *"Nimm das. Geh nicht zurück, wo du herkamst — dort kennen sie deinen Weg. Versteh das nicht als Warnung. Versteh das als das Einzige, was ich dir noch geben kann."*

Er streckt die Hand mit der Scherbe aus.

### Die Ablehn-Option

**CD-Entscheid:** Der Spieler darf das Fragment ablehnen.

Das ist keine Illusion einer Wahl. Es ist eine echte Verzweigung.

**Wenn der Spieler annimmt (Standard-Pfad):**
- Das Fragment wechselt in das Inventar des Spielers
- Hieronymus Vael stirbt kurz danach
- Schattenfieber-Exposition beginnt sofort: Lymph-Wert steigt minimal (kaum wahrnehmbar in Minute 15, signifikant in Stunde 3)
- Die drei Boten erscheinen (→ Abschnitt 3.2)
- Das Spiel öffnet sich in die volle Freiheit von Schwarzrand

**Wenn der Spieler ablehnt (Alternativer Einstieg):**

Der Spieler sagt Nein. Oder sagt nichts und wendet sich ab.

Hieronymus Vael schaut ihn an. Er hat keine Energie für Überzeugungsarbeit. Er legt die Scherbe ins Gras neben sich, schließt die Augen.

*Was dann passiert:*

1. Vael stirbt. Die Scherbe liegt im Gras. Der Spieler kann Schwarzrand betreten.
2. **Kurzfristige Konsequenz (erste Stunde):** Die drei Boten erscheinen trotzdem. Sie fragen nach der Scherbe. Der Spieler kann sagen, er habe sie nicht. Das stimmt. Alle drei Boten glauben ihm zunächst — aber die Glasmacher-Gilde hat Schwellenlinsen. Vreni Kast weiß, dass jemand in der Nähe des Toten war. Sie fragt nach.
3. **Mittelfristige Konsequenz (Akt 1):** Die Scherbe bleibt an Hieronymus' Sterbeort. Sie ist nicht weg — sie liegt da. Wer sie sucht, findet sie. Andere Akteure (Fraktionsboten) finden sie innerhalb von Stunden, wenn der Spieler sie nicht aufhebt. Der Spieler hat ein Zeitfenster.
4. **Langfristige Konsequenz:** Wer die Scherbe nie nimmt, spielt einen anderen Akt-1-Einstieg. Die Fraktionen nähern sich dem Spieler aus einem anderen Winkel — nicht als möglicher Träger des Fragments, sondern als möglicher Zeuge. Das öffnet bestimmte Quest-Optionen (Zeuge-Rolle), schließt andere (Fragment-Träger-Rolle). Spätestens in Akt 1, Beat 3 führt jeder Pfad zur selben zentralen Frage: Was ist das Fragment? Warum ist es hier? Warum stirbt jeder, der es trägt?

<!-- Darius: Namis Halbseite zur Ablehn-Option (versprochen Mi 10:00) sollte hier die konkreten Dialog-Optionen und den genauen Beat-Ablauf des Ablehn-Pfads ergänzen. Ich habe die systemische Struktur gesetzt; sie hat die Stimmen. -->

**Warum diese Entscheidung richtig ist:**

Das Briefing fordert: Immersive Sim. Echte Wahlfreiheit. Ein Spiel, das vorgibt, man könne ablehnen, es dann aber erzwingend macht, ist keine Immersive Sim — es ist ein Schienenspiel mit Illusionsknöpfen. Die Ablehn-Option muss real sein, um das Vertrauen des Spielers zu verdienen. Wenn er weiß, dass "Nein" tatsächlich Nein bedeutet, wählt er mit anderen Augen.

### Beat-Struktur der Intro-Sequenz

**Beat 1 — Ankunft:** Spieler betritt die Welt. Stadtrand. Nebel. Vael liegt da. Keine Erklärung, keine Exposition. Der Spieler sieht einen sterbenden Mann.

**Beat 2 — Die Scherbe:** Vael spricht. Kurz, erschöpft, klar. Die Übergabe-Szene. Spieler entscheidet: Nehmen oder ablehnen.

**Beat 3 — Die ersten Minuten nach Vael:** Der Spieler ist alleine. Drei Boten nähern sich — eine Uniformierte (Krone), ein ziviler junger Mann mit versiegeltem Brief (Orden), und... niemand. Die Gilden-Reaktion ist Vreni Kast, die "zufällig" auf dem Markt ist, wenn der Spieler die Stadt betritt.

**Beat 4 — Erster Fraktionskontakt:** Der Spieler spricht mit einem der drei Boten zuerst. Das ist die erste nicht-erzwungene Entscheidung. Die Welt merkt sie sich.

**Beat 5 — Schwarzrand:** Der Spieler betritt die Stadt zum ersten Mal richtig. Er sieht die vertikale Schichtung. Er hat keine Ahnung, wo er steht.

---

## 3.2 Akt 1 — Das Fragment

### Spieler-Fantasie

*"Ich verstehe gerade, was dieser Ort bedeutet. Und ich beginne zu verstehen, dass ich in der Mitte von etwas bin, das schon lange vor mir lief."*

### Erzählraum

Akt 1 ist die Exposition. Nicht durch Lore-Dumps — durch Erfahrung. Der Spieler erkundet Schwarzrand. Er trifft die Schlüssel-NPCs (→ GDD Kap. 4). Er beginnt, die Machtverhältnisse zu verstehen.

**Zeitliche Länge:** Akt 1 sollte die ersten 8–12 Spielstunden umfassen. Der Spieler soll Zeit haben, die Welt zu atmen, bevor der erste Act-1-Kulminationspunkt kommt.

### Schlüssel-Beats Akt 1

**Die drei Fraktionskontakte:** Der Spieler lernt alle drei kennen. Das kann in beliebiger Reihenfolge geschehen. Adelhaid Brenn (Krone) will das Fragment. Ivo Scherer (Orden) will es untersuchen. Vreni Kast (Gilden) will es analysieren. Alle drei haben gute Argumente. Keines der Argumente ist vollständig wahr.

**Die erste Fraktionsentscheidung:** Ab einem bestimmten Punkt in Akt 1 verlangt eine Fraktion eine Entscheidung — eine Aufgabe, die signalisiert, mit wem der Spieler arbeitet. Dieser Moment ist keine Zwangshandlung; der Spieler kann sich verweigern. Aber die Fraktionen werden ungeduldiger, je länger er wartet.

**Salva und die vierte Perspektive:** Salva (Tiervolk) erscheint frühzeitig in Akt 1. Er ist kein Auftraggeber — er ist ein Kontext-Lieferant (→ GDD Kap. 4). Die Information, die er über das Fragment hat, verändert nicht den Questpfad, aber die Interpretation. Der Spieler, der Salva gründlich befragt, versteht mehr — und misstraut den drei Fraktionen früher.

**Das erste Fieberflüstern:** Irgendwann in Akt 1 bemerkt der Spieler das erste Schattenfieber-Symptom. Das ist kein Story-Trigger — es ist eine organische Konsequenz des Lymph-Wert-Anstiegs. Schatten bewegen sich nicht richtig. Ein Geräusch hallt nach. Der Spieler sieht etwas, das nicht da ist. Eine Sekunde. Dann ist es vorbei.

**Der Akt-1-Kulminationspunkt:** Jeder Fraktionspfad hat einen Akt-1-Kulminationspunkt, der in den Akt-2-Raum führt. Beispiel Krone-Pfad: Brenn gibt dem Spieler den Auftrag, eine Schwarzmarkt-Scherbe zu sichern, bevor die Gilden es tun. Das führt den Spieler erstmals tief in den Schlund. Dort sieht er, was Brenns "kontrollierte Quarantäne" konkret bedeutet. Das ist die Moment der Kompliziertheit.

---

## 3.3 Hauptquest — "Der Schwellenanker"

### Spieler-Fantasie

*"Ich verfolge ein Objekt und merke, dass ich mich selbst verfolge."*

### Narrative Grundfrage

Die zentrale Frage des Hauptquests: **War ich immer hier, oder hat der Schwellenanker mich gerufen?**

Diese Frage wird nie direkt beantwortet. Das ist keine Schwäche der Geschichte — das ist die Geschichte.

Der Spieler kommt als Fremder. Ohne Gedächtnis an den Weg hierher. Ohne klare Motivation außer: Er war in der Nähe, als Vael starb. Oder: Er hat das Fragment genommen. Oder abgelehnt. In jedem Fall befindet er sich jetzt in Schwarzrand, und Schwarzrand hat Konsequenzen für ihn.

Irgendwann, irgendwo zwischen Akt 1 und Akt 2, stellt der Spieler fest: Das Fragment reagiert auf ihn. Nicht auf jeden. Auf ihn spezifisch. Der Lymph-Wert steigt schneller als bei anderen. Visions-Fragmente zeigen Orte, die er noch nie gesehen hat. Der Schwellenanker kennt ihn irgendwie. Oder er kennt den Schwellenanker.

### Akt-Struktur der Hauptquest

**Akt 1 — Das Fragment (parallel zu Abschnitt 3.2)**

Gameplay-Ziel: Den Ursprung des Fragments verstehen.
Narrative Frage: Was habe ich in der Hand?

Der Spieler sammelt Informationen aus drei Quellen (die drei Fraktionen liefern jeweils eine Teilwahrheit), Salva ergänzt eine vierte Perspektive, und das Fragment selbst "zeigt" gelegentlich Bilder — Dünnstellen, Kammern, Tiefen — die keiner erklären kann.

Am Ende von Akt 1 weiß der Spieler: Das Fragment ist ein Stück von etwas Größerem. Dieses Größere liegt irgendwo unter Schwarzrand. Und alle drei Fraktionen suchen es seit einer Generation.

**Akt 2 — Das Muster**

Gameplay-Ziel: Die anderen Fragmente finden.

Narrative Frage: Wer hat den Schwellenanker zerstört, und warum?

Das Fragment ist nicht einzigartig. In Akt 2 entdeckt der Spieler, dass der Schwellenanker in Stücke zerbrochen wurde — wann, durch wen, ob absichtlich. Die Fraktionen haben Fragmente, oder wissen wo sie sind, und halten diese Information zurück. Akt 2 ist ein Netz aus Halbwahrheiten und verdeckten Interessen.

**Mechanische Verknüpfung:** Jedes Fragment, das der Spieler findet oder berührt, erhöht den Lymph-Wert. Das ist keine Falle — es ist eine Einladung. Wer das Muster aktiv sucht, nähert sich der Schwelle. Der Spieler entscheidet, wie weit er geht.

**Die Koalitions-Enthüllung:** In Akt 2 entdeckt der Spieler, wer die Wurzelkammer geöffnet hat: Es war eine Koalition aus allen drei Fraktionen — Orden-Gelehrter, Gilden-Expedition, Kron-Beauftragter. Jeder gibt die Schuld den anderen. Alle haben sie. Das ist der Moment, in dem keine Fraktion mehr "richtig" sein kann — jede hat eine Leiche in ihrem Keller, buchstäblich.

**Akt 2 Kulminationspunkt:** Der Spieler findet den Weg zur Wurzelkammer. Er muss entscheiden, ob er hinabsteigt. Bis hierhin war die Geschichte verhandelbar. Ab hier nicht mehr.

**Akt 3 — Die Schwelle**

Gameplay-Ziel: Den Schwellenanker wiederherstellen oder zerstören oder keines von beidem.

Narrative Frage: Was tue ich mit dem, was ich weiß?

Der Spieler erreicht die Wurzelkammer. Was er dort findet, hängt von seinen bisherigen Entscheidungen ab — aber die Kammer selbst ist real, konsistent, und physisch präsent. In ihr: die natürliche Position des Schwellenankers. Leer, seit einer Generation. Das Schattenfieber steigt von unten wie Grundwasser.

Der Spieler hält Fragmente des Schwellenankers. Er kann sie zurücklegen. Er kann sie behalten. Er kann sie einer Fraktion überlassen. Er kann sie zerstören. Jede Entscheidung hat systemische Konsequenzen für die Welt von Schwarzrand.

### Die drei Hauptenden

**Ende 1 — Restauration (Krone-affin)**

Der Spieler legt alle Fragmente in die Wurzelkammer zurück. Der Schwellenanker stabilisiert die Schwelle. Das Schattenfieber reckt sich nicht. Schwarzrand überlebt.

*Konsequenz:* Die Krone kontrolliert die Kammer militärisch. Das Schattenfieber wird zum Staatsgeheimnis verwaltet. Die untersten Schichten bleiben, wo sie sind. Die Welt ist stabiler — und ungerechter als je zuvor. Brenn bekommt, was sie will. Die Schwächsten zahlen weiter den Preis.

**Ende 2 — Destillation (Gilden-affin)**

Der Spieler übergibt die Fragmente den Gilden. Die Glasmacher-Gilde synthetisiert den Schwellenanker als Rohstoff. Die Schwelle wird nutzbar — kontrollierbar, handelbar, profitierend. Das Schattenfieber eskaliert kurzfristig (Kontrollverlust in der Übergangsphase), dann stabilisiert die neue Gilden-Chemie.

*Konsequenz:* Die Gilden monopolisieren die Schwelle als Ressource. Das ist der konsequenteste Ausdruck des Medieval-Cyberpunk-Paradigmas: Die Natur wird zur Ware. Vreni Kast triumphiert. Die Profite bleiben oben. Die Kosten bleiben unten.

**Ende 3 — Öffnung (Schwellenaffin)**

Der Spieler gibt keine Fragmente ab. Er legt sie nicht zurück. Er hält sie. Und er bleibt in der Kammer.

Was passiert: Die Schwelle öffnet sich weiter. Das ist kein Weltuntergang — es ist eine Transformation. Schattenfieber-Betroffene in Stadium II und III beginnen, zu verstehen, was sie sind. Etwas kommt durch. Es ist nicht nur Krankheit — es ist das, wovon das Tiervolk immer gesprochen hat: Kommunikation.

*Konsequenz:* Schwarzrand verändert sich fundamental. Ob das besser oder schlechter ist, ist unklar. Der Orden verliert die Deutungshoheit. Die Krone verliert die Kontrolle. Die Gilden verlieren die Rohstoffquelle. Aber die Menschen in den untersten Schichten — die, die ohnehin schon tief in der Schwelle leben — werden zu etwas, das die anderen Fraktionen nicht mehr ignorieren können.

*Dies ist das einzige Ende, das die Frage "Kommunikation oder Krankheit?" beantwortet. Und die Antwort ist: beide.*

### Der Schwellenanker als mechanischer Hauptquest-Anker

Der Schwellenanker ist im Hauptquest mehr als ein Aufgabenobjekt. Er ist eine mechanische Beziehung:

- **Resonanz-Intensität:** Je höher der Lymph-Wert des Spielers, desto stärker "antwortet" der Schwellenanker. Visuelle Effekte intensivieren sich. Zusatz-Informationen werden zugänglich (Lore-Fragmente, die nur sichtbar sind, wenn der Spieler in Stadium I–II ist).
- **Fragment-Auffinden:** Der Schwellenanker-Puls (→ Kap. 2.5, Lymph-Stufe III-Vorteil) ist kein abstraktes HUD-Element — er ist eine physische Empfindung im Spiel, die die Richtung von anderen Fragmenten anzeigt.
- **Entscheidungspunkt:** Der finale Akt-3-Entscheid ist der einzige Moment im Spiel, an dem die Mechanik (Lymph-Wert, Fraktionsruf, verfügbare Fragmente) direkt die zugänglichen Enden bestimmt. Ein Spieler ohne ausreichenden Lymph-Wert kann Ende 3 nicht erreichen. Ein Spieler mit feindseligen Gilden kann Ende 2 nicht wählen.

---

## 3.4 Fraktionsquests

<!-- Darius: Diese Ausarbeitungen sind für v1 strukturell vollständig. Dialog-Details und spezifische Quest-Texte kommen in v2 mit Namis Kollaboration. -->

### Krone-Questlinie — "Das Erste Siegel"

**Hauptkontakt:** Marschall Adelhaid Brenn

**Questlinie-Fantasie:** *"Ich habe Legitimität erkauft. Jetzt zahle ich den Preis dafür."*

**Kernspannung der Krone-Linie:** Die Krone will Ordnung. Brenn glaubt an Ordnung. Der Spieler kann daran glauben — bis er sieht, was Ordnung kostet.

**Quest-Verlauf:**

*Quest 1 — "Passierschein"*
Brenn braucht jemanden ohne Kronstempel, der einen Auftrag in der Unterstadt erledigt. Der Spieler holt Informationen über eine Schwarzmarkt-Scherbe. Einfache Einführung in die Krone-Mechanik: Bewegungsfreiheit als Ressource, Krone als Schutzmacht.

*Quest 2 — "Quarantäne"*
Eine Unterkanal-Zone wurde gesperrt. Offiziell: Routineinspektion. Tatsächlich: Schattenfieber-Ausbruch unter vierzig Zivilisten. Brenn hat die Zone versiegelt. Der Spieler wird geschickt, den "Bericht" zu überbringen. Er trifft Menschen, die nicht wissen, warum sie eingesperrt sind. Siebzehn sind bereits gestorben.

*Entscheidungspunkt:* Der Spieler kann Brenns Anweisung befolgen (Bericht abliefern, zurückkehren). Er kann die Zone öffnen (Krone-Ruf sinkt, sieben der verbliebenen dreiundzwanzig überleben, Schattenfieber breitet sich in einen neuen Bereich aus). Er kann beides nicht tun und die Information verkaufen (an Orden oder Gilden).

*Quest 3 — "Das Archiv"*
Brenn weiß von Akten im Kronarchiv, die das Relikt erwähnen. Sie darf sie nicht lesen. Sie schickt den Spieler, sie zu stehlen. Was der Spieler findet: Die Krone kennt den Schwellenanker seit Generationen. Nicht das Fragment — das Original. Und hat nie gehandelt.

*Quest 4 — "Point of No Return"*
Brenn erfährt, was der Schwellenanker wirklich ist. Sie zieht sofort die militärische Konsequenz: Das muss der Krone gehören. Sie bittet den Spieler nicht. Sie verlangt. Dieser Moment definiert, ob der Spieler weiter mit der Krone geht — oder ob Brenn ab jetzt ein Hindernis ist.

---

### Gilden-Questlinie — "Der Rohstoff"

**Hauptkontakt:** Gildenmeisterin Vreni Kast

**Questlinie-Fantasie:** *"Ich baue echte Macht auf. Ich sehe, was sie kostet."*

**Kernspannung der Gilden-Linie:** Die Gilden sind die ehrlichste Fraktion — sie sagen, was sie wollen, und was es kostet. Aber Ehrlichkeit ist kein Schutz vor der Konsequenz dessen, was man tut.

**Quest-Verlauf:**

*Quest 1 — "Das Angebot"*
Kast trifft den Spieler "zufällig" auf dem Markt. Sie bietet Analyse des Fragments — nicht Besitz, Analyse. Zugang zu ihrer Werkstatt, ihrer Ausrüstung. Der Spieler bekommt erste Einblicke in die Gilden-Infrastruktur und die Materialsprache.

*Quest 2 — "Kanalrecht"*
Die Gerber-Gilde kontrolliert die Kanäle. Kast braucht Zugang zu einem tiefen Kanal-Abschnitt, den die Gerber gesperrt haben. Der Spieler verhandelt, kauft oder erzwingt den Zugang. Einführung in die Gilde-Mikropolitik: Die Gilden sind kein Block.

*Quest 3 — "Das Destillationsarchiv"*
Der Spieler findet Kasts Kellerarchiv. Destillationsversuche ohne Überlebende. Kast verteidigt das Archiv nicht moralisch: "Das waren Freiwillige. Das Schattenfieber hätte sie trotzdem getötet." Der Spieler entscheidet, wie er damit umgeht.

*Quest 4 — "Synthese"*
Kast hat genug Daten. Sie kann das Schattenfieber synthetisieren — in einem kleinen Maßstab. Sie braucht nur noch den Schwellenanker als finalen Datenpunkt. Dieser Quest ist der Gilden-Point-of-No-Return.

---

### Orden-Questlinie — "Die Prüfung"

**Hauptkontakt:** Bruder Ivo Scherer

**Questlinie-Fantasie:** *"Ich verstehe mehr als alle anderen. Der Preis dafür wird erst später fällig."*

**Kernspannung der Orden-Linie:** Der Orden hat das tiefste Wissen. Aber Wissen ist Kontrolle — und der Orden will beides.

**Quest-Verlauf:**

*Quest 1 — "Der Archivist"*
Scherer bietet Zugang zu einem Teil des Archivs. Erster Lore-Zugang, erste Fertigkeitsbücher (→ Nervensystem-Leveling-Unlock). Einführung in Scherers Informationsbroker-Mechanik: jede Information hat einen Preis.

*Quest 2 — "Die Kopie"*
Scherer zeigt dem Spieler seinen ur-Text-Fragmentfund. Fragmentarisch — und die fehlenden Stellen beschreiben genau, wie man den Schwellenanker zerstört. Ob das Auslassung oder Vergessen war, bleibt offen. Der Spieler kann Scherer danach fragen. Scherer sagt: "Ich weiß es nicht mehr."

*Quest 3 — "Deutungshoheit"*
Ein Priester im unteren Orden-Rang predigt eine Abweichler-Version des Schöpfungsmythos — näher an der biologischen Wahrheit als der offizielle Orden. Scherer schickt den Spieler, den Priester zum Schweigen zu bringen. "Zum Schweigen bringen" kann viele Formen annehmen. Der Orden-Quest ist der erste, der den Spieler offen mit dem Widerspruch zwischen Ordenslehre und biologischer Realität konfrontiert.

*Quest 4 — "Der Hochritus"*
Scherer bietet Zugang zum Orden-Hochritus: ein Ritual, das Schattenfieber-Stadium III stabilisieren kann. Dafür braucht der Orden den Schwellenanker. Der Spieler muss entscheiden, ob er zahlt — und womit.

---

## 3.5 Nebenquests

### "Der Zeuge"

**Typ:** Character-Quest
**NPC:** Alter Mann in den untersten Slums von Schwarzrand, Zeuge der "Öffnung" vor einer Generation

**Spieler-Fantasie:** *"Ich erfahre, was wirklich passiert ist — von jemandem, der dabei war."*

**Kurzbeschreibung:** Der alte Mann heißt Benedikt Haas. Er war Tunnel-Arbeiter bei der Gilden-Expedition, die die Wurzelkammer geöffnet hat. Er lebt im Schlund, isoliert, paranoid. Er ist der einzige Mensch in Schwarzrand, der alle drei Fraktionen aus der Koalitions-Nacht erkannt hat. Und er hat Angst.

**Quest-Struktur:**
- Der Spieler findet Haas über Salvas Hinweisnetz (Salva kennt ihn — oder kennt jemanden, der ihn kennt)
- Haas erzählt nicht auf Befehl. Er testet den Spieler zuerst: Beweise, dass du niemandem von der Fraktionskoalition arbeitest. Das ist schwer, wenn man gerade dabei ist, genau das zu tun.
- Wenn Haas vertraut: Er beschreibt die Nacht der Öffnung. Was er sah. Was die Fraktion-Vertreter sagten. Und warum er seither schweigt.
- Dramatischer Schluss: Haas bittet den Spieler um eine Aufgabe. Er will sterben — aber nicht durch das Fieber. Er will, dass jemand weiß, was er weiß, bevor er geht. Der Spieler kann annehmen oder ablehnen.

**Belohnung:** Haas gibt dem Spieler ein Objekt aus der Öffnungsnacht: Ein zerbrochenes Siegel, das alle drei Fraktionszeichen trägt. Unmöglich — aber real. Das ist der Beweis für die Koalition.

---

### "Die Weber-Gilde und das, was leuchtet"

**Typ:** Gilden-Seitenquest, Crafting-orientiert
**NPC:** Weberin Greth Saal, Mittelrang Weber-Gilde

**Spieler-Fantasie:** *"Ich verstehe, wie Macht durch Material fließt."*

**Kurzbeschreibung:** Greth Saal webt Schwellenfäden in Textilien — Fäden aus Organismen, die in Dünnstellen wachsen. Biolumineszent, reißfest, selbstreparierend. Begehrt von der Oberschicht. Und giftig für die Weber, die sie verarbeiten. Greth braucht jemanden außerhalb der Gilde, der ihr eine Ladung Fäden direkt aus dem Schlund beschafft — ohne den Gerber-Gilde-Zoll.

**Quest-Struktur:**
- Der Spieler beschafft die Fäden im Schlund (Schattenfieber-Exposition-Bereich)
- Dabei entdeckt er: die Weber, die in diesem Bereich arbeiten, leben alle in frühem Stadium II. Die Gilde weiß das. Das ist der Preis, den Greth nicht ausspricht.
- Entscheidungspunkt: Der Spieler kann die Fäden liefern (Gilden-Ruf +, Weber-Mikropolitik-Zugang). Er kann sie behalten und anderweitig verkaufen. Er kann die Information über die kranken Weber an den Orden oder die Krone weitergeben.

**Belohnung:** Zugang zu einer Weber-Gilde-Werkstatt und Rezepturen für biolumineszente Textilien (Crafting-Klasse III–IV).

---

### "Salvatore und die Karawane"

**Typ:** Tiervolk-Seitenquest, Lore-Quest
**NPC:** Salva

**Spieler-Fantasie:** *"Ich erfahre, was Salva wirklich ist — und was er wirklich weiß."*

**Kurzbeschreibung:** Salva verschwindet für eine Spielperiode. Wenn er zurückkommt, ist er verändert. Der Spieler kann nachfragen. Salva sagt: "Ich habe den Ursprungsort gefunden."

Was er gefunden hat: Den letzten bekannten Ort der Karawane, die vor Jahren verschwand — mit dem Objekt, das dem Schwellenanker ähnelte. Salva war das einzige Überlebende. Er war damals bereits in Dünnstellen-Nähe exponiert. Die Exposition hat ihn verändert — die Schuppenhaut, die erweiterten Sinne. Er ist kein Mensch mehr im biologischen Ursprungssinn. Er ist etwas dazwischen.

**Quest-Struktur:**
- Der Spieler kauft die Information über den Karawanenursprungsort von Salva (hoher Preis — Gold oder eine Gefälligkeit)
- Der Ort ist ein verfallenes Handelsposten außerhalb von Schwarzrand. Dort findet der Spieler Überreste der Karawane und ein weiteres Fragment
- Salva begleitet den Spieler optional. Er gibt keine Erklärungen. Er zeigt Richtungen.
- Am Posten: Der Spieler sieht Spuren, die zeigen, dass die Karawane nicht von außen angegriffen wurde. Sie hat sich von innen aufgelöst. Das Fragment war der Auslöser.

**Belohnung:** Ein weiteres Fragment (Hauptquest-Fortschritt) + Salvas vollständiges Vertrauen (Zugang zu seinen tiefsten Informationen).

---

## 3.6 Erzählerische Prinzipien

### Das epistemische Prinzip

Kein NPC im Spiel kennt die vollständige Wahrheit über den Schwellenanker. Der Spieler auch nicht. Die Geschichte ist ein Puzzle, das der Spieler aus Halbwahrheiten zusammensetzt. Die "Wahrheit" des Endes hängt davon ab, welche Quellen der Spieler befragt hat und welchen er geglaubt hat.

Das ist kein Versteck von Exposition. Es ist eine strukturelle Entscheidung: In einer Welt, in der drei Fraktionen aktiv konkurrierende Wahrheiten produzieren, kann kein Protagonist vollständige Wahrheit besitzen. Der Spieler erlebt dasselbe epistemische Problem wie die NPCs.

### Unreliable Memory

Ab Schattenfieber-Stadium II (Wandlung) werden Erinnerungen fragmentarisch. Das Spiel zeigt gelegentlich Szenen anders als beim ersten Erleben — ein Satz, den Hieronymus Vael sagte, klingt plötzlich anders. Ein Detail in Brenns erstem Gespräch fehlt. Das ist keine Continuity-Fehler — es ist eine mechanikvermittelte Erfahrung des Kontrollverlusts.

Der Spieler weiß nicht, welche Version wahr ist. Das ist Absicht.

### Die Erzählgeschwindigkeit

Akt 1: Langsam. Der Spieler soll Schwarzrand kennenlernen, bevor die Geschichte eskaliert.
Akt 2: Mittel. Die Informationsdichte steigt. Fraktionskonflikte spitzen sich zu.
Akt 3: Hoch. Alles läuft auf die Wurzelkammer zu. Der Spieler hat keine Zeit mehr für Ausweichen.

Die Spieler-Fantasie der ersten Stunde (Fremder betritt Sandbox) darf nicht gebrochen werden. Akt 1 muss diese Fantasie leben lassen. Die Geschichte zieht sich erst in Akt 2 eng.

---

![Schwarzrand: Vertikale Stadtschichtung](../concepts/day02-vera/environments/stadtschnitt-vertikale-schichtung_nano-banana-pro.png)

*Konzeptbild: Stadtschnitt Schwarzrand — die drei vertikalen Schichten (Obere Ränder / Mittelwand / Schlund) bilden den Schauplatz aller drei Akte.*

---

<!-- Darius: v2 dieses Kapitels braucht: Namis vollständige Ablehn-Option-Halbseite (Dialog-Optionen, Beat-Ablauf), ausformulierte Quest-Dialoge für mindestens zwei Quests, Leo-Feedback zur Erzählpacing-Logik. Quests 1-3 der Fraktionslinien sind strukturell gesetzt, aber textlich noch Stichpunkte. Das ist bewusst — das ist Namis Terrain. -->

*Versionsstatus: v1 — Vollständige Akt-Struktur, alle drei Fraktionsquests skizziert, drei Nebenquests ausgearbeitet, Ablehn-Option systemisch integriert. Dialog-Ausarbeitung und Nami-Kollaboration folgen in v2.*

\clearpage

# GDD Kapitel 04 — Schlüsselfiguren & NPCs

<!-- Version 2 — Tag 3, Mittwoch -->
<!-- Änderungen gegenüber v1: "Schwellenanker" als offizieller Relikt-Name gesetzt, Ablehn-Option eingebaut, Autor-Metadaten und Post-It-Verweise in HTML-Kommentare verschoben, Fragment-Szene ausformuliert -->

---

## Strukturprinzip

Figuren werden nicht von innen nach außen beschrieben. Die Stimme kommt zuerst, dann die Funktion. Ein NPC ohne eigene Stimme hat kein Recht auf Existenz im Spiel.

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

**Das epistemische Prinzip:** Der Fremde lernt die Welt durch Missverständnisse. Ein Gildenmeister, der ihm die Hand schüttelt, hat gerade eine Verpflichtung eingefordert — der Fremde weiß das nicht, noch nicht. Ein Ordensbote, der "ehrenwert" sagt, meint "gebunden." Die Krone bittet nicht — sie erwartet. Der Spieler lernt das langsam. Zu langsam, manchmal.

**Schattenfieber-Status:** Stufe 1 (Rauschen) ab Minute fünfzehn des Spiels. Nach dem Fragment. Das Rauschen gehört zum Charakter — er soll es erst sehr viel später als Symptom erkennen, wenn überhaupt.

**Visuelle Leitlinie:** Keine definierte Silhouette. Keine festgelegte Körperhaltung. Die Ausrüstung zu Beginn ist Unterschicht — Eisen, ungefärbtes Leinen, aufgearbeitetes Leder. Das wird sich verändern, aber das erste Bild muss das sein.

---

## 4.2 Der Sterbende — Intro-NPC

**In-World-Name:** Hieronymus Vael
**Funktion:** Intro-Sequenz, Quest-Auslöser, erster Schattenfieber-Spiegel

### Wer er ist

Hieronymus Vael war Bote. Nicht Krone, nicht Orden, nicht Gilden — er war **freier Bote**, einer der wenigen, die zwischen allen Lagern liefen, weil alle Lager solche Leute brauchen. Er wusste zu viel von zu vielen. Und er hat etwas transportiert, das er nicht hätte transportieren sollen: die Scherbe des Schwellenankers. Jetzt stirbt er daran. Stufe 3 des Schattenfiebers — die Schwelle — und er weiß, dass er nicht zurückkommt.

Er ist ca. fünfzig Jahre alt, sieht achtzig aus. Die Haut an seinen Händen ist dünn geworden wie Papier, darunter laufen Muster, die aussehen wie tinte-eingeschriebene Adern, aber dunkler. Er riecht nach Erde. Sein Atem geht in kurzen Stößen.

Er liegt am Stadtrand, im Gras zwischen zwei ausrangierten Karrengeleisen. Es ist früher Morgen. Nebel. Er hat sich hierhin geschleppt, weil er wusste: die Stadt war nicht sicher. Nicht mit dem, was er trägt.

### Was er vom Fremden will

Explizit: Dass der Fremde die Scherbe nimmt. Dass jemand anderes weiterlebt, wenn er nicht mehr kann.

Versteckt: Absolution. Hieronymus hat jemandem vertraut, dem er nicht hätte vertrauen dürfen. Das Stück Schwellenanker war ein Auftrag — bezahlt, legal, professionell. Aber er hat die Fragen nicht gestellt, die er hätte stellen sollen. Er stirbt nicht nur an der Scherbe. Er stirbt an seiner eigenen Bequemlichkeit. Der Fremde ist nicht sein Retter. Er ist Hieronymus' letzter Zeuge.

### Was er nie zugeben würde

Dass er weiß, wer den Auftrag gegeben hat. Er weiß es. Er sagt es nicht, weil er Angst hat, dass dieses Wissen den Fremden umbringt, bevor er überhaupt angefangen hat. Vielleicht. Oder weil er sich schämt.

### Seine Stimme

Hieronymus spricht in kurzen Sätzen. Er hat keine Energie für lange Erklärungen. Aber er ist kein Rätsel-NPC — er versucht zu erklären, scheitert aber an Zeit und Atem. Die Lücken in seinem Sprechen sind keine Absicht, sondern Erschöpfung.

**Charakteristischer Satz:**

> "Nimm das. Geh nicht zurück, wo du herkamst — dort kennen sie deinen Weg. Versteh das nicht als Warnung. Versteh das als das Einzige, was ich dir noch geben kann."

Er sagt "Versteh das" zweimal. Das ist sein Muster — er hat sein Leben damit verbracht, sicherzugehen, dass Botschaften ankommen. Auch jetzt noch.

### Spielerrelevanz

Die Fragment-Übergabe — die Scherbe des Schwellenankers — ist der **Clip-Moment**. Sie muss in den ersten fünfzehn Minuten passieren.

Kurz danach erscheinen die drei Fraktionsboten. Dass der Fremde die Scherbe hat, ist entweder schon bekannt — oder wird innerhalb von Minuten bekannt. Das ist die erste narrative Frage: Wie?

Der Spieler kann Hieronymus nach seinem Tod durchsuchen. Er findet wenig: ein zerrissenes Pergamentstück mit drei Siegeln (Krone, Orden, Gilden — alle drei, was unmöglich sein sollte). Das ist eine Spur, die erst viel später aufgelöst wird.

**Unreliable-Narrator-Moment:** In Stufe 2 (Risse) erinnert sich der Spieler an die Begegnung mit Hieronymus. Was er "erinnert," stimmt nicht exakt mit dem überein, was passiert ist. Kleiner Unterschied — Hieronymus hat etwas gesagt oder nicht gesagt. Der Spieler weiß nicht, welche Version wahr ist.

### Dramatischer Wendepunkt

Hieronymus stirbt in den ersten zwanzig Minuten. Aber: Wenn der Spieler im späteren Spielverlauf herausfindet, wer den Auftrag gegeben hat, verändert das die Erinnerung an diesen ersten Moment. Hieronymus wird rückwirkend komplizierter. Das ist sein Wendepunkt — post-mortem.

---

## 4.3 Die Ablehn-Option — Wenn der Spieler das Fragment verweigert

<!-- Neu in v2 — eingebaut nach CD-Entscheid: Spieler DARF ablehnen -->

Dies ist kein Nebenpfad. Es ist eine vollwertige Möglichkeit mit eigener narrativer Logik.

### Was passiert

Hieronymus hält die Scherbe des Schwellenankers aus. Sein letzter Atemzug ist fast aufgebraucht. Der Spieler hat eine Dialogoption: **Das Fragment nicht nehmen.**

Wenn der Spieler ablehnt, sagt der Fremde nichts oder etwas Kurzes — "Das gehört mir nicht" oder Schweigen, je nach Spielervariante. Hieronymus versteht es. Er legt die Scherbe ins Gras neben sich. Er stirbt. Die Scherbe liegt da.

Zwanzig Sekunden vergehen. Der Spieler steht daneben. Die Schatten verhalten sich falsch für einen Moment — aber es passiert dem Spieler nicht, weil er das Fragment nicht berührt hat. Es passiert trotzdem. Das Schwellensubstrat ist schon in der Luft, in der Erde, im Nebel. Der Clip-Moment ist leiser, aber er ist da.

Dann erscheint eine Gestalt. Einer der drei Fraktionsboten — nicht der, der offiziell geschickt wurde, sondern ein Zweiter, der im Hintergrund gewartet hat. Er nimmt die Scherbe. Er geht. Der Spieler hat jetzt kein Fragment und einen Toten und drei Fraktionsboten, die auf ihn warten.

### Konsequenzen

**Sofort:** Der Spieler beginnt das Spiel ohne die Scherbe. Er ist kein Fragment-Träger — er ist Zeuge. Das verändert, wie die Fraktionen ihn einschätzen: nicht als Gefahr, sondern als Ressource. Als jemanden, der weiß, wo die Scherbe zuletzt war.

**Kurzfristig:** Die drei Boten behandeln den Spieler anders. Er wird nicht umworben — er wird befragt. Das erste Fraktionsgespräch ist kein Angebot, sondern ein Verhör. Jede Fraktion will wissen, was er gesehen hat.

**Mittelfristig:** Der Spieler muss das Fragment aufspüren, um Zugang zum Hauptquest zu bekommen. Der Weg ist länger. Er durchquert mehr der Stadt, bevor der erste Act beginnt. Das ist eine vertiefte Tutorial-Phase — er sieht mehr von Schwarzrand, lernt mehr über die Fraktionen, bevor die Haupthandlung ihn einholt.

**Die Schattenfieber-Frage:** Wer das Fragment nicht nimmt, bekommt trotzdem Schattenfieber. Langsamer. Aus der Umgebung, nicht aus dem direkten Kontakt. Stufe 1 beginnt nicht in Minute fünfzehn, sondern irgendwann in der ersten Spielstunde — unmerklich, ohne Clip-Moment, ohne Ankerpunkt. Der Spieler erkennt es nicht als Moment. Das ist die härtere Version.

### Emotionale Signatur

Die Ablehn-Option verändert die moralische Grundmelodie des Spielbeginns. Der Standard-Pfad sagt: *Ich wurde in etwas hineingezogen.* Die Ablehn-Option sagt: *Ich habe mich entschieden, mich nicht einzumischen — und bin trotzdem drin.*

Das ist kein Gewissen. Das ist Konsequenz. Das Spiel wertet nicht. Weder Pfad ist besser oder schlechter. Aber die emotionale Textur ist verschieden, und die Figuren, die der Spieler im ersten Act trifft, spiegeln das wider.

Hieronymus Vael stirbt auf beiden Pfaden. Auf dem Standard-Pfad ist der Fremde sein letzter Empfänger. Auf dem Ablehn-Pfad ist er sein letzter Zeuge — was in mancher Hinsicht das Schwerere ist.

---

## 4.4 Fraktionsvertreter — Schlüssel-NPCs

*Je ein Hauptkontakt pro Fraktion. Kein Gut/Böse. Jede Figur hat einen sympathischen Einstiegspunkt und einen Moment der Kompliziertheit.*

---

### 4.4.1 Krone — Marschall Adelhaid Brenn

**Funktion:** Erster Kontakt zur Krone, Militärbehörde, potenzielle Auftraggeberin in Act 1

#### Wer sie ist

Adelhaid Brenn ist fünfundvierzig. Sie hat dreiundzwanzig Jahre in der Kronarmee gedient, davon acht als Marschall der Stadtgarnison. Sie trägt Tiegelstahl-Rüstung, gebürstet, ohne Verzierung — nicht aus Bescheidenheit, sondern weil Verzierungen im Nahkampf Angriffspunkte sind. Sie ist die Person, die den Schwellenanker als erste offiziell zur Kenntnis nimmt: Sie kennt den Namen Hieronymus Vael, und sie wollte ihn vor drei Tagen befragen.

Sie ist kein Schurke. Sie ist jemand, der Ordnung aufrechterhalten hat, weil Ordnung das Einzige ist, das die Schwächsten schützt. Wenn die Krone fällt, fallen zuerst die Menschen in den untersten Stadtschichten. Das glaubt sie. Das hat sie gesehen.

#### Was sie vom Fremden will

Explizit: Die Scherbe des Schwellenankers. Wenn sie den Fremden nicht überzeugen kann, sie freiwillig abzugeben, dann zumindest seine Zusammenarbeit.

Versteckt: Einen Vorwand, um das Schattenfieber-Problem zu lösen, ohne dass ihre Vorgesetzten wissen, dass es ein Problem gibt. Die Garnison verliert Soldaten — Schattenfieber-Exposition in den Unterkanal-Bereichen der Stadt. Sie hat es bisher nicht gemeldet, weil ein offizieller Bericht eine Quarantäne bedeuten würde, und eine Quarantäne bedeutet, dass die Kaufleute der Gilden sich beschweren, und dann greift der Gildenrat ein, und dann hat sie plötzlich Gilden-Aufseher in ihrer Kaserne. Das will sie nicht.

#### Was sie nie zugeben würde

Dass die Krone — nicht nur lokale Garnison, sondern die Kronbehörde selbst — den Schwellenanker seit Jahren kennt. Nicht das Fragment. Das Original. Und dass sie aus dieser Kenntnis nie eine Pflicht abgeleitet hat, die ihr unbequem gewesen wäre. Sie weiß nicht, was der Schwellenanker *ist* — aber sie weiß, dass Akten darüber existieren, die sie nicht lesen durfte.

#### Ihre Stimme

Brenn spricht direkt und ohne Umwege. Sie sagt nie "vielleicht," sie sagt "es wäre denkbar." Sie sagt nie "ich weiß nicht," sie sagt "das ist noch nicht ermittelt." Bürokratische Sprache als Selbstschutz, nicht als Täuschung. Sie ist kein Lügner — sie ist jemand, dem Präzision wichtiger ist als Ehrlichkeit.

Sie fragt viele Gegenfragen. Nicht als Verhörtaktik, sondern weil sie keine Entscheidung trifft, die sie nicht vollständig versteht.

**Charakteristischer Satz:**

> "Ich bitte Sie nicht, mir zu vertrauen. Das wäre unvernünftig. Ich bitte Sie, die Konsequenzen der Alternative zu verstehen."

#### Spielerrelevanz

**Boten-Szene:** Brenns Bote erscheint als einer der drei Boten nach Hieronymus' Tod. Er ist höflich, uniformiert, unauffällig — und hartnäckig.

**Fraktions-Aufnahme:** Der Spieler kann sich Brenn und der Krone anschließen. Sie bietet Unterkunft in der Kaserne, Zugang zu Kronpassagen, und Ausrüstung aus Kronbeständen.

**Schattenfieber-Reaktion der Krone:** Unterdrückung. Das Schattenfieber ist ein militärisches Problem. Man löst es wie ein militärisches Problem. Schweigen, Eindämmen, Kontrollieren.

**Moral-Komplikation:** Im mittleren Spielverlauf stellt der Spieler fest, dass Brenn einen Unterkanal-Bereich hat sperren lassen — mit Menschen drin. Schattenfieber-Exposition. Sie nennt es "kontrollierte Quarantäne." Es sind vierzig Menschen. Siebzehn sind gestorben.

**Ablehn-Option-Variante:** Wenn der Spieler das Fragment nicht genommen hat, ist Brenns Bote der, der es aufhebt. Das macht Brenn zur frühen Besitzerin der Scherbe — sie ist im Vorteil, will aber noch immer den Zeugen. Der erste Kontakt ist ein Verhör, kein Angebot.

#### Dramatischer Wendepunkt

Brenn erfährt, was der Schwellenanker wirklich ist — ein Schwellen-Stabilisator, der die Grenze in der Gleichgewicht hält. Wenn sie das versteht, zieht sie sofort die politische Konsequenz: Wenn der Schwellenanker die Schwelle stabilisiert, und die Schwelle ist das, was das Schattenfieber kontrolliert, dann ist der Schwellenanker eine Waffe. Eine, die die Krone besitzen muss. Nicht aus Bosheit. Aus militärischer Logik. Das ist der Moment, in dem sie aufhört, eine Verbündete zu sein und anfängt, ein Hindernis zu werden — ohne dass sie sich verändert hat.

---

### 4.4.2 Orden — Bruder Ivo Scherer

**Funktion:** Erster Kontakt zum Orden, Deutungs-Instanz, Informationsbroker (mit Preis)

#### Wer er ist

Ivo Scherer ist zweiunddreißig. Er sieht jünger aus und weiß das — er nutzt es. Er ist kein hoher Ordensmann, er ist Mittelrang: ein Forschungsbruder mit Archivzugang und genug Bildung, um gefährlich zu sein, aber zu wenig hierarchischen Status, um unangreifbar zu sein. Das macht ihn interessant. Er ist klug genug, den Machtspielern im Orden zu helfen, ohne je selbst einer zu werden. Das nennt er Demut. Es ist Selbstschutz.

Er trägt schwarze Ordensgewänder mit einem einzelnen indigofarbenen Ordenssiegel. Die Hände sind tintenbeschmiert. Er lächelt oft — aber das Lächeln erreicht die Augen nur, wenn er etwas Interessantes hört.

#### Was er vom Fremden will

Explizit: Das Fragment zu untersuchen. Nicht zu besitzen — er ist clever genug, diese Formulierung zu wählen. Er will Zugang, nicht Kontrolle. Vorerst.

Versteckt: Wissen, das er monopolisieren kann. Der Orden hat ein Bildungsmonopol, aber das Bildungsmonopol funktioniert nur, solange der Orden weiß, was andere nicht wissen. Ein Schwellenanker-Fragment, das auftaucht und kursiert? Das ist eine Wissenslücke. Lücken machen ihn nervös.

#### Was er nie zugeben würde

Dass er einen Ur-Text über den Schwellenanker gesehen hat. Fragmentarisch, unvollständig — aber er hat ihn gesehen, vor drei Jahren, in den Archivuntergeschossen, und er hat ihn nicht gemeldet. Er hat ihn kopiert. Die Kopie liegt in seinem Quartier. Er weiß, dass der Orden das als Häresie behandeln würde, nicht weil der Text ketzerisch ist, sondern weil nicht-gemeldete Archivauffunde Amtsverluste bedeuten.

#### Seine Stimme

Scherer spricht in langen, präzisen Sätzen mit Zwischensätzen, die immer etwas sagen, das er direkt nicht sagen möchte. Er stellt Fragen, die Aussagen sind. Er wiederholt Formulierungen des Gesprächspartners, leicht verändert — "Sie sagten, er drückte Ihnen etwas in die Hand. *Drückte.* Das ist ein Wort mit Druck dahinter."

**Charakteristischer Satz:**

> "Was Sie da beschreiben, ist entweder sehr gefährlich oder sehr wichtig. In meiner Erfahrung ist es meistens beides. Ich frage mich, ob Sie den Unterschied erkennen, wann die eine Eigenschaft in die andere kippt."

#### Spielerrelevanz

**Boten-Szene:** Scherers Kontaktmann — kein uniformierter Bote, ein zivil gekleideter junger Mann, der aussieht wie ein Kaufmannslehrling — spricht den Fremden unauffällig an. Er übergibt ein versiegeltes Briefchen mit einer Adresse.

**Fraktions-Aufnahme:** Der Orden bietet Zugang zum Archiv (Fertigkeitsbücher, Upgrade-Pfade), Unterkunft in einem Ordenshaus, und Scherers persönliche Deutungsleistung.

**Schattenfieber-Reaktion des Ordens:** Deutungshoheit. Der Orden sagt nicht, was das Schattenfieber *ist* — er sagt, was es *bedeutet*. Das ist eine Theologie-Aussage, keine Medizin-Aussage. Wer nicht unter Ordensdeutungshoheit lebt, ist ungeschützt.

**Informationsbroker-Mechanik:** Scherer ist der NPC, über den der Spieler am meisten über die Weltgeschichte erfährt. Aber jede Information hat einen Preis — nicht notwendigerweise Geld. Manchmal eine Gunst.

#### Dramatischer Wendepunkt

Scherer zeigt dem Spieler (unter bestimmten Bedingungen) seinen Ur-Text-Fragmentfund. Das ist sein letztes Vertrauens-Kapital. Aber: Der Spieler kann in diesem Moment sehen, dass die Kopie unvollständig ist — und dass die fehlenden Stellen genau das sind, was erklärt, wie man den Schwellenanker *zerstört.* Scherer hat das nicht kopiert. Vielleicht aus Vergessen. Vielleicht nicht.

---

### 4.4.3 Gilden — Gildenmeisterin Vreni Kast

**Funktion:** Erster Kontakt zu den Gilden, Wirtschaftsmacht, Vermittlerin und Händlerin

#### Wer sie ist

Vreni Kast ist zweiundfünfzig. Sie ist Meisterin der Glasmacher-Gilde — optische Instrumente, Alchemie-Phiolen, Bergkristall-Linsen. Das ist nicht die größte Gilde, aber es ist eine der technologisch avanciertesten. Glasmacher sehen, was andere nicht sehen — buchstäblich und im übertragenen Sinn. Sie ist kurz, unscheinbar, trägt immer eine Lupe an einer Kette. Ihre Hände sind vernarbt von Jahrzehnten an Werkbänken.

Sie hat aus einer Handwerkerfamilie ohne Gildenstatus in den Gildenrat aufgestiegen. Das war nicht Glück. Das war dreißig Jahre kalkuliertes Handeln.

#### Was sie vom Fremden will

Explizit: Das Fragment analysieren. Sie formuliert es als Angebot — Dienstleistungen und Information im Tausch für Zugang. Kein Besitz. Analyse.

Versteckt: Zu verstehen, was der Schwellenanker von sich abstrahlt. Scherers Orden hat Deutungshoheit über das Nicht-Messbare. Die Gilden wollen das Messbare — und wenn etwas mit dem Fragment passiert, das messbar ist, will Kast das erste Messinstrument sein, das es misst.

#### Was sie nie zugeben würde

Dass die Glasmacher-Gilde bereits seit zwei Generationen versucht, das Schattenfieber zu synthetisieren. Nicht heilen — synthetisieren. Als Rohstoff. Die Experimente haben keine Überlebenden hinterlassen. Die Überreste liegen im untersten Kellergeschoss des Gildenhauses. Sie nennt es intern "das Destillationsarchiv." Es riecht dort nach verbranntem Haar und etwas Süßlichem.

#### Ihre Stimme

Kast redet schnell, präzise, und lässt dem Gesprächspartner keine Zeit zum Innehalten. Sie gibt viele Informationen, bevor der andere eine Frage stellen kann — das ist keine Offenheit, das ist Überflutung. Wen sie mag, gibt sie Spitznamen. Wen sie nicht mag, nennt sie "Kollege."

Sie macht sich selten Sorgen. Wenn sie sich doch Sorgen macht, beginnt sie Sätze mit "Das ist interessant" — was das Gegenteil von dem ist, was sie meint.

**Charakteristischer Satz:**

> "Sie halten das gerade in der Hand und wissen nicht, was es ist. Das ist die unangenehmste Position, in der man sich befinden kann — wertvolles Unwissen. Ich kann das ändern. Nicht umsonst, natürlich. Aber ich glaube, wir werden uns einig."

#### Spielerrelevanz

**Boten-Szene:** Kast schickt keinen Boten. Sie wartet. Sie weiß, dass der Fremde in die Unterstadt muss — und dort kontrollieren die Gilden die Märkte. Der erste Kontakt ist zufällig inszeniert, aber nicht zufällig.

**Fraktions-Aufnahme:** Die Gilden bieten Zugang zu Materialien (bessere Ausrüstung, Alchemie-Rezepturen), ein Handelsnetz das Informationen liefert, und Geld. Direkter als Krone und Orden.

**Schattenfieber-Reaktion der Gilden:** Verwertung. Das Schattenfieber ist kein Feind — es ist ein unkontrolliertes Potenzial. Die Gilden wollen es kontrollierbar machen.

**Handels-Mechanik:** Vreni Kast ist der NPC, über den Spieler Zugang zu Nicht-Standard-Ausrüstung bekommen. Viele ihrer besten Angebote sind mit Bedingungen verknüpft, die erst später relevant werden.

#### Dramatischer Wendepunkt

Der Spieler entdeckt das Destillationsarchiv. Das ist Kasts Point of No Return — nicht für die Spielfigur, sondern für den Spieler: Er muss entscheiden, ob das, was er über Kast weiß, ändert, was er bereit ist, mit ihr zu tun. Kast selbst verteidigt das Archiv nicht moralisch. Sie sagt: "Das waren Freiwillige. Das Schattenfieber hätte sie trotzdem getötet." Das kann wahr sein. Das ändert nichts daran, was das Archiv ist.

---

## 4.5 Tiervolk — Salva

**Funktion:** Informationsbroker, Händler, Verbindung zur Unterstadt und zu Netzwerken außerhalb der Fraktionen

<!-- Tiervolk-Eigenname für Salva ist noch Platzhalter — wartet auf Namenssystem-Input -->

### Eine Vorbemerkung zum Tiervolk

Das Tiervolk ist kein Volk. "Tiervolk" ist ein abwertender Begriff der Stadtbevölkerung für eine lose Gemeinschaft von Händlern und Informationsmaklern, die teilweise Merkmale aufweisen, die die Stadtbevölkerung als "tierisch" bezeichnet: Schuppenhaut, längere Gliedmaßen, Pupillen in anderen Formen, Geruchswahrnehmung, die über menschliche Norm geht. Das ist kein übernatürliches Merkmal. Es ist eine Anpassung — Generationen von Exposition an bestimmte Materialien und Umgebungen in bestimmten Regionen, deren Genaues nicht bekannt ist.

Sie nennen sich intern "die Reisenden." Das Wort Tiervolk benutzen sie für sich selbst nicht. Wer es ihnen gegenüber benutzt, bekommt höflich einen doppelten Preis.

Die Reisenden verkaufen, was andere nicht verkaufen, wissen, was andere nicht wissen, und bewegen sich in Räumen, die für die drei Fraktionen unsichtbar sind.

### Wer Salva ist

Salva ist zwischen dreißig und fünfzig — das ist schwer zu sagen, und er gibt keine Auskunft darüber. Er ist Informationsbroker und Kontaktvermittler. Er hat keine Gilde-Mitgliedschaft, keine Kronen-Akkreditierung, keinen Ordensstatus. Er hat ein Netz aus Kontakten, das alle drei Fraktionen umspannt — ohne dass irgendjemand von den anderen weiß, dass er auch für sie arbeitet.

Er hat schuppige Haut um die Schläfen und Handgelenke, einen länglichen Hals, Pupillen, die sich im Dunkeln weiten wie die eines Katers. Er trägt immer etwas Gestohlenes aus der Oberschicht — eine Faser Brokatseide als Tuchstreifen, eine einzelne Lapislazuli-Applikation an seiner Jacke. Das ist keine Zurschaustellung. Das ist Kompass: wo der Wert ist, war Salva zuerst.

### Was er vom Fremden will

Explizit: Einen Kunden, der zahlt. Der Fremde ist neu, schuldet niemandem etwas, kennt keine lokalen Regeln. Das ist eine ideale Ausgangslage für jemanden, der Informationen verkauft.

Versteckt: Schutz. Salva ist in einer gefährlichen Position. Alle drei Fraktionen dulden die Reisenden, weil sie nützlich sind — aber "dulden" ist kein Status, der anhält. Der Fremde, der keine Fraktion hat, ist vorübergehend unberührbar. Das ist nützlich.

### Was er nie zugeben würde

Dass er den Schwellenanker schon einmal gesehen hat. Nicht dieses spezifische Fragment — aber etwas Ähnliches, vor Jahren, in einer Handelsroute weit südlich der Stadt. Es kam mit einer Karawane, und die Karawane kam nicht an. Er war das einzige Überlebende. Er hat nie darüber gesprochen, weil er keine Erklärung hat, die nicht verrückt klingt.

### Seine Stimme

Salva redet in Konjunktiven. "Man könnte sagen." "Es wäre denkbar, dass." Er macht nie direkte Behauptungen über heikle Themen — nicht weil er lügt, sondern weil direkte Behauptungen ihn angreifbar machen. Wenn er etwas als Fakt bezeichnet, ist es ein Fakt.

Er macht manchmal eine lange Pause mitten in einem Satz. Nicht für Dramatik — er hört gerade etwas, das andere nicht hören.

**Charakteristischer Satz:**

> "Was Sie in der Hand halten, hat drei verschiedene Preisschilder — je nachdem, wen Sie fragen. Ich rate Ihnen, nicht alle drei zu fragen. Nicht gleichzeitig."

### Spielerrelevanz

- Salva ist der NPC, der dem Fremden am frühesten erklärt, wie die Stadt *wirklich* funktioniert — nicht die offizielle Version.
- Er ist kein Quest-Geber. Er ist ein **Kontext-Lieferant**. Die Informationen, die er verkauft, verändern nicht den Verlauf von Quests, sondern wie der Spieler sie versteht.
- Er reagiert auf Fraktionswahl: Wenn der Spieler einer Fraktion beitritt, wird Salva vorsichtiger. Nicht feindlich — vorsichtiger.
- **Schattenfieber-Status:** Salva hat Exposition — nicht Krankheit, aber Nähe. Die Reisenden, die in bestimmten Unterstadt-Bereichen handeln, kommen regelmäßig in Kontakt mit Schwellenbereichen.
- Er ist der einzige NPC, der den Fremden beim ersten Treffen beim korrekten Namen nennt — obwohl der Fremde ihn ihm nicht gesagt hat. Das ist ein Rätsel, das das Spiel nicht auflöst.

**Ablehn-Option-Variante:** Wenn der Spieler das Fragment nicht genommen hat, weiß Salva es — er war dort. Im Hintergrund, unsichtbar. "Ich habe gesehen, was Sie getan haben. Das war ungewöhnlich." Er verlangt nichts dafür. Noch nicht.

### Dramatischer Wendepunkt

Salva verschwindet für eine längere Spielperiode. Wenn er zurückkommt, sieht er verändert aus — nicht dramatisch, aber die Schuppenhaut hat sich ausgebreitet, sein Geruch ist anders. Er spricht nicht darüber. Wenn der Spieler fragt, sagt er: "Das ist irrelevant. Was ich gefunden habe, ist das Gegenteil."

Was er gefunden hat: den Ursprungsort des Fragments. Er gibt diese Information gegen einen sehr hohen Preis weiter.

---

## 4.6 Fraktionskosmologien — Narrative Grundlage

<!-- Dieser Abschnitt wurde von den WBB-Ethos-Notizen in das GDD überführt, da er die NPC-Stimmen direkt bedingt -->

### Die drei Schöpfungserzählungen als Unreliable Narrators auf Weltebene

Der Orden hat einen **kanonischen Text**: die Ordensgenesis. Eine göttliche Ordnung hat die Welt erschaffen und die Schwelle als Schutzwall gesetzt. Das Schattenfieber ist der Beweis, dass der Schutzwall durchbrochen wurde — durch menschliche Überheblichkeit. Der Orden ist der Hüter dieses Wissens.

**Was der Orden verschweigt:** Der Ur-Text, aus dem die Ordensgenesis abgeleitet ist, beschreibt die Schwelle nicht als Schutzwall. Er beschreibt sie als Membran — etwas, das in beide Richtungen durchlässig ist, von Natur aus. Das Schattenfieber ist nicht Strafe. Es ist Kontakt. Der Orden hat diese Lesart unterdrückt, weil sie die Deutungshoheit aufhebt.

Die Krone hat **keine systematische Kosmologie** — das ist ihr ehrlichstes Merkmal. Das Schattenfieber ist ein Feind wie andere Feinde — man bekämpft es, man kontrolliert es, man berichtet es nicht weiter, wenn der Bericht mehr Schaden anrichtet als das Schweigen.

**Was die Krone nicht weiß:** Es gibt im Kronarchiv Berichte über den Schwellenanker, die älter sind als die Stadt selbst. Das Kronarchiv weiß es. Die Menschen, die das Archiv verwalten, wissen, dass sie die Berichte nicht lesen dürfen. Sie wissen nicht, warum.

Die Gilden haben eine **Gründungschronik**: Wissen ist Arbeit. Material ist Wissen. Das Schattenfieber ist ein Material-Problem mit einer Material-Lösung.

**Was die Gilden nicht sagen:** Die Destillationsversuche der Glasmacher haben etwas Reproduzierbares ergeben. Ein Extrakt. Er stabilisiert Schattenfieber-Opfer in Stufe 1 — kurz. Danach beschleunigt er die Progression dramatisch. Die Gilden haben diese Information als nicht-brauchbar klassifiziert. Nicht als gefährlich. Als nicht-brauchbar.

### Das Tiervolk — eine vierte Kosmologie

Die Reisenden glauben, dass das Schattenfieber kein Durchsickern ist. Es ist eine **Kommunikation**. Etwas jenseits der Schwelle kommuniziert. Das, was wir Schattenfieber nennen, sind die Empfänger dieser Kommunikation — Körper, die versuchen, in einer Sprache zu antworten, die sie nicht sprechen können.

Kein NPC im Spiel bestätigt das. Kein Text widerlegt es.

---

## 4.7 Quest-Skizzen

### Intro-Quest: "Was er in der Hand hielt"

**Trigger:** Spieler betritt die Spielwelt. Früher Morgen, Stadtrand von Schwarzrand, Nebel.
**Einstieg:** Hieronymus Vael stirbt. Übergabe der Scherbe des Schwellenankers. Drei Boten erscheinen innerhalb von Minuten.
**Erste Entscheidung:** Zu welchem Boten geht der Spieler zuerst?

Dies ist keine Moral-Entscheidung. Der Spieler kennt die Fraktionen noch nicht. Er geht zu dem Boten, dessen Angebot sich zuerst richtig anfühlt. Die Welt merkt es sich.

**Struktur:**

- Beat 1 — Hieronymus. Die Übergabe der Schwellenanker-Scherbe. Das Rauschen beginnt (Schattenfieber Stufe 1, kaum wahrnehmbar).
- Beat 2 — Die drei Boten. Kurze Kontakte. Keine Entscheidung nötig — alle drei geben Adressen. Aber wer der erste Besuch ist, prägt die Eröffnungssequenz.
- Beat 3 — Erste Adresse. Der Spieler betritt die Stadt zum ersten Mal richtig. Er bemerkt die Schichtung. Er hat keine Ahnung, wo er steht.

**Clip-Moment:** Die Fragment-Übergabe. Hieronymus' letzter Satz. Das erste Rauschen — eine Sekunde lang sind die Schatten nicht dort, wo sie sein sollten.

**Ablehn-Variante:**

- Beat 1 — Hieronymus. Der Spieler weigert sich. Die Scherbe liegt im Gras.
- Beat 1b — Ein Fraktionsbote nimmt die Scherbe. Der Clip-Moment passiert trotzdem, gedämpft.
- Beat 2 — Die drei Boten behandeln den Spieler als Zeugen, nicht als Fragment-Träger. Erster Kontakt ist Verhör.
- Beat 3 — Der Spieler muss das Fragment aufspüren, bevor der Hauptquest-Strang beginnt.

---

### Hauptquest-Strang: "Der Schwellenanker"

Die zentrale Frage des Hauptquests: **War ich immer hier, oder hat der Schwellenanker mich gerufen?**

Diese Frage wird nie direkt beantwortet. Das ist keine Schwäche der Story, das ist die Story.

**Act 1 — Die Scherbe:** Der Spieler hat ein Stück von etwas, das viele wollen und keiner versteht. Die drei Fraktionen wollen es aus unterschiedlichen Gründen. Salva will es für Geld. Der Spieler beginnt, Schwarzrand zu verstehen.

**Act 2 — Das Muster:** Die Scherbe ist nicht einzigartig. Es gibt andere. Hinweise darauf, dass der Schwellenanker in Stücke zerbrochen wurde — wann, durch wen, warum. Die Fraktionen haben unterschiedliche Stücke. Oder wissen, wo die anderen sind. Der Spieler navigiert ein Netz aus Halbwahrheiten.

**Act 3 — Die Schwelle:** Der Spieler erreicht den Ursprungsort — die Wurzelkammer in den Tiefen von Schwarzrand. Was er dort findet, hängt von seinen Entscheidungen ab. Der Schwellenanker stabilisiert die Schwelle. Wenn er zerstört wird, öffnet sich die Schwelle weiter. Wenn er erhalten wird, bleibt das Schattenfieber kontrollierbar — aber nichts ändert sich an den Bedingungen, unter denen die Stadt die Schwächsten behandelt.

**Endkonsequenzen (drei Hauptäste, keine eindeutige "richtige" Entscheidung):**

1. Den Schwellenanker der Krone übergeben. Die Schwelle bleibt stabil. Die Krone kontrolliert das Schattenfieber militärisch. Die Stadt überlebt. Die untersten Schichten bleiben, wo sie sind.
2. Den Schwellenanker dem Orden übergeben. Die Schwelle wird durch Ordenswissen verwaltet. Das Schattenfieber wird zur Theologie. Wer nicht unter Ordensdeutungshoheit lebt, ist ungeschützt.
3. Den Schwellenanker niemandem geben. Die Schwelle öffnet sich weiter. Das Schattenfieber eskaliert. Aber etwas kommt durch — und was durchkommt, ist nicht nur Krankheit.

---

## 4.8 Noch offen

<!-- Offene Punkte für interne Koordination -->

- **Fragment-Szene (ausformuliert):** Halbe Seite für Finn/Leo — in diesem Dokument als Beat 1 in Abschnitt 4.7 skizziert. Ausformulierte Sequenz folgt als eigenständiges Szenarien-Dokument.
- **Nebenquest-Ausarbeitung:** "Der Zeuge" (alter Mann in den Slums) und zwei weitere Ideen folgen in v3.
- **Tiervolk-Eigenname für Salva:** Platzhalter — Namenssystem-Input noch ausstehend.
- **Düsterkeit der Intro-Szene:** CD-Entscheid noch offen. Tonalität der Sterbeszene (kurz/ausgedehnt) beeinflusst Beat 1.

\clearpage

# GDD Kapitel 05 — Visuelle Designsprache & Art Direction

<!-- Vera: v1 | Tag 3, Mittwoch | Konzept Art + Art Direction -->
<!-- Status: Erster Entwurf — vollständige Struktur, alle Abschnitte besetzt. Bilder aus Tag 2 und Tag 3 eingebettet. -->

---

## 5.0 Prämisse: Was diese Welt visuell sagt

RELICS ist kein generisches Mittelalter. Es ist eine Welt, in der **Materialien Macht bedeuten** — und in der das sofort lesbar ist. Wer in welchem Material gekleidet ist, aus welchem Stein sein Haus gebaut wurde, mit welchem Werkzeug er hantiert: das sagt mehr über seinen Platz in der Welt als jeder Dialog.

Die visuelle Aufgabe ist, diese Materialsprache so klar und konsistent umzusetzen, dass ein Spieler nach drei Stunden Spielzeit sofort weiß, wessen Gebiete er betritt — ohne ein einziges Wort zu lesen.

**Leitfrage für jede Design-Entscheidung:**
*Ist das auf 50 Meter lesbar? (Silhouette-Regel, Dark Souls)*

---

## 5.1 Visuelle Vision — Medieval Cyberpunk als Materialsprache

Das Briefing verwendet "Medieval Cyberpunk" als Strukturprinzip, nicht als Ästhetik-Label. Die visuellen Konsequenzen:

| Cyberpunk-Konzept | Visuelle Übersetzung in RELICS |
|---|---|
| Megacorporations | Gildenheraldik in Stein gemeißelt, eisenbeschlagene Gildentore, Zunftzeichen an Fassaden |
| Neon-Ästhetik | Alchemische Laternen mit getöntem Glas, phosphoreszierende Mineralkanäle, Biolumineszenz in Mauerwerk-Fugen |
| Vertikalität | Vier Stadtschichten übereinander — jede Schicht eine eigene Epoche, ein eigener Stil, eine eigene Physik |
| High-Tech, Low-Life | Polierter Damaszener-Stahl oben, gestohlene Eisenreste unten — niemals beschriftet, immer gezeigt |
| Überwachungsstaat | Ordenssiegel auf Torbögen, versiegelte Dokumente, Kapuzenträger an Weggabelungen |
| Augmentierung/Biotech | Alchemische Narbenzeichnungen, Schattenfieber-Gefäßlinien unter der Haut, Knocheneinlagen |

**Was wir NICHT machen:**
- Keine Hexagone in der visuellen Sprache (Briefing-Ausschluss)
- Kein Steampunk (kein Zahnrad, kein Dampf, kein Messing-Übergewicht)
- Kein Anachronismus (kein Schießpulver, kein Buchdruck, keine mechanischen Uhren außer Gilden-Prototypen)

---

## 5.2 Farbpalette & Materialsprache nach Fraktion

Jede Fraktion hat eine eigene Materialsprache, die ihren Platz in der Machtstruktur ausdrückt. Die Paletten sind nicht willkürlich — sie folgen der Logik von Ressourcenkontrolle.

### 5.2.1 Die Krone — Kosmologie des Blutes

Die Krone kontrolliert Militär und Tradition. Ihre Materialsprache ist Einschüchterung durch Perfektion: kein überflüssiges Element, jedes Detail ein Statussymbol.

**Palette:** All-Black / Anthrazit mit EIN Blutrot-Akzent. Kaltes Weißlicht auf poliertem Metall.

**Materialien Oberschicht:**
- Titan-Legierungen und Damaszener-Stahl (gebürstet, nicht poliert)
- Geschliffener Obsidian als Intarsien
- Schwere Brokatseide in Schwarz (Goldfaden nur an Kanten, minimal)
- Kristallglas-Phiolen mit tiefblauem / indigofarbigem Inhalt
- Blutroter Siegellack als einziger Farbakzent

![Krone — Materialpalette: Titanrüstung, Obsidian-Intarsien, Blutrot-Signet, Damaszener-Stahl](../concepts/day02-vera/factions/fraktion-krone-materialpalette_seedream-4-5.png)

<!-- Vera: Krone-Palette freigegeben vom CD. Weißer Hintergrund statt Schwarz (Prompt-Drift), aber Materiallesbarkeit und Akzentfarbe sitzen. Für v0.2 Iteration: Hintergrund auf Schwarzstein anpassen. -->

**Architektur der Krone:**
- Massives Gestein — Stampflehm und Kalkstein in brutalisierten Blöcken
- Keine Ornamentik außer Wappenzeichen
- Cantilevierte Plattformen — Macht durch Ingenieurleistung demonstriert
- Crystal-Glas-Lichtschächte als architektonisches Statement (Licht von oben als Herrschaftssymbol)

**Silhouette-Regel:** Kronensoldaten müssen auf 50m von Ordensboten unterscheidbar sein → Kronenarmour hat breitere Schulterplatten, kürzere Silhouette, kein weißer Stoff sichtbar.

---

### 5.2.2 Der Orden — Kosmologie des Wissens

Der Orden kontrolliert Bildung und Inquisition. Seine Materialsprache ist Reinheit als Drohung: Weiß, das kein Fleck toleriert, ist eine politische Aussage.

**Palette:** All-White / Hellgrau mit EIN blassgrünem Lumineszenz-Akzent. Silberne Präzisions-Details.

**Materialien Oberschicht:**
- Gebleichtes schweres Leinentuch (geometrisch präzise Stickerei, silberner Faden)
- Kristallglas-Optiklinsen in Messingfassungen (Bildungsmonopol visualisiert)
- Vellum-Manuskriptseiten mit dichter Schrift
- Blassgrüne Alchemie-Phiolen (das einzige Farbsignal — Wissen als leuchtendes Gift)
- Knochen-Rosenkranz mit schwarzem Obsidian-Mittelelement (einziger Dunkelakzent)

![Orden — Materialpalette: Weißes Leinengewand, Kristalllinse, Vellum-Manuskript, grüne Alchemiephiole](../concepts/day02-vera/factions/fraktion-orden-materialpalette_seedream-4-5.png)

<!-- Vera: Orden-Palette freigegeben. Das Kreuz-Symbol auf dem Gewand: Modell hat ein christliches Kreuz ergänzt, das nicht gebrieeft war. Lore-Frage an Emre/Nami: Hat der Orden ein Kreuz-Symbol, oder ein anderes Signet? Für v0.2 Iteration klären und Prompt entsprechend anpassen. -->

**Architektur des Ordens:**
- Romanische Elemente: Rundbögen, dicke Mauern, Krypta-Gewölbe
- Helle, geschliffene Kalkstein-Oberflächen (Reinheit durch Material)
- Schmale Schlitzfenster — kontrollierte Lichtmenge als Machtgeste
- Bibliotheken in Turmform — vertikale Wissenshoheit

**Silhouette-Regel:** Ordensboten haben hochgeschlossene schmale Silhouette, weißer Umhang, kein Metall sichtbar. Gegenpol zur massiven Kronen-Armour.

---

### 5.2.3 Die Gilden — Ontologie des Materials

Die Gilden kontrollieren Produktion und Handel. Ihre Materialsprache ist akkumulierter Reichtum: Jedes Objekt hat einen Preis, und der ist signifikant.

**Palette:** Tiefbraun, Warmambber, Mitternachtsindigo, Malachitgrün — mit poliertem Bronze und Gold als Akzente.

**Materialien Mittelschicht/Oberschicht:**
- Schwere Brokatseide in Nachtindigo mit gewebter Gold-Borte
- Polierter Malachit-Cabochon-Anhänger (Handelsstatus-Signal)
- Bernstein-Perlenreihe (organisch, aber wertvoll)
- Bronzehammer auf Dunkelstein (Werkzeug als Statussymbol)
- Vegetabil gegerbtes Sattlerleder mit geometrischen Blindprägungen
- Keramiktiegel mit Kupferpatina, kleine Glasphiolen mit Pigmenten (Produktionskontrolle)

![Gilden — Materialpalette: Indigoseide, Malachit-Anhänger, Bernsteinkette, Bronzewerkzeug, Sattlerleder](../concepts/day03-vera/factions/fraktion-gilden-materialpalette-v2_nano-banana-2.png)

<!-- Vera: Gilden-Palette v2 — kein Text mehr. Nano Banana 2 hat die Materialzusammenstellung sehr gut getroffen: Erdtöne dominant, Malachit und Bernstein als Farbakzente, Bronzehammer als Würdezeichen. Für v0.2: Kontraktbogen mit Wachssiegel expliziter machen (Gilden als Vertragsrechts-Akteur). -->

**Architektur der Gilden:**
- Bauhaus-Inspiration: klare Linien, Funktionalität als Ästhetik
- Integrierte Werkstätten im Erdgeschoss (Produktion als Fassade sichtbar)
- Bronzebeschläge und Metallintarsien an Sandstein-Fassaden
- Zunftzeichen in Stein gemeißelt — Heraldik als Identitätspolitik
- Modulare Fassaden: Erweiterungen wenn Gilde wächst, Schrumpfungen wenn sie fällt

**Silhouette-Regel:** Gildenmeister haben breiten Stand, Lederschürze oder schweres Brokattuch, Werkzeughalter sichtbar. Mittelklasse-Silhouette — nicht so schlank wie Krone, nicht so ärmlich wie Unterschicht.

---

## 5.3 Architektur-Designsprache — Die vier Schichten Schwarzrands

Schwarzrand ist eine gerichtete Stadt. Sie orientiert sich zur Schwelle hin — die Architektur schwillt, lehnt und greift in Richtung des Abgrunds. Das ist kein Fehler der Stadtplanung. Es ist die physische Manifestation einer Zivilisation, die ihre Existenz auf einer kosmologischen Dünnstelle errichtet hat.

![Schwarzrand — Stadtschnitt: Vier Schichten in diagonaler Tiefenperspektive](../concepts/day03-vera/environments/stadtschnitt-schwarzrand-v2_gpt-image-1-5.png)

<!-- Vera: Stadtschnitt v2 — schräge Tiefenperspektive statt frontaler Querschnitt. Das Schwarzrand-Richtungskonzept (alles zeigt zur Schwelle) kommt jetzt durch. Dramatischer als v1. Für WBB Kap 2 (Topos): dieses Bild direkt einbetten als Orientierungsbild für die geographische Beschreibung. Tobi: bitte bei UE5-Aufbau als Referenz nutzen — die diagonale Orientierung ist kein Zufall. -->

### Schicht 1 — Slums (Untergrund, Schwellenähe)

Physik: Schwelle am nächsten. Realität porös. Biolumineszenz überall.

- **Material:** Gestohlene Ziegel, Holzreste, Lappen als Trennwände. Knochen-Schnitzereien.
- **Licht:** Einzige Lichtquelle: biolumineszente organische Ablagerungen in Mörtelfugen — grünlich, schwach, unzuverlässig.
- **Atmosphäre:** Deckenhöhe unter 2 Meter. Tunnel, keine Straßen. Alles riecht nach feuchtem Stein.
- **Bewohner:** Schattenfieber-Opfer, illegale Alchemisten, Schwarzmarkt-Händler, Kinder der Armen.

**Designregel:** Slums dürfen NICHT pittoresk sein. Kein romantisierter Armuts-Aesthetic. Wenn es schön ist, ist es bedrohlich schön — weil die Biolumineszenz das Fieber signalisiert.

### Schicht 2 — Mittelstadt (Fachwerk und Romanik)

Historisches Herzstück: fränkische Fachwerkhäuser über romanischen Kellergewölben.

- **Material:** Fachwerk aus Eiche, Sandstein für Fundamente und Gewölbe. Warmamberfarbenes Talgkerzenlicht.
- **Licht:** Kleine Fenster mit einfachen Glasscheiben (Buntglas nur in Zunfthäusern). Laternen mit Tiertalg.
- **Atmosphäre:** Laut, eng, lebendig. Märktreiben, Werkstattlärm, Stiefelgeräusch auf Kopfsteinpflaster.
- **Hybridzonen:** An den Rändern zu Schicht 3 — Edelstahlbeschläge am Fachwerk, Bauhaus-Fensterrahmen in romanischen Bögen. Die Mittelschicht will aufsteigen und zeigt es.

**Designregel:** Hier ist die meiste spielerische Zeit. Lesbar, lebendig, nicht monoton — jede Gasse hat eine andere Gilde, jede Fassade ist ein anderer Zunftcharakter.

### Schicht 3 — Gilden- und Ordensdistrikte (Brutalistisch/Bauhaus)

Machtarchitektur als Einschüchterung.

- **Material:** Geschlagener Kalkstein und Stampflehm. Geometrische Formen. Metallintarsien in Böden und Fassaden.
- **Licht:** Polierte Oberflächen reflektieren indirektes Licht — nie direkte Flamme. Eiskaltes weißes Licht.
- **Atmosphäre:** Still. Weiträumige Plätze, keine Marktstände. Wachen alle zwanzig Meter.
- **Gildenhallen:** Offen nach vorn (Produktion sichtbar — Macht durch Transparenz). Türme als Signet.
- **Ordensbibliotheken:** Geschlossen, keine Fenster nach unten, schmale Schlitzfenster nach oben.

**Designregel:** Hier wirkt der Spieler klein. Gebäude sind mindestens dreimal menschliche Höhe. Plätze haben keine schützenden Ecken. Das ist beabsichtigt — Kontrollarchitektur.

### Schicht 4 — Kronenfestung (Geometrischer Brutalismus)

Das absolute Oben. Hier endet die Hierarchie.

- **Material:** Reiner geometrischer Stein. Kein Ornament. Cantilevierte Plattformen über dem Abgrund.
- **Licht:** Tageslicht durch Kristallglas-Lichtschächte. Licht als Privilege — je höher, desto mehr Sonne.
- **Atmosphäre:** Windgepeitschte Terrassen. Hängende Gärten am Rand des Nichts. Schweigen.
- **Richtungsgeste:** Die Kronenfestung lehnt am weitesten in Richtung Schwelle. Der König kennt die Gefahr und steht dennoch am nächsten — das ist der Beweis seiner Legitimation.

**Designregel:** Keine natürliche Vegetation außer den Hängegärten. Kein Lärm. Ein Spieler, der hier steht, ist entweder mächtig oder in extremer Gefahr.

---

## 5.4 Charakter-Design-Prinzipien

### Hauptprinzip: Comme des Garçons trifft mittelalterliche Rüstung

Silhouetten sind tailored, körperbetont, geschichtet. Kein Übergewicht an Schmuck. Jedes Detail hat Funktion.

**Schichtung (für alle Charaktere):**
1. Grundlage: Gambeson (Steppstoff) oder einfaches Leinengewand
2. Mittelschicht: Kettenhemd-Segmente oder geschnürtes Leder
3. Außenschicht: Platten-Elemente (nicht vollständig — Beweglichkeit bleibt sichtbar)

**Oberfläche:**
- Gebürstetes Metall, nicht poliert (außer Krone-Eliten: poliert als Statussignal)
- Geätzte Ornamente und Nieten-Muster (nicht dekorativ, sondern Marker)
- Patina an Kanten (Alter und Gebrauch sind Würde)

**Akzente (nach Fraktion):**
- Krone: Blutrot-Email, Goldfaden-Stickerei minimal, schwarzes Brokattuch
- Orden: Silber-Stickerei, Knochendetails, weißes Leinengewebe
- Gilden: Bernstein-Einlagen, Malachit-Applikationen, Lederpunzierungen

**Asymmetrie als Prinzip:** Avant-garde Silhouetten — kein symmetrisches Mittelalterkostüm. Eine Schulter breiter. Eine Seite Kettenhemd, andere Seite Platte. Das ist das "High Fashion"-Signal.

### Tiervolk

Händler und Diebe. Leicht alien vs. menschlich clean. Nicht tribal.

- Federleichte Materialien — Chitin-Applikationen, Beinlamellen aus natürlichen Quellen
- Farben: Nicht die Fraktionspaletten. Eigenständige Erdtöne — sandigeres Braun, gedämpftes Ochre.
- Silhouetten: Schlanker, beweglicher — Diebe-Ästhetik. Kein Plattenrüstungsgewicht.
- Keine Stammesornamentik — der Fehler, der sich von "alien" trennt.

---

## 5.5 Relikt — Der Schwellenanker

### 5.5.1 Formsprache

Der Schwellenanker ist eine **komprimierte gefaltete geologische Formation** — nicht Knochen, nicht Kristall, nicht Werkzeug. Er ist zu regelmäßig für Zufall, zu organisch für Handwerk. Entstanden durch Jahrtausende von Schwelle-Einwirkung auf Mineral.

**Form-Deskription:** Fistgroße Knollen-Masse. Sedimentgestein, das in sich gefaltet und unter extremem Druck komprimiert wurde. Oberfläche: dichtes Netz von osszifizierten Mikro-Kanälen, die durch kalzifizierte organische Matrix verlaufen. Die Kanäle sind das visuelle Key-Feature — sie verraten den Schwellenanker, wenn alles andere ihn als normalen Stein erscheinen lässt.

**Was er NICHT ist:**
- Kein Wirbelsäulenknochen (abgewiesen: Briefing-Entscheidung, kein anatomisches Artefakt)
- Kein Kristall (zu clean, zu ordentlich — Kristall impliziert Wachstum, Schwellenanker impliziert Kompression)
- Kein Schmuckstück (keine Fassung, keine Politur, kein Design-Eingriff)

### 5.5.2 Drei Zustände

Die Dramaturgie des Schwellenankern wird visuell über drei Zustände erzählt. Diese Zustände sind Gameplay-Information — der Spieler lernt, sie zu lesen.

![Schwellenanker — Drei Zustände: Ruhend | Aktiviert | Auflösung](../concepts/day03-vera/relics/relikt-drei-zustaende-v2_nano-banana-pro.png)

<!-- Vera: Dreier-Vergleich v2 — kein Text mehr, geologisch-organische Form (kein Wirbelsäulenreferenz). Die drei Zustände sind klar unterscheidbar durch Materialzustand und Licht. Das Modell hat die Formkonsistenz zwischen den drei Objekten deutlich besser hinbekommen als v1. Für Darius/Kap 2-3: dieses Bild direkt als Mechanik-Illustration nutzen. -->

**Zustand Null — Ruhend:**
Aschgrau. Kein Glanz, kein Licht. Die Mikro-Kanäle sind leer — dunkel, trocken, unremarkable. Auf 10 Meter Entfernung: ein Stein. Nur bei direkter Betrachtung verrät das pathologische Regelmäßigkeit der Kanäle etwas Außergewöhnliches.

*Spieler-Lesbarkeit:* Das Relikt ist inaktiv. Kein Effekt, keine Reaktion, keine Interaktion möglich.

**Zustand Eins — Aktiviert:**
Biolumineszenz von innen. Pale Blue-Violett füllt die Mikro-Kanäle wie phosphoreszierende Flüssigkeit in einem Kreislaufsystem. Der Glanz diffus, von innen heraus — nicht von der Oberfläche. Schön. Tief unsettling.

*Spieler-Lesbarkeit:* Das Relikt resoniert. Schwellenfieber-Empfindlichkeit maximal. Gameplay: besondere Fähigkeiten aktiv, aber Lymph-System unter Belastung.

**Zustand Drei — Auflösung:**
Ränder evaporieren als feines mineralisches Partikelstaub. Inneres Leuchten: überhell und hässlich — übersteuert, kränklich Gelbgrün an den aufbrechenden Kanalrändern. Das Schöne ist weg. Die Formation verliert Kohärenz.

*Spieler-Lesbarkeit:* Kritischer Zustand. Weiterführung verursacht irreversible Schwelle-Kontamination. Abort or continue — das ist die Spielerentscheidung.

### 5.5.3 Hero-Shot

Der Schwellenanker in seiner atmosphärischen Präsentation: auf einem Altar in einem Gewölberaum, als einzige Lichtquelle. Die Spielerfigur am Bildrand, klein, awed.

![Schwellenanker — Hero-Shot: Aktivierter Zustand auf Altar, Gewölberaum](../concepts/day02-vera/relics/relikt-hero-shot-aktiviert_gpt-image-1-5.png)

<!-- Vera: Hero-Shot ist die stärkste cineastische Darstellung. Das Problem: GPT hat eine zu kristalline Form erzeugt — zu clean, zu ordentlich, verliert die organisch-geologische Qualität. Für v0.2: Hero-Shot mit Nano Banana Pro iterieren (bessere Constraint-Adherence für organische Formen). -->

---

## 5.6 Schattenfieber — Visuelle Progression

Das Schattenfieber ist biologisch. Seine visuelle Progression zeigt diesen biologischen Charakter: keine magische Aura, keine Spektral-Effekte, keine leuchtenden Augen. Das Fieber verändert den Körper von innen.

### Stufe 1 — Sensorisch (reversibel)

**Sichtbares Zeichen:** Hauchfeine Blutgefäß-Linien unter der Haut, vor allem an Handgelenken und Halsansatz. Kaum sichtbar — nur bei direktem Licht und naher Distanz.

**Farbe:** Blassviolett, exakt so wie der aktivierte Schwellenanker. Das ist kein Zufall.

**Design-Regel:** In Stufe 1 wirkt der Charakter nicht "krank." Er wirkt interessant. Fast schön. Das ist die Falle.

### Stufe 2 — Mutativ (managebar)

**Sichtbares Zeichen:** Gefäßlinien jetzt deutlich — treten aus der Haut hervor als leicht erhabene Kanäle. Hautton drumherum verschoben (grauer, kühler).

**Biotech-Konsequenz:** In dieser Stufe ist Schattenfieber spielbar. Die Gefäßlinien leiten Energie. Spezialfähigkeiten werden möglich — mit Körperkosten.

**Design-Regel:** Schicht-2-Charaktere mit Schattenfieber sind im Spiel sichtbar. Kein Stigma-Klischee — Fieber ist manchmal Macht. Der moralische Preis ist nicht der Körper, sondern das, was man für den Körper tut.

### Stufe 3 — Auflösung (irreversibel)

**Sichtbares Zeichen:** Material-Transition. Haut wird transluzent. Darunter: die Gefäßlinien leuchten kränklich gelbgrün — identische Farbverschiebung wie Schwellenanker-Zustand-Drei. Die Person evaporiert an den Rändern.

**Design-Regel:** Stufe-3-Charaktere sind selten im Spiel sichtbar. Wenn, dann immer isoliert, immer traurig, nie als Bedrohung. Sie sind Warnung, nicht Monster.

### UI-Korrespondenz

Die Levelingsicht (halbtransparentes Nervensystem — Cardio / Muskel / Lymph) entspricht direkt der Schattenfieber-Visualisierung. Das Lymph-Subsystem leuchtet blassviolett wenn das Fieber aktiv ist. Je stärker das Leuchten, desto näher Stufe 2.

**Warum das funktioniert:** Der Spieler trägt das Schattenfieber-System buchstäblich im Körper. Die Schwelle ist nicht außen. Sie ist innen. Das ist das Gefühl, das RELICS erzeugen soll.

---

## 5.7 Referenz-Kanon

### Primäre Referenzen

**Dark Souls / Elden Ring:**
- Licht aus dem Körper heraus, nicht von oben
- Architektur als emotionaler Raum
- 50-Meter-Silhouette-Regel konsequent angewendet
- Dunkel als Normalzustand (Licht ist Privileg, nicht Default)

**Control (Remedy):**
- Brutalismus als emotionale Raumsprache
- Das Unheimliche durch geometrische Perfektion erzeugen
- Material als Machtträger

**Hollow Knight:**
- Vertikalität als Weltstruktur
- Biolumineszenz in Dunkel als primäre visuelle Sprache
- Größenverhältnisse als emotionale Aussage

**Dishonored:**
- Sozialer Status durch visuelle Schichtung immer sichtbar
- Vertikalität im Level-Design: Dächer als separate Gesellschaft
- Materialsprache für Klassen konsequent getrennt

### Architektur-Referenzen

**Gaudi:** Organisch-strukturelle Formen. Biolumineszenz-Kanäle folgen dieser Logik — Struktur und Ornament sind dasselbe.

**Le Corbusier / Bauhaus:** Gilden-Architektur. Funktion als Ästhetik. Das Werkzeug IS das Design.

**Brutalismus (Smithson, Lasdun):** Krone-Festung und Ordensgebäude. Macht durch Masse. Einschüchterung durch Geometrie.

### Anti-Referenzen (was wir nicht machen)

- **World of Warcraft:** Übergesättigte Farben, lesbares Fraktionssystem durch bunte Plakate. Das Gegenteil von RELICS.
- **Generic Fantasy Stock:** Braune Schmutzoptik ohne Designwillen. RELICS ist Schmutz MIT Designwillen.
- **Steampunk-Ornamentik:** Zahnräder als Dekoration. Bei uns sind Zahnräder, wenn überhaupt vorhanden, versteckt in Mechanismen.

---

## 5.8 Art Direction-Checkliste (für alle Assets)

Jedes Asset (Umgebung, Charakter, UI, Effekt) muss gegen diese Liste geprüft werden:

- [ ] **Fraktion lesbar?** — Welche Fraktion "spricht" dieses Asset? Auch neutrale Assets brauchen eine soziale Verortung.
- [ ] **Schicht lesbar?** — Oberschicht, Mittelschicht oder Unterschicht? Materialien müssen eindeutig sein.
- [ ] **50-Meter-Silhouette?** — Ist das auf Distanz lesbar?
- [ ] **Farbpalette korrekt?** — Dominante Neutralfarbe + maximal EIN kräftiger Akzent.
- [ ] **Keine verbotenen Elemente?** — Kein Hexagon, kein Zahnrad, kein Dampf, kein Sci-Fi-Material.
- [ ] **Materiallogik stimmt?** — Passt das Material zum Wohlstand der Figur/des Ortes?
- [ ] **Schattenfieber berücksichtigt?** — Bei relevanten Charakteren/Orten: Blassviolett-Kanäle sichtbar?
- [ ] **Licht als Privilege?** — Wer hat Zugang zu guter Beleuchtung? Zeigt das Asset das?

---

<!-- Vera: GDD Kap 5 v1 — vollständige Erstfassung. Fehlend für v0.2:
     - Detailliertere Charakter-Konzepte (Krone-Soldat, Ordensbote, Gildenmeister als einzelne Figuren)
     - Hero-Shot des Schwellenankern iterieren (zu kristallin in v1)
     - Stadtschnitt auch in WBB Kap 2 einbetten (Tobi/Emre koordinieren)
     - UI-Designsprache (Leveling-Sicht, Karten-Visualisierung) ist noch nicht abgedeckt — für v0.2
     Frage an Darius: Soll Kap 5 auch die Leveling-UI (Nervensystem-Sicht) visuell spezifizieren, oder ist das Kap 2 (Mechaniken)?
-->

\clearpage

# GDD Kapitel 6: Technische Spezifikation & Produktion

**RELICS: Schwellenanker**

<!-- Tobi: v3-Änderungen gegenüber v2: (1) Interface-Spezifikation Lymph → PP-Trigger als neuer Abschnitt 6.4.7 ergänzt — das war Darius' Blocker, (2) Autorname aus sichtbarem Dokumentkopf in HTML-Kommentar verschoben, (3) "(Nami-Alignment)" und "(Nami)" aus sichtbarem Text entfernt, (4) "Tobi's System" auf neutral umformuliert, (5) Tippfehler "M_SchattenfiebertOverlay" in 6.4.5 korrigiert zu "M_SchattenfiebertOverlay" — nein: korrekter Name ist M_Schattenfieber_Overlay. -->

<!-- Tobi: Verfasser Kap. 6: Tobias Richter, Technical Artist. Datum v1: Tag 2, Dienstag, 10:00 Uhr. -->

---

> **Anmerkung zur Dokumentstruktur**
> Dieses Kapitel ist die technische Antwort auf das kreative Briefing. Jede Entscheidung hier hat einen Grund — und den schreibe ich dazu. Wenn eine Entscheidung keine Begründung hat, gehört sie nicht ins Dokument.

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

*Anmerkung*: Die Minimum-Konfiguration nutzt Lumen im Software-RT-Modus. Das degeneriert GI-Qualität in den Slum-Unterebenen merklich. Akzeptabel — die Unterebenen sind dunkel per Design.

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

Lumen ist das wichtigste und gleichzeitig riskanteste System im Projekt. Die Begründung ist direkt: eine lebendige, biolumineszente Stadt mit phosphoreszierenden Mineralien, Alchemie-Lampen und Schattenfieber-Mutationen braucht echte dynamische GI. Statisches Baked Lighting würde jeden Runtime-Zustandswechsel — das Aktivieren des Schwellenankens, eine Schattenfieber-Eskalation, die Biolumineszenz-Klasse-A-Emitter — optisch inkonsistent machen.

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
| **Layer 0** | Untergrund, Kanal-System, Slum-Keller | Phosphoreszierendes Blau-Grün, vereinzelt Feuerschein | Hoch — subtile PP-Basis-Ambience aktiv |
| **Layer 1** | Straßenebene, Handwerkerviertel, Marktplätze | Warmes Kerzenlicht, Buntglas-Farbflecken aus Obergeschossen | Mittel |
| **Layer 2** | Brücken, Arkaden, niederer Gilden-Bereich | Diffuses Tageslicht durch Bergkristall-Linsen-Streuung | Niedrig |
| **Layer 3** | Türme, Gildenhochbau, Ordensanlagen, Kronenpalast | Klares Tageslicht, Bergkristall-Linsen direkt, Metallic-Reflektionen | Minimal |

*Technische Implementierung:*
- Jeder Data Layer ist eine eigenständige Streaming-Einheit mit eigenem Post-Process-Volume-Stack
- Manuelle Occlusion-Volumes an allen Schicht-Übergängen — Layer 3 cullt aggressiv Layer 0 und 1 wenn Sichtlinien getrennt
- Ebenen-Übergänge (Treppen, Lifte, Schächte) sind als "Transition Zones" definiert — beide angrenzenden Layer gleichzeitig geladen für 60m Radius um den Übergang
- **Schichtgrenzen-Entscheidung (Vera, Tag 2)**: oben fließend, unten diskret. World-Partition-Setup kann damit final geplant werden. Obere Ebenen (Layer 2–3) nutzen Blend-Volumes; untere Ebenen (Layer 0–1) haben harte Data-Layer-Cuts. Diese Frage ist abgeschlossen.

<!-- Tobi: Vera-Abstimmung zu Schichtgrenzen ist erledigt (Tag 2 Meeting). -->

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

Für Cutscenes, Dialoge und Schwellenanker-Aktivierungs-Sequenzen nutzen wir **UE5 Sequencer** mit eigenem Kamerasystem.

- Cinematic-Kameras sind separate Kamera-Akteure — sie übernehmen temporär die Kontrolle, blenden zurück auf Spieler-Camera
- DOF: echtes Bokeh-DOF im Cinematic-Modus (Performance-Kosten akzeptiert für Kino-Qualität)
- **Kamera-Führungsprinzip**: Statische Langzeiteinstellungen, langsame Zooms, keine handheld-Simulation. Die Kamera ruht — die Welt bewegt sich in ihr. Das gilt für alle Haupt-Cutscenes.

<!-- Tobi: Tarkowski als Einfluss für Kamerastil, nach Nami-Input Tag 2. Im Fließtext keinen Autorname mehr. -->

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
- Beispiele: Bergkristall-Linsen der Gildenmeister, große Alchemie-Lampen in Ordenskorridoren, der aktivierte Schwellenanker (Zustand 2)
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

Das Schattenfieber-PP-System ist das komplexeste Single-Feature im Projekt. Es muss drei klar definierte Stufen mit smoothem Übergang abbilden und darf kein hartcodiertes System sein — alle Parameter müssen Blueprint-seitig steuerbar bleiben, damit das Gameplay-Team Inhalte ohne Tech-Art-Beteiligung implementieren kann.

**Blueprint-Architektur:**

```
BP_Schattenfieber
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

Der `ShadowFever_Intensity`-Wert wird vom Gameplay-Blueprint geschrieben (Lymph-Subsystem → Interface, siehe 6.4.7). Das PP-System liest den Wert und reagiert. Die genaue Interface-Definition steht in Abschnitt 6.4.7.

**Übergänge**: Immer geblended über die Timeline-Kurve. Kein Hard-Switch zwischen Stufen. Minimum-Blend-Zeit: 2 Sekunden pro Stufe.

---

### 6.4.2 Stufe 0 — Basis (kein Schattenfieber)

Normaler Spielzustand. Der PP_Stage_0-Stack ist trotzdem aktiv — er setzt die Color-Grading-Basis für RELICS.

- **Color Grading**: ACES-Tonemapping, leicht kühle Schattenbereiche (Shadow Gain: RGB 0.95 / 0.95 / 1.02)
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
- **Film Grain**: hochgesetzt auf 0.45, Körnung feiner (0.7) — das "Rauschen" des einsetzenden Fiebers
- **Schattenbereich-Kühlung**: Shadow Gain +0.05 auf Blaukanal — Schatten werden kälter
- **Vignette**: 0.15 Intensität — kaum bemerkbar, rahmt aber den Blick

**Was nicht aktiv ist**: kein DOF, keine Vertex-Animation, keine Geometrie-Eingriffe. Das kommt in Stufe 2.

*Visuelles Konzept*: Die Chromatic Aberration ist das optische Echo — das Bild "klingt nach" im visuellen Sinne. Eine winzige Farb-Verschiebung, die sich wie ein Nachbild anfühlt.

<!-- Tobi: Ursprünglicher Hinweis auf Sound-Design und Nami-Input aus Kommentar rausgenommen, da kein Autorenname im sichtbaren Text. -->

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
- **Full-Screen-Overlay**: `M_Schattenfieber_Overlay` — ein Custom-Depth-Masking-Shader mit organischen Rissstrukturen. Die Risse entstehen an Bildrändern und wandern langsam zur Bildmitte. Bewegungsgeschwindigkeit abhängig von `ShadowFever_Intensity`.
- **Geometrie-Lücken**: Ausgewählte Wand-Meshes zeigen temporäre schwarze Flächenbereiche — als würden Teile der Weltgeometrie nicht mehr existieren. Technisch: ein separater Render-Pass mit Masked-Visibility über Custom Stencil Buffer.
- **Indigo-Bloom**: Emissive-Quellen bekommen starken Indigo-Halo — Bloom-Radius 8.0, Tint stark Richtung Indigo/Violett
- **Chromatic Aberration**: 1.5 Pixel, chaotisch (Rauschwert statt Sinuswelle)
- **Nervensystem-Visualisierung**: startet automatisch (→ 6.5)

**Was diese Stufe mit dem Schwellenanker-Shader verbindet**: Der kritische Schwellenanker-Zustand (→ 6.6) nutzt dasselbe visuelle Vokabular wie Stufe 3 — Rissstrukturen, Innen-Leuchten, Indigo-Tönung. Das ist keine Koinzidenz. Der Schwellenanker und die Krankheit sprechen dieselbe Sprache. Intentionale Ambiguität.

*Accessibility-Option*: Bei aktiviertem Modus werden Geometrie-Lücken deaktiviert, Overlay-Intensität auf 0.6 reduziert. Die Stufe bleibt narrativ funktional.

---

### 6.4.6 Schattenfieber-Ambient (Layer-gebunden)

Unabhängig vom Spieler-Infektionslevel haben die Data Layers eine Baseline Schattenfieber-Ambience:

- Layer 0 (Untergrund): `ShadowFever_Ambient = 0.15` — die Schwelle ist hier dünn, das spürt man
- Layer 1 (Straße): `ShadowFever_Ambient = 0.05`
- Layer 2 (Arkaden): `ShadowFever_Ambient = 0.0`
- Layer 3 (Türme): `ShadowFever_Ambient = 0.0`

Der Ambient-Wert addiert auf den Spieler-Wert. Ein Spieler ohne Infektion in Layer 0 läuft bei effektiv 0.15 — im Normalzustand nicht bewusst, aber da. Technische Narratologie: die Architektur erzählt die Kosmologie.

<!-- Tobi: Offene Frage an Emre — sind Tiervolk-Siedlungen an festen "dünnen Orten" oder wandern die? Statisch = Ambient-Wert Layer-gebunden (bereits implementiert). Dynamisch = NPC-Proximity-gesteuert, deutlich aufwendiger. Antwort steht noch aus. -->

---

### 6.4.7 Interface-Spezifikation: Lymph-Subsystem → PP-Trigger

<!-- Tobi: Das ist der Abschnitt, den Darius gebraucht hat. Vollständige Blueprint-Interface-Definition. Wer ShadowFever_Intensity schreibt, wer liest, welche Werte zu welchen PP-Stufen führen. Stand v3, Tag 3 Mittwoch. -->

Das Lymph-Subsystem (Gameplay-Seite, Darius' Verantwortung) und das Schattenfieber-PP-System (Tech-Art-Seite) kommunizieren über ein klar definiertes Blueprint-Interface. Diese Spezifikation legt den Vertrag zwischen beiden Systemen fest.

#### Überblick: Wer schreibt, wer liest

```
Gameplay-Seite (Darius):          Tech-Art-Seite (Tobias):
BP_LymphSubsystem                 BP_Schattenfieber
    │                                     │
    │── schreibt ──►  ShadowFever_Intensity (0.0–3.0)
    │                                     │
    │◄── liest ──────  OnStageThresholdReached(float Stage)
    │
    └── schreibt ──►  ShadowFever_Ambient (addiert, Layer-gebunden, READ ONLY für Gameplay)
```

Das Gameplay-System schreibt `ShadowFever_Intensity`. Das PP-System schreibt nichts zurück — es feuert Events. Das Gameplay-System hört auf diese Events und reagiert (z.B. Gameplay-Konsequenzen bei Stufenwechsel).

---

#### Interface-Funktion: `SetShadowFeverIntensity(float Value)`

**Aufrufender**: `BP_LymphSubsystem` (Gameplay)
**Empfänger**: `BP_Schattenfieber` (Tech-Art)

```
Signatur:      void SetShadowFeverIntensity(float Value)
Werte-Range:   0.0 – 3.0
Einheit:       normierter Intensity-Wert, keine physikalische Einheit
Clamp:         intern geclampt auf [0.0, 3.0] — Über-/Unterschreitung wird abgefangen
```

**Mapping Lymph-Stufe → ShadowFever_Intensity-Wert:**

| Lymph-Stufe (Darius) | ShadowFever_Intensity | PP-Stufe aktiv | Spielerlebnis |
|---|---|---|---|
| Untrained (Basis) | 0.0 – 0.2 | Stufe 0 (Basis) | Kein sichtbares Fieber |
| Geübt | 0.2 – 0.8 | Stufe 0 → 1 (gleitend) | Peripherie-Rauschen, Spieler unsicher |
| Fortgeschritten | 0.8 – 1.8 | Stufe 1 → 2 (gleitend) | Eindeutige Symptome, bewusst spürbar |
| Meister | 1.8 – 3.0 | Stufe 2 → 3 (gleitend) | Auflösung, Schwellen-Erfahrung |

*Wichtig*: Die Werte sind **kontinuierlich**, nicht diskret. Das PP-System blended fließend über die gesamte Range. Darius entscheidet, wie schnell die Lymph-Stufen steigen — das PP-System folgt.

**Zusätzliche Gameplay-Einflüsse auf den Wert:**

Der Wert setzt sich zusammen aus:
```
ShadowFever_Intensity = Lymph_BaseValue + Exposure_Delta + ShadowFever_Ambient
```

- `Lymph_BaseValue`: der Kernwert aus dem Lymph-Fortschritt (Darius' System)
- `Exposure_Delta`: temporäre Erhöhung durch Exposition (Slum-Bereiche, Infizierte NPCs, Schwellenanker-Kontakt) — klingt über Zeit ab
- `ShadowFever_Ambient`: Layer-gebundener Basiswert (read-only für Gameplay, wird vom PP-System addiert)

<!-- Tobi: Exposure_Delta ist ein Vorschlag meinerseits — Darius entscheidet, ob er das so implementiert oder anders strukturiert. Der PP-Empfänger braucht nur den finalen kombinierten Wert. Wie der zusammengesetzt wird, ist Gameplay-Logik. -->

---

#### Interface-Event: `OnStageThresholdReached`

**Sender**: `BP_Schattenfieber` (Tech-Art)
**Empfänger**: `BP_LymphSubsystem` (Gameplay — abonniert dieses Event)

```
Signatur:      Event OnStageThresholdReached(float Stage)
Werte:         1.0 (Stufe 1 erreicht), 2.0 (Stufe 2 erreicht), 3.0 (Stufe 3 erreicht)
Richtung:      Aufwärts UND Abwärts (Stage-Abfall unter Schwelle feuert ebenfalls)
```

Das Gameplay-System kann auf dieses Event reagieren mit:
- Gameplay-Mechanik-Freischaltung (z.B. Fähigkeiten bei Stufe 2+)
- NPC-Reaktionen triggern (NPCs erkennen infizierte Spieler)
- Journal-Eintrag / Narrative-Beat schreiben
- Sound-Cue auslösen (Sound-Design-Verantwortung)

---

#### Interface-Funktion: `GetCurrentShadowFeverStage()` (optional, read-only)

```
Signatur:      float GetCurrentShadowFeverStage()
Rückgabe:      aktueller ShadowFever_Intensity-Wert (0.0–3.0)
Zweck:         Gameplay-seitige Abfrage für z.B. HUD-Anzeige oder Dialogue-Conditionals
```

---

#### Fraktions-Presets (optionale Erweiterung)

Wenn Nami bestätigt, dass Fraktionswahl unterschiedliche PP-Presets erfordert, kann das Gameplay-System folgende Funktion aufrufen:

```
Signatur:      void SetFactionPPPreset(EFaction Faction)
Werte:         EFaction::Krone | EFaction::Gilden | EFaction::Orden
Effekt:        Lädt einen Preset-Stack auf PP_Stage_0 — verändert die Basis-Tonalität
               Krone:  wärmerer Basiston, Ambience reduziert (Unterdrückung sichtbar)
               Gilden: neutraler Basiston, Emissive-Intensität leicht erhöht
               Orden:  kühler Basiston, Schattenbereiche dunkler (Wissen = Tiefe)
```

<!-- Tobi: Das ist ein Vorschlag, kein gesetztes Feature. Nami muss bestätigen, ob Fraktions-PP-Presets narrativ gewünscht sind. Wenn ja, ist das ein kleiner Aufwand (drei PP_Stage_0-Varianten). Wenn nein, brauchen wir nur den generischen Stage-0. -->

---

#### Blueprint-Verbindungsschema (schematisch)

```
BP_LymphSubsystem
    │
    ├── OnLymphLevelUp ──────────────────────────► BerechneIntensity()
    │                                                    │
    │                                           SetShadowFeverIntensity(value)
    │                                                    │
    │                                          BP_Schattenfieber
    │                                                    │
    │                                          Timeline blended PP-Stack
    │                                                    │
    │◄────────────── OnStageThresholdReached ────────────┘
    │
    ├── OnNarrativeTrigger (optional)
    ├── OnNPCReaction (optional)
    └── OnSoundCue (Sound-Design)
```

---

#### Zusammenfassung für Darius

Das PP-System braucht von Gameplay-Seite genau **einen Float** (0.0–3.0). Wie dieser Float berechnet wird — aus Lymph-Fortschritt, Expositions-Akkumulation, Fraktions-Modifikatoren — ist vollständig in Darius' Hand. Das Tech-Art-System ist bewusst so gebaut, dass keine Abhängigkeit in die andere Richtung existiert: kein PP-Code greift auf Gameplay-Variablen zu.

Das PP-System feuert Events zurück. Darius abonniert, was er braucht.

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

## 6.6 Schwellenanker-Shader — Master Material System

<!-- Tobi: Asset-Namen: M_Schwellenanker_Master, MI_Schwellenanker_Dormant, MI_Schwellenanker_Resonant, MI_Schwellenanker_Critical, T_Schwellenanker_Riss_01, BP_Schwellenanker. -->

### 6.6.1 Konzept

Der Schwellenanker — der kosmologische Resonanzpunkt, das namensgebende Artefakt dieser Spieliteration — existiert als ein einziges Mesh mit einem Master-Material und drei Material-Instanzen. Die Übergänge zwischen den Zuständen sind immer geblended, nie hart. Der Schwellenanker ist kein Gadget; er ist ein kosmologisches Instrument. Das muss im Material sichtbar sein.

**Zur Form**: Vera hat die Geometriebeschreibung auf "folded geological formation, compressed ossified mineral cluster" spezifiziert — weg von einer wirbelsäulenartigen Struktur. Das hat Shader-Konsequenzen: SSS-Radius und Riss-Topologie müssen auf eine verdichtete, mineralische Form kalibriert werden, nicht auf eine langgestreckte organische. Der Riss-Procedural-Noise (`T_Schwellenanker_Riss_01`) wird entsprechend neu kalibriert — komprimierte Rissstrukturen statt radialer Brüche.

<!-- Tobi: Vera hat die Form-Beschreibung geändert (Tag 3 Briefing). Shader-Konsequenz: SSS-Radius-Kalibrierung neu, T_Schwellenanker_Riss_01 Noise-Profil anpassen. Kein großer Aufwand — ein Parametertuning, kein Umbau. -->

---

### 6.6.2 Drei Zustände

**Zustand 1 — Ruhezustand (dormant):**
Der Schwellenanker ruht. Er ist nicht tot — er ist latent lebendig.

- **Base Material**: transluzentes, mattes Grundmaterial
- **Subsurface Scattering (SSS)**: aktiv, warme Untertonfarbe (RGB 1.0 / 0.85 / 0.7 — leicht goldenes Hautton-Unterlicht)
- **SSS-Radius**: 0.8 cm — das Licht streut tief, wie durch organisches Gewebe. Bei mineralischer Kompression ggf. auf 0.5 cm reduzieren (Abstimmung nach erster Vera-Referenz).
- **Roughness**: 0.55 — nicht spiegelnd, aber nicht stumpf. Polierter Knochen oder Elfenbein-Charakter. Bei mineralischer Form: ggf. Richtung 0.45 (glattere Kompressionsflächen).
- **Emissive**: 0.0 — kein aktives Leuchten
- **Lumen-Emitter**: deaktiviert

*Designabsicht*: Der Schwellenanker soll schon im Ruhezustand anders aussehen als totes Material. Das SSS erzeugt innere Lebendigkeit — etwas ist da, schläft aber.

---

**Zustand 2 — Aktiver Zustand (resonant):**
Der Schwellenanker ist aktiviert. Er ist zur Lichtquelle geworden.

- **Base Material**: dasselbe Grundmaterial, aber SSS-Intensität um 40% erhöht
- **Emissive-Layer**: hochgefahren, Farbe = warmes Indigo-Weiß (RGB 0.85 / 0.8 / 1.2, überbelichtet bei 3.5)
- **Lumen-Emitter**: aktiviert (Klasse A) — der Schwellenanker wirft echtes GI in die Szene, färbt umliegende Wände und Böden
- **Lichtfarbe Lumen**: leicht violett-weiß (CCT 7500K mit Indigo-Bias) — kühler als natürliches Licht, kalt und klar
- **Lichtradius**: 4m für direkte Lumen-Reichweite, darüber Bloom-Halo
- **Bloom-Halo**: 6.0 Radius, Indigo-Tint — sichtbar auch auf Screenshots, nicht nur in Bewegung

*Designabsicht*: Der aktivierte Schwellenanker soll sofort als Lichtquelle erkennbar sein. Er ist die wichtigste dynamische Lichtquelle in jeder Szene, in der er aktiv ist.

---

**Zustand 3 — Kritischer Zustand (überlastet):**
Der Schwellenanker ist am Limit. Das kosmologische Instrument bricht unter Last.

- **Base Material**: Riss-Overlay-Layer aktiv — ein Masked-Texture-Layer projiziert organische Rissstrukturen auf die Oberfläche
- **Riss-Struktur**: `T_Schwellenanker_Riss_01` (Procedural Noise-basiert, komprimierte Rissgeometrie passend zur mineralischen Grundform — kein symmetrisches Muster) — Risse öffnen sich im Laufe des kritischen Zustands (Blend-Parameter steuert Öffnungsgrad)
- **Innenleuchten**: durch die Risse scheint das Emissive-Innere — lokal höhere Emissive-Intensität an Riss-Kanten (8.0+, kalt-violett)
- **Subsurface Scattering**: jetzt blau-violett getönt (RGB 0.7 / 0.6 / 1.3) — die Wärme ist weg, das SSS-Licht ist kalt
- **Lumen-Emitter**: flackernd, instabil (Blueprint-gesteuerte Intensitätsschwankung, 2–8 Hz unregelmäßig)
- **Lichtfarbe**: hart-violett (CCT >10000K, stark ins Ultraviolett verschoben)
- **Vertex-Animation**: das Mesh selbst vibriert leicht (±0.2mm, 12 Hz) — submillimeter, erzeugt nervöses Shimmern

*Designabsicht*: Visuelles Vokabular entspricht bewusst PP-Stufe 3. Der Schwellenanker und das Schattenfieber sprechen dieselbe Sprache: Rissstrukturen, Kalt-Violett, Innenleuchten, Instabilität. Der Spieler sieht diese Verbindung — ob er sie versteht, ist Erzählung. Zustand 3 zeigt keine kontrollierte Instabilität, sondern ein Objekt kurz vor dem Bruch — das Riss-Blend-Parametersystem erlaubt es, diesen Brechpunkt für Act 3 sequenziell aufzuziehen.

<!-- Tobi: Namis narrativer Kommentar (Tag 3 Briefing) — "ein Anker kann reißen" — ist für Act 3 relevant. Im Shader ist das angelegt: Rissstrukturen mit steuerbarem Öffnungsgrad. Kein neuer Shader-Aufwand nötig, nur Blueprint-Kurven-Authoring. -->

---

### 6.6.3 Master-Material-Struktur (M_Schwellenanker_Master)

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

**Drei Material-Instanzen**: `MI_Schwellenanker_Dormant`, `MI_Schwellenanker_Resonant`, `MI_Schwellenanker_Critical` — alle vom selben Master. Blueprint interpoliert zwischen den Instanz-Parametern über `State_Alpha`.

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

<!-- Tobi: Houdini-Terrain wartet auf Emres Topos-Kapitel. Stadtname, Sichtachsen, Gebirgs-Kontext fehlen noch. Emre hat Topos als Fokus für Tag 3 genannt — ich nehme an, bis Ende heute kommt genug Material für erste Constraint-Kurven. -->

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

**Warum kein AgX?** AgX ist für Photography optimiert und komprimiert Highlights weicher. RELICS braucht scharfe, klare Lichter — die Bergkristall-Linsen, die Schwellenanker-Emitter müssen leuchten, nicht weich werden. ACES gibt uns das.

---

### 6.8.2 Display-Kalibrierung (internes Studio)

Alle Arbeitsstationen im Studio haben kalibrierte Displays (Delta-E < 2.0). Die Referenz-LUT läuft auf einem Samsung Odyssey OLED, der als "Goldstandard"-Display dient. Spieler-seitig gibt es keine Kontrolle — daher sind alle Emissive-Werte so kalibriert, dass sie auch auf einem Standard-SDR-Display (sRGB, 200 cd/m² Peak) korrekt wirken. HDR-Displays bekommen automatisch einen separaten Display-Transform mit erweiterten Highlight-Bereichen.

---

## 6.9 Produktion & Release-Pipeline

### 6.9.1 Milestone-Übersicht

| Milestone | Technischer Status | Schlüssel-Deliverables |
|---|---|---|
| **Pre-Alpha** | Prototyp-Pipeline | Rendering-Architektur steht, Material-Master-Systeme gebaut, World Partition Setup stabil |
| **Alpha** (Streamer) | Feature-Freeze Rendering | Data Layers gesetzt, Lumen-Konfiguration fixiert, PP-System stabil, Schwellenanker-Shader stabil. Standard: stabil + konsistent, NICHT polished |
| **Beta** | Tuning-Phase | Alle bestehenden Systeme werden getuned — Performance-Optimierung, visuelle Feinheit, Accessibility vollständig |
| **Full Release** | Feinschliff + große Setpieces | Abschließende Lighting-Pass für alle Hauptorte, Cinematic-Sequenzen final |
| **DLC** | Erweiterung auf stabiler Basis | Neue Assets auf bestehenden Systemen — kein neues technisches Risiko in DLC-Phase |

**Alpha ist der härteste Freeze**: Nach Alpha-Abgabe sind folgende Systeme nicht mehr änderbar:
- Data Layer-Struktur (Schichtanzahl, Naming, Streaming-Logik)
- Lumen-Konfiguration (RT-Modus pro Layer)
- Schattenfieber-PP-System-Architektur (Blueprint-Struktur, Parameter-Namen)
- Schwellenanker-Master-Material-Struktur (Parameter-Gruppen, Slot-Namen)
- Kamerasystem-Grundstruktur
- **Interface-Spezifikation Lymph → PP-Trigger** (Funktionsnamen, Parameter-Typen, Event-Namen)

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
- Lymph-PP-Interface implementiert und mit Gameplay-Team getestet
- Schwellenanker-Master-Material (alle drei Zustände)
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
| Nervensystem Arm-Mesh | MITTEL | Hoher Animations-Aufwand im FP-Modus | Eigenständiger Task, 3-Wochen-Schätzung, eigenständige Asset-Klasse |
| Schwellenanker-Shader-Synchronität | NIEDRIG | State-Alpha-Drift zwischen Blueprint und Material | Interface-Konvention festgelegt, Parameternamen dokumentiert |
| Lymph-PP-Interface-Drift | NIEDRIG | Gameplay ändert Parameternamen nach Alpha-Freeze | Interface-Namen in 6.4.7 festgeschrieben, Alpha-Freeze gilt explizit |

---

\clearpage
