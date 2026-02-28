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

## CD-Feedback (Di 09:00 — BRIEFING) — AKTUALISIERT

**1. Schattenfieber — Wahrheit vs. Propaganda**
- ✅ **GEKLÄRT:** Es gibt EINE biologisch erklärbare Wahrheit zum Schattenfieber
- ✅ **GEKLÄRT:** Jede Fraktion interpretiert es unterschiedlich durch ihre ideologische Linse
- ✅ **GEKLÄRT:** Das ist NICHT Mystik → Propaganda, Kontrolle, Machtspiel
- **Nami:** Mythos-Kap zeigt, was JEDE Fraktion SAGT. Die Wahrheit offenbart sich in WBB/GDD-Technik-Kapitel.

**2. Relikt — CD-Brainstorm HEUTE**
- **NEU:** Relikt ist direkt von CD (nicht Darius vorgegeben)
- **NEU:** Team brainstormt heute (Di 10:00–12:30) OPTIONEN
- **NEU:** Vera generiert SKETCHES (2–3 Variationen pro Option, schnell explorativ)
- **Lieferpfad:**
  - Di 10:00–12:30: Team-Brainstorm (Finn sammelt Optionen)
  - Di 12:30: Finn → Vera Handoff (schriftliche Notiz mit Optionen + Kontext)
  - Di 14:00–17:00: Vera rendert Sketches (parallel zur Recherche)
  - Di 18:00: Sketches in `gallery/concepts/day02/`
  - Mi morgen: CD entscheidet, welche Option wird erste Iteration

**3. Release-Modell — Single Release + DLC-Strategie**
- ✅ **GEKLÄRT:** Main Release (nicht Episoden) → Alpha (optional) → Beta → Full Release → Post-Launch DLCs
- ✅ **GEKLÄRT:** DLCs sind groß (nicht kleine Patches, sondern Welterweiterungen)
- **Tobi:** Strukturiert das in GDD Kap 6 (Release-Strategie). Input von Darius braucht's parallel.

**4. Vera — Production Phase ab JETZT**
- ✅ **GEKLÄRT:** Montag war Research, kein Druck
- ✅ **GEKLÄRT:** Ab heute (Dienstag) = Production Phase — Bilder entstehen PARALLEL zur Recherche, nicht nach
- **Vera:** Braucht Input von mir (Di 12:30 Relikt-Notiz), dann wird gearbeitet

## CD-Feedback (Mi 09:00 — BRIEFING) — NEUEST

**1. Saubere Dokumente für Export**
- ✅ Alle PDFs sollen fertig aussehen — keine Notizen, Anmerkungen oder Autor-Namen
- ✅ Alle Kommentare/Anmerkungen gehören in HTML-Kommentare (`<!-- ... -->`) im Markdown
- ✅ HTML-Kommentare rendern nicht mit aus, bleiben aber für Team & CD im Quelltext sichtbar
- **Aktion:** Darius, Nami, Emre, Vera — räumt eure Inhalte sauber auf vor Finalexport heute Abend

**2. Bilder in die Dokumente packen — PRIORITÄT**
- ✅ Vera-Bilder müssen in WBB und/oder GDD eingebaut sein
- ✅ Materialpaletten (Krone, Orden) sind super
- ✅ Gilden-Palette: zu viel Text generiert — kürzen
- ✅ Artefakt/Relikt:
  - `relikt-drei-zustaende-vergleich_nano-banana-2` kommt am nächsten, aber Text weg
  - `relikt-hero-shot-aktiviert_gpt-image-1-5` sieht cool aus — mitnehmen
  - Keine Wirbelsäule als Hauptmotiv (zu abstrakt)
- ✅ Umgebung: `stadtschnitt-vertikale-schichtung` sieht unnatürlich aus — nächste Iteration braucht's
- **Aktion:** Vera & Darius: Bilder in Art Direction (Kap 5) einbauen. Nami: Materialpaletten/Fraktions-Visuals in Mythos/Ethos?

**3. Relikt-Terminologie aktualisiert**
- ✅ **NEUER BEGRIFF:** "Schwellenanker" (nicht "Herz" oder "Wurzel")
- ✅ Verwendung überall aktualisieren (Darius, Nami, Emre, Vera, Tobi)

**4. Spieler-Interaktion mit Fragment**
- ✅ Spieler DARF das Fragment ablehnen (mechanisch wichtig)

## Darius-Fragen (4 Offene) — Deadline: Di 17:00

**Noch zu klären:**
1. **Stadtfrage:** Eine zentrale vertikal-geschichtete Stadt oder mehrere überlagerte Städte? → wirkt auf Vera, Emre, Tobi
2. **Schattenfieber-Scope:** Nur Statuseffekt oder hauptquest-antreibender Plot? → wirkt auf Nami, Tobi
3. **Tiervolk:** Spielbar-Rasse oder nur NPC-Flavor? → wirkt auf Emre
4. **Release-Strategie:** Single-Release oder Episodisch? Premium oder Indie-Budget? → wirkt auf Tobi

