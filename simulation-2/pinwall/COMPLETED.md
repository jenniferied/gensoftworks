# GenSoftworks — Status & Open Questions

## Open Questions für Creative Director (Darius)

**Priorität: Bis Dienstag 17:00 klären — wirkt auf alle Kapitel**

### 1. Stadtfrage (Art Direction & Worldbuilding)
**Kontext:** Vera muss wissen, wie viele Städte es gibt und wie sie strukturiert sind.
- **Option A:** Eine zentrale Stadt (vertikal geschichtet: Oberschicht–Mittelschicht–Slums)
- **Option B:** Mehrere Städte, überlagert (temporal oder spatial) — z.B. Stadt als Ruine mit neuer Siedlung drüber
- **Implikation:** Karten-Aufteilung, Quest-Geographie, Concept Art Schwerpunkt
- **Entscheidung erforderlich:** JA / verantwortlich: Darius
- **Status:** ⏳ Pending

### 2. Schattenfieber als narrative Arc oder Mechanic?
**Kontext:** Nami (Narrative) und Tobi (Tech) müssen es wissen.
- **Ist Schattenfieber nur ein Statuseffekt?** (wie Vergiftung in Skyrim) Oder ein hauptquest-antreibender Plot-Punkt?
- **Hat es eine Heilung?** Oder ist es permanent?
- **Implikation:** Quest-Struktur, Charakter-Builds, Gameplay-Balance
- **Status:** ⏳ Pending

### 3. Tiervolk als spielbar oder nur NPC?
**Kontext:** Emre (Worldbuilding) muss Kultur & Ethos definieren.
- **Spielbar als Charakter-Rasse?** (wie in Elder Scrolls)
- **Oder nur als Quest-Giver & Merchant-Flavor?** (wie in Witcher 3)
- **Implikation:** Character Creation Menü, Startzonen, NPC-Netzwerk
- **Status:** ⏳ Pending

### 4. Release-Strategie & Budget
**Kontext:** Tobi (Tech) muss Timeline & Scope definieren.
- **Single Release** (komplett 2028+) oder **episodisch** (3 Episoden, je 1 Jahr)?
- **Monetarisierung:** Premium AAA oder Indie-Budget?
- **Plattformen:** PC only oder auch Konsole?
- **Implikation:** GDD Kap 6 (Tech & Produktion), Team-Sizing, Asset-Pipeline
- **Status:** ⏳ Pending

---

## Status by Chapter

| Kapitel | Verantwortlich | Phase | Status | Deadline |
|---------|----------------|-------|--------|----------|
| **GDD Kap 1** — Spielübersicht & Säulen | Darius | Research → Draft | 🔵 In Progress | Mi 15:00 |
| **GDD Kap 2** — Kernmechaniken | Darius | Research → Draft | 🔵 In Progress | Mi 15:00 |
| **GDD Kap 3** — Erzählkonzept | Darius | Research → Draft | 🔵 In Progress | Mi 15:00 |
| **GDD Kap 4** — Schlüsselfiguren & NPCs | Nami | Research → Draft | 🔵 In Progress | Mi 15:00 |
| **GDD Kap 5** — Art Direction | Darius + Vera | Research | ⏳ Pending | Do 15:00 |
| **GDD Kap 6** — Technik & Produktion | Tobi | Research | ⏳ Pending | Mi 15:00 |
| **WBB Kap 1** — Mythos | Nami | Research → Draft | 🔵 In Progress | Mi 15:00 |
| **WBB Kap 2** — Topos | Emre | Research → Draft | 🔵 In Progress | Mi 15:00 |
| **WBB Kap 3** — Ethos | Nami + Emre | Research | ⏳ Pending | Do 15:00 |
| **Concept Art v0.1–v0.3** | Vera | Research → Render | 🔵 In Progress | Do 17:00 |
| **QA & Konsistenz** | Leo | All phases | 🔵 In Progress | Fr 17:00 |

---

## Blockers (aktuell)

**Keine technischen Blocker. Alle recherchieren parallel.**

Mögliche Verzögerungen:
- Vera wartet auf Darius-Input für Stadtstruktur (Mi Früh)
- Tobi wartet auf Darius-Input für Release-Strategie (Mi Früh)

---

## Notizen für Simulation 2

- **Forschungsmodus:** Mo–Di alle in `library/` recherchieren. Keine Git-Commits nötig — nur lokale Notizen.
- **Produktionsmodus:** Mi–Fr alle `.md` direktet nach `gallery/gdd/` oder `gallery/wbb/` committen.
- **Concept Art:** Vera speichert Prompts & Renders nach `gallery/concepts/day{N}/` (mit Subfoldern: `charaktere/`, `environments/`, `waffen/`, `mode/`)
- **PDF-Export:** Finn triggert täglich (Mi–Fr 20:00) via Pandoc — Snapshot mit Timestamp.
- **Memory Updates:** Alle Agenten aktualisieren eigene Memory nach jedem Workday (Erkenntnisse, offene Fragen, Nächste Schritte).

---

## Freitag-Checklist (Finn)

- [ ] Alle `.md` Dateien reviewed (Leo-QA bestanden)
- [ ] Concept Art in finale Ordnung sortiert
- [ ] PDF v0.3 kompiliert & Preview geprüft
- [ ] Git-Commit: `final: simulation-2 gdd+wbb v0.3 complete`
- [ ] README mit Kapitel-Übersicht generiert
- [ ] Archive ready (für Export)
