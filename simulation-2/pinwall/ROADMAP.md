# GenSoftworks — Simulation 2 Roadmap

**Projekt:** RELICS — Medieval Cyberpunk CRPG
**Deadline:** Freitag, 28. Februar 2026
**Deliverables:** GDD (6 Kapitel) + WBB (3 Kapitel) + Concept Art + PDF-Snapshots (v0.1–v0.3)

---

## Wochenstruktur

### Montag–Dienstag: Recherche & Worldbuilding Foundation
**Fokus:** Tiefe statt Breite. Jeder Agent erfasst die Kerninformationen für sein Kapitel.

| Agent | Aufgabe | Kanban | Deadline |
|-------|---------|--------|----------|
| **Darius** (CD) | GDD Kap 1–2: Spielübersicht, Designsäulen, Kernmechaniken brainstormen | Design Foundation | Di 17:00 |
| **Nami** | WBB Kap 1: Mythos (Kosmologie, Schöpfung, Schattenseuche-Lore) | Narrative Foundation | Di 17:00 |
| **Emre** | WBB Kap 2: Topos (Geographie, Kernregion, Architektur, Karten-Outline) | World Foundation | Di 17:00 |
| **Vera** | Concept Art Foundation (Materialsprache, Silhouetten, Fraktions-Palette) + **Stadtfrage klären** (CD-Input) | Visual Foundation | Di 17:00 |
| **Tobi** | Tech Research: Engine, Pipeline, Monetarisierung, Release-Modell | Tech Foundation | Di 17:00 |
| **Leo** | QA Framework: Vollständigkeits-Checkliste (Wolf 2013), Konsistenz-Prüfpunkte | Process Foundation | Di 17:00 |
| **Finn** (Produktion) | Roadmap + Sprint-Planung, Blocker identifizieren, Info-Flow organisieren | Roadmap | Mo 17:00 |

---

### Mittwoch–Freitag: Produktion & PDF-Exports

#### Mittwoch (v0.1)
**Modus:** Erste vollständige Fassungen aller Kapitel (Draft-Qualität)

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Darius** | GDD Kap 1–3: Spielübersicht, Kernmechaniken, Erzählkonzept (Draft) | `.md` | Mittwoch 15:00 |
| **Nami** | GDD Kap 4: Schlüsselfiguren & NPCs (Draft) + WBB Kap 1 Draft | `.md` | Mittwoch 15:00 |
| **Emre** | WBB Kap 2: Topos (Draft) + Klastrup/Tosca-Abdeckung | `.md` | Mittwoch 15:00 |
| **Vera** | Concept Art v0.1 (10–15 Bilder: Charaktere, Umgebungen, Rüstung, Materialpalette) | `.png` | Mittwoch 17:00 |
| **Tobi** | GDD Kap 6: Tech Spec & Produktion (Draft) | `.md` | Mittwoch 15:00 |
| **Leo** | QA-Pass über alle Draft-Kapitel, Konsistenz-Feedback | `.md` (Bericht) | Mittwoch 18:00 |
| **Finn** | Qualität-Review, Leo-Feedback aggregieren, Blocker notieren | Sprint-Anpassung | Mittwoch 18:00 |

**PDF v0.1 um Mittwoch 20:00:** GDD + WBB + Concept Art Preview

---

#### Donnerstag (v0.2)
**Modus:** Vertiefung, Leo-Feedback integrieren, Konsistenz prüfen

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Darius** | GDD Kap 5: Art Direction (unter Vera-Input) | `.md` | Donnerstag 15:00 |
| **Nami** | WBB Kap 3: Ethos (Völker, Kulturen, Alltagsleben) + Fraktions-Deep-Dive | `.md` | Donnerstag 15:00 |
| **Emre** | Geographie verfeinern, Wolf-Infrastrukturen abdecken (Zeitleisten, Genealogien) | `.md` | Donnerstag 15:00 |
| **Vera** | Concept Art v0.2 (Iteration auf Feedback: +5–10 Bilder, Detailvertiefung) | `.png` | Donnerstag 17:00 |
| **Tobi** | Release-Roadmap, Monetarisierung, Risiken & Timeline (Kapitel 6 finalisieren) | `.md` | Donnerstag 15:00 |
| **Leo** | Zweiter QA-Pass, Cross-Referenzen prüfen, Lücken identifizieren | `.md` (Bericht) | Donnerstag 18:00 |
| **Finn** | Aggregation, Konsistenz-Audit, Final-Review-Liste für Freitag | Status | Donnerstag 19:00 |

**PDF v0.2 um Donnerstag 21:00:** GDD + WBB + Concept Art (erweitert)

---

#### Freitag (v0.3 & Final)
**Modus:** Finale Polishing, Fehlerkorrekturen, Export

| Agent | Aufgabe | Output | Ziel |
|-------|---------|--------|------|
| **Alle** | Final-Review-Liste von Finn durcharbeiten, Fehler korrigieren, Lücken schließen | `.md` (aktualisiert) | Freitag 14:00 |
| **Vera** | Final-Render (Concept Art v0.3): Alle Bilder, finale Ordnung für PDF | `.png` | Freitag 16:00 |
| **Finn** | Build PDF v0.3, Format-Check, Links prüfen, README generieren | `.pdf` | Freitag 17:00 |

**Finale PDF v0.3 um Freitag 17:30:** Submission-Ready

---

## Offene Fragen für Creative Director

1. **Stadtfrage (Vera):** Eine zentrale Stadt oder mehrere überlagerte Städte (vertikal/temporal)? Implikation für Worldmap und Questline.
2. **Schattenfieber-Narrative:** Ist es nur ein Statuseffekt oder ein narrative Arc im Hauptquest?
3. **Tiervolk-Relevanz:** Spielbar? Quest-Giver? Oder NPC-Flavor nur?
4. **Release-Strategie:** Single-Release oder Episodisch? Budget-Implikation für Tobi.

---

## Kanban-Status (Überblick)

```
[BACKLOG] → [RESEARCH] → [DRAFT] → [REVISION] → [FINAL] → [SHIPPED]
   ✓            ✓           ◀ Do        Do–Fr        Fr          Fr
```

---

## Produkt-Gates

- **Mittwoch 20:00:** v0.1 Lock (QA passt, Feedback aus)
- **Donnerstag 21:00:** v0.2 Lock (Konsistenz-Audit bestanden)
- **Freitag 17:30:** v0.3 Final (Release Ready)

---

## Anmerkungen für Finn

- **Priorität:** Vollständigkeit vor Glanz. Ein Draft ist besser als kein Draft.
- **Info-Fluss:** Täglich (Mi–Fr 18:00) Sprint-Sync mit Darius & Leo, um Blocker zu identifizieren.
- **Vera-Stadtfrage:** CD-Input bis Dienstag einholen, sonst weitermachen mit Annahme: eine vertikale Stadt (Cyberpunk-Standard).
- **PDF-Snapshots:** Automatisiert ab Mittwoch (täglich um 20:00, via Pandoc-Export)
- **Repos-Struktur:** Alle Markdown-Outputs → `gallery/gdd/` und `gallery/wbb/`. Concept Art → `gallery/concepts/day01/` bis `day05/`. Logs → `traces/`.
