# QA-Bericht Tag 4 — Leo
## Hygiene & Konsistenz-Pass über alle 9 Kapitel

**Datum:** Tag 4, Donnerstag, 10:00 Uhr
**Status:** v0.2-Snapshot vorbereitet
**Schweregrad Findings:** 3 LOW, 1 MEDIUM

---

## Executive Summary

Alle 9 Kapitel sind sauber für den v0.2-Export. CD-Feedback (Relikt → Schwellenanker, Zeitlinie = Covid, Tiervolk = Symbiose) ist durchgehend implementiert. Zwei Minor-Inkonsistenzen gefunden, beide nicht-blockierend. Seitenbudget im Rahmen (GDD 42/60, WBB 33/60).

---

## 1. Hygiene-Checkliste

### 1.1 Autorenerwähnungen im sichtbaren Text
Status: ✅ CLEAR
- Alle Autorennamen sind in HTML-Kommentare (`<!-- Darius: ... -->`) verschoben
- Keine sichtbaren Namen im Fließtext (anders als Tag-3-Snapshot)
- Export-ready

### 1.2 Recherche-Kommentare / Post-Its
Status: ✅ KLAR mit Anmerkung
- Recherche-Links sind als HTML-Kommentare gekennzeichnet
- **Beispiel:** Kap 5, Zeile 58: `<!-- Vera: Krone-Palette freigegeben vom CD. ... -->`
- Keine sichtbaren TODO-Listen mehr
- **Anmerkung:** Manche sind detailliert (Vera-Feedback eingearbeitet), das ist gut

### 1.3 Wolf-Checklisten / Infrastruktur-Checks
Status: ⚠️ BELASSEN, NICHT ENTFERNEN
- Kap 1–3 (WBB) haben am Ende formale Wolf-Infrastruktur-Checklisten
- **Diese gehören dort hin** — das ist methodische Dokumentation, nicht Team-Kommunikation
- Format: `| Infrastruktur | Status | Anmerkung |` — saubere Tabelle
- **Keep-as-is für v0.2**

### 1.4 "Offene Fragen"-Anhänge
Status: ✅ OK (korrekt in HTML-Kommentaren oder Anhängen)
- GDD Kap 6: Offene Punkte sind als `<!-- Tobi: Offene Fragen & Abhängigkeiten -->` strukturiert
- WBB Anhänge sind eigenständige Abschnitte mit `<!-- Interne Koordination — nicht für PDF-Export -->` Header
- **QA-Urteil:** Das ist klar als intern markiert und wird beim PDF-Export rausgefiltert
- Akzeptabel

### 1.5 "Anmerkung für XY" Blöcke
Status: ✅ SAUBER
- Alle sind in HTML-Kommentare oder Anhänge verlagert
- Keine sichtbaren "An Darius: ...", "An Vera: ..." mehr
- GDD Kap 3, Zeile 195: `<!-- Darius: v2 dieses Kapitels braucht: ... -->` — ist Kommentar, nicht sichtbar

---

## 2. Konsistenz-Check nach CD-Antworten (Tag 4 Briefing)

### 2.1 Relikt-Namenspolitik → Schwellenanker
Status: ✅ KONSISTENT
- **CD-Entscheid:** "Schwellenanker" ist der offizielle In-World-Name
- **Überall durchgehend:**
  - GDD 01: "Der Schwellenanker" (Zeile 25, etc.)
  - GDD 02: "Schwellenanker" in Abschnitten 2.5, 2.6
  - GDD 03: Hauptquest dreht sich um "Der Schwellenanker", nicht "das Relikt"
  - GDD 04: "Hieronymus Vael" hält "eine Scherbe aus... [dem Schwellenanker]" (Zeile 29)
  - GDD 05: "Relikt — Der Schwellenanker" als Abschnitt-Titel (Zeile 215)
  - GDD 06: "M_Schwellenanker_Master" als Shader-Name (Zeile 549)
  - WBB 01: "Der Schwellenanker ist ein Grenzstabilisator" (Zeile 250)
  - WBB 02: "Ankerkammer" als Ort, in dem Schwellenanker lag (Zeile 22, etc.)
  - WBB 03: "die Ankerkammer" in Landmarken-Abschnitt (Zeile 203)
- **Gut:** Keine Vermischung mit "Wurzel", "Relikt" (als Gegenstand), "Schwellenanker-Relikt" etc.
- ✅ PASS

