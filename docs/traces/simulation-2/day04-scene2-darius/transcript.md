# Transcript: day04-scene2-darius

Session: `7f799efb-bffb-4919-a3a4-72a2b260c43e`
Source: `agent-a41a36467e87e1dd5.jsonl`
Entries: 94
Start: 2026-02-28T23:51:39.844Z
End: 2026-03-01T00:06:35.071Z

---

---
### USER PROMPT [23:51:39]

Du bist in einer Simulation. Tag 4 (Donnerstag), Szene 2: WORK, 10:00 Uhr. Du arbeitest alleine an deinem Schreibtisch.

**Deine Aufgabe heute:**
1. **GDD Kap 2 v2 (Kernmechaniken)** — Tiervolk als eigener Händlertyp integrieren (dauerhaft, Symbiose). Schattenfieber als körperreaktionsabhängig einarbeiten. Cleanup: Autorenerwähnungen raus, Recherche-Kommentare in HTML-Kommentare.
2. **GDD Kap 3 v2 (Erzählkonzept)** — Zeitlinie aktualisieren: Covid-Analogie (jahrelange Anbahnung, nicht plötzlicher Ausbruch). Akt 1 überarbeiten. Cleanup.
3. **Cleanup aller deiner Kapitel** (Kap 1 v2, 2 v2, 3 v2) — keine Autorenerwähnungen, keine Recherche-Kommentare, keine internen Notizen im sichtbaren Text. Alles was nicht in eine professionelle PDF gehört → HTML-Kommentare oder löschen.

**Neue CD-Informationen:**
- Tiervolk = kosmologisch fremde Wesen in dauerhafter Symbiose mit Tieren (Emre bestätigt: dauerhaft, irreversibel). Motivation: brauchen Materialien die Symbiose stabilisieren → Handelsinteresse
- Zeitlinie der Öffnung = jahrelange Anbahnung wie Covid. Früherer Ausbruch weit weg, jetzt lokale Eskalation
- Schattenfieber = Infektion die je nach Körperreaktion transformiert
- Max 60 Seiten pro Dokument gesamt

**Existierende Dateien die du überarbeitest:**
- `simulation-2/gallery/gdd/01-spieluebersicht-v2.md` (bleibt v2, nur Cleanup)
- `simulation-2/gallery/gdd/02-kernmechaniken-v1.md` → schreibe v2
- `simulation-2/gallery/gdd/03-erzaehlkonzept-v1.md` → schreibe v2

**Seitenlimit beachten:** Das gesamte GDD hat 6 Kapitel und darf max 60 Seiten sein. Deine 3 Kapitel sollten zusammen ca. 25–35 Seiten umfassen. Kürze aktiv.

**Quellen die du nutzen kannst:**
- Emres WBB Kap 1 v2: `simulation-2/gallery/wbb/01-mythos-v2.md`
- Emres WBB Kap 2 v1: `simulation-2/gallery/wbb/02-topos-v1.md`
- Namis GDD Kap 4 v2: `simulation-2/gallery/gdd/04-schluesselfiguren-v2.md`

Lies deine Memory: `simulation-2/agents/darius-memory.md`

Produziere die v2-Versionen. Schreib sie als Dateien. Aktualisiere deine Memory. Deutsch. WICHTIG: Echte Umlaute (ä ö ü ß), NIEMALS ae/oe/ue/ss.


**ASSISTANT** [23:51:42]:
Ich lese zuerst meine Memory und alle relevanten Dateien.


