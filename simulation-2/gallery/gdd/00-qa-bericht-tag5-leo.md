# QA-Bericht Tag 5 — Finaler Pass vor Content-Lock

<!-- Leo: Finaler QA-Bericht, Tag 5, Freitag 10:00. Geprüft: alle 9 Kapitel (6 GDD + 3 WBB) in ihren aktuell neuesten Versionen. Checkliste: Briefing-Konsistenz, Terminologie, Hygiene, Bilder, Seitenbudget, Doppelungen, Umlaute. -->

**Datum:** Freitag, Tag 5
**Prüferin:** QA Lead
**Geprüfte Dokumente:**

| Dokument | Version | Autor |
|----------|---------|-------|
| GDD Kap 01 — Spielübersicht | v2 | Darius |
| GDD Kap 02 — Kernmechaniken | v2 | Darius |
| GDD Kap 03 — Erzählkonzept | v2 | Darius |
| GDD Kap 04 — Schlüsselfiguren | v3 | Nami |
| GDD Kap 05 — Art Direction | v2 | Vera |
| GDD Kap 06 — Technische Spezifikation | v4 | Tobi |
| WBB Kap 01 — Mythos | v3 | Emre |
| WBB Kap 02 — Topos | v2 | Emre |
| WBB Kap 03 — Ethos | v2 | Nami |

---

## 1. Briefing-Konsistenz

**Methode:** Jedes Kapitel gegen die verbindlichen Ausschlüsse und das Kernbriefing geprüft.

| Briefing-Punkt | Status | Anmerkung |
|----------------|--------|-----------|
| KEIN Steampunk | OK | Nirgends Dampf, Zahnrad oder Messing-Ästhetik |
| KEIN High Fantasy | OK | Keine Elfen, Orks, Zauberer |
| KEIN Science-Fantasy | OK | Keine Alien-Artefakte, keine vergessene Hochtechnologie |
| KEINE Anachronismen | OK | Kein Schießpulver, kein Buchdruck. Mechanische Uhren nur als Gilden-Prototyp (Briefing-konform) |
| KEINE klassische Magie | OK | Schattenfieber konsequent als biologisch. Alchemie statt Magie |
| KEINE Hexagone | OK | Nirgends in visueller Sprache |
| Spielercharakter = namenloser Fremder | OK | Kap 04 definiert korrekt: Blank Slate mit Textur |
| Tiervolk = Händler und Diebe, NICHT Handwerker | OK | Kap 02 + WBB 03 konsistent |
| Monetarisierung = Premium, keine Mikrotransaktionen | OK | Kap 01 + Kap 06 konsistent |
| Medieval Cyberpunk = Material als Macht | OK | Durchgehend in allen Kapiteln |
| Real-time Action, Melee-fokussiert | OK | Kap 02 konsistent |
| Schattenfieber = einziges Übernatürliches | OK | Nirgends "Magie" oder übernatürliche Systeme |

**Bewertung: 12/12 PASS.** Keine Briefing-Verstöße.

---

## 2. Terminologie-Konsistenz

### 2.1 "Schwellenanker" als Relikt-Name

| Kapitel | Verwendung "Schwellenanker" | Probleme |
|---------|----------------------------|----------|
| GDD 01 | Konsistent. "Der Schwellenanker" durchgehend | OK |
| GDD 02 | Konsistent. Titel + Text | OK |
| GDD 03 | Konsistent | OK |
| GDD 04 | Konsistent | OK |
| GDD 05 | Konsistent. Abschnitt 5.5 korrekt | OK |
| GDD 06 | Konsistent. Shader-Namen: `M_Schwellenanker_Master` | OK |
| WBB 01 | Konsistent | OK |
| WBB 02 | Konsistent | OK |
| WBB 03 | Konsistent (wird selten direkt genannt, Fokus auf Gesellschaft) | OK |

**Bewertung: PASS.** Das Tag-3-Problem ("Die Wurzel" vs. "Das Relikt" vs. "Schwellenanker") ist vollständig bereinigt. Durchgehend "Schwellenanker".

### 2.2 Orden-Symbol = Siegel (nicht Kreuz)