### 2.2 Tiervolk = Symbiose (nicht Mutation, nicht Exposition)
Status: ✅ KONSISTENT
- **CD-Entscheid:** Tiervolk ist dritter kosmologischer Faktor, Symbiose, nicht primär von Schwarzrand-Exposition stammend
- **Umsetzung:**
  - GDD 01, Zeile 224: "Tiervolk: Spielbar oder NPC? → NPC — Händler und Informationsbroker. Nicht spielbar. Leicht alien in Ästhetik, nicht tribal. Eigene Händler-Netzwerke parallel zu den Gilden."
  - GDD 04, Kap 4.5: Salva als "Tiervolk" (Name bleibt Platzhalter), "Reisende" ist interne Bezeichnung
  - GDD 04, Zeile 273: "Das Tiervolk ist kein Volk. 'Tiervolk' ist ein abwertender Begriff... Sie nennen sich intern 'die Reisenden.'"
  - WBB 03, Kap 3.3: Vollständige Kulturgeschichte als eigenes Volk mit Kosmologie ("Die Schwelle kommuniziert")
  - **Wichtig:** WBB 01, W-004 steht noch als offen ("Tiervolk kosmologischer Ursprung ungeklärt"), aber der Text ist **nicht** "Exposition auf Nicht-Menschen" — das ist korrekt. Die Ambiguität ist beabsichtigt.
- ✅ PASS (mit Anmerkung: W-004 offen = OK, das ist Weltbau-Geheimnis, nicht Fehler)

### 2.3 Zeitlinie = jahrelange Anbahnung (Covid-Kontext)
Status: ✅ KONSISTENT mit Vorsicht
- **CD-Entscheid:** "Zeitlinie = Covid" (jahrelange Anbahnung, nicht plötzlich)
- **Umsetzung:**
  - GDD 01, Zeile 227–228: "Öffnung vor einer Generation"
  - WBB 01, Zeile 220–222: "Vor einer Generation — die Zeitzeugen leben noch, aber sie widersprechen einander"
  - WBB 01, W-006: "Zeitlinie 'vor einer Generation' unkonkretisiert. Arbeitshypothese: 25 Jahre."
  - WBB 02, Zeile 87: "Das ist das Rauschen der einsetzenden Fiebers" (erste Stufe ist schnell, Progression dauert länger)
  - **Aber:** Die Öffnung selbst ist noch "plötzlich" beschrieben (WBB 01, Zeile 230: "Das Schattenfieber... breitete sich explosionsartig aus"). Das ist nicht "jahrelange Anbahnung der Öffnung", sondern "jahrelange Anbahnung davor" + "plötzliche Konsequenzen".
  - **CD-Interpretation:** "Covid" heißt eher: das System war jahrelang instabil, die Öffnung war der Kipppunkt, dann Exponentialwachstum. Das ist konsistent mit den Texten.
- ⚠️ **Minor-Diskrepanz:** WBB 01 könnte expliziter machen, dass die Öffnung eine Konsequenz jahrelanger Anspannung war, nicht ein Zufall. Aber blockiert nicht.
- ✅ PASS (mit Aufwärm-Empfehlung für v0.3)

### 2.4 Schattenfieber = Körperreaktion (biologisch, nicht mystisch)
Status: ✅ KONSISTENT
- **CD-Entscheid:** Schattenfieber ist biologische Reaktion des Lymphsystems, kein Übernatürliches (außer der Schwelle selbst)
- **Umsetzung:**
  - GDD 02, Kap 2.5: Lymph-Subsystem koppelt direkt an Schattenfieber-Progression (drei biologische Stadien: Flüstern/Wandlung/Entgrenzung)
  - GDD 06, Kap 6.4: Schattenfieber-PP-System ist Post-Processing, nicht Magie — visuelle Kodierung der biologischen Reaktion
  - WBB 01, Kap 3.1–3.3: "Schwellensubstrat" ist beschrieben als Katalysator (nicht Substanz), lagert im Lymphsystem ab, kausale Biologie
  - GDD 04: "Hieronymus Vael liegt am Stadtrand... Schattenfieber Stadium III. Er hat nicht mehr lange." — biologisches Sterben, nicht mystisches
- ✅ PASS

