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

## CD-Feedback (Di 09:00 — BRIEFING)

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

## CD-Feedback (Mi 09:00 — BRIEFING)

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

## CD-Feedback (Do 09:00 — BRIEFING)

**1. v0.1 Export erfolgreich ✅**
- PDF v0.1 delivered Mi 18:00 (alle Kapitel außer GDD 5 + WBB 3)
- Concept Art integriert, sieht gut aus
- Team ist on track

**2. Seitenbudget-Optimierung JETZT**
- **Problem:** v0.1 = 70–85 Seiten (zu viel)
- **Target:** Max 60 Seiten pro Dokument (GDD 60, WBB 35)
- **Strategie:** Gezieltes Kürzen (Doppelungen → HTML-Kommentare, Details → Anhänge)
- **Aktion:** Do 10:00–15:00 alle Agenten kürzen parallel

**3. Cleanup: Autorenerwähnungen, Checklisten**
- ✅ HTML-Kommentare statt sichtbarer Text
- ✅ Checklisten (z.B. Wolf-Prüfungen) in separate Dokumente oder Kommentare

**4. Vera-Budget erweitert: $5 gesamt**
- ✅ v0.1 genutzt: ~$1.50 (9 Bilder)
- ✅ v0.2 Budget: Tiervolk-Designs (Symbiose-Folk), Environment-Iteration (besserer Stadtschnitt?), Relikt-Hero v2 Varianten
- ✅ Fokus: Tiervolk = Symbiose-Volk (visuell zeigen: verbundene Entitäten, Kommunikation, biologische Verwobenheit)

**5. CD-Clarifications für Design**
- ✅ **Tiervolk:** Nicht spielbar (noch), aber visuelle Präsenz wichtig. Symbiose-Konzept = Inspiration: Myzelium-Netzwerk, Bienenstock mit Intelligenz, Schwarmlogik
- ✅ **Zeitlinie:** Schattenfieber-Trigger könnte Covid-Analogie sein (Pandemie, Ursprung unklar, Propaganda-Potenzial)
- ✅ **Schattenfieber-Wahrheit:** Körperreaktion (nicht mystisch), virales oder biologisches Agens → verändert Neurologie/Biologie → Sichtzeichen (Haut, Bewegung, Verhalten)

## Dienstag — MEETING & Outputs

**Di 13:00 — MEETING (Küche):**
- ✅ **Eröffnet:** Alle Outputs sind geliefert
- ✅ **Darius (GDD Kap 1):** High Concept geschärft, 4 Fragen beantwortet
- ✅ **Emre (WBB Kap 2):** Schwarzrand als Stadtname, Schwelle, Schattenfieber-Biologie, Gilden-Monopol, 3 Schöpfungsmythen. Tiervolk kosmologisch offen.
- ✅ **Nami (GDD Kap 4):** 5 Schlüsselfiguren, Intro-Quest + Hauptquest-Skizze
- ✅ **Vera:** 9 Concept-Art-Bilder (Relikt, Fraktionspaletten, Stadtschnitt), $0.67/$2.00 Budget verwendet
- ✅ **Tobi (GDD Kap 6):** Tech Spec (UE5, Nanite, Lumen, Schattenfieber-PP, Relikt-Shader, Release-Pipeline)
- ✅ **Leo:** Wolf-Checkliste finalisiert, Alpha-Erste-Stunde-Checkliste, Talking Points
- ✅ **Finn:** Roadmap + COMPLETED.md aktualisiert

## Mittwoch 10:00 — WORK Block Start

**Typ**: WORK | **Uhrzeit**: 10:00 | **Teilnehmer**: alle 7

