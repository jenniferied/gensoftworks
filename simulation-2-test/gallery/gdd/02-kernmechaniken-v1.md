# GDD-02: Kernmechaniken

**Autor:** Darius Engel, Game Director
**QA:** Leo Brandt (Spielermarkt & Community)
**Narrativ-Sync:** Nami Osei (Erzählkonzept)
**Version:** V0.5 (Tag 2, Dienstag — Nachmittags-Überarbeitung)
**Status:** Zwischen Outline und V1 — Strukturen stehen, Schlüsselabschnitte angereichert, offene Fragen reduziert
**Änderungslog:**
- V1-Outline (Tag 2 Vormittag): Kapitelstruktur + Kernpunkte
- V0.5 (Tag 2 Nachmittag): Leos QA-Bedingungen integriert, Schattenfieber-Stufen-Mapping mit Nami synchronisiert, CD-Entscheidungen eingearbeitet (Tod/Infektion, Lebende Krone, Namenssysteme, Combat-Skill-Ceiling)
- V0.5.1 (Tag 5 Nachmittag): Arbeitsbegriff "Ymir" → "Emer" (2x: Kap. 2.7, Kap. 6.1) — Leo Fischer, QA

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
- Schattenfieber-Combat-Integration: Schattenreflex (erweitertes Parry-Window), Fieber-Puls (Aö, kostet HP)
- Perfekte Paraden: Winzigstes Timing-Fenster, maximal belohnend (Spezial-Riposte)

### 1.3 Waffenklassen (vorläufig)
- **Schwerter** (Einhand/Zweihand): Allrounder, mittlere Geschwindigkeit, ausgewogenes Moveset
- **Äxte/Hämmer** (Einhand/Zweihand): Langsam, hoher Schaden, Schildbrecher
- **Dolche/Kurzwaffen**: Schnell, niedriger Einzelschaden, Combo-orientiert, Giftapplikation
- **Bögen**: Ranged, Haltungsschaden, kein Hauptwaffen-Fokus (Unterstützung)
- **Armbrüste**: Schwerer Ranged-Schaden, lange Nachladezeit, Situationswaffe
- **Schilde**: Defensiv, Block-Effizienz, Schildstoss als Unterbrechung

**Offene Frage:** Waffenklassen-Anzahl für den Vertical Slice? Empfehlung: 3-4 Nahkampf + 1 Ranged für V1.

### 1.4 Feinddesign-Prinzipien
- Feinde haben EIGENE Movesets, nicht nur skalierte Spieler-Angriffe
- Feindtypen definiert durch Verhalten, nicht nur durch Werte: Aggressive, Defensive, Taktiker, Infizierte
- Infizierte Feinde nutzen Schattenfieber-Fähigkeiten — Vorschau für den Spieler ("Das könnte ICH auch")
- Keine Level-Skalierung: Gebiete haben feste Feindstärke. Manche Gegner sind zu früh zu stark. Komm später wieder.

### 1.5 Tod und Konsequenz
- Tod ist ein Rückschlag, kein Game Over — Checkpoint-System mit fairen Abständen
- Keine Erfahrungspunkt-Strafe bei Tod
- **Tod beeinflusst den Infektionswert NICHT** (CD-bestätigt). Begründung: Tod ist bereits Strafe genug. Infektionsanstieg bei Tod würde Risk/Reward des Schattenfieber-Systems untergraben und die bewusste Entscheidung zur Nutzung verwischen.
- Konsequenz durch WELT-Reaktion: Bestimmte Situationen verändern sich bei erneutem Versuch (NPC-Kommentare, veränderte Wachpositionen)

---

## 2. Schattenfieber-System

> **QA-Einschätzung (Leo):** 40% des QA-Aufwands entfällt auf das Schattenfieber-System. Es ist gleichzeitig grösster USP und grösstes Risiko. Die folgenden drei nicht-verhandelbaren Bedingungen sind das Ergebnis von Leos Community- und Marktanalyse.

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
- Fünf mechanische Stufen mit spürbaren Schwellen
- Vierter Ast im Nervensystem-Leveling (nur ab Stufe 1+)
- NICHT heilbar, nur kontrollierbar (CD-bestätigt)
- Jede Stufe = andere Spielerfahrung, KEINE ist schlechter als die andere

