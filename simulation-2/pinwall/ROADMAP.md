# GenSoftworks — Simulation 2 Roadmap

**Projekt:** RELICS — Medieval Cyberpunk CRPG
**Deadline:** Freitag, 28. Februar 2026
**Deliverables:** GDD (6 Kapitel) + WBB (3 Kapitel) + Concept Art + PDF-Snapshots (v0.1–v0.3)

---

## Wochenstruktur

### Montag (✅ Abgeschlossen): Recherche Foundation
**Fokus:** Briefing verstehen, Library durcharbeiten, Team-Setup.

- ✅ Briefing: Tonalität, Genre, Materialsprache, 3 Fraktionen, Schattenfieber-Rahmen
- ✅ Memory initialisieren
- ✅ Recherche parallel (Vera: Materialpalette, Darius: Mechanik-Grundlagen, Nami: Narrative-Struktur, Emre: Architektur, Tobi: Tech-Stack, Leo: QA-Framework)

**Erkenntnis aus Briefing:** Schattenfieber hat EINE biologische Wahrheit. Fraktionen interpretieren unterschiedlich (Propaganda-Layer). Das ist kein Geheimnis, sondern Feature: Mythos zeigt Erzählungen, WBB/GDD enthüllen die Wahrheit.

---

### Dienstag (✅ Abgeschlossen): Recherche + Production Start

#### Bis 09:00 — BRIEFING (Finn moderiert)
- ✅ CD-Feedback integriert:
  - **Schattenfieber:** Eine biologische Wahrheit geklärt, jede Fraktion ihre Interpretation
  - **Relikt:** CD verlangt Brainstorm-Optionen → Vera bekommt Notiz bis 12:30
  - **Release:** Main → Alpha (opt) → Beta → Full → DLCs. Tobi strukturiert Kap 6.
  - **Vera:** Tempo erhöht ab JETZT → Production Phase (Bilder parallel, nicht nach Recherche)
  - **Darius:** Vier offene Fragen bis 17:00 (geklärt für alle anderen)

#### 10:00–12:30 — WORK (parallel)
| Agent | Aufgabe | Kanban | Deadline | ✅ Status |
|-------|---------|--------|----------|----------|
| **Darius** | GDD Kap 1–2: Spielübersicht, Mechaniken + 4 Fragen | Design Foundation | Di 17:00 | ✅ GDD 1 geliefert, Fragen geklärt |
| **Nami** | WBB Kap 1: Mythos-Outline (3 Fraktions-Erzählungen) | Narrative Foundation | Mi 15:00 | ✅ WBB 1 geliefert |
| **Emre** | WBB Kap 2: Topos-Foundation | World Foundation | Mi 15:00 | ✅ WBB 2 geliefert |
| **Vera** | Materialpalette-Finalisierung, dann 12:30 Notiz erhalten | Visual Foundation | Di 12:30 Notiz | ✅ 9 Concept-Art-Bilder generiert |
| **Tobi** | Tech Research: Release-Modell, Engine, Monetarisierung | Tech Foundation | Mi 15:00 | ✅ GDD Kap 6 v1 geliefert |
| **Leo** | QA Framework: Wolf-Checkliste, Konsistenz-Kriterien | Process Foundation | Mi 17:00 | ✅ Checklisten geliefert |
| **Finn** | Notiz für Vera vorbereiten | Roadmap Update | Di 12:30 | ✅ Done |

#### 12:30 — Finn → Vera: Relikt-Brainstorm-Notiz
- ✅ **Handoff erfolgt:** Vera erhält schriftliche Notiz mit CD-Input + Team-Brainstorm

#### 12:30–17:00 — Vera: Relikt-Sketches (Production Phase)
- ✅ **Tempo:** 2–3 Variationen pro Option (explorativ, schnell)
- ✅ **Output:** 9 Concept-Art-Bilder generiert (Relikt, Fraktionspaletten, Stadtschnitt)

