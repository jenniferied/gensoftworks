# Cross-Document-Konsistenz-Report

**Autorin:** Leo Fischer, QA Lead
**Datum:** Tag 4 (Donnerstag), Szene 2 — Peer-Review-Session
**Gegenstand:** Alle 6 Kerndokumente (WBB-01, GDD-01, GDD-02, GDD-03, GDD-05, GDD-06)
**Methode:** Systematischer Abgleich nach Terminologie, Stufengrenzen, Fraktionslogik und Widerspruechen

---

## 1. Gesamtbefund

Die dokumentenuebergreifende Konsistenz ist fuer Tag 4 einer Produktion mit sieben Autoren bemerkenswert hoch. Die kosmologische Grundlage aus WBB-01 (Emre) traegt alle Dokumente. Das Drei-Fraktionen-Modell (Krone/Gilden/Orden) ist in jedem Dokument korrekt und mit der jeweils richtigen Perspektive umgesetzt. Biotech-Philosophie ("kein Steampunk, alles organisch"), Schattenfieber als "nicht heilbar, nur kontrollierbar", die Lebende Krone als organisches Artefakt der Grossen Flechtung — das zieht sich sauber durch.

Trotzdem: Zwei Inkonsistenzen, die jetzt behoben werden muessen, bevor die V2-Produktion beginnt.

---

## 2. Terminologie-Konsistenz (WBB-01 als Referenz)

### Befund: Ueberwiegend sauber

Emres kosmologisches Lexikon (WBB-01) definiert die verbindlichen RELICS-eigenen Begriffe. Ich habe alle GDD-Dokumente gegen dieses Lexikon geprueft:

| Begriff | WBB-01 | GDD-01 | GDD-02 | GDD-03 | GDD-05 | GDD-06 |
|---------|--------|--------|--------|--------|--------|--------|
| Emer (Urwesen) | Definiert | Korrekt | **"Ymir-Material"** | Korrekt | Korrekt | — |
| Mittelgrund | Definiert | Korrekt | Korrekt | Korrekt | Korrekt | Korrekt |
| Hohlicht / Stillfeld | Definiert | — | — | Korrekt | Korrekt | — |
| Hauten (Membranen) | Definiert | — | — | Korrekt | Korrekt | — |
| Grosse Flechtung | Definiert | — | "Ur-Bindung" | Korrekt | Korrekt | — |
| Faulung / Schwund / Entflechtung | Definiert | Korrekt | — | Korrekt | Korrekt | — |
| Lebende Krone | Definiert | Korrekt | Korrekt | Korrekt | Korrekt | — |
| Tharm (Gilden-Name) | Definiert | — | — | Korrekt | — | — |

### INKONSISTENZ NR. 1: "Ymir-Material" in GDD-02

**Fundstelle:** GDD-02, Abschnitt 2.7: "Die Lebende Krone und das Schattenfieber greifen auf dasselbe 'Ymir-Material' zu (WBB-01, Kap. 6)."

**Problem:** "Ymir" ist der nordische Arbeitsname. Emres WBB-01 hat den RELICS-eigenen Begriff "Emer" eingefuehrt — mit klarer Herleitung aus urgermanisch *aima-*. Das Lexikon in WBB-01 stellt ausdruecklich klar: "Alle nordischen Begriffe dienen als Entwickler-Referenz. In der Spielwelt existieren ausschliesslich die RELICS-eigenen Bezeichnungen."

Ironischerweise warnt GDD-02 selbst in Abschnitt 6.1 (Namenssysteme): "Emres WBB-01 nutzt nordische Begriffe als Arbeitsbegriffe — diese muessen VOR der V1-Produktion durch RELICS-eigene Namen ersetzt werden." Darius hat seine eigene Regel nicht konsequent angewandt.

Zusaetzlich: GDD-02 verwendet an einer Stelle den Begriff "Ur-Bindung" statt "Grosse Flechtung". WBB-01 definiert "die Flechtung" und "die Grosse Flechtung" als korrekte Begriffe. "Ur-Bindung" existiert im Lexikon nicht.

**Schwere:** Niedrig — reiner Textfehler, kein Designproblem.

**Empfehlung:** Darius ersetzt in der V2 "Ymir-Material" durch "Emer-Material" und "Ur-Bindung" durch "Grosse Flechtung". Drei Minuten Arbeit.

---

## 3. Schattenfieber-Stufengrenzen — Cross-Document-Abgleich

### Befund: Systematische Divergenz in der Grauzone