### 2.3 Stufen-Mapping: Mechanik x Narrativ x Wahrnehmung

Die folgende Tabelle synchronisiert Darius' fünf mechanische Stufen mit Namis drei narrativen Zuständen (Rauschen, Risse, Schwelle). Die narrativen Zustände sind KEINE separaten Systeme — sie sind die erlebbare Oberflächenerscheinung der mechanischen Stufen.

| Mech. Stufe | Wert | Name | Narrativer Zustand (Nami) | Kern-Fantasie | Zentrale Fähigkeit | Narrative Auswirkung |
|-------------|------|------|---------------------------|---------------|---------------------|---------------------|
| 0 | 0 | Rein | Gesund | Underdog, rein menschlich | Volle Nervensystem-Effizienz, uneingeschränkte Sozialinteraktion | Standard-Erzählung: klare, zuverlässige Wahrnehmung |
| 1 | 1-25 | Gezeichnet | Rauschen | "Ich sehe, was andere nicht sehen" | Schattensinne (passiv): Verstecktes sichtbar, Emotionsauren | Subtile Textveränderungen in Dialogen. Umgebungshinweise, die andere nicht sehen. Einzelne Worte in NPC-Sätzen verschieben sich. Spieler bemerkt es vielleicht nicht sofort. |
| 2 | 26-50 | Infiziert | Rauschen → Risse (Übergang) | Mächtig, aber sichtbar anders | Schattenreflex, Schatten-Schritt, Schmerzunterdrückung | Übergangszone: Hinweise werden deutlicher, erste fragwürdige Wahrnehmungen. Gesprächsoptionen erscheinen, die andere nicht hören. |
| 3 | 51-75 | Verwandelt | Risse | Kein Mensch mehr, aber mächtig | Schattenprojektion, Fieber-Puls, Tiefensicht | Alternative Dialoge mit Figuren, die möglicherweise anders reden als erwartet. Fragwürdige Questgeber. NPCs reagieren irritiert auf Antworten, die der Spieler für normal hält. |
| 4 | 76-100 | Entfesselt | Schwelle | Das Monster — und vielleicht ist das okay | Schattenform, Fieber-Ruf, Schattenwurzeln + Kontrollverlust-Episoden | Parallel-Narrativ: Dialoge mit Figuren, die möglicherweise nicht existieren. Daseinsebenen werden durchlässig. Der Spieler kann nicht mehr unterscheiden, welche Gespräche "echt" sind. |

**Übergangs-Design:**
- Stufenübergänge sind KEINE harten Schalter. Der Infektionswert bestimmt die Intensität innerhalb einer Stufe graduell.
- Beispiel: Bei Wert 15 sind Schattensinne schwächer als bei Wert 24. Es gibt keinen Moment, in dem alles "anspringt".
- Die narrativen Zustände haben weiche Grenzen: "Rauschen" beginnt ab dem ersten Infektionspunkt und intensiviert sich. "Risse" setzt schrittweise ab ca. Wert 40 ein. "Schwelle" wird ab ca. Wert 70 spürbar.
- **QA-Relevanz (Leo)**: Genau dieser graduelle Übergang ist der Grund für den hohen QA-Aufwand. Jeder der ~100 Infektionswerte muss sich in der Spielerfahrung "richtig" anfühlen.

### 2.4 Infektionsfortschritt

**Steigerung:**
- Umgebungsexposition (verseuchte Orte, Kampf gegen Infizierte) — NUR mit vorheriger Warnung (Bedingung 1+3). Der Spieler sieht/hört/spürt, dass ein Ort verseucht ist, BEVOR er ihn betritt.
- Bewusste Nutzung (Schattenfieber-Fähigkeiten einsetzen: ~0.5-1 Punkt pro Einsatz) — jede Fähigkeitsnutzung zeigt den Infektionsanstieg im UI
- Story-Events (Schlüsselmomente, Boss-Begegnungen) — IMMER als bewusste Spielerentscheidung präsentiert, nie als Cutscene-Zwang
- Kontakt mit der Lebenden Krone (siehe 2.7) — Relikt-Interaktion als hochriskante, hochbelohnende Infektionsquelle
- Tod erhöt den Infektionswert NICHT (CD-bestätigt)

