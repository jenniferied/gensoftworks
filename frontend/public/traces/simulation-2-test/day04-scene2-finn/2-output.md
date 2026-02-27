# Finn — Tag 4, Szene 2 (WORK) — Output

## Peer-Review: GDD-01 Spielübersicht (Darius, V1)

**Reviewer:** Finn Bergmann, Producer
**Datum:** Tag 4 (Donnerstag), Vormittag
**Bewertung:** Starkes V1-Dokument. Klare Vision, saubere Struktur, gute Referenztrennung. Fünf Punkte müssen in V2 adressiert werden.

---

### Was funktioniert

1. **Elevator Pitch** — Präzise, verkaufbar, differenziert. "Kein Spiel über Auserwählte" ist ein starkes Alleinstellungsmerkmal in einem Markt, der voll davon ist. Der Pitch funktioniert sowohl intern (Teamausrichtung) als auch extern (Pitch-Deck, Store Page).

2. **Validierungstests** — Jede Design-Säule hat ein konkretes Erfolgskriterium. Das ist kein Selbstzweck — das hilft dem ganzen Team bei jeder einzelnen Designentscheidung. Wenn Nami einen Dialog schreibt, kann sie gegen Säule 1 prüfen. Wenn Vera ein Level baut, gegen Säule 6. Das ist Producer-Gold.

3. **Referenzrahmen** — Die Trennung in "Lernen von" und "Anders als" schafft Klarheit. Besonders die Anti-Referenzen (Skyrim-Vampirismus, Witcher-Protagonist, BG3-Combat) helfen, weil sie Diskussionen abkürzen. Wenn jemand fragt "Warum nicht rundenbasiert?" — Antwort steht im GDD-01.

4. **Spielerfahrungs-Bogen** (1h / 10h / 40h) — Exzellent strukturiert, konsistent mit Namis GDD-03. Das ist genau die Art von Dokument, das downstream Arbeit spart.

5. **Monetarisierung** — CD-konform, realistisch, klar. Kein Overscoping.

---

### Was in V2 adressiert werden muss

#### P1 — Scope-Realitätscheck bei drei Säulen

Säulen 1, 3 und 5 sind scope-kompatibel. Bei drei Säulen kollidiert die Vision mit unseren Ressourcen:

| Säule | Problem | Empfehlung |
|--------|---------|------------|
| **2 (Combat)** | Wir haben keinen Gameplay-Programmer. "Präzises" Real-Time-Combat in Blueprints ist grenzwertig. Das Risiko steht in der ROADMAP als "Kritisch/Hoch". | V2 sollte einen Absatz enthalten, der die Combat-Ambition explizit an Tobis Machbarkeitsanalyse koppelt. "Die vollständige Umsetzung dieses Systems setzt einen Gameplay-Programmer voraus" — das muss drinstehen, nicht nur in der ROADMAP. |
| **4 (Weltdichte)** | "Jeder NPC hat einen Namen und Tagesablauf" + 4-6 km2 + null Filler. Gothic 2 hatte dafür 30+ Leute. Wir sind 7. | V2 sollte den Vertical-Slice-Scope explizit benennen: Eine Stadt, ein Dungeon, ein Queststrang — das ist die machbare Einheit. Der Rest ist Vision für Skalierung. |
| **6 (Vertikalität)** | "Dishonored in Open World" existiert nicht, weil es extrem teuer ist. Jeder vertikale Weg muss handgebaut werden. Vera allein kann das nicht. | V2 sollte klären, wie die Vertikalität mit Houdini-Terrain und modularen Kits skalierbar wird. Verweis auf GDD-06 Kap. 4 (Tobis Pipeline). |

Das ist kein Urteil über die Vision. Die Vision ist stark. Aber ein GDD, das nicht sagt, wo die Grenzen sind, wird in der Produktion zum Problem.

#### P2 — Zielgruppen-Diskrepanz