Vier Dokumente definieren Schattenfieber-Schwellenwerte. Sie verwenden zwei verschiedene Systeme (Darius: 5 mechanische Stufen, Nami: 3 narrative Zustaende) und mappen sie unterschiedlich aufeinander.

### Die Tabelle der Wahrheiten

| Infektionswert | GDD-02 (Darius, Mechanik) | GDD-03 (Nami, Narrativ) | GDD-05 (Vera, Visuell) | GDD-06 (Tobi, Technik) |
|----------------|--------------------------|------------------------|------------------------|------------------------|
| 0 | Stufe 0 (Rein) | Gesund | — | Stufe 0 (Baseline) |
| 1-25 | Stufe 1 (Gezeichnet) | Rauschen | Rauschen | Stufe 1 |
| 26-40 | Stufe 2 (Infiziert) | Rauschen | Rauschen | Stufe 2 |
| **41-50** | **Stufe 2 (Infiziert)** | **Risse** | **Risse** | **Stufe 2** |
| 51-69 | Stufe 3 (Verwandelt) | Risse | Risse | Stufe 3 |
| **70-75** | **Stufe 3 (Verwandelt)** | **Risse** | **Risse** | **Stufe 3 (Halluzinationen starten!)** |
| **76-80** | **Stufe 4 (Entfesselt)** | **Risse** | **Schwelle** | **Stufe 4** |
| 81-100 | Stufe 4 (Entfesselt) | Schwelle | Schwelle | Stufe 4 |

### INKONSISTENZ NR. 2: Die Grauzone Wert 70-80

**Kern des Problems:** Es gibt drei Konfliktstellen:

**a) Wert 70-75 — Halluzinationen vor der Schwelle.**
Tobis technische Interpolation (GDD-06, Kap. 5.4) startet Halluzinations-Effekte ab Infektionswert 70: "Halluzinationen: Aktivierung ab Wert 70, Intensitaet skaliert mit (Infektionswert - 70) / 30". Das heisst: Ein Spieler bei Wert 72 sieht bereits Halluzinationen. Laut Nami (GDD-03) ist dieser Spieler aber noch im Zustand "Risse" — nicht "Schwelle". Die Halluzinations-Effekte sind narrativ ein Schwelle-Phaenomen. Technisch starten sie bereits in den Rissen.

**b) Wert 76-80 — Entfesselt, aber noch Risse.**
Darius' mechanische Stufe 4 (Entfesselt) beginnt bei Wert 76. Namis narrativer Zustand "Schwelle" beginnt erst bei Wert 81. Das heisst: Ein Spieler bei Wert 78 ist mechanisch "entfesselt" und hat Zugang zu Apex-Faehigkeiten — erlebt aber narrativ noch "Risse" statt "Schwelle". Die Parallel-Narrative und die moeglicherweise-nicht-existierenden NPCs, die Nami fuer die Schwelle beschreibt, muessten laut ihrer eigenen Logik erst ab 81 einsetzen. Aber Tobi baut schon ab 76 die volle Stufe-4-Rendering-Pipeline.

**c) Vera-Hybrid.**
Vera (GDD-05) hat einen eigenen Kompromiss gebaut: Ihre visuelle "Stufe 1: Rauschen" geht bis Wert 40 (= Nami), ihre "Stufe 2-3: Risse" geht von 41-75 (= Darius fuer das obere Ende), und "Stufe 4: Schwelle" startet bei 76 (= Darius). Das ist in sich logisch, weicht aber sowohl von Namis Grenzen (Risse bis 80) als auch von Tobis Halluzinations-Start (70) ab.

**Schwere:** Mittel bis hoch — das betrifft direkt die Implementierung. Wenn Tobi ab Wert 70 Halluzinationen rendert, aber Nami erst ab Wert 81 Schwelle-Dialoge liefert, erlebt der Spieler 10 Punkte lang visuelle Halluzinationen mit Risse-Dialogen. Das ist entweder ein Feature (die visuellen Effekte laufen der narrativen Erfahrung voraus) oder ein Bug (der Spieler sieht Dinge, zu denen die Geschichte noch nicht passt).

**Empfehlung:** Darius, Nami und Tobi muessen sich auf EINE verbindliche Schwellenwert-Tabelle einigen. Mein Vorschlag als QA:

| Narrativer Zustand | Infektionswert | Mechanische Stufen |
|--------------------|--------------:|-------------------|
| Gesund | 0 | Stufe 0 |
| Rauschen | 1-40 | Stufe 1 (1-25) + Stufe 2 (26-40) |
| Risse | 41-75 | Stufe 2 (41-50) + Stufe 3 (51-75) |
| Schwelle | 76-100 | Stufe 4 (76-100) |