#### 17:00 — Darius Deadline: 4 Fragen
- ✅ **Alle 4 Fragen geklärt:**
  1. ✅ **Stadtfrage:** Eine zentrale Stadt (Schwarzrand) ← KLÄRT
  2. ✅ **Schattenfieber-Scope:** Hauptquest-Mechanik (nicht nur Status)
  3. ✅ **Tiervolk:** Kosmologisch offen (keine Entscheidung bis Mi)
  4. ✅ **Release-Strategie:** Main + DLC-Model (Single Release)

#### 18:00 — Vera: Relikt-Sketches liefern
- ✅ **Output:** 9 Bilder generiert (später in `gallery/concepts/` organisiert)

---

### Mittwoch (✅ Abgeschlossen): Production & Cleanup

**Modus:** Cleanup + Polish, HTML-Kommente entfernen, Vera-Bilder integrieren, v0.1 Ready für Export

#### 09:00 — BRIEFING (Küche)
- ✅ CD-Feedback durchgesagt:
  - **HTML-Kommente:** Alle Anmerkungen ins Markdown, nicht im PDF
  - **Bilder-Integration:** Vera-Concept-Art MUSS in GDD/WBB eingebaut sein
  - **Materialpaletten:** Krone + Orden ✅, Gilden-Text kürzen
  - **Relikt:** `hero-shot-aktiviert` + `drei-zustaende-vergleich` (Text weg)
  - **Stadtschnitt:** Skipped diese Version, nächste Iteration
  - **Schwellenanker:** Rename abgeschlossen (alle Agents)

#### 10:00–15:00 — WORK Block (parallel)

| Agent | Aufgabe | Output | Ziel | ✅ Status |
|-------|---------|--------|------|----------|
| **Darius** | Finalisiert GDD Kap 1–3, integriert Vera-Bilder in Kap 5, räumt HTML-Kommentare auf | `.md` | Mi 15:00 | ✅ Delivered |
| **Nami** | Finalisiert WBB Kap 1 + Materialpaletten in Mythos/Ethos, räumt auf | `.md` | Mi 15:00 | ✅ Delivered |
| **Emre** | Finalisiert WBB Kap 2 (Topos), räumt auf | `.md` | Mi 15:00 | ✅ Delivered |
| **Vera** | Gilden-Palette Text kürzen, letzte Renders, räumt Metadaten auf | `.png` | Mi 17:00 | ✅ Delivered |
| **Tobi** | Finalisiert GDD Kap 6, räumt HTML-Kommentare auf | `.md` | Mi 15:00 | ✅ Delivered |
| **Leo** | Konsistenz-Prüfung v0.1, erstellt Feedback-Liste | `.md` (Bericht) | Mi 18:00 | ✅ Delivered |
| **Finn** | **Koordiniert Handoffs**, checkt Bilder-Integration, validiert gegen Briefing, aktualisiert ROADMAP & COMPLETED | Status | Mi 18:00 | ✅ DONE |

#### 15:00–17:00 — WORK Block (Sprintpause)
- Optional: Refinement auf Feedback

#### 17:00 — MEETING (Küche)
- ✅ **Checkpoint:** Alle v0.1 Drafts fertig? Blockers identifizieren?

#### 18:00 — PDF v0.1 exportieren
- ✅ **GDD v0.1:** Kap 1–3, 4, 6 (5 = Do)
- ✅ **WBB v0.1:** Kap 1, 2 (3 = Do)
- ✅ **Concept Art:** 9 Renders (Relikt-States, Fraktions-Paletten)

---

### Donnerstag (🔵 IN PROGRESS): Vertiefung & Konsistenz

**Modus:** Leo-Feedback integrieren, v0.2 Build + Seitenkürzen

#### 09:00 — BRIEFING (CD-Input für Do/Fr)
**Themen:**
- v0.1 Export erfolgreich abgeschlossen
- **Seitenbudget:** Ziel ist max 60 Seiten pro Dokument (GDD + WBB derzeit 70–85 Seiten)
- **Cleanup-Aktion:** Autorenerwähnungen, Checklisten, manche Anhänge entfernen oder in HTML-Kommentare
- **Bilder:** Vera hat $5 Budget → mehr Konzepte (Tiervolk, Environment, Relikt-Hero v2)
- **CD-Clarifications:** Tiervolk = Symbiose, Zeitlinie = Covid-Analogie, Schattenfieber = Körperreaktion

