# Schattenfieber als Gameplay-System — Vergleichsanalyse und Konzeptentwurf

**Autor:** Darius Engel, Game Director
**Datum:** Tag 1 (Montag), Szene 5 — WORK
**Typ:** Recherche & Konzeption
**Status:** V0 (Arbeitsversion, Nachmittagsblock)

---

## 1. Vergleichsanalyse: Infektions- und Transformationsmechaniken

### 1.1 Methodik

Ich analysiere fuenf Referenzsysteme entlang von vier Kriterien:

| Kriterium | Beschreibung |
|-----------|-------------|
| **Spektrum** | Gibt es Abstufungen oder ist es binaer? |
| **Anreiz** | Hat der Spieler einen Grund, die Transformation zu WOLLEN? |
| **Spielbarkeit** | Kann man das Spiel auf jeder Stufe sinnvoll weiterspielen? |
| **Integration** | Ist die Transformation Teil des Kernspiels oder ein Overlay? |

---

### 1.2 Vampirismus — Skyrim (Sanguinare Vampiris / Vampire Lord)

**Mechanik:** Zufaellige Infektion durch Vampir-Kampf. 3 Tage Inkubation. 4 Stufen, eskalieren automatisch (24h ohne Blut = naechste Stufe). Stufe 4 = NPC-Aggression. Vampire Lord (Dawnguard DLC) = Ueberform mit eigener Skill-Leiste.

| Kriterium | Bewertung | Kommentar |
|-----------|-----------|-----------|
| Spektrum | Mittel | 4 Stufen existieren, aber nur Stufe 1 und Vampire Lord sind spielbar. Stufe 2-3 sind Durchgangsraum. |
| Anreiz | Schwach-Mittel | Vampire Lord ist stark, aber Basis-Vampirismus hat kaum Vorteile, die das Risiko rechtfertigen. |
| Spielbarkeit | Schlecht | Stufe 4 unterbricht das Spiel (NPC-Aggression). Heilung ist trivial — also kein echtes Commitment. |
| Integration | Schwach | Vampirismus existiert NEBEN dem Hauptspiel. Es veraendert nicht, wie man spielt, nur was man darf. |

**Takeaway fuer RELICS:** Stufensystem ja, aber jede Stufe muss eine spielbare Nische sein. KEINE Stufe darf das Spiel unterbrechen. Und die Nutzung muss ein bewusstes Commitment sein, nicht trivial umkehrbar.

---

### 1.3 Vampirismus — Vampire: The Masquerade – Bloodlines

**Mechanik:** Vampir-Sein ist die Praemisse, nicht die Option. Humanity-Meter (1-10, Start bei 7) sinkt durch Mord. Niedrig = Frenzy-Risiko (kurzer Kontrollverlust, automatische Aggression). Blood Points als Ressource fuer Disziplinen (Clan-spezifische Faehigkeiten). Blut beschaffen = aktives Gameplay (NPCs beissen, Ratten, Blutbeutel).

| Kriterium | Bewertung | Kommentar |
|-----------|-----------|-----------|
| Spektrum | Gut | Humanity ist ein echtes Spektrum. Jeder Punkt zaehlt. |
| Anreiz | Stark | Disziplinen sind TRANSFORMATIV — sie veraendern, wie man spielt. Nicht nur Zahlenwerte. |
| Spielbarkeit | Gut | Man kann bei jeder Humanity-Stufe spielen. Niedriger = haerter, aber nicht unmoeglich. |
| Integration | Exzellent | Vampirismus IST das Spiel. Blut-Beschaffung, Humanity-Management, Disziplinen — alles ist miteinander verwoben. |

**Takeaway fuer RELICS:** Goldstandard fuer Integration. Das Schattenfieber sollte wie Bloodlines' Vampirismus funktionieren — es IST Teil des Kernspiels, nicht optional. Aber: Im Gegensatz zu Bloodlines muss RELICS auch einen nicht-infizierten Pfad bieten, der vollwertig spielbar ist. Sonst funktioniert die Wahlfreiheit nicht.

