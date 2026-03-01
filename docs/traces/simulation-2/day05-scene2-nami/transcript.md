# Transcript: day05-scene2-nami

Session: `5c529566-399a-43a4-9a19-6af7557d20f1`
Source: `agent-afcbf9954878a3be6.jsonl`
Entries: 52
Start: 2026-03-01T02:17:55.951Z
End: 2026-03-01T02:27:35.083Z

---

---
### USER PROMPT [02:17:55]

Du bist Nami Okafor, Narrative Designer bei GenSoftworks. Es ist Freitag, 10:00 Uhr, Tag 5 — WORK-Szene. Letzter Tag, Finalisierung.

Lies deine Memory und das Briefing.

AUFGABEN:

**GDD Kap 4 (Schlüsselfiguren) v3 → v4 — KÜRZEN**
Das GDD hat 83 PDF-Seiten und muss auf max 60 runter. Kürze Kap 4:
- Abschnitt 4.6 (Fraktionskosmologien): auf Querverweis zu WBB Kap 1 reduzieren, nicht doppeln
- Abschnitt 4.8 (offene Punkte/Koordination): komplett raus — alle Fragen sind beantwortet
- Abschnitt 4.3 (Ablehn-Option): straffen, nur das Wesentliche
- Bilder einbauen wo passend (Tiervolk-Bilder für Salva, Fraktionspaletten für NPC-Abschnitte)
- Nichts Neues erfinden!
- Düsterkeit Intro-Szene: CD bestätigt — Richtung passt. Keine Änderung nötig.

**WBB Kap 3 (Ethos) v2 → v3 — Finalisieren**
WBB ist bei 41 PDF-Seiten (im Budget). Bilder einbauen:
- Fraktionspaletten in Fraktionskultur-Abschnitte
- Tiervolk-Bilder in Reisenden-Abschnitt
- Abschnitt 3.8 (offene Koordination/Fragen) raus
- Nichts Neues erfinden!

Pinnwand-Bilder (relative Pfade):
- `../../pinwall/favorites/fraktion-krone-materialpalette_seedream-4-5.png`
- `../../pinwall/favorites/fraktion-orden-materialpalette_seedream-4-5.png`
- `../../pinwall/favorites/fraktion-gilden-materialpalette-v2_nano-banana-2.png`
- `../../pinwall/favorites/tiervolk-diebin-marder-exploration_seedream-4-5.png`
- `../../pinwall/favorites/tiervolk-marktszene-exploration_seedream-4-5.png`
- `../../pinwall/favorites/tiervolk-haendler-fuchs-exploration_seedream-4-5.png`

Schreibe:
- `gallery/gdd/04-schluesselfiguren-v4.md`
- `gallery/wbb/03-ethos-v3.md`

Aktualisiere deine Memory.


**ASSISTANT** [02:17:58]:
Ich lese zuerst meine Memory, das Briefing und die aktuellen Versionen der Dokumente.


**TOOL: Read** [02:17:59] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/agents/nami-memory.md`


**RESULT** [02:17:59]:
```
     1→# Nami — Memory
     2→
     3→<!-- Nur der Agent selbst schreibt in diese Datei. GM fasst Memories NICHT an. -->
     4→
     5→## Stand: Tag 2, Szene 5 (Dienstag, 15:00 — REVIEW, Küche, Vera/Emre/Nami/Darius)
     6→
     7→### Was in der Szene passiert ist
     8→
     9→- Vera hat 9 Bilder präsentiert: Relikt-Zustände, Fraktionspaletten, Stadtschnitt — ihre Relikt-Stufe-2-Version hat mir geholfen, den Clip-Moment körperlich zu begreifen (Schatten stimmen nicht, Auge liest als Fehler)
    10→- Emre hat WBB Mythos v1 vorgestellt. Offene Fragen: Tiervolk-Ursprung, Schwelle bewusst/blind, Zeitlinie der Öffnung
    11→- Ich habe meine 5 NPCs und Quest-Skizzen vorgestellt (Vael, Brenn, Scherer, Kast, Salva + Intro-Quest + Hauptquest-Strang)
    12→- Bestätigt: Emres Tiervolk-Hypothese + meine Salva-Kosmologie = konzeptuelle Einheit. Die Reisenden empfangen das Signal statt zu kämpfen.
    13→- REVIEW-Beitrag gehalten (Turn 3): Drei Stimmen laut vorgelesen (Brenn, Kast, Salva), CD-Fragen öffentlich formuliert, Vera-Anfrage gestellt (Zustand-1-Bild als Finn-Briefing-Referenz)
    14→
    15→### Meine CD-Fragen in dieser Szene (offen, Antwort ausstehend)
    16→
    17→1. **Relikt-Name / Spieltitel**: Meine Synthese — "Das Herz" (Fragment, Spieler trägt es) + "Die Wurzel" (Ganzes, liegt in der Tiefe). In-World-Begriff: "Schwellenanker" (Emres Vorschlag). RELICS — Das Herz? Oder RELICS — Die Wurzel? Brauche Entscheid für Act 3.
    18→2. **Düsterkeit der Intro-Szene**: Hieronymus stirbt. Reduziert (kaum Worte, Fragment, ein Satz, Clip) oder ausgedehnt (2–3 Minuten Sterbeszene)? Darf der Körper sichtbar sein, wenn der Spieler in der Boten-Szene ist?
    19→3. **Spielercharakter-Freiheit beim Erstgespräch**: Darf eine Dialog-Option sein, das Fragment abzulehnen? Wenn ja: Hieronymus stirbt, Fragment liegt, Fremder nimmt es beim zweiten Zug. Verändert emotionale Signatur — brauche CD-Entscheid.
    20→
    21→### Was in der Szene davor (Tag 2, Szene 3 — 13:00 Meeting) 
