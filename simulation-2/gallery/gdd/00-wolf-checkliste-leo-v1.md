# Wolf-Checkliste für RELICS: Alpha-Build QA

**Autor:** Leo Fischer
**Kontext:** Spielerperspektiv-Prüfwerkzeug basierend auf Mark J. P. Wolfs neun Infrastrukturen imaginärer Welten (2013, Kap. 3)
**Verwendung:** QA-Checkliste für Konsistenz + Spielerimmersion. Was merkt der Spieler? Was ist nur Backend?

---

## Überblick: Die neun Infrastrukturen

Wolf definiert neun "Sekundäre Welten-Infrastrukturen" als Gerüst, das Welten konsistent hält:
1. **Karten** (Maps) — räumliche Struktur
2. **Zeitleisten** (Timelines) — chronologische Ordnung
3. **Genealogien** (Genealogies) — Figurennetze
4. **Natur** (Nature) — Flora, Fauna, Ökologie
5. **Kultur** (Culture) — Bräuche, Alltag, Religion
6. **Sprache** (Language) — Namenssysteme, Dialekte
7. **Mythologie** (Mythology) — Schöpfungsmythen, Legenden
8. **Philosophie** (Philosophy) — Weltsicht, Ethik
9. **Verknüpfung** (Tying Together) — Wechselwirkungen

**Leo's Twist:** Für jede Infrastruktur unterscheide ich zwischen:
- **SICHTBAR:** Was der Spieler im Gameplay merkt (UI, Mechaniken, NPCs, Dialog, Umgebung)
- **BACKEND:** Konsistenz, die nur bei Close-Reading auffällt (Lore-Kohärenz, historische Tiefe)
- **CRITICAL:** Fehler, die Immersion killen

---

## 1. KARTEN — Topografie & räumliche Navigation

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Stadtarchitektur visuell kohärent**
  - Oberschicht-Viertel: Brutalistisch, Bauhaus, Hängende Gärten. Sichtbar unterschiedlich von Unterschicht.
  - Unterschicht: Versteckt, Kanäle, Slums. Muss sich "getrennt" anfühlen. Nicht zufällig verteilt.
  - **SICHTBAR:** Erste 5 Min — sieht Spieler die vertikale Schichtung? (Krone/Orden oben, Gilden verteilt, Slums unten)
  - **CRITICAL:** Wenn ein Oberschicht-NPCs-Palazzo neben einer Slum-Hütte steht ohne Übergangsviertel = Glaubwürdigkeit kaputt

- [ ] **Karte funktioniert als Spielsandbox**
  - Kann ich frei navigieren oder bin ich auf Pfaden?
  - Gibt es explorative Anreize (abseits gelegene Höhlen, versteckte Queste)?
  - **SICHTBAR:** Gameplay-Freiheit in den ersten 30 Min. "Kann ich dorthin?"
  - **BACKEND:** Konsistente Wegfindung ohne Clipping/Phasing

- [ ] **Relikt-Resonanz an räumlichen Ankerpunkten**
  - Das Relikt sitzt an einer "dünnen Stelle" (Schwellen-Konzept). Ist diese räumlich wahrnehmbar?
  - Gibt es visuelle Anomalien um das Relikt (Flora/Fauna?), die die Spielerin hinzieht?
  - **SICHTBAR:** Erste Begegnung mit Relikt sollte sich UNTERSCHIEDLICH anfühlen vom Rest der Map
  - **CRITICAL:** Wenn Relikt wie ein normales Gegenstand aussieht = Spieler verpasst es, Darius hat Angst

- [ ] **Fraktions-Gebiete räumlich erkennbar**
  - Krone: Schloss, Verwaltung (Zentral?)
  - Orden: Klöster, Archive (oben/Höhe?)
  - Gilden: Werkstätten, Märkte (verteilt)
  - **SICHTBAR:** Nach 1 Stunde soll Spieler wissen: "Ah, DAS ist Krone-Gebiet"
  - **BACKEND:** Konsistente Fahnenmale, Wappenschilder, Architektur-Codes

---

## 2. ZEITLEISTEN — Geschichte, Konflikte, Wendepunkte

### Spielerperspektive: Was merkt der Spieler?

- [ ] **"Sterbender gibt Fremden Relikt-Scherbe" — temporale Klarheit**
  - Ist der Wendepunkt zeitlich verankert? ("Der König starb letzte Nacht", "Es ist drei Tage vor der Krönung")
  - **SICHTBAR:** Dialog-Exposition ohne Codex-Dump. NPCs sollten Zeit-Kontext natürlich erwähnen
  - **CRITICAL:** Wenn Spieler nach 1 Stunde nicht weiß, "wann" das Spiel stattfindet = Problem