### 2.5 Schwellenanker-Mechanik (Resonanz, nicht einfaches Tool)
Status: ⚠️ VAGUE-OK
- **CD-Entscheid (implizit):** Schwellenanker ist kein "Gegenstand, den man nutzt" — er ist ein Resonanzobjekt
- **Umsetzung:**
  - GDD 03, Zeile 185–191: "Der Schwellenanker als mechanischer Hauptquest-Anker — Resonanz-Intensität, Fragment-Auffinden, Entscheidungspunkt"
  - WBB 01, Zeile 250: "Der Schwellenanker ist ein Grenzstabilisator" (beschreibt, was er *ist*, nicht, wie man ihn *benutzt*)
  - **Das Problem:** WBB 01 Zeile 250 ist immer noch zu vage. "Stabilisator" könnte bedeuten: aktives Ding, das man umlegen kann, ODER: statisches Ding, das einfach da sein muss
  - GDD 06, Kap 6.6: Shader beschreibt Zustand-Übergänge, aber nicht den mechanisch-spielerischen Einsatz
  - **QA-Urteil:** Das ist nicht falsch, aber nicht konkret genug für Tobi/Darius. Sollte in GDD v1.1 geklärt werden: "Der Spieler hält Fragmente des Schwellenankers. Er kann sie zurücklegen. Er kann sie behalten. Er kann sie einer Fraktion überlassen. Er kann sie zerstören." (Das steht in GDD 03, Zeile 158, ist aber nicht in die Mechanik-Kapitel zurückgeflossen.)
- ⚠️ **MEDIUM-Findings:** GDD 02/06 sollten explizit sagen, dass der Schwellenanker nicht "benutzt" wird, sondern dass der Spieler **Fragmente trägt und mit Fragmenten interagiert**. Das ist ein Design-Punkt, der im QA auftauchen wird.
- **Nicht blockierend für v0.2**, aber sollte in v0.2-Alpha-Feedback berücksichtigt werden

---

## 3. Format-Konsistenz

### 3.1 Bild-Einbettung
Status: ✅ OK
- Alle Bilder sind via Markdown eingebettet: `![Titel](../concepts/...)`
- Pfade sind relativ und kohärent
- Vera hat Tag 3 vier Bilder produziert, alle sind referenziert:
  - `fraktion-krone-materialpalette_seedream-4-5.png` (GDD 05, WBB 01/03)
  - `fraktion-orden-materialpalette_seedream-4-5.png` (GDD 05, WBB 01/03)
  - `fraktion-gilden-materialpalette-v2_nano-banana-2.png` (GDD 05, WBB 03)
  - `stadtschnitt-schwarzrand-v2_gpt-image-1-5.png` (GDD 05, WBB 02)
  - `relikt-drei-zustaende-v2_nano-banana-pro.png` (GDD 05, GDD 06, GDD 02)
- ✅ PASS