**Senkung:**
- Alchemie-Suppressiva (-3 bis -5 Punkte, teuer, Wirkung nimmt bei hohem Wert ab)
- Orden-Reinigung (-10 bis -15 Punkte, nur bei Orden-Allianz, ab Stufe 3 verweigert)
- Ruhe und Isolation (-1/Tag, nur bis Stufe 2)

**Hard Cap:** Infektionswert kann NIE unter die höchste je erreichte Stufenschwelle fallen. Die Infektion vergisst nicht.

### 2.5 Kosten-Nutzen-Matrix

> Die Tabelle muss gegen Bedingung 2 (sofortige Power Fantasy) validiert werden. JEDE Zeile ab Stufe 1 muss einen klaren, sofort erlebbaren Vorteil haben, der die Kosten aufwiegt — zumindest im Moment der Entscheidung.

| Stufe | Nutzen (sofort erlebbar) | Kosten (wachsend) | Stufe-0-Äquivalent |
|-------|-------------------------|-------------------|---------------------|
| 0 | Volle Systemeffizienz, voller Weltzugang, vollständige Alchemie-Wirkung | Kein Zugang zu Schattenfähigkeiten, keine zweite Wahrnehmungsschicht | — |
| 1 | **Schattensinne** (Exploration-Vorteil): Verstecktes sichtbar, Emotionsauren, neue Wege | Lymph -5%, Misstrauen aufmerksamer NPCs | Volle Alchemie als Alternative zu Schattensinnen |
| 2 | **Aktive Kampf-Fähigkeiten**: Schattenreflex, Schatten-Schritt — neue Kampfdimension | Lymph -15%, Cardio -10%, sichtbar infiziert, Krone distanziert | Fortgeschrittene Trainer-Fähigkeiten (Ebene 2+3) |
| 3 | **Fortgeschrittene Fähigkeiten**, +15% Melee, Tiefensicht | Alle Äste -25%, Krone feindlich, Orden jagt | Meister-Alchemie + Positionierung + Setup-Plays |
| 4 | **Apex-Fähigkeiten**, massive Kampfkraft, volle Doppelwahrnehmung | Alle Äste -40-50%, Kontrollverlust, soziale Isolation | Kein direktes Äquivalent — Stufe 0 hat dafür volle soziale Integration |

**Stufe-0-Äquivalent (neu):** Jede Schattenfieber-Stufe hat eine nicht-infizierte Alternative, die denselben Spielraum abdeckt, aber mit anderen Mitteln. Das sichert ab, dass Stufe 0 sich NIE wie "der langweilige Weg" anfühlt.

### 2.6 Weltreaktivität
- NPCs reagieren auf Infektionsstufe (Angst, Mitleid, Nützlichkeit, Feindschaft)
- Fraktionen verschieben Zugang: Orden schliesst früh, Krone später, Gilden pragmatisch
- Infizierte NPCs erkennen den Spieler ab Stufe 2+ als "einen von ihnen"
- Mögliche emergente vierte Fraktion: Untergrund der Infizierten (offene Frage für Emre/Nami)
- Umgebungseffekte: Tiere fliehen, Pflanzen reagieren (ab Stufe 3+)

### 2.7 Das Relikt: Die Lebende Krone

> CD-Entscheidung: Das Relikt dieser Iteration ist die **Lebende Krone** — ein Biotech-Artefakt aus der Ur-Bindung.

