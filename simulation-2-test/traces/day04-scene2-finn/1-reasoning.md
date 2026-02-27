# Finn — Tag 4, Szene 2 (WORK) — Reasoning

## Meine Ueberlegungen zum Review

### 1. Design-Saeulen — Scope-Check

Sechs Saeulen. Ich gehe sie einzeln durch:

**Saeule 1 (Spielerwelt-Immersion):** Character Creator, reaktive NPCs, kein Auserwaehlter. Realistisch im Scope? Character Creator ist UE5-Standard (MetaHuman oder Modular-Kit). Reaktive NPCs mit Fraktionsreputation — das ist Datenbank-Arbeit und Quest-Scripting, kein technisches Monster. Machbar. ABER: "Jede Entscheidung hat Konsequenzen" ist ein Versprechen, das exponentiell Aufwand erzeugt. Das muss ich flaggen.

**Saeule 2 (Real-Time Combat):** Kein Difficulty Slider, gewichtiges Melee, Skill-Ceiling als Spektrum. Grosses Problem: Wir haben keinen Gameplay-Programmer. Das steht in der Risiko-Tabelle als "Kritisch/Hoch". Darius schreibt ein System, das wir aktuell nicht implementieren koennen. Blueprint-Prototyp als Bruecke, ja — aber ein "praezises" Kampfsystem in Blueprints ist grenzwertig. Muss rein ins Review.

**Saeule 3 (Koerperliche Progression):** Nervensystem-Leveling, Trainer in der Welt, transformative Perks. Konzeptionell stark, technisch ueberschaubar (UI-System + Stat-Management). Der Trainer-Ansatz reduziert sogar Content-Aufwand im Vergleich zu einem vollen Skill-Tree, weil er Progression an existierende NPCs koppelt. Kein Scope-Problem.

**Saeule 4 (Handgemachte Weltdichte):** "Jeder NPC hat einen Namen und Tagesablauf." 4-6 km2. Null Filler-Quests. Das ist die teuerste Saeule. Gothic 2 hatte 400+ NPCs mit Tagesablaeufen — dafuer ein Team von 30+ Leuten. Wir sind 7. Auch wenn die Semi-Open-World kleiner ausfaellt: Dieser Anspruch muss gegen die Realitaet geprueft werden. Fuer den Vertical Slice machbar (eine Stadt, ein Dungeon), fuer das volle Spiel ohne Teamvergroesserung nicht. Muss rein.

**Saeule 5 (Fraktionsdynamik):** Drei Fraktionen, exklusive Inhalte, Replay-Motivation. Das ist narrativer Content, kein Tech-Problem. Nami und Emre koennen das konzipieren. Der Haken: Drei exklusive Questlines bedeuten 3x Produktionsaufwand bei 1x Spielzeit pro Durchgang. Klassisches RPG-Dilemma. Fuer die Konzeptphase kein Blocker, aber fuer die Produktionsplanung kritisch.

**Saeule 6 (Vertikales Raumdesign):** "Was du siehst, kannst du erreichen" + Sightline-Navigation + keine Ladebildschirme. Das ist der USP Nr. 3 als Level-Design-Prinzip. Dishonored in Open-World — gibt es nicht, weil es extrem teuer ist. Jeder vertikale Weg muss handgebaut werden. Vera allein kann das nicht. Houdini-Terrain hilft bei Landschaft, aber nicht bei begehbaren Daechern. Flaggen.

**Fazit Saeulen:** Saeulen 1, 3, 5 sind scope-kompatibel. Saeulen 2, 4, 6 haben Scope-Risiken, die im Dokument nicht adressiert werden. Darius schreibt wie ein Game Director mit 50 Leuten — das ist sein Job, die Vision gross zu denken. Mein Job ist, die Stellen zu markieren, wo Vision und Ressourcen kollidieren.

### 2. Zielgruppe — Diskrepanz

