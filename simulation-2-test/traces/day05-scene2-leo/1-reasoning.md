# Reasoning — Leo Fischer, Tag 05, Szene 2

Ich gehe die fünf Prüfpunkte durch, Dokument für Dokument, so wie ich es auch live spielen würde: ohne Vorwissen, nur mit dem, was auf dem Bildschirm steht.

---

## 1. Stufentabelle

**GDD-02 (Darius, V0.5):**
Tabelle in Kap. 2.3: Stufe 1 = 1–25 (Rauschen), Stufe 2 = 26–50 (Rauschen→Risse), Stufe 3 = 51–75 (Risse), Stufe 4 = 76–100 (Schwelle).
Der Übergangstext präzisiert: "Risse setzt schrittweise ab ca. Wert 40 ein. Schwelle wird ab ca. Wert 70 spürbar."
Das ist eine "weiche Grenzen"-Formulierung, kein festes Mapping.

**GDD-05 (Vera, V1):**
Kap. 7.2 sagt explizit:
- Stufe 1: Rauschen, Infektionswert **1–40**
- Stufe 2–3: Risse, Infektionswert **41–75**
- Stufe 4: Schwelle, Infektionswert **76–100**

Das ist ein HARTES Mapping, abweichend von Darius' Stufentabelle (1–25 / 26–50 / 51–75 / 76–100).

**GDD-03 (Nami, V1):**
Kap. — Rauschen ca. **1–40**, Risse ca. **41–80**, Schwelle ab **80+** (implizit).
Nami schreibt "ca." — weiche Grenzen, aber mit anderen Zahlenwerten als Vera.

**GDD-06 (Tobi, V1):**
Kap. 5.3 nennt Stufen als Gameplay-Ebenen (0/1/2/3/4) und ordnet ihnen technische Effekte zu.
Der Graduelle-Interpolation-Abschnitt (5.4) nennt: Halluzinationen ab Wert 70, Geometrische Verzerrung ab ~45. Das deckt sich eher mit Namis "weichen" Grenzen als mit Veras hartem 41-75/76-100-Schema.

**Fazit — Stufentabelle:**
INKONSISTENZ. Drei verschiedene Mappings kursieren:
- Darius: mechanische Stufen 0–4, narrative Zonen als "weiche Grenzen" mit ~40 und ~70 als Orientierungspunkten
- Vera: hartes visuelles Schema 1–40 / 41–75 / 76–100
- Nami: hartes narratives Schema ca. 1–40 / ca. 41–80 / 80+

Vera und Nami widersprechen sich konkret: Vera setzt Risse bis 75, Nami bis 80. Schwelle beginnt bei Vera mit 76, bei Nami erst bei ~80+. Das sind fünf Punkte Differenz — klingt klein, ist aber gameplay-relevant (wo genau wechselt der Parallel-Narrativ ein?). Ausserdem stimmen weder Vera noch Nami mit Darius' mechanischer Basistabelle überein, die Stufe 3 bei 51–75 setzt, nicht bei 41–75.

---

## 2. Emer-Terminologie

**WBB-01 (Emre, V1):**
Lexikon ist vollständig und konsistent. Alle Kernbegriffe definiert: Galt, Emer, Tharm, Hohlicht, Mittelgrund, Stillfeld, Hauten, Flechtung etc.
Emer taucht in allen Folgedokumenten auf — ich prüfe, ob die Verwendung korrekt ist.

**GDD-05 (Vera):**
"Die Welt wurde aus dem Emer geformt" — korrekt.
"Emer-Material" — korrekt als Werkstoff-Begriff.

**GDD-02 (Darius):**
"Ymir-Material" in Kap. 2.7 — das ist der INTERNE Entwickler-Begriff, nicht die Spielwelt-Bezeichnung. Emre hat im WBB-01 explizit festgelegt, dass nordische Begriffe NUR als Entwickler-Referenz dienen und in der Spielwelt durch RELICS-eigene Namen ersetzt werden müssen. "Ymir-Material" hätte in GDD-02 bereits durch "Emer-Material" ersetzt werden sollen. Ist es nicht.

**GDD-03 (Nami), GDD-06 (Tobi):**
Verwenden konsequent "Emer-Material" — korrekt.

**Fazit — Terminologie:**
EIN Fehler: GDD-02 Kap. 2.7 verwendet noch "Ymir-Material". Muss auf "Emer-Material" korrigiert werden. Sonst konsistent.

---

## 3. Hex-Codes

