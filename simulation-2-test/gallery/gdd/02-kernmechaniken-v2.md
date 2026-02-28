---
dokument: GDD-02
titel: Kernmechaniken
version: 2
autor: Darius Engel
status: Entwurf
datum: "Tag 6, Montag"
querverweise: ["GDD-01", "GDD-03", "GDD-05", "GDD-06", "WBB-01"]
---

# GDD-02: Kernmechaniken

**Autor:** Darius Engel, Game Director
**QA:** Leo Brandt (Spielermarkt & Community)
**Narrativ-Sync:** Nami Osei (Erzählkonzept)
**Version:** V2 (Tag 6, Montag — Verlängerungstag)
**Status:** Entwurf
**Änderungslog:**
- V1/V0.5 (Tag 2-3): Kapitelstruktur, Kernpunkte, QA-Bedingungen, Stufen-Mapping
- V0.5.1 (Tag 5): Ymir → Emer (Leo Fischer, QA)
- V2 (Tag 6): Namenssystem durchgehend (Emer, Große Flechtung), Stufengrenzen auf CD-Tabelle (Rauschen 1-40, Risse 41-75, Schwelle 76-100), Waffenklassen für Vertical Slice festgezurrt, Suchtmechanik bei Alchemie-Buffs, Nervensystem-Äste mit kosmologischem Einzeiler, Kontrollverlust = narrativ, Schatten-Ast als eigener Abschnitt, Trainer als Fraktions-Erzähler, Maret als optionaler Kompanion

**Querverweise:** `GDD-01` (Spielübersicht V2), `GDD-03` (Erzählkonzept), `GDD-05` (Designsprache), `GDD-06` (Technik), `WBB-01` (Mythos V2)

---

## 1. Combat-System

### 1.1 Grundphilosophie
- Real-time Action, Melee-fokussiert, gewichtig
- KEIN Difficulty Slider — die Welt bestimmt die Schwierigkeit (Gothic-Prinzip)
- Skill-Ceiling als Spektrum (CD-bestätigt): Einstieg intuitiv, Mastery belohnend — nie erzwungen
- Jeder Kampf soll sich BEDEUTSAM anfühlen — keine Trash-Mobs, kein Grind
- Spieler-Fantasie: "Ich habe diesen Kampf gewonnen, weil ich besser geworden bin — nicht weil ich Level 50 bin."

**Skill-Ceiling-Spektrum (Detail):**
Das System muss auf BEIDEN Enden des Spektrums funktionieren. Ein Spieler, der nur Basisaktionen nutzt, soll jede Begegnung bestehen können (mit Vorbereitung und Geduld). Ein Spieler, der Cancel-Windows und Setup-Plays beherrscht, soll sich belohnt fühlen (schnellere Kills, elegantere Lösungen, optionale Herausforderungen). Kein Spieler soll das Gefühl haben, er müsste Mastery-Techniken lernen, um weiterzukommen. Aber jeder Spieler soll sehen KÖNNEN, was möglich wäre.

### 1.2 Kampfschichten (drei Ebenen)

#### Ebene 1 — Basis (sofort zugänglich)
- Leichter Angriff, schwerer Angriff, Block, Ausweichen
- Ausdauer-Management: Jede Aktion kostet Ausdauer, Übertreiben wird bestraft
- Ziel-Lock-On optional (nicht erzwungen)
- Jeder Spieler kann sofort kämpfen — Gothic-Gewicht, Skyrim-Zugänglichkeit

#### Ebene 2 — Fortgeschritten (erlernt durch Trainer + Übung)
- Parade/Riposte: Präzises Timing-Fenster, belohnt mit Gegenangriff
- Positionierung: Flankenangriffe, Rückenattacken, Höhenvorteile (Vertikalität!)
- Waffenspezifische Kombos: Abhängig von Waffenklasse, erlernt bei Trainern
- Umgebungsinteraktion: Objekte treten/werfen, Engstellen nutzen, Gegner in Fallen locken

#### Ebene 3 — Mastery (belohnend, nie erzwungen)
- Cancel-Windows: Fortgeschrittene Spieler können Animationen unterbrechen für Feints
- Setup-Plays: Alchemie-Vorbereitung (Öle, Gifte) + Positionierung + Timing als koordinierte Strategie
- Schattenfieber-Combat-Integration: Schattenreflex (erweitertes Parry-Window), Fieber-Puls (AoE, kostet HP)
- Perfekte Paraden: Winzigstes Timing-Fenster, maximal belohnend (Spezial-Riposte)

### 1.3 Waffenklassen (Vertical Slice — festgezurrt)

> V2-Änderung: Die offene Frage aus V1 ("Waffenklassen-Anzahl für den Vertical Slice?") ist entschieden. Vier Nahkampfklassen + Bogen. Armbrüste und Schilde fallen in dieser Iteration nicht raus, sondern werden als Erweiterungspool für Post-Slice behandelt.

**Im Vertical Slice spielbar:**

| Klasse | Typ | Spielgefühl | Trainer-Fraktion |
|--------|-----|-------------|------------------|
| **Schwert (Einhand)** | Nahkampf | Allrounder, mittlere Geschwindigkeit, ausgewogenes Moveset. Einstiegswaffe. | Krone (Militärausbildung) |
| **Zweihandschwert** | Nahkampf | Langsam, hoher Schaden, Reichweite. Kontrolliert den Raum. Bestraft Fehler härter. | Krone (Elitetruppen) |
| **Dolche/Kurzwaffen** | Nahkampf | Schnell, niedriger Einzelschaden, Combo-orientiert. Giftapplikation als USP. Erfordert Nähe. | Gilden (Schwarzmarkt-Trainer), Tiervolk |
| **Axt (Einhand)** | Nahkampf | Mittlere Geschwindigkeit, hoher Stagger-Wert. Schildbrecher. Weniger Combos, mehr Einzeltreffer-Wucht. | Orden (pragmatische Kampfschulung) |
| **Bogen** | Ranged | Unterstützungswaffe, Haltungsschaden, kein Hauptwaffen-Fokus. Taktische Eröffnung vor Nahkampf. | Gilden (Jagdtradition) |

**Erweiterungspool (Post-Slice):**
- Äxte (Zweihand), Hämmer, Armbrüste, Schilde als Offhand-Option
- Diese Klassen sind designt, aber nicht für den Vertical Slice priorisiert — sie würden den Scope sprengen, ohne die Kernfantasie zu erweitern

**Waffen und Fraktionen:**
Jede Fraktion hat exklusive Trainer für bestimmte Waffenstile und fortgeschrittene Techniken. Das Einhandschwert ist überall als Basis verfügbar — aber der Krone-Schwertmeister lehrt andere Kombos als der Gilden-Fechtlehrer. Waffenwahl IST Fraktionsaussage.

### 1.4 Feinddesign-Prinzipien
- Feinde haben EIGENE Movesets, nicht nur skalierte Spieler-Angriffe
- Feindtypen definiert durch Verhalten, nicht nur durch Werte: Aggressive, Defensive, Taktiker, Infizierte
- Infizierte Feinde nutzen Schattenfieber-Fähigkeiten — Vorschau für den Spieler ("Das könnte ICH auch")
- Keine Level-Skalierung: Gebiete haben feste Feindstärke. Manche Gegner sind zu früh zu stark. Komm später wieder.
- **Maret als Spiegel (V2):** Die optionale Kompanionin Maret kämpft mit Schattenfieber-Fähigkeiten, die der Spieler noch nicht oder nie haben wird. Sie zeigt, was möglich ist — und was es kostet. (→ Abschnitt 2.10)

