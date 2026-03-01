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

#### 17:00 — MEETING (Küche)
- ✅ **Checkpoint:** Alle v0.1 Drafts fertig, keine Blockers

#### 18:00 — PDF v0.1 exportieren
- ✅ **GDD v0.1:** Kap 1–4, 6 (Kap 5 = Do)
- ✅ **WBB v0.1:** Kap 1, 2 (Kap 3 = Do)
- ✅ **Concept Art:** 9 Renders (Relikt-States, Fraktions-Paletten)

---

### Donnerstag (✅ Abgeschlossen): Vertiefung & Konsistenz

**Modus:** Leo-Feedback integrieren, v0.2 Build + Seitenkürzen

#### 09:00 — BRIEFING (CD-Input für Do/Fr)
- ✅ v0.1 Export erfolgreich
- ✅ **Seitenbudget:** Ziel max 60 Seiten GDD, max 35 Seiten WBB
- ✅ **Cleanup:** Autorenerwähnungen, Checklisten raus/HTML-Kommentare
- ✅ **Vera:** $5 Budget → Tiervolk, Environment, Relikt-Hero v2
- ✅ **CD-Clarifications:** Tiervolk = Symbiose, Zeitlinie = Covid-Analogie, Schattenfieber = Körperreaktion

#### 10:00–15:00 — WORK Block (parallel)

| Agent | Aufgabe | Output | Ziel | ✅ Status |
|-------|---------|--------|------|----------|
| **Darius** | GDD Kap 5: Art Direction (Bilder komplett, Text optimiert) | `.md` | Do 15:00 | ✅ Delivered (v2) |
| **Nami** | WBB Kap 3: Ethos (Völker, Kulturen, Alltagsleben) | `.md` | Do 15:00 | ✅ Delivered (v2) |
| **Emre** | WBB Kap 2 kürzen, Geographie verfeinern | `.md` | Do 15:00 | ✅ Delivered (v2) |
| **Vera** | Concept Art v0.2 (Tiervolk, Environment, Relikt-Hero v2) | `.png` | Do 17:00 | ✅ 8 neue Bilder |
| **Tobi** | GDD Kap 6 kürzen, Release-Roadmap | `.md` | Do 15:00 | ✅ Delivered (v4) |
| **Leo** | QA-Pass 2 (Konsistenz, Cross-Referenzen) | `.md` | Do 18:00 | ✅ Bericht geliefert |
| **Finn** | Seitenbudget-Audit, Ownership Do/Fr | Status | Do 19:00 | ✅ DONE |

#### 17:00 — MEETING
- ✅ v0.2 Ready

#### 20:00 — PDF v0.2 exportieren
- ✅ **GDD v0.2:** Alle 6 Kapitel, 83 PDF-Seiten (über Budget)
- ✅ **WBB v0.2:** Alle 3 Kapitel, 41 PDF-Seiten (im Budget)
- ✅ **Concept Art v0.2:** 17 Renders (9 + 8 neue)
- ✅ **Pinnwand:** 11 Bilder (nach Korrektur)

---

### Freitag (🔴 AKTIV — Letzter Tag): Final & Submission

**Modus:** Radikales Kürzen (GDD 83 → 60 Seiten), Bilder massiv generieren + einbauen, v0.3 Final

#### 09:00 — BRIEFING (Finale CD-Input) ✅
- ✅ **GDD:** 83 PDF-Seiten → max 60 (23 Seiten kürzen!)
- ✅ **WBB:** 41 PDF-Seiten → OK, Luft für mehr Bilder
- ✅ **Pinnwand:** 11 Bilder (nach Korrektur), CD will 10–30
- ✅ **Vera-Budget:** $5–10 (erhöht!) — massiv Bilder generieren
- ✅ **Content-Lock:** 15:00
- ✅ **KEINE weiteren Fragen an CD**

#### 10:00–15:00 — WORK Block (parallel, 🔴 AKTIV)