**Format:** Darius schreibt's hin (kurz, klar, nicht poliert). Ich gebe's weiter.

## Dienstag 13:00 — MEETING (Küche)

**Livemoment (Di 13:00 - 13:15):**
- ✅ **Eröffnet:** Alle Outputs sind geliefert
- ✅ **Darius (GDD Kap 1):** High Concept geschärft, 4 Fragen beantwortet
- ✅ **Emre (WBB Kap 2):** Schwarzrand als Stadtname, Schwelle, Schattenfieber-Biologie, Gilden-Monopol, 3 Schöpfungsmythen. Tiervolk kosmologisch offen.
- ✅ **Nami (GDD Kap 4):** 5 Schlüsselfiguren, Intro-Quest + Hauptquest-Skizze
- ✅ **Vera:** 9 Concept-Art-Bilder (Relikt, Fraktionspaletten, Stadtschnitt), $0.67/$2.00 Budget verwendet
- ✅ **Tobi (GDD Kap 6):** Tech Spec (UE5, Nanite, Lumen, Schattenfieber-PP, Relikt-Shader, Release-Pipeline)
- ✅ **Leo:** Wolf-Checkliste finalisiert, Alpha-Erste-Stunde-Checkliste, Talking Points
- ✅ **Finn:** Roadmap + COMPLETED.md aktualisiert
- **Diskussion folgt:** Schwarzrand-Bestätigung, Darius-Fragen-Status, Abhängigkeiten

## Wochenplan (AKTUALISIERT — Mi 09:00 BRIEFING)

**Montag–Dienstag (10:00–17:00):** Research + Production Start
- ✅ Montag: Alle recherchiert parallel
- ✅ **Dienstag 10:00–12:30:** Alle recherchiert/produziert parallel
  - ✅ Darius: GDD Kap 1–2 + 4 Fragen
  - ✅ Nami: Mythos-Outline finalisiert
  - ✅ Emre: Topos-Foundation mit Schwarzrand-Integration
  - ✅ Vera: Materialpalette finalisiert + 9 Concept-Art-Bilder
  - ✅ Tobi: Release-Modell Research + GDD Kap 6
  - ✅ Leo: QA-Framework finalisiert
- ✅ **Di 13:00:** MEETING — Eröffnung abgeschlossen
- **Di 16:00:** Finn ↔ Darius Status-Check (Fragen-Tracking)
- **Di 17:00:** Darius-Deadline (4 Fragen schriftlich)
- **Di 18:00:** Vera-Sketches liefern (`gallery/concepts/day02/`)

**MITTWOCH (HEUTE) — PRODUKTION & EXPORT**
- **Mi 09:00:** BRIEFING (Küche) — CD-Feedback durchgesagt, Tagesplan
- **Mi 10:00–15:00:** WORK Block
  - **Darius:** Finalisiert GDD Kap 1–3, integriert Vera-Bilder in Kap 5, räumt Kommentare auf
  - **Nami:** Finalisiert WBB Kap 1 (Mythos) + Materialpalette/Fraktions-Visuals, räumt auf
  - **Emre:** Finalisiert WBB Kap 2 (Topos), räumt auf
  - **Vera:** Letzter Polish auf Concept Art (Gilden-Palette Text kürzen, Stadtschnitt optional nächste Iteration), räumt auf
  - **Tobi:** Finalisiert GDD Kap 6, räumt auf
  - **Leo:** Prüft Konsistenz, erstellt Feedback-Liste
  - **Finn:** Koordiniert Handoffs, checkt Bilder-Integration, validiert gegen Briefing
- **Mi 15:00–17:00:** WORK Block (Sprintpause)
- **Mi 17:00:** MEETING (Küche) — Alle liefern? Blocker? Letzter Check vor Export
- **Mi 18:00:** PDF v0.1 (GDD + WBB) exportieren
- **Mi 20:00:** PDF final archiviert

**Do–Fr:** Feedback-Iteration v0.2 & v0.3

## Meine Rolle (Finn) — AKTUALISIERT