- [ ] **Fraktions-Spannungen zeitlich nachvollziehbar**
  - Krone vs. Orden vs. Gilden — gibt es einen Konflikt, der GERADE läuft?
  - Spieler sollte verstehen: "Warum können diese Fraktionen nicht einfach miteinander reden?"
  - **SICHTBAR:** Erste Quest-Einstieg sollte zeigen, dass Fraktions-Asymmetrie ECHT ist
  - **BACKEND:** Zeitleiste mit konkreten Ereignissen (nicht nur "irgendwann war Krieg")

- [ ] **Relikt-Historischer Kontext**
  - Ist das Relikt ALT? Oder NEU?
  - Gab es Vorkommnisse? (andere Relikte, Schatten-Krisen?)
  - **SICHTBAR:** Optional-Lore für neugierige Spieler (Codex-Einträge, NPC-Dialog)
  - **BACKEND:** Konsistente Zeitleiste, die keinen Anachronismus erzeugt

- [ ] **Schattenfieber — zeitliche Eskalation**
  - Wird es schlimmer? Gibt es Berichte von Infizierungen?
  - **SICHTBAR:** Ambient-Dialog-Scheints ("Hast du gehört, dass dritte Kind in der Gasse...")
  - **CRITICAL:** Wenn Schattenfieber sich nicht als ZEITLICHE BEDROHUNG anfühlt = Spieler nimmt es nicht ernst

---

## 3. GENEALOGIEN — Figurennetze & Dynastien

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Fraktions-Hierarchien sichtbar**
  - Krone: König, Adel, Soldaten (vertikale Hierarchie)
  - Orden: Patriarch, Priester, Inquisitoren (Autorität-Struktur)
  - Gilden: Meister, Gesellen, Lehrlinge (Kompetenz-Struktur)
  - **SICHTBAR:** Erste 30 Min — Spieler sollte wenig Haupt-NPCs pro Fraktion kennen, aber ihre Rollen verstehen
  - **CRITICAL:** Wenn NPCs ohne erkennbare Rolle auftreten = verwirrt

- [ ] **"Familie" als Einstieg in Erzählung**
  - Der sterbende NPC hat eine Familie? Feinde? Verbündete?
  - Spieler sollte EMOTIONAL an dieser Figur hängen, nicht nur mechanisch
  - **SICHTBAR:** Dialog-Chemie, Voice-Acting, Animation. Macht die Sterbeszene FEEL?
  - **BACKEND:** Genealogie-Konsistenz (wer ist mit wem verwandt, beruflich, romantisch?)

- [ ] **Fraktions-interne Spannungen (Genealogie)**
  - Gibt es Rivalen INNERHALB einer Fraktion?
  - Z.B. zwei Gildenmeister, die unterschiedliche Positionen haben?
  - **SICHTBAR:** Quest-Verzweigungen sollten zeigen: "Die Krone ist nicht eins. Es gibt unterschiedliche Agenden."
  - **BACKEND:** NPC-Listen mit Beziehungen

---

## 4. NATUR — Flora, Fauna, Ökologie

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Schattenfieber verändert Biologie sichtbar**
  - Infizierte Tiere: merkwürdig? Gefährlich? Biolumineszent?
  - **SICHTBAR:** Wenn Spieler infiziert wird, soll sie körperlich SPÜREN, dass was falsch ist
  - **CRITICAL:** Wenn Schattenfieber als "magische Krankheit" wirkt statt "biologische Mutation" = Tonalität-Fehler

- [ ] **Mitteleuropäische Ökologie (nicht generisch Fantasy)**
  - Waldtypen: Laubwald, Nadelwald (geografisch sinnvoll)
  - Jahreszeiten: Sichtbar? (im Spiel-Zeitablauf)
  - **SICHTBAR:** Environment Art sollte SEIN, nicht "Generic Medieval Forest"
  - **BACKEND:** Vera's Responsibility. Leo prüft: Fühlt sich die Natur vertraut + übernatürlich an?

- [ ] **Tiervolk: Material-Handel, nicht mystisch**
  - Tiervolk = "Händler und Diebe, nicht Handwerker" (Briefing)
  - Sie sollten MODERN-Cyberpunk wirken: Finesse, Diebstahl, Netzwerke
  - **SICHTBAR:** Wenn Tiervolk auftritt, sollte es anders SPIELEN (schneller, politischer)
  - **CRITICAL:** Kein tribal-Magic-Vibe. Sie sind Cyberpunk-Operatoren.