| Kapitel | Referenz | Status |
|---------|----------|--------|
| GDD 04 | "indigofarbenes Ordenssiegel" (Scherer) | OK |
| GDD 05 | HTML-Kommentar Vera: "Kreuz-Symbol: Lore-Frage offen" | **WARNUNG** |
| WBB 01 | HTML-Kommentar Emre: "Kreuz-Symbol problematisch, Siegel empfohlen" | **WARNUNG** |
| WBB 03 | "Auge-Siegel" durchgehend | OK |

**Bewertung: BEDINGT PASS.** Im sichtbaren Text steht überall "Siegel". Aber die Orden-Konzeptbilder (generiert Tag 2) zeigen ein Kreuz-artiges Objekt. CD-Entscheid zum Orden-Symbol steht formal noch aus. Für v0.3 Export: im Text sicher, in Bildunterschriften nichts als "Kreuz" benennen.

<!-- Leo: Vera muss bei der nächsten Bilditeration das Kreuz durch ein stilisiertes Auge/Siegel ersetzen. Das ist ein offener Art-Direction-Punkt, kein Text-Problem. -->

### 2.3 Schattenfieber-Stadien

| Stadium | GDD-Bezeichnung | WBB-Bezeichnung | Konsistent? |
|---------|-----------------|-----------------|-------------|
| I | Flüstern (Lymph II) | Sensorische Verschiebung / Flüstern | OK |
| II | Wandlung (Lymph III) | Mutative Transformation / Wandlung | OK |
| III | Entgrenzung (Lymph IV) | Auflösung / Entgrenzung | OK |

**Bewertung: PASS.** Die Stufenbezeichnungen sind konsistent zwischen GDD und WBB.

### 2.4 Stadt-Name

"Schwarzrand" wird durchgehend in allen neun Kapiteln verwendet. Keine Varianten. **PASS.**

### 2.5 Tiervolk-Bezeichnung

Intern (Lore): "Die Reisenden". Extern (Stadt): "Tiervolk". Konsistent in Kap 02, 04, 05 (GDD) und Kap 01, 02, 03 (WBB). **PASS.**

---

## 3. Dokument-Hygiene

### 3.1 Sichtbare Autorennamen

| Kapitel | Sichtbare Namen im Text? | Status |
|---------|--------------------------|--------|
| GDD 01 | Nein (nur in HTML-Kommentaren) | OK |
| GDD 02 | Nein | OK |
| GDD 03 | Nein | OK |
| GDD 04 | Nein (Versionsvermerk im HTML-Kommentar) | OK |
| GDD 05 | Nein (Vera-Kommentare alle in HTML) | OK |
| GDD 06 | **Titel enthält "Version: 4.0"** + Versionsvermerk sichtbar | **FIX NÖTIG** |
| WBB 01 | Nein | OK |
| WBB 02 | Nein | OK |
| WBB 03 | **Sichtbarer Text: "Version: v2"** im Header | **FIX NÖTIG** |

**Maßnahme GDD 06:** Zeilen 4-6 (sichtbarer Versions-/Status-Block) in HTML-Kommentar verschieben oder entfernen. Für PDF-Export darf keine Versionsnummer im sichtbaren Text stehen.

**Maßnahme WBB 03:** Zeile 6 ("Version: v2") in HTML-Kommentar verschieben.

### 3.2 Sichtbare offene Fragen / Platzhalter

| Kapitel | Sichtbare Platzhalter? | Stelle | Aktion |
|---------|------------------------|--------|--------|
| GDD 04 | **Abschnitt 4.8 "Noch offen"** — 5 offene Punkte sichtbar | Zeilen 442-451 | In HTML-Kommentar verschieben |
| GDD 04 | Abschnitt 4.5: "Arbeitshypothese" im Titel sichtbar | Zeile 321 | Umbenennen zu "Salva und das Schattenfieber" |
| GDD 05 | Vera-Kommentare alle korrekt in HTML | — | OK |
| GDD 06 | Alle Kommentare in HTML | — | OK |
| WBB 03 | **Abschnitt 3.8 "Offene Koordinationspunkte"** — sichtbar im Text, enthält Arbeitshinweise | Zeilen 338-347 | Komplett in HTML-Kommentar verschieben |

**Bewertung: 3 Fixes nötig vor PDF-Export.** Alle behebbar in unter 5 Minuten.