### Notizen
- **Tagesplan:** Mi 10:00–15:00 Cleanup + Polish, Mi 17:00 MEETING, Mi 18:00 PDF v0.1 Export
- **Status:** Alle Kapitel v0.1 Draft fertig von Di. Mi = Cleanup + Bilder-Integration + QA
- **Kritischer Pfad:** HTML-Kommentare raus, Vera-Bilder in GDD/WBB einbauen, Schwellenanker-Rename überall
- **Bildliste:** Handoff-Notiz für Darius geschrieben (03-bildliste-handoff-vera-finn.md) — zeigt ihm welche 2 Relikt-Bilder + 3 Paletten in welche Kapitel passen
- **Vera-Aktion:** Gilden-Palette Text bis heute 12:00 kürzen (CD braucht)
- **Darius-Aktion:** Vera-Bilder in GDD Kap 5 einbauen, HTML-Kommentare entfernen
- **Timeline:** v0.1 Lock um Mi 20:00 (QA passt), Do v0.2, Fr v0.3 Final

### Ergebnisse
- ✅ **ROADMAP.md:** Dienstag geschlossen, Mittwoch mit aktuellen Status-Updates, Abhängigkeiten/Blockers neu geordnet
- ✅ **COMPLETED.md:** All Di Outputs dokumentiert, Mi Status aktuell, v0.1 Deliverables > In Progress übersetzt
- ✅ **Bildliste:** 03-bildliste-handoff-vera-finn.md geschrieben — pragmatisch, kurz, actionable für Darius

### Persönliches
- Team läuft smooth. Keine Blocker bisher.
- Mi 18:00 PDF-Export ist realistisch.
- Vera's Tempo passt — 9 Bilder, richtige Richtung, schnell iterierbar.

## Donnerstag (Do) 10:00 — WORK Block Start

**Typ**: WORK | **Uhrzeit**: 10:00 | **Teilnehmer**: alle 7

### Notizen
- **Tagesplan:** Do 10:00–15:00 v0.2 Build (Expansion + Kürzen), Do 17:00 MEETING, Do 20:00 PDF v0.2 Export
- **Status:** v0.1 erfolgreich exported Mi 18:00. Do = Seitenbudget-Optimization + neue Kapitel (GDD Kap 5, WBB Kap 3)
- **Kritischer Blocker:** Gesamtgröße 70–85 Seiten (zu viel). Target: GDD ~60, WBB ~35
- **Strategie:** Gezieltes Kürzen (Doppelungen, Details → HTML-Kommentare) + Expansion (neue Kapitel + Vera-Bilder v0.2)
- **Vera-Budget:** $5 gesamt, v0.1 genutzt ~$1.50 → Do/Fr ~$3.50 übrig für Tiervolk, Environment, Relikt-Hero v2 Varianten
- **Ownership-Verteilung:** Darius (Kap 5 Art Direction), Nami (WBB Kap 3 Ethos), Emre (Kap 2 Refinement/Kürzen), Vera (v0.2 Bilder), Tobi (Kap 6 Kürzen), Leo (QA-Pass 2)
- **Bildliste für Vera:** Tiervolk (Symbiose-Designs), Environment (besserer Stadtschnitt), Relikt-Hero v2 (alternative Varianten)

### Ergebnisse
- ✅ **ROADMAP.md:** Donnerstag-Status aktualisiert, v0.2-Gate dokumentiert, Ownership Do/Fr klar
- ✅ **COMPLETED.md:** Mi abgeschlossen, Do In Progress dokumentiert, Seitenbudget-Bericht hinzugefügt
- ✅ **Seitenbudget-Audit:** Grobe Zahlen ermittelt (GDD ~45 ohne Kap 5, +Kap 5/6 Kürzen = ~60; WBB ~20 ohne Kap 3, +Kap 3 = ~30)
- ✅ **Bildliste-Notiz:** (zu schreiben, vor Team-Handoff ~11:00)

### Offene Fragen
- Nami: Braucht sie Vera-Bilder für WBB Kap 3 (Ethos)? Oder nur visuelle Referenzen?
- Darius: Kann er GDD Kap 5 ohne weitere Vera-Input shapen, oder muss er auf Do 12:00 warten?

### Persönliches
- Seitenbudget-Issue war vorhersehbar (Leo hat's Mi identifiziert). Jetzt pragmatisches Kürzen ohne Qualitätsverlust.
- Team-Stimmung positiv: Mi Export erfolgreich, jetzt klare Targets für Do.
- Vera hat Budget-Luft für qualitativ hochwertigere Iteration (Tiervolk wird wichtig für Weltaufbau).
