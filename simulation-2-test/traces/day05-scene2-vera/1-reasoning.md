# Vera — Tag 05, Szene 2 (WORK) — Reasoning

## Was ich gelesen habe

- GDD-05 V1 (gallery) — vollständiger Text, Status Tag 3
- GDD-02 V0.5 (gallery) — Stufen-Mapping, Nervensystem, Trainer-System
- Logbuch day04-scene2 — Darius-Review meines GDD-05
- Logbuch day04-scene3 — CD-Entscheidung Stufengrenzen
- Logbuch day04-scene5 — V2-Arbeiten stattgefunden (Vera: "Stufe-0-Baseline, neue Stufengrenzen, Gameplay-Orte, gemischte Sets")
- Logbuch day05-scene1 — Briefing: GDD-05 V2 finalisieren

## Diagnose: Was fehlt / falsch ist in V1

### 1. Stufengrenzen — Befund

GDD-05 V1 Kap. 7.2 hat bereits die richtigen narrativen Grenzen:
- Stufe 1: Rauschen (1-40) → korrekt
- Stufe 2-3: Risse (41-75) → korrekt
- Stufe 4: Schwelle (76-100) → korrekt

Aber: In V1 werden "Stufe 1", "Stufe 2-3", "Stufe 4" als visuelle Bezeichner genutzt. Das ist inkonsistent mit GDD-02 (mechanische Stufen 0-4) und der CD-Tabelle. In V2 muss ich klar zwischen NARRATIVEN Zuständen (Rauschen/Risse/Schwelle) und MECHANISCHEN Stufen (0-4) unterscheiden.

### 2. Stufe-0-Baseline — Befund

Fehlt komplett in V1. GDD-02 definiert Stufe 0 explizit mit visuellen Implikationen (volle Nervensystem-Effizienz, keine Schatten-Überlagerungen). GDD-05 springt direkt in Rauschen. Das ist ein Loch: Wie sieht der Spieler OHNE Infektion aus? Wie sieht die Welt ohne Schattensinne aus? Baseline nötig für alles was darüber liegt.

### 3. Gameplay-Orte — Befund

V1 Kap. 8 (Environments) beschreibt Regionstypen (Krone-Stadt, Gilden-Stadt, etc.) aber KEINE gameplay-spezifischen Orte. Darius nennt explizit: Alchemie-Station, Trainer, Händler. Diese drei sind in GDD-02 mechanikseitig definiert, fehlen aber in GDD-05 visuell. Ohne Fraktionsvarianten weiß kein Art-Director, wie ein Gilden-Trainer vs. Krone-Trainer aussieht.

### 4. Hex-Codes — Befund

Mein eigenes Review von GDD-06 (Tag 4): Tobi hat die Hex-Codes teilweise übernommen, aber es gab einen Widerspruch bei Krone-Biolumineszenz. GDD-05 schreibt `#C5A030` (Altgold-Highlight). GDD-06 muss dieselben Werte haben. Ich prüfe: In GDD-05 V1 stehen alle Fraktions-Paletten mit Hex-Codes — die müssen 1:1 in V2 übertragen werden, ohne Abweichungen.

ACES-Validierung: ACES-Mapping bedeutet sRGB-Werte, die im UE5-Tonemapping (ACES) korrekt aussehen. Warme Farben (Altgold, Amber) müssen leicht tiefer angesetzt sein als im Display-normalen Raum, weil ACES sie aufhellt. Die bestehenden Hex-Codes in V1 sind bereits mit diesem Offset designed. In V2 nichts ändern — nur bestätigen.

### 5. Gemischte Sets — Befund

V1 Kap. 5.4 erwähnt Customization-System, aber kein Dominanzprinzip. Problem: Wenn Spieler Krone-Samtumhang + Gilden-Chitin-Stiefel kombiniert — welche Fraktionsfarbe dominiert? Wie liest das UI? Das Prinzip muss in V2 explizit stehen: Mehrheitsregel (>50% Fraktion = Fraktionslesen), oder Oberkörper-Dominanz (Rüstungstorso bestimmt Fraktion), oder Layer-Hierarchie.

## Entscheidungen für V2

- Stufengrenzen: Einheitliche Referenztabelle einfügen, beide Systeme (narrativ + mechanisch) klar trennen
- Stufe-0-Baseline: Neues Unterkapitel in Kap. 7, vor Rauschen
- Gameplay-Orte: Neues Unterkapitel in Kap. 8, pro Ort drei Fraktionsvarianten
- Hex-Codes: Bestehende Codes beibehalten, ACES-Hinweis ergänzen
- Dominanzprinzip: Oberkörper-Dominanz — der Torso-Slot bestimmt die Fraktionslesbarkeit; Akzente (bis 2 abweichende Slots) werden toleriert, drei oder mehr abweichende Slots = visuell neutral (Händler-Lesart)
- Version-Header: V1 → V2 aktualisieren, Tag 3 → Tag 5

## Strukturplan V2

Alle bestehenden Kapitel bleiben. Änderungen:
- Header: Status + Version + Datum
- Kap. 7.2: Einheitliche Stufentabelle vorne, dann Stufe-0-Baseline als neuer Block
- Kap. 7.2 Abschnitte: "Stufe 0: Rein", dann "Rauschen", "Risse", "Schwelle" (konsistente Namensgebung)
- Kap. 8.5 (neu): Gameplay-Orte
- Kap. 5.4: Dominanzprinzip ergänzen
- Kap. 4.4: ACES-Hinweis ergänzen