- Die Lebende Krone ist ein organisches Artefakt, das auf die kosmologische Ur-Bindung (WBB-01, Kap. 4) zurückgeht
- Sie ist LEBENDIG im wörtlichen Sinne: Sie reagiert, wächst, verändert sich — Biotech auf kosmologischer Ebene
- Fraktions-Interpretationen:
  - **Krone**: Dynastisches Erbe, Legitimation der Herrschaft, Zeichen göttlichen Auftrags
  - **Gilden**: Das wertvollste Handelsgut der Welt, Machtinstrument ohne ideologische Bindung
  - **Orden**: Erkenntniswerkzeug, Schlüssel zum Verständnis der Ur-Bindung und der Daseinsebenen
- Schattenfieber-Verbindung: Die Lebende Krone und das Schattenfieber greifen auf dasselbe "Emer-Material" zu (WBB-01, Kap. 6). Die Krone ist die kontrollierte Form, das Schattenfieber die unkontrollierte.
- Kontakt mit der Krone KANN den Infektionswert erhöhen — massiv, aber unter Bedingung 1 und 3 (Transparenz, bewusste Entscheidung)

**Offene Fragen zum Relikt:**
- [ ] Wie interagiert der Spieler physisch mit der Krone? Tragen? Berühren? Studieren? (Emre + Darius)
- [ ] Kann die Krone das Schattenfieber kontrollieren, nicht nur erhöhen? (CD-Rückfrage)
- [ ] Visuelle Erscheinung: Organisch, pulsierend, wurzelartig? (Vera)

### 2.8 Transparenz-UI (QA-Anforderung)

> Direkte Umsetzung von Bedingung 1. Dieses UI-Modul ist KEIN "nice-to-have" — es ist systemkritisch.

- **Infektionsanzeige**: Permanenter Balken/Indikator (nicht als Zahl, sondern als organische Visualisierung — passend zum Nervensystem-UI)
- **Warnhinweis**: Wenn der Spieler eine infektionssteigernde Zone betritt, Aktion ausführt oder Story-Entscheidung trifft → visueller + auditiver Cue BEVOR die Erhöhung eintritt
- **Fähigkeitskosten**: Jede Schattenfieber-Fähigkeit zeigt ihren Infektionskosten-Wert im Tooltip
- **Stufenwarnung**: Wenn der Spieler kurz vor einer neuen Stufenschwelle steht (5 Punkte entfernt), bekommt er einen besonderen Hinweis — die Schwelle ist permanent
- **Design-Vorgabe für Vera**: Die Infektionsanzeige soll sich organisch in die Nervensystem-Visualisierung einfügen. Kein separates HUD-Element, sondern Teil desselben körperlichen Systems.

### 2.9 Offene Design-Fragen (aktualisiert)

- [x] ~~Tod und Schattenfieber~~ → Tod erhöt den Wert NICHT (CD-bestätigt)
- [ ] Spezialisierungen innerhalb der Stufen (verschiedene Manifestationen) — V2-Feature?
- [ ] Interaktion mit dem Tiervolk (immun? anders infiziert?) — abhängig von Emres WBB-01
- [ ] Balancing Stufe 0 vs. Stufe 4 — Stufe-0-Äquivalent-Spalte ist ein erster Ansatz, muss durchgetestet werden (QA mit Leo)
- [ ] Kontrollverlust-Episoden (Stufe 4): Länge, Freqünz, Trigger — müssen Bedingung 3 respektieren (Spieler darf nicht das Gefühl haben, die Kontrolle "versehentlich" verloren zu haben; der Kontrollverlust muss als Konsequenz einer BEWUSST getroffenen Entscheidung lesbar sein)
- [ ] Narrativer Zustand "Schwelle" (Stufe 4): Welche Questgeber sind "echt"? Gibt es eine Metäbene, die dem Spieler Hinweise gibt? (Nami + Darius)

---

## 3. Nervensystem-Leveling

### 3.1 Systemübersicht
- Vier physiologische Äste statt klassischer Skill-Trees
- Begrenzte Leveling-Punkte pro Level-Up — Ressourcenkonkurrenz erzwingt Spezialisierung
- Visuelle Darstellung: Halbtransparente Nervensystem-Ansicht des Körpers (Biotech-Futurismus)
- Progression ist KÖRPERLICH, nicht abstrakt