---

### 1.4 Hollowing — Dark Souls (Serie)

**Mechanik:** DS1: Tod = Hollow (menschliche Form verloren, kein Coop). DS2: Jeder Tod = -5% max HP (bis -50%). Human Effigy stellt wieder her. DS3: Hollowing als versteckter Wert, steigt mit Tod bei bestimmter Questline, kosmetisch + einige Quest-Effekte.

| Kriterium | Bewertung | Kommentar |
|-----------|-----------|-----------|
| Spektrum | Gemischt | DS1: Binaer. DS2: Echtes Spektrum (5%-Schritte). DS3: Fast irrelevant. |
| Anreiz | Schlecht | Hollowing hat KEINE Vorteile. Es ist nur Bestrafung. Warum sollte der Spieler es wollen? |
| Spielbarkeit | Mittel | DS2 ist am haertesten — 50% HP-Verlust ist brutal, aber spielbar. DS1/3 kaum spuerbar. |
| Integration | Thematisch stark, mechanisch schwach | Hollowing ist narrativ zentral, aber mechanisch kaum relevant. Verschwendetes Potenzial. |

**Takeaway fuer RELICS:** Hollowing ist das Negativbeispiel. Es beweist: Transformation durch REINE Bestrafung funktioniert nicht als System. Es muss einen GRUND geben, die Transformation zu akzeptieren. Thematische Integration allein reicht nicht — die Mechanik muss mitziehen.

---

### 1.5 Beasthood / Insight — Bloodborne

