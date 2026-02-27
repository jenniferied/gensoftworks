# Tobi — Tag 05, Szene 2 (WORK) — Output

**Datum:** Tag 5, Freitag, Szene 2 (WORK Vormittag)
**Aufgabe:** GDD-06 V2 finalisieren
**Ergebnis:** GDD-06 V2 fertig. Datei: `gallery/gdd/06-technik-produktion.md` (überschrieben)

---

## Prüfliste — Ergebnisse

| Punkt | Status | Befund |
|-------|--------|--------|
| 1. Hex-Codes 1:1 aus GDD-05 | **FEHLEND in V1 — in V2 eingetragen** | V1 hatte nur Farbbeschreibungen ohne Hex. V2 referenziert GDD-05 verbindlich, Hex-Tabelle in Kap. 4.1 eingefügt |
| 2. Hauten-Shader SSS+WPO, Nanite-Ausnahme | **FEHLEND in V1 — in V2 neu** | Kap. 1.4 "Organische Shader-Architektur" hinzugefügt. SSS-Profil, WPO-Regelwerk, Nanite-Ausnahmen katalogisiert |
| 3. Drei-Schichten-Rendering | **FEHLEND in V1 — in V2 neu** | Kap. 5.1 erweitert: Mittelgrund/Hohlicht/Stillfeld als PP-Volume-Schichten. 3-5 Segmente definiert |
| 4. Halluzinations-Start 76 | **FEHLER in V1 — in V2 korrigiert** | V1 startete bei 70 (Interpolationsformel). CD-Lock: 76. Formel korrigiert. Stufengrenzen angepasst |
| 5. Budget 45k EUR, GAS Pflicht | **TEILWEISE in V1 — in V2 explizit** | Kap. 8.2 um Anforderungsprofil Gameplay-Programmer ergänzt, GAS als Ausschlusskritierium |
| 6. Performance-Tiers 1080p30/1440p60/4K60 | **KORREKT in V1 — unverändert** | Tiers stimmen. Redaktionelle Notiz zu Minimum-Tier-Benchmark hinzugefügt |

---

## Änderungslog V2 (zusammengefasst)

- **NEU Kap. 1.4:** Organische Shader-Architektur (Hauten-Shader, SSS-Profile, WPO, Nanite-Grenze)
- **KORRIGIERT Kap. 4.1:** Hex-Code-Tabelle mit GDD-05-Werten
- **ERWEITERT Kap. 5.1:** Drei-Schichten-Rendering (Mittelgrund / Hohlicht / Stillfeld)
- **KORRIGIERT Kap. 5.3:** Stufengrenzen auf CD-Lock (Rauschen 1-40, Risse 41-75, Schwelle 76-100)
- **KORRIGIERT Kap. 5.4:** Halluzinations-Interpolationsformel: Start bei 76, nicht 70
- **ERWEITERT Kap. 8.2:** Anforderungsprofil Gameplay-Programmer, GAS als Pflicht-Kriterium explizit
- **Aenderungslog:** V2-Eintrag gesetzt

---

## Offene Punkte (für Review)

- **Hauten-Segmente:** Memory sagt "3-5 Segmente" für Hohlicht/Stillfeld. Ich nehme 3 als Standard, 5 als Maximum. Brauche Bestätigung von Emre (Lore: Wie viele Übergänge zwischen den Ebenen pro Szene realistisch?).
- **Zwei Schattenfieber-Farbprofile:** Memory nennt zwei Profile. Interpretation: Profil A = spielerseitig (MPC-gesteuert), Profil B = Zonenbefalls (Level-Volume). Muss von Emre/Darius bestätigt werden.
- **Minimum-Tier:** GTX 1070 provisorisch. Final nach Benchmark-Phase (Woche 6-8).

---

## Nächste Schritte

1. GDD-06 V2 bei heutigem Review vorstellen
2. Meeting mit Emre: Hauten-Segmentanzahl + Schattenfieber-Farbprofile klären
3. Kamera-Blueprint V0.1 starten (war schon in V1 als nächster Schritt markiert, noch offen)