### 3.2 Die vier Äste

| Ast | Systeme | Kern-Attribute | Gameplay-Effekte |
|-----|---------|---------------|-----------------|
| **Cardio/Atmung** | Herz, Lunge, Kreislauf | Ausdauer, Regeneration, Bewegung | Sprint-Dauer, Schwimmen, Ausweich-Distanz, Erholungsrate |
| **Muskel/Skelett** | Muskeln, Knochen, Sehnen | Stärke, Resistenz, Waffenhandhabung | Schadensoutput, Block-Stabilität, Tragekapazität, Waffenfreischaltung |
| **Lymph/Immun** | Immunsystem, Stoffwechsel | Alchemie-Effizienz, Gift-Resistenz, Heilung | Trank-Wirkung, Krankheitsresistenz, passive Regeneration, Schattenfieber-Unterdrückung |
| **Schatten** | Schattennervensystem | Schattensinne, Fähigkeiten, Wahrnehmung | NUR ab Infektionsstufe 1+; siehe Schattenfieber-System |

### 3.3 Trainer-System
- Fähigkeiten werden bei NPCs in der Welt gelernt, NICHT im Menu geklickt
- Jede Fraktion hat EXKLUSIVE Trainer (für bestimmte Fähigkeiten/Waffenstile)
- Trainer verlangen: Geld + Ruf + Vorbedingung (z.B. "Zeig mir, dass du parieren kannst")
- Gothic-Referenz: Die Welt ist das Klassenzimmer

### 3.4 Perks/Fähigkeiten-Prinzip
- TRANSFORMATIV, nicht numerisch — Perks verändern WIE man spielt, nicht nur Zahlenwerte
- Korrekt: "Du kannst jetzt im Sprint angreifen" / "Paraden reflektieren Projektile"
- Falsch: "+20% Schwertschaden" / "+50 HP"
- Numerische Steigerungen kommen durch die Ast-Investition selbst, nicht durch einzelne Perks

### 3.5 Offene Design-Fragen
- [ ] Punkte pro Level-Up: Feste Anzahl oder skalierend?
- [ ] Max-Level: Reicht für wie viele Äste? Empfehlung: 2 Äste voll + 1 halb ODER 3 Äste mittel
- [ ] Respec möglich? Wenn ja, unter welchen Bedingungen? (Trainer? Kosten? Einmalig?)
- [ ] Visuelle Darstellung: Wie genau sieht die Nervensystem-Ansicht im UI aus? (Vera)

---

## 4. Alchemie und Crafting

### 4.1 Design-Philosophie
- Alchemie ersetzt Magie — es ist das primäre "übernatürliche" Werkzeug für Stufe-0-Spieler
- Wenige, bedeutsame Rezepte statt endloser Crafting-Listen
- Zutaten-Beschaffung als Explorations-Motivation
- Crafting ist NICHT endlos wiederholbar (begrenzte Zutaten, keine Respawn-Pflanzen)
- **Biotech-Forschung IST gefährlich** (CD-bestätigt): Alchemie ist nicht sicher. Experimente können schiefgehen, Nebenwirkungen sind real. Das ist keine Bestrafungsmechanik, sondern Weltkonsequenz — in einer Welt, die auf einem toten Urwesen gebaut ist, ist jeder Eingriff in die Biologie ein Risiko.

### 4.2 Produktkategorien