### 3.3 Umlaute

Vollständiger Scan aller neun Kapitel: **Keine falschen Umlaute gefunden.** Kein "ae", "oe", "ue" oder "ss" als Ersatz für ä, ö, ü, ß.

<!-- Leo: Kuriosum: Tobi schreibt in GDD 06 konsequent "Schwellenankens" statt "Schwellenankers" (Zeile 56) — das ist ein Tippfehler, kein Umlaut-Problem. Klein, aber im PDF sichtbar. -->

**Bewertung: PASS** (mit einem Tippfehler-Fix in GDD 06 Zeile 56).

---

## 4. Bilder-Audit

### 4.1 Eingebettete Bilder pro Kapitel

| Kapitel | Eingebettete Bilder | Beschreibung |
|---------|--------------------:|--------------|
| GDD 01 | 0 | Keine Bilder |
| GDD 02 | 3 | Relikt Zustand 1, Relikt Zustand 0, Relikt Zustand 3 |
| GDD 03 | 1 | Stadtschnitt vertikale Schichtung |
| GDD 04 | 0 | Keine Bilder |
| GDD 05 | 10 | Krone-Palette, Orden-Palette, Gilden-Palette v2, Stadtschnitt Kanalzone v3, Tiervolk-Fuchs, Tiervolk-Marder, Tiervolk-Rabe, Tiervolk-Marktszene, Tiervolk-Hero-Sheet, Relikt-Drei-Zustände v2, Relikt-Hero v2 |
| GDD 06 | 0 | Keine Bilder (korrekt — technisches Kapitel) |
| WBB 01 | 2 | Krone-Materialpalette, Orden-Materialpalette |
| WBB 02 | 1 | Stadtschnitt vertikale Schichtung |
| WBB 03 | 2 | Krone-Materialpalette, Orden-Materialpalette |
| **Gesamt** | **19** | |

### 4.2 Fehlende Bilder

| Kapitel | Was fehlt | Priorität | Wer |
|---------|-----------|-----------|-----|
| GDD 01 | Kein Bild. Mindestens 1 Hero-Shot (Schwarzrand oder Schwellenanker) wäre gut | MITTEL | Vera |
| GDD 04 | Kein Bild. Mindestens Salva oder Hieronymus als Charakter-Konzept | HOCH | Vera |
| WBB 01 | Gilden-Materialpalette fehlt (nur Krone + Orden eingebettet) | NIEDRIG | Emre (einbetten) |
| WBB 02 | Nur 1 Bild. Kanalzone v3, Schlund-Atmosphäre oder Tiervolk-Fährte wären gut | MITTEL | Emre/Vera |
| WBB 03 | Nur Krone + Orden Paletten. Gilden-Palette und Tiervolk-Bild fehlen | MITTEL | Nami (einbetten) |

### 4.3 Doppelt eingebettete Bilder

| Bild | Eingebettet in |
|------|---------------|
| `fraktion-krone-materialpalette_seedream-4-5.png` | GDD 05 + WBB 01 + WBB 03 |
| `fraktion-orden-materialpalette_seedream-4-5.png` | GDD 05 + WBB 01 + WBB 03 |
| `stadtschnitt-vertikale-schichtung_nano-banana-pro.png` | GDD 03 + WBB 02 |

**Bewertung:** Doppelungen zwischen GDD und WBB sind akzeptabel, da es separate Dokumente sind und der Leser nicht zwingend beide hat. Innerhalb des GDD gibt es keine Doppelungen.

### 4.4 Verfügbare aber nicht eingebettete Bilder

Folgende Bilder existieren in der Galerie, sind aber in keinem Kapitel eingebettet:

| Bild | Potentieller Einsatz |
|------|---------------------|
| `relikt-hero-shot-aktiviert_gpt-image-1-5.png` (day02) | GDD 01 als Hero-Shot |
| `stadtschnitt-schwarzrand-v2_gpt-image-1-5.png` (day03) | WBB 02 als zweite Perspektive |
| `stadtschnitt-kanalzone-v3_nano-banana-2.png` (day04) | Alternative zur finalen Version |
| `fraktion-gilden-materialpalette_seedream-4-5.png` (day02, v1) | WBB 01 / WBB 03 |