**TOOL: Read** [23:51:42] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/agents/darius-memory.md`


**RESULT** [23:51:42]:
```
     1→# Darius — Memory
     2→
     3→<!-- Nur der Agent selbst schreibt in diese Datei. GM fasst Memories NICHT an. -->
     4→
     5→## Tag 1 — Szene 2 (10:00 Uhr, Montag)
     6→
     7→**Gelesen:**
     8→- Deus Ex "Shooter: Majestic Revelations" v5.3e (Ion Storm, 1997) — Warren Spectors annotiertes GDD
     9→- Diablo Pitch Document (Condor, 1994)
    10→
    11→**Kernerkenntnisse aus der Recherche:**
    12→- Spector beginnt mit einem philosophischen High Concept, das alle Systeme ableitet — das will ich für RELICS übernehmen
    13→- "Deep Simulation of Small Environments" > riesige, flache Open World. Gothic-Prinzip bestätigt.
    14→- Skill-Granularität ist ein bekanntes Problem: Deus Ex löst es mit 4 Qualitätsstufen statt 1-100-Skalen — mein Referenzmodell für das Nervensystem-Leveling
    15→- Diablo zeigt: ein klares "Game Feel"-Statement schlägt jede Mechanik-Beschreibung
    16→
    17→**Erste Designentscheidungen (vorläufig):**
    18→- Nervensystem-Leveling: 3 Subsysteme (Cardio, Muskel, Lymph), Use-based Progression, 4 Qualitätsstufen
    19→- Materialklasse als echte Gameplay-Variable, nicht nur Kosmetik
    20→- Fraktionsruf = Ressourcenzugang (Krone: Territorium/Passagen, Gilden: Materialien/Rezepturen, Orden: Wissen/Fertigkeitsbücher)
    21→- Design-Säulen Erstentwurf: Immersive Simulation / Fraktionspolitik / Körperlicher Fortschritt / Dichte vor Breite
    22→
    23→**Produzierte Artefakte:**
    24→- `simulation-2/gallery/gdd/00-recherche-notizen-darius.md` — Recherche-Notat, Tag 1
    25→
    26→---
    27→
    28→## Tag 2 — Szene 1 (09:00 Uhr, Dienstag) — Briefing Küche
    29→
    30→**CD-Feedback (via Finn):**
    31→- Schattenfieber: EINE biologische Wahrheit. Fraktionen interpretieren es verschieden — verschieden falsch, verschieden nah dran. Harter Kern muss definiert werden.
    32→- Relikt: CD dreht Frage zurück. Vorschläge + Bilder gewünscht. Vera produziert, Darius/Emre/Nami denken mit.
    33→- Release-Modell: Alpha (Streamer
... [truncated]
```


**TOOL: Read** [23:51:43] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/01-spieluebersicht-v2.md`


**RESULT** [23:51:43]:
```
     1→# GDD Kapitel 01 — Spielübersicht & Design-Säulen
     2→
     3→<!-- Darius: v2 — Aktualisierungen: "Schwarzrand" als offizieller Stadtname, "Schwellenanker" als Relikt-Bezeichnung (CD bestätigt, Tag 3 Briefing). Alle Statuszeilen und Autorenvermerke in HTML-Kommentare verschoben. Offene Punkte in Kap. 11 als beantwortet markiert. -->
     4→
     5→<!-- Status: v2 | Tag 3, Mittwoch | Autor: Darius Engel -->
     6→
     7→---
     8→
     9→## 1. Projekttitel & Format
    10→
    11→**Serientitel:** RELICS
    12→**Erste Iteration:** RELICS: Der Schwellenanker
    13→**Format:** Single-Player Computer-Rollenspiel
    14→**Perspektive:** Third-Person / First-Person, nahtlos umschaltbar
    15→**Monetarisierung:** Premium, einmaliger Kaufpreis — keine Mikrotransaktionen, keine kleinen Add-ons. DLCs nach Full Release, ausschließlich groß.
    16→
    17→---
    18→
    19→## 2. High Concept Statement
    20→
    21→RELICS fragt: *Wem gehört diese Welt — und was bist du bereit zu tun, um darin zu überleben?*
    22→
    23→Du bist ein Fremder. Du weißt nicht, wer du warst. Du weißt nicht, warum du hier bist. Aber die Stadt vor dir funktioniert ohne dich — sie hat Regeln, Mächte, Hierarchien, die sich über Jahrhunderte eingeschliffen haben. Drei Fraktionen teilen die Welt unter sich auf: die Krone mit ihrem Militär und ihren leeren Kassen, die Gilden mit ihren Monopolen und ihrem Geld, der Orden mit seinem Wissen und seiner Inquisition. Keine ist gut. Keine ist böse. Alle sind konsequent.
    24→
    25→Und dann gibt es das Schattenfieber. Eine Seuche, die den Körper verändert. Jede Fraktion hat eine andere Erklärung — alle drei liegen falsch, aber jede liegt anders falsch. Die Wahrheit liegt tiefer. Unter der Stadt, in der Stille unter dem Stein, wartet etwas, das die Grenze zwischen den Ebenen des Seins zusammenhält. Es heißt der **Schwellenanker**. Es schwächt sich ab. Und das Fieber breitet sich aus.
    26→
    27→Du wirst hineingezogen, ob du willst oder n
... [truncated]
```


**ASSISTANT** [23:51:49]:
Jetzt lese ich die v1-Versionen von Kap. 2 und 3, sowie die WBB-Quellen.


**TOOL: Read** [23:51:51] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/02-kernmechaniken-v1.md`


**RESULT** [23:51:51]:
```
     1→# GDD Kapitel 02 — Kernmechaniken
     2→
     3→<!-- Status: v1 | Tag 3, Mittwoch | Autor: Darius Engel -->
     4→<!-- Darius: Dieses Kapitel definiert alle Kernsysteme von RELICS: Der Schwellenanker. Jedes System ist aus den vier Design-Säulen abgeleitet. Spieler-Fantasie-Statement steht über jeder Mechanik-Beschreibung — ist das nicht da, ist das Feature raus. -->
     5→
     6→---
     7→
     8→## Überblick
     9→
    10→Dieses Kapitel beschreibt die fünf Kernsysteme von RELICS: Der Schwellenanker. Jedes System ist direkt aus den Design-Säulen von Kapitel 1 abgeleitet und muss gegen mindestens zwei Säulen bestehen:
    11→
    12→1. **Kampfsystem** — Säule I (Immersive Sim) + Säule III (Körperlicher Fortschritt)
    13→2. **Nervensystem-Leveling** — Säule III (Körperlicher Fortschritt) + Säule I (Immersive Sim)
    14→3. **Crafting & Materialsystem** — Säule II (Fraktionspolitik) + Säule IV (Dichte vor Breite)
    15→4. **Fraktionsruf-System** — Säule II (Fraktionspolitik) + Säule I (Immersive Sim)
    16→5. **Schattenfieber-Progression** — Säule III (Körperlicher Fortschritt) + Säule II (Fraktionspolitik)
    17→
    18→---
    19→
    20→## 2.1 Kampfsystem
    21→
    22→### Spieler-Fantasie
    23→
    24→*"Jeder Kampf kostet mich etwas. Wenn ich gewinne, habe ich es mir verdient."*
    25→
    26→### Designprinzipien
    27→
    28→Das Kampfsystem von RELICS ist kein Showroom für Combo-Systeme. Es ist eine mechanische Umsetzung von Schwere und Konsequenz — den zwei Kerneigenschaften des Game-Feel-Statements aus Kapitel 1. Kämpfe sollen sich anstrengend anfühlen, nicht befriedigend-flüssig. Der Spieler soll nach einem schweren Kampf *erschöpft* sein, nicht triumphierend-leicht.
    29→
    30→**Referenz:** Gothic 2 (Piranha Bytes, 2002) — Kampf als Risiko, nicht als Komfort. Dark Souls (FromSoftware, 2011) — Positionierung, Gewicht, Kosten.
    31→
    32→### Kernmechaniken des Kampfes
    33→
    34→**Ausdauersystem (Stamina)**
    35→
    36→Die 
... [truncated]
```


**TOOL: Read** [23:51:51] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/03-erzaehlkonzept-v1.md`


**RESULT** [23:51:52]:
```
     1→# GDD Kapitel 03 — Erzählkonzept
     2→
     3→<!-- Status: v1 | Tag 3, Mittwoch | Autor: Darius Engel -->
     4→<!-- Darius: Dieses Kapitel ist in enger Abstimmung mit Nami Okafors GDD Kap. 4 entstanden. Nami hat Figuren und Quest-Skizzen geliefert; ich habe die systemische Struktur und die Spieler-Aktiv-Mechaniken hinzugefügt. Die Ablehn-Option (Spieler darf Fragment verweigern) ist CD-bestätigt und hier vollständig ausgearbeitet. -->
     5→<!-- Darius: Verwendete Quellen: GDD Kap. 4 v1 (Nami, Tag 2), WBB Kap. 1 v1 (Emre, Tag 2), Briefing. Nami hat die Figuren-Stimmen, ich habe die Quest-Mechanik. Das Erzählkonzept braucht v2 mit Namis ausformuliertem Halbseiten-Text zur Ablehn-Option (war für Mi 10:00 versprochen). -->
     6→
     7→---
     8→
     9→## Überblick
    10→
    11→Das Erzählkonzept von RELICS: Der Schwellenanker definiert, wie die Geschichte erzählt wird — nicht was die Geschichte ist. Die Handlung ist ein Werkzeug, um die vier Design-Säulen erfahrbar zu machen.
    12→
    13→**Zentrales Erzählprinzip:** Der Spieler ist kein Held. Er ist ein Fremder, der in eine Situation hineingezogen wird, die ohne ihn bereits bestand. Die Geschichte ist nicht über den Spieler — sie ist eine Geschichte, in der der Spieler Entscheidungen trifft.
    14→
    15→**Erzählstruktur:** Drei Akte, drei Fraktionspfade, mehrere Questlinien, die sich überschneiden und widersprechen. Kein Akt ist vollständig linear. Jeder Akt hat einen "Open-World-Raum", in dem der Spieler die Welt erkundet, bevor er den nächsten narrativen Anker betritt.
    16→
    17→---
    18→
    19→## 3.1 Intro-Sequenz — "Was er in der Hand hielt"
    20→
    21→### Spieler-Fantasie
    22→
    23→*"In den ersten fünfzehn Minuten muss ich verstehen, was dieser Ort ist. Nicht durch Exposition — durch Erleben."*
    24→
    25→### Die Szene
    26→
    27→**Zeitpunkt:** Früher Morgen. Die Stadt Schwarzrand liegt im Nebel. Der Spieler betritt die Spielwelt zum ersten Mal.
    28→
    29→**Der
... [truncated]
```


**ASSISTANT** [23:51:55]:
Jetzt lese ich die WBB-Quellen und Namis Kap. 4.


**TOOL: Read** [23:51:57] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/01-mythos-v2.md`


**RESULT** [23:51:57]:
```
     1→# WBB Kapitel 1 — Mythos
     2→
     3→<!-- Emre: v2 — Überarbeitung nach CD-Feedback Tag 3. Änderungen: "Relikt" → "Schwellenanker" wo der Gegenstand gemeint ist, alle Teamnotizen in Kommentare verschoben, Fraktionspaletten eingebettet, professioneller WBB-Stil. -->
     4→
     5→**RELICS: Schwellenanker — World Building Bible**
     6→**Kapitel 1: Mythos**
     7→
     8→---
     9→
    10→## Vorbemerkung zur Methodik
    11→
    12→Dieses Kapitel folgt Klastrup/Toscas (2004) Definition von *Mythos* als "das Hintergrundwissen, das man braucht, um Ereignisse in der Welt zu interpretieren." Es definiert die kosmologische Ordnung, den Ursprung des Schattenfiebers und die Schöpfungserzählungen der drei Fraktionen.
    13→
    14→Wolfs (2013) Infrastrukturen *Mythologie*, *Zeitleisten* und *Verknüpfung* sind hier primär adressiert. Tolkiens (1947) Subcreation-Prinzip gilt als oberstes Gesetz: Die innere Wahrheit der Welt darf nie gebrochen werden. Das Schattenfieber ist das einzige Übernatürliche — es wird nie trivialisiert.
    15→
    16→**Methodische Regel:** Es gibt EINE biologische Wahrheit hinter dem Schattenfieber. Die Fraktionen interpretieren diese Wahrheit verschieden. Das Kapitel stellt zuerst die Wahrheit dar (Autorenebene), dann die drei kulturellen Deutungen (Weltebene). Der Spieler erfährt die Wahrheit nie vollständig — er bewegt sich zwischen den Deutungen.
    17→
    18→---
    19→
    20→## 1. Die Schwelle — Kosmologische Ordnung
    21→
    22→### 1.1 Die Struktur der Existenz
    23→
    24→Die Welt von RELICS besteht aus zwei Existenzebenen:
    25→
    26→**Die Diesseite** (*Stoffwelt*) — die materielle Realität, in der Menschen leben, sterben und bauen. Sie folgt erkennbaren Naturgesetzen. Materie hat Gewicht, Zeit hat Richtung, Körper haben Grenzen.
    27→
    28→**Die Schwelle** (*das Jenseit*) — eine andere Existenzebene, die keine räumliche "Richtung" hat, sondern eher als Zustand beschrieben werden muss. Die Schwelle ist kein Ort,
... [truncated]
```


**TOOL: Read** [23:51:57] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v2.md`


**RESULT** [23:51:57]:
```
     1→# GDD Kapitel 04 — Schlüsselfiguren & NPCs
     2→
     3→<!-- Version 2 — Tag 3, Mittwoch -->
     4→<!-- Änderungen gegenüber v1: "Schwellenanker" als offizieller Relikt-Name gesetzt, Ablehn-Option eingebaut, Autor-Metadaten und Post-It-Verweise in HTML-Kommentare verschoben, Fragment-Szene ausformuliert -->
     5→
     6→---
     7→
     8→## Strukturprinzip
     9→
    10→Figuren werden nicht von innen nach außen beschrieben. Die Stimme kommt zuerst, dann die Funktion. Ein NPC ohne eigene Stimme hat kein Recht auf Existenz im Spiel.
    11→
    12→Jede Figur wird beschrieben nach:
    13→
    14→1. **Wer sie ist** — in drei Sätzen, kein Infodump
    15→2. **Was sie vom Fremden will** — explizit und versteckt
    16→3. **Was sie nie zugeben würde** — die Risse in der Fassade
    17→4. **Ihre Stimme** — ein Muster, eine Eigenheit, ein charakteristischer Satz
    18→5. **Spielerrelevanz** — Quest-Anker, Reaktion auf Fraktionswahl, Schattenfieber-Verhältnis
    19→6. **Dramatischer Wendepunkt** — der Moment, in dem die Figur kompliziert wird
    20→
    21→---
    22→
    23→## 4.1 Der Fremde — Spielercharakter
    24→
    25→*Kein vollständiger NPC-Eintrag, da spielergesteuert. Aber die Leerstelle muss benannt werden.*
    26→
    27→Der Fremde ist kein Held. Er ist eine **Frage in Menschengestalt.**
    28→
    29→Er kommt von woanders — woher, das wählt der Spieler bei der Charaktererstellung, und es beeinflusst, wie die Welt auf ihn reagiert, aber nicht, was er "ist." Er hat einen Namen, den wir nie aussprechen. Er hat eine Vergangenheit, die wir in Dialogoptionen andeuten, aber nie erzählen. Er ist **Blank Slate mit Textur** — kein leeres Blatt, sondern ein Blatt, das schon beschrieben war und abgewischt wurde.
    30→
    31→**Das epistemische Prinzip:** Der Fremde lernt die Welt durch Missverständnisse. Ein Gildenmeister, der ihm die Hand schüttelt, hat gerade eine Verpflichtung eingefordert — der Fremde weiß das nicht, noch nicht. Ein Ordensbote, der
... [truncated]
```


**ASSISTANT** [23:52:01]:
Jetzt lese ich auch die WBB Kap. 2 für den Tiervolk-Abschnitt.


**TOOL: Read** [23:52:02] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/02-topos-v1.md`


**RESULT** [23:52:03]:
```
     1→# WBB Kapitel 2 — Topos
     2→
     3→<!-- Emre: v1 — Erstfassung Tag 3. Topos nach Klastrup/Tosca: "das Wissen darüber, was man von der Physik und Navigation der Welt erwarten kann." Wolf-Infrastrukturen Karten, Natur und Kultur hier primär adressiert. -->
     4→
     5→**RELICS: Schwellenanker — World Building Bible**
     6→**Kapitel 2: Topos**
     7→
     8→---
     9→
    10→## Vorbemerkung
    11→
    12→Topos beschreibt die physische Welt: Geographie, Klima, Architektur, Flora, Fauna — alles, was der Spieler sehen, betreten und erkunden kann. Klastrup/Tosca (2004) definieren Topos als "das Wissen darüber, was man von der Physik und Navigation der Welt erwarten kann." Für RELICS bedeutet das: Der Spieler muss intuitiv verstehen, dass *aufsteigen* sicherer wird und *absteigen* gefährlicher. Dass Materialien Macht bedeuten. Dass der Nebel nicht nur Nebel ist.
    13→
    14→Wolfs (2013) Infrastrukturen *Karten*, *Natur* und *Kultur* sind hier primär adressiert. Dieses Kapitel ergänzt die kosmologische Ordnung aus Kapitel 1 (Mythos) um ihre physische Manifestation: Wo genau befindet sich die Schwelle? Wie formt sie die Geologie? Was wächst, was lebt, was stirbt an einem Ort, an dem die Realität porös ist?
    15→
    16→---
    17→
    18→## 1. Der Talkessel — Geologie von Schwarzrand
    19→
    20→### 1.1 Entstehung
    21→
    22→Schwarzrand liegt in einem Talkessel, der vor geologischen Zeitaltern durch den Einbruch einer unterirdischen Kaverne entstand. Die Felswände — steil, zerklüftet, aus geschichtetem Kalkstein und Schiefergestein — ragen bis zu dreihundert Meter über den Talboden auf. Der Kessel misst an seiner breitesten Stelle knapp zwei Kilometer im Durchmesser und verengt sich nach unten trichterförmig. Am tiefsten Punkt, weit unter dem heutigen Straßenniveau, liegt die Ankerkammer.
    23→
    24→Die Geologie allein erklärt den Talkessel nicht vollständig. Die Gesteinsschichten zeigen Anomalien: Kristalleinschlüsse, die keiner bekannten M
... [truncated]
```


**ASSISTANT** [23:52:12]:
Ich habe jetzt alle relevanten Quellen gelesen. Jetzt schreibe ich die v2-Dokumente. Ich beginne mit dem Cleanup von Kap. 1 (nur Autorenzeile aufräumen) und dann schreibe ich die vollständigen v2-Versionen für Kap. 2 und 3.

Zunächst: Kap. 1 v2 braucht nur minimale Änderungen — die Sichtbarzeile mit dem Tiervolk-Status muss aktualisiert werden (W-004 jetzt durch CD geschlossen: Tiervolk = kosmologisch-fremde Wesen in dauerhafter Symbiose). Ich überarbeite die Tabelle in Abschnitt 10.


**TOOL: Write** [23:54:18] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/01-spieluebersicht-v2.md`
```
# GDD Kapitel 01 — Spielübersicht & Design-Säulen

<!-- Darius: v2 — Aktualisierungen: "Schwarzrand" als offizieller Stadtname, "Schwellenanker" als Relikt-Bezeichnung (CD bestätigt, Tag 3 Briefing). Tiervolk-Eintrag in Tabelle 10 aktualisiert nach CD-Feedback Tag 4: Tiervolk = kosmologisch-fremde Wesen in dauerhafter, irreversibler Symbiose mit Tieren. Alle Statuszeilen und Autorenvermerke in HTML-Kommentare verschoben. -->

---

## 1. Projekttitel & Format

**Serientitel:** RELICS
**Erste Iter
... [truncated]
```


**RESULT** [23:54:18]:
```
The file /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/01-spieluebersicht-v2.md has been updated successfully.
```


**ASSISTANT** [23:54:24]:
Jetzt schreibe ich GDD Kap. 2 v2 — mit Tiervolk als eigenem Händlertyp, Schattenfieber als körperreaktionsabhängig, und vollständigem Cleanup.


**TOOL: Write** [23:57:34] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/02-kernmechaniken-v2.md`
```
# GDD Kapitel 02 — Kernmechaniken

<!-- Darius: v2 — Wesentliche Änderungen gegenüber v1: (1) Tiervolk als eigenständiger sechster Händlertyp integriert — dauerhaft-symbiotische Wesen mit spezifischem Handelsinteresse (Symbiose-Stabilisierungs-Materialien). (2) Schattenfieber als körperreaktionsabhängig ausgearbeitet — gleiche Exposition, individuelle Transformation, kein einheitlicher Pfad. (3) Autorenvermerke und Recherche-Kommentare bereinigt. (4) Seitenvolumen gekürzt. -->

---

## Überblick
... [truncated]
```


**RESULT** [23:57:34]:
```
File created successfully at: /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/02-kernmechaniken-v2.md
```


**ASSISTANT** [23:57:41]:
Jetzt schreibe ich GDD Kap. 3 v2 mit der aktualisierten Zeitlinie (Covid-Analogie) und dem überarbeiteten Akt 1.


**TOOL: Write** [00:01:17] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md`
```
# GDD Kapitel 03 — Erzählkonzept

<!-- Darius: v2 — Wesentliche Änderungen gegenüber v1: (1) Zeitlinie der Öffnung überarbeitet: jahrelange Anbahnung (Covid-Analogie), kein plötzlicher Ausbruch. Akt 1 trägt diese Logik: Spieler kommt in eine Stadt, die sich seit Jahren langsam verändert, nicht in eine Akutkatastrophe. (2) Tiervolk-Integration: Salva ist kein Exot — er ist Teil eines langen Musters, das Spieler und Stadt verbindet. (3) Cleanup: Autorenerwähnungen, Planungskommentare, Namis-Placeh
... [truncated]
```


**RESULT** [00:01:17]:
```
File created successfully at: /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md
```


**ASSISTANT** [00:01:27]:
Gut. Jetzt aktualisiere ich meine Memory und führe dann den Git-Commit durch.


**TOOL: Read** [00:01:27] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/agents/darius-memory.md`


**RESULT** [00:01:27]:
```
   230→
   231→# Tag 4 Szene 1
   232→**Typ**: BRIEFING | **Uhrzeit**: 09:00 | **Teilnehmer**: alle 7
   233→
   234→## Notizen
   235→- CD-Antworten heute: Tiervolk = kosmologisch-fremde Wesen in Symbiose mit Tieren (W-004 geschlossen), Zeitlinie der Öffnung = jahrelange Anbahnung wie Covid (W-006 geschlossen), Schattenfieber = Transformation je nach Körperreaktion (bestätigt Lymph-Subsystem)
   236→- Stadtschnitt-Feedback: zwei Gebäudetypen übereinander ist Quatsch — Vera-Problem, nicht meins
   237→- Seitenbudget: 60 Seiten MAX, aber Kürzen bleibt Priorität
   238→- Cleanup: Autorenerwähnungen, Recherche-Notizen, Wolf-Checklisten, offene-Fragen-Anhänge → weg oder in HTML-Kommentare
   239→- Vera: Gilden-Palette v2 + Relikt-Zustände v2, $5 Budget für mehr Bilder
   240→
   241→## Ergebnisse
   242→- Meine Ownership heute: GDD Kap 1 v3 (CD-Antworten einarbeiten, Cleanup), Kap 2 v2 (Tiervolk-Symbiose als Systemtyp, Zeitlinie-Implikationen, Leo-Balancing), Kap 3 v2 (Zeitlinie-Anpassung erster Akt, Nami-Dialog), Cleanup aller drei Kapitel exportfertig bis 18:00
   243→- Kritische Frage an Emre: Tiervolk-Symbiose — dauerhaft mit einem Tier oder situativ? Bestimmt ob statischer oder dynamischer Händlertyp in Kap. 2
   244→
   245→## Offene Fragen
   246→- Emre: Tiervolk-Symbiose dauerhaft oder situativ? Brauche Antwort bis 11:00
   247→- Nami: Dialog-Ausarbeitung Kap. 3 v2 — wann liegt das vor?
   248→- Leo: Balancing-Feedback (Ruf-Schwellenwerte, Lymph-Akkumulation) für Kap. 2 v2 — steht das?
   249→
   250→## Persönliches
   251→- CD-Antworten zu Tiervolk und Zeitlinie sind substanziell. Das ist nicht Lore-Kosmetik — das verändert Systemlogik in Kap. 2 und Quest-Timing in Kap. 3.
   252→- "Transformation je nach Körperreaktion" ist das stärkste Systemelement, das der CD bisher freigegeben hat. Drei Spieler, Stufe II, drei verschiedene Ergebnisse — das ist echte Immersive-Sim-Substanz.
   253→- Export-Deadline 18:00 ist eng. Kein Spielraum für Nachfragen, die nicht bis
... [truncated]
```


**TOOL: Write** [00:04:39] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/agents/darius-memory.md`
```
# Darius — Memory

<!-- Nur der Agent selbst schreibt in diese Datei. GM fasst Memories NICHT an. -->

## Tag 1 — Szene 2 (10:00 Uhr, Montag)

**Gelesen:**
- Deus Ex "Shooter: Majestic Revelations" v5.3e (Ion Storm, 1997) — Warren Spectors annotiertes GDD
- Diablo Pitch Document (Condor, 1994)

**Kernerkenntnisse aus der Recherche:**
- Spector beginnt mit einem philosophischen High Concept, das alle Systeme ableitet — das will ich für RELICS übernehmen
- "Deep Simulation of Small Environments" >
... [truncated]
```


**RESULT** [00:04:39]:
```
The file /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/agents/darius-memory.md has been updated successfully.
```


**ASSISTANT** [00:04:44]:
Jetzt der Git-Commit.


**TOOL: Bash** [00:04:45] → `git add simulation-2/gallery/gdd/01-spieluebersicht-v2.md simulation-2/gallery/gdd/02-kernmechaniken-v2.md simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md simulation-2/agents/darius-memory.md && git `


**RESULT** [00:04:45]:
```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   simulation-2/agents/darius-memory.md
	new file:   simulation-2/gallery/gdd/02-kernmechaniken-v2.md
	new file:   simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   simulation-2/gallery/concepts/results-day04-vera.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env.local
	simulation-2/gallery/concepts/day04-vera/3-image-prompts-characters.json
	simulation-2/gallery/concepts/day04-vera/environments/
	simulation-2/gallery/concepts/day04-vera/relics/
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-diebin-marder-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-haendler-fuchs-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-rabe-bote-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/results-day04-vera-chars.json
	simulation-2/gallery/gdd/04-schluesselfiguren-v3.md
	simulation-2/gallery/gdd/05-art-direction-v2.md
	simulation-2/gallery/wbb/01-mythos-v3.md
	simulation-2/gallery/wbb/02-topos-v2.md
	simulation-2/gallery/wbb/03-ethos-v2.md
	simulation-2/gallery/wbb/salva-fremde-schattenfieber-fuer-nami.md
	simulation-2/gallery/wbb/tiervolk-lore-ankerpunkte-fuer-darius.md
```


**TOOL: Bash** [00:05:05] → `git commit -m "$(cat <<'EOF'
sim2/day04-s2: darius WORK

GDD Kap 1 v2 (Cleanup: Tiervolk-Eintrag, Körperreaktions-Varianz), Kap 2 v2 (Tiervolk als sechstes System, Händlernetz-Mechanik, Körperreaktion`


**ERROR** [00:05:05]:
```
Exit code 1
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   simulation-2/gallery/concepts/results-day04-vera.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env.local
	simulation-2/gallery/concepts/day04-vera/3-image-prompts-characters.json
	simulation-2/gallery/concepts/day04-vera/environments/
	simulation-2/gallery/concepts/day04-vera/relics/
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-diebin-marder-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-haendler-fuchs-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-rabe-bote-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/results-day04-vera-chars.json
	simulation-2/gallery/gdd/05-art-direction-v2.md
	simulation-2/gallery/wbb/01-mythos-v3.md
	simulation-2/gallery/wbb/02-topos-v2.md
	simulation-2/gallery/wbb/salva-fremde-schattenfieber-fuer-nami.md
	simulation-2/gallery/wbb/tiervolk-lore-ankerpunkte-fuer-darius.md

no changes added to commit (use "git add" and/or "git commit -a")

On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   simulation-2/gallery/concepts/results-day04-vera.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env.local
	simulation-2/gallery/concepts/day04-vera/3-image-prompts-characters.json
	simulation-2/gallery/concepts/day04-vera/environments/
	simulation-2/gallery/concepts/day04-vera/relics/
	simulation-2/gallery/concepts/day04-vera/t
... [truncated]
```


**ASSISTANT** [00:05:09]:
Der Commit ist schon durchgegangen (Exit-Code 1 durch den Hook-Output, aber der Commit hat stattgefunden — "ahead of 'origin/main' by 1 commit"). Jetzt pushen.


**TOOL: Bash** [00:05:09] → `git push`


**RESULT** [00:05:10]:
```
Everything up-to-date
```


**TOOL: Bash** [00:05:13] → `git log --oneline -5`


**RESULT** [00:05:13]:
```
fd24554 sim2/day04-s2: nami WORK
f866037 sim2/day04-s2: tobi WORK
09147bf sim2/day04-s2: leo WORK — QA-Pass über alle 9 Kapitel, v0.2-Export-Ready
45c373b sim2/day04-s2: finn WORK
13e4e0b sim2/day04-s1: leo BRIEFING
```


**ASSISTANT** [00:05:17]:
Mein Commit ist noch nicht in der History. Der Push hat "Everything up-to-date" gemeldet, was bedeutet mein lokaler Commit war nicht staged. Ich überprüfe und committe erneut.


**TOOL: Bash** [00:05:18] → `git status && git diff --cached --name-only`


**RESULT** [00:05:18]:
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   simulation-2/agents/emre-memory.md
	modified:   simulation-2/gallery/concepts/results-day04-vera.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env.local
	simulation-2/gallery/concepts/day04-vera/3-image-prompts-characters.json
	simulation-2/gallery/concepts/day04-vera/environments/
	simulation-2/gallery/concepts/day04-vera/relics/
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-diebin-marder-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-haendler-fuchs-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/day04-vera/tiervolk/tiervolk-rabe-bote-exploration_seedream-4-5.png
	simulation-2/gallery/concepts/results-day04-vera-chars.json
	simulation-2/gallery/gdd/05-art-direction-v2.md
	simulation-2/gallery/wbb/01-mythos-v3.md
	simulation-2/gallery/wbb/02-topos-v2.md
	simulation-2/gallery/wbb/salva-fremde-schattenfieber-fuer-nami.md
	simulation-2/gallery/wbb/tiervolk-lore-ankerpunkte-fuer-darius.md

no changes added to commit (use "git add" and/or "git commit -a")
```


**ASSISTANT** [00:05:22]:
Die Dateien sind nicht im Status — andere Agenten haben bereits gepusht und mein lokaler Stand wurde als "up-to-date" gemergt. Ich prüfe ob meine Dateien bereits existieren und stage sie neu.


**TOOL: Bash** [00:05:24] → `ls -la /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/02-kernmechaniken-v2.md /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md`


**RESULT** [00:05:24]:
```
-rw-r--r--@ 1 jennifer  staff  24977 Mar  1 00:57 /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/02-kernmechaniken-v2.md
-rw-r--r--@ 1 jennifer  staff  26890 Mar  1 01:01 /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md
```


**TOOL: Bash** [00:05:29] → `git add simulation-2/gallery/gdd/01-spieluebersicht-v2.md simulation-2/gallery/gdd/02-kernmechaniken-v2.md simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md simulation-2/agents/darius-memory.md && git `


**RESULT** [00:05:29]:
```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env.local

nothing added to commit but untracked files present (use "git add" to track)
```


**ASSISTANT** [00:05:33]:
Mein vorheriger Commit (der scheinbar fehlgeschlagen war) ist tatsächlich drin und wartet auf Push. "ahead of 'origin/main' by 1 commit" — ich muss jetzt pushen.


**TOOL: Bash** [00:05:34] → `git log --oneline -3 && git push`


**ERROR** [00:05:45]:
```
Exit code 1
98ac4c2 sim2/day04-s2: emre WORK
fd24554 sim2/day04-s2: nami WORK
f866037 sim2/day04-s2: tobi WORK
To https://github.com/jenniferied/gensoftworks.git
 ! [remote rejected] main -> main (cannot lock ref 'refs/heads/main': is at 98ac4c2ade866a4b927b3a6302f9eb6d8a12e0df but expected fd24554e69488c341a9508da0679e9cae1d1fc1e)
error: failed to push some refs to 'https://github.com/jenniferied/gensoftworks.git'

98ac4c2 sim2/day04-s2: emre WORK
fd24554 sim2/day04-s2: nami WORK
f866037 sim2/day04-s2: tobi WORK
To https://github.com/jenniferied/gensoftworks.git
 ! [remote rejected] main -> main (cannot lock ref 'refs/heads/main': is at 98ac4c2ade866a4b927b3a6302f9eb6d8a12e0df but expected fd24554e69488c341a9508da0679e9cae1d1fc1e)
error: failed to push some refs to 'https://github.com/jenniferied/gensoftworks.git'
```


**TOOL: Bash** [00:05:48] → `git pull --rebase && git push`


**RESULT** [00:05:49]:
```
Already up to date.
Everything up-to-date
```


**TOOL: Bash** [00:05:53] → `git log --oneline -5`


**RESULT** [00:05:53]:
```
98ac4c2 sim2/day04-s2: emre WORK
fd24554 sim2/day04-s2: nami WORK
f866037 sim2/day04-s2: tobi WORK
09147bf sim2/day04-s2: leo WORK — QA-Pass über alle 9 Kapitel, v0.2-Export-Ready
45c373b sim2/day04-s2: finn WORK
```


**ASSISTANT** [00:05:57]:
Mein Commit ist nicht in der Remote-History. Das ist ein Konkurrenz-Push-Problem — andere Agenten haben gleichzeitig gepusht. Ich starte neu mit einem sauberen Commit.


**TOOL: Bash** [00:05:57] → `git status`


**RESULT** [00:05:57]:
```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env.local

nothing added to commit but untracked files present (use "git add" to track)
```


**ASSISTANT** [00:06:01]:
Der lokale Stand ist sauber — alle drei Dateien wurden gecreated/modified und befinden sich bereits im Remote-Stand (sie wurden offenbar mit einem anderen Commit mitgepusht). Ich prüfe ob die Dateien tatsächlich in remote sind.


**TOOL: Bash** [00:06:02] → `git show HEAD --stat 2>/dev/null | head -20`


**RESULT** [00:06:02]:
```
commit 98ac4c2ade866a4b927b3a6302f9eb6d8a12e0df
Author: Jennifer Meier <m.jennifer@outlook.com>
Date:   Sun Mar 1 01:05:21 2026 +0100

    sim2/day04-s2: emre WORK
    
    WBB Mythos v3: Tiervolk als kosmologisch fremde Wesen (Symbiose), Covid-Analogie Zeitlinie, W-004/W-006 geschlossen.
    WBB Topos v2: Tiervolk-Viertel (Die Fährte), Wolf-Checkliste in Kommentar, Cleanup.
    Lieferungen: Tiervolk-Lore-Ankerpunkte fuer Darius, Salva-Fremde-Schattenfieber fuer Nami.
    
    Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

 simulation-2/agents/emre-memory.md                 |  60 +++
 .../day04-vera/3-image-prompts-characters.json     |  29 ++
 ...adtschnitt-kanalzone-v3-final_gpt-image-1-5.png | Bin 0 -> 2003118 bytes
 .../stadtschnitt-kanalzone-v3_nano-banana-2.png    | Bin 0 -> 1879014 bytes
 .../relics/relikt-hero-v2_nano-banana-pro.png      | Bin 0 -> 1569337 bytes
 ...volk-diebin-marder-exploration_seedream-4-5.png | Bin 0 -> 9750237 bytes
 ...olk-haendler-fuchs-exploration_seedream-4-5.png | Bin 0 -> 10440148 bytes
 ...tiervolk-rabe-bote-exploration_seedream-4-5.png | Bin 0 -> 10447625 bytes
```


**ASSISTANT** [00:06:06]:
Meine Dateien wurden aus dem lokalen Commit (der als "ahead of origin" gezeigt wurde) durch den Rebase verloren. Die Dateien existieren auf der Disk — sie müssen neu committiert werden.


**TOOL: Bash** [00:06:08] → `git add /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/01-spieluebersicht-v2.md /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/02-kernmechaniken-v2.md /`


**RESULT** [00:06:08]:
```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.env.local

nothing added to commit but untracked files present (use "git add" to track)
```


**ASSISTANT** [00:06:12]:
Git sagt "nothing added to commit" — das bedeutet, die Dateien wurden bereits im vorherigen Commit (der rebasiert und gepusht wurde) oder im Emre-Commit mitgenommen. Ich prüfe den Remote-Stand der Dateien.


**TOOL: Bash** [00:06:13] → `git show origin/main:simulation-2/gallery/gdd/02-kernmechaniken-v2.md 2>&1 | head -5`


**RESULT** [00:06:13]:
```
# GDD Kapitel 02 — Kernmechaniken

<!-- Darius: v2 — Wesentliche Änderungen gegenüber v1: (1) Tiervolk als eigenständiger sechster Händlertyp integriert — dauerhaft-symbiotische Wesen mit spezifischem Handelsinteresse (Symbiose-Stabilisierungs-Materialien). (2) Schattenfieber als körperreaktionsabhängig ausgearbeitet — gleiche Exposition, individuelle Transformation, kein einheitlicher Pfad. (3) Autorenvermerke und Recherche-Kommentare bereinigt. (4) Seitenvolumen gekürzt. -->

---
```


**ASSISTANT** [00:06:17]:
Die Datei ist bereits in der Remote. Offenbar wurde sie durch den Rebase-Prozess bereits mitgenommen — der git-Status zeigt "nothing to commit" weil alles sauber ist. Alles ist korrekt gepusht.

Ich verifiziere kurz, dass auch die Memory und Kap. 3 dort sind:


**TOOL: Bash** [00:06:18] → `git show origin/main:simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md 2>&1 | head -3 && git show origin/main:simulation-2/agents/darius-memory.md 2>&1 | tail -5`


**RESULT** [00:06:18]:
```
# GDD Kapitel 03 — Erzählkonzept

<!-- Darius: v2 — Wesentliche Änderungen gegenüber v1: (1) Zeitlinie der Öffnung überarbeitet: jahrelange Anbahnung (Covid-Analogie), kein plötzlicher Ausbruch. Akt 1 trägt diese Logik: Spieler kommt in eine Stadt, die sich seit Jahren langsam verändert, nicht in eine Akutkatastrophe. (2) Tiervolk-Integration: Salva ist kein Exot — er ist Teil eines langen Musters, das Spieler und Stadt verbindet. (3) Cleanup: Autorenerwähnungen, Planungskommentare, Namis-Placeholder bereinigt. Ablehn-Option vollständig integriert (aus GDD Kap. 4 v2, Nami). -->

## Persönliches
- Tiervolk als sechstes System — das war die richtige Entscheidung. Es ist kein Add-on zur Gildenstruktur, es ist ein genuiner dritter Zugangspfad für verbrannte Spielfiguren. Das hat Systemrelevanz.
- Die Covid-Analogie in Kap. 3 hat das Erzählkonzept stärker gemacht. "Verwaltete Katastrophe" als Istzustand ist überzeugender als eine frische Apokalypse — und passt zu den Fraktionen, die alle aus Routine böse handeln, nicht aus Bosheit.
- Körperreaktions-Varianz ist das Feature, das RELICS von anderen RPGs unterscheidet. Drei Spieler, Stadium II, drei verschiedene Transformationen. Das muss in der Streamer-Alpha erlebbar sein — sonst verschenken wir das stärkste Alleinstellungsmerkmal.
```


**ASSISTANT** [00:06:35]:
Alles ist in der Remote. Die Arbeit ist vollständig.

---

Tag 4, Szene 2 — Arbeit abgeschlossen.

**Was produziert wurde:**

**`simulation-2/gallery/gdd/01-spieluebersicht-v2.md`** — Cleanup und Update:
- Tiervolk-Eintrag in Tabelle 10 aktualisiert: kosmologisch-fremde Wesen in dauerhafter, irreversibler Symbiose, Handelsinteresse durch Symbiose-Stabilisierungs-Bedarf
- Magie-Zeile in Genre-Tabelle: "Transformationen je nach Körperreaktion" statt "Mutationen"
- Alle sichtbaren Autorenvermerke bereinigt

**`simulation-2/gallery/gdd/02-kernmechaniken-v2.md`** — Vollständige Überarbeitung:
- **Sechstes System neu:** Händlernetz & Tiervolk (Abschnitt 2.6) — Tiervolk als eigenständiger Händlertyp mit Vertrauens-Transaktions-Logik (binär, nicht skalierbar), drei Warenkategorien (Symbiose-Materialien-Import, Exklusive-Waren, Informationen), Sicherheitsnetz für verbrannte Spielfiguren
- **Körperreaktions-Varianz** als explizites Feature in Abschnitt 2.5 ausgearbeitet: gleiche Exposition, individuelle Transformation — Expositionsquelle, Fraktionspfad, Körperliche Baseline als Variable
- Systeminteraktionen auf sechs Systeme erweitert, Tiervolk-Cross-Interaktionen eingewoben

**`simulation-2/gallery/gdd/03-erzaehlkonzept-v2.md`** — Vollständige Überarbeitung:
- **Neuer Abschnitt 3.1:** "Die Zeitlinie der Öffnung — Erzählerischer Hintergrund" — Covid-Analogie als Erzählgerüst, verwaltete Katastrophe als Istzustand, frühere Ausbrüche weit weg als Frühwarnzeichen
- **Akt 1 überarbeitet:** Spieler kommt nicht in Akutkatastrophe, sondern in Gesellschaft im Dauerzustand. Zeitlinie rückwärts lernen.
- **Nebenquest "Salvatore und die Karawane"** aktualisiert: Karawane war Frühwarnzeichen der jahrelangen Anbahnung
- Erzählerische Prinzipien: Covid-Logik als Moral-Architektur aller drei Akte (Istzustand / Prozess / Entscheidung)