| Kategorie | Funktion | Beispiele |
|-----------|----------|-----------|
| **Heilung** | HP-Wiederherstellung, Regeneration | Heiltrank (sofort), Regenerationstinktur (über Zeit) |
| **Combat-Buffs** | Temporäre Kampfverstärkung | Waffenöle (Elementarschaden), Reflexelixier (Parry-Window +), Stärketrank |
| **Schattenfieber-Kontrolle** | Infektionswert beeinflussen | Suppressiva (senkt Wert), Stabilisatoren (verhindert Anstieg temporär), Booster (erhöht Wert bewusst für Fähigkeits-Burst) |
| **Gifte** | Offensiv, Waffen-Applikation | Lähmendes Gift (Ausdauer-Entzug), Nervenagent (Wahrnehmungsstoerung beim Feind), Kontaktgift (Falle) |
| **Utility** | Exploration, Überleben | Nachtsicht-Tinktur, Atem-Verlängerer (Unterwasser), Klettergrip (verbesserte Haftung) |
| **Schutz** (neu) | Anti-Infektions-Präparate | Schattenresistenz-Öl (temporärer Schutz in verseuchten Zonen), Immunbooster (Infektionsanstieg halbiert für X Minuten) |

Die neue Kategorie "Schutz" ist ein direktes Ergebnis von Bedingung 3 (kein versehentliches Infizieren). Stufe-0-Spieler brauchen taktische Werkzeuge, um infektionsgefährliche Gebiete und Kämpfe zu bestreiten, OHNE sich zu infizieren. Das macht Alchemie für reine Spieler genauso wertvoll wie Schattenfieber-Fähigkeiten für infizierte Spieler.

### 4.3 Herstellungsprozess
- Zutaten finden (Exploration, Handel, Beute)
- Rezepte lernen (Trainer-Prinzip: Alchemisten-NPCs, Lore-Fragmente, Experiment)
- Herstellung an Alchemie-Stationen (feste Orte in der Welt, NICHT tragbar)
- Qualitätsstufen: Basis → Verbessert → Meister (abhängig von Lymph-Ast und Trainer-Rang)

### 4.4 Schnittstelle zu anderen Systemen
- **Lymph-Ast:** Bestimmt Trank-Wirkung und verfügbare Rezepte
- **Schattenfieber:** Suppressiva als wichtigste Produktkategorie; hoher Infektionswert = schwächere Alchemie-Wirkung (Trade-Off!)
- **Combat:** Waffenöle und Gifte als taktische Vorbereitung vor Kämpfen
- **Fraktionen:** Exklusive Rezepte pro Fraktion (Orden: Reinigungsmittel, Gilden: Handelsgifte, Krone: Militärtränke)
- **Stufe-0-Spielpfad:** Schutz-Kategorie als mechanisches Äquivalent zu Schattenfieber-Resistenz (QA-validiert)

### 4.5 Offene Design-Fragen
- [ ] Rezeptanzahl für den Vertical Slice? Empfehlung: 15-20 Basisrezepte
- [ ] Experiment-System: Kann der Spieler Zutaten frei kombinieren? Oder nur bekannte Rezepte?
- [ ] Suchtmechanik: Haben Combat-Buffs Nebenwirkungen bei Überkonsum? (passt zur Briefing-Referenz "Echte Drogen, Amphetamine")
- [ ] Tiervolk als Alchemie-Händler: Exklusive Zutaten? Andere Tradition?

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
- Stufe 1+: Schattensinne enthüllen versteckte Objekte, Geheimgänge, vergiftete Gegenstände
- Stufe 2+: Emotionsauren an NPCs, Tiefensicht für Schatzsuche
- Die Welt hat ZWEI Schichten — und Schattenfieber zeigt die zweite
- **Stufe-0-Alternative**: Alchemie (Nachtsicht-Tinktur), genaue Beobachtung, NPC-Hinweise — andere Methode, gleicher Inhalt (QA-validiert)

### 5.5 Points of Interest (Typen)

| Typ | Beispiele | Belohnung |
|-----|----------|-----------|
| **Siedlungen** | Städte, Dörfer, Einzelhöfe | NPCs, Quests, Trainer, Handel |
| **Dungeons** | Katakomben, Minen, Ruinen, Ordensfestungen | Ausrüstung, Lore, Boss-Gegner |
| **Schattenfieber-Zonen** | Verseuchte Gebiete, Ritualstätten | Infektionsrisiko (mit Vorwarnung!), seltene Alchemie-Zutaten, Lore |
| **Landmarken** | Aussichtspunkte, Statuen, Ruinen | Kartenenthülllung, Orientierung, Lore |
| **Verstecke** | Schmugglerlager, Diebesverstecke, Tiervolk-Lager | Handel (Schwarzmarkt), Quests, Alchemie |

