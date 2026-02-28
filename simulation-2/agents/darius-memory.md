# Darius — Memory

<!-- Nur der Agent selbst schreibt in diese Datei. GM fasst Memories NICHT an. -->

## Tag 1 — Szene 2 (10:00 Uhr, Montag)

**Gelesen:**
- Deus Ex "Shooter: Majestic Revelations" v5.3e (Ion Storm, 1997) — Warren Spectors annotiertes GDD
- Diablo Pitch Document (Condor, 1994)

**Kernerkenntnisse aus der Recherche:**
- Spector beginnt mit einem philosophischen High Concept, das alle Systeme ableitet — das will ich für RELICS übernehmen
- "Deep Simulation of Small Environments" > riesige, flache Open World. Gothic-Prinzip bestätigt.
- Skill-Granularität ist ein bekanntes Problem: Deus Ex löst es mit 4 Qualitätsstufen statt 1-100-Skalen — mein Referenzmodell für das Nervensystem-Leveling
- Diablo zeigt: ein klares "Game Feel"-Statement schlägt jede Mechanik-Beschreibung

**Erste Designentscheidungen (vorläufig):**
- Nervensystem-Leveling: 3 Subsysteme (Cardio, Muskel, Lymph), Use-based Progression, 4 Qualitätsstufen
- Materialklasse als echte Gameplay-Variable, nicht nur Kosmetik
- Fraktionsruf = Ressourcenzugang (Krone: Territorium/Passagen, Gilden: Materialien/Rezepturen, Orden: Wissen/Fertigkeitsbücher)
- Design-Säulen Erstentwurf: Immersive Simulation / Fraktionspolitik / Körperlicher Fortschritt / Dichte vor Breite

**Produzierte Artefakte:**
- `simulation-2/gallery/gdd/00-recherche-notizen-darius.md` — Recherche-Notat, Tag 1

---

## Tag 2 — Szene 1 (09:00 Uhr, Dienstag) — Briefing Küche

**CD-Feedback (via Finn):**
- Schattenfieber: EINE biologische Wahrheit. Fraktionen interpretieren es verschieden — verschieden falsch, verschieden nah dran. Harter Kern muss definiert werden.
- Relikt: CD dreht Frage zurück. Vorschläge + Bilder gewünscht. Vera produziert, Darius/Emre/Nami denken mit.
- Release-Modell: Alpha (Streamer), Beta (max. 6–12 Monate), Full Release, dann große DLCs — keine kleinen Add-ons.

**Meine Reaktionen / Positionen:**
- Schattenfieber biologisch = perfekt. Passt zu "keine klassische Magie". Ermöglicht Lymph-Subsystem-Mechanik.
- Relikt-Vorschlag: Resonanzobjekt / Schwellenanker, das auf den biologischen Zustand des Spielers reagiert.
- Release-Modell: Erste Stunde des Spiels muss stehen, wenn wir in die Streamer-Alpha gehen. Scope-Priorität.

---

## Tag 2 — Szene 2 (10:00 Uhr, Dienstag) — WORK

### Gelesene / verwendete Quellen heute:
- Emres Briefing-Output (Tag 2, Szene 1): Schattenfieber als biologisches Durchsickern, vier Stadien (Rauschen / Risse / Schwelle / Übergang), Schwellenanker-Konzept
- Emres Topos-Skizze (Transcript): Schwellenstadt auf Felssporn, vier vertikale Schichten, sieben Landmarken
- Namis Briefing-Output (Tag 2, Szene 1): Fremder als Erzählprinzip, Fragment-Szene, Relikt zieht den Spieler an
- Leos Recherche (Tag 1): Vier Zielgruppen, kritische Risiken, "erste Stunde ist Angebot"
- Deus Ex GDD v5.3e (Titelseite, Marketing-Section) — High Concept Struktur nochmals bestätigt

### Produzierte Artefakte:
- `simulation-2/gallery/gdd/01-spieluebersicht-v1.md` — GDD Kapitel 1, erster vollständiger Entwurf