### 1.5 Tod und Konsequenz
- Tod ist ein Rückschlag, kein Game Over — Checkpoint-System mit fairen Abständen
- Keine Erfahrungspunkt-Strafe bei Tod
- **Tod beeinflusst den Infektionswert NICHT** (CD-bestätigt). Begründung: Tod ist bereits Strafe genug. Infektionsanstieg bei Tod würde Risk/Reward des Schattenfieber-Systems untergraben und die bewusste Entscheidung zur Nutzung verwischen.
- Konsequenz durch WELT-Reaktion: Bestimmte Situationen verändern sich bei erneutem Versuch (NPC-Kommentare, veränderte Wachpositionen)

---

## 2. Schattenfieber-System

> **QA-Einschätzung (Leo):** 40% des QA-Aufwands entfällt auf das Schattenfieber-System. Es ist gleichzeitig größter USP und größtes Risiko. Die folgenden drei nicht-verhandelbaren Bedingungen sind das Ergebnis von Leos Community- und Marktanalyse.

### 2.1 Drei Nicht-Verhandelbare Bedingungen (QA-validiert)

Diese drei Bedingungen haben Veto-Recht über jede Schattenfieber-Designentscheidung. Wenn ein Feature eine dieser Bedingungen verletzt, wird es geändert oder gestrichen — ohne Ausnahme.