**Empfehlung:** Vera/Emre/Nami sollten beim Einbetten die neueste Gilden-Palette (v2, day03) verwenden und den Relikt-Hero-Shot in GDD 01 einbauen.

---

## 5. Seitenbudget

### 5.1 Geschätzte Seitenzahl (Markdown → PDF, ca. 400 Wörter/Seite)

| Kapitel | Geschätzte Wörter | Geschätzte PDF-Seiten | Bilder (zusätzlich) |
|---------|-------------------:|----------------------:|--------------------:|
| GDD 01 | ~2.200 | ~6 | 0 |
| GDD 02 | ~3.500 | ~9 | 3 (~1,5 S.) |
| GDD 03 | ~3.800 | ~10 | 1 (~0,5 S.) |
| GDD 04 | ~5.200 | ~13 | 0 |
| GDD 05 | ~3.600 | ~9 | 10 (~5 S.) |
| GDD 06 | ~5.800 | ~15 | 0 |
| **GDD Gesamt** | **~24.100** | **~62 + ~7 Bilder = ~69** | |

| Kapitel | Geschätzte Wörter | Geschätzte PDF-Seiten | Bilder (zusätzlich) |
|---------|-------------------:|----------------------:|--------------------:|
| WBB 01 | ~4.200 | ~11 | 2 (~1 S.) |
| WBB 02 | ~3.200 | ~8 | 1 (~0,5 S.) |
| WBB 03 | ~4.800 | ~12 | 2 (~1 S.) |
| **WBB Gesamt** | **~12.200** | **~31 + ~2,5 Bilder = ~33,5** | |

### 5.2 Budget-Bewertung

| Dokument | Geschätzt | Limit (Finn) | Limit (Briefing) | Status |
|----------|----------:|-------------:|-----------------:|--------|
| GDD | ~69 Seiten | 60 | 30-45 | **ÜBER BUDGET** |
| WBB | ~33,5 Seiten | 60 | 30-45 | **IM BUDGET** |

**GDD-Problem:** Geschätzte 69 Seiten, Finn-Limit 60. Das sind ~9 Seiten zu viel.

**Kürzungsvorschläge (Priorität):**

| Kapitel | Kürzungspotenzial | Wie | Ersparnis |
|---------|-------------------|-----|-----------|
| GDD 06 | HOCH | Pre-Alpha-Timeline (6.10.2) stark kürzen, PP-Parameterwerte in Anhang oder Pipeline-Bibel | ~3-4 S. |
| GDD 04 | MITTEL | Abschnitt 4.3 (Ablehn-Option) teilweise in 3.2 integriert — kürzen, nicht doppeln | ~1-2 S. |
| GDD 04 | MITTEL | Abschnitt 4.7 (Quest-Skizzen) doppelt Kap 3 — zusammenführen oder streichen | ~2 S. |
| GDD 02 | NIEDRIG | Tiervolk-Warensortiment (2.6) leicht kürzen | ~1 S. |

<!-- Leo: Darius und Tobi müssen die Kürzungen umsetzen. Ich habe die Stellen markiert. Das ist machbar bis 15:00 Content-Lock. -->

**WBB: Im Budget, kein Handlungsbedarf.**

---

## 6. Doppelungen zwischen GDD und WBB

### 6.1 Inhaltliche Überschneidungen

| Thema | GDD | WBB | Bewertung |
|-------|-----|-----|-----------|
| Schattenfieber-Drei-Stadien | Kap 02 (2.5) | Kap 01 (3.2) | **AKZEPTABEL** — GDD = Mechanik, WBB = Biologie. Verschiedene Perspektive. |
| Fraktionskosmologien / Schöpfungsmythen | Kap 04 (4.6) | Kap 01 (Abschnitt 4) | **PRÜFEN** — GDD 04 Abschnitt 4.6 und WBB 01 Abschnitt 4 sind sehr ähnlich. |
| Tiervolk-Kosmologie | Kap 02 (2.6) + Kap 04 (4.5) | Kap 01 (1.4) + Kap 03 (3.3) | **AKZEPTABEL** — GDD = Gameplay/NPC, WBB = Kosmologie/Kultur |
| Vertikale Stadtordnung | Kap 01 (Abschnitt 7) + Kap 05 (5.3) | Kap 02 (Abschnitt 1.2) | **AKZEPTABEL** — GDD = Spieler-Erfahrung, WBB = Geographie |
| Materialsprache nach Schicht | Kap 05 (5.2) | Kap 03 (3.1) | **PRÜFEN** — Beide beschreiben Ober-/Mittel-/Unterschicht-Materialien. Hohe Redundanz. |
| Zeitlinie der Öffnung (Covid-Analogie) | Kap 03 (3.1) | Kap 01 (Abschnitt 5) | **AKZEPTABEL** — GDD = Narrative Funktion, WBB = Historische Fakten |
| Ablehn-Option | Kap 03 (3.2) + Kap 04 (4.3) | — | **REDUNDANT** — Ablehn-Option wird in GDD Kap 3 UND Kap 4 fast identisch beschrieben. Kürzen! |