**GDD-05 (Vera) — die Quelle:**
Krone: `#3D3D3D`, `#8B1A2B`, `#C5A030`
Gilden: `#7A6E5D`, `#C49A20`, `#2EC4B6`
Orden: `#E8E4DE`, `#4A5568`, `#D4A017`
Schattenfieber: `#2D0A31`, `#39FF14`
Tiervolk: `#CC7722`, `#C04000`, `#C2B280`

Krone-Biolumineszenz in Kap. 8.4: `#C5A030` — stimmt mit Highlight überein.
Gilden-Licht: `#C49A20` bis `#2EC4B6` — korrekt.
Orden-Licht: `#E8E4DE` — korrekt.

**GDD-06 (Tobi):**
Keine Hex-Codes direkt genannt — verweist auf "Krone: Warm (Amber, Dunkelgold, Efeugrün)" und "Gilden: Kühle Toene (Blaugrün, Bronze, Schwarz)". Das ist Beschreibung, kein Code-Verweis. Kein Konflikt, aber auch keine Bestätigung.

**Fazit — Hex-Codes:**
Konsistent innerhalb GDD-05. Kein anderes Dokument widerspricht. GDD-06 nutzt Textbeschreibungen statt Codes — kein Fehler, aber Vera sollte Tobi die Palette formell übergeben, damit Shader-Arbeit auf denselben Werten basiert.

---

## 4. Ungefüge

**WBB-01 (Emre):**
Im Kosmologischen Lexikon definiert: "Der Ungefüge — Kein Name, nur Titel. 'Der, der nicht passt.' Keiner Fraktion zugeordnet." In Kap. 5 als mythologische Figur ausgeführt (Loki-Referenz). Konsistent und vollständig.

**GDD-01, GDD-02, GDD-03, GDD-05, GDD-06:**
Kein einziges Mal erwähnt. Der Ungefüge ist als mythologischer Hintergrund in WBB-01 kanonisiert, aber in keinem GDD-Dokument operationalisiert. Das muss nicht zwingend ein Fehler sein — Emres Aufgabe ist WBB, nicht GDD. Aber als QA-Hinweis: Die Figur wird bisher nur im Mythos-Layer gehalten. Wenn der Ungefüge narrativ relevant werden soll (und bei einer Loki-Figur wäre das naheliegend), braucht es eine Absprache mit Nami für GDD-03/04.

**Fazit — Ungefüge:**
In WBB-01 kanonisiert. In GDD-Dokumenten nicht aufgegriffen. Kein Widerspruch, aber fehlende Brücke zwischen Lore und Gameplay-Narrativ.

---

## 5. Flechtfest

**GDD-03 (Nami, V1):**
Erwähnt zweimal:
- Kap. 2.3 Tonalität: "eine Krone-Wache erwähnt beiläufig 'das Flechtfest', als wäre es Allgemeinwissen"
- Kap. 4.1 Dialogsystem-Beispielabschnitt (Krone-Vokabular): "Sie spricht vom 'Flechtfest', als wäre es gestern gewesen."

Flechtfest wird als Krone-spezifischer Kulturbegriff für das Ereignis der Grossen Flechtung behandelt — ein Fest oder Gedenktag. Das passt zu WBB-01 (Grosse Flechtung als historischer Nullpunkt).

**WBB-01 (Emre):**
Das Wort "Flechtfest" taucht nicht auf. Emre nennt die Grosse Flechtung, aber keinen Feiertag oder Kulturritus, der darauf basiert.

**Fazit — Flechtfest:**
Nami hat den Begriff eingeführt ohne Abstimmung mit Emre. Kein Widerspruch zum WBB, aber auch keine Verankerung darin. Entweder Emre fügt Flechtfest ins WBB-03 (Ethos/Kultur) ein, oder Nami bestätigt die Herkunft des Begriffs. Momentan: einseitig kanonisiert, nicht durchgehend verankert.

---

## Gesamtbewertung

| Punkt | Status | Schwere |
|---|---|---|
| Stufentabelle | INKONSISTENZ — drei verschiedene Mappings | HOCH |
| Emer-Terminologie | EIN Fehler — GDD-02 Kap. 2.7 "Ymir-Material" | NIEDRIG |
| Hex-Codes | Konsistent | OK |
| Ungefüge | Kanonisiert in WBB, nicht operationalisiert in GDD | HINWEIS |
| Flechtfest | Einseitig eingebracht (Nami), kein WBB-Anker | MITTEL |
