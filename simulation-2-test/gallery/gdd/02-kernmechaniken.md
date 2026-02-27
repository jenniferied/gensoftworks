# GDD-02: Kernmechaniken

**Autor:** Darius Engel, Game Director
**QA:** Leo Brandt (Spielermarkt & Community)
**Narrativ-Sync:** Nami Osei (Erzaehlkonzept)
**Version:** V0.5 (Tag 2, Dienstag — Nachmittags-Ueberarbeitung)
**Status:** Zwischen Outline und V1 — Strukturen stehen, Schluesselabschnitte angereichert, offene Fragen reduziert
**Aenderungslog:**
- V1-Outline (Tag 2 Vormittag): Kapitelstruktur + Kernpunkte
- V0.5 (Tag 2 Nachmittag): Leos QA-Bedingungen integriert, Schattenfieber-Stufen-Mapping mit Nami synchronisiert, CD-Entscheidungen eingearbeitet (Tod/Infektion, Lebende Krone, Namenssysteme, Combat-Skill-Ceiling)

---

## 1. Combat-System

### 1.1 Grundphilosophie
- Real-time Action, Melee-fokussiert, gewichtig
- KEIN Difficulty Slider — die Welt bestimmt die Schwierigkeit (Gothic-Prinzip)
- Skill-Ceiling als Spektrum (CD-bestaetigt): Einstieg intuitiv, Mastery belohnend — nie erzwungen
- Jeder Kampf soll sich BEDEUTSAM anfuehlen — keine Trash-Mobs, kein Grind
- Spieler-Fantasie: "Ich habe diesen Kampf gewonnen, weil ich besser geworden bin — nicht weil ich Level 50 bin."

**Skill-Ceiling-Spektrum (Detail):**
Das System muss auf BEIDEN Enden des Spektrums funktionieren. Ein Spieler, der nur Basisaktionen nutzt, soll jede Begegnung bestehen koennen (mit Vorbereitung und Geduld). Ein Spieler, der Cancel-Windows und Setup-Plays beherrscht, soll sich belohnt fuehlen (schnellere Kills, elegantere Loesungen, optionale Herausforderungen). Kein Spieler soll das Gefuehl haben, er muesste Mastery-Techniken lernen, um weiterzukommen. Aber jeder Spieler soll sehen KOENNEN, was moeglich waere.

### 1.2 Kampfschichten (drei Ebenen)

#### Ebene 1 — Basis (sofort zugaenglich)
- Leichter Angriff, schwerer Angriff, Block, Ausweichen
- Ausdauer-Management: Jede Aktion kostet Ausdauer, Uebertreiben wird bestraft
- Ziel-Lock-On optional (nicht erzwungen)
- Jeder Spieler kann sofort kaempfen — Gothic-Gewicht, Skyrim-Zugaenglichkeit

#### Ebene 2 — Fortgeschritten (erlernt durch Trainer + Uebung)
- Parade/Riposte: Praezises Timing-Fenster, belohnt mit Gegenangriff
- Positionierung: Flankenangriffe, Rueckenattacken, Hoehenvorteile (Vertikalitaet!)
- Waffenspezifische Kombos: Abhaengig von Waffenklasse, erlernt bei Trainern
- Umgebungsinteraktion: Objekte treten/werfen, Engstellen nutzen, Gegner in Fallen locken

#### Ebene 3 — Mastery (belohnend, nie erzwungen)
- Cancel-Windows: Fortgeschrittene Spieler koennen Animationen unterbrechen fuer Feints
- Setup-Plays: Alchemie-Vorbereitung (Oele, Gifte) + Positionierung + Timing als koordinierte Strategie
- Schattenfieber-Combat-Integration: Schattenreflex (erweitertes Parry-Window), Fieber-Puls (AoE, kostet HP)
- Perfekte Paraden: Winzigstes Timing-Fenster, maximal belohnend (Spezial-Riposte)

### 1.3 Waffenklassen (vorlaeufig)
- **Schwerter** (Einhand/Zweihand): Allrounder, mittlere Geschwindigkeit, ausgewogenes Moveset
- **Aexte/Haemmer** (Einhand/Zweihand): Langsam, hoher Schaden, Schildbrecher
- **Dolche/Kurzwaffen**: Schnell, niedriger Einzelschaden, Combo-orientiert, Giftapplikation
- **Boegen**: Ranged, Haltungsschaden, kein Hauptwaffen-Fokus (Unterstuetzung)
- **Armbrueste**: Schwerer Ranged-Schaden, lange Nachladezeit, Situationswaffe
- **Schilde**: Defensiv, Block-Effizienz, Schildstoss als Unterbrechung

**Offene Frage:** Waffenklassen-Anzahl fuer den Vertical Slice? Empfehlung: 3-4 Nahkampf + 1 Ranged fuer V1.