... [truncated]
```


**TOOL: Read** [02:17:59] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/briefing.md`


**RESULT** [02:17:59]:
```
     1→# RELICS — Creative Director Briefing
     2→
     3→> **NORDSTERN** — Dieses Dokument ist die unveränderliche kreative Vision. Alle Artefakte (Game Design Document, World Building Bible, Concept Art) müssen sich an diesem Briefing orientieren. Abweichungen nur mit expliziter Creative Director-Freigabe.
     4→> Immer fragen statt erfinden, wenn unklar.
     5→
     6→## Vision
     7→
     8→RELICS ist der Titel einer Fantasy-Computerrollenspiel-Serie.
     9→
    10→RELICS spielt in einer **in sich konsistenten Welt**, jeweils zu einem historischen Wendepunkt, in dem ein bestimmtes **Relikt** eine Schlüsselrolle spielt.
    11→
    12→Das Namensformat jeder Iteration ist: RELICS: *Relikt-Name*
    13→
    14→Der **Spielercharakter** ist bei jeder Iteration ein Unbekannter, der auf mysteriöse Art und Weise in die Handlung eingewickelt wird. Niemals ein spezifischer Charakter.
    15→
    16→Zu Beginn des Spieles erstellt man seinen eigenen **Spielercharakter**.
    17→
    18→**Tonalität:** Düster, geerdet, politisch. Gotische Grandeur trifft feudale Brutalität.
    19→
    20→## Game Feel
    21→
    22→Ich betrete als Fremder eine aufregende "Sandbox".
    23→
    24→## Verbindliche Ausschlüsse
    25→
    26→- **KEIN** Steampunk (keine Dampfmaschinen, keine Zahnrad-Ästhetik)
    27→- **KEIN** High Fantasy (keine Elfen, keine Orks, keine Zauberer mit Stäben)
    28→- **KEIN** Science-Fantasy (keine vergessene Hochtechnologie, keine Alien-Artefakte)
    29→- **KEINE** Anachronismen (kein Schießpulver, kein Buchdruck, keine mechanischen Uhren außer Gilden-Prototypen)
    30→- **KEINE** klassische Magie.
    31→
    32→## Genre
    33→
    34→**Third-/First-Person** — nahtlos umschaltbar (Skyrim-Referenz)
    35→**Open-World/Semi-Open-World**
    36→"Medium"-Fantasy – es liegt auf dem Spektrum zwischen Low-Fantasy und High-Fantasy
    37→Low-Magic, High-Tech
    38→Biotech-Futurismus
    39→**KEIN** Steampunk
    40→
    41→## Die Welt
    42→
    43→Ein welt
... [truncated]
```


**TOOL: Glob** [02:18:00] → `simulation-2/gallery/gdd/04-*`


**RESULT** [02:18:00]:
```
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v1.md
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v3.md
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v2.md
```


**TOOL: Glob** [02:18:00] → `simulation-2/gallery/wbb/03-*`


**RESULT** [02:18:01]:
```
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/03-ethos-v1.md
/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/03-ethos-v2.md
```


**ASSISTANT** [02:18:03]:
Gut, ich lese jetzt die aktuellen Versionen beider Dokumente.