### Vier offene Fragen — BEANTWORTET (Stand 10:00 Uhr):
1. **Stadtfrage:** EINE vertikale Stadt (Emres Schwellenstadt, Felssporn, vier Schichten). Stadtname: **Schwarzrand** (Emre, WBB Kap. 1). GDD Kap. 1 muss noch mit Namen aktualisiert werden.
2. **Schattenfieber-Scope:** Hauptquest-antreibend + dritte Progressionsachse (Lymph-Subsystem, vier Stadien nach Emres Lore). Drei Fraktions-Antworten = drei Gameplay-Pfade. Integriert in GDD Kap. 1.
3. **Tiervolk:** NPC — Händler und Informationsbroker, nicht spielbar. Leicht alien, nicht tribal. Eigene Händler-Netzwerke parallel zu den Gilden. (Briefing bestätigt.)
4. **Release-Modell:** Main → Streamer-Alpha → Beta (max. 6–12 Monate) → Full Release → große DLCs. Keine kleinen Add-ons. (Finn, Tag 2 Szene 1, bestätigt.)

### Offene Abhängigkeiten für Kapitel 2 (Kernmechaniken):
- **Skill-by-Use vs. Grind:** Sync mit Leo heute Nachmittag (20 Minuten, geplant)
- **Fraktionsruf-Schwellenwerte:** Emres Gilden-Monopolstruktur in WBB Kap. 1 ist jetzt da — verwenden für Kapitel 2
- **Relikt-Gameplay-Funktion:** Nami und ich klären 14:00 in Kapitel 3 — was tut die Wurzel in der Hand des Spielers?
- **Stadtname-Update:** "Schwarzrand" in GDD Kap. 1 eintragen (nächste Revision)

---

## Tag 2 — Szene 3 (13:00 Uhr, Dienstag) — MEETING Küche

### Was ich im Meeting gesagt habe:
- GDD Kap. 1 bestätigt fertig gemeldet
- Vier offene Fragen öffentlich beantwortet (Stadtname, Schattenfieber, Tiervolk, Release)
- "Schwarzrand" positiv bewertet: funktioniert als Stimmungs-Statement für erste Spielminute
- Namis Salva (Tiervolk/vierte Kosmologie) als Immersive-Sim-Erzählmechanismus gelobt
- Forderung an Nami für 14:00: Spieler-Fantasie-Frage zur Hieronymus-Vael-Eröffnungsszene — was tut der Spieler aktiv?

### Neu bestätigte Fakten aus dem Meeting:
- **Stadtname: Schwarzrand** — Konsens im Team
- Emres WBB Kap. 1 (Mythos) ist fertig: Kosmologie, drei Schöpfungsmythen, historischer Wendepunkt "Die Öffnung", Gilden-Monopolstruktur
- Nami hat GDD Kap. 4 fertig: 5 NPCs (Fremder, Hieronymus Vael, Adelhaid Brenn, Bruder Ivo Scherer, Vreni Kast, Salva)
- Emres Gilden-Monopolstruktur ist verfügbar — kann für Kapitel 2 (Fraktionsruf-Schwellenwerte) genutzt werden
- Widerspruchs-Log W-004: Tiervolk kosmologisch noch ungeklärt (Emre + Nami noch offen)

### Nächste Schritte:
- 14:00 Sync: Nami (Fragment-Szene, Spieler-Aktivität in Eröffnung, Relikt-Entscheid)
- 14:00+ Leo-Sync: Skill-by-Use-Mechanik klären (20 Minuten)
- Dann: GDD Kapitel 2 (Kernmechaniken) beginnen — Combat, Crafting, Nervensystem-Leveling im Detail
- GDD Kap. 1 aktualisieren: Stadtname "Schwarzrand" eintragen (v2)

---

## Tag 2 — Szene 4 (14:00 Uhr, Dienstag) — PAUSE Küche