### 1.4 Feinddesign-Prinzipien
- Feinde haben EIGENE Movesets, nicht nur skalierte Spieler-Angriffe
- Feindtypen definiert durch Verhalten, nicht nur durch Werte: Aggressive, Defensive, Taktiker, Infizierte
- Infizierte Feinde nutzen Schattenfieber-Faehigkeiten — Vorschau fuer den Spieler ("Das koennte ICH auch")
- Keine Level-Skalierung: Gebiete haben feste Feindstaerke. Manche Gegner sind zu frueh zu stark. Komm spaeter wieder.

### 1.5 Tod und Konsequenz
- Tod ist ein Rueckschlag, kein Game Over — Checkpoint-System mit fairen Abstaenden
- Keine Erfahrungspunkt-Strafe bei Tod
- **Tod beeinflusst den Infektionswert NICHT** (CD-bestaetigt). Begruendung: Tod ist bereits Strafe genug. Infektionsanstieg bei Tod wuerde Risk/Reward des Schattenfieber-Systems untergraben und die bewusste Entscheidung zur Nutzung verwischen.
- Konsequenz durch WELT-Reaktion: Bestimmte Situationen veraendern sich bei erneutem Versuch (NPC-Kommentare, veraenderte Wachpositionen)

---

## 2. Schattenfieber-System

> **QA-Einschaetzung (Leo):** 40% des QA-Aufwands entfaellt auf das Schattenfieber-System. Es ist gleichzeitig groesster USP und groesstes Risiko. Die folgenden drei nicht-verhandelbaren Bedingungen sind das Ergebnis von Leos Community- und Marktanalyse.

### 2.1 Drei Nicht-Verhandelbare Bedingungen (QA-validiert)

Diese drei Bedingungen haben Veto-Recht ueber jede Schattenfieber-Designentscheidung. Wenn ein Feature eine dieser Bedingungen verletzt, wird es geaendert oder gestrichen — ohne Ausnahme.