**Mechanik:** Zwei gegenlaeufige Achsen. Beasthood = temporaerer Kampf-Buff (mehr physischer Schaden, weniger Verteidigung). Aktiviert durch Beast Blood Pellets oder Beast Claw Waffe. Insight = permanente Wahrnehmung (gesammelt durch Boss-Entdeckung, Madman's Knowledge). Mehr Insight = neue Feinde sichtbar, veraenderte Musik, weniger Frenzy-Resistenz, weniger Beasthood-Potential.

| Kriterium | Bewertung | Kommentar |
|-----------|-----------|-----------|
| Spektrum | Gut (Insight) / Schwach (Beasthood) | Insight ist ein echtes Spektrum mit mehreren Schwellen. Beasthood ist ein temporaerer Buff. |
| Anreiz | Gut | Beide Seiten haben echte Vorteile. Insight zeigt neue Inhalte. Beasthood gibt Kampfkraft. |
| Spielbarkeit | Gut | Kein Zustand blockiert das Spiel. Insight veraendert die Welt, aber man kann immer weiterspielen. |
| Integration | Mittel | Insight ist atmosphaerisch brillant, aber mechanisch unterkomplex. Beasthood ist kaum mehr als ein Buff-Item. |

**Takeaway fuer RELICS:** Bloodbornes Insight ist die staerkste Einzelidee in dieser Analyse. Die Welt VERAENDERT SICH durch deinen Zustand — das ist die Art von Feedback, die das Schattenfieber braucht. Ein infizierter Spieler sieht, hoert, erlebt eine ANDERE Welt als ein reiner. Das ist narrativ UND mechanisch stark.

---

### 1.6 Chaos-Corruption — Warhammer (Total War, Darktide, Fantasy-Universum)

**Mechanik:** Regional und/oder persoenlich. In Total War: Warhammer breitet sich Corruption auf der Weltkarte aus (Unruhen, Attrition, veraenderte Feinde). Persoenlich: Chaos-Marks als permanente Transformation (Nurgle = Resilienz, Tzeentch = Manipulation, Khorne = Kampf, Slaanesh = Verfuehrung). Unumkehrbar ab gewissem Punkt.

| Kriterium | Bewertung | Kommentar |
|-----------|-----------|-----------|
| Spektrum | Gut | Corruption-Stufen mit klaren Schwellen. Chaos-Marks als Spezialisierung innerhalb der Corruption. |
| Anreiz | Stark | Chaos-Marks geben maechtige, thematische Vorteile. Jeder Gott bietet einen anderen Spielstil. |
| Spielbarkeit | Mittel | Strategiespiel — persoenliche Identifikation fehlt. Aber die Systeme sind gut designt. |
| Integration | Gut (im Strategiekontext) | Corruption ist Teil der Kampagnenmechanik, nicht aufgesetzt. |

**Takeaway fuer RELICS:** Die Idee von SPEZIALISIERUNGEN innerhalb der Infektion ist stark. Was, wenn das Schattenfieber nicht einen linearen Pfad hat, sondern sich ab einer bestimmten Stufe VERZWEIGT? Verschiedene Manifestationen, verschiedene Faehigkeiten, verschiedene Kosten. Das waere eine zusaetzliche Build-Diversity-Schicht.

---

## 2. Synthese: Fuenf Design-Prinzipien fuer das Schattenfieber

| # | Prinzip | Aus Referenz gelernt |
|---|---------|---------------------|
| **S1** | **Spektrum, nicht Schalter.** Fuenf Stufen, jede spuerbar anders. | Skyrim-Fehler (binaer), DS2-Erfolg (graduell) |
| **S2** | **Nutzen MUSS attraktiv sein.** Jede Stufe bietet transformative Faehigkeiten, nicht nur Zahlenwerte. | DS-Fehler (nur Bestrafung), Bloodlines-Erfolg (Disziplinen) |
| **S3** | **Kosten veraendern, blockieren nicht.** Keine Stufe unterbricht das Spiel. Kosten sind sozial und koerperlich, nicht "Game Over". | Skyrim-Fehler (NPC-Aggression Stufe 4), Bloodborne-Erfolg (Insight) |
| **S4** | **Die Welt reagiert auf deinen Zustand.** NPCs, Fraktionen, die Umgebung selbst veraendern sich. | Bloodborne-Insight (Wahrnehmungswandel), Bloodlines (soziale Konsequenzen) |
| **S5** | **Integration ins Kernsystem.** Das Schattenfieber ist Teil des Nervensystem-Levelings, kein separates Overlay. | Bloodlines (Vampirismus = das Spiel), Bloodborne-Fehler (Beasthood = nur Buff) |

---

## 3. Konzeptentwurf: Schattenfieber als Gameplay-System

### 3.1 Grundstruktur

Das Schattenfieber ist ein **permanenter Infektionswert von 0 bis 100**, aufgeteilt in fuenf Stufen. Es erweitert das Nervensystem-Leveling um einen **vierten Ast** (Schattennervensystem), der mit den drei bestehenden Aesten um Ressourcen konkurriert.

```
NERVENSYSTEM-LEVELING (4 Aeste)

[Cardio/Atmung]     → Ausdauer, Regeneration, Bewegung
[Muskel/Skelett]    → Staerke, Resistenz, Waffenhandhabung
[Lymph/Immun]       → Alchemie-Effizienz, Gift-Resistenz, Heilung
[Schatten]          → Schattensinne, Schattenfieber-Faehigkeiten, Wahrnehmung
                       (NUR zugaenglich ab Infektionsstufe 1+)

INFEKTIONSWERT (0–100) bestimmt:
→ Welche Schatten-Faehigkeiten verfuegbar sind
→ Wie stark die Interferenz mit den drei normalen Aesten ist
→ Wie die Welt auf den Spieler reagiert
```

### 3.2 Fuenf Stufen im Detail

#### Stufe 0 — Rein (Infektionswert 0–10)

| Aspekt | Beschreibung |
|--------|-------------|
| **Koerperlich** | Keine sichtbaren Veraenderungen. |
| **Faehigkeiten** | Kein Zugang zum Schatten-Ast. Alle drei normalen Aeste auf 100%. |
| **Sozial** | NPCs behandeln dich normal. Alle Fraktionen offen. |
| **Spieler-Fantasie** | "Ich bin ein normaler Mensch in einer gefaehrlichen Welt. Meine Staerke kommt aus Training und Ausruestung." |

**Game Design Note:** Stufe 0 muss ein VOLLWERTIGER Spielpfad sein. Kein "Du verpasst was, wenn du dich nicht infizierst." Der reine Spieler hat den Vorteil vollstaendiger Nervensystem-Effizienz und uneingeschraenkter sozialer Interaktion. Das ist stark genug.

---

#### Stufe 1 — Gezeichnet (Infektionswert 11–25)

| Aspekt | Beschreibung |
|--------|-------------|
| **Koerperlich** | Subtil: leicht verfaerbte Adern unter der Haut, Augen reflektieren Licht in Dunkelheit (wie Tieraugen). Nur bei genauem Hinsehen erkennbar. |
| **Faehigkeiten** | **Schattensinne** (passiv): Versteckte Objekte sichtbar (vergiftete Speisen, geheime Durchgaenge, Fallen). Emotionszustaende von NPCs als Aura wahrnehmbar. |
| **Nervensystem-Interferenz** | Lymph-Ast: -5% Effizienz. Leicht erhoehte Anfaelligkeit fuer Gifte und Krankheiten. |
| **Sozial** | Aufmerksame NPCs werden misstrauisch. Der Orden erhaelt Verdachts-Hinweise. Heiler erkennen die Infektion. |
| **Spieler-Fantasie** | "Ich sehe Dinge, die andere nicht sehen. Es ist nuetzlich — aber es hat mich veraendert." |

**Game Design Note:** Stufe 1 ist der "Einstiegspunkt". Der Spieler bekommt einen echten Vorteil (Exploration wird reicher), zahlt aber fast nichts. Das soll neugierig machen auf mehr — OHNE zu zwingen.

---

#### Stufe 2 — Infiziert (Infektionswert 26–50)

| Aspekt | Beschreibung |
|--------|-------------|
| **Koerperlich** | Deutlich: Dunkle Adern sichtbar an Haenden und Hals. Augen leuchten bei Aktivierung der Faehigkeiten. Haut wird blasser. Nicht mehr versteckbar. |
| **Faehigkeiten** | **Schattensinne** (erweitert) + **Aktive Faehigkeiten**: Schattenreflex (verlaengertes Parry-Window im Kampf), Schatten-Schritt (kurzer Dash durch Schatten, ~3m), Schmerzunterdrueckung (temporaer Schadensreduktion, danach verzoegerter Schaden). |
| **Nervensystem-Interferenz** | Lymph: -15%. Cardio: -10%. Ausdauer regeneriert langsamer. Alchemie-Tränke wirken schwaecher. |
| **Sozial** | Spaltung: Manche NPCs fuerchten dich, manche suchen deine Hilfe (andere Infizierte, verzweifelte Auftraggeber). Krone wird distanziert. Orden beginnt aktive Ueberwachung. Gilden bleiben pragmatisch — du bist nuetzlich. |
| **Spieler-Fantasie** | "Ich bin staerker als jeder normale Mensch. Aber jeder sieht, dass ich anders bin. Manche brauchen mich, manche jagen mich." |

**Game Design Note:** Stufe 2 ist der Wendepunkt. Ab hier ist die Infektion SICHTBAR — der Spieler kann sie nicht mehr verstecken. Das veraendert das Spiel fundamental: neue Quests werden verfuegbar, alte fallen weg. NICHT als Strafe, sondern als ANDERE Erfahrung.

---

#### Stufe 3 — Verwandelt (Infektionswert 51–75)

| Aspekt | Beschreibung |
|--------|-------------|
| **Koerperlich** | Stark: Schattenadern als sichtbares Netzwerk unter der Haut. Unnatuerliche Bewegungsmuster (zu schnell, zu fliessend). Stimme hat ein Echo. Pupillen veraendern sich. |
| **Faehigkeiten** | Alle vorherigen + **Fortgeschrittene Faehigkeiten**: Schattenprojektion (eine Schatten-Kopie fuer ~10 Sekunden als Ablenkung), Fieber-Puls (AoE-Schockwelle, betaeubt Feinde kurz, kostet HP), Tiefensicht (durch duenne Waende sehen, Schatzsuche). |
| **Nervensystem-Interferenz** | Alle drei Aeste: -25%. Muskel kompensiert teilweise durch Schatten-Kraft (+15% roher Nahkampfschaden). Netto: Spezialisierter, aber fragiler. |
| **Sozial** | Krone: Aktive Feindschaft (Kopfgeld). Orden: Jagd-Prioritaet (eigener Questbogen). Gilden: Noch tolerant, aber nur solange du nuetzlich bist. Infizierte NPCs erkennen dich als "einen von ihnen" — neue Fraktion? Neue Quests? |
| **Spieler-Fantasie** | "Ich bin kein Mensch mehr. Nicht ganz. Aber was ich geworden bin, ist maechtig — und die Maechtigen fuerchten mich." |

**Game Design Note:** Ab Stufe 3 beginnt das Spiel sich FUNDAMENTAL zu veraendern. Zwei Fraktionen werden feindlich — das schliesst Questlines, aber oeffnet NEUE (Untergrundbewegung der Infizierten, Gilden-Sondermissionen). Der Spieler, der Stufe 3 erreicht, spielt ein ANDERES Spiel als der auf Stufe 0. Beide Spiele muessen gleich gut sein.

---

#### Stufe 4 — Entfesselt (Infektionswert 76–100)

| Aspekt | Beschreibung |
|--------|-------------|
| **Koerperlich** | Fundamental: Die Grenze zwischen Mensch und Schattenfieber-Wesen verschwimmt. Temporaere koerperliche Transformationen moeglich (Gliedmassen aus Schatten, Schattenpanzer). Im Ruhezustand: unruhige Aura, Tiere fliehen, Pflanzen welken in unmittelbarer Naehe. |
| **Faehigkeiten** | Alle vorherigen (verstaerkt) + **Apex-Faehigkeiten**: Schattenform (volle Verwandlung fuer ~15 Sekunden, enorme Kampfkraft, danach Erschoepfung), Fieber-Ruf (andere Infizierte in der Naehe werden verstaerkt — Coop-Synergie), Schattenwurzeln (Gebiet markieren, Feinde darin verlangsamt und sichtbar). |
| **Nervensystem-Interferenz** | Alle drei Aeste: -40 bis -50%. Schatten-Ast kompensiert massiv im Kampf, aber Regeneration, Alchemie und Ausdauer sind am Boden. Abhaengigkeit von Schattenfieber-Faehigkeiten ist total. |
| **Kontrollverlust** | NEU: Fieber-Episoden. In Stresssituationen (niedriges HP, bestimmte Story-Trigger) kann der Spieler kurzzeitig die Kontrolle verlieren. Kamera wechselt, der Charakter handelt autonom (~5 Sekunden, skriptgesteuert). Danach: Konsequenzen (verletzte NPCs, zerbrochene Allianzen). |
| **Sozial** | Die meisten NPCs fliehen oder greifen an. Nur Infizierte, bestimmte Gilden-Kontakte und eine moegliche "Schattenfieber-Fraktion" interagieren noch. Haendler-Zugang stark eingeschraenkt (Schwarzmarkt). |
| **Spieler-Fantasie** | "Ich bin das Monster. Die Frage ist nicht mehr, ob ich die Macht habe — sondern ob ich noch ICH bin." |

**Game Design Note:** Stufe 4 ist das "Hard Mode"-Aequivalent — nicht durch Zahlenwerte, sondern durch Spielwelt-Reaktion. Kontrollverlust-Episoden muessen SORGFAELTIG designt sein: kurz (~5 Sekunden), skriptgesteuert (nicht zufaellig), mit klaren Vorwarnzeichen (visuelle/akustische Cues). Der Spieler soll SPANNUNG spueren, nicht Frustration. Vergleich: Scarecrow-Sequenzen in Batman: Arkham Asylum — der Spieler verliert kurz die Kontrolle, aber es fuehlt sich wie ein Event an, nicht wie ein Bug.

---

### 3.3 Infektionsfortschritt

**Wie steigt der Infektionswert?**

| Quelle | Typ | Beispiele |
|--------|-----|-----------|
| **Umgebungsexposition** | Passiv | Schattenfieber-verseuchte Orte (Katakomben, alte Ritualstaetten). Kampf gegen Infizierte Gegner. Konsum bestimmter Substanzen. |
| **Bewusste Nutzung** | Aktiv | Schattenfieber-Faehigkeiten einsetzen erhoeht den Wert leicht (~0.5-1 Punkt pro Einsatz). Alchemie-Praeparate, die den Schatten-Ast boosten. Bestimmte Quest-Entscheidungen. |
| **Story-Events** | Skriptgesteuert | Schluesselmomente in der Hauptquest. Boss-Begegnungen mit Infizierten. Rituale. |

**Wie senkt man den Infektionswert?**

| Methode | Effekt | Einschraenkung |
|---------|--------|---------------|
| **Alchemie-Suppressiva** | -3 bis -5 Punkte | Teuer, seltene Zutaten. Wirkung nimmt bei hoeherem Wert ab. |
| **Orden-Reinigung** | -10 bis -15 Punkte | NUR bei Orden-Allianz verfuegbar. Schmerzhaft (temporaerer Stat-Malus). Ab Stufe 3 verweigert der Orden die Behandlung. |
| **Ruhe und Isolation** | -1 Punkt pro Tag | Langsam, aber kostenlos. Funktioniert nur bis Stufe 2. |

**HARD CAP:** Der Infektionswert kann NIEMALS unter die hoechste je erreichte Stufen-Schwelle fallen.
- Warst du je auf Stufe 1 (11+)? Minimum ist 11.
- Warst du je auf Stufe 2 (26+)? Minimum ist 26.
- Etc.

Die Infektion vergisst nicht. Das ist die zentrale Design-Entscheidung.

---

### 3.4 Interaktion mit dem Nervensystem-Leveling

```
LEVELING-PUNKTE (begrenzt pro Level-Up)

Verteilung auf vier Aeste:

[Cardio]  ████████░░  → Ausdauer, Sprint, Schwimmen
[Muskel]  ██████░░░░  → Schaden, Block, Tragen
[Lymph]   ████░░░░░░  → Alchemie, Resistenz, Heilung
[Schatten] ██░░░░░░░░  → Schattensinne, Faehigkeiten (NUR ab Stufe 1+)

INTERFERENZ durch Infektionswert:
Stufe 0: Kein Schatten-Ast. Alle drei Aeste 100%.
Stufe 1: Schatten verfuegbar. Lymph -5%.
Stufe 2: Schatten erweitert. Lymph -15%, Cardio -10%.
Stufe 3: Schatten fortgeschritten. Alle drei -25%. Kompensation: +15% Melee-Schaden.
Stufe 4: Schatten Apex. Alle drei -40-50%. Kompensation: Massive Schatten-Faehigkeiten.
```

**Die Kernspannung:** Leveling-Punkte im Schatten-Ast investieren LOHNT sich nur, wenn der Infektionswert hoch genug ist. Aber ein hoher Infektionswert SCHWAECHT die anderen Aeste. Der Spieler muss entscheiden: Breit aufstellen oder spezialisieren?

**Emergente Builds:**

| Build | Infektionsstufe | Schwerpunkte | Spielstil |
|-------|----------------|-------------|-----------|
| **Reiner Krieger** | 0 | Muskel + Cardio | Klassisch: schwere Waffen, hohe Ausdauer, volles Parry-System. Kein Zugang zu Schattensinnen. |
| **Alchemist** | 0-1 | Lymph + Cardio | Trank-fokussiert: Gifte, Heiltranke, Buff-Oele. Leichte Schattensinne fuer Zutaten-Erkennung. |
| **Schattenspaether** | 1-2 | Schatten + Cardio | Exploration-fokussiert: Schattensinne fuer Geheimnisse, Schatten-Schritt fuer Stealth. Fragil, aber allwissend. |
| **Hybrid-Kaempfer** | 2-3 | Muskel + Schatten | Risk/Reward: Schattenreflex und Fieber-Puls im Kampf. Weniger Ausdauer, aber explosive Spitzen. |
| **Schattenbestie** | 3-4 | Schatten (voll) | Glass Cannon: Enorme Schattenfieber-Macht, minimale konventionelle Stats. Sozialer Aussenseiter. |

---

### 3.5 Spieler-Fantasie: Warum macht das Spass?

| Stufe | Was der Spieler FUEHLT | Vergleich |
|-------|----------------------|-----------|
| 0 | "Ich bin der Underdog. Alles, was ich habe, habe ich mir verdient." | Gothic 2: Null-zu-Held |
| 1 | "Ich habe einen Vorteil, den niemand sonst hat. Ich weiss Dinge." | Bloodborne: Insight |
| 2 | "Ich werde maechtig — aber die Welt sieht mich anders. Spannend." | Dishonored: Chaos beginnt |
| 3 | "Ich bin etwas Besonderes. Gefaehrlich. Die Regeln gelten nicht mehr fuer mich." | VtM: Low Humanity Vampire |
| 4 | "Ich bin ein Monster. Und vielleicht ist das okay." | Bloodborne: Beasthood-Fantasie (voll realisiert) |

Die BESTE Version dieses Systems funktioniert so: **Jeder Spieler findet seine Stufe.** Der vorsichtige Spieler bleibt bei 0-1. Der neugierige testet 2. Der risikofreudige geht auf 3-4. Keiner wird bestraft, alle bekommen eine ANDERE, gleich wertvolle Erfahrung.

---

## 4. Offene Fragen fuer das Team

| # | Frage | Fuer wen | Prioritaet |
|---|-------|----------|-----------|
| 1 | Wie interagiert Schattenfieber mit dem Tiervolk? Sind Tiermenschen immun? Anders infiziert? Natuerlicher Zustand? | Emre (Lore) | Hoch |
| 2 | Welche narrativen Konsequenzen hat jede Stufe? Dialogvarianten, Quest-Verzweigungen, NPC-Reaktionen? | Nami (Narrativ) | Hoch |
| 3 | Kontrollverlust auf Stufe 4 — wie visualisiert man das, ohne es frustrierend zu machen? Kamera-Effekte, Post-Processing, Sound? | Vera (Art) + Tobi (Tech) | Mittel |
| 4 | Kann das Schattenfieber sich INNERHALB der Stufen spezialisieren? (Verschiedene Manifestationen, aehnlich Warhammer Chaos-Marks?) | Emre (Lore) + Darius (Design, ich) | Mittel — V2-Feature |
| 5 | Balancing: Ist Stufe 0 wirklich gleichwertig zu Stufe 3+? Oder braucht Stufe 0 eigene exklusive Vorteile? | Leo (Balancing) | Hoch |
| 6 | Alchemie als Schnittstelle: Suppressiva, Booster, Stabilisatoren — wie komplex wird das Crafting? | Darius (Design, ich) | Mittel — GDD 02 |
| 7 | Fraktions-Interaktion: Ab welcher Stufe schliesst welche Fraktion den Spieler aus? Wie genau? | Nami + Emre | Hoch |

---

## 5. Naechste Schritte

- Ergebnisse im Review (Szene 6) vorstellen — Feedback einholen
- Morgen (Dienstag, Recherche-Tag): Combat-Skill-Ceiling analysieren, Schattenfieber-Faehigkeiten im Detail skizzieren
- Ab Mittwoch: V1 der Kernmechaniken-Sektion (GDD-02) beginnen — Schattenfieber als Core System einbauen
- Bilaterales Gespraech mit Emre: Schattenfieber-Lore und Tiervolk-Verbindung
- Bilaterales Gespraech mit Leo: Balancing-Framework fuer Stufe-0-vs-Stufe-4-Gleichwertigkeit

---

*Darius Engel, Game Design Corner, 14:00–15:45*