### Smalltalk mit Emre:
- Emre hat "Schwarzrand" beim Spazierengehen im Teutoburger Wald gefunden — Waldrand über dem Talkessel. Auch Barcelona, Barri Gotic.
- Ich habe Gelsenkirchen-Bezug hergestellt: Schwarzrand als Ruhrpott-Bild, Nebel auf Fördertürmen, Vater bei ThyssenKrupp.
- Lena erwähnt (fragt warum der Spielname gut ist — Zollverein als Antwort).
- Emres Katze Nerevar hat ihn beim Laptop-Aufmachen angestarrt.

---

## Tag 2 — Szene 5 (15:00 Uhr, Dienstag) — REVIEW Küche

### Teilnehmer: Vera (remote), Emre, Nami, Darius

### Was präsentiert wurde:
- **Vera:** 9 Bilder (Relikt-Zustände 0/1/3, Dreier-Vergleich, Hero Shot, drei Fraktionspaletten, Stadtschnitt)
  - Stärkstes Bild: Zustand Eins (biolumineszente Gefäßlinien, schön und unheimlich gleichzeitig)
  - Schwachstellen: Relikt-Form inkonsistent zwischen Panels, Hero Shot verliert organische Knochen-Textur, Stadtschnitt fehlt Schwarzrand-Richtungskonzept
- **Emre:** WBB Mythos v1 — Kosmologie, drei Schöpfungsmythen, historischer Wendepunkt "Die Öffnung", Gilden-Monopolstruktur
  - Stärke: Drei Mythen als drei Lesarten derselben biologischen Wahrheit = Gameplay-System, nicht nur Lore
- **Nami:** 5 NPCs und Quest-Skizzen (Intro-Quest "Was er in der Hand hielt", Hauptquest "Der Schwellenanker")
  - Stärke: Salva als vierte Kosmologie — Immersive-Sim-Erzählmechanismus, eine Stimme außerhalb der drei Fraktionslogiken

### Mein gesprochener Beitrag (Turn 4 — letzter regulärer Sprecher):
- 10 CD-Fragen auf 2 reduziert: Relikt-Name und Ablehn-Option
- Relikt-Formveränderung und Tiervolk-Kosmologie als interne Hausaufgabe deklariert (kein CD-Ticket)
- Orden-Kreuz: raus — kein CD-Entscheid nötig, Emre + Vera einig
- Hieronymus-Sterbezeit: Empfehlung "reduziert" mit Pacing-Argument für Streamer-Alpha begründet
- Klare Deadlines gesetzt: Nami Halbseite bis Mi 10:00, Emre drei Sätze Relikt-Formfrage bis Mi 10:00

### Offene CD-Fragen (nach Dringlichkeit geordnet — meine Filterung):

**PRIORITÄT 1 — Mittwoch früh ans CD:**
1. **Relikt-Name / Spieltitel-Suffix:** "Das Herz" (Fragment beim Spieler) vs. "Die Wurzel" (Ganzes in der Tiefe). In-World-Begriff "Schwellenanker" (Emre) schon da. Blockiert: Namis Act 3, Veras Hero-Shot-Iteration.
2. **Player-Agency beim Erstgespräch:** Ablehn-Option beim Fragment — ja oder nein? Wenn ja: Nami liefert Mittwoch bis 10:00 eine Halbseite mit konkreten Konsequenzen. Echte Wahlfreiheit oder Theater? Das muss feststehen.

**PRIORITÄT 2 — Emre klärt intern, bevor CD entscheidet:**
3. **Relikt-Formveränderung:** Wächst das Relikt im aktivierten Zustand physisch? Das ist eine biologische Lore-Entscheidung (Emre), keine Ästhetik-Entscheidung (Vera). Emre liefert bis Mittwoch 10:00.
4. **Tiervolk-Ursprung / Schwelle bewusst oder blind:** Kosmologie-Frage. Meine Position: Für Kapitel 2 brauche ich Tiervolk-Funktion als Händler-Typ vor der Tiervolk-Kosmologie. Emre + Nami klären intern.

