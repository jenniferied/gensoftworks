# QA-Arbeitsergebnis — Leo Fischer, Tag 4 Szene 5

## 1. Stufentabellen-Check (verbindlich: Rauschen 1-40, Risse 41-75, Schwelle 76-100)

| Dokument | Fundstelle | Alter Wert | Neuer Wert | Verantwortlich |
|----------|-----------|-----------|-----------|----------------|
| GDD-02 Kap. 2.3 | "Rauschen ab erstem Punkt, Risse ca. Wert 40, Schwelle ca. Wert 70" | ~40 / ~70 | exakt 41 / exakt 76 | Darius |
| GDD-02 Kap. 2.3 Tabelle | Stufe 2 = 26-50 "Rauschen zu Risse", Stufe 3 = 51-75 "Risse" | Uebergang bei ~40 | Rauschen endet bei 40, Risse beginnen bei 41 | Darius |
| GDD-02 Kap. 2.7 | "Ymir-Material" | Ymir | Emer | Darius |
| GDD-02 Kap. 2.7 | "Ur-Bindung" | Ur-Bindung | Grosse Flechtung | Darius |
| GDD-06 Kap. 5.4 | Halluzinationen: "Aktivierung ab Wert 70" | 70 | 76 | Tobi |
| GDD-06 Kap. 5.4 | Formel: "(Infektionswert - 70) / 30" | 70/30 | 76/24 | Tobi |
| GDD-03 | Schwelle-Uebergang implizit bei ~80 | ~80 | 76 | Nami |
| GDD-05 Kap. 7.2 | Veras Mapping stimmt bereits (Rauschen 1-40, Risse 41-75, Schwelle 76-100) | -- | Kein Aenderungsbedarf | -- |

**Bonus:** GDD-06 Kap. 4.1 -- Krone-Materialfarben "Amber, Dunkelgold, Efeugruen" abgleichen mit Veras Palette (Aschgrau, Karmin, Altgold). Kein Blocker, aber Tobi und Vera sollten das klaeren.

## 2. Spielerperspektiv-Update

Die Vision haelt. Sechs Dokumente, eine Welt -- das fuehlt sich nach Tag 4 bemerkenswert geschlossen an. Das Stufentabellen-Problem war der einzige systemische Fehler, und der ist jetzt geloest.

Als Spielerin: Die Schattenfieber-Entscheidung wird staerker, wenn Halluzinationen und Schwelle-Narrative synchron bei 76 starten. Kein Auseinanderklaffen zwischen dem, was ich sehe, und dem, was NPCs sagen.

## 3. QA-Checkliste fuer morgen (V2-Konsistenz-Check)

- [ ] Stufentabelle: Alle sechs Dokumente gegen Rauschen 1-40 / Risse 41-75 / Schwelle 76-100 pruefen
- [ ] Terminologie: "Emer-Material" statt "Ymir-Material", "Grosse Flechtung" statt "Ur-Bindung"
- [ ] Halluzinations-Start: Ueberall Wert 76
- [ ] Farbkonsistenz: Hex-Codes zwischen GDD-05 und GDD-06 abgleichen
- [ ] Stufe-0-Baseline: In GDD-05 V2 vorhanden?
- [ ] Ungefuege: In GDD-03 V2 eingebaut? (Emres Anmerkung)
- [ ] Flechtfest: In GDD-03 V2 kanonisiert?
- [ ] Nervensystem-Narrativ: In GDD-02 V2 ergaenzt? (Namis Anmerkung)
- [ ] Drei-Schichten-Rendering: In GDD-06 V2 dokumentiert?

---

*Leo Fischer, QA-Ecke, Tag 4 Donnerstag Nachmittag. Tabelle steht, Checkliste steht, morgen frueh wird geprueft.*