#### 10:00–15:00 — WORK Block (parallel)

| Agent | Aufgabe | Output | Ziel | Status |
|-------|---------|--------|------|--------|
| **Darius** | GDD Kap 5: Art Direction (Bilder komplett, Text optimiert) | `.md` | Do 15:00 | 🔵 In Progress |
| **Nami** | WBB Kap 3: Ethos (Völker, Kulturen, Alltagsleben) + Materialpaletten-Erzählungen | `.md` | Do 15:00 | 🔵 In Progress |
| **Emre** | WBB Kap 2 kürzen, Geographie verfeinern, Wolf-Infrastrukturen abdecken | `.md` | Do 15:00 | 🔵 In Progress |
| **Vera** | Concept Art v0.2 (Tiervolk-Designs, Environment-Iteration, Relikt-Hero v2 Varianten) | `.png` | Do 17:00 | 🔵 In Progress |
| **Tobi** | GDD Kap 6 kürzen, Release-Roadmap, Monetarisierung, Timeline | `.md` | Do 15:00 | 🔵 In Progress |
| **Leo** | Zweiter QA-Pass (Konsistenz, Cross-Referenzen, Lücken), Feedback-Liste aktualisieren | `.md` (Bericht) | Do 18:00 | 🔵 In Progress |
| **Finn** | Seitenbudget-Audit, Ownership-Verteilung Do/Fr, Final-Review-Liste vorbereiten | Status | Do 19:00 | 🔵 ACTIVE |

#### 15:00–17:00 — WORK Block (Sprintpause)
- Optional: Leo-Feedback integrieren, kürzen

#### 17:00 — MEETING (Küche)
- **Checkpoint:** v0.2 Ready? Seitenbudget-Status? Blockers für Freitag?

#### 20:00 — PDF v0.2 exportieren (Zielzeit)
- **GDD v0.2:** Kap 1–5, 6 (alle Kapitel, gekürzt)
- **WBB v0.2:** Kap 1–3 (alle Kapitel)
- **Concept Art:** 9 + ~10 neue Renders (v0.2 erweitert)

---

### Freitag (⏳ PENDING): Final & Submission

**Modus:** Finale Polishing, Korrektionen, Export

#### 09:00 — BRIEFING (Finale CD-Input)
- **Qualitäts-Checkpoint:** Alle Links, Bild-Referenzen, Kapitel-Nummern korrekt?
- **Export-Standard:** PDF-Format sauber, Inhaltsverzeichnis, Seitennummern?

#### 10:00–14:00 — WORK Block (Fehlerkorrektur)
| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Alle** | Final-Review-Liste von Finn durcharbeiten, Fehler korrigieren, Feinschliff | `.md` (aktualisiert) | Fr 14:00 |
| **Vera** | Final-Render v0.3: Alle Bilder, finale Bildordnung für PDF-Layout | `.png` | Fr 16:00 |
| **Finn** | Build PDF v0.3, Format-Check, Links prüfen, Inhaltsverzeichnis, README | `.pdf` + `.md` | Fr 17:00 |

#### 17:30 — Finale PDF v0.3: Submission-Ready

---

## Kanban-Status (Überblick)

```
[BACKLOG] → [RESEARCH] → [DRAFT] → [REVISION] → [FINAL] → [SHIPPED]
   ✅          ✅ (Di)      ✅ (Mi)       🔵 (Do)      ⏳ (Fr)       Fr
```

---

## Offene Fragen / Blocker (Donnerstag 10:00)

**Für CD (geklärt):**
- ✅ Tiervolk = Symbiose-Volk (keine Spielbarkeit nötig)
- ✅ Zeitlinie = Covid-Analogie (Schattenfieber-Trigger)
- ✅ Schattenfieber = biologische Körperreaktion (nicht übernatürlich)

**Für Team (Action Items Do):**
1. **Seitenbudget:** Alle Kapitel auf max 60 Seiten pro Dokument kürzen
2. **GDD Kap 5:** Alle Vera-Bilder eingebaut + Text optimiert (Darius)
3. **WBB Kap 3:** Fertiggestellt + Ethos-Framework vollständig (Nami)
4. **WBB Kap 2:** Gekürzt, verfeinert (Emre)
5. **GDD Kap 6:** Gekürzt, Tech Spec + Release-Roadmap klar (Tobi)
6. **Vera:** Tiervolk + Environment + Relikt-Hero v2 Varianten ($5 Budget)
7. **Leo:** QA-Feedback auf Kürzungen validieren

