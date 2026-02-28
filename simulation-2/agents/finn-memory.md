# Finn — Memory (Simulation 2)

## Briefing & Vision (Mo 10:00)

**RELICS:** Medieval Cyberpunk CRPG — Fantasy-Welt an historischem Wendepunkt.
- **Tonalität:** Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.
- **Genre:** Third-/First-Person Open-World, Medium-Fantasy, Low-Magic High-Tech, Biotech-Futurismus.
- **KEINE:** Steampunk, High Fantasy, Science-Fantasy, klassische Magie, Anachronismen.

**Kernelemente (Briefing-Seite 49–100):**
- Medieval Epoche (Spätmittelalter), Mitteleuropa-Setting, Germanische Mythologie (Inspiration)
- Cyberpunk als Struktur: Technologischer Fortschritt erzeugt Ungleichheit (Material-Beherrschung statt Digital)
- Materialsprache definiert sozialen Status: Oberschicht (Edelmetalle, Kristallglas, Monochromatik + ein Akzent) → Mittelschicht (gehärteter Stahl, Leinen, Erdtöne) → Unterschicht (Eisen, Knochen, Flick-Stoffe)
- Architektur: Vertikal geschichtet (Brutalist/Bauhaus-Elemente), Handwerksviertel, Slums unter Brücken versteckt
- **Drei Fraktionen (keine ist gut/böse):** Die Krone (Feudalmonarchie im Verfall) | Die Gilden (Handels-/Handwerksmonopole) | Der Orden (Religiös-militärisch, Bildungsmonopol)
- **Einziges Übernatürliche:** Schattenfieber — eine Seuche, die Opfer verändert

**Deliverables:**
- **GDD:** 6 Kapitel (Spielübersicht, Kernmechaniken, Erzählkonzept, Schlüsselfiguren, Art Direction, Technik & Produktion)
- **WBB:** 3 Kapitel (Mythos, Topos, Ethos) — basierend auf Klastrup/Tosca
- **Concept Art:** Charaktere, Umgebungen, Rüstung, Materialpalette (High Fashion Medieval + Biotech)
- **Seite Budget:** je 30–45 Seiten inkl. Concept Art
- **Deadline:** Freitag (28.2.2026), PDF-Snapshots Mi–Fr (v0.1–v0.3)

## Team & Rollen

| Agent | Rolle | Kanban-Fokus |
|-------|-------|--------------|
| **Darius Engel** | Creative Director, Game Designer | GDD Kap 1–3 (Spielübersicht, Mechaniken, Narrative) + Kap 5 (Art Direction) |
| **Nami Okafor** | Narrative Designer | GDD Kap 4 (Schlüsselfiguren) + WBB Kap 1 (Mythos) + WBB Kap 3 (Ethos) |
| **Emre Yilmaz** | World Builder | WBB Kap 2 (Topos) + Geographie, Architektur, Karten |
| **Vera Kowalski** | Concept Artist | Concept Art v0.1–v0.3 (Materialpalette, Charaktere, Umgebungen, Rüstung) |
| **Tobi Richter** | Technical Artist | GDD Kap 6 (Tech Spec, Produktion, Release-Strategie, Monetarisierung) |
| **Leo Fischer** | QA & Konsistenz | Vollständigkeits-Checklist (Wolf 2013), Konsistenz-Prüfung Mi–Fr |
| **Finn Bergmann** | Producer (ich) | Roadmap, Sprint-Planung, Info-Fluss, Blocker-Clearance, Final-Review |

## Wochenplan (Eingefasst)

**Mo–Di (10:00–17:00):** Research Phase
- Alle recherchieren parallel. Kein Druck auf Output. Keine Commits nötig.
- Darius: Spielübersicht & Mechaniken brainstormen
- Nami: Mythos-Foundation (Kosmologie, Schöpfung, Schattenfieber-Lore)
- Emre: Topos-Foundation (Geographie, Architektur, Karten-Outline)
- Vera: Materialsprache, Silhouetten, Fraktions-Palette (+ **warten auf Darius Stadtfrage**)
- Tobi: Engine, Pipeline, Monetarisierung, Release-Modell
- Leo: Wolf-Checklist vorbereiten