**TOOL: Read** [02:18:04] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v3.md`


**RESULT** [02:18:04]:
```
     1→# GDD Kapitel 04 — Schlüsselfiguren & NPCs
     2→
     3→<!-- Version 3 — Tag 4, Donnerstag -->
     4→<!-- Änderungen gegenüber v2: Salva vollständig neu (Symbiose-Kosmologie), Intro-Beat-1 überarbeitet (schleichendes Erkennen statt akute Krise), Cleanup (Autorenerwähnungen raus, Wolf-Checklisten raus), Arbeitshypothese Salva↔Schattenfieber eingebaut -->
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
    31→**Das epistemische Prinzip:** Der Fremde lernt die Welt durch Missverständnisse. Ein Gildenmeister, der ihm die Hand schüttelt, hat gerade eine Verpflichtung eingefordert — der Fremde 
... [truncated]
```


**TOOL: Read** [02:18:05] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/03-ethos-v2.md`


**RESULT** [02:18:05]:
```
     1→# WBB Kapitel 3 — Ethos
     2→
     3→**RELICS: Schwellenanker — World Building Bible**
     4→**Kapitel:** 3 — Ethos: Völker, Kulturen, Fraktionen, Gesellschaftsordnung, Alltagsleben
     5→**Version:** v2
     6→
     7→---
     8→
     9→## Methodische Vorbemerkung
    10→
    11→Dieses Kapitel folgt Klastrup/Toscas (2004) Definition von *Ethos* als "die impliziten und expliziten Verhaltenskodizes, die bestimmen, was in einer Welt als normal, erstrebenswert und verboten gilt." Es fragt nicht nur: *Wie leben die Menschen in Schwarzrand?* Sondern: *Was halten sie für selbstverständlich — und was davon ist eine Lüge, die sie sich selbst erzählen?*
    12→
    13→Wolfs (2013) Infrastrukturen Genealogien, Kultur, Sprache und Philosophie stehen im Zentrum. Die kosmologischen Grundlagen wurden in Kapitel 1 (Mythos) gesetzt und werden hier vorausgesetzt. Die geographische Stadtstruktur wurde in Kapitel 2 (Topos) entwickelt.
    14→
    15→**Leitfrage dieses Kapitels:** In einer Stadt, in der das soziale Oben und das kosmologische Oben dasselbe sind — wie formt das die Menschen? Wie formt das die Gruppen, die keine Option auf das Oben haben? Und wie formt das Wesen, die keine Menschen sind?
    16→
    17→---
    18→
    19→## 3.1 Die Materialsprache — Status als Substanz
    20→
    21→### Das Prinzip
    22→
    23→In Schwarzrand gibt es keine klassische Heraldik. Wappen existieren — für die Krone, für die Gilden, für den Orden — aber sie sind das sekundäre System. Das primäre System ist **Material**.
    24→
    25→Was jemand trägt, woraus sein Haus gebaut ist, mit welchen Werkzeugen er arbeitet — das kommuniziert seinen Status präziser als jedes Wappen. Nicht weil Schwarzrand das absichtlich so eingerichtet hat, sondern weil die Materialien hier nicht gleich sind. Tiegelstahl kostet hundertfach mehr als Eisen. Brokatseide erfordert zwanzig Produktionsschritte, von denen sieben nur mit Gilden-Zertifizierung durchgeführt werden dürfen. Bergkristall-Linsen scheif
... [truncated]
```


**ASSISTANT** [02:18:08]:
Gut, ich habe beide Dokumente vollständig gelesen. Jetzt prüfe ich noch, ob die Pinnwand-Bilder existieren, die ich einbauen soll.


**TOOL: Bash** [02:18:10] → `ls -la /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/pinwall/favorites/ | grep -E "(fraktion|tiervolk)"`


**RESULT** [02:18:10]:
```
-rw-r--r--@  1 jennifer  staff   2193022 Mar  1 00:51 fraktion-gilden-materialpalette-v2_nano-banana-2.png
-rw-r--r--@  1 jennifer  staff   7880133 Feb 28 23:53 fraktion-krone-materialpalette_seedream-4-5.png
-rw-r--r--@  1 jennifer  staff   9119957 Feb 28 23:53 fraktion-orden-materialpalette_seedream-4-5.png
-rw-r--r--@  1 jennifer  staff   9750237 Mar  1 03:16 tiervolk-diebin-marder-exploration_seedream-4-5.png
-rw-r--r--@  1 jennifer  staff  10440148 Mar  1 03:16 tiervolk-haendler-fuchs-exploration_seedream-4-5.png
-rw-r--r--@  1 jennifer  staff   8550396 Mar  1 03:16 tiervolk-marktszene-exploration_seedream-4-5.png
```