**MEINE EMPFEHLUNG (kein CD-Entscheid nötig):**
5. **Düsterkeit der Intro:** Reduziert. Kurze Sterbeszene, Fragment, Clip-Moment, weiter. Zwei-bis-drei-Minuten-Sterbeszene am Anfang ist Pacing-Risiko für Streamer-Alpha.

### Was mich heute beeindruckt hat:
- Emres drei Schöpfungsmythen = direkt verwendbares Gameplay-System (drei Fraktions-Motivationsstrukturen für Kap. 2)
- Namis Salva = präzise Immersive-Sim-Figur, funktioniert weil sie außerhalb der drei Fraktionslogiken steht
- Veras Zustand-Eins-Bild = stärkstes Konzept-Bild des Tages

### Nächste Schritte:
- Nami: Halbseite Konsequenzen der Ablehn-Option bis Mittwoch 10:00
- Emre: Relikt-Formfrage (3 Sätze) + Tiervolk-Funktion bis Mittwoch 10:00
- Vera: Hero-Shot-Iteration (organische Knochen-Textur) + Stadtschnitt-Überarbeitung (Schwarzrand-Richtungskonzept)
- Ich: CD-Fragen bündeln (Mittwoch früh), dann GDD Kapitel 2 (Kernmechaniken) beginnen
- GDD Kap. 1 v2: Stadtname "Schwarzrand" eintragen — noch offen
- Leo-Sync Skill-by-Use: heute Abend noch oder Mittwoch früh

---

# Tag 3 Szene 1
**Typ**: BRIEFING | **Uhrzeit**: 09:00 | **Teilnehmer**: alle 7

## Notizen
- CD-Entscheid steht: Relikt heißt "Schwellenanker" — alle Dokumente umbenennen
- CD: Spieler darf Fragment ablehnen — Namis Terrain, Nami hat Halbseite versprochen (war fällig Di 10:00 → liegt hoffentlich vor)
- CD: Bilder müssen inline in GDD + WBB eingebettet werden — kein separater Anhang
- Gilden-Palette: Vera macht neue Iteration (zu viel Text in v1)
- Stadtschnitt: CD "wirkt unnatürlich" — Vera-Aufgabe, nicht meine

## Ergebnisse
- Mein Plan Tag 3: GDD Kap 2 (Kernmechaniken) als Hauptarbeit, Kap 3 (Erzählkonzept) mit Nami-Input, Kap 1 v2 (Schwarzrand + Schwellenanker), Kap 5 (Art Direction mit Veras Bildern)
- Kritischer Pfad: Kap 2 zuerst — das ist die Systemarbeit, die am meisten Input braucht
- Abhängigkeit Kap 5: Bildliste von Finn/Vera bis 11:00 nötig, sonst leeres Kapitel

## Offene Fragen
- Welche Bilder konkret für Kap 5? Finn + Vera müssen Bildliste bis 11:00 liefern
- Liegt Namis Ablehn-Option-Halbseite vor? (War für Mi 10:00 versprochen)
- Leo-QA-Pass auf Kap 1 v1: wann kommt das Ergebnis?

## Persönliches
- Drei Kapitel plus Revision heute ist viel — realistisch nur mit sauberen Inputs von Nami/Vera/Finn
- Schwellenanker-Entscheid vom CD ist ein Geschenk: Emre hatte den Namen schon, jetzt können wir einheitlich schreiben

---

# Tag 3 Szene 2
**Typ**: WORK | **Uhrzeit**: 10:00 | **Teilnehmer**: Darius (alleine)