### 5.6 Offene Design-Fragen
- [ ] Schnellreise: Ja/Nein? Wenn ja, unter welchen Bedingungen? Empfehlung: Erst im zweiten Akt, als narrative Belohnung
- [ ] Karte: Wie viel zeigt die Spielerkarte? Empfehlung: Handgezeichnet, wird durch Exploration aufgedeckt
- [ ] Tages-/Nachtzyklus: Welche Gameplay-Auswirkungen? NPC-Routinen, Gegnerverhalten, Schattenfieber-Intensität?
- [ ] Wetter: Reiner Atmosphäre-Effekt oder Gameplay-relevant? (z.B. Regen = besseres Schleichen, Nebel = eingeschränkte Sicht)

---

## 6. Querschnittsthemen

### 6.1 Namenssysteme

> CD-Entscheidung: RELICS verwendet eigene Namenssysteme, KEINE nordisch/germanischen Namen in der Spielwelt.

- Fraktionen, Orte, Charaktere und Artefakte tragen eigene Namen, die zur Welt gehören
- Germanische Mythologie ist INSPIRATION, nicht Vorlage für die Nomenklatur
- Emres WBB-01 nutzt nordische Begriffe (Emer, Ginnungagap, etc.) als Arbeitsbegriffe — diese müssen VOR der V1-Produktion durch RELICS-eigene Namen ersetzt werden
- **Auswirkung auf GDD-02**: Stufennamen ("Rein", "Gezeichnet", "Infiziert", "Verwandelt", "Entfesselt") sind Arbeitsnamen und müssen geprüft werden — passen sie zum eigenen Namenssystem?
- **Zuständig**: Emre (Namenssystem-Framework) + Nami (Charakternamen) + Darius (Systemnamen)

### 6.2 Build-Archetypen (emergent, nicht vordefiniert)

| Build | Schattenfieber | Schwerpunkte | Spielstil |
|-------|---------------|-------------|-----------|
| Reiner Krieger | Stufe 0 | Muskel + Cardio | Schwere Waffen, Ausdauer, volles Parry |
| Alchemist | Stufe 0-1 | Lymph + Cardio | Trank-fokussiert, Gifte, Buff-Öle, Schutz-Präparate |
| Schattenspäther | Stufe 1-2 | Schatten + Cardio | Exploration, Stealth, Schatten-Schritt |
| Hybrid-Kämpfer | Stufe 2-3 | Muskel + Schatten | Risk/Reward, explosive Spitzen |
| Schattenbestie | Stufe 3-4 | Schatten (voll) | Glass Cannon, sozialer Aussenseiter, Parallel-Narrativ |

### 6.3 System-Interaktionen

```
COMBAT <-> SCHATTENFIEBER
  Schattenreflex erweitert Parry
  Fieber-Puls als Aö (kostet HP)
  Infizierte Feinde = Vorschau eigener Fähigkeiten
  Schutz-Alchemie als Stufe-0-Alternative (QA)

SCHATTENFIEBER <-> NERVENSYSTEM
  Vierter Ast konkurriert um Leveling-Punkte
  Hohe Infektion = schwache konventionelle Äste
  Spezialisierung vs. Breite

ALCHEMIE <-> SCHATTENFIEBER
  Suppressiva senken Infektionswert
  Booster erhöhen ihn bewusst
  Schutz-Präparate verhindern Anstieg (Stufe-0-Werkzeug)
  Lymph-Ast bestimmt Alchemie-Effizienz

EXPLORATION <-> SCHATTENFIEBER
  Verseuchte Zonen erhöhen Infektion (MIT Vorwarnung)
  Schattensinne enthüllen versteckte Inhalte
  Stufe-0-Alternative: Alchemie + Beobachtung
  Exploration belohnt mit Alchemie-Zutaten

FRAKTIONEN <-> SCHATTENFIEBER
  Infektionsstufe beeinflusst Fraktionszugang
  Exklusive Trainer/Rezepte pro Fraktion
  Orden bietet Reinigung, jagt aber ab Stufe 3

NARRATIV <-> SCHATTENFIEBER (Nami-Sync)
  Rauschen: Subtile Textverschiebungen (Stufe 1-2)
  Risse: Alternative Dialoge, fragwürdige Questgeber (Stufe 3)
  Schwelle: Parallel-Narrativ, unentscheidbare Realität (Stufe 4)
  Schattenfieber-Dialoge sind spielbar, nicht nur atmosphärisch
```

