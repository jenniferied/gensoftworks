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
