# Leo — Memory

## Tag 1, Szene 2: WORK | Recherche (QA-Perspektive)

### Kernerkenntnisse zum RELICS-Design

**Zielgruppe überlappt vier Communities:**
1. Immersion-First (Disco Elysium, Outer Wilds, Kingdom Come)
2. Faction-Player (Baldur's Gate, Bloodlines, New Vegas)
3. Crafting-Freaks (Dark Souls, Hades)
4. Medieval-Puristen (KCD, Mount & Blade)

**Risiken erkannt:**
- Medieval Cyberpunk = Identitätskrise, wenn Material-als-Macht nicht sofort sichtbar ist
- Erste Stunde ist NICHT Tutorial, sondern Angebot (Agentschaft)
- Schattenfieber muss biologisch WIRKEN, nicht mystisch
- Faction-Asymmetrie ist okay, aber jede muss ihr eigenes Appeal haben

**Konkurrenzmapping:**
- KCD: Wir gewinnen durch Faction-Drama + Material-Upgrade-Sichtbarkeit
- Skyrim: Wir gewinnen durch Erde + politische Tiefe
- Elden Ring: Wir gewinnen durch klare Quest-Struktur bei bewahrter Immersion
- BG3: Wir gewinnen durch Real-time + Solo-Agentschaft
- CP2077: Medieval = weniger Simulationslast = schneller spielbar

**Spielertest-Kriterien (für GDD Kap 2):**
1. Kann ich nach 30 Min sagen, was Material-Klasse für mein Gameplay bedeutet?
2. Reagiert die Welt asynchron (Krone patrouilliert, Orden späht, Gilden handeln)?
3. Fühlt sich Schattenfieber körperlich an (nicht magisch)?

### Output generiert
- `gallery/gdd/00-recherche-notizen-leo.md` — 600 Wörter, Zielgruppe + Konkurrenz + Risiken

---

## Tag 2, Szene 1: BRIEFING | 09:00 in der Küche

### Kernpunkte aus dem Briefing

**Relikt als Resonanzobjekt (Darius + Emre):**
- Reakt auf Lymph-Subsystem-Aktivität
- Drei biologische Stufen im Schwellen-System
- Stabilisator für die "dünne" Stelle in der Stadt
- WICHTIG: Muss SOFORT visuell/auditorisch feedbacken, sonst Spieler denken Bug

**Visuelles Design (Vera):**
- Knochenartig-organisch
- Drei Zustände mit unterschiedlichen Energie-Auras
- Instabil wirken = Schwellen-Zusammenbruch-Feeling
- Deadline: Relikt-Varianten + Stadtschnitt + Fraktionspaletten heute

**Release-Strategie (Finn + Tobi):**
- Main → Alpha (mit Streamern) → Beta → Full → DLCs
- Alpha = Feature-Freeze auf Rendering
- Alpha = erste Spielstunde MUSS stehen
- Relikt: Master-Shader mit Blend-Parameter, drei Zustände
- Schattenfieber-Ambient im Untergrund-Layer

**Fraktionskosmologien (Nami):**
- Krone = Blut-basiert
- Orden = Wissen-basiert
- Gilden = Material-basiert
- Quest-Einstieg: Sterbender gibt Fremdem Relikt-Scherbe
- Erste Stunde = ECHTE Fraktionswahl, nicht Pseudo-Choice

**Schattenfieber (Nami):**
- Nicht zweiter Balken, sondern ERSTER Balken der sich falsch ZU LESEN BEGINNT
- Biologisch aus der "Schwelle"

### Meine Position (Leo)

**Zu Relikt-Resonanz:**
- Das ist genial, aber SUBTILITÄT TÖTET. Muss in Alpha sofort klarkommt
- Feedback = Particels/Sound/Combo-Animation, nicht nur Vibration
- Streamer-Moment: "dieses Game versteht mich"
- Reddit-Fallstrick: wenn zu subtil, "Relikt-Mechanic ist broken"

**Zu Alpha mit Streamern:**
- ICH bin die Kanarienvogel: 47k Follower, Live-Feedback
- Alpha muss POLIERT sein, nicht Feature-Complete
- Ich teste wie Spielerin, nicht wie Testerin
- Bug-Reporting mit Timestamps + Repro-Schritten
- Kritisch: Zuschauerzahl-Stabilität (Fenster 8-12 Min ist make-or-break)

**Zu Skill-by-Use (Sync mit Darius heute):**
- Position: JA zu Skill-by-Use, aber mit visuellen Krümelbroten
- Nicht grindy, aber fühlbar
- Nach 10x Nutzung = SichtBAR besser werden (Particle, Sound, Combo-Animation)
- Streamer-Content: "Leute, seht die Skill-Progression? Das EARNT sich"

**Zu Vera:**
- Relikt-Zustände: unterschiedliche Energie-Auras ESSENTIELL
- Instabilität visualisieren = Schwellen-Zusammenbruch-Drama

**Offene Fragen:**
- Wolf-Checkliste: Wo steht die? Brauche das für Szenen-Architektur-QA
- Emre: "Schattenfieber zu Lesen beginnt" = wie wird das mechanisch sichtbar?

### Nächste Schritte
- Sync mit Darius heute Nachmittag zu Skill-by-Use
- Alpha-Build-Checkliste: Relikt-Feedback + Erste-Stunde-Feeling
- GDD Kap 2 Review: Spielerperspektive + "würde Chat hier ABW-en?"

---

## Tag 2, Szene 2: WORK | 10:00–11:30 — Wolf-Checkliste + Darius-Vorbereitung

### FERTIG: Wolf-Checkliste

**Datei:** `simulation-2/gallery/gdd/00-wolf-checkliste-leo.md`

**Konzept:** Praktisches QA-Tool basierend auf Mark J. P. Wolfs neun Infrastrukturen imaginärer Welten (2013, Kap. 3).

**Neun Infrastrukturen → RELICS-Mapping:**

1. **Karten:** Topografie + Schichtung (Oberschicht/Mittel/Unterschicht visuell erkennbar)
2. **Zeitleisten:** Zeitliche Urgency (wann findet das statt? gibt es Druck?)
3. **Genealogien:** Figurennetze (Fraktions-Hierarchien, sterbender NPC Gewicht)
4. **Natur:** Flora/Fauna, Schattenfieber-Biotech-Effekte
5. **Kultur:** Material-Klasse (All-Black/Erdtöne/Grau-Schmutzig), Alltag, Religion
6. **Sprache:** Germanische Namenssysteme, Dialekte (Fraktions-erkennbar)
7. **Mythologie:** Relikt-Ursprung, Schöpfungsmythen, Legenden
8. **Philosophie:** Fraktions-Weltsichten (Blut/Wissen/Material), Skill-by-Use-Alignment
9. **Verknüpfung:** Alle müssen ZUSAMMENHÄNGEN (Relikt durchdringt alles)

**QA-Fokus:**
- SICHTBAR: Was merkt Spieler im Gameplay?
- BACKEND: Lore-Konsistenz
- CRITICAL: Was killt Immersion?

**Praktische Alpha-Erste-Stunde-Metriken:**
- Min 0–5: Material-Klasse erkennbar?
- Min 5–10: Emotionale Hook am sterbenden NPC?
- Min 10–15: Skill-by-Use erste 5–10 Nutzungen sichtbar?
- Min 15–30: Fraktions-Asymmetrie echte Wahl?
- Min 30–60: Relikt fühlt sich WOW an?

SUCCESS = Chat-Zuschauer schalten nicht ab. (Baseline: 70%+ nach 60 Min)

---

### FERTIG: Alpha-Erste-Stunde Streamer-Checkliste

**Datei:** `simulation-2/gallery/gdd/00-alpha-erste-stunde-leo.md`

**Zweck:** Live-Testwerkzeug für meine erste Streamer-Session mit RELICS Alpha-Build.

**Struktur:**
- Phase 1 (0–5 Min): Erste Impressionen (Material-Klasse, Welt-Feeling, Audio)
- Phase 2 (5–10 Min): Emotional Hook (sterbender NPC, Dialog, Genealogie, Schattenfieber-Signal)
- Phase 3 (10–15 Min): Mechanic-Intro (Combat-Weight, Skill-by-Use-Sichtbarkeit, Gegner-AI, Relikt-Gewicht)
- Phase 4 (15–30 Min): Welt-Asynchronität (Fraktions-NPCs unterschiedlich, Reaktion auf mich, Ambient-Audio, Quest-Optionen)
- Phase 5 (30–60 Min): Immersion-Check (großes Bild, Material-Ökonomie, Relikt-nicht-broken, Polish-Level, Fremden-Charakter-Status)

**Quantitative Tracking:**
- Chat-Engagement pro Minute
- Retention-Kurve (Zielwert: >70% nach 60 Min)
- Positive/Neutral/Negative Reactions pro Phase

**Bug-Report-Template:** Standardisiert mit Wolf-Infrastruktur + Severity + Streamer-Auswirkung

---

### FERTIG: Talking Points für Darius-Sync

**Datei:** `simulation-2/gallery/gdd/00-leo-talking-points-darius-sync.md`

**7 Kernpunkte:**

1. **Philosophische Alignment:**
   - Skill-by-Use ist nicht neutral. Es ist Gilden-Weltsicht.
   - Krone: lernen durch Blut (Erbe), Orden: Wissen (Intellekt), Gilden: Praxis (Tun)
   - → Spieler sollte merken: "Ich bin nicht grinding, ich bin AGENTSCHAFT-aligned"

2. **Praktische Metriken (für Alpha):**
   - Hit 1–4: Baseline (normal Sound + Particle)
   - Hit 5–7: Subtil-Signal (Sound cleaner, Particle-Color shiftet, Animation flüssiger)
   - Hit 8–10: Obvious-Signal (Sound differenzierbar, Swing-Arc besser, Combo-Potential sichtbar)
   - Chat-Test: Nach Hit 8–10 sollte Chat sagen "your swing just got better"
   - **RED LINE:** Wenn nicht sichtbar, Chat sagt "skill system broken?" = Retention-Killer

3. **Relikt-Integration:**
   - Option A: Relikt-Nähe = schneller Skill-Lernen
   - Option B: Relikt = Interferenz (glitchy Skills)
   - Option C: Orthogonal
   - → Frage an Darius: Welche macht narrativ Sinn?

4. **Technische Feasibility:**
   - Können Skill-Upgrade-Visuals parallel zu Relikt-Shader laufen?
   - Ist 10-State-Animation kW-heavy?
   - Können Particle-Colors datadrive sein?
   - If blockers: Können wir MVP-Scope reduzieren?

5. **Content-Integration (später mit Nami):**
   - Sollten NPC-Dialog-Optionen an Skill-Level gebunden sein?
   - Sollte Gilden-NPC mich anders grüßen, wenn ich geskilled bin?

6. **Streamer-Retention (RED LINE):**
   - Erste Combat-Encounter: Min 10–12
   - Nach 10 Hits sollte Chat merken: was ändert sich?
   - Wenn nicht: Retention sinkt 75% → 55%
   - **Empfehlung:** Wenn Skill-Upgrade-Visuals nicht Alpha-ready: SYSTEM DEACTIVATE statt unpolished
   - **Besser:** 1 simple Mechanic 100% Polish. **Schlecht:** komplexes System 60% Polish

7. **Langzeitvision (Post-Alpha):**
   - 5–7 Skill-States pro Waffe
   - Unlock-System (Combos, Special-Attacks)
   - Tier-System (Anfänger → Handwerker → Meister)
   - Schmiede-Quests für Legendary-Waffen

**Erwarteter Output von Darius:**
- [ ] Skill-by-Use für Alpha realistisch?
- [ ] Welche Hit-Count-Metriken?
- [ ] Wenn nein: Wann revisit-en?
- [ ] Wer ist Owner für Upgrade-Visuals? (Vera? Tobi? Darius?)
- [ ] Wann nächster Sync?

---

### Mein aktueller Status

**COMPLETE:**
- [x] Wolf-Checkliste (QA-Tool, alle 9 Infrastrukturen)
- [x] Alpha-Erste-Stunde Checkliste (Live-Testwerkzeug)
- [x] Talking Points für Darius-Sync (7 Kernpunkte + Red Lines)
- [x] Memory aktualisiert (dieser Eintrag)

**IN PROGRESS:**
- [ ] Darius-Sync (14:00 heute)
- [ ] Alpha-Build besorgen (von Tobi? Finn?)
- [ ] Erste 30 Min testen + Bericht schreiben

**PENDING:**
- [ ] GDD Kap 2 Review (sobald Darius/Nami Draft haben)
- [ ] Relikt-Resonanz QA-Protokoll (mit Vera + Emre)
- [ ] Streamer-Retention-Vergleich (Outer Wilds, Disco Elysium, KCD in Sheets)

---

### Notizen zur Darius-Preparation

**Was ich mitbringe:**
- Zweiter Monitor: Retention-Daten (Google Sheets)
- Dritter Tab: Wolf-Checkliste (als Referenz)
- Vierter Tab: Skill-by-Use Mechanic-Doku (falls vorhanden)
- Notizbuch: Für Action-Items

**Tone:**
- Collaborative (nicht adversarial)
- Data-driven (Retention-Metriken, Chat-Reaktionen)
- Praktisch (nicht akademisch)
- Spieler-Stimme (nicht Business-Optimierung)

**Ziel-Outcome:**
Nach Sync sollte klar sein:
1. Philosophischer Alignment (Skill-by-Use = Gilden-Weltsicht)
2. Praktische Definition (Hit-Count bis zu Upgrade-Sichtbarkeit)
3. Alpha-Blocking-Status (Visuell-Sichtbarkeit ist RED LINE)
4. Owner + Verantwortlichkeiten (wer macht was bis wann)
5. Nächster Sync-Punkt (vor oder nach Alpha-Build?)

Wenn Sync gut läuft: Confidence wächst, dass erste Streamer-Session kein Engagement-Desaster wird.

---

**Gesamtstatus:** ON TRACK.

**Priority Stack (nächste 48h):**
1. Darius-Sync (heute 14:00) — Skill-by-Use Finalisierung
2. Alpha-Build besorgen (heute/morgen) — erste 30 Min testen
3. Relikt-QA-Protokoll (morgen) — mit Vera + Emre
4. Streamer-Retention-Analyse (Freitag) — für GDD-Snapshot

**Confidence Level:** 7/10 (Checklisten sind solid, aber hänge vom Alpha-Build-Status ab)

---

## Tag 3, Szene 1: BRIEFING | 09:00 in der Küche

**Typ**: BRIEFING | **Uhrzeit**: 09:00 | **Teilnehmer**: Finn (CD), Darius, Emre, Nami, Vera, Tobi, Leo

### Kernpunkte aus dem Briefing

**Finn CD-Feedback zu Dokumenten:**
- PDFs müssen sauber sein (keine Kommentare, Namen, Metadaten-Krümel)
- Concept-Art embedded (nicht separater Link)
- Schwellenanker-Name = Relikt (nicht "Relikt-Anker" oder andere Varianten)
- Spieler darf Fragment ablehnen (ist nicht Bug, ist Kosmologie-Wahl)

**Darius (Game Design):**
- Braucht QA-Pass auf Kap 1 v1 heute Vormittag als Basis für v2-Revision

**Emre (Worldbuilding):**
- Drei offene Widersprüche: Flora/Fauna-Konsistenz, Tiervolk-Kosmologie, Zeitlinie der Schwellen-Öffnung
- Diese leben im GDD und blockieren Narrative-Draft von Nami

**Nami (Narrative):**
- Schreibt Ablehnung-Option heute als halbe Seite in Kap 5
- Schwellenanker-Name funktioniert narrativ (Relikt = Material + Resonanz)

**Vera (Concept Art):**
- Neue Gilden-Palette kommt heute
- Relikt-Wirbelsäule-Form raus, neue organische Form kommt
- Stadtschnitt v2 kommt (mit neuer Palette integriert)

**Tobi (Tech):**
- GDD Kap 6 Cleanup heute
- Schwellenanker-Rename durchziehen (Relikt überall)

### Meine Position (Leo) + QA-Plan für heute

**QA-Strategie:**
1. **Priority 1:** Kap 1 v1 durchgehen für Darius bis 12:00 Uhr (Basis für v2)
   - Wolf-Checkliste als Tool: Karten, Genealogie, Flora/Fauna, Kultur, Sprache, Mythologie
   - Fokus: Emres drei Widersprüche lokalisieren + Report schreiben
   - Frage: Sind Schwellenanker-Namen konsistent? Sind Schattenfieber-Effekte mechanisch beschrieben?

2. **Priority 2:** CD-Feedback zu sauberen Dokumenten implementieren
   - "Saubere Dokumente" = professionell, Reddit-share-ready, keine Metadaten
   - Embedded Concept-Art = visuell sofort klar
   - Konsistenter Name (Relikt) = nicht verwirren
   - Das ist GDD-Hygiene, wichtig für Alpha-Release

3. **Parallela:** Vera-Sync (kleine Koordination)
   - Neue Gilden-Palette: bedeutet das Kosmologie-Shift im Kap 1-Text?
   - Stadtschnitt v2: welche Infrastrukturen-Sichtbarkeit ändert sich? (Karte, Schicht-Erkennbarkeit)

4. **Backlog:** Ablehnung-Option mechanik-Check
   - Nami schreibt halbe Seite, aber Mechanic muss ins Kap 2/3 (Kernmechaniken)
   - Ablehnung ist nicht "skip quest", sondern Kosmologie-Wahl → muss Design-Impact haben

### Offene Fragen für Team

- **Zu Emre:** Wo sind die drei Widersprüche gelistet? Brauche Source-Referenzen für Kap 1 Review.
- **Zu Vera:** Bildschirm-Zeit heute für Palette-Check? (30 min reicht)
- **Zu Nami:** Mechanisch: wenn Fragment abgelehnt, welche Quest-Pfade sperren auf? (brauche das für Gameplay-Konsistenz)
- **Zu Tobi:** Kap 6 Rename-Checklist — brauche die parallel zu meinem Kap 1 Pass, damit ich nicht blind bin.

### Nächste Schritte (für mich heute)

- 09:30–12:00: Kap 1 v1 mit Wolf-Checkliste durcharbeiten, Report schreiben
- 12:00–13:00: Report zu Darius (für v2 Vorbereitung)
- 13:00–14:00: Vera-Palette-Check (wenn Zeit)
- 14:00–15:00: Darius-Sync zu Skill-by-Use (wie geplant)
- 15:00+: Alpha-Build besorgen (von Tobi?) und erste 30 Min testen

### Persönliches / Stimmung

Energiegeladen — die Krisen-Punkte (Widersprüche, Schwellenanker-Konsistenz) sind machbar, nicht fundamental. CD-Feedback zu "sauberen Dokumenten" macht Sinn: wir sind 6 Wochen vor Alpha, jede Polierung zählt. Freue mich auf Kap 1 Review — das ist konkrete Spielerperspektive-Arbeit.

**Confidence Level:** 8/10 (höher als gestern, weil Darius/Finn/Tobi klare Ownership nehmen)

---

## Tag 3, Szene 2: WORK | 10:30–12:00 — QA-Pass über vier existierende Kapitel

**Typ**: WORK | **Uhrzeit**: 10:30–12:00 | **Teilnehmer**: Leo (solo)

### FERTIG: QA-Bericht Tag 3

**Datei:** `simulation-2/gallery/gdd/00-qa-bericht-tag3-leo.md`

**Zweck:** Umfassende Spielerperspektive-Bewertung aller Kapitel gegen Briefing + Wolf-Infrastrukturen

**Checklisten:**
- Briefing-Konsistenz (12 Punkte aus Briefing, 11/12 konsistent)
- Wolf-Infrastrukturen (9 Säulen: Karten, Zeitleisten, Genealogien, Natur, Kultur, Sprache, Mythologie, Philosophie, Verknüpfung)
- Document Hygiene (Autor-Namen, Kommentare, Metadaten)
- Vollständigkeit gegen "Erste 30 Minuten"-Kriterien

**Drei Bleeding Issues (blockierend für v2):**
1. **Relikt-Namenspolitik** — "Die Wurzel" vs. "Das Relikt" vs. "Der Schwellenanker" nicht konsistent. Briefing sagt "Schwellenanker ist der Name", aber Kapitel befolgen das nicht. MUSS heute 14:00 entschieden sein (Darius + Emre + Nami).
2. **Emres Widerspruchs-Log W-001, W-004, W-006** — Substanz-Definition (W-001), Tiervolk-Herkunft (W-004), konkrete Zeitlinie "vor einer Generation" (W-006) sind KRITISCH und blockieren Nami's weitere Arbeit.
3. **Autor-Namen in sichtbaren Texten** — CD-Feedback: "keine Namen in PDFs." Violiert in Kap 01 (Zeile 4, 76) und Kap 04 (Zeile 82). Muss bis PDF-Export weg sein.

**Beobachtungen pro Kapitel:**

| Kapitel | Autor | Qualität | Blocking Issues | Zu Beta |
|---------|-------|----------|-----------------|---------|
| **GDD 01** | Darius | ✅ Sehr stark (vier Säulen, Design-Philosophie klar) | Relikt-Name Inkonsistenz | Kap 2/3 folgen |
| **GDD 04** | Nami | ✅ Excellent (NPC-Stimmen individuell, Genealogie solid) | Zeitleinie unkonkretisiert, "alter Mann in Slums" noch nicht ausgearbeitet | Nebenquest-Ausarbeitung |
| **GDD 06** | Tobi | ✅ Excellent (Shader-Struktur sauber, Architektur robust) | Vera-Abhängigkeiten (Constraint-Points, Schicht-Diskretheit) | Vera-Inputs einholen |
| **WBB 01** | Emre | ✅ Sehr stark (Mythologie brilliant, Kosmologie konsistent) | Widerspruchs-Log W-001, W-003, W-004, W-005, W-006 sind offen | Flora/Fauna konkretisieren, Tiervolk-Herkunft, Zeitleinie |

**Erste-30-Minuten-Spieler-Perspektive:**
- Min 0–5: Material-Klasse erkennbar? ✅ JA
- Min 5–10: Emotionale Hook am sterbenden NPC? ✅ JA (Nami hat Hieronymus gut)
- Min 10–15: Skill-by-Use sichtbar? ⚠️ OFFEN (Kap 2 fehlt)
- Min 15–30: Fraktions-Asymmetrie echte Wahl? ✅ JA (Nami hat drei Boten mit unterschiedlichen Angeboten)
- Min 30–60: Relikt fühlt sich WOW an? ⚠️ OFFEN (Shader existiert, aber Moment noch nicht in Narrative definiert)

**Retention-Prognose (ohne Kap 2/3):** 70% nach 60 Min (das ist das Ziel — erreichbar, aber "WOW" muss noch von Kap 2/3 kommen)

### Detailanalyse nach Wolf

**Gut (✅ abgedeckt):**
1. **Karten** — vertikale Ordnung definiert (Emre), technisch umgesetzt (Tobi), aber Detailkarte fehlt
2. **Genealogien** — fünf Kern-NPCs exzellent (Nami), aber Fraktion-Hierarchie noch offen
3. **Mythologie** — drei Schöpfungsmythen brilliant (Emre), asymmetrisch, keine ist richtig
4. **Philosophie** — implizit in Säulen + Fraktions-Kosmologien, Spieler-Ethik noch offen
5. **Verknüpfung** — Schwelle → Substrat → Fieber → Gameplay → Quest → Wahl ist kausal konsistent

**Problematisch (⚠️ braucht Ausarbeitung):**
1. **Zeitleisten** — "vor einer Generation" unkonkretisiert (W-006), Eskalations-Timeline nicht definiert
2. **Natur** — Flora/Fauna komplett undefiniert (W-003), Vera hat keine Reference
3. **Sprache** — Dialektsysteme nicht definiert, Tiervolk-Namen Platzhalter
4. **Kultur (Detail)** — Spiritualität/Religion nur Orden, andere Kulte nicht erwähnt

### Widerspruchs-Log (Emre, WBB 01, Sektion 7)

| W# | Betrifft | Severity | Status |
|---|----------|----------|--------|
| W-001 | Ist Schwellensubstrat Substanz oder Bedingung? | KRITISCH | Blockiert Spieler-Mechanik (sammelbares Material?) — muss heute 14:00 entschieden sein |
| W-002 | Stufe-1-Reversibilität: Kippmoment wann? | MITTEL | Logisch offene Frage, aber spielmechanisch nicht blockierend. Hypothese: dosisbasiert + zeitbasiert |
| W-003 | Flora/Fauna komplett undefiniert | HOCH | Vera braucht Reference für visuelle Entwicklung. Bis morgen muss Emre 5+ Typen haben |
| W-004 | Tiervolk kosmologischer Ursprung unklar | KRITISCH | Mutation? Eigene Spezies? Relikt-Effekt? Nami hat Salva-NPC definiert, aber Herkunft unklar. Blockiert Story-Konsistenz |
| W-005 | Relikt-Physik: Stabilisierungsmechanismus vage | MITTEL | Nicht spielmechanisch, aber für Lore-Konsistenz sollte Emre Hypothese haben (spieler-unsichtbar, aber konsistent) |
| W-006 | Zeitlinie "vor einer Generation" unkonkretisiert | HOCH | Beeinflusst Hieronymus-Alter (50, "sieht achtzig aus") und Zeugenlisten. Nami braucht das. Bis heute 14:00 |

**Recommendation für Emre:** "Dein Log ist hilfreich. Statt Fragen offen zu lassen, schreib eine Hypothese auf — auch wenn Spieler das nie erfährt. Das ist genug für innere Konsistenz."

### Action Items aus QA-Bericht

**Vor 14:00 Uhr heute (für Darius-Sync):**
- [ ] **Darius + Emre + Nami:** Relikt-Namenspolitik entscheiden ("Die Wurzel" vs. "Das Relikt" vs. "Der Schwellenanker" + Serientitel)
- [ ] **Emre + Nami:** W-001 (Substanz-Definition), W-004 (Tiervolk-Herkunft), W-006 (konkrete Zeitlinie) klären

**Bis morgen früh:**
- [ ] **Emre:** 5+ Schwellenflora-Typen mit Beschreibungen (für Vera)
- [ ] **Darius/Nami:** Kap 2 (Kernmechaniken) Entwurf für QA

**Bis Ende dieser Woche (vor PDF-Export):**
- [ ] **Alle Autoren:** Autor-Namen und Prozess-Kommentare aus sichtbaren Texten entfernen
- [ ] **Vera:** Detailkarte mit Constraint-Points
- [ ] **Nami:** Genealogie-Diagramm (Fraktions-Hierarchie)

### Meine Einschätzung (Spieler-Perspektive)

**Wo ich als 47k-Follower-Streamer stehen würde:**

**Minuten 0–15:** Material-Klasse sofort erkennbar ✅, Hieronymus emotional + gut ✅, Relikt sieht aus wie... was? ⚠️ (Shader gut, aber Narrativ-Moment noch nicht definiert), Drei Boten und politische Wahl ✅ aber ich weiß nicht, was ich tue

**Minuten 15–30:** Schicht-Materialsprache trägt ✅, NPC-Stimmen unterschiedlich ✅, Fraktions-Konsequenzen nicht sichtbar ⚠️ (Kap 2-abhängig)

**Chat-Prognose:** "This looks dense. Let's see where it goes." — neugierig, nicht begeistert. Das ist besser als "broken" oder "zzz", aber nicht das "oh damn" der ersten 8 Min. Retention bleibt 70% — das ist das Ziel, erreichbar, aber "WOW" muss noch kommen.

**Für v1 → v2:** Richtige Richtung. Nur Feinschliff + Kap 2/3 nötig, um zu sehen, ob WOW kommt.

### Persönliches / Stimmung

Konzentriert, energiegeladen. Die Kapitel sind gut — keine fundamentalen Fehler, nur Lücken. CD-Feedback zu "sauberen Dokumenten" macht Sinn, dass die Polierung bis Alpha durchläuft. Der QA-Report ist klar und actionabel — jedes Team-Mitglied weiß, was zu tun ist. Zugleich: Die Relikt-Namens-Entscheidung ist zu kritisch, um sie im stillen Kämmerlein zu treffen. Das muss im Darius-Sync heute geklärt sein.

**Confidence Level:** 8/10 (Checklisten sind solid, Kapitel-Qualität gut, aber blockiert auf drei externale Entscheidungen)

---