- **Sprint-Meister:** Blocker-Clearance, Info-Flow (CD zu Team und zurück)
- **Gatekeeper:** CD-Aufmerksamkeit ist kostbar — Termine, Notizen mit Kontext, Prioritäten
- **Handoff-Manager:** Di 12:30 Vera-Notiz mit Relikt-Brainstorm (PENDING)
- **Sync-Moderator:** Di 14:00 Nami (PENDING), Di 16:00 Darius (PENDING), tägliche Mi–Fr Syncs mit Darius & Leo
- **Qualitäts-Gate:** Outputs gegen Briefing checken vor Leo-QA
- **Repos-Struktur:** `gallery/gdd/`, `gallery/wbb/`, `gallery/concepts/day{N}/`, Logs → `traces/`
- **PDF-Automation:** Pandoc-Export Mi–Fr 20:00
- **Roadmap & COMPLETED:** Laufend aktualisieren (keine Commits durch mich — GM macht's am Ende)
- **HTML-Kommentar-Moderation:** Alle Kommentare sind für mich sichtbar, aber nicht im finalen Export

## Library & Referenzen

Alle recherchieren in `library/` (Repo-Root). Wichtige Dateien:
- Schell (2010) GDD-Struktur
- Klastrup/Tosca (2004) Transmediale Welten (Mythos–Topos–Ethos)
- Wolf (2013) Neun Infrastrukturen imaginärer Welten (Checkliste!)
- Elder Scrolls, Gothic, Dishonored, Vampires the Masquerade: Bloodlines als Referenzen
- **NICHT:** Witcher 3 (man spielt bestimmten Charakter), Baldur's Gate 3 (rundenbasiert, Partyplay)

## Notizen zur Simulation 2

- **5 Szenen pro Tag:** BRIEFING (Finn) → WORK (einzeln) → MEETING (Finn) → PAUSE (random) → WORK (einzeln) → REVIEW (Finn)
- **Finn moderiert Briefings & Reviews**, filtert Darius-Input
- **Memory ist Langzeit-Gedächtnis**, wird zwischen Szenen mit Erkenntnissen gefüllt
- **Keine Trace-Dateien für Finn-Arbeit** (Roadmap & COMPLETED.md sind Artefakte, nicht Traces)
- **Pragmatismus über Perfektion:** Ein Draft ist besser als Lähmung durch Perfektionismus
- **CD-Feedback ist Nordstern:** Alle Prioritäten ordnen sich danach

## Erkenntnisse bis Mi 09:00

1. **Schwarzrand ist Stadtname:** Emre hat geliefert, Durchsage bei MEETING erfolgt. Vera, Emre und Tobi müssen Vertikal-Struktur abstimmen.
2. **Vera liefert zu Quote:** 9 Bilder = produktiv. Aber: Stadtschnitt-Bild wirkt unnatürlich, braucht nächste Iteration.
3. **Tiervolk ist offene Frage:** Emre braucht Darius-Antwort zu Spielbarkeit/NPC-Status bevor Topos finalisiert wird.
4. **Darius-Fragen sind kritischer Pfad:** Vera (Stadtfrage), Emre (Stadtfrage + Tiervolk), Tobi (Release-Strategie) hängen davon ab.
5. **Team ist synchronisiert:** Alle wissen welche Info sie brauchen, von wem, und bis wann.
6. **HTML-Kommentare sind neue Spielregel:** Alle Notizen & Kommentare müssen aus PDF raus, aber im Markdown sichtbar sein.
7. **Bilder-Integration ist TODAY Priority:** Vera-Concept-Art MUSS in GDD/WBB-Text eingebaut sein — nicht separater Anhang.

## Abhängigkeiten (kritisch) — LIVE MI 09:00

```
HTML-Kommentar-Cleanup (Mi 10:00–15:00)
├─ Darius: GDD Kap 1–3, 5 — keine Anmerkungen im Text
├─ Nami: WBB Kap 1, 3 + Materialpaletten — keine Anmerkungen
├─ Emre: WBB Kap 2 — keine Anmerkungen
├─ Vera: Concept Art Metadaten — keine Künstler-Namen
└─ Tobi: GDD Kap 6 — keine Anmerkungen

Bilder-Integration (Mi 10:00–15:00)
├─ Vera: Polish + Gilden-Palette Text kürzen
├─ Darius: Vera-Bilder in Kap 5 einbauen
├─ Nami: Fraktions-Materialpaletten in Mythos/Ethos einbinden?
└─ Finn: Validiert vor Export (saubere Platzierung)

Schwellenanker-Rename (Mi 10:00)
├─ Darius: GDD Kap 1–3, 5
├─ Nami: WBB Kap 1, 3, GDD Kap 4
├─ Emre: WBB Kap 2
├─ Vera: Concept Art Beschriftungen
└─ Tobi: GDD Kap 6 (Shader, Tech Spec)

Export-Deadline (Mi 18:00)
└─ Alle v0.1 Drafts → Leo QA → Finn Final-Check → PDF Pandoc Export
```

## Nächste Schritte (unmittelbar)

1. **Mi 10:00:** WORK Block startet — alle arbeiten parallel an Cleanup + Polish
2. **Mi 10:00–12:00:** Ich (Finn) fahre Runde durch Repo, checke HTML-Kommentar-Status
3. **Mi 13:00–14:00:** Erste PAUSE (zufällig besetzt)
4. **Mi 14:00:** Nami fragen: "Brauchst du Vera-Bilder für Mythos/Ethos?"
5. **Mi 15:00:** Darius-Sync: "Alle Kommentare weg? Vera-Bilder in Kap 5 eingebaut?"
6. **Mi 17:00:** MEETING (Küche) — Sind alle v0.1 bereit?
7. **Mi 18:00:** Pandoc Export starten (GDD v0.1 + WBB v0.1 als PDF)
