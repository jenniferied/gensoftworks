# GenSoftworks — Simulation 2 Roadmap

**Projekt:** RELICS — Medieval Cyberpunk CRPG
**Deadline:** Freitag, 28. Februar 2026
**Deliverables:** GDD (6 Kapitel) + WBB (3 Kapitel) + Concept Art + PDF-Snapshots (v0.1–v0.3)

---

## Wochenstruktur

### Montag (Abgeschlossen): Recherche Foundation
**Fokus:** Briefing verstehen, Library durcharbeiten, Team-Setup.

- ✅ Briefing: Tonalität, Genre, Materialsprache, 3 Fraktionen, Schattenfieber-Rahmen
- ✅ Memory initialisieren
- ✅ Recherche parallel (Vera: Materialpalette, Darius: Mechanik-Grundlagen, Nami: Narrative-Struktur, Emre: Architektur, Tobi: Tech-Stack, Leo: QA-Framework)

**Erkenntnis aus Briefing:** Schattenfieber hat EINE biologische Wahrheit. Fraktionen interpretieren unterschiedlich (Propaganda-Layer). Das ist kein Geheimnis, sondern Feature: Mythos zeigt Erzählungen, WBB/GDD enthüllen die Wahrheit.

---

### Dienstag (HEUTE): Recherche + Production Start + Relikt-Brainstorm

#### Bis 09:00 — BRIEFING (Finn moderiert)
- ✅ CD-Feedback integriert:
  - **Schattenfieber:** Nicht "offene Frage" → **geklärt:** Eine biologische Wahrheit, jede Fraktion ihre Interpretation
  - **Relikt:** CD verlangt Brainstorm-Optionen → Vera bekommt Notiz bis 12:30
  - **Release:** Main → Alpha (opt) → Beta → Full → DLCs. Tobi strukturiert Kap 6.
  - **Vera:** Tempo erhöht ab JETZT → Production Phase (Bilder parallel, nicht nach Recherche)
  - **Darius:** Vier offene Fragen bis 17:00 (geklärt für alle anderen)

#### 10:00–12:30 — WORK (parallel)
| Agent | Aufgabe | Kanban | Deadline |
|-------|---------|--------|----------|
| **Darius** | GDD Kap 1–2: Spielübersicht, Mechaniken + **4 Fragen beantworten** | Design Foundation | Di 17:00 |
| **Nami** | WBB Kap 1: Mythos-Outline (3 Fraktions-Erzählungen zu Schattenfieber) + **Di 14:00 Input-Check** | Narrative Foundation | Mi 15:00 |
| **Emre** | WBB Kap 2: Topos-Foundation (Stadtfrage-Status bis Mi morgen) | World Foundation | Mi 15:00 |
| **Vera** | Concept Art: Materialpalette-Finalisierung, dann **12:30 Notiz von Finn erhalten** | Visual Foundation | Di 12:30 Notiz, Di 18:00 Sketches |
| **Tobi** | Tech Research: Release-Modell, Engine-Decision, Monetarisierung (abhängig Darius-Input) | Tech Foundation | Mi 15:00 |
| **Leo** | QA Framework: Wolf-Checkliste finalisieren, Konsistenz-Kriterien | Process Foundation | Mi 17:00 |
| **Finn** | Notiz für Vera vorbereiten (Relikt-Brainstorm-Optionen) | Roadmap Update | Di 12:30 |

#### 12:30 — Finn → Vera: Relikt-Brainstorm-Notiz
**Handoff:** Finn gibt Vera schriftliche Notiz mit CD-Input + Team-Brainstorm zu Relikt-Optionen.

#### 12:30–17:00 — Vera: Relikt-Sketches (Production Phase)
- **Tempo:** 2–3 Variationen pro Option (explorativ, schnell)
- **Output:** Sketches/Renders bis 18:00 in `simulation-2/gallery/concepts/day02/`

#### 14:00 — Finn ↔ Nami: Input-Check (5 min)
**Ziel:** Nami weiß, was sie von Darius/anderen braucht, um Mythos-Outline zu finalisieren.

#### 16:00 — Finn ↔ Darius: CD-Status-Check
**Ziel:** Darius hat seine 4 Fragen nach 17:00 beantwortet? Erste Checks.

#### 17:00 — Darius Deadline: 4 Fragen
1. **Stadtfrage:** Eine zentrale Stadt oder mehrere überlagert?
2. **Schattenfieber-Scope:** Statuseffekt oder hauptquest-Plot?
3. **Tiervolk:** Spielbar oder NPC-only?
4. **Release-Strategie:** Single oder Episodisch?

**Format:** Kurz, klar, nicht poliert. Finn leitet weiter.

#### 18:00 — Vera: Relikt-Sketches liefern
**Output:** `simulation-2/gallery/concepts/day02/` (getagged mit Optionen-Namen)

---

### Mittwoch–Freitag: Production & PDF-Exports

#### Mittwoch (v0.1)
**Modus:** Erste vollständige Fassungen aller Kapitel (Draft-Qualität)

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Darius** | GDD Kap 1–3: Spielübersicht, Kernmechaniken, Erzählkonzept (Draft) | `.md` | Mi 15:00 |
| **Nami** | GDD Kap 4: Schlüsselfiguren & NPCs (Draft) + WBB Kap 1 Draft | `.md` | Mi 15:00 |
| **Emre** | WBB Kap 2: Topos (Draft) + Klastrup/Tosca-Abdeckung | `.md` | Mi 15:00 |
| **Vera** | Concept Art v0.1 (10–15 Bilder: Charaktere, Umgebungen, Rüstung, Materialpalette) | `.png` | Mi 17:00 |
| **Tobi** | GDD Kap 6: Tech Spec & Produktion (Draft) — mit Darius-Input von Di 17:00 | `.md` | Mi 15:00 |
| **Leo** | QA-Pass über alle Draft-Kapitel, Konsistenz-Feedback | `.md` (Bericht) | Mi 18:00 |
| **Finn** | Qualität-Review, Leo-Feedback aggregieren, Blocker notieren | Sprint-Anpassung | Mi 18:00 |