Darius schreibt "22 bis 35". Leo hat "25 bis 40" identifiziert. Beides kann nicht stimmen:

- **Unteres Ende:** Ein 22-Jähriger war 0, als Gothic 2 rauskam. Die Gothic-Community, die Darius als "klein, laut, loyal" beschreibt, fängt realistisch bei 28+ an.
- **Oberes Ende:** Leo hat recht — die Zielgruppe ist älter geworden. 35 als Obergrenze schneidet genau die Leute ab, die Gothic damals gespielt haben und jetzt Geld haben.

**Empfehlung:** 25-40 übernehmen, wie Leo es identifiziert hat. Das ist ehrlicher und schliesst die tatsächliche Kernzielgruppe ein. Darius und Leo sollten das im Bilateral klären.

#### P3 — Kamerapriorität unklar

Das Briefing und CD-Entscheidung Nr. 7 sagen: "TP Primärmodus, FP ist V2". Das bedeutet: 70% weniger Animationsarbeit in Phase 1.

GDD-01 schreibt: "Third-/First-Person Action-RPG (nahtlos umschaltbar)". Das klingt nach Gleichberechtigung beider Modi. Wenn Tobi das liest, plant er Animation für beide. Wenn Vera das liest, modelliert sie Waffen, die in FP funktionieren müssen.

**Empfehlung:** V2 muss klar sagen: "Third-Person ist der Primärmodus. First-Person-Unterstützung ist für eine spätere Entwicklungsphase geplant." Ein Satz. Spart Wochen.

#### P4 — Fehlende Elemente aus dem Briefing

Zwei Punkte aus dem Briefing/CD-Entscheidungen fehlen im GDD-01:

1. **Tiervolk** — Das Briefing definiert sie als "Händler und Diebe, NICHT Handwerker, leicht alien vs. menschlich clean." Im GDD-01 kommen sie nicht vor. Für ein Übersichtsdokument muss das mindestens erwähnt werden — in der Weltbeschreibung oder bei den Fraktionen. Die sind ein visuell und narrativ wichtiges Element.

2. **Biotech-Sichtbarkeit ist fraktionsabhängig** (CD-Entscheidung Nr. 4) — Das USP "Biotech-Medieval" wird beschrieben, aber nicht, dass die Sichtbarkeit der Biotech je nach Fraktion variiert. Das ist ein zentraler Designhebel, der in V2 rein muss.

#### P5 — Konsequenz-Versprechen quantifizieren

"Jede Entscheidung hat Konsequenzen" steht mehrfach im Dokument. Das ist ein Versprechen, das exponentiell Aufwand erzeugt. Jeder Entscheidungsknoten mit 3 Ausgängen, der wiederum 3 Folgezustände hat, produziert Content-Bedarf, der schnell unbezahlbar wird.

**Empfehlung:** V2 sollte definieren, was "Konsequenz" konkret bedeutet. Vorschlag: Konsequenzen operieren auf drei Ebenen — (1) Dialogreaktion (billig), (2) Fraktionsreputation (mittel), (3) Weltzustandsänderung (teuer). Das gibt Nami und Emre ein Werkzeug, um Konsequenzen zu planen, ohne dass jede Nebenquest drei Enden mit eigenen Cutscenes braucht.

---

### Zusammenfassung für Darius

Moin Darius. Starkes Dokument. Die Vision sitzt, der Pitch verkauft, die Validierungstests sind das Beste, was bisher aus dem GDD rausgekommen ist. Fünf Punkte für V2: Scope-Realität bei drei Säulen benennen, Zielgruppe mit Leo abgleichen, Kamera-Priorität präzisieren, Tiervolk und Biotech-Fraktionssichtbarkeit ergänzen, Konsequenz-Versprechen operationalisieren. Nichts davon ist ein Richtungswechsel — alles ist Präzisierung. Was brauchst du von mir?

---

*Finn Bergmann, Küche (Kaffee), Tag 4 Donnerstag Vormittag*
