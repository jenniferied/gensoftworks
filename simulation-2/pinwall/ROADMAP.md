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
| **Emre** | WBB Kap 2: Topos-Foundation | World Foundation | Mi 15:00 | 🔵 In Progress |
| **Vera** | Materialpalette-Finalisierung, dann 12:30 Notiz erhalten | Visual Foundation | Di 12:30 Notiz | ✅ Prompts vorbereitet, Rendering läuft |
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

### Mittwoch (🔵 IN PROGRESS): Production & Cleanup

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

| Agent | Aufgabe | Output | Ziel | 🔵 Status |
|-------|---------|--------|------|----------|
| **Darius** | Finalisiert GDD Kap 1–3, integriert Vera-Bilder in Kap 5, räumt HTML-Kommentare auf | `.md` | Mi 15:00 | 🔵 In Progress |
| **Nami** | Finalisiert WBB Kap 1 + Materialpaletten in Mythos/Ethos, räumt auf | `.md` | Mi 15:00 | 🔵 In Progress |
| **Emre** | Finalisiert WBB Kap 2 (Topos), räumt auf | `.md` | Mi 15:00 | ⏳ Pending |
| **Vera** | Gilden-Palette Text kürzen, letzte Renders, räumt Metadaten auf | `.png` | Mi 17:00 | 🔵 In Progress |
| **Tobi** | Finalisiert GDD Kap 6, räumt HTML-Kommentare auf | `.md` | Mi 15:00 | ⏳ Pending |
| **Leo** | Konsistenz-Prüfung v0.1, erstellt Feedback-Liste | `.md` (Bericht) | Mi 18:00 | 🔵 In Progress |
| **Finn** | **Koordiniert Handoffs**, checkt Bilder-Integration, validiert gegen Briefing, aktualisiert ROADMAP & COMPLETED | Status | Mi 18:00 | 🔵 ACTIVE |

#### 15:00–17:00 — WORK Block (Sprintpause)
- Optional: Refinement auf Feedback

#### 17:00 — MEETING (Küche)
- **Checkpoint:** Alle v0.1 Drafts fertig? Blocker identifizieren?

#### 18:00 — PDF v0.1 exportieren
- **GDD v0.1:** Kap 1–3, 4, 6 (5 = Do)
- **WBB v0.1:** Kap 1, 2 (3 = Do)
- **Concept Art:** 9 Renders (Relikt-States, Fraktions-Paletten, Stadtschnitt-optional)

---

### Donnerstag (⏳ PENDING): Vertiefung & Konsistenz

**Modus:** Leo-Feedback integrieren, v0.2 Build

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Darius** | GDD Kap 5: Art Direction (unter Vera-Input) | `.md` | Do 15:00 |
| **Nami** | WBB Kap 3: Ethos (Völker, Kulturen, Alltagsleben) + Fraktions-Deep-Dive | `.md` | Do 15:00 |
| **Emre** | Geographie verfeinern, Wolf-Infrastrukturen abdecken | `.md` | Do 15:00 |
| **Vera** | Concept Art v0.2 (Iteration: +5–10 Bilder, Stadtschnitt v1 neu) | `.png` | Do 17:00 |
| **Tobi** | Release-Roadmap, Monetarisierung, Timeline | `.md` | Do 15:00 |
| **Leo** | Zweiter QA-Pass, Cross-Referenzen, Lücken identifizieren | `.md` (Bericht) | Do 18:00 |
| **Finn** | Aggregation, Konsistenz-Audit, Final-Review-Liste vorbereiten | Status | Do 19:00 |

**PDF v0.2 um Donnerstag 21:00:** GDD + WBB (+ Concept Art, erweitert)

---

### Freitag (⏳ PENDING): Final & Submission

**Modus:** Finale Polishing, Korrektionen, Export

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Alle** | Final-Review-Liste von Finn durcharbeiten, Fehler korrigieren | `.md` (aktualisiert) | Fr 14:00 |
| **Vera** | Final-Render v0.3: Alle Bilder, finale Ordnung für PDF | `.png` | Fr 16:00 |
| **Finn** | Build PDF v0.3, Format-Check, Links prüfen, README | `.pdf` | Fr 17:00 |

**Finale PDF v0.3 um Freitag 17:30:** Submission-Ready

---

## Kanban-Status (Überblick)

```
[BACKLOG] → [RESEARCH] → [DRAFT] → [REVISION] → [FINAL] → [SHIPPED]
   ✅          ✅ (Di)      ◀ Mi         Do–Fr        Fr          Fr
```

---

## Offene Fragen / Blocker (Mittwoch 10:00)

**Für CD (noch offen):**
- ❌ **Keine blockierenden Fragen mehr** — alle 4 Darius-Fragen geklärt

**Für Team (Action Items):**
1. Darius: GDD Kap 1–3 finalisieren + Vera-Bilder in Kap 5 einbauen
2. Nami: Materialpaletten-Visuals in Mythos/Ethos einflechten
3. Vera: Gilden-Palette Text kürzen, Metadaten bereinigen
4. Tobi: GDD Kap 6 HTML-Kommentare entfernen
5. Emre: WBB Kap 2 finalisieren
6. Leo: Konsistenz-Pass + Feedback-Liste erstellen

---

## Produkt-Gates

- **Dienstag 17:00:** ✅ Darius-Fragen beantwortet → Vera-Sketches available
- **Mittwoch 20:00:** 🔵 v0.1 Lock (QA passt, Feedback aus)
- **Donnerstag 21:00:** ⏳ v0.2 Lock (Konsistenz-Audit bestanden)
- **Freitag 17:30:** ⏳ v0.3 Final (Release Ready)

---

## Notizen für Finn (Mi 10:00)

- ✅ **ROADMAP aktualisiert** (gerade) — Dienstag geschlossen, Mittwoch mit Status aktuell
- ✅ **Bildliste für Darius schreiben** — welche Vera-Bilder in welche Kapitel (HANDOFF-Notiz)
- **10:00–12:00:** Runde durch Repo fahren, HTML-Kommentar-Status checken
- **12:00–13:00:** Bildliste finalisieren + an Darius geben
- **17:00:** MEETING — alle v0.1 Ready?
- **18:00:** PDF Export starten

---

## Repos-Struktur

- Alle Markdown-Outputs → `gallery/gdd/` und `gallery/wbb/`
- Concept Art → `gallery/concepts/` (später: `day02/`, `day03/` etc. für Versionierung)
- Logs → `traces/`
- **Priorität:** Vollständigkeit vor Glanz. Ein Draft ist besser als Lähmung.