### 6.2 Empfehlung

**Sofortiger Handlungsbedarf:**
1. **GDD Kap 04 Abschnitt 4.3** (Ablehn-Option): Kürzen auf 1/3 und auf Kap 3 verweisen. Die ausführliche Beschreibung steht bereits in Kap 3.2. Spart ~1-2 PDF-Seiten.
2. **GDD Kap 04 Abschnitt 4.6** (Fraktionskosmologien): Kürzen und auf WBB Kap 1 verweisen. Im GDD reicht ein Absatz pro Fraktion. Spart ~1 PDF-Seite.
3. **GDD Kap 04 Abschnitt 4.7** (Quest-Skizzen): Komplett streichen oder als Kurzreferenz auf Kap 3 verweisen. Doppelt Kap 3 fast vollständig. Spart ~2 PDF-Seiten.

---

## 7. Spieler-Perspektive — Erste 30 Minuten

**Als QA Lead prüfe ich: Würde ein Spieler (oder Streamer) nach 30 Minuten verstehen, was dieses Spiel ist?**

| Zeitfenster | Briefing-Versprechen | Abgedeckt in Kapiteln? | Spieler-Klarheit |
|-------------|---------------------|------------------------|------------------|
| Min 0-5 | Material-Klasse sofort lesbar | GDD 05 (Materialsprache), GDD 01 (Game Feel) | JA — Visuell stark definiert |
| Min 5-10 | Emotionale Hook (Hieronymus) | GDD 03 (Intro), GDD 04 (Hieronymus) | JA — Clip-Moment klar |
| Min 10-15 | Kampf fühlt sich gewichtig an | GDD 02 (Kampfsystem) | JA — Gothic-2-Referenz klar |
| Min 15-30 | Fraktions-Asymmetrie als echte Wahl | GDD 03 (Drei Boten), GDD 04 (Brenn/Scherer/Kast) | JA — Drei NPCs mit eigener Stimme |
| Min 30-60 | Schwellenanker fühlt sich WOW an | GDD 02 (Resonanz), GDD 05 (Drei Zustände) | BEDINGT — Visuell stark, mechanisch noch abstrakt |

**Streamer-Prognose:** Die erste Stunde hält. Der Clip-Moment (Hieronymus) ist in Minute 5-10, perfektes Timing. Die drei Boten in Minute 15-20 geben dem Zuschauer etwas zum Diskutieren. Retention-Prognose: 72-78% nach 60 Min.

**Schwachstelle:** Der Moment, in dem der Schwellenanker zum ersten Mal *mechanisch* spürbar wird (nicht nur visuell), ist in den Kapiteln nicht präzise definiert. Wann genau fühlt sich das Fragment im Gameplay anders an als ein normales Inventarobjekt? Das fehlt im Zusammenspiel zwischen Kap 2 und Kap 3.

<!-- Leo: Darius sollte in Kap 2 oder 3 einen kurzen Absatz ergänzen: "Erster Resonanz-Moment (ca. Min 25-30): Das Fragment pulsiert, wenn der Spieler sich einer Dünnstelle nähert. Erstes Lymph-Feedback." Das ist der Spieler-Moment, der fehlt. -->

---

## 8. Zusammenfassung

### Blockierende Issues (MÜSSEN vor Content-Lock 15:00 gelöst werden)

