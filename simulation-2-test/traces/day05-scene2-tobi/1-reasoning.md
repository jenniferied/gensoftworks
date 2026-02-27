# Tobi — Tag 05, Szene 2 (WORK) — Reasoning

## Ausgangslage

GDD-06 V1 ist ein solides Fundament. Die Architektur steht: GAS, Lumen, Nanite, Schattenfieber-MPC, Drei-Tier-Performance. Was V2 braucht, ist Präzision — die Stellen, die in V1 noch mit "offen" oder "abzustimmen" markiert waren, müssen jetzt entweder befüllt oder mit konkreten Nächsten Schritten versehen werden.

## Prüfpunkt 1: Hex-Codes aus GDD-05

GDD-05 (Vera, V1) ist die Referenz. Ich gehe die relevanten Hex-Codes durch:

**Fraktionspaletten GDD-05:**
- Krone: `#3D3D3D` (Basis), `#8B1A2B` (Akzent), `#C5A030` (Highlight)
- Gilden: `#7A6E5D` (Basis), `#C49A20` (Akzent), `#2EC4B6` (Highlight)
- Orden: `#E8E4DE` (Basis), `#4A5568` (Akzent), `#D4A017` (Highlight)
- Schattenfieber: `#2D0A31` + `#39FF14`
- Tiervolk: `#CC7722`, `#C04000`, `#C2B280`
- Wildnis/Neutral: `#5C6B3C`, `#8B7355`, `#9E9E9E`

In GDD-06 V1 steht in Kap. 1.2 Farb-Pipeline nur das Prinzip (ACES, Deakins-Referenz). Die konkreten Hex-Codes fehlen dort vollständig. Ebenso in Kap. 4.1 bei den Material-Instanzen: nur allgemeine Farbbeschreibungen ("Amber, Dunkelgold, Efeugrün") — keine Hex-Werte.

**Fazit:** Hex-Codes müssen in GDD-06 V2 explizit eingetragen werden, 1:1 aus GDD-05. Das ist eine Kompatibilitätspflicht — die Shader-Parameter müssen die Art-Direction-Vorgaben ohne Interpretation treffen.

## Prüfpunkt 2: Hauten-Shader (SSS + WPO)

In V1 steht im Nanite-Abschnitt (Kap. 1.2): Skeletal Meshes unterstützen kein Nanite, also klassische LOD-Ketten für Charaktere.

Was fehlt: ein dedizierter Abschnitt zum **Hauten-Shader** als eigenem technischen System. Die Welt ist aus Emer-Fleisch geformt — jede Oberfläche, die organisch ist, braucht Subsurface Scattering. Das ist nicht trivial.

**SSS (Subsurface Scattering):**
- Ü5 hat zwei Methoden: `Subsurface` Shading Model (legacy, baked) und `Subsurface Profile` (physikalisch, screen-space). Ich will Subsurface Profile — es liefert Burley-SSS, das in Ü5.3+ deutlich verbessert wurde.
- Performance-Implikation: Subsurface Profile ist Screen-Space, kostet ~0.3-0.5 ms zusätzlich pro Screen-Fill. Muss im Budget stehen.
- Nanite-Ausnahme: Hier ist die Überschneidung. Organische Wand-Segmente (Biotech-Elemente, pulsierende Adern) wären theoretisch Nanite-fähig als statische Meshes — ABER: wenn sie SSS brauchen UND animiert sind (WPO), müssen sie als traditionelle Meshes bleiben.

**WPO (World Position Offset):**
- Pulsierende Biotech-Elemente, atmende Wände, Schattenfieber-Vegetation — alles braucht WPO.
- Nanite + WPO: Seit Ü 5.1 unterstützt Nanite WPO *grundsätzlich*, aber mit Einschränkungen: Displacement muss aktiviert sein, Performance-Kosten steigen. Für kleine Puls-Animationen (<5% Displacement) ist Nanite+WPO vertretbar. Für starke Schattenfieber-Deformationen (Stufe 3-4) empfehle ich traditionelle Meshes.
- **Klarregelung für V2:** Nanite-Ausnahmen explizit katalogisieren: was bleibt traditionell, was ist Nanite+WPO, was ist reines Nanite.

**Fazit:** Neuer Abschnitt in Kap. 1.2 oder Kap. 5 nötig: "Organische Shader-Architektur" — Hauten, SSS, WPO, Nanite-Grenze klar ziehen.

## Prüfpunkt 3: Drei-Schichten-Rendering

Memory sagt: "Mittelgrund=Level, Hohlicht/Stillfeld=PP+3-5 Segmente". Das ist neu gegenüber V1 — V1 nennt nur das Schattenfieber als PP-System.

Der Kontext aus der Lore (WBB-01, Emre): Es gibt drei Daseinsebenen — Mittelgrund (die Welt), Hohlicht (unterhalb), Stillfeld (oberhalb). Die Spieler-Wahrnehmung bricht ab Schattenfieber-Stufe 4 (Schwelle) in diese anderen Ebenen ein.

**Technisch:**
- **Mittelgrund:** Standard-Rendering-Pipeline. Das ist die Welt wie sie ist. Kein extra PP-Overhead.
- **Hohlicht:** Eine "untere" Rendering-Ebene. Visuelle Konvention laut Lore: dunkler, komprimierter, Farben in Richtung Violett-Schwarz. Technisch: eigenes PP-Volume mit Hohlicht-spezifischen Einstellungen. Nicht permanent sichtbar — nur wenn Schattenfieber-Schwelle überschritten (Infektionswert 76+) oder in spezifischen Level-Zonen.
- **Stillfeld:** Die "obere" Ebene. Laut Lore stärker und gefährlicher. Technisch: noch ein PP-Volume-Profil, heller, entsättigter, geometrische Verzerrung stärker.
- **3-5 Segmente:** Das meint die Anzahl aktiver PP-Volume-Profile pro Szene. Mittelgrund-Standard + 2 Ebenen-Profile + 1 Schattenfieber-Profil (spielerseitig) + ggf. 1 Zonen-Profil = max. 5. Das ist in Ü5 mit Priority-Blending realisierbar.

