# Reasoning — Leo, Tag 4, Szene 2

## Vorgehen

Systematischer Abgleich aller 6 Dokumente. Ich gehe die Pruefkriterien einzeln durch und lese die relevanten Stellen quer.

## 1. Terminologie-Konsistenz (WBB-01 als Referenz)

Emres WBB-01 definiert ein kosmologisches Lexikon mit klaren RELICS-eigenen Begriffen. Ich pruefe, ob alle GDD-Dokumente diese Begriffe korrekt verwenden.

**Befund:** Insgesamt beeindruckend konsistent. Die Kernbegriffe (Emer, Mittelgrund, Hauten, Flechtung/Grosse Flechtung, Faulung/Schwund/Entflechtung, Lebende Krone, Hohlicht, Stillfeld) werden in allen Dokumenten korrekt und einheitlich verwendet.

**ABER:** In GDD-02, Abschnitt 2.7, steht woertlich: "Die Lebende Krone und das Schattenfieber greifen auf dasselbe 'Ymir-Material' zu". Das ist ein Arbeitsbegriff aus der nordischen Vorlage. Emres WBB-01 hat den RELICS-eigenen Begriff "Emer" explizit eingefuehrt. Und GDD-02, Abschnitt 6.1 warnt selbst davor, dass "Emres WBB-01 nordische Begriffe als Arbeitsbegriffe nutzt — diese muessen VOR der V1-Produktion durch RELICS-eigene Namen ersetzt werden". Darius hat das in seinem eigenen Dokument noch nicht konsequent umgesetzt. Das ist Inkonsistenz Nr. 1.

## 2. Schattenfieber-Stufengrenzen — der grosse Vergleich

Hier wird es interessant. Vier Dokumente definieren Schattenfieber-Schwellenwerte, und sie tun es NICHT identisch.

### GDD-02 (Darius, Mechanik — die Referenz):
- Stufe 0: Wert 0
- Stufe 1 (Gezeichnet/Rauschen): 1-25
- Stufe 2 (Infiziert/Rauschen-Risse): 26-50
- Stufe 3 (Verwandelt/Risse): 51-75
- Stufe 4 (Entfesselt/Schwelle): 76-100

Namis drei narrative Zustaende in GDD-02 Tabelle:
- Rauschen beginnt ab Wert 1, intensiviert sich
- Risse "setzt schrittweise ab ca. Wert 40 ein"
- Schwelle "wird ab ca. Wert 70 spuerbar"

### GDD-03 (Nami, Narrativ):
- Rauschen: ca. 1-40
- Risse: ca. 41-80
- Schwelle: ca. 81-100

### GDD-05 (Vera, Visuell):
- Stufe 1 (Rauschen): 1-40
- Stufe 2-3 (Risse): 41-75
- Stufe 4 (Schwelle): 76-100

### GDD-06 (Tobi, Technik):
- Stufe 0: 0
- Stufe 1: 1-25
- Stufe 2: 26-50
- Stufe 3: 51-75
- Stufe 4: 76-100

**Das Problem:** Namis narrative Grenzen und Darius' mechanische Grenzen laufen NICHT synchron — und das ist teilweise beabsichtigt (weiche vs. harte Grenzen), aber teilweise widerspruechlich:

- In GDD-02 beginnen "Risse" ab ca. Wert 40. In GDD-03 beginnen "Risse" ab Wert 41. Das passt noch.
- ABER: In GDD-03 gehen "Risse" bis Wert 80. In GDD-02 beginnt "Schwelle" ab ca. Wert 70. Das ist ein Overlap von 10 Punkten — Wert 70-80 ist gleichzeitig "Risse" (Nami, GDD-03) und "Schwelle" (Darius, GDD-02).
- Vera (GDD-05) folgt einem Hybrid: Sie verwendet "Rauschen" bis Wert 40 (= Nami), "Risse" fuer Stufen 2-3 also Wert 41-75 (weder Darius noch Nami exakt), und "Schwelle" ab 76 (= Darius).
- Tobi (GDD-06) folgt exakt Darius' fuenf mechanischen Stufen — aber er referenziert AUCH Namis drei Zustaende als Validierungsgrundlage.

Ergebnis: Es gibt eine Grauzone zwischen Wert 70-80, wo die Dokumente sich widersprechen. Das ist Inkonsistenz Nr. 2 — und die wichtigere, weil sie sich direkt auf die Implementierung auswirkt. Tobi muss wissen, ab welchem Wert "Schwelle"-Effekte einsetzen. Seine technische Interpolation startet Halluzinationen ab Wert 70 — das passt zu Darius, aber NICHT zu Nami (die "Schwelle" erst ab 81 ansetzt).

## 3. Fraktions-Farbpalette: GDD-05 vs. GDD-06

Vera (GDD-05) definiert die Krone-Palette als: Aschgrau (#3D3D3D), Karmin (#8B1A2B), Altgold (#C5A030).

Tobi (GDD-06) beschreibt die Krone-Material-Instanzen als: "Eleganter Zerfall. Gold-Patina, Risse in edlem Stein, verwilderte Ornamente. Farben: Warm (Amber, Dunkelgold, Efeugruen)."

Das ist kein direkter Widerspruch — Tobi beschreibt Material-Eigenschaften, nicht die Farbpalette. Aber "Amber" und "Efeugruen" tauchen in Veras Krone-Palette nicht auf. Amber ist bei Vera eine GILDEN-Farbe (#C49A20), und Gruen ist nirgends in der Krone-Palette. Das ist zumindest eine Unschaerfe, die geklaert werden sollte, aber kein harter Widerspruch, weil Tobi explizit auf Material-Instanzen referenziert und nicht auf die UI-Farbpalette.

## 4. Weitere Pruefungen (kein Widerspruch gefunden)

- Lebende Krone: Konsistent als organisches Artefakt der Grossen Flechtung beschrieben (WBB-01, GDD-01, GDD-02, GDD-03, GDD-05)
- Fraktions-Interpretationen: Dreigliedriges Muster (Krone/Gilden/Orden) durchgehend konsistent
- Biotech-Philosophie: "Kein Steampunk, alles organisch" konsistent in allen Dokumenten
- Schattenfieber als "nicht heilbar, nur kontrollierbar": Konsistent in GDD-01, GDD-02, GDD-03
- Kamera (FP/TP nahtlos): GDD-01 und GDD-06 stimmen ueberein
- Engine (UE5): GDD-01 und GDD-06 stimmen ueberein

## Zusammenfassung

Zwei klare Inkonsistenzen gefunden:
1. "Ymir-Material" in GDD-02 statt "Emer-Material" (Terminologie-Versehen)
2. Schattenfieber-Stufengrenzen divergieren zwischen den Dokumenten (Wert 70-80 Grauzone)

Alles andere ist bemerkenswert konsistent fuer Tag 4 einer Produktion mit 7 Autoren.