### 3.2 Abschnitt-Struktur
Status: ✅ SAUBER
- Alle Kapitel haben Versionsstatus am Anfang: `<!-- Status: v2 | Tag 3, Mittwoch | Autor: Darius Engel -->`
- Alle Kapitel haben finale Versionsstatus-Zeile: `*Versionsstatus: v2 — ...*`
- Überschriften-Hierarchie ist konsistent (# Kapitel, ## Sektion, ### Subsekt, #### Detail)
- ✅ PASS

---

## 4. Seitenbudget-Analyse

### 4.1 GDD (max 60 Seiten)

| Kapitel | Seiten (geschätzt) | Status |
|---------|-------------------|--------|
| 01 Spielübersicht | 5 | ✅ |
| 02 Kernmechaniken | 7 | ✅ |
| 03 Erzählkonzept | 6 | ✅ |
| 04 Schlüsselfiguren | 7 | ✅ |
| 05 Art Direction | 6 | ✅ |
| 06 Technische Spez. | 11 | ✅ (1/6 der Budget, rechtfertigt sich durch Komplexität) |
| **Gesamt** | **42** | **✅ 70% Ausnutzung** |

### 4.2 WBB (max 60 Seiten, aber Referenzmaterial)

| Kapitel | Seiten (geschätzt) | Status |
|---------|-------------------|--------|
| 01 Mythos | 10 | ✅ |
| 02 Topos | 12 | ✅ |
| 03 Ethos | 11 | ✅ |
| **Gesamt** | **33** | **✅ 55% Ausnutzung** |

---

## 5. Blockierende vs. Nicht-Blockierende Findings

### Blockierend (für Alpha): KEINE

### Medium-Priority (sollten vor Beta geklärt werden):

1. **Schwellenanker-Nutzungs-Mechanik** — GDD 02/06 sollte explizit machen, dass Fragmente "getragen", nicht "benutzt" werden. Status: Wissen vorhanden (GDD 03, Zeile 158), aber nicht in Tech-Kapitel zurückgeflossen.
   - **Zuständig:** Darius (GDD 02) + Tobi (GDD 06)
   - **Dringlichkeit:** vor Beta

2. **Öffnung der Ankerkammer als jahrelange Instabilität** — WBB 01 könnte expliziter sein, dass die Öffnung Konsequenz jahrelanger Schwächung war, nicht Zufall. Momentan zu summarisch.
   - **Zuständig:** Emre (WBB 01)
   - **Dringlichkeit:** vor Beta (für Lore-Konsistenz)

### Low-Priority (interessant, nicht kritisch):

3. **W-006 (Zeitlinie konkrete Jahre)** — "vor einer Generation" bleibt vage (Arbeitshypothese: 25 Jahre). Sollte beim GDD-Finalen geklärt werden.
   - **Zuständig:** CD (Entscheid), dann Emre (Umsetzung)

4. **W-004 (Tiervolk kosmologischer Ursprung)** — Bleibt absichtlich offen als Weltbau-Geheimnis. Akzeptabel, aber sollte vor Beta geklärt werden, damit das Spiel nicht versehentlich eine Erklärung gibt.
   - **Zuständig:** Emre + Nami (Narrativ-Konsistenz)

---

## 6. Persönliche QA-Perspektive (Leo)

### Was funktioniert:

- **Game Feel** (Kap 1): Die vier Säulen sitzen. Kein Zweifel, dass der Spieler sich schwer, reibungsvoll, bedroht UND erstaunt fühlt. Das ist das richtige Gefühl für diese Welt.
- **Erste 30 Minuten** (Kap 2–4): Hieronymus Vael stirbt, Fragment-Übergabe, drei Boten, erste Fraktionswahl. Das ist ein starker Clip-Moment. Chat wird nicht abschalten.
- **Erzähl-Architektur** (Kap 3): Drei Akte, offene Fraktionsquests, Ablehn-Option ist real. Das ist nicht auf Schienen. Das ist echte Spielerperspektive.
- **Materialsprache** (GDD 05 + WBB 03): Jedes Material erzählt Status. Das ist so viel subtiler als HUD-Icons. Das funktioniert.

### Was noch unbequem ist:

- **Schwelle-Physik unkonkret:** Der Spieler wird fragen: "Was ist die Schwelle genau? Wie funktioniert sie?" Wir haben: "Es ist eine Existenzebene, die näher und ferner sein kann." Das ist cool, aber wenn sie auf Schwarzrand treffen und erste Anomalien sehen, brauchen sie RAUM für die Erklärung. GDD 06 ist gut (visuelle Codierung), aber die narrative Erklärung ist immer noch in WBB versteckt.
  - **Für Alpha:** Nami sollte eine kurze NPC-Erklärung haben, die der Spieler in den ersten zwei Stunden kriegt. "Die Schwelle ist wie... [Analogie]." Moment.

- **Streamer-Safety:** Ich teste live. Wenn das Schattenfieber-PP-System (Stufe 2–3) Motion-Sickness triggert, muss die Accessibility-Option (Kap 6.4.4) **sofort** sichtbar sein. Das steht im Spiel, aber nicht in der Launch-Checkliste. Sollte rot markiert werden.

---

## 7. Empfehlung für v0.2-Export

**Status:** ✅ FREIGABE EMPFOHLEN

Alle 9 Kapitel sind sauber, konsistent und bereit für den v0.2-Snapshot. Die drei Medium-Priority-Findings sind nicht blockierend, sollten aber in die nächste Iteration (v0.2-Alpha-Feedback-Loop) eingebaut werden.

**Action-Items für Team:**
1. Darius: GDD 02 + Tobi GDD 06 — Schwellenanker-Fragment-Nutzung explizit machen
2. Emre: WBB 01 — Öffnung der Ankerkammer als Kipppunkt kontextualisieren
3. Nami: GDD 04 Quest-Dialog — kurze Schwelle-Erklärung einbauen (falls nicht schon in v2)
4. Tobi: Accessibility-Checklist für Alpha-Build — Motion-Sickness-Option prominent machen

---

**Bericht geschrieben von:** Leo Fischer, QA Lead
**Uhrzeit:** Tag 4, 10:45 Uhr
**Confidence-Level:** 8/10 — Kapitel sind gut, aber die Schwelle-Konzept-Kommunikation noch nicht spieler-zentriert genug.