**Bedingung 1: TRANSPARENZ VOR INFEKTION**
- Der Spieler muss JEDERZEIT wissen, welche Aktion seinen Infektionswert erhoehen kann und um wie viel
- Keine versteckten Infektionsquellen. Keine "Ueberraschung, du bist jetzt infiziert"
- UI-Feedback: Klarer Indikator wenn der Spieler sich in einer infektionserhoehenden Situation befindet (visuell, auditiv, haptisch)
- Infektionserhoehende Aktionen muessen eine explizite Bestaetigung haben ODER einen klar wahrnehmbaren Moment der bewussten Entscheidung bieten
- **Goldstandard**: Bloodborne Insight — der Spieler sammelt Insight durch spezifische, erkennbare Aktionen (Bosse sehen, Madman's Knowledge nutzen). Es gibt keine versehentliche Insight-Erhoehung
- **Anti-Referenz**: Skyrim Vampirismus — Infektion passiert im Kampf durch einen zufaelligen Statuseffekt, den Spieler oft nicht bemerken. Der haeufigste Community-Complaint: "Ich wusste nicht, dass ich Vampir werde"

**Bedingung 2: SOFORTIGE POWER FANTASY NACH INFEKTION**
- Ab dem ERSTEN PUNKT Infektionswert muss der Spieler etwas Cooles koennen, das er vorher nicht konnte
- Kein "Stufe 1 ist nur Nachteile, die guten Sachen kommen spaeter" — das widerspricht der Kernfantasie
- Schattensinne (Stufe 1) muessen sofort als Upgrade erlebbar sein: Verstecktes sehen, Emotionen lesen, eine ZWEITE SCHICHT der Welt wahrnehmen
- Der Spieler soll nach der ersten Infektion denken: "Das war es wert. Was kommt noch?"
- **Goldstandard**: Bloodborne — der erste Insight-Punkt zeigt sofort die Puppe im Hunter's Dream. Die Welt veraendert sich. Der Spieler fuehlt sich belohnt.

**Bedingung 3: KEIN VERSEHENTLICHES INFIZIEREN**
- Infektion darf NIEMALS durch Zufall, Unachtsamkeit oder unklare Mechaniken passieren
- Jeder Infektionspunkt muss auf eine BEWUSSTE SPIELERENTSCHEIDUNG zurueckfuehrbar sein
- Kampf gegen Infizierte = Infektionsrisiko? Dann muss das VOR dem Kampf klar kommuniziert werden, und der Spieler muss eine taktische Wahl haben (Distanzwaffen, Alchemie-Schutz, Umgehen)
- Story-Events, die Infektion erhoehen: Muessen als Entscheidung praesentiert werden, nicht als Cutscene-Zwang
- **Design-Test**: Wenn ein Spieler nach 20 Stunden sagt "Ich wollte Stufe 0 bleiben, aber irgendwie bin ich Stufe 2" — dann haben wir versagt

### 2.2 Systemuebersicht
- Permanenter Infektionswert: 0-100
- Fuenf mechanische Stufen mit spuerbaren Schwellen
- Vierter Ast im Nervensystem-Leveling (nur ab Stufe 1+)
- NICHT heilbar, nur kontrollierbar (CD-bestaetigt)
- Jede Stufe = andere Spielerfahrung, KEINE ist schlechter als die andere

### 2.3 Stufen-Mapping: Mechanik x Narrativ x Wahrnehmung

Die folgende Tabelle synchronisiert Darius' fuenf mechanische Stufen mit Namis drei narrativen Zustaenden (Rauschen, Risse, Schwelle). Die narrativen Zustaende sind KEINE separaten Systeme — sie sind die erlebbare Oberflaechenerscheinung der mechanischen Stufen.

| Mech. Stufe | Wert | Name | Narrativer Zustand (Nami) | Kern-Fantasie | Zentrale Faehigkeit | Narrative Auswirkung |
|-------------|------|------|---------------------------|---------------|---------------------|---------------------|
| 0 | 0 | Rein | Gesund | Underdog, rein menschlich | Volle Nervensystem-Effizienz, uneingeschraenkte Sozialinteraktion | Standard-Erzaehlung: klare, zuverlaessige Wahrnehmung |
| 1 | 1-25 | Gezeichnet | Rauschen | "Ich sehe, was andere nicht sehen" | Schattensinne (passiv): Verstecktes sichtbar, Emotionsauren | Subtile Textveraenderungen in Dialogen. Umgebungshinweise, die andere nicht sehen. Einzelne Worte in NPC-Saetzen verschieben sich. Spieler bemerkt es vielleicht nicht sofort. |
| 2 | 26-50 | Infiziert | Rauschen → Risse (Uebergang) | Maechtig, aber sichtbar anders | Schattenreflex, Schatten-Schritt, Schmerzunterdrueckung | Uebergangszone: Hinweise werden deutlicher, erste fragwuerdige Wahrnehmungen. Gespraechsoptionen erscheinen, die andere nicht hoeren. |
| 3 | 51-75 | Verwandelt | Risse | Kein Mensch mehr, aber maechtig | Schattenprojektion, Fieber-Puls, Tiefensicht | Alternative Dialoge mit Figuren, die moeglicherweise anders reden als erwartet. Fragwuerdige Questgeber. NPCs reagieren irritiert auf Antworten, die der Spieler fuer normal haelt. |
| 4 | 76-100 | Entfesselt | Schwelle | Das Monster — und vielleicht ist das okay | Schattenform, Fieber-Ruf, Schattenwurzeln + Kontrollverlust-Episoden | Parallel-Narrativ: Dialoge mit Figuren, die moeglicherweise nicht existieren. Daseinsebenen werden durchlaessig. Der Spieler kann nicht mehr unterscheiden, welche Gespraeche "echt" sind. |

**Uebergangs-Design:**
- Stufenuebergaenge sind KEINE harten Schalter. Der Infektionswert bestimmt die Intensitaet innerhalb einer Stufe graduell.
- Beispiel: Bei Wert 15 sind Schattensinne schwaecher als bei Wert 24. Es gibt keinen Moment, in dem alles "anspringt".
- Die narrativen Zustaende haben weiche Grenzen: "Rauschen" beginnt ab dem ersten Infektionspunkt und intensiviert sich. "Risse" setzt schrittweise ab ca. Wert 40 ein. "Schwelle" wird ab ca. Wert 70 spuerbar.
- **QA-Relevanz (Leo)**: Genau dieser graduelle Uebergang ist der Grund fuer den hohen QA-Aufwand. Jeder der ~100 Infektionswerte muss sich in der Spielerfahrung "richtig" anfuehlen.

### 2.4 Infektionsfortschritt

**Steigerung:**
- Umgebungsexposition (verseuchte Orte, Kampf gegen Infizierte) — NUR mit vorheriger Warnung (Bedingung 1+3). Der Spieler sieht/hoert/spuert, dass ein Ort verseucht ist, BEVOR er ihn betritt.
- Bewusste Nutzung (Schattenfieber-Faehigkeiten einsetzen: ~0.5-1 Punkt pro Einsatz) — jede Faehigkeitsnutzung zeigt den Infektionsanstieg im UI
- Story-Events (Schluesselmomente, Boss-Begegnungen) — IMMER als bewusste Spielerentscheidung praesentiert, nie als Cutscene-Zwang
- Kontakt mit der Lebenden Krone (siehe 2.7) — Relikt-Interaktion als hochriskante, hochbelohnende Infektionsquelle
- Tod erhoet den Infektionswert NICHT (CD-bestaetigt)

**Senkung:**
- Alchemie-Suppressiva (-3 bis -5 Punkte, teuer, Wirkung nimmt bei hohem Wert ab)
- Orden-Reinigung (-10 bis -15 Punkte, nur bei Orden-Allianz, ab Stufe 3 verweigert)
- Ruhe und Isolation (-1/Tag, nur bis Stufe 2)

**Hard Cap:** Infektionswert kann NIE unter die hoechste je erreichte Stufenschwelle fallen. Die Infektion vergisst nicht.

### 2.5 Kosten-Nutzen-Matrix

> Die Tabelle muss gegen Bedingung 2 (sofortige Power Fantasy) validiert werden. JEDE Zeile ab Stufe 1 muss einen klaren, sofort erlebbaren Vorteil haben, der die Kosten aufwiegt — zumindest im Moment der Entscheidung.

| Stufe | Nutzen (sofort erlebbar) | Kosten (wachsend) | Stufe-0-Aequivalent |
|-------|-------------------------|-------------------|---------------------|
| 0 | Volle Systemeffizienz, voller Weltzugang, vollstaendige Alchemie-Wirkung | Kein Zugang zu Schattenfaehigkeiten, keine zweite Wahrnehmungsschicht | — |
| 1 | **Schattensinne** (Exploration-Vorteil): Verstecktes sichtbar, Emotionsauren, neue Wege | Lymph -5%, Misstrauen aufmerksamer NPCs | Volle Alchemie als Alternative zu Schattensinnen |
| 2 | **Aktive Kampf-Faehigkeiten**: Schattenreflex, Schatten-Schritt — neue Kampfdimension | Lymph -15%, Cardio -10%, sichtbar infiziert, Krone distanziert | Fortgeschrittene Trainer-Faehigkeiten (Ebene 2+3) |
| 3 | **Fortgeschrittene Faehigkeiten**, +15% Melee, Tiefensicht | Alle Aeste -25%, Krone feindlich, Orden jagt | Meister-Alchemie + Positionierung + Setup-Plays |
| 4 | **Apex-Faehigkeiten**, massive Kampfkraft, volle Doppelwahrnehmung | Alle Aeste -40-50%, Kontrollverlust, soziale Isolation | Kein direktes Aequivalent — Stufe 0 hat dafuer volle soziale Integration |

**Stufe-0-Aequivalent (neu):** Jede Schattenfieber-Stufe hat eine nicht-infizierte Alternative, die denselben Spielraum abdeckt, aber mit anderen Mitteln. Das sichert ab, dass Stufe 0 sich NIE wie "der langweilige Weg" anfuehlt.

### 2.6 Weltreaktivitaet
- NPCs reagieren auf Infektionsstufe (Angst, Mitleid, Nuetzlichkeit, Feindschaft)
- Fraktionen verschieben Zugang: Orden schliesst frueh, Krone spaeter, Gilden pragmatisch
- Infizierte NPCs erkennen den Spieler ab Stufe 2+ als "einen von ihnen"
- Moegliche emergente vierte Fraktion: Untergrund der Infizierten (offene Frage fuer Emre/Nami)
- Umgebungseffekte: Tiere fliehen, Pflanzen reagieren (ab Stufe 3+)

### 2.7 Das Relikt: Die Lebende Krone

> CD-Entscheidung: Das Relikt dieser Iteration ist die **Lebende Krone** — ein Biotech-Artefakt aus der Ur-Bindung.

- Die Lebende Krone ist ein organisches Artefakt, das auf die kosmologische Ur-Bindung (WBB-01, Kap. 4) zurueckgeht
- Sie ist LEBENDIG im woertlichen Sinne: Sie reagiert, waechst, veraendert sich — Biotech auf kosmologischer Ebene
- Fraktions-Interpretationen:
  - **Krone**: Dynastisches Erbe, Legitimation der Herrschaft, Zeichen goettlichen Auftrags
  - **Gilden**: Das wertvollste Handelsgut der Welt, Machtinstrument ohne ideologische Bindung
  - **Orden**: Erkenntniswerkzeug, Schluessel zum Verstaendnis der Ur-Bindung und der Daseinsebenen
- Schattenfieber-Verbindung: Die Lebende Krone und das Schattenfieber greifen auf dasselbe "Ymir-Material" zu (WBB-01, Kap. 6). Die Krone ist die kontrollierte Form, das Schattenfieber die unkontrollierte.
- Kontakt mit der Krone KANN den Infektionswert erhoehen — massiv, aber unter Bedingung 1 und 3 (Transparenz, bewusste Entscheidung)

**Offene Fragen zum Relikt:**
- [ ] Wie interagiert der Spieler physisch mit der Krone? Tragen? Beruehren? Studieren? (Emre + Darius)
- [ ] Kann die Krone das Schattenfieber kontrollieren, nicht nur erhoehen? (CD-Rueckfrage)
- [ ] Visuelle Erscheinung: Organisch, pulsierend, wurzelartig? (Vera)

### 2.8 Transparenz-UI (QA-Anforderung)

> Direkte Umsetzung von Bedingung 1. Dieses UI-Modul ist KEIN "nice-to-have" — es ist systemkritisch.

- **Infektionsanzeige**: Permanenter Balken/Indikator (nicht als Zahl, sondern als organische Visualisierung — passend zum Nervensystem-UI)
- **Warnhinweis**: Wenn der Spieler eine infektionssteigernde Zone betritt, Aktion ausfuehrt oder Story-Entscheidung trifft → visueller + auditiver Cue BEVOR die Erhoehung eintritt
- **Faehigkeitskosten**: Jede Schattenfieber-Faehigkeit zeigt ihren Infektionskosten-Wert im Tooltip
- **Stufenwarnung**: Wenn der Spieler kurz vor einer neuen Stufenschwelle steht (5 Punkte entfernt), bekommt er einen besonderen Hinweis — die Schwelle ist permanent
- **Design-Vorgabe fuer Vera**: Die Infektionsanzeige soll sich organisch in die Nervensystem-Visualisierung einfuegen. Kein separates HUD-Element, sondern Teil desselben koerperlichen Systems.

### 2.9 Offene Design-Fragen (aktualisiert)

- [x] ~~Tod und Schattenfieber~~ → Tod erhoet den Wert NICHT (CD-bestaetigt)
- [ ] Spezialisierungen innerhalb der Stufen (verschiedene Manifestationen) — V2-Feature?
- [ ] Interaktion mit dem Tiervolk (immun? anders infiziert?) — abhaengig von Emres WBB-01
- [ ] Balancing Stufe 0 vs. Stufe 4 — Stufe-0-Aequivalent-Spalte ist ein erster Ansatz, muss durchgetestet werden (QA mit Leo)
- [ ] Kontrollverlust-Episoden (Stufe 4): Laenge, Frequenz, Trigger — muessen Bedingung 3 respektieren (Spieler darf nicht das Gefuehl haben, die Kontrolle "versehentlich" verloren zu haben; der Kontrollverlust muss als Konsequenz einer BEWUSST getroffenen Entscheidung lesbar sein)
- [ ] Narrativer Zustand "Schwelle" (Stufe 4): Welche Questgeber sind "echt"? Gibt es eine Metaebene, die dem Spieler Hinweise gibt? (Nami + Darius)

---

## 3. Nervensystem-Leveling

### 3.1 Systemuebersicht
- Vier physiologische Aeste statt klassischer Skill-Trees
- Begrenzte Leveling-Punkte pro Level-Up — Ressourcenkonkurrenz erzwingt Spezialisierung
- Visuelle Darstellung: Halbtransparente Nervensystem-Ansicht des Koerpers (Biotech-Futurismus)
- Progression ist KOERPERLICH, nicht abstrakt

### 3.2 Die vier Aeste

| Ast | Systeme | Kern-Attribute | Gameplay-Effekte |
|-----|---------|---------------|-----------------|
| **Cardio/Atmung** | Herz, Lunge, Kreislauf | Ausdauer, Regeneration, Bewegung | Sprint-Dauer, Schwimmen, Ausweich-Distanz, Erholungsrate |
| **Muskel/Skelett** | Muskeln, Knochen, Sehnen | Staerke, Resistenz, Waffenhandhabung | Schadensoutput, Block-Stabilitaet, Tragekapazitaet, Waffenfreischaltung |
| **Lymph/Immun** | Immunsystem, Stoffwechsel | Alchemie-Effizienz, Gift-Resistenz, Heilung | Trank-Wirkung, Krankheitsresistenz, passive Regeneration, Schattenfieber-Unterdrueckung |
| **Schatten** | Schattennervensystem | Schattensinne, Faehigkeiten, Wahrnehmung | NUR ab Infektionsstufe 1+; siehe Schattenfieber-System |

### 3.3 Trainer-System
- Faehigkeiten werden bei NPCs in der Welt gelernt, NICHT im Menu geklickt
- Jede Fraktion hat EXKLUSIVE Trainer (fuer bestimmte Faehigkeiten/Waffenstile)
- Trainer verlangen: Geld + Ruf + Vorbedingung (z.B. "Zeig mir, dass du parieren kannst")
- Gothic-Referenz: Die Welt ist das Klassenzimmer

### 3.4 Perks/Faehigkeiten-Prinzip
- TRANSFORMATIV, nicht numerisch — Perks veraendern WIE man spielt, nicht nur Zahlenwerte
- Korrekt: "Du kannst jetzt im Sprint angreifen" / "Paraden reflektieren Projektile"
- Falsch: "+20% Schwertschaden" / "+50 HP"
- Numerische Steigerungen kommen durch die Ast-Investition selbst, nicht durch einzelne Perks

### 3.5 Offene Design-Fragen
- [ ] Punkte pro Level-Up: Feste Anzahl oder skalierend?
- [ ] Max-Level: Reicht fuer wie viele Aeste? Empfehlung: 2 Aeste voll + 1 halb ODER 3 Aeste mittel
- [ ] Respec moeglich? Wenn ja, unter welchen Bedingungen? (Trainer? Kosten? Einmalig?)
- [ ] Visuelle Darstellung: Wie genau sieht die Nervensystem-Ansicht im UI aus? (Vera)

---

## 4. Alchemie und Crafting

### 4.1 Design-Philosophie
- Alchemie ersetzt Magie — es ist das primaere "uebernatuerliche" Werkzeug fuer Stufe-0-Spieler
- Wenige, bedeutsame Rezepte statt endloser Crafting-Listen
- Zutaten-Beschaffung als Explorations-Motivation
- Crafting ist NICHT endlos wiederholbar (begrenzte Zutaten, keine Respawn-Pflanzen)
- **Biotech-Forschung IST gefaehrlich** (CD-bestaetigt): Alchemie ist nicht sicher. Experimente koennen schiefgehen, Nebenwirkungen sind real. Das ist keine Bestrafungsmechanik, sondern Weltkonsequenz — in einer Welt, die auf einem toten Urwesen gebaut ist, ist jeder Eingriff in die Biologie ein Risiko.

### 4.2 Produktkategorien

| Kategorie | Funktion | Beispiele |
|-----------|----------|-----------|
| **Heilung** | HP-Wiederherstellung, Regeneration | Heiltrank (sofort), Regenerationstinktur (ueber Zeit) |
| **Combat-Buffs** | Temporaere Kampfverstaerkung | Waffenoele (Elementarschaden), Reflexelixier (Parry-Window +), Staerketrank |
| **Schattenfieber-Kontrolle** | Infektionswert beeinflussen | Suppressiva (senkt Wert), Stabilisatoren (verhindert Anstieg temporaer), Booster (erhoeht Wert bewusst fuer Faehigkeits-Burst) |
| **Gifte** | Offensiv, Waffen-Applikation | Laehmendes Gift (Ausdauer-Entzug), Nervenagent (Wahrnehmungsstoerung beim Feind), Kontaktgift (Falle) |
| **Utility** | Exploration, Ueberleben | Nachtsicht-Tinktur, Atem-Verlaengerer (Unterwasser), Klettergrip (verbesserte Haftung) |
| **Schutz** (neu) | Anti-Infektions-Praeparate | Schattenresistenz-Oel (temporaerer Schutz in verseuchten Zonen), Immunbooster (Infektionsanstieg halbiert fuer X Minuten) |

Die neue Kategorie "Schutz" ist ein direktes Ergebnis von Bedingung 3 (kein versehentliches Infizieren). Stufe-0-Spieler brauchen taktische Werkzeuge, um infektionsgefaehrliche Gebiete und Kaempfe zu bestreiten, OHNE sich zu infizieren. Das macht Alchemie fuer reine Spieler genauso wertvoll wie Schattenfieber-Faehigkeiten fuer infizierte Spieler.

### 4.3 Herstellungsprozess
- Zutaten finden (Exploration, Handel, Beute)
- Rezepte lernen (Trainer-Prinzip: Alchemisten-NPCs, Lore-Fragmente, Experiment)
- Herstellung an Alchemie-Stationen (feste Orte in der Welt, NICHT tragbar)
- Qualitaetsstufen: Basis → Verbessert → Meister (abhaengig von Lymph-Ast und Trainer-Rang)

### 4.4 Schnittstelle zu anderen Systemen
- **Lymph-Ast:** Bestimmt Trank-Wirkung und verfuegbare Rezepte
- **Schattenfieber:** Suppressiva als wichtigste Produktkategorie; hoher Infektionswert = schwaechere Alchemie-Wirkung (Trade-Off!)
- **Combat:** Waffenoele und Gifte als taktische Vorbereitung vor Kaempfen
- **Fraktionen:** Exklusive Rezepte pro Fraktion (Orden: Reinigungsmittel, Gilden: Handelsgifte, Krone: Militaertraenke)
- **Stufe-0-Spielpfad:** Schutz-Kategorie als mechanisches Aequivalent zu Schattenfieber-Resistenz (QA-validiert)

### 4.5 Offene Design-Fragen
- [ ] Rezeptanzahl fuer den Vertical Slice? Empfehlung: 15-20 Basisrezepte
- [ ] Experiment-System: Kann der Spieler Zutaten frei kombinieren? Oder nur bekannte Rezepte?
- [ ] Suchtmechanik: Haben Combat-Buffs Nebenwirkungen bei Ueberkonsum? (passt zur Briefing-Referenz "Echte Drogen, Amphetamine")
- [ ] Tiervolk als Alchemie-Haendler: Exklusive Zutaten? Andere Tradition?

---

## 5. Exploration und Weltnavigation

### 5.1 Weltstruktur
- Semi-Open-World: Eine zusammenhaengende Kernregion (~4-6 km²)
- Gothic-Dichte: Wenig Leerraum, hohe POI-Dichte, handplatziert
- Keine Schnellreise (oder: spaet freischaltbar, als Luxus, nicht als Notwendigkeit)
- Zusammenhaengende Oberwelt ohne Ladebildschirme

### 5.2 Vertikalitaet
- Staedte: Begehbare Dachlandschaften, Keller, Kanalisation, Bruecken, Turmebenen
- Wildnis: Klippen, Hoehlen, Baumkronen, Flussbetten, Bergpaesse
- Immer mehrere Wege: Hauptweg (sicher, lang), Schleichweg (riskant, kurz), Vertikalweg (Geschick erforderlich)
- Dishonored-Prinzip: Der Raum hat drei Dimensionen

### 5.3 Belohnungsstruktur
- Neugier wird IMMER belohnt: Abseits der Wege = Alchemie-Zutaten, Lore-Fragmente, versteckte NPCs, Schattenfieber-Hotspots
- Keine Quest-Marker auf der Karte (oder: minimal, abschaltbar) — Beschreibungen, Sightlines, NPC-Hinweise
- Umweltpuzzles: Kombination aus Beobachtung, Alchemie und Schattensinnen
- Handplatzierte Schaetze mit narrativer Einbettung (Warum liegt das hier? Wer hat es versteckt?)

### 5.4 Sichtbarkeitsschichten (Schattenfieber-Integration)
- Stufe 0: Normale Wahrnehmung — Geheimtueren und Fallen nur durch genaues Hinsehen findbar
- Stufe 1+: Schattensinne enthuellen versteckte Objekte, Geheimgaenge, vergiftete Gegenstaende
- Stufe 2+: Emotionsauren an NPCs, Tiefensicht fuer Schatzsuche
- Die Welt hat ZWEI Schichten — und Schattenfieber zeigt die zweite
- **Stufe-0-Alternative**: Alchemie (Nachtsicht-Tinktur), genaue Beobachtung, NPC-Hinweise — andere Methode, gleicher Inhalt (QA-validiert)

### 5.5 Points of Interest (Typen)

| Typ | Beispiele | Belohnung |
|-----|----------|-----------|
| **Siedlungen** | Staedte, Doerfer, Einzelhoefe | NPCs, Quests, Trainer, Handel |
| **Dungeons** | Katakomben, Minen, Ruinen, Ordensfestungen | Ausruestung, Lore, Boss-Gegner |
| **Schattenfieber-Zonen** | Verseuchte Gebiete, Ritualstaetten | Infektionsrisiko (mit Vorwarnung!), seltene Alchemie-Zutaten, Lore |
| **Landmarken** | Aussichtspunkte, Statuen, Ruinen | Kartenenthuelllung, Orientierung, Lore |
| **Verstecke** | Schmugglerlager, Diebesverstecke, Tiervolk-Lager | Handel (Schwarzmarkt), Quests, Alchemie |

### 5.6 Offene Design-Fragen
- [ ] Schnellreise: Ja/Nein? Wenn ja, unter welchen Bedingungen? Empfehlung: Erst im zweiten Akt, als narrative Belohnung
- [ ] Karte: Wie viel zeigt die Spielerkarte? Empfehlung: Handgezeichnet, wird durch Exploration aufgedeckt
- [ ] Tages-/Nachtzyklus: Welche Gameplay-Auswirkungen? NPC-Routinen, Gegnerverhalten, Schattenfieber-Intensitaet?
- [ ] Wetter: Reiner Atmosphaere-Effekt oder Gameplay-relevant? (z.B. Regen = besseres Schleichen, Nebel = eingeschraenkte Sicht)

---

## 6. Querschnittsthemen

### 6.1 Namenssysteme

> CD-Entscheidung: RELICS verwendet eigene Namenssysteme, KEINE nordisch/germanischen Namen in der Spielwelt.

- Fraktionen, Orte, Charaktere und Artefakte tragen eigene Namen, die zur Welt gehoeren
- Germanische Mythologie ist INSPIRATION, nicht Vorlage fuer die Nomenklatur
- Emres WBB-01 nutzt nordische Begriffe (Ymir, Ginnungagap, etc.) als Arbeitsbegriffe — diese muessen VOR der V1-Produktion durch RELICS-eigene Namen ersetzt werden
- **Auswirkung auf GDD-02**: Stufennamen ("Rein", "Gezeichnet", "Infiziert", "Verwandelt", "Entfesselt") sind Arbeitsnamen und muessen geprueft werden — passen sie zum eigenen Namenssystem?
- **Zustaendig**: Emre (Namenssystem-Framework) + Nami (Charakternamen) + Darius (Systemnamen)

### 6.2 Build-Archetypen (emergent, nicht vordefiniert)

| Build | Schattenfieber | Schwerpunkte | Spielstil |
|-------|---------------|-------------|-----------|
| Reiner Krieger | Stufe 0 | Muskel + Cardio | Schwere Waffen, Ausdauer, volles Parry |
| Alchemist | Stufe 0-1 | Lymph + Cardio | Trank-fokussiert, Gifte, Buff-Oele, Schutz-Praeparate |
| Schattenspaether | Stufe 1-2 | Schatten + Cardio | Exploration, Stealth, Schatten-Schritt |
| Hybrid-Kaempfer | Stufe 2-3 | Muskel + Schatten | Risk/Reward, explosive Spitzen |
| Schattenbestie | Stufe 3-4 | Schatten (voll) | Glass Cannon, sozialer Aussenseiter, Parallel-Narrativ |

### 6.3 System-Interaktionen

```
COMBAT <-> SCHATTENFIEBER
  Schattenreflex erweitert Parry
  Fieber-Puls als AoE (kostet HP)
  Infizierte Feinde = Vorschau eigener Faehigkeiten
  Schutz-Alchemie als Stufe-0-Alternative (QA)

SCHATTENFIEBER <-> NERVENSYSTEM
  Vierter Ast konkurriert um Leveling-Punkte
  Hohe Infektion = schwache konventionelle Aeste
  Spezialisierung vs. Breite

ALCHEMIE <-> SCHATTENFIEBER
  Suppressiva senken Infektionswert
  Booster erhoehen ihn bewusst
  Schutz-Praeparate verhindern Anstieg (Stufe-0-Werkzeug)
  Lymph-Ast bestimmt Alchemie-Effizienz

EXPLORATION <-> SCHATTENFIEBER
  Verseuchte Zonen erhoehen Infektion (MIT Vorwarnung)
  Schattensinne enthuellen versteckte Inhalte
  Stufe-0-Alternative: Alchemie + Beobachtung
  Exploration belohnt mit Alchemie-Zutaten

FRAKTIONEN <-> SCHATTENFIEBER
  Infektionsstufe beeinflusst Fraktionszugang
  Exklusive Trainer/Rezepte pro Fraktion
  Orden bietet Reinigung, jagt aber ab Stufe 3

NARRATIV <-> SCHATTENFIEBER (Nami-Sync)
  Rauschen: Subtile Textverschiebungen (Stufe 1-2)
  Risse: Alternative Dialoge, fragwuerdige Questgeber (Stufe 3)
  Schwelle: Parallel-Narrativ, unentscheidbare Realitaet (Stufe 4)
  Schattenfieber-Dialoge sind spielbar, nicht nur atmosphaerisch
```

### 6.4 Balancing-Leitlinien
- Stufe 0 = gleichwertig zu Stufe 4 — ANDERE Erfahrung, nicht schlechtere
- Keine "Best Build"-Situation — Trade-Offs muessen echt sein
- Die Welt-Schwierigkeit wird durch Geographie bestimmt, nicht durch Slider
- Vertikaler Fortschritt (maechtig werden) UND horizontaler Fortschritt (anders werden)
- Stufe-0-Aequivalent-Tabelle (2.5) als Balancing-Grundlage
- QA-Schleife: Leo prueft jede Mechanik aus Spielersicht — 40% Fokus auf Schattenfieber

### 6.5 QA-Risikomatrix (Leo-Input)

| Risiko | Schwere | Wahrscheinlichkeit | Mitigation |
|--------|---------|---------------------|------------|
| Versehentliche Infektion | KRITISCH | Hoch (ohne Massnahmen) | Bedingung 3 + Schutz-Alchemie + UI-Warnungen |
| Stufe 0 fuehlt sich leer an | HOCH | Mittel | Stufe-0-Aequivalente, exklusive Alchemie-Inhalte |
| Stufenuebergaenge fuehlbar machen | HOCH | Hoch | Gradueller Uebergang, QA pro Infektionswert |
| Kontrollverlust frustriert statt fasziniert | MITTEL | Mittel | Transparenz, Spieler muss Konsequenz vorher verstehen |
| Community-Backlash "nicht heilbar" | MITTEL | Sicher | Transparente Kommunikation VOR Release, "kontrollierbar" als Frame |
| Schattenfieber-Dialoge brechen Quests | HOCH | Hoch | Systematisches Testing aller Quest-States x Infektionsstufen |

---

## 7. Zusammenfassung: Naechste Schritte

| Aufgabe | Verantwortlich | Timeline | Status |
|---------|---------------|---------|--------|
| QA-Schleife: Spielerperspektive auf GDD-02 | Darius + Leo | Tag 2 Nachmittag | ERLEDIGT (V0.5) |
| Schattenfieber-Stufen-Mapping mit Nami | Darius + Nami | Tag 2 Nachmittag | ERLEDIGT (V0.5) |
| Schutz-Alchemie-Kategorie mit Nami validieren (narrativer Sinn) | Darius + Nami | Tag 3 | Offen |
| Lebende Krone: Interaktionsdesign | Darius + Emre | Tag 3 | Offen |
| RELICS-eigene Namenssysteme | Emre + Nami + Darius | Tag 3-4 | Offen |
| Combat-Detail: Waffenklassen-Movesets | Darius | Tag 3 (V1) | Offen |
| Alchemie-Rezeptliste (V1) inkl. Schutz-Kategorie | Darius | Tag 3 (V1) | Offen |
| Balancing-Framework (Stufe 0 vs. Stufe 4) | Leo + Darius | Tag 3 (V1) | Vorbereitet (Aequivalent-Tabelle) |
| Kontrollverlust-Episoden: Detail-Design | Darius + Vera + Tobi | Tag 4 | Offen |
| Transparenz-UI: Wireframes | Vera + Darius | Tag 4 | Offen |

---

*Darius Engel, Game Design Corner, Tag 2 Nachmittag — V0.5 nach QA-Schleife mit Leo und Stufen-Sync mit Nami*