---

## Seitenbudget-Status (Do 10:00)

**Aktuell (aus v0.1):**
- GDD Kap 1–3: ~21 Seiten (Target: 15–18)
- GDD Kap 4: ~10 Seiten (Target: 8–10) ✅
- GDD Kap 5: ~6 Seiten (Target: 8–12) — wird erweitert
- GDD Kap 6: ~14 Seiten (Target: 12–15)
- **GDD gesamt:** ~51 Seiten (Target: ~50–60) — OK, aber etwas Luft

**WBB:**
- WBB Kap 1: ~9 Seiten (Target: 8–10) ✅
- WBB Kap 2: ~11 Seiten (Target: 10–12) — etwas kürzen
- WBB Kap 3: ~10 Seiten (Target: 10–12) — neu
- **WBB gesamt:** ~30 Seiten (Target: ~30–35) ✅

**Strategie:**
- GDD Kap 5 erweitern (mit Vera-Bildern)
- Kap 1–3 gezielt kürzen (Doppelungen, Details → HTML-Kommentare)
- WBB Kap 2 leicht trimmen
- **Ziel:** GDD ~60 Seiten, WBB ~35 Seiten = ~95 Seiten gesamt (mit Concept Art dann ~115 Seiten Total)

---

## Produkt-Gates

- ✅ **Dienstag 17:00:** Darius-Fragen beantwortet → Vera-Sketches available
- ✅ **Mittwoch 20:00:** v0.1 Lock (QA passt, Feedback aus)
- 🔵 **Donnerstag 20:00:** v0.2 Lock (Konsistenz-Audit bestanden, gekürzt)
- ⏳ **Freitag 17:30:** v0.3 Final (Release Ready)

---

## Ownership & Dependency-Verteilung (Do/Fr)

```
Do 10:00–15:00: Parallel Cleanup + Expansion
├─ Darius: GDD Kap 5 (Art Direction) — hängt von Vera-Bildern ab
├─ Nami: WBB Kap 3 (Ethos) — unabhängig, kann parallel
├─ Emre: WBB Kap 2 Refinement — unabhängig
├─ Vera: Concept Art v0.2 (3–5 Bilder, Tiervolk/Environment)
├─ Tobi: GDD Kap 6 Finalization — unabhängig
├─ Leo: QA-Pass 2 — läuft parallel, Feedback Do 18:00
└─ Finn: Audit + Koordination — wartet auf Do 15:00 Status von allen

Fr 10:00–14:00: Final Review & Fehlerkorrektur
├─ Alle: Finn-Liste durcharbeiten
├─ Vera: Final-Renders (Do v0.2 Bilder + Fr Feinschliff)
└─ Finn: PDF-Build v0.3
```

---

## Notizen für Finn (Do 10:00)

- ✅ **Memory aktualisiert** (gerade gemacht)
- ✅ **ROADMAP aktualisiert** (für Do/Fr Status)
- ✅ **COMPLETED.md aktualisiert** (Mi abgeschlossen, Do In Progress)
- **10:00–11:00:** Seitenbudget-Analyse: Welche Kapitel kürzen?
- **11:00–12:00:** Bildliste für Vera aktualisieren (Tiervolk, Environment, Relikt-Hero v2)
- **12:00–15:00:** Team-Koordination, Handoff-Notizen schreiben
- **15:00–17:00:** Status-Runde (alle Do-Outputs da?)
- **17:00:** MEETING — v0.2 Ready?
- **19:00–21:00:** v0.2 PDF Export starten, QA-Liste für Fr generieren

---

## Repos-Struktur

- Alle Markdown-Outputs → `gallery/gdd/` und `gallery/wbb/`
- Concept Art → `gallery/concepts/` (Versionierung: `day02/`, `day03/` etc.)
- Logs → `traces/`
- **Priorität:** Konsistenz vor Perfektionismus. Kürzen &> Glanz.