---

## 5. KULTUR — Bräuche, Alltag, Religion

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Material-Klasse ist SICHTBAR**
  - Oberschicht: All-Black, All-White, Monochrom + einzelner neon-Akzent
  - Mittelschicht: Erdtöne, gedeckte Farben
  - Unterschicht: Grau, Braun, schmutzig + gestohlene leuchtende Teile
  - **SICHTBAR:** Nach 30 Min sollte Spieler wissen: "Dieser NPC ist Oberschicht, weil er nur Weiß trägt"
  - **CRITICAL:** Wenn Materialsprache konsistent, Immersion steigt. Wenn chaotisch, wirkt Welt billig.

- [ ] **Alltag ist erkennbar (nicht nur Combat)**
  - Zivile NPCs machen was? (Weber webt, Schmiede schmiedet, Mönch betet?)
  - **SICHTBAR:** Ambient-Animation, AI-Schedules. Leben sich nicht live anfühlen?
  - **BACKEND:** Gilden-Monopole sollten sich in Alltag widerspiegeln (warum gibt es nur eine Schmiede?)

- [ ] **Religion (Orden) ist subtil, nicht mystisch**
  - Orden = Bildungsmonopol + Überwachung (Briefing)
  - Sind Mönche sichtbar in der Stadt? Inquisitoren?
  - **SICHTBAR:** Kirchen/Klöster sollten sich von Schloss/Werkstatt unterscheiden
  - **CRITICAL:** Kein "magischer Glaube". Orden sollte politisch-rational wirken

- [ ] **Bräuche: Fraktions-spezifisch**
  - Krone: Tournamente, Hofzeremoniell?
  - Orden: Prozessionen, Archive?
  - Gilden: Zunfttreffen, Meisterschaften?
  - **SICHTBAR:** Optional-Queste sollten diese Bräuche zeigen
  - **BACKEND:** Nami's Responsibility. Aber Leo prüft: Würde Streamer das interessant finden?

---

## 6. SPRACHE — Namenssysteme, Dialekte

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Namen sind germanisch (keine Generik-Fantasy)**
  - Krone: Hochdeutsche Namen (Friedrich, Margarete, Leopold)
  - Orden: Religiöse Namen (Gottfried, Agnes, Bruno)
  - Gilden: Handwerks-Familiennamen (Müller, Weber, Schmidt)
  - Tiervolk: ???  (noch zu definieren mit Team)
  - **SICHTBAR:** Wenn Spieler einen Namen hört, sollte sie Fraktions-Zugehörigkeit erraten können
  - **CRITICAL:** Wenn Namen generisch wirken ("Zarthaxion") = Fantasy-Cliché-Gefühl

- [ ] **Dialekte (optional, aber impactful)**
  - Unterschicht spricht anders als Oberschicht?
  - Tiervolk hat Akzent?
  - **SICHTBAR:** Voice-Acting. Unterschiedliche Dialekte machen Welt DICHT
  - **BACKEND:** Nicht übertreiben (Spieler soll verstehen, nicht verwirrt sein)

- [ ] **Codex-Sprache konsistent mit Dialog**
  - Wenn Spieler Lore liest, soll es sich wie "aus dieser Welt" anfühlen
  - **BACKEND:** Nami's Responsibility. Leo prüft: Zu akademisch? Oder lebendig?

---

## 7. MYTHOLOGIE — Schöpfungsmythen, Legenden, Prophezeiungen

### Spielerperspektive: Was merkt der Spieler?

- [ ] **Relikt hat mythologischen Ursprung**
  - Wer hat das Relikt geschaffen? Woher kommt es?
  - Optional-Lore für Deep-Dive-Spieler
  - **SICHTBAR:** Erste Begegnung sollte RÄTSELHAFT sein (nicht erklärend)
  - **CRITICAL:** Spieler soll fühlen: "Das ist älter als alles, was ich kenne"

- [ ] **Germanische Mythologie (subtil)**
  - Yggdrasil-Referenzen? (Schwellen zwischen Welten?)
  - Wotan/Orden-Parallele?
  - **SICHTBAR:** Optional. Nur für Spieler, die suchen.
  - **BACKEND:** Darf NICHT forciert sein. Tonal leicht, nicht "preachy"