**Bedingung 1: TRANSPARENZ VOR INFEKTION**
- Der Spieler muss JEDERZEIT wissen, welche Aktion seinen Infektionswert erhöhen kann und um wie viel
- Keine versteckten Infektionsquellen. Keine "Überraschung, du bist jetzt infiziert"
- UI-Feedback: Klarer Indikator wenn der Spieler sich in einer infektionserhöhenden Situation befindet (visuell, auditiv, haptisch)
- Infektionserhöhende Aktionen müssen eine explizite Bestätigung haben ODER einen klar wahrnehmbaren Moment der bewussten Entscheidung bieten
- **Goldstandard**: Bloodborne Insight — der Spieler sammelt Insight durch spezifische, erkennbare Aktionen (Bosse sehen, Madman's Knowledge nutzen). Es gibt keine versehentliche Insight-Erhöhung
- **Anti-Referenz**: Skyrim Vampirismus — Infektion passiert im Kampf durch einen zufälligen Statuseffekt, den Spieler oft nicht bemerken. Der häufigste Community-Complaint: "Ich wusste nicht, dass ich Vampir werde"

**Bedingung 2: SOFORTIGE POWER FANTASY NACH INFEKTION**
- Ab dem ERSTEN PUNKT Infektionswert muss der Spieler etwas Cooles können, das er vorher nicht konnte
- Kein "Stufe 1 ist nur Nachteile, die guten Sachen kommen später" — das widerspricht der Kernfantasie
- Schattensinne (Stufe 1) müssen sofort als Upgrade erlebbar sein: Verstecktes sehen, Emotionen lesen, eine ZWEITE SCHICHT der Welt wahrnehmen
- Der Spieler soll nach der ersten Infektion denken: "Das war es wert. Was kommt noch?"
- **Goldstandard**: Bloodborne — der erste Insight-Punkt zeigt sofort die Puppe im Hunter's Dream. Die Welt verändert sich. Der Spieler fühlt sich belohnt.

**Bedingung 3: KEIN VERSEHENTLICHES INFIZIEREN**
- Infektion darf NIEMALS durch Zufall, Unachtsamkeit oder unklare Mechaniken passieren
- Jeder Infektionspunkt muss auf eine BEWUSSTE SPIELERENTSCHEIDUNG zurückführbar sein
- Kampf gegen Infizierte = Infektionsrisiko? Dann muss das VOR dem Kampf klar kommuniziert werden, und der Spieler muss eine taktische Wahl haben (Distanzwaffen, Alchemie-Schutz, Umgehen)
- Story-Events, die Infektion erhöhen: Müssen als Entscheidung präsentiert werden, nicht als Cutscene-Zwang
- **Design-Test**: Wenn ein Spieler nach 20 Stunden sagt "Ich wollte Stufe 0 bleiben, aber irgendwie bin ich Stufe 2" — dann haben wir versagt

### 2.2 Systemübersicht
- Permanenter Infektionswert: 0-100
- Drei narrative Zonen mit graduellen Übergängen (CD-bestätigt, V2)
- Vierter Ast im Nervensystem-Leveling (nur ab Infektionswert 1+)
- NICHT heilbar, nur kontrollierbar (CD-bestätigt)
- Kosmologische Verankerung: Das Schattenfieber greift auf dasselbe Emer-Material zu, aus dem die Welt gebaut ist (→ WBB-01, Kap. 2+6). Es ist keine Krankheit im medizinischen Sinn — es ist eine unkontrollierte Rückverbindung zum Emer-Körper. Wer das Schattenfieber trägt, dessen eigener Körper erinnert sich daran, dass er aus dem Emer stammt.

### 2.3 Drei-Zonen-Modell (CD-bestätigt)

> V2-Änderung: Die fünf mechanischen Stufen aus V1 werden durch ein Drei-Zonen-Modell ersetzt, das Darius' Mechanik und Namis narrative Zustände vereint. Die CD-Tabelle (Tag 4, Standup) legt die Grenzen fest.

**Überblick:**

| Zone | Infektionswert | Narrativer Zustand | Kern-Fantasie |
|------|---------------|---------------------|---------------|
| **Rauschen** | 1–40 | Subtile Verschiebungen. Die Welt flüstert. | "Ich sehe, was andere nicht sehen." |
| **Risse** | 41–75 | Die Wahrnehmung bricht auf. Fragwürdige Eindrücke. | "Ich bin mächtig — aber bin ich noch ich?" |
| **Schwelle** | 76–100 | Parallel-Narrativ. Was ist echt? Halluzinations-Start. | "Das Monster — und vielleicht ist das okay." |

**Stufe 0 (Infektionswert 0): Rein**
- Volle Nervensystem-Effizienz, uneingeschränkte Sozialinteraktion
- Kein Zugang zu Schatten-Fähigkeiten — aber voller Zugang zu Alchemie, Trainer-System, allen Fraktionen
- Spieler-Fantasie: "Ich bin der Underdog, rein menschlich — und ich beweise, dass das reicht."

**Zone 1 — Rauschen (Infektionswert 1–40)**
- **Früh (1-15):** Schattensinne (passiv) — Verstecktes sichtbar, erste Emotionsauren an NPCs. Subtile Textveränderungen in Dialogen. Spieler bemerkt es vielleicht nicht sofort.
- **Mitte (16-30):** Schattensinne verstärkt. Schattenreflex (erweitertes Parry-Window). Erste sichtbare körperliche Veränderungen. Aufmerksame NPCs werden misstrauisch.
- **Spät (31-40):** Schatten-Schritt (kurze Teleportation), Schmerzunterdrückung. Übergangszone: Hinweise werden deutlicher, erste fragwürdige Wahrnehmungen. Gesprächsoptionen erscheinen, die andere nicht hören.
- **Kosten:** Lymph-Ast-Effizienz sinkt graduell (-5% bis -15%). Misstrauen bei aufmerksamen NPCs.

**Zone 2 — Risse (Infektionswert 41–75)**
- **Früh (41-55):** Schattenprojektion (Ablenkung auf Distanz). +10% Melee-Schaden. Alternative Dialoge mit Figuren, die möglicherweise anders reden als erwartet.
- **Mitte (56-65):** Fieber-Puls (AoE, kostet HP). Tiefensicht (Schatzsuche, Ressourcen-Scan). Fragwürdige Questgeber. NPCs reagieren irritiert auf Antworten, die der Spieler für normal hält.
- **Spät (66-75):** Schattenprojektion erweitert (kampffähiges Schattenbild). +15% Melee. Krone distanziert sich. Orden beginnt, den Spieler als Bedrohung einzustufen.
- **Kosten:** Alle konventionellen Äste -15% bis -25%. Sichtbar infiziert. Fraktionszugang verschiebt sich dramatisch.

**Zone 3 — Schwelle (Infektionswert 76–100)**
- **Halluzinations-Start ab Wert 76** (CD-bestätigt): Der Spieler kann nicht mehr sicher unterscheiden, welche Dialoge, NPCs und Quests "echt" sind. Das ist kein Bug — es ist die Kernfantasie dieser Zone.
- **Früh (76-85):** Schattenform (kurzzeitige Unverwundbarkeit). Fieber-Ruf (zieht infizierte Kreaturen als Verbündete an). Parallel-Narrativ beginnt: Gespräche mit Figuren, die möglicherweise nicht existieren.
- **Spät (86-100):** Schattenwurzeln (Flächenkontrolle, organische Barrieren). Kontrollverlust-Episoden (→ 2.6). Volle Doppelwahrnehmung: Daseinsebenen werden durchlässig.
- **Kosten:** Alle konventionellen Äste -40% bis -50%. Soziale Isolation. Krone und Orden sind feindlich. Kontrollverlust-Episoden.
- **Apex-Power:** Massive Kampfkraft, Fähigkeiten auf kosmologischer Ebene — der Spieler greift direkt auf Emer-Material zu.

**Übergangs-Design:**
- Zonenübergänge sind KEINE harten Schalter. Der Infektionswert bestimmt die Intensität innerhalb einer Zone graduell.
- Beispiel: Bei Wert 15 sind Schattensinne schwächer als bei Wert 38. Es gibt keinen Moment, in dem alles "anspringt".
- Rauschen intensiviert sich ab dem ersten Infektionspunkt. Risse setzen schrittweise ab ca. Wert 41 ein. Schwelle wird ab Wert 76 spürbar — und ab hier beginnen Halluzinationen.
- **QA-Relevanz (Leo)**: Der graduelle Übergang ist der Grund für den hohen QA-Aufwand. Jeder der ~100 Infektionswerte muss sich in der Spielerfahrung "richtig" anfühlen.

### 2.4 Infektionsfortschritt

**Steigerung:**
- Umgebungsexposition (verseuchte Orte, Kampf gegen Infizierte) — NUR mit vorheriger Warnung (Bedingung 1+3). Der Spieler sieht/hört/spürt, dass ein Ort verseucht ist, BEVOR er ihn betritt.
- Bewusste Nutzung (Schattenfieber-Fähigkeiten einsetzen: ~0,5–1 Punkt pro Einsatz) — jede Fähigkeitsnutzung zeigt den Infektionsanstieg im UI
- Story-Events (Schlüsselmomente, Boss-Begegnungen) — IMMER als bewusste Spielerentscheidung präsentiert, nie als Cutscene-Zwang
- Kontakt mit der Lebenden Krone (→ 2.8) — Relikt-Interaktion als hochriskante, hochbelohnende Infektionsquelle
- Tod erhöht den Infektionswert NICHT (CD-bestätigt)

**Senkung:**
- Alchemie-Suppressiva (-3 bis -5 Punkte, teuer, Wirkung nimmt bei hohem Wert ab)
- Orden-Reinigung (-10 bis -15 Punkte, nur bei Orden-Allianz, ab Zone Risse zunehmend verweigert)
- Ruhe und Isolation (-1/Tag, nur innerhalb von Rauschen)

**Hard Cap:** Infektionswert kann NIE unter die höchste je erreichte Zonenschwelle fallen. Die Infektion vergisst nicht. Wer einmal in der Zone Risse war (41+), kommt nicht mehr unter 41 zurück.

### 2.5 Kosten-Nutzen-Matrix

> Jede Zeile muss gegen Bedingung 2 (sofortige Power Fantasy) validiert werden. JEDE Zone ab Rauschen muss einen klaren, sofort erlebbaren Vorteil haben, der die Kosten aufwiegt — zumindest im Moment der Entscheidung.

| Zone | Nutzen (sofort erlebbar) | Kosten (wachsend) | Stufe-0-Äquivalent |
|------|-------------------------|-------------------|---------------------|
| Rein (0) | Volle Systemeffizienz, voller Weltzugang, vollständige Alchemie-Wirkung | Kein Zugang zu Schattenfähigkeiten, keine zweite Wahrnehmungsschicht | — |
| Rauschen (1-40) | **Schattensinne** (Exploration-Vorteil): Verstecktes sichtbar, Emotionsauren, neue Wege. Ab 16: Schattenreflex. Ab 31: Schatten-Schritt. | Lymph -5% bis -15%, Misstrauen aufmerksamer NPCs | Volle Alchemie + Nachtsicht-Tinktur als Schattensinne-Alternative |
| Risse (41-75) | **Fortgeschrittene Kampffähigkeiten**: Schattenprojektion, Fieber-Puls, +10-15% Melee, Tiefensicht | Alle Äste -15% bis -25%, sichtbar infiziert, Krone distanziert, Orden feindselig | Meister-Alchemie + Setup-Plays + Positionierung (Ebene 2+3) |
| Schwelle (76-100) | **Apex-Fähigkeiten**: Schattenform, Fieber-Ruf, Schattenwurzeln, massive Kampfkraft, Zugriff auf Emer-Material | Alle Äste -40-50%, Kontrollverlust, soziale Isolation, Halluzinationen | Kein direktes Äquivalent — Rein hat dafür volle soziale Integration und zuverlässige Wahrnehmung |

**Stufe-0-Äquivalent:** Jede Schattenfieber-Zone hat eine nicht-infizierte Alternative, die denselben Spielraum abdeckt, aber mit anderen Mitteln. Das sichert ab, dass Stufe 0 sich NIE wie "der langweilige Weg" anfühlt.

### 2.6 Kontrollverlust (V2 — narrativ definiert)

> V2-Änderung: In V1 war Kontrollverlust als offene Designfrage markiert. Die Entscheidung ist gefallen: Kontrollverlust ist NARRATIV, nicht mechanisch. Der Spieler verliert nie die Kontrolle über seinen Charakter. Was sich verändert, ist die Zuverlässigkeit seiner Wahrnehmung.

**Prinzip:** Die Steuerung bleibt IMMER beim Spieler. Kein Kontrollverlust im Input-Sinne — kein "dein Charakter macht jetzt was anderes als du willst". Was passiert, ist subtiler und verstörender: Die Welt, die der Spieler wahrnimmt, weicht von der "echten" Welt ab.

**Kontrollverlust-Episoden (Zone Schwelle, ab Wert 76):**
- **Trigger:** Hohe Stresssituationen (Bosskampf, Fraktionsverrat, Relikt-Kontakt). NICHT zufällig — der Spieler muss den Trigger als Konsequenz einer bewussten Entscheidung lesen können (Bedingung 3).
- **Dauer:** 30-90 Sekunden. Kurz genug, um nicht zu frustrieren. Lang genug, um zu verunsichern.
- **Was passiert:** Die Umgebung verändert sich visuell und auditiv. NPCs sagen andere Dinge. Wege führen anders als erwartet. Der Spieler navigiert durch eine Welt, die möglicherweise nicht die echte ist — aber er steuert dabei normal.
- **Nachher:** Die Episode endet. Der Spieler steht dort, wo er "wirklich" stand. Oder vielleicht nicht. Es gibt keinen UI-Hinweis, ob die Episode vorbei ist oder ob die "normale" Welt die Halluzination war.
- **Frequenz:** Maximal 2-3 pro Spielstunde auf Wert 90+. Seltener auf 76-85.

**Design-Ziel:** Der Spieler soll denken: "Ich habe die Kontrolle — aber kann ich meinen Augen trauen?" Das ist Horror durch Unsicherheit, nicht durch Ohnmacht.

**QA-Absicherung (Bedingung 3):** Jede Kontrollverlust-Episode muss auf eine bewusste Entscheidung zurückführbar sein. Der Spieler hat gewählt, in der Zone Schwelle zu sein. Er hat gewählt, diese Fähigkeiten zu nutzen. Der Kontrollverlust ist die Konsequenz — nicht die Strafe.

### 2.7 Weltreaktivität
- NPCs reagieren auf Infektionszone (Angst, Mitleid, Nützlichkeit, Feindschaft)
- Fraktionen verschieben Zugang: Orden schließt früh, Krone später, Gilden pragmatisch
- Infizierte NPCs erkennen den Spieler ab Zone Rauschen (spät) als "einen von ihnen"
- Mögliche emergente vierte Fraktion: Untergrund der Infizierten (offene Frage für Emre/Nami)
- Umgebungseffekte: Tiere fliehen, Pflanzen reagieren (ab Zone Risse)

### 2.8 Das Relikt: Die Lebende Krone

> CD-Entscheidung: Das Relikt dieser Iteration ist die **Lebende Krone** — ein Biotech-Artefakt aus der Großen Flechtung.

- Die Lebende Krone ist ein organisches Artefakt, das auf die kosmologische Große Flechtung (WBB-01, Kap. 4) zurückgeht — den Akt, der Emers Körper in die geschichtete Welt verwandelte und die Hauten (Membranen zwischen den Daseinsebenen) stabilisierte.
- Sie ist LEBENDIG im wörtlichen Sinne: Sie reagiert, wächst, verändert sich — Biotech auf kosmologischer Ebene. Sie besteht aus Emer-Material in seiner reinsten erhaltenen Form.
- Fraktions-Interpretationen:
  - **Krone**: Dynastisches Erbe, Legitimation der Herrschaft, Zeichen göttlichen Auftrags. Sigvalts Pflicht, weitergetragen.
  - **Gilden**: Das wertvollste Handelsgut der Welt, Machtinstrument ohne ideologische Bindung. Der Tharm hat einen Preis — die Krone ist sein teuerstes Stück.
  - **Orden**: Erkenntniswerkzeug, Schlüssel zum Verständnis der Großen Flechtung und der Daseinsebenen. Halvards Erbe: Verstehen kommt vor Verwandeln.
- Schattenfieber-Verbindung: Die Lebende Krone und das Schattenfieber greifen auf dasselbe Emer-Material zu (WBB-01, Kap. 6). Die Krone ist die kontrollierte Form, das Schattenfieber die unkontrollierte. Beide sind Rückverbindungen zum Emer-Körper — die eine geformt, die andere wild.
- Kontakt mit der Krone KANN den Infektionswert erhöhen — massiv, aber unter Bedingung 1 und 3 (Transparenz, bewusste Entscheidung)

**Offene Fragen zum Relikt:**
- [ ] Wie interagiert der Spieler physisch mit der Krone? Tragen? Berühren? Studieren? (Emre + Darius)
- [ ] Kann die Krone das Schattenfieber kontrollieren, nicht nur erhöhen? (CD-Rückfrage)
- [ ] Visuelle Erscheinung: Organisch, pulsierend, wurzelartig? (Vera)

### 2.9 Transparenz-UI (QA-Anforderung)

> Direkte Umsetzung von Bedingung 1. Dieses UI-Modul ist KEIN "nice-to-have" — es ist systemkritisch.

- **Infektionsanzeige**: Permanenter Balken/Indikator (nicht als Zahl, sondern als organische Visualisierung — passend zum Nervensystem-UI). Die drei Zonen (Rauschen, Risse, Schwelle) sind visuell unterscheidbar.
- **Warnhinweis**: Wenn der Spieler eine infektionssteigernde Zone betritt, Aktion ausführt oder Story-Entscheidung trifft → visueller + auditiver Cue BEVOR die Erhöhung eintritt
- **Fähigkeitskosten**: Jede Schattenfieber-Fähigkeit zeigt ihren Infektionskosten-Wert im Tooltip
- **Zonenwechsel-Warnung**: Wenn der Spieler kurz vor einer neuen Zonengrenze steht (5 Punkte entfernt), bekommt er einen besonderen Hinweis — der Zonenwechsel ist permanent (Hard Cap)
- **Halluzinations-Warnung** (Zone Schwelle): Ab Wert 76 gibt es KEINEN UI-Hinweis, ob die aktuelle Wahrnehmung real ist. Das ist Absicht — die fehlende Transparenz IST die Konsequenz.
- **Design-Vorgabe für Vera**: Die Infektionsanzeige soll sich organisch in die Nervensystem-Visualisierung einfügen. Kein separates HUD-Element, sondern Teil desselben körperlichen Systems.

### 2.10 Maret als optionaler Kompanion (V2 — neu)

> V2-Ergänzung: Maret wurde im Briefing (Tag 6) als optionaler Kompanion bestätigt — fraktionslos, Schattenfieber-Spiegel, kein Pflicht-NPC.

**Design-Rolle:** Maret ist kein Kompanion im BioWare-Sinne (kein Party-Mitglied, keine Romance-Option, kein ständiger Begleiter). Sie ist eine **narrative Spielmechanik** — ein wandelnder Spiegel des Schattenfieber-Systems.

**Mechanische Funktion:**
- **Für Stufe-0-Spieler:** Maret zeigt, was Schattenfieber kann und kostet. Ihre Fähigkeiten im Kampf (wenn sie den Spieler begleitet) demonstrieren Schattenfähigkeiten als Vorschau. Sie ist die lebende Antwort auf die Frage: "Was würde passieren, wenn ich mich infizieren lasse?"
- **Für infizierte Spieler:** Maret ist ein Vergleichspunkt. Ihre Infektion verläuft anders als die des Spielers — sie ist weiter fortgeschritten, aber kontrollierter (oder unkontrollierter, je nach ihrem eigenen Zustand). Sie macht die Varianz des Schattenfieber-Systems sichtbar.
- **Fraktionslos:** Maret gehört keiner Fraktion an. Das macht sie zugänglich für alle Spielstile, aber es gibt keine Fraktionsboni durch ihre Begleitung.
- **Optional:** Der Spieler kann Maret ablehnen, verlieren oder aussperren. Sie ist keine Pflicht — aber ihr Fehlen ist spürbar.

**Narrative Verankerung:**
- Maret ist eine eigenständige Figur mit eigener Geschichte (→ GDD-03, GDD-04)
- Ihr Schattenfieber-Status verändert sich im Spielverlauf — unabhängig vom Spieler
- In der Zone Schwelle wird Maret zum Unsicherheitsfaktor: Ist sie noch real? Ist sie eine Halluzination? Sieht der Spieler die echte Maret oder eine Schattenfieber-Projektion?

**Cassius bleibt stationär:** Cassius ist der andere Schlüssel-NPC aus dem Erzählkonzept. Er bleibt ein stationärer Questgeber — kein Kompanion. Die Arbeitsteilung ist klar: Cassius gibt Aufträge, Maret begleitet.

### 2.11 Offene Design-Fragen (V2-Stand, aktualisiert)

- [x] ~~Tod und Schattenfieber~~ → Tod erhöht den Wert NICHT (CD-bestätigt)
- [x] ~~Kontrollverlust-Design~~ → narrativ, nicht mechanisch (V2 definiert)
- [x] ~~Stufengrenzen~~ → Rauschen 1-40, Risse 41-75, Schwelle 76-100 (CD-bestätigt)
- [ ] Spezialisierungen innerhalb der Zonen (verschiedene Manifestationen) — V3-Feature?
- [ ] Interaktion mit dem Tiervolk (immun? anders infiziert?) — abhängig von Emres WBB-01
- [ ] Balancing Stufe 0 vs. Zone Schwelle — Stufe-0-Äquivalent-Spalte ist ein erster Ansatz, muss durchgetestet werden (QA mit Leo)
- [ ] Narrativer Zustand "Schwelle": Welche Questgeber sind "echt"? Gibt es eine Metaebene, die dem Spieler Hinweise gibt? (Nami + Darius)

---

## 3. Nervensystem-Leveling

### 3.1 Systemübersicht
- Vier physiologische Äste statt klassischer Skill-Trees
- Begrenzte Leveling-Punkte pro Level-Up — Ressourcenkonkurrenz erzwingt Spezialisierung
- Visuelle Darstellung: Halbtransparente Nervensystem-Ansicht des Körpers (Biotech-Futurismus)
- Progression ist KÖRPERLICH, nicht abstrakt
- **Kosmologische Verankerung (V2):** Der Spielercharakter IST Emer-Material — wie alles in dieser Welt. Die vier Äste sind vier Arten, dieses Material bewusst zu aktivieren. Das Nervensystem-Leveling ist kein abstraktes "Punkte ausgeben" — es ist das gezielte Wecken von Emer-Potenzial im eigenen Körper.

### 3.2 Die vier Äste

> V2-Ergänzung: Jeder Ast erhält einen kosmologischen Einzeiler, der ihn in Emres Weltbau verankert (Namis Punkt aus dem Tag-4-Standup). Die Einzeiler sind NICHT im Spiel sichtbar — sie sind Design-Leitlinien für das Team.

| Ast | Systeme | Kern-Attribute | Gameplay-Effekte | Kosmologischer Einzeiler |
|-----|---------|---------------|-----------------|--------------------------|
| **Cardio/Atmung** | Herz, Lunge, Kreislauf | Ausdauer, Regeneration, Bewegung | Sprint-Dauer, Schwimmen, Ausweich-Distanz, Erholungsrate | *Das Blut des Emer fließt noch — wer den Kreislauf stärkt, schöpft aus seinem Strom.* |
| **Muskel/Skelett** | Muskeln, Knochen, Sehnen | Stärke, Resistenz, Waffenhandhabung | Schadensoutput, Block-Stabilität, Tragekapazität, Waffenfreischaltung | *Die Knochen des Emer tragen die Gebirge — wer seine eigenen stärkt, trägt deren Echo.* |
| **Lymph/Immun** | Immunsystem, Stoffwechsel | Alchemie-Effizienz, Gift-Resistenz, Heilung | Trank-Wirkung, Krankheitsresistenz, passive Regeneration, Schattenfieber-Unterdrückung | *Der Stoffwechsel der Welt verarbeitet noch Emer-Material — wer sein Immunsystem meistert, spricht dieselbe Sprache.* |
| **Schatten** | Schattennervensystem | Schattensinne, Fähigkeiten, Wahrnehmung | NUR ab Infektionswert 1+; → Abschnitt 3.5 | *Der Emer ist nicht tot — er rauscht. Wer hinhört, wird verändert.* |

### 3.3 Trainer als Fraktions-Erzähler (V2 — erweitert)

> V2-Änderung: Trainer wurden in V1 als mechanisches System beschrieben (Geld + Ruf + Vorbedingung). In V2 wird ihre NARRATIVE Funktion gleichwertig behandelt. Trainer sind nicht nur Skill-Verkäufer — sie sind die Stimmen ihrer Fraktionen.

**Grundprinzip:**
- Fähigkeiten werden bei NPCs in der Welt gelernt, NICHT im Menü geklickt
- Jede Fraktion hat EXKLUSIVE Trainer (für bestimmte Fähigkeiten/Waffenstile)
- Trainer verlangen: Geld + Ruf + Vorbedingung (z.B. "Zeig mir, dass du parieren kannst")
- Gothic-Referenz: Die Welt ist das Klassenzimmer

**Trainer als Fraktions-Erzähler:**
Jeder Trainer ERKLÄRT seine Fähigkeit im Kontext seiner Fraktion. Der Krone-Schwertmeister lehrt nicht einfach "Parade Level 2" — er erzählt, warum die Krone diese Technik braucht, woher sie stammt, wer damit gewonnen und wer damit verloren hat. Der Gilden-Giftmischer beschreibt nicht nur die Wirkung — er rechnet den Marktwert vor. Der Orden-Gelehrte verbindet jede Fähigkeit mit der kosmologischen Ordnung.

**Mechanische Auswirkung:**
- Dieselbe Fähigkeit kann bei verschiedenen Fraktions-Trainern leicht ANDERS funktionieren (nicht stärker/schwächer — anders). Beispiel: "Parade" bei der Krone ist defensive Standfestigkeit. "Parade" bei den Gilden ist ein Setup für einen Gegenangriff. Beide heißen "Parade". Beide funktionieren. Beide erzählen etwas über die Fraktion.
- Exklusive Fähigkeiten existieren weiterhin — aber die fraktionsübergreifenden Basis-Fähigkeiten haben fraktionsspezifische FLAVORS.

**Trainer-Typen im Vertical Slice:**

| Fraktion | Trainer-Typ | Exklusive Fähigkeiten | Erzähl-Tonalität |
|----------|-------------|----------------------|-------------------|
| **Krone** | Waffenmeister, Taktiker | Schwert-Mastery, Schildtechniken (Post-Slice), Formationskampf | Pflicht, Ehre, militärische Disziplin |
| **Gilden** | Fechtlehrer, Giftmischer, Alchemisten | Dolch-Mastery, Gift-Applikation, Handels-Alchemie | Kosten-Nutzen, Effizienz, Pragmatismus |
| **Orden** | Kampfgelehrte, Forscher | Axt-Grundlagen, Lymph-Mastery, Schattenfieber-Theorie | Erkenntnis, Ordnung, kosmologischer Kontext |
| **Tiervolk** | Straßenlehrer, Jäger | Bogen-Techniken, Dolch-Varianten, Schleichtechniken | Überlebensinstinkt, Improvisation, Randwissen |

### 3.4 Perks/Fähigkeiten-Prinzip
- TRANSFORMATIV, nicht numerisch — Perks verändern WIE man spielt, nicht nur Zahlenwerte
- Korrekt: "Du kannst jetzt im Sprint angreifen" / "Paraden reflektieren Projektile"
- Falsch: "+20% Schwertschaden" / "+50 HP"
- Numerische Steigerungen kommen durch die Ast-Investition selbst, nicht durch einzelne Perks

### 3.5 Der Schatten-Ast (V2 — eigener Abschnitt)

> V2-Änderung: In V1 war der Schatten-Ast eine Zeile in der Äste-Tabelle. Er verdient einen eigenen Abschnitt, weil er fundamental anders funktioniert als die drei konventionellen Äste.

**Zugangsvoraussetzung:** Infektionswert 1+ (ein einziger Punkt Schattenfieber genügt). Ab diesem Moment erscheint der Schatten-Ast in der Nervensystem-Ansicht — als viertes, dunkleres Geflecht, das sich durch die drei konventionellen Äste zieht.

**Grundmechanik:**
- Der Schatten-Ast konkurriert um dieselben Leveling-Punkte wie die drei konventionellen Äste
- Investition in den Schatten-Ast verstärkt Schattenfieber-Fähigkeiten UND erhöht die Effizienz der Infektions-Nutzung (weniger Infektionsanstieg pro Fähigkeitseinsatz bei hoher Schatten-Investition)
- ABER: Jeder Punkt im Schatten-Ast ist ein Punkt, der NICHT in Cardio, Muskel oder Lymph investiert wird — die Spezialisierungsfrage ist real und permanent

**Interaktion mit konventionellen Ästen:**
- Hoher Schatten-Ast + niedriger Lymph = maximale Schattenfieber-Power, aber minimale Alchemie-Effizienz und Schattenfieber-Unterdrückung
- Hoher Schatten-Ast + hoher Cardio = Schattenfähigkeiten mit hoher Mobilität (Schatten-Schritt + Sprint)
- Hoher Schatten-Ast + hoher Muskel = Schattenfieber-verstärkter Nahkampf (Fieber-Puls + Melee-Bonus)
- Balancierter Schatten = moderate Fähigkeiten in allem, Mastery in nichts — generalist, nicht spezialist

**Kosmologische Verankerung:**
Der Schatten-Ast ist kein viertes Organsystem — er ist die Emer-Resonanz im Körper des Spielers. Das Schattenfieber weckt etwas, das immer schon da war: die Erinnerung des Emer-Materials an seinen Ursprungszustand. Wer den Schatten-Ast ausbaut, kultiviert diese Erinnerung — bewusst, gezielt, riskant.

**Fähigkeiten-Progression im Schatten-Ast:**

| Schatten-Stufe | Fähigkeiten | Voraussetzung |
|----------------|-------------|---------------|
| 1-3 | Schattensinne (passiv), Emotionsauren | Infektionswert 1+ |
| 4-6 | Schattenreflex, Schatten-Schritt | Infektionswert 16+, Rauschen |
| 7-9 | Schattenprojektion, Fieber-Puls, Tiefensicht | Infektionswert 41+, Risse |
| 10-12 | Schattenform, Fieber-Ruf, Schattenwurzeln | Infektionswert 76+, Schwelle |

**Visuelle Darstellung:**
Der Schatten-Ast soll sich visuell von den drei konventionellen Ästen unterscheiden — organischer, dunkler, pulsierend. Er wächst DURCH die anderen Äste hindurch, nicht neben ihnen. Mit steigender Investition dominiert er die Nervensystem-Ansicht optisch — eine visuelle Warnung, die gleichzeitig eine visuelle Belohnung ist.

### 3.6 Offene Design-Fragen
- [ ] Punkte pro Level-Up: Feste Anzahl oder skalierend?
- [ ] Max-Level: Reicht für wie viele Äste? Empfehlung: 2 Äste voll + 1 halb ODER 3 Äste mittel
- [ ] Respec möglich? Wenn ja, unter welchen Bedingungen? (Trainer? Kosten? Einmalig?)
- [ ] Visuelle Darstellung: Wie genau sieht die Nervensystem-Ansicht im UI aus? (Vera)
- [ ] Schatten-Ast: Separate Punkte oder gleicher Pool? (V2-Empfehlung: gleicher Pool — die Ressourcenkonkurrenz IST die Mechanik)

---

## 4. Alchemie und Crafting

### 4.1 Design-Philosophie
- Alchemie ersetzt Magie — es ist das primäre "übernatürliche" Werkzeug für Stufe-0-Spieler
- Wenige, bedeutsame Rezepte statt endloser Crafting-Listen
- Zutaten-Beschaffung als Explorations-Motivation
- Crafting ist NICHT endlos wiederholbar (begrenzte Zutaten, keine Respawn-Pflanzen)
- **Biotech-Forschung IST gefährlich** (CD-bestätigt): Alchemie ist nicht sicher. Experimente können schiefgehen, Nebenwirkungen sind real. Das ist keine Bestrafungsmechanik, sondern Weltkonsequenz — in einer Welt, die auf dem Emer-Körper gebaut ist, ist jeder Eingriff in die Biologie ein Risiko.

### 4.2 Produktkategorien

| Kategorie | Funktion | Beispiele |
|-----------|----------|-----------|
| **Heilung** | HP-Wiederherstellung, Regeneration | Heiltrank (sofort), Regenerationstinktur (über Zeit) |
| **Combat-Buffs** | Temporäre Kampfverstärkung | Waffenöle (Elementarschaden), Reflexelixier (Parry-Window +), Stärketrank |
| **Schattenfieber-Kontrolle** | Infektionswert beeinflussen | Suppressiva (senkt Wert), Stabilisatoren (verhindert Anstieg temporär), Booster (erhöht Wert bewusst für Fähigkeits-Burst) |
| **Gifte** | Offensiv, Waffen-Applikation | Lähmendes Gift (Ausdauer-Entzug), Nervenagent (Wahrnehmungsstörung beim Feind), Kontaktgift (Falle) |
| **Utility** | Exploration, Überleben | Nachtsicht-Tinktur, Atem-Verlängerer (Unterwasser), Klettergrip (verbesserte Haftung) |
| **Schutz** | Anti-Infektions-Präparate | Schattenresistenz-Öl (temporärer Schutz in verseuchten Zonen), Immunbooster (Infektionsanstieg halbiert für X Minuten) |

Die Kategorie "Schutz" ist ein direktes Ergebnis von Bedingung 3 (kein versehentliches Infizieren). Stufe-0-Spieler brauchen taktische Werkzeuge, um infektionsgefährliche Gebiete und Kämpfe zu bestreiten, OHNE sich zu infizieren. Das macht Alchemie für reine Spieler genauso wertvoll wie Schattenfieber-Fähigkeiten für infizierte Spieler.

### 4.3 Suchtmechanik bei Combat-Buffs (V2 — neu)

> V2-Ergänzung: Die offene Frage aus V1 ("Suchtmechanik: Haben Combat-Buffs Nebenwirkungen bei Überkonsum?") ist jetzt beantwortet. Ja — mit einem klaren Design-Prinzip: Sucht ist ein Risiko-Management-System, KEINE Bestrafungsspirale.

**Grundprinzip:** Das Briefing nennt "Echte Drogen, Amphetamine" als Designrichtung. Alchemie-Buffs sind in dieser Welt keine harmlosen Power-Ups — sie sind Eingriffe in Emer-Material, und der Körper reagiert darauf. Aber: Die Suchtmechanik darf den Spieler nie in eine Abwärtsspirale treiben, aus der er nicht mehr herauskommt. Sie ist ein Werkzeug zur Risikobewertung, kein Bestrafungsinstrument.

**Mechanik — Gewöhnung statt Entzug:**

| Konsumhäufigkeit | Effekt | Spieler-Erfahrung |
|------------------|--------|-------------------|
| **Gelegentlich** (1-2 pro Quest) | Volle Wirkung, keine Nebenwirkungen | "Dieses Zeug ist gut. Ich nutze es, wenn ich es brauche." |
| **Regelmäßig** (3-5 pro Quest) | Volle Wirkung, Toleranz-Aufbau: nächste Dosis braucht 2 Zutaten statt 1 | "Ich brauche mehr davon. Lohnt sich das noch?" |
| **Exzessiv** (6+ pro Quest) | Volle Wirkung, aber temporäre Nacheffekte: Cardio-Malus nach Abklingen, Lymph-Schwankungen | "Ich bin nach dem Kampf für 2 Minuten langsamer. War es das wert?" |

**Was Sucht NICHT ist:**
- KEINE permanente Stat-Reduktion. Der Spieler kann IMMER aufhören, ohne bleibende Schäden.
- KEIN Entzugs-Debuff, der den Spieler handlungsunfähig macht.
- KEINE versteckte Mechanik — der Spieler sieht im Tooltip: "Gewöhnung: 2/5. Nächste Stufe erhöht Materialkosten."
- KEINE moralische Wertung durch das Spiel. NPCs kommentieren vielleicht ("Du siehst nicht gut aus"), aber das System selbst urteilt nicht.

**Was Sucht IST:**
- Ein RESSOURCEN-Management-System: Häufiger Konsum = höhere Materialkosten. Der Spieler muss entscheiden: Investiere ich knappe Zutaten in häufige schwache Buffs oder seltene starke?
- Ein TEMPO-Werkzeug: Nacheffekte nach exzessivem Konsum erzwingen kurze Pausen — das verlangsamt den Spielrhythmus, ohne ihn zu blockieren.
- Ein NARRATIVES Signal: Der Körper reagiert auf Alchemie wie auf jede andere Manipulation von Emer-Material — mit Gegenreaktion. Das ist Welt-Konsistenz, nicht Strafe.

**Gewöhnung zurücksetzen:**
- Gewöhnung baut sich bei Nicht-Konsum über Zeit ab (1 Stufe pro Spieltag ohne Konsum)
- Lymph-Ast-Investition beschleunigt den Abbau
- Kein "Reset-Trank" — der Körper braucht Zeit, nicht Alchemie

**Interaktion mit Schattenfieber:**
- Infizierte Spieler (Zone Rauschen+) haben eine HÖHERE Grundtoleranz — ihr Emer-Material ist bereits aktiviert, also reagiert es weniger stark auf Alchemie-Buffs. Vorteil: Mehr Konsum ohne Nacheffekte. Nachteil: Alchemie wirkt generell schwächer (Lymph-Malus durch Infektion).

### 4.4 Herstellungsprozess
- Zutaten finden (Exploration, Handel, Beute)
- Rezepte lernen (Trainer-Prinzip: Alchemisten-NPCs, Lore-Fragmente, Experiment)
- Herstellung an Alchemie-Stationen (feste Orte in der Welt, NICHT tragbar)
- Qualitätsstufen: Basis → Verbessert → Meister (abhängig von Lymph-Ast und Trainer-Rang)

### 4.5 Schnittstelle zu anderen Systemen
- **Lymph-Ast:** Bestimmt Trank-Wirkung und verfügbare Rezepte
- **Schattenfieber:** Suppressiva als wichtigste Produktkategorie; hoher Infektionswert = schwächere Alchemie-Wirkung (Trade-Off!)
- **Combat:** Waffenöle und Gifte als taktische Vorbereitung vor Kämpfen
- **Fraktionen:** Exklusive Rezepte pro Fraktion (Orden: Reinigungsmittel, Gilden: Handelsgifte, Krone: Militärtränke)
- **Stufe-0-Spielpfad:** Schutz-Kategorie als mechanisches Äquivalent zu Schattenfieber-Resistenz (QA-validiert)
- **Suchtmechanik:** Gewöhnung erhöht Materialkosten → Explorations-Motivation (mehr Zutaten nötig) → Tiervolk-Schwarzmarkt als Quelle

### 4.6 Offene Design-Fragen
- [ ] Rezeptanzahl für den Vertical Slice? Empfehlung: 15-20 Basisrezepte
- [ ] Experiment-System: Kann der Spieler Zutaten frei kombinieren? Oder nur bekannte Rezepte?
- [ ] Tiervolk als Alchemie-Händler: Exklusive Zutaten? Andere Tradition?
- [x] ~~Suchtmechanik~~ → Gewöhnungs-System definiert (V2)

---

## 5. Exploration und Weltnavigation

### 5.1 Weltstruktur
- Semi-Open-World: Eine zusammenhängende Kernregion (~4-6 km²)
- Gothic-Dichte: Wenig Leerraum, hohe POI-Dichte, handplatziert
- Keine Schnellreise (oder: spät freischaltbar, als Luxus, nicht als Notwendigkeit)
- Zusammenhängende Oberwelt ohne Ladebildschirme

### 5.2 Vertikalität
- Städte: Begehbare Dachlandschaften, Keller, Kanalisation, Brücken, Turmebenen
- Wildnis: Klippen, Höhlen, Baumkronen, Flussbetten, Bergpässe
- Immer mehrere Wege: Hauptweg (sicher, lang), Schleichweg (riskant, kurz), Vertikalweg (Geschick erforderlich)
- Dishonored-Prinzip: Der Raum hat drei Dimensionen

### 5.3 Belohnungsstruktur
- Neugier wird IMMER belohnt: Abseits der Wege = Alchemie-Zutaten, Lore-Fragmente, versteckte NPCs, Schattenfieber-Hotspots
- Keine Quest-Marker auf der Karte (oder: minimal, abschaltbar) — Beschreibungen, Sightlines, NPC-Hinweise
- Umweltpuzzles: Kombination aus Beobachtung, Alchemie und Schattensinnen
- Handplatzierte Schätze mit narrativer Einbettung (Warum liegt das hier? Wer hat es versteckt?)

### 5.4 Sichtbarkeitsschichten (Schattenfieber-Integration)
- Stufe 0: Normale Wahrnehmung — Geheimtüren und Fallen nur durch genaues Hinsehen findbar
- Zone Rauschen: Schattensinne enthüllen versteckte Objekte, Geheimgänge, vergiftete Gegenstände
- Zone Risse: Emotionsauren an NPCs, Tiefensicht für Schatzsuche, alternative Wege durch Schatten-Schritt
- Zone Schwelle: Doppelwahrnehmung — die "zweite Schicht" ist permanent sichtbar, aber nicht immer vertrauenswürdig
- Die Welt hat ZWEI Schichten — und Schattenfieber zeigt die zweite
- **Stufe-0-Alternative**: Alchemie (Nachtsicht-Tinktur), genaue Beobachtung, NPC-Hinweise — andere Methode, gleicher Inhalt (QA-validiert)

### 5.5 Points of Interest (Typen)

| Typ | Beispiele | Belohnung |
|-----|----------|-----------|
| **Siedlungen** | Städte, Dörfer, Einzelhöfe | NPCs, Quests, Trainer, Handel |
| **Dungeons** | Katakomben, Minen, Ruinen, Ordensfestungen | Ausrüstung, Lore, Boss-Gegner |
| **Schattenfieber-Zonen** | Verseuchte Gebiete, Ritualstätten | Infektionsrisiko (mit Vorwarnung!), seltene Alchemie-Zutaten, Lore |
| **Landmarken** | Aussichtspunkte, Statuen, Ruinen | Kartenenthüllung, Orientierung, Lore |
| **Verstecke** | Schmugglerlager, Diebesverstecke, Tiervolk-Lager | Handel (Schwarzmarkt), Quests, Alchemie |

### 5.6 Offene Design-Fragen
- [ ] Schnellreise: Ja/Nein? Wenn ja, unter welchen Bedingungen? Empfehlung: Erst im zweiten Akt, als narrative Belohnung
- [ ] Karte: Wie viel zeigt die Spielerkarte? Empfehlung: Handgezeichnet, wird durch Exploration aufgedeckt
- [ ] Tages-/Nachtzyklus: Welche Gameplay-Auswirkungen? NPC-Routinen, Gegnerverhalten, Schattenfieber-Intensität?
- [ ] Wetter: Reiner Atmosphäre-Effekt oder Gameplay-relevant? (z.B. Regen = besseres Schleichen, Nebel = eingeschränkte Sicht)

---

## 6. Querschnittsthemen

### 6.1 Namenssysteme (V2 — aktualisiert)

> CD-Entscheidung: RELICS verwendet eigene Namenssysteme, KEINE nordisch/germanischen Namen in der Spielwelt. Das WBB-01 V2 liefert das vollständige Kosmologische Lexikon (→ WBB-01, Lexikon).

**Durchgehend aktualisierte Begriffe in GDD-02:**

| Alter Begriff (V1) | RELICS-Begriff (V2) | Kontext |
|---------------------|----------------------|---------|
| Ymir | **Emer** | Das Urwesen, dessen Körper zur Welt wurde |
| Ur-Bindung | **Große Flechtung** | Der kosmologische Akt, der die Schichten trennte |
| Daseinsebenen (allgemein) | **Hohlicht / Mittelgrund / Stillfeld** | Die drei Schichten der Welt |
| Membranen | **Hauten** | Trennschichten zwischen den Daseinsebenen |
| Kosmologische Erosion | **Faulung** (Krone), **Schwund** (Gilden), **Entflechtung** (Orden) | Je nach Fraktions-Perspektive |

**Arbeitsnamen im GDD:**
- Schattenfieber-Zonen (Rauschen, Risse, Schwelle) — Arbeitsnamen, die zum eigenen Namenssystem passen. Können so bleiben.
- Schattenfieber-Fähigkeitsnamen (Schattensinne, Schattenreflex, Schatten-Schritt, etc.) — Arbeitsnamen. Müssen vor V3 geprüft werden.
- Infektionsstufen-Bezeichnungen aus V1 (Rein, Gezeichnet, Infiziert, Verwandelt, Entfesselt) — durch das Drei-Zonen-Modell abgelöst.

### 6.2 Build-Archetypen (emergent, nicht vordefiniert)

| Build | Schattenfieber-Zone | Schwerpunkte | Spielstil |
|-------|---------------------|-------------|-----------|
| Reiner Krieger | Stufe 0 | Muskel + Cardio | Schwere Waffen, Ausdauer, volles Parry |
| Alchemist | Stufe 0 / Rauschen (früh) | Lymph + Cardio | Trank-fokussiert, Gifte, Buff-Öle, Schutz-Präparate |
| Schattenspäher | Rauschen | Schatten + Cardio | Exploration, Stealth, Schatten-Schritt |
| Hybrid-Kämpfer | Risse | Muskel + Schatten | Risk/Reward, explosive Spitzen |
| Schattenbestie | Schwelle | Schatten (voll) | Glass Cannon, sozialer Außenseiter, Parallel-Narrativ |

### 6.3 System-Interaktionen

```
COMBAT <-> SCHATTENFIEBER
  Schattenreflex erweitert Parry (Zone Rauschen)
  Fieber-Puls als AoE (Zone Risse, kostet HP)
  Infizierte Feinde = Vorschau eigener Fähigkeiten
  Maret als wandelnde Schattenfieber-Demonstration
  Schutz-Alchemie als Stufe-0-Alternative (QA)

SCHATTENFIEBER <-> NERVENSYSTEM
  Schatten-Ast konkurriert um Leveling-Punkte (gleicher Pool)
  Hohe Infektion = schwache konventionelle Äste
  Spezialisierung vs. Breite — die zentrale Build-Frage
  Kosmologische Verankerung: Emer-Resonanz

ALCHEMIE <-> SCHATTENFIEBER
  Suppressiva senken Infektionswert
  Booster erhöhen ihn bewusst
  Schutz-Präparate verhindern Anstieg (Stufe-0-Werkzeug)
  Lymph-Ast bestimmt Alchemie-Effizienz
  Suchtmechanik: Gewöhnung als Ressourcen-Management

EXPLORATION <-> SCHATTENFIEBER
  Verseuchte Zonen erhöhen Infektion (MIT Vorwarnung)
  Schattensinne enthüllen versteckte Inhalte
  Stufe-0-Alternative: Alchemie + Beobachtung
  Exploration belohnt mit Alchemie-Zutaten

FRAKTIONEN <-> SCHATTENFIEBER
  Infektionszone beeinflusst Fraktionszugang
  Exklusive Trainer/Rezepte pro Fraktion
  Trainer als Fraktions-Erzähler (V2)
  Orden bietet Reinigung, distanziert sich ab Zone Risse

NARRATIV <-> SCHATTENFIEBER (Nami-Sync)
  Rauschen (1-40): Subtile Textverschiebungen
  Risse (41-75): Alternative Dialoge, fragwürdige Questgeber
  Schwelle (76-100): Parallel-Narrativ, Halluzinationen ab Wert 76
  Kontrollverlust = narrativ, nicht mechanisch (V2)
  Maret als Schattenfieber-Spiegel
```

### 6.4 Balancing-Leitlinien
- Stufe 0 = gleichwertig zu Zone Schwelle — ANDERE Erfahrung, nicht schlechtere
- Keine "Best Build"-Situation — Trade-Offs müssen echt sein
- Die Welt-Schwierigkeit wird durch Geographie bestimmt, nicht durch Slider
- Vertikaler Fortschritt (mächtig werden) UND horizontaler Fortschritt (anders werden)
- Stufe-0-Äquivalent-Tabelle (2.5) als Balancing-Grundlage
- QA-Schleife: Leo prüft jede Mechanik aus Spielersicht — 40% Fokus auf Schattenfieber
- Suchtmechanik: Gewöhnung darf nie zur Bestrafungsspirale werden (Leo-Veto bei Verletzung)

### 6.5 QA-Risikomatrix (Leo-Input)

| Risiko | Schwere | Wahrscheinlichkeit | Mitigation |
|--------|---------|---------------------|------------|
| Versehentliche Infektion | KRITISCH | Hoch (ohne Maßnahmen) | Bedingung 3 + Schutz-Alchemie + UI-Warnungen |
| Stufe 0 fühlt sich leer an | HOCH | Mittel | Stufe-0-Äquivalente, exklusive Alchemie-Inhalte |
| Zonenübergänge fühlbar machen | HOCH | Hoch | Gradueller Übergang, QA pro Infektionswert |
| Kontrollverlust frustriert statt fasziniert | MITTEL | Mittel | Narrativer Kontrollverlust (V2), Steuerung bleibt |
| Community-Backlash "nicht heilbar" | MITTEL | Sicher | Transparente Kommunikation VOR Release, "kontrollierbar" als Frame |
| Schattenfieber-Dialoge brechen Quests | HOCH | Hoch | Systematisches Testing aller Quest-States x Infektionszonen |
| Suchtmechanik wird als Bestrafung gelesen | MITTEL | Mittel | Transparenz (Tooltip), kein permanenter Schaden, Leo-Veto |
| Maret-Halluzination bricht Quests | MITTEL | Mittel | Maret-Quests als eigenständig flaggen, Halluzinations-Maret löst keine Quest-Trigger aus |

---

## 7. Zusammenfassung: Nächste Schritte

| Aufgabe | Verantwortlich | Timeline | Status |
|---------|---------------|---------|--------|
| QA-Schleife: Spielerperspektive auf GDD-02 | Darius + Leo | Tag 2 | ERLEDIGT (V0.5) |
| Schattenfieber-Stufen-Mapping mit Nami | Darius + Nami | Tag 2 | ERLEDIGT (V0.5) |
| Stufengrenzen auf CD-Tabelle | CD + Darius | Tag 4 | ERLEDIGT (V2) |
| Namenssystem durchgehend (Emer, Große Flechtung) | Leo + Darius | Tag 5-6 | ERLEDIGT (V2) |
| Waffenklassen für Vertical Slice festzurren | Darius | Tag 6 | ERLEDIGT (V2) |
| Suchtmechanik Alchemie designen | Darius | Tag 6 | ERLEDIGT (V2) |
| Nervensystem-Äste kosmologisch verankern | Darius + Emre | Tag 6 | ERLEDIGT (V2) |
| Kontrollverlust definieren | Darius + Nami | Tag 6 | ERLEDIGT (V2) |
| Schatten-Ast eigener Abschnitt | Darius | Tag 6 | ERLEDIGT (V2) |
| Trainer als Fraktions-Erzähler | Darius | Tag 6 | ERLEDIGT (V2) |
| Maret als optionaler Kompanion | Darius + Nami | Tag 6 | ERLEDIGT (V2) |
| Lebende Krone: Interaktionsdesign | Darius + Emre | Tag 7+ | Offen |
| Schattenfieber-Fähigkeitsnamen prüfen | Emre + Darius | Tag 7+ | Offen |
| Combat-Detail: Waffenklassen-Movesets | Darius | Tag 7+ (V3) | Offen |
| Alchemie-Rezeptliste (V1) inkl. Schutz-Kategorie | Darius | Tag 7+ (V3) | Offen |
| Balancing-Framework (Stufe 0 vs. Schwelle) | Leo + Darius | Tag 7+ (V3) | Vorbereitet (Äquivalent-Tabelle) |
| Transparenz-UI: Wireframes | Vera + Darius | Tag 7+ | Offen |

---

*Darius Engel, Game Design Corner, Tag 6 (Montag) — V2*
*"Macht es Spaß? Was ist die Spieler-Fantasie hier?" — Neun V2-Punkte umgesetzt. Das Dokument hat jetzt eine kosmologische Verankerung, festgezurrte Waffenklassen, eine Suchtmechanik ohne Bestrafungsspirale, und Maret als wandelnden Schattenfieber-Spiegel.*