**PDF v0.1 um Mittwoch 20:00:** GDD + WBB + Concept Art Preview

---

#### Donnerstag (v0.2)
**Modus:** Vertiefung, Leo-Feedback integrieren, Konsistenz prüfen

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Darius** | GDD Kap 5: Art Direction (unter Vera-Input) | `.md` | Do 15:00 |
| **Nami** | WBB Kap 3: Ethos (Völker, Kulturen, Alltagsleben) + Fraktions-Deep-Dive | `.md` | Do 15:00 |
| **Emre** | Geographie verfeinern, Wolf-Infrastrukturen abdecken (Zeitleisten, Genealogien) | `.md` | Do 15:00 |
| **Vera** | Concept Art v0.2 (Iteration auf Feedback: +5–10 Bilder, Detailvertiefung) | `.png` | Do 17:00 |
| **Tobi** | Release-Roadmap, Monetarisierung, Risiken & Timeline (Kapitel 6 finalisieren) | `.md` | Do 15:00 |
| **Leo** | Zweiter QA-Pass, Cross-Referenzen prüfen, Lücken identifizieren | `.md` (Bericht) | Do 18:00 |
| **Finn** | Aggregation, Konsistenz-Audit, Final-Review-Liste für Freitag | Status | Do 19:00 |

**PDF v0.2 um Donnerstag 21:00:** GDD + WBB + Concept Art (erweitert)

---

#### Freitag (v0.3 & Final)
**Modus:** Finale Polishing, Fehlerkorrektionen, Export

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Alle** | Final-Review-Liste von Finn durcharbeiten, Fehler korrigieren, Lücken schließen | `.md` (aktualisiert) | Fr 14:00 |
| **Vera** | Final-Render (Concept Art v0.3): Alle Bilder, finale Ordnung für PDF | `.png` | Fr 16:00 |
| **Finn** | Build PDF v0.3, Format-Check, Links prüfen, README generieren | `.pdf` | Fr 17:00 |

**Finale PDF v0.3 um Freitag 17:30:** Submission-Ready

---

## Kanban-Status (Überblick)

```
[BACKLOG] → [RESEARCH] → [DRAFT] → [REVISION] → [FINAL] → [SHIPPED]
   ✅          ✅ (Di)      ◀ Mi         Do–Fr        Fr          Fr
```

---

## Offene Fragen für Creative Director (Darius) — Deadline: Di 17:00

### Noch zu klären:
1. **Stadtfrage (Vera, Emre):** Eine zentrale Stadt oder mehrere überlagerte? → Implikation: Worldmap, Quest-Geographie
2. **Tiervolk (Emre):** Spielbar oder NPC-only? → Implikation: Character Creation, Startzonen
3. **Relikt-Entscheidung (CD solo):** Welche Option aus Vera-Sketches wird erste Iteration?

### Bereits geklärt (aus Briefing Di 09:00):
- ✅ **Schattenfieber:** Eine biologische Wahrheit (nicht Geheimnis). Fraktionen interpretieren unterschiedlich.
- ✅ **Release-Modell:** Main + Alpha (opt) + Beta + Full + DLCs.
- ✅ **Vera-Tempo:** Production Phase ab sofort (Bilder parallel, nicht nach Recherche).

---

## Produkt-Gates

- **Dienstag 17:00:** Darius-Fragen beantwortet → Vera-Sketches available → Nami-Input klar
- **Mittwoch 20:00:** v0.1 Lock (QA passt, Feedback aus)
- **Donnerstag 21:00:** v0.2 Lock (Konsistenz-Audit bestanden)
- **Freitag 17:30:** v0.3 Final (Release Ready)

---

## Anmerkungen für Finn

- **Info-Fluss:** Täglich (Mi–Fr 18:00) Sprint-Sync mit Darius & Leo, um Blocker zu identifizieren.
- **Vera-Priorität:** Di 12:30 Notiz mit Relikt-Brainstorm-Optionen. Di 18:00 Sketches review. Mi morgen weitergeben für Darius-Entscheidung.
- **Nami-Sync:** Di 14:00 (5 min) Input-Check.
- **Darius-Status:** Di 16:00 Check, Di 17:00 4-Fragen-Deadline.
- **PDF-Snapshots:** Automatisiert ab Mittwoch (täglich um 20:00, via Pandoc-Export).
- **Repos-Struktur:** Alle Markdown-Outputs → `gallery/gdd/` und `gallery/wbb/`. Concept Art → `gallery/concepts/day{N}/`. Logs → `traces/`.
- **Priorität:** Vollständigkeit vor Glanz. Ein Draft ist besser als Lähmung.

---

## Notizen zur Simulation 2

- **Forschungsmodus:** Mo–Di alle in `library/` recherchieren.
- **Produktionsmodus:** Mi–Fr alle `.md` direkt nach `gallery/gdd/` oder `gallery/wbb/` committen.
- **Memory Updates:** Alle Agenten aktualisieren eigene Memory nach jedem Workday.