Darius schreibt "22 bis 35". Leo hat in seinem Spielerperspektiv-Bericht "25-40" identifiziert. Das ist eine signifikante Diskrepanz am unteren UND oberen Ende:
- 22-24: Sind die wirklich Hardcore-RPG-Spieler, die mit Gothic sozialisiert wurden? Gothic 2 ist von 2002. Ein 22-Jaehriger war damals 0. Das passt nicht.
- 35-40: Leo hat recht — die Gothic-Community ist aelter geworden. Die sind jetzt 30-45. Das obere Ende wegzuschneiden verliert genau die Community, die Darius in der Kernzielgruppe als "klein, laut, loyal" beschreibt.

Empfehlung: 25-40 uebernehmen, wie Leo es hat. Das ist ehrlicher und schliesst die tatsaechliche Gothic-Community ein.

### 3. Referenzrahmen vs. CD-Entscheidungen

Ich pruefe gegen die 11 bestaetigten CD-Punkte:

- CD-7 sagt "TP Primaermodus, FP ist V2". Darius schreibt "Third-/First-Person (nahtlos umschaltbar)". Das klingt nach Gleichberechtigung beider Modi. Muss praezisiert werden — TP ist Primary, FP kommt spaeter. Sonst plant Tobi Animation fuer beide Modi gleichzeitig, und wir verlieren den 70%-Vorteil.
- CD-4 sagt "Biotech-Sichtbarkeit fraktionsabhaengig". Im Dokument steht "Biotech-Medieval" als USP, aber die Fraktionsabhaengigkeit der Sichtbarkeit wird nicht erwaehnt. Fehlt.
- CD-9 "Krone bewusst blind" — steht gut im Fraktionsabschnitt: "bemerkt aber nicht, dass sie selbst zum Verfall beitraegt". Check.
- CD-10 Arbeitstitel "RELICS: Die Lebende Krone" — durchgaengig verwendet. Check.
- "Tiervolk" aus dem Briefing (Haendler und Diebe, nicht Handwerker, leicht alien) — kommt im GDD-01 ueberhaupt nicht vor. Das ist eine Luecke. Muss mindestens erwaehnt werden.

### 4. Budget/Timeline

Tobis GDD-06 sagt 45k EUR Budget. Das Dokument verspricht:
- Character Creator (MetaHuman-basiert oder modular: kostet Zeit, nicht Geld)
- Vertikales Raumdesign ohne Ladebildschirme (UE5 World Partition: tech-seitig machbar, asset-seitig teuer)
- "Jeder Quadratmeter handplatziert" (Art-Budget ist der Flaschenhals)
- Real-Time Combat mit Skill-Ceiling (Programmer-Budget ist der Flaschenhals)

Darius' Dokument macht keine Budget-Aussagen — das ist auch nicht sein Job, das steht in GDD-06. Aber: Die Saeulen implizieren Budgets, die GDD-06 nicht abdeckt. Das muss in V2 harmonisiert werden.

### 5. Was ist richtig gut

Das will ich auch sagen, weil es stimmt:
- Der Elevator Pitch ist praezise und verkaufbar. "Kein Spiel ueber Auserwaehlte" — das ist ein klares Differenzierungsmerkmal.
- Die Validierungstests pro Saeule sind exzellent. Jede Saeule hat ein konkretes Erfolgskriterium. Das hilft bei jeder Designentscheidung downstream.
- Der Referenzrahmen ist sauber getrennt in "Lernen von" und "Anders als". Das schafft Klarheit fuer das ganze Team.
- Die Spielerfahrungs-Section (1h / 10h / 40h) ist genau das, was Nami fuer GDD-03 braucht, und es ist konsistent mit dem, was sie geschrieben hat.
- Die Monetarisierung ist CD-konform und realistisch.

### 6. ROADMAP-Update

Stand Donnerstag Tag 4:
- Peer-Reviews laufen planmaessig
- Mein Review von GDD-01 ist das erste fertige Ergebnis heute
- Andere Reviews: Emre+Nami, Darius+Leo, Vera+Tobi — Status muss ich im Meeting abfragen
- Roadmap-Aktualisierung: "Stand" auf Tag 4 setzen, Peer-Review-Status eintragen, naechste Schritte klar machen