| Agent | Aufgabe | Output | Ziel | Status |
|-------|---------|--------|------|--------|
| **Darius** | GDD Kap 1, 2, 3, 5 kürzen + Bilder einbauen | `.md` | Fr 15:00 | 🔴 AKTIV |
| **Nami** | GDD Kap 4 kürzen + WBB Kap 1, 3 Bilder einbauen | `.md` | Fr 15:00 | 🔴 AKTIV |
| **Emre** | WBB Kap 2 Bilder einbauen, Dünnstelle vage lassen | `.md` | Fr 15:00 | 🔴 AKTIV |
| **Vera** | Pinnwand korrigieren, massiv Bilder generieren ($5–10) | `.png` | Fr 15:00 | 🔴 AKTIV |
| **Tobi** | GDD Kap 6 kürzen | `.md` | Fr 15:00 | 🔴 AKTIV |
| **Leo** | QA-Pass 3 final (Seitenbudget, Konsistenz, Briefing-Abgleich) | `.md` | Fr 15:00 | 🔴 AKTIV |
| **Finn** | Koordination, ROADMAP/COMPLETED, v0.3 Export | Status | Fr 18:00 | 🔴 AKTIV |

#### 15:00 — CONTENT-LOCK
- Alle Text-Änderungen einfrieren
- Nur noch Bilder-Einbau und Formatierung

#### 17:00 — MEETING (Finaler Check)
- Seitenbudget-Status: GDD unter 60?
- Alle Bilder eingebaut?
- Letzte Korrekturen

#### 18:00–20:00 — PDF v0.3 Final exportieren
- **GDD v0.3:** Alle 6 Kapitel, Ziel max 60 PDF-Seiten
- **WBB v0.3:** Alle 3 Kapitel, Ziel max 35 PDF-Seiten
- **Concept Art v0.3:** 11+ Bilder auf Pinnwand, weitere in Dokumenten
- **SUBMISSION READY**

---

## Kanban-Status (Überblick)

```
[BACKLOG] → [RESEARCH] → [DRAFT] → [REVISION] → [FINAL] → [SHIPPED]
   ✅          ✅ (Di)      ✅ (Mi)    ✅ (Do)      🔴 (Fr)    Fr 20:00
```

---

## Produkt-Gates

- ✅ **Dienstag 17:00:** Darius-Fragen beantwortet → Vera-Sketches available
- ✅ **Mittwoch 20:00:** v0.1 Lock (QA passt, Feedback aus)
- ✅ **Donnerstag 20:00:** v0.2 Lock (alle Kapitel, 83+41 Seiten)
- 🔴 **Freitag 15:00:** Content-Lock (Text eingefroren)
- 🔴 **Freitag 18:00–20:00:** v0.3 Final (Submission Ready)

---

## Seitenbudget-Status (Fr 10:00)

**v0.2 Ist-Stand (aus PDF-Export):**
- **GDD v0.2:** 83 PDF-Seiten (Target: max 60) — **23 Seiten über Budget!**
- **WBB v0.2:** 41 PDF-Seiten (Target: max 35) — im Budget, Luft für Bilder

**Kürzungsstrategie Freitag:**
- GDD Kap 1–3: Doppelungen eliminieren, Details in HTML-Kommentare
- GDD Kap 4: Figuren-Beschreibungen straffen
- GDD Kap 5: Bilder statt Fließtext (Concept Art spricht für sich)
- GDD Kap 6: Technische Details kürzen, Tabellen komprimieren
- WBB: Bilder einbauen, Text halten oder leicht kürzen

**Ziel v0.3:**
- GDD: max 60 PDF-Seiten
- WBB: max 35 PDF-Seiten (mit mehr Bildern)

---

## Pinnwand-Status (Fr 10:00)

**Aktuell: 11 Bilder auf Pinnwand** (`pinwall/favorites/`)
1. fraktion-gilden-materialpalette-v2_nano-banana-2
2. fraktion-krone-materialpalette_seedream-4-5
3. fraktion-orden-materialpalette_seedream-4-5
4. relikt-drei-zustaende-v2_nano-banana-pro
5. relikt-hero-shot-aktiviert_gpt-image-1-5
6. relikt-hero-v2_nano-banana-pro
7. stadtschnitt-kanalzone-v3-final_gpt-image-1-5
8. stadtschnitt-kanalzone-v3_nano-banana-2
9. tiervolk-diebin-marder-exploration_seedream-4-5
10. tiervolk-haendler-fuchs-exploration_seedream-4-5
11. tiervolk-marktszene-exploration_seedream-4-5

**Vera-Budget heute:** $5–10 → massiv erweitern (CD will 10–30 Bilder auf Pinnwand)

---

## Repos-Struktur

- Alle Markdown-Outputs → `gallery/gdd/` und `gallery/wbb/`
- Concept Art → `gallery/concepts/` (Versionierung: `day02/`, `day03/`, `day04/`, `day05/`)
- Pinnwand-Favoriten → `pinwall/favorites/`
- Logs → `traces/`
- **Priorität:** Kürzen vor Glanz. Seitenbudget einhalten.