- [ ] **Jede Fraktion hat ihre Mythologie**
  - Krone: "Wir sind von alten Königen abstammend"
  - Orden: "Wissen ist heilig"
  - Gilden: "Material = Macht"
  - **SICHTBAR:** NPCs sollten ihre Weltsicht durch Mythen ausdrücken
  - **BACKEND:** Mythologische Konsistenz (widersprechen sich die Mythen? Absicht?)

---

## 8. PHILOSOPHIE — Weltsicht, Ethik, Wertesysteme

### Spielerperspektive: Was merkt der Spieler?

- [ ] **"Skill-by-Use" hat philosophischen Grund**
  - Krone: "Erbe = Macht" (Geburt)
  - Orden: "Bildung = Macht" (Wissen)
  - Gilden: "Handwerk = Macht" (Praxis)
  - Spieler: Du lernst durch Tun (Skill-by-Use) — also philosophisch GITDERN-aligned, nicht Order-aligned
  - **SICHTBAR:** Nach Skill-Upgrade sollte Dialog-Option anders sein ("Ich WEISS jetzt, wie man das macht")
  - **CRITICAL:** Skill-System muss spielerisch mit Weltanschauung SYNC sein

- [ ] **"Echte Fraktionswahl" hat ethischen Grund**
  - Krone: "Ich will Ordnung" (Tradition)
  - Orden: "Ich will Kontrolle" (Wissen)
  - Gilden: "Ich will Wohlstand" (Material)
  - **SICHTBAR:** Jede Quest sollte drei Lösungen haben (jeweils Fraktion-aligned)
  - **CRITICAL:** Spieler soll nicht fühlen: "Alle Fraktionen sind gleich." Sie sollten echte Dilemmen sein

- [ ] **Schattenfieber: philosophische Bedrohung**
  - Was passiert, wenn der Körper / die Hierarchie / das Wissen kaputt geht?
  - **SICHTBAR:** Infizierte NPCs sollten VERZWEIFELT sein, nicht nur "zombie-like"
  - **BACKEND:** Schattenfieber-Philosophie mit Emre klären (Was bedeutet es, infiziert zu sein?)

---

## 9. VERKNÜPFUNG — Wechselwirkungen zwischen Infrastrukturen

### Spielerperspektive: Was merkt der Spieler?

Diese ist die WICHTIGSTE für Immersion. Alle neun Infrastrukturen sollten ZUSAMMENHÄNGEN.

- [ ] **Karte + Kultur = Raum-Verhalten**
  - Oberschicht-Viertel: Ruhig, organisiert, sichtbare Wachen
  - Unterschicht: Chaotisch, schnell, versteckte Drusen-Quellen
  - Wenn Spieler durch verschiedene Viertel geht, sollte GAMEPLAY sich unterscheiden
  - **SICHTBAR:** Encounters, NPCs, Loot sollten schicht-konsistent sein
  - **CRITICAL:** Wenn Unterschicht wie Oberschicht spielbar ist = Immersion kaputt

- [ ] **Zeitleiste + Mythologie = Sinnhaftigkeit**
  - "Vor 500 Jahren kam das Relikt" (Zeitleiste) = "Deshalb ist es in DIESEM Tempel" (Mythologie + Karte)
  - **SICHTBAR:** Wenn Spieler Environment erforscht, Lore sollte räumliche Strukturen erklären
  - **BACKEND:** Nami + Emre sollten koordinieren

- [ ] **Genealogie + Fraktions-Philosophie = NPC-Motivation**
  - Eine Krone-Adelige hat Grund, Orden zu bekämpfen, weil ihre PHILOSOPHIE unterschiedlich ist
  - Nicht random Feindschaft, sondern strukturelle Unverträglichkeit
  - **SICHTBAR:** Wenn Spieler NPC-Quests macht, sollte Motivation aus Weltbau klar sein
  - **CRITICAL:** Keine "just because"-Quests. Alles muss aus Weltkohärenz folgen

- [ ] **Kultur + Sprache + Natur = Glaubwürdigkeit**
  - Wenn eine Gegend AUSSIEHT wie Mitteleuropa (Natur), KLINGT wie Deutsch (Sprache), und LEBT wie MA (Kultur), ist Immersion komplett
  - **SICHTBAR:** Gesamtes Paket: Environment + NPC-Aussehen + Dialog + Alltag
  - **CRITICAL:** Wenn eins nicht passt, wirkt alles falsch