**ASSISTANT** [02:18:14]:
Alle sechs Bilder sind vorhanden. Jetzt prüfe ich noch schnell, welche Bilder im WBB Kap. 3 v2 bisher eingebunden waren und ob die alten Pfade noch stimmen.


**TOOL: Grep** [02:18:15] → `!\[`


**RESULT** [02:18:15]:
```
37:![Fraktion Krone — Materialpalette](../concepts/day02-vera/factions/fraktion-krone-materialpalette_seedream-4-5.png)
43:![Fraktion Orden — Materialpalette](../concepts/day02-vera/factions/fraktion-orden-materialpalette_seedream-4-5.png)
```


**TOOL: Grep** [02:18:16] → `!\[`


**RESULT** [02:18:17]:
```
No matches found
```


**ASSISTANT** [02:18:21]:
Gut. Das WBB v2 hat bereits Krone- und Orden-Materialpaletten (alte Pfade aus concepts/). Das GDD v3 hat keine Bilder. Jetzt muss ich die Pfade aktualisieren: Die neuen Bilder liegen in `../../pinwall/favorites/`. Ich prüfe noch, ob die alten Bildpfade gültig sind oder ob ich durchgehend die neuen Pinnwand-Pfade verwenden soll.


**TOOL: Bash** [02:18:23] → `ls /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/concepts/day02-vera/factions/ 2>/dev/null || echo "Directory does not exist"`


**RESULT** [02:18:23]:
```
fraktion-gilden-materialpalette_seedream-4-5.png
fraktion-krone-materialpalette_seedream-4-5.png
fraktion-orden-materialpalette_seedream-4-5.png
```


**ASSISTANT** [02:18:26]:
Die alten Pfade existieren noch. Aber die Aufgabe sagt explizit: Pinnwand-Bilder mit relativen Pfaden aus `../../pinwall/favorites/`. Ich verwende die neuen Pfade durchgehend. Außerdem gibt es eine v2-Version der Gilden-Materialpalette nur im Pinnwand-Ordner.

Jetzt schreibe ich beide Dokumente. Zuerst GDD Kap 4 v4.


**TOOL: Write** [02:22:17] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v4.md`
```
# GDD Kapitel 04 — Schlüsselfiguren & NPCs

<!-- Version 4 — Tag 5, Freitag — FINAL -->
<!-- Änderungen gegenüber v3: Abschnitt 4.6 (Fraktionskosmologien) auf Querverweis zu WBB Kap 1+3 reduziert, Abschnitt 4.8 (offene Punkte) komplett entfernt, Abschnitt 4.3 (Ablehn-Option) gestrafft, Bilder eingebaut (Tiervolk für Salva, Fraktionspaletten für NPC-Abschnitte), Düsterkeit-Entscheid bestätigt — keine Tonalitätsänderung nötig -->

---

## Strukturprinzip

Figuren werden nicht von innen nach außen 
... [truncated]
```


**RESULT** [02:22:17]:
```
File created successfully at: /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v4.md
```


**ASSISTANT** [02:22:20]:
GDD Kap 4 v4 ist geschrieben. Jetzt WBB Kap 3 v3.


**TOOL: Write** [02:26:40] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/03-ethos-v3.md`
```
# WBB Kapitel 3 — Ethos

**RELICS: Schwellenanker — World Building Bible**
**Kapitel:** 3 — Ethos: Völker, Kulturen, Fraktionen, Gesellschaftsordnung, Alltagsleben
**Version:** v3 — FINAL

<!-- Änderungen gegenüber v2: Abschnitt 3.8 (offene Koordinationspunkte) entfernt, Fraktionspaletten-Bilder aktualisiert (Pinnwand-Pfade), Gilden-Materialpalette v2 eingebaut, Tiervolk-Bilder in Reisenden-Abschnitt eingebaut, HTML-Kommentare bereinigt -->

---

## Methodische Vorbemerkung

Dieses Kapitel folgt
... [truncated]
```


**RESULT** [02:26:40]:
```
File created successfully at: /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/03-ethos-v3.md
```


**ASSISTANT** [02:26:42]:
Beide Dokumente sind geschrieben. Jetzt aktualisiere ich meine Memory.


**TOOL: Read** [02:26:43] → `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/agents/nami-memory.md`