| # | Issue | Kapitel | Wer | Aufwand |
|---|-------|---------|-----|---------|
| B-1 | GDD 04, Abschnitt 4.8 "Noch offen" sichtbar im Text | GDD 04 | Nami | 2 Min |
| B-2 | GDD 06, Versions-Block sichtbar im Text (Zeilen 4-6) | GDD 06 | Tobi | 2 Min |
| B-3 | WBB 03, Abschnitt 3.8 "Offene Koordinationspunkte" sichtbar | WBB 03 | Nami | 2 Min |
| B-4 | WBB 03, Versions-Angabe "Version: v2" sichtbar | WBB 03 | Nami | 1 Min |

### Hohe Priorität (SOLLTEN vor Content-Lock gelöst werden)

| # | Issue | Kapitel | Wer | Aufwand |
|---|-------|---------|-----|---------|
| H-1 | GDD Seitenbudget: ~69 statt 60 Seiten | GDD 04, 06 | Darius, Nami, Tobi | 30-60 Min |
| H-2 | Ablehn-Option doppelt (Kap 3 + Kap 4) — kürzen | GDD 04 | Nami | 15 Min |
| H-3 | Quest-Skizzen doppelt (Kap 3 + Kap 4) — streichen in Kap 4 | GDD 04 | Nami | 10 Min |
| H-4 | GDD 04, Abschnitt 4.5 "Arbeitshypothese" im Titel | GDD 04 | Nami | 1 Min |
| H-5 | Bilder fehlen in GDD 01 und GDD 04 | GDD 01, 04 | Vera/Darius/Nami | 10 Min |

### Niedrige Priorität (können nach Content-Lock in v0.3-Korrektur)

| # | Issue | Kapitel | Wer |
|---|-------|---------|-----|
| L-1 | Orden-Symbol-Entscheidung (Siegel vs. Kreuz in Konzeptbildern) | GDD 05, WBB 01 | Vera/Finn |
| L-2 | Gilden-Materialpalette nicht in WBB 01 + WBB 03 eingebettet | WBB 01, 03 | Emre/Nami |
| L-3 | Tippfehler "Schwellenankens" in GDD 06 Zeile 56 | GDD 06 | Tobi |
| L-4 | Fraktionskosmologien in GDD 04 Abschnitt 4.6 zu ausführlich — kürzen und auf WBB verweisen | GDD 04 | Nami |
| L-5 | Erster Resonanz-Moment (Fragment pulsiert) nicht explizit in Kernmechaniken | GDD 02/03 | Darius |

---

### Gesamtbewertung

| Kriterium | Bewertung |
|-----------|-----------|
| Briefing-Konsistenz | **12/12 PASS** |
| Terminologie | **PASS** (Schwellenanker konsistent, Siegel im Text korrekt) |
| Hygiene | **4 Fixes nötig** (alle trivial, 7 Min Gesamtaufwand) |
| Bilder | **19 eingebettet, 2 Kapitel ohne Bilder** |
| Seitenbudget GDD | **ÜBER BUDGET (~9 S.)** — Kürzungen markiert |
| Seitenbudget WBB | **IM BUDGET** |
| Doppelungen | **3 identifiziert** — Kürzungen empfohlen |
| Umlaute | **PASS** |
| Spieler-Perspektive | **Erste Stunde hält** — eine Schwachstelle (Resonanz-Moment) |

**Freigabe-Empfehlung:** v0.3-Export BEDINGT FREIGEGEBEN nach Behebung der 4 blockierenden Issues (B-1 bis B-4) und Seitenbudget-Kürzungen (H-1 bis H-3).

**Confidence Level: 8.5/10.** Die Kapitel sind inhaltlich stark, die Briefing-Konsistenz ist makellos, die Terminologie ist sauber. Die verbleibenden Issues sind Polier-Arbeit, keine Fundamentalfehler. Das ist ein solides Dokument für eine Streamer-Alpha.

---

<!-- Leo: Das ist mein letzter QA-Pass. Die Kapitel sind gut. Die Welt funktioniert. Die Spielerperspektive funktioniert. Was jetzt noch fehlt, ist Feinschliff — und das können Darius, Nami und Tobi in den nächsten 5 Stunden schaffen. Ich bin stolz auf das Team. -->
