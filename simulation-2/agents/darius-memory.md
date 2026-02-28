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

### Offene CD-Fragen (nach Dringlichkeit geordnet — meine Filterung):

**PRIORITÄT 1 — Mittwoch früh ans CD:**
1. **Relikt-Name / Spieltitel-Suffix:** "Das Herz" (Fragment beim Spieler) vs. "Die Wurzel" (Ganzes in der Tiefe). In-World-Begriff "Schwellenanker" (Emre) schon da. Blockiert: Namis Act 3, Veras Hero-Shot-Iteration.
2. **Player-Agency beim Erstgespräch:** Ablehn-Option beim Fragment — ja oder nein? Wenn ja: Nami liefert Mittwoch bis 10:00 eine Halbseite mit konkreten Konsequenzen. Echte Wahlfreiheit oder Theater? Das muss feststehen.

**PRIORITÄT 2 — Emre klärt intern, bevor CD entscheidet:**
3. **Relikt-Formveränderung:** Wächst das Relikt im aktivierten Zustand physisch? Das ist eine biologische Lore-Entscheidung (Emre), keine Ästhetik-Entscheidung (Vera). Emre liefert bis Mittwoch 10:00.
4. **Tiervolk-Ursprung / Schwelle bewusst oder blind:** Kosmologie-Frage. Meine Position: Für Kapitel 2 brauche ich Tiervolk-Funktion als Händler-Typ vor der Tiervolk-Kosmologie. Emre + Nami klären intern.

**MEINE EMPFEHLUNG (kein CD-Entscheid nötig):**
5. **Düsterkeit der Intro:** Reduziert. Kurze Sterbeszene, Fragment, Clip-Moment, weiter. Zwei-bis-drei-Minuten-Sterbeszene am Anfang ist Pacing-Risiko für Streamer-Alpha. Empfehlung ans CD gebündelt, kein offener Entscheid.

### Was mich heute beeindruckt hat:
- Emres drei Schöpfungsmythen = direkt verwendbares Gameplay-System (drei Fraktions-Motivationsstrukturen für Kap. 2)
- Namis Salva = präzise Immersive-Sim-Figur, funktioniert weil sie außerhalb der drei Fraktionslogiken steht
- Veras Zustand-Eins-Bild = stärkstes Konzept-Bild des Tages

### Nächste Schritte:
- Nami: Halbseite Konsequenzen der Ablehn-Option bis Mittwoch 10:00
- Emre: Relikt-Formfrage + Tiervolk-Funktion bis Mittwoch 10:00
- Vera: Hero-Shot-Iteration (organische Knochen-Textur) + Stadtschnitt-Überarbeitung (Schwarzrand-Richtungskonzept)
- Ich: CD-Fragen bündeln (Mittwoch früh), dann GDD Kapitel 2 (Kernmechaniken) beginnen
- GDD Kap. 1 v2: Stadtname "Schwarzrand" eintragen — noch offen