**Mi–Fr (10:00–17:00):** Production Phase
- **Mi 15:00:** Alle liefern Draft v0.1 (Vollständigkeit > Perfektion)
- **Mi 20:00:** PDF v0.1 generiert
- **Do 15:00:** Alle liefern v0.2 (Leo-Feedback integriert)
- **Do 21:00:** PDF v0.2 generiert
- **Fr 14:00–17:30:** Final Polishing, PDF v0.3 kompiliert & submitted

## Offene Fragen für Darius (Critical Path)

**Bis Dienstag 17:00 entscheiden:**

1. **Stadtfrage:** Eine zentrale vertikal-geschichtete Stadt oder mehrere überlagerte Städte? → Vera, Emre warten.
2. **Schattenfieber:** Nur Statuseffekt oder hauptquest-antreibender Plot? → Nami, Tobi warten.
3. **Tiervolk:** Spielbar-Rasse oder nur NPC-Flavor? → Emre wartet.
4. **Release-Strategie:** Single-Release oder Episodisch? Premium oder Indie-Budget? → Tobi wartet.

## Meine Rolle (Finn)

- **Sprint-Meister:** Daily Sync Mi–Fr (18:00) mit Darius & Leo → Blocker identifizieren, Info-Flow anpassen
- **Qualitäts-Gate:** Alle Outputs against Briefing checken. Leo-QA Review weitergeben.
- **Repos-Struktur:** `gallery/gdd/`, `gallery/wbb/`, `gallery/concepts/day{N}/`, Logs → `traces/`
- **PDF-Automation:** Pandoc-Export Mi–Fr 20:00 (+ Timestamp)
- **Final-Review:** Freitag morgens Checkliste mit allen durcharbeiten
- **Keine Commits für COMPLETED.md & ROADMAP.md** — diese sind Arbeitsdokumente, nicht Artefakte

## Library & Referenzen

Alle recherchieren in `library/` (Repo-Root). Wichtige Dateien:
- Schell (2010) GDD-Struktur
- Klastrup/Tosca (2004) Transmediale Welten (Mythos–Topos–Ethos)
- Wolf (2013) Neun Infrastrukturen imaginärer Welten (Checkliste!)
- Elder Scrolls, Gothic, Dishonored, Vampires the Masquerade: Bloodlines als Referenzen
- **NICHT:** Witcher 3 (man spielt bestimmten Charakter), Baldur's Gate 3 (rundenbasiert, Partyplay)

## Nächste Schritte (Montag Afternoon)

1. Darius im 1:1 fragen: Stadtfrage, Schattenfieber-Scope, Tiervolk-Status, Release-Strategie
2. Vera vorwarnen: Input kommt bis Di 17:00 oder working assumption (eine vertikale Stadt)
3. Tobi + Nami: Release-Input abhängig von Darius-Entscheidungen, Plan B bereit (Indie Single-Release)
4. Leo: Wolf-Checklist teilen, Konsistenz-Prüfpunkte vorbereiten
5. Mi 09:00 vor Produktion: Alle Memory-Updates checken, offene Fragen Schachtelnd klären

## Notizen zur Simulation 2

- **5 Szenen pro Tag:** BRIEFING (Finn) → WORK (einzeln) → MEETING (Finn) → PAUSE (random) → WORK (einzeln) → REVIEW (Finn)
- **Finn moderiert Briefings & Reviews**, filtert Darius-Input
- **Memory ist Langzeit-Gedächtnis**, wird zwischen Szenen mit Erkenntnissen gefüllt
- **Keine Trace-Dateien für Finn-Arbeit** (Roadmap & COMPLETED.md sind Artefakte, nicht Traces)
- **Pragmatismus über Perfektion:** Ein Draft ist besser als Paralysys durch Perfektionismus