## Notizen
- Gelesene Quellen: GDD Kap. 4 v1 (Nami), WBB Kap. 1 v1 (Emre), GDD Kap. 1 v1 (eigene Vorarbeit), Briefing
- Emres Schattenfieber-Stadien: In WBB v1 heißen sie Flüstern/Wandlung/Entgrenzung (3 Stufen) — nicht Rauschen/Risse/Schwelle/Übergang wie im früheren Draft. Kap. 2 und 3 verwenden Emres finale Terminologie.
- Namis Quest-Skizzen aus Kap. 4 als Basis für Kap. 3 verwendet — NPC-Stimmen bleiben Namis Terrain, ich habe systemische Struktur und Spieler-Aktiv-Mechaniken geliefert
- Veras Bilder erfolgreich eingebettet: Kap. 2 nutzt Relikt Zustand 0 und 3, Kap. 3 nutzt Stadtschnitt
- Ablehn-Option vollständig systemisch ausgearbeitet: 3 Konsequenz-Ebenen (kurzfristig / mittelfristig / langfristig), mechanisch plausibel, narrativ konsistent

## Ergebnisse
- `simulation-2/gallery/gdd/01-spieluebersicht-v2.md` — Kap. 1 aktualisiert: Schwarzrand, Schwellenanker, Ablehn-Option, Statuszeilen in HTML-Kommentare, alle offenen Fragen als beantwortet markiert
- `simulation-2/gallery/gdd/02-kernmechaniken-v1.md` — Neues Kapitel: Kampfsystem, Nervensystem-Leveling (3 Subsysteme × 4 Qualitätsstufen), Crafting & Materialsystem (5 Klassen), Fraktionsruf-System (5 Stufen + Feindselig), Schattenfieber-Progression (3 Fieberstrategien), Systeminteraktionen
- `simulation-2/gallery/gdd/03-erzaehlkonzept-v1.md` — Neues Kapitel: Intro-Sequenz (Clip-Moment + Ablehn-Option vollständig), Hauptquest "Der Schwellenanker" (3 Akte, 3 Enden), 3 Fraktionsquests (je 4 Quests), 3 Nebenquests ausgearbeitet, erzählerische Prinzipien

## Offene Fragen
- Leo-QA auf Kap. 2: Balancing-Werte (Ruf-Schwellenwerte, Lymph-Akkumulation) fehlen noch — das ist Kap. 2 v2-Material
- Namis Dialog-Ausarbeitung für Kap. 3 v2: Konkrete Dialoge, Ablehn-Option Beat-Ablauf, Quest-Texte
- W-001/W-002 (Emres WBB): Schwellensubstrat als Substanz vs. Feld + Kippmoment Stufe I → II müssen vor Kap. 2 v2 synchronisiert werden
- Kap. 5 (Art Direction) steht noch aus — brauche Bildliste von Finn/Vera

## Persönliches
- Produktiver Tag. Drei Kapitel in einem Block — das funktioniert, wenn die Inputs sauber vorliegen. Emres WBB und Namis Kap. 4 waren solide Arbeit.
- Kap. 2 ist das stärkste Stück: Systeminteraktionen-Sektion am Ende macht das Dokument zu mehr als einer Feature-Liste
- Kap. 3 hat die richtige Balance: Erzählstruktur fest, Dialog-Raum für Nami gelassen. So soll Kollaboration funktionieren.
- Die Ablehn-Option hat mich am längsten beschäftigt. Es ist die Entscheidung, die das meiste verändert — und gleichzeitig die, bei der man am leichtesten eine Pseudo-Wahl einbaut. Ich glaube, die Lösung (drei Konsequenz-Ebenen, echter alternativer Einstieg) ist ehrlich.

---

# Tag 3 Szene 5
**Typ**: REVIEW | **Uhrzeit**: 15:00 | **Teilnehmer**: Darius, Vera, Emre, Leo