- [ ] **Relikt + alle neun Infrastrukturen = Welt-als-Charakter**
  - Das Relikt sollte nicht nur Mechanic sein, sondern VERKÖRPERUNG aller Infrastrukturen
  - Relikt-Geschichte = Mythologie
  - Relikt-Effekt auf Flora/Fauna = Natur
  - Relikt-Konflikt zwischen Fraktionen = Philosophie
  - Relikt-Resonanz = Karte
  - usw.
  - **SICHTBAR:** Wenn Spieler Relikt interagiert, sollte es sich wie KERN der Welt anfühlen
  - **CRITICAL:** Relikt darf nicht isoliert sein. Es muss ALLES durchdringen.

---

## Praxis: Checklisten-Workflow (QA-Einsatz)

### Alpha-Build-Test (erste 60 Minuten)

**Tag 1: SICHTBAR-Checks** (was merkt der Spieler?)
1. Starte Spiel. Keine Designdocs vorher lesen.
2. Notiere in nächsten 5 Min: Welche Infrastruktur-Signale merke ich?
   - Sehe ich unterschiedliche Schichten? (Karte + Kultur)
   - Höre ich verschiedene Sprachstile? (Sprache)
   - Merke ich zeitliche Urgency? (Zeitleiste)
3. Nach 30 Min: Schreibe "Erste-Eindruck-Bericht" (Spielerperspektive)
4. Nach 60 Min: Ist die Fraktions-Wahl ECHT? (Philosophie)

**Tag 2: BACKEND-Checks** (Lore-Konsistenz)
1. Lese alle verfügbaren Codex/Lore-Einträge
2. Prüfe: Widersprechen sich Zeitleiste + Mythologie?
3. Prüfe: Sind NPC-Genealogien konsistent?
4. Schreibe "Lore-Audit"-Bericht

**Day 3: VERKNÜPFUNG-Checks** (Weltkohärenz)
1. "Wenn ich die Karte als Person nehmen würde: Macht sie Sinn?"
2. "Wenn ich die Regeln des Relikt-Philosophie nehme: Erklärt es die Welt?"
3. Schreibe "Weltkohärenz"-Bericht

### Beispiel-Bug-Report (mit Wolf-Infrastruktur)

```
RELICS: Alpha, Erste Stunde
Infrastruktur: Karte + Kultur
Severity: HIGH (Immersion)

Beschreibung:
Nach Intro treffe ich auf reiche Kaufleute in Slum-Viertel.
Sie tragen All-White-Oberschicht-Klamotten.
Umgebung ist aber eindeutig Unterschicht (morsche Häuser, Ratten).

Problem:
- Material-Klasse (Kultur) passt nicht zu räumlichen Kontext (Karte)
- Spieler: "Warum sind Oberschicht hier? Sind die verloren?"

Lösung:
Option A: NPCs umziehen zu Oberschicht-Viertel
Option B: NPC-Kostüme ändern zu Mittelschicht
Option C: Dialog erklären warum Oberschicht hier ist
```

---

## Mein QA-Fokus für RELICS Alpha

**Kanarienvogel-Rolle (Leo streamt für 47K Follower):**

Das wichtigste ist nicht, dass alle 9 Infrastrukturen PERFECT sind.
Sondern dass sie KOHÄRENT FÜHLEN.

1. **Minute 0–5:** Merkt Streamer-Chat die Material-Klasse? ("Ooh fancy" vs. "meh")
2. **Minute 5–10:** Hängt Spieler emotionell am sterbenden NPC? (Genealogie + Kultur + Dialog)
3. **Minute 10–15:** Versteht Spieler die zeitliche Situation? ("Warte, wann findet das statt?")
4. **Minute 15–30:** Gibt es ECHTE Fraktionswahl oder nur Illusion? (Philosophie)
5. **Minute 30–60:** Fühlt sich Relikt-Resonanz WOW an oder buggy? (Alle Infrastrukturen)

Wenn Chat nicht abschaltet beim Intro = SUCCESS.

---

## Nächste Schritte

- [ ] Sync mit Darius: Skill-by-Use (philosophischer Grund?) — heute Nachmittag
- [ ] Alpha-Build besorgen + erste Stunde testen
- [ ] Relikt-Resonanz QA (mit Tobi, wenn Build kaputt)
- [ ] Streamer-Mock-Test (testen wie Zuschauer reagieren)
- [ ] Feedback in Tracking-Spreadsheet notieren

---

**Aktualisiert:** Tag 2, Szene 2 (Dienstag 10:00)
**Status:** DRAFT — Finalisierung nach Skill-by-Use Sync mit Darius