### 6.4 Balancing-Leitlinien
- Stufe 0 = gleichwertig zu Stufe 4 — ANDERE Erfahrung, nicht schlechtere
- Keine "Best Build"-Situation — Trade-Offs müssen echt sein
- Die Welt-Schwierigkeit wird durch Geographie bestimmt, nicht durch Slider
- Vertikaler Fortschritt (mächtig werden) UND horizontaler Fortschritt (anders werden)
- Stufe-0-Äquivalent-Tabelle (2.5) als Balancing-Grundlage
- QA-Schleife: Leo prüft jede Mechanik aus Spielersicht — 40% Fokus auf Schattenfieber

### 6.5 QA-Risikomatrix (Leo-Input)

| Risiko | Schwere | Wahrscheinlichkeit | Mitigation |
|--------|---------|---------------------|------------|
| Versehentliche Infektion | KRITISCH | Hoch (ohne Massnahmen) | Bedingung 3 + Schutz-Alchemie + UI-Warnungen |
| Stufe 0 fühlt sich leer an | HOCH | Mittel | Stufe-0-Äquivalente, exklusive Alchemie-Inhalte |
| Stufenübergänge fühlbar machen | HOCH | Hoch | Gradueller Übergang, QA pro Infektionswert |
| Kontrollverlust frustriert statt fasziniert | MITTEL | Mittel | Transparenz, Spieler muss Konsequenz vorher verstehen |
| Community-Backlash "nicht heilbar" | MITTEL | Sicher | Transparente Kommunikation VOR Release, "kontrollierbar" als Frame |
| Schattenfieber-Dialoge brechen Quests | HOCH | Hoch | Systematisches Testing aller Quest-States x Infektionsstufen |

---

## 7. Zusammenfassung: Nächste Schritte

| Aufgabe | Verantwortlich | Timeline | Status |
|---------|---------------|---------|--------|
| QA-Schleife: Spielerperspektive auf GDD-02 | Darius + Leo | Tag 2 Nachmittag | ERLEDIGT (V0.5) |
| Schattenfieber-Stufen-Mapping mit Nami | Darius + Nami | Tag 2 Nachmittag | ERLEDIGT (V0.5) |
| Schutz-Alchemie-Kategorie mit Nami validieren (narrativer Sinn) | Darius + Nami | Tag 3 | Offen |
| Lebende Krone: Interaktionsdesign | Darius + Emre | Tag 3 | Offen |
| RELICS-eigene Namenssysteme | Emre + Nami + Darius | Tag 3-4 | Offen |
| Combat-Detail: Waffenklassen-Movesets | Darius | Tag 3 (V1) | Offen |
| Alchemie-Rezeptliste (V1) inkl. Schutz-Kategorie | Darius | Tag 3 (V1) | Offen |
| Balancing-Framework (Stufe 0 vs. Stufe 4) | Leo + Darius | Tag 3 (V1) | Vorbereitet (Äquivalent-Tabelle) |
| Kontrollverlust-Episoden: Detail-Design | Darius + Vera + Tobi | Tag 4 | Offen |
| Transparenz-UI: Wireframes | Vera + Darius | Tag 4 | Offen |

---

*Darius Engel, Game Design Corner, Tag 2 Nachmittag — V0.5 nach QA-Schleife mit Leo und Stufen-Sync mit Nami*
*Leo Fischer, Tag 5 Nachmittag — V0.5.1: Ymir → Emer (Kap. 2.7 + 6.1)*