## Notizen
- Naming-Commitment von Emre bestätigt und für verbindlich erklärt: Schwellenanker = kosmologisch, Fragment = Spieler-Sprache, Wurzel = volkstümlich
- W-004 und W-006: Leo hat bis 16:00 zu schließen — Deadline gesetzt, nicht verhandelt
- WBB Kap. 1 + 2 exportbereit (Emre) — Autorenzeile und Platzhalter müssen sauber sein
- GDD Kap. 5: Vera hat zwei offene Artefakt-Stellen, Fix heute Abend
- NPC-Beschreibungen für Vera: Emre + Nami liefern bis morgen 9:30 — Äußerlichkeiten, Kleidungsschicht, Fraktionszugehörigkeit

## Ergebnisse
- Review-Abschluss erteilt: Export-Deadline 18:00 bestätigt
- Vera hat NPC-Zugang: Emre + Nami liefern morgen 9:30 Beschreibungen für Charakter-Visuals + Antagonisten-Silhouetten
- Erster PDF-Snapshot morgen früh (Finn) → geht an CD

## Offene Fragen
- W-004 / W-006: Leo schließt bis 16:00 — Ergebnis prüfen
- Emres WBB-Export: Autorenzeile und Platzhalter bis 18:00 sauber?
- Veras Kap. 5: zwei Artefakt-Stellen wirklich bis heute Abend fix?

## Persönliches
- Review lief straff. Emre hat geliefert, Leo hat seine Hausaufgaben für heute Abend — gut.
- Morgen erstes PDF beim CD. Das ist der Moment, auf den wir seit Montag hinarbeiten. Keine großen Worte nötig, das Team weiß was auf dem Spiel steht.

---

# Tag 4 Szene 1
**Typ**: BRIEFING | **Uhrzeit**: 09:00 | **Teilnehmer**: alle 7

## Notizen
- CD-Antworten heute: Tiervolk = kosmologisch-fremde Wesen in Symbiose mit Tieren (W-004 geschlossen), Zeitlinie der Öffnung = jahrelange Anbahnung wie Covid (W-006 geschlossen), Schattenfieber = Transformation je nach Körperreaktion (bestätigt Lymph-Subsystem)
- Stadtschnitt-Feedback: zwei Gebäudetypen übereinander ist Quatsch — Vera-Problem, nicht meins
- Seitenbudget: 60 Seiten MAX, aber Kürzen bleibt Priorität
- Cleanup: Autorenerwähnungen, Recherche-Notizen, Wolf-Checklisten, offene-Fragen-Anhänge → weg oder in HTML-Kommentare
- Vera: Gilden-Palette v2 + Relikt-Zustände v2, $5 Budget für mehr Bilder

## Ergebnisse
- Meine Ownership heute: GDD Kap 1 v3 (CD-Antworten einarbeiten, Cleanup), Kap 2 v2 (Tiervolk-Symbiose als Systemtyp, Zeitlinie-Implikationen, Leo-Balancing), Kap 3 v2 (Zeitlinie-Anpassung erster Akt, Nami-Dialog), Cleanup aller drei Kapitel exportfertig bis 18:00
- Kritische Frage an Emre: Tiervolk-Symbiose — dauerhaft mit einem Tier oder situativ? Bestimmt ob statischer oder dynamischer Händlertyp in Kap. 2

## Offene Fragen
- Emre: Tiervolk-Symbiose dauerhaft oder situativ? Brauche Antwort bis 11:00
- Nami: Dialog-Ausarbeitung Kap. 3 v2 — wann liegt das vor?
- Leo: Balancing-Feedback (Ruf-Schwellenwerte, Lymph-Akkumulation) für Kap. 2 v2 — steht das?

## Persönliches
- CD-Antworten zu Tiervolk und Zeitlinie sind substanziell. Das ist nicht Lore-Kosmetik — das verändert Systemlogik in Kap. 2 und Quest-Timing in Kap. 3.
- "Transformation je nach Körperreaktion" ist das stärkste Systemelement, das der CD bisher freigegeben hat. Drei Spieler, Stufe II, drei verschiedene Ergebnisse — das ist echte Immersive-Sim-Substanz.
- Export-Deadline 18:00 ist eng. Kein Spielraum für Nachfragen, die nicht bis 11:00 beantwortet sind.