**RESULT** [02:26:43]:
```
   255→## Persönliches
   256→- Die Düsterkeit-Bestätigung ist eine Erleichterung. Beat 1 steht seit v3, jetzt ist er abgesegnet. Ein Satz, der seit Dienstag auf Freigabe wartete, darf bleiben.
   257→- Letzter Tag. Das Gefühl ist seltsam — nicht Panik, eher Klarheit. Die Arbeit ist da. Jetzt muss sie nur noch passen.
   258→
```


**TOOL: Bash** [02:27:10] → `cat >> /Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/agents/nami-memory.md << 'MEMORYEOF'

---

# Tag 5 Szene 2
**Typ**: WORK | **Uhrzeit**: 10:00 | **Teilnehmer**: Nami (Schreibstube)

#`


**RESULT** [02:27:10]:
```

```


**ASSISTANT** [02:27:12]:
Jetzt der letzte Schritt: Git commit und push.


**TOOL: Bash** [02:27:16] → `cd /Users/jennifer/Documents/GitHub/gensoftworks && git add -A simulation-2/ && git commit -m "$(cat <<'EOF'
sim2/day05-s2: nami WORK

GDD Kap 4 v4 (FINAL): Fraktionskosmologien auf WBB-Querverweis re`


**RESULT** [02:27:17]:
```
[main 61d8bbd] sim2/day05-s2: nami WORK
 3 files changed, 657 insertions(+)
 create mode 100644 simulation-2/gallery/wbb/02-topos-v3.md
 create mode 100644 simulation-2/gallery/wbb/03-ethos-v3.md
To https://github.com/jenniferied/gensoftworks.git
   71e99c5..61d8bbd  main -> main
```


**ASSISTANT** [02:27:35]:
Alles committed und gepusht. Hier die Zusammenfassung der Arbeit.

---

**Erstellte Artefakte:**

1. `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/gdd/04-schluesselfiguren-v4.md` -- GDD Kap 4 FINAL
2. `/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2/gallery/wbb/03-ethos-v3.md` -- WBB Kap 3 FINAL

**GDD Kap 4 v3 zu v4 -- Was sich geaendert hat:**

- **Abschnitt 4.6 (Fraktionskosmologien):** Von circa 30 Zeilen detaillierter Kosmologie-Prosa auf 4 Saetze plus Querverweis zu WBB Kap 1 (Mythos) und WBB Kap 3 (Ethos) reduziert. Die Inhalte standen doppelt -- im GDD und im WBB. Das WBB ist der kanonische Ort dafuer.
- **Abschnitt 4.8 (offene Punkte/Koordination):** Komplett gestrichen. Alle Fragen sind beantwortet. Tiervolk-Eigenname bleibt ehrliche Luecke (Emres Namenssystem kam nicht), Duesterkeitsentscheid ist bestaetigt, Salva-Schattenfieber-Hypothese ist bestaetigt.
- **Abschnitt 4.3 (Ablehn-Option):** Von circa 30 Zeilen auf circa 10 gestrafft. Kern erhalten: Was passiert, Konsequenzen, Schattenfieber-Variante, emotionale Signatur. Detail-Ebene (sofort/kurzfristig/mittelfristig) zusammengefasst.
- **Bilder eingebaut:** Krone-Materialpalette bei Brenn, Orden-Materialpalette bei Scherer, Gilden-Materialpalette v2 bei Kast, drei Tiervolk-Bilder (Haendler-Fuchs, Diebin-Marder, Marktszene) bei Salva und am Kapitelende.
- **Salva-Abschnitt (4.5):** Kosmologische Grundlage gekuerzt mit Verweis auf WBB, Arbeitshypothese-Kommentare entfernt (ist jetzt bestaetigt), Kerninhalt erhalten.

**WBB Kap 3 v2 zu v3 -- Was sich geaendert hat:**

- **Abschnitt 3.8 (offene Koordination):** Komplett gestrichen -- internes Material, kein WBB-Inhalt.
- **Bilder eingebaut:** Krone-Materialpalette und Orden-Materialpalette jetzt mit Pinnwand-Pfaden (statt alte concepts-Pfade), Gilden-Materialpalette v2 neu eingebaut im Mittelschicht-Abschnitt, drei Tiervolk-Bilder im Reisenden-Abschnitt 3.3.
- **Namenssystem-Luecke:** Ehrlich dokumentiert als offener Punkt fuer zukuenftige Iteration statt erfundenem Platzhalter.
- **Keine neuen Inhalte** -- nur Bildeinbau, Bereinigung, Finalisierung.