**Fazit:** Kap. 5 (Schattenfieber-Tech) muss um die Drei-Schichten-Architektur erweitert werden. Klare Trennung: Was ist spielerseitig (MPC-gesteuert), was ist zonen-/lore-basiert (Level-Volumes).

## Prüfpunkt 4: Halluzinations-Start auf 76

V1 sagt in Kap. 5.3 Tabelle (Stufe 4): "Infektionswert 76-100" — das stimmt.
V1 sagt in Kap. 5.4 Graduelle Interpolation: "Halluzinationen: Aktivierung ab Wert 70, Intensität skaliert mit `(Infektionswert - 70) / 30`."

**Konflikt.** Die Tabelle sagt 76, die Interpolationsformel startet bei 70. Das muss aufgelöst werden. CD-Vorgabe ist verbindlich: Schwelle beginnt bei 76.

**Korrektur für V2:** Interpolationsformel anpassen auf `max(0, (Infektionswert - 76) / 24)`. Startpunkt 76, Maximum 100, Skalierungsbereich 24.

Ebenso überprüfen: Stufe 3 endet bei 75, nicht 76. Die Stufen-Grenzen sind:
- Rauschen: 1-40
- Risse: 41-75
- Schwelle: 76-100
Das entspricht CD-Vorgabe. V1 hat "26-50" und "51-75" als Stufen-2-und-3-Grenzen — das weicht ab. V1 war offenbar noch vor dem CD-Lock geschrieben. Diese Werte müssen korrigiert werden.

**Korrektur-Tabelle für V2:**
- Stufe 1 (Gezeichnet): 1-25 → bleibt, da sub-Rauschen
- Stufe 2 (Infiziert): 26-40 → entspricht Rest von Rauschen
- Stufe 3 (Verwandelt): 41-75 → Risse komplett
- Stufe 4 (Entfesselt): 76-100 → Schwelle komplett

Oder: Ich passe die Stufen-Benennung an die Lore-Terminologie an und streiche die Eigenbezeichnungen ("Gezeichnet", "Infiziert") zugunsten von Nami/Emres Terminologie. Letzteres ist sauberer.

## Prüfpunkt 5: Budget 45k EUR, GAS-Erfahrung Pflicht

V1 Kap. 8.2 sagt: 45.000 EUR Gesamt-Mittelwert, Gameplay-Programmer 20.000-25.000 EUR, "GAS-Erfahrung erforderlich" steht implizit (Kap. 3.1: "Kein Teammitglied hat die C++-Tiefe...").

Was fehlt: GAS-Erfahrung als **explizites Muss-Kriterium** im Freelancer-Profil, nicht nur als Kontextinformation. In V2 kommt ein Abschnitt "Anforderungsprofil Gameplay-Programmer" mit konkreten Kriterien.

**GAS-Erfahrung Pflicht:** Wer kein GAS kann, kann nicht anfangen. Das ist nicht verhandelbar. Im Budget bleibt es bei 45k.

## Prüfpunkt 6: Performance-Tiers

V1 Kap. 6.1:
- Minimum: GTX 1070 / RX 5700, 30 fps, 1080p — **stimmt**
- Empfohlen: RTX 3070 / RX 6800, 60 fps, 1440p — **stimmt**
- High-End: RTX 4080+, 60 fps, 4K — **stimmt**

Alle drei Tiers entsprechen der Vorgabe (1080p30 / 1440p60 / 4K60). Kein Korrekturbedarf.

Aber: Der Minimum-Tier zeigt GTX 1070. Die aktuell gängigere Grenze liegt bei GTX 1660/RX 5500 XT. V1 erwähnt das selbst. Ich nehme das in V2 als redaktionelle Notiz auf: "Minimum-Tier wird nach Benchmark-Phase (Woche 6-8) final gesetzt."

## Was V2 neu bringt (Zusammenfassung der Änderungen)

1. **Hex-Code-Tabelle** in Kap. 4.1: Material-Instanzen bekommen die GDD-05-Hex-Codes 1:1 eingetragen
2. **Organische Shader-Architektur** (neues Kap. 1.4 oder Anhang C): Hauten-Shader, SSS-Profile, WPO-Regelwerk, Nanite-Ausnahmen katalogisiert
3. **Drei-Schichten-Rendering** (Erweiterung Kap. 5): Mittelgrund/Hohlicht/Stillfeld als PP-Volume-Schichten definiert
4. **Stufen-Korrektur** Kap. 5.3+5.4: Stufengrenzen auf CD-Lock angepasst, Interpolationsformel Halluzinationen auf Start 76 korrigiert
5. **Freelancer-Anforderungsprofil** (Erweiterung Kap. 8.2): GAS als Pflicht-Kriterium explizit, konkrete Ausschreibungs-Kriterien
6. **Version und Änderungslog** aktualisiert

## Offene Fragen die ich NICHT erfinde

- Hauten-Ebenen in der Lore: Wie viele Segmente sollen pro Übergang aktiv sein? Memory sagt "3-5" — ich nehme 3 als Standard, 5 als Maximum und markiere es als "zu validieren mit Emre".
- Schattenfieber-Farbprofile: Memory nennt "zwei Profile". Was sind die zwei? Ein Profil für spielerseitigen Infektionswert, eines für befallene Zonen? Das nehme ich so an, muss aber von Emre/Darius bestätigt werden.