Das heisst: Tobis Halluzinations-Start verschiebt sich von 70 auf 76. Namis "Risse" enden bei 75 statt 80. Veras Mapping bleibt wie es ist. Darius' fuenf mechanische Stufen bleiben unveraendert — nur das Mapping auf die narrativen Zustaende wird geschaerft.

---

## 4. Weitere Pruefpunkte (keine Widersprueche)

### Lebende Krone
Konsistenz ueber alle Dokumente. Ueberall als organisches Artefakt der Grossen Flechtung beschrieben. Fraktions-Interpretationen (Krone: dynastisches Erbe, Gilden: Handelsgut, Orden: Erkenntniswerkzeug) stimmen in WBB-01, GDD-01, GDD-02, GDD-03 und GDD-05 ueberein.

### Biotech-Philosophie
"Kein Steampunk, alles organisch" — durchgehend konsistent. GDD-01 (Design-Saeule), GDD-05 (Biotech-Grammatik), GDD-06 (Material-Pipeline) sagen alle dasselbe.

### Fraktionslogik
Drei Fraktionen, drei Perspektiven, keine ist gut oder boese — in allen Dokumenten korrekt. Die tragische Ironie der Krone (beansprucht Stabilitaet, beschleunigt Faulung) wird in WBB-01, GDD-01 und GDD-03 korrekt beschrieben.

### Kamera und Engine
FP/TP nahtlos umschaltbar (GDD-01 Saeule, GDD-06 Kamera-System): konsistent. UE5 als Engine: konsistent.

### Farbpalette — Unschaerfe (kein Widerspruch)
Vera (GDD-05) definiert Krone-Farben als Aschgrau, Karmin, Altgold. Tobi (GDD-06) beschreibt Krone-Materialien mit "Amber, Dunkelgold, Efeugruen". Das ist keine direkte Kollision — Tobi beschreibt Material-Instanzen auf Asset-Ebene, nicht die UI/Art-Direction-Palette. Trotzdem sollte Vera mit Tobi einmal abgleichen, ob "Efeugruen" als Krone-Material-Farbe in die verbindliche Palette gehoert oder ob das ein Tobi-Sologang ist.

---

## 5. Spielergefuehl-Check

Kurzer Perspektivwechsel — nicht als QA, sondern als Spielerin:

Wenn ich diese Dokumente als zusammenhaengende Vision lese, dann STIMMT die Vision. Die Welt fuehlt sich an wie ein Ort, den ich betreten moechte. Das Schattenfieber klingt wie etwas, das ich freiwillig ausprobieren wuerde — und das ist das hoechste Lob, das ich einer Infektionsmechanik machen kann. Die Fraktionen klingen wie Gruppen, bei denen ich mich NICHT entscheiden koennte — und das ist genau das Ziel.

Was mich als Spielerin stoeren wuerde: Wenn die Halluzinationen vor den passenden Dialogen kommen. Wenn ich bei Wert 72 Waende atmen sehe, aber die NPCs noch so reden, als waere alles normal — dann merke ich das. Und dann bricht die Immersion. Genau deshalb muss Inkonsistenz Nr. 2 behoben werden.

---

## 6. Zusammenfassung und Massnahmen

| Nr. | Inkonsistenz | Schwere | Verantwortlich | Empfehlung |
|-----|-------------|---------|---------------|------------|
| 1 | "Ymir-Material" und "Ur-Bindung" in GDD-02 statt RELICS-eigener Begriffe "Emer-Material" und "Grosse Flechtung" | Niedrig | Darius | Suchen-Ersetzen in V2. Drei Minuten. |
| 2 | Schattenfieber-Stufengrenzen divergieren: Halluzinationen ab Wert 70 (Tobi), Schwelle ab Wert 81 (Nami), Stufe 4 ab Wert 76 (Darius) | Mittel-Hoch | Darius + Nami + Tobi | Verbindliche Schwellenwert-Tabelle. Mein Vorschlag: Rauschen 1-40, Risse 41-75, Schwelle 76-100. Halluzinations-Start = 76. |

**Bonus-Hinweis:** Vera und Tobi sollten die Krone-Materialfarben abgleichen (Efeugruen?). Kein Blocker, aber besser jetzt als bei der Asset-Produktion.

---

*Leo Fischer, QA-Ecke, Tag 4 Donnerstag Vormittag. Sechs Dokumente, zwei Fehler, eine Vision, die haelt.*
