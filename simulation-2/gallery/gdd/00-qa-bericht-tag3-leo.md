# QA-Bericht Tag 3 — Leo Fischer

**Datum:** Mittwoch, Tag 3, 10:30–12:00 Uhr
**QA-Typ:** Kapitel-Review (Spielerperspektive + Briefing-Konsistenz)
**Reviewer:** Leo Fischer, QA Lead
**Checkliste:** Wolf-Infrastrukturen, Terminologie, Sauberkeit, Vollständigkeit, interne Konsistenz

**Umfang:** 4 Kapitel gereviewed
- `01-spieluebersicht-v1.md` (Darius)
- `04-schluesselfiguren-v1.md` (Nami)
- `06-technische-spezifikation-v1.md` (Tobi)
- WBB `01-mythos-v1.md` (Emre)

---

## TL;DR — Executive Summary

**Allgemeines:** Die Kapitel hängen kohärent zusammen. Die vier Agenten haben gut kommuniziert. Aber: **Drei KRITISCHE Blocking-Punkte**, die vor Darius' v2-Revision gelöst sein müssen, und **eine Design-Doc-Hygiene-Schuld**, die bis zur Alpha-Freigabe weg muss.

**Bleeding Issues** (sofort handeln):
1. **Relikt-Namenspolitik** — Vier verschiedene Label für dasselbe Objekt. Briefing sagt "Schwellenanker" ist der Name. Kapitel befolgen das nicht konsistent.
2. **Emres Widersprüche-Log** — W-001 (Substanz vs. Bedingung), W-003 (Flora/Fauna undefiniert), W-004 (Tiervolk kosmologischer Ursprung), W-005 (Relikt-Physik vage).
3. **Autor-Nummern in sichtbaren Texten** — CD-Feedback: "Saubere Dokumente, keine Namen." Violiert in Kap 01 und Kap 04.

---

## Detailanalyse nach Wolf-Infrastrukturen

### 1. Karten (Geographie, räumliche Ordnung)

**Status:** ✅ Teilweise stark, teilweise Lücke

**Gut:**
- Emre (WBB 01) definiert die vertikale Ordnung klar: Oben = Sicherheit, Unten = Schwellennähe
- Tobi (Kap 06) hat die Schicht-Architektur technisch umgesetzt (vier Data Layers, Streaming-Logik)
- Schwarzrand-Topografie ist beschrieben (Talkessel, Felswände, vertikale Stadt)

**Problematisch:**
- **Keine Detailkarte.** Wo sind die Gilden-Viertel konkret? Wo die Ordenssitze? Wo der Kronpalast? Das sieht nach Vera-Aufgabe aus, aber: Im GDD sollte mindestens erwähnt sein, welche NPCs in welcher Schicht sichtbar werden (Spieler-Erkenntnis). Kap 04 (Nami) hat das ansatzweise: "Der Spieler merkt die Schichtung" — aber nicht konkret.
- **Houdini-Terrain-Constraints fehlen** — Tobi schreibt in 6.7.1: "Offene Frage an Vera: Gibt es definierte Punkte für Stadteingang, wichtige Sichtachsen?" Das ist KRITISCH und sollte vor Woche 1–4 Pre-Alpha geklärt sein, nicht offen.

**QA-Empfehlung:** Vera sollte bis Ende heute eine Skizze (Schichttrennung, Hauptzugangsrouten, 2–3 definierte Sichtachsen) bereitstellen. Kann dann in WBB Kap 2 (Topos) ausgearbeitet werden.

---

### 2. Zeitleisten (Geschichte, Konflikte, Wendepunkte)

**Status:** ⚠️ Skizziert, aber kritische Lücken

**Gut:**
- Emre definiert: "Vor einer Generation wurde die Wurzelkammer geöffnet" — das ist der Wendepunkt
- Darius (Kap 01) referenziert das: "Die Öffnung" ist die narrative Absicht
- Nami (Kap 04) baut Quest-Struktur drauf: Act 1 = Fragment-Suche, Act 2 = Muster erkennen, Act 3 = Ursprung

**Problematisch:**
- **"Vor einer Generation" ist nicht konkretisiert.** Emre schreibt in Widerspruchs-Log W-006: "20 Jahre? 30 Jahre? 40 Jahre?" Das beeinflusst, welche NPCs Zeitzeugen sind. Hieronymus Vael (Kap 04) sollte einer sein, aber sein Alter (ca. 50, "sieht achtzig aus") muss konsistent sein.
- **Keine Zeitleiste der Fraktionen.** Wann spalten die Fraktionen sich? Wann gründen die Gilden ihre Monopole? Das ist implizit in Emre (WBB 01, Abschnitt 6 — Gilden-Monopolstruktur), aber nicht chronologisiert.
- **Relikt-Entfernung vs. Schattenfieber-Eskalation nicht konkretisiert.** Emre schreibt: "Vor einer Generation [...] öffnete jemand die Wurzelkammer. [...] Das Schattenfieber breitete sich explosionsartig aus." Aber: wie lange dauerte die Eskalation? Wochen? Monate? Das ändert alles für Spieler-Verstehen.

**QA-Empfehlung:** Emre + Nami müssen gemeinsam festlegen:
- Konkrete Jahreszahl der Öffnung
- Eskalations-Zeitleiste (Schattenfieber-Ausbreitung)
- Wer war Zeuge wann (für Nami's Quest-Struktur)

Bis Ende heute sollte da Klarheit sein. Ist für Act 1 blockierend.

---

### 3. Genealogien (Figurennetze, Dynastien)

**Status:** ⚠️ Grundstruktur, aber NPC-Netzwerk unvollständig

**Gut:**
- Nami (Kap 04) hat fünf Kernfiguren stark ausgearbeitet: Hieronymus, Adelhaid Brenn (Krone), Ivo Scherer (Orden), Vreni Kast (Gilden), Salva (Tiervolk)
- Jede Figur hat klare Stimme und versteckte Absichten — das ist Qualität
- Fraktions-Hierarchien angedeutet: "Marschall" (Brenn), "Forschungsbruder" (Scherer), "Gildenmeisterin" (Kast)

**Problematisch:**
- **Keine Feudal-Hierarchie.** Wer ist der König/die Königin? Wer führt den Orden? Wer ist der Gildenrat-Chef? Nami schreibt "Spieler kann Fraktionen beitreten" — aber mit welchen NPCs? Nur mit den fünf?
- **Tiervolk-Status unklar.** Salva ist "keine Fraktion, sondern lose Gemeinschaft." Nami schreibt in Kap 04: "Das Tiervolk ist kein Volk" (Section 4.4). Aber: Wer sind die anderen Reisenden? Hat jeder einen Namen/eine Rolle?
- **Nami erwähnt "alte Mann in den Slums" (Nebenquest-Idee, Section 4.6).** Aber: Name? Funktion? Das ist noch eine Nebennotiz, nicht ausgearbeitet.

**QA-Beobachtung:** Die Kern-5-Figuren sind hervorragend. Aber die Welt fühlt sich klein an, wenn nur diese 5 prägen. Gothic 2 hat 50+ benannte NPCs mit Tagesablauf. RELICS strebt "Dichte vor Breite" an — aber es braucht genug Dichte, dass die Welt atmet. Das ist für v1 okay (Skelet), aber muss bis Beta ausgebaut sein.

**QA-Empfehlung:** Nami sollte bis Beta ein Genealogie-Diagram zeichnen: Fraktions-Hierarchie mit 3–5 NPCs pro Fraktion, dann sekundäre Kontakte. Das ist ein großes Dokument, aber für Quest-Planung essential.

---

### 4. Natur (Flora, Fauna, Ökologie)

**Status:** ❌ Kritisch unterentwickelt

**Gut:**
- Emre erwähnt Schattenflora und Schwellenfauna — klingt richtig
- Tobi (Kap 06) hat "Vegetation-Infiltration" als PCG-System — schön
- Biolumineszenz ist konsistent über alle Kapitel (Kap 06, WBB 01)

**Problematisch:**
- **Emre schreibt selbst (WBB 01, W-003): "Komplett undefiniert. [...] Muss in Kap. 2 (Topos) kommen."**
- **Was sind konkrete Pflanzen/Tiere?** Gibt es Schwellen-Pilze? Schwellen-Insekten? Mutierte Waldtiere? Nichts davon ist beschrieben.
- **Tiervolk-Herkunft unklar.** Briefing sagt: "Tiervolk weniger tribal, leicht alien vs. menschlich clean." Aber: Sind sie menschliche Mutanten? Eigene Spezies? Emre schreibt in Widerspruchs-Log W-004: "Muss geklärt werden. KRITISCH."
- **Nahrungskette/Ökologie fehlt.** Das scheint zu Vera-/Emre-Aufgabe (Topos-Kapitel) zu gehören, aber sollte hier angedeutet sein.

**QA-Warnung:** Das ist nicht "schön zu haben". Das ist Welt-Konsistenz. Ein Spieler, der in den Schlund steigt, sieht Pflanzen. Diese Pflanzen müssen visuell erzählen, dass die Schwelle hier nah ist. Vera braucht Referenzen. Emre muss die liefern. **Bis Beta ist das blockierend für die visuelle Kontinuität.**

**QA-Empfehlung:** Emre macht für WBB Kap 2 (Topos) eine Natur-Unterliste: 5–7 Schwellenflora-Typen (mit Name, Visuelle Beschreibung, biologischer Zweck), 3–4 Schwellenfauna (dito), Tiervolk-Herkunftshypothese (auch wenn Spieler das nie erfährt — für innere Konsistenz).

---

### 5. Kultur (Bräuche, Kunst, Religion, Alltagsleben)

**Status:** ✅ Stark

**Gut:**
- Darius (Kap 01) hat Materialsprache perfekt: Oberschicht = All-Black/Monochrom, Unterschicht = Grau/Schmutzig + gestohlene Farbe
- Emre (WBB 01) hat Fraktions-Kosmologien detailliert: Krone (Legitimation durch Siegel), Orden (Legitimation durch Wissen), Gilden (Legitimation durch Material)
- Nami (Kap 04) zeigt Alltagsleben durch NPC-Stimmen: Brenn spricht bürokratisch, Scherer stellt Gegenfragen, Kast spricht schnell
- Gilden-Monopole konkretisiert in Emre (WBB 01, Abschnitt 6): Schmiede, Glasmacher, Weber, Gerber, Goldschmiede, Kerzenzieher, Pergamenter, Steinmetze

**Lücken:**
- **Religion/Spiritualität.** Der Orden hat eine Theologie, aber: Gibt es andere Glaubenssysteme? Private Altäre in den Slums? Aberglaube? Nami könnte das ausbauen, aber es ist nicht da.
- **Alltag in den Schichten.** Was essen die Unterschicht-Bewohner? Was machen sie nachts? Wo schlafen sie? Das ist Material für Welt-Glaubhaftigkeit — kommt aber erst in "Topos"-Kapitel.

**QA-Note:** Die Kultur-Tiefe ist hier sehr gut. Nicht perfectible, aber solide.

---

### 6. Sprache (Namenssysteme, Dialekte)

**Status:** ⚠️ Ansatz, aber nicht vollständig

**Gut:**
- Schwarzrand — Name funktioniert (Emre, WBB 01)
- Charakter-Namen haben germanischen Klang: Adelhaid, Ivo, Vreni, Hieronymus — korrekt für "Mitteleuropa + germanische Mythologie"
- Fraktion-Labels sind klar: Krone, Orden, Gilden

**Problematisch:**
- **Keine Dialektsysteme.** Sprechen Unterschicht-NPCs anders als Oberschicht? Emre hat das nicht definiert. Nami könnte es in die Stimmen-Beschreibung einbauen (z.B. "Brenn spricht wie eine Offizierin, korrekt, ohne Dialekt").
- **Tiervolk-Namen.** Salva ist "Platzhalter" (Nami, Kap 04). Wie nennen sich die Reisenden untereinander? Gibt es ein Tiervolk-Namenssystem?
- **Schwellenphänomene-Vokabular nicht etabliert.** Emre schreibt "Flüstern" (Stufe 1), "Wandlung" (Stufe 2), "Entgrenzung" (Stufe 3) — aber sind das echte Straßen-Namen? Oder NPC-Jargon? Spieler-Vokabular?

**QA-Empfehlung:** Für WBB Kap 3 (Ethos) sollte Nami/Emre ein Sprachsystem definieren. Nicht obligatorisch für GDD v2, aber wichtig bis Beta.

---

### 7. Mythologie (Schöpfungsmythen, Legenden, Prophezeiungen)

**Status:** ✅ Sehr stark

**Gut:**
- Emre (WBB 01, Abschnitt 4) hat drei Schöpfungsmythen ausarbeitet — jeder mit klarer Fraktion und verstecktem Inhalt:
  - Krone: "Das Erste Siegel" (Legitimation durch kosmische Notwendigkeit)
  - Orden: "Die Prüfung" (Legitimation durch Wissen)
  - Gilden: "Der Rohstoff" (Legitimation durch Material)
- Jeder Mythos hat "Was sie verrät" + "Was sie verschweigt" — das ist Qualitäts-Struktur
- Emre schreibt explizit: "Keine ist vollständig wahr. Keine ist vollständig falsch." Das ist genau richtig.

**Kleine Lücke:**
- **Keine Volkslegenden.** Gibt es Märchen im Schlund? Übernatürliche Geschichten, die Spieler hören? Das ist Detail, kann aber in Quests eingehen.
- **Prophezeiungen?** Briefing sagt "kein High Fantasy" — also wahrscheinlich keine klassischen Prophezeiungen. Aber: Gibt es dunkle Ahnungen bei den alten NPCs?

**QA-Note:** Dieser Teil ist hervorragend. Emres mythologische Struktur ist die Stärke dieses GDD-Sets.

---

### 8. Philosophie (Weltsicht, Ethik, Wertesysteme)

**Status:** ✅ Implizit stark, könnte expliziter sein

**Gut:**
- Darius (Kap 01) hat Philosophie in die Design-Säulen eingebaut:
  - Säule I (Immersive Simulation): "Die Welt reagiert auf mich"
  - Säule II (Fraktionspolitik): "Ich wähle nicht die gute Fraktion"
  - Säule III (Körperlicher Fortschritt): "Mein Körper ist mein Fortschrittsanzeiger"
  - Säule IV (Dichte vor Breite): "Diese Welt existierte, bevor ich ankam"
- Emre (WBB 01) hat Fraktion-Philosophien in den Mythen: Materialismus (Gilden), Providentialismus (Orden), Souveränismus (Krone)
- Nami (Kap 04, Section 4.4): "Die Wahrheit ist eine Arbeit, die der Spieler leisten muss" — das ist eine Epistemologie-Statement

**Könnte ausgearbeitet werden:**
- **Spieler-Ethik** nicht explizit. Welche moralischen Dilemmata soll der Spieler erleben? "Fragment ablehnen ist Kosmologie-Wahl" (Briefing) — aber wo sind andere ethische Fragen?
- **Nihilismus-Falle.** Wenn Spieler sich in einer Welt sieht, wo "keine Fraktion gut ist," kann das existenzbedrohend wirken (was gewollt ist) oder deprimierend (was nicht gewollt ist). Wie balanciert das Design dagegen?

**QA-Note:** Philosophie ist implizit gut. Für Streamer-Alpha ist das ausreichend.

---

### 9. Verknüpfung (Wechselwirkungen zwischen Infrastrukturen)

**Status:** ✅ Sehr gut

**Übersicht der Verknüpfungen:**
```
Schwelle (Geographie)
  ↓
Schwellensubstrat (Biologie)
  ↓
Schattenfieber (Drei Stufen)
  ↓
Lymph-Subsystem (Gameplay, Darius)
  ↓
Fraktions-Reaktionen (Lore, Emre + Nami)
  ↓
Quest-Struktur (Nami)
  ↓
NPC-Motivationen (Nami)
  ↓
Spieler-Entscheidungen
```

Das ist eine lineare Kette, die aufgeht. Das ist gut. Keine Widersprüche in der Verknüpfung.

**Aber: Siehe "Widerspruchs-Log" unten.**

---

## Terminologie & Namenspolitik — KRITISCHES PROBLEM

**Bleeding Issue #1: Relikt-Labeling**

Das Briefing schreibt (siehe Memory Tag 3, Briefing-Abschnitt):
> "Schwellenanker-Name = Relikt (nicht "Relikt-Anker" oder andere Varianten)"

**Wie die Kapitel das handhaben:**

| Kapitel | Autor | Label | Zitat |
|---------|-------|-------|-------|
| GDD 01 | Darius | "Die Wurzel" | "die Wurzel als Schwellenanker ist lore-seitig gesetzt" (Zeile 238) |
| GDD 04 | Nami | "Das Relikt" + "Der Schwellenanker" | "das Relikt ist ein Schwellen-Stabilisator" (WBB 01) + "der Hauptquest dreht sich um diese Suche" (ohne Label) |
| WBB 01 | Emre | "Das Relikt" / "Schwellen-Stabilisator" | "Das Relikt ist ein Schwellen-Stabilisator." (Zeile 241) |
| GDD 06 | Tobi | "Das Relikt" | "Das Relikt -- der Schwellen-Stabilisator" (Section 6.6) |

**Das Problem:**
- Darius nennt es "Die Wurzel" — Emre definiert "Wurzelkammer" (Ort) + "das Relikt" (Objekt)
- Nami schreibt manchmal "Fragment" (das Stück), manchmal "das Relikt" (das Ganze), manchmal "Der Schwellenanker" (Label für Quest?)
- Das Briefing sagt: Der Serientitel ist "RELICS: [Relikt-Name]". Wenn das Objekt "Die Wurzel" heißt, dann "RELICS: Die Wurzel". Aber Emre nennt es "Das Relikt."

**Spielerperspektive:** Ein Spieler hört in der ersten Stunde:
1. Hieronymus übergibt "Fragment" → "Das Relikt"?
2. Boten sprechen über "Das Relikt" oder "Die Wurzel"?
3. In Quests: "Finde den Schwellenanker"?
4. Im HUD: "Quest: Das Relikt zurückbringen"?

Das ist verwirren.

**QA-Entscheidung anfordern:**
Darius + Emre + Nami müssen bis 14:00 Uhr HEUTE entscheiden:
1. **Internaler Name (Lore):** "Die Wurzel" oder "Das Relikt"?
2. **Spieler-Label (Quest/HUD):** "Das Relikt" oder "Der Schwellenanker"?
3. **Serientitel:** "RELICS: Die Wurzel" oder "RELICS: Das Relikt"?

Meine QA-Empfehlung:
- **Intern (Emre/Nami-Dialog):** "Die Wurzel" = das ursprüngliche, stabile Objekt in der Wurzelkammer. "Das Relikt" / "Das Fragment" = das Stück, das der Spieler trägt.
- **Spieler-Sicht:** "Der Schwellenanker" (allgemeiner NPC-Begriff) oder "Die Wurzel" (wenn Spieler sie findet). Nicht "das Relikt" — zu abstrakt.
- **Serientitel:** "RELICS: Die Wurzel" klingt besser als "Die Fragmente" oder "Das Relikt."

Aber das ist eine Entscheidung, nicht meine Empfehlung. **MUSS GELÖST SEIN BIS V2.**

---

## Sauberkeit — CD-Feedback-Violationen

**Bleeding Issue #2: Autor-Namen im sichtbaren Text**

CD-Feedback (Briefing-Log, Tag 3 09:00):
> "PDFs müssen sauber sein (keine Kommentare, Namen, Metadaten-Krümel)"

**Violationen gefunden:**

**In Kap 01 (Darius, Spielübersicht):**
- Zeile 4: "Quellen: Briefing, Deus Ex GDD v5.3e (Spector/Ion Storm 1997), Diablo Pitch Document (Condor 1994), **eigene Recherche-Notizen Tag 1, Emre-Output Tag 2, Nami-Notizen Tag 1, Leo-Analyse Tag 1**"
- Zeile 76: "Referenzen | Gothic 2, Deus Ex, Vampires the Masquerade: Bloodlines, Prey 2017 | **Leo (Recherche Tag 1): "Dichte statt Breite ist unser schärfstes Unterscheidungsmerkmal."**"

Das sind Quellen-Referenzen auf andere Agenten. Das ist im Arbeitsdokument okay, aber NICHT in der PDF-Freigabe. Das muss zu neutralen Labels werden: "Forschung Tag 1" statt "Leo-Analyse Tag 1", oder einfach raus.

**In Kap 04 (Nami, Schlüsselfiguren):**
- Zeile 3: "Autorin: Nami Okafor — Narrative Designer" (okay)
- Zeile 82: "Die Fragment-Übergabe ist der **Clip-Moment (Leo, 14:00 Sync)**."

Das ist ein Prozess-Kommentar. "Leo, 14:00 Sync" ist ein interner Referenz. In der Spieler-PDF hat das nichts zu suchen.

**In Kap 06 (Tobi, Tech-Spec) und WBB 01 (Emre, Mythos):**
- Keine großen Violationen, aber: WBB 01 Zeile 46: "*Design-Anmerkung: Die germanische Mythologie...*" — das ist Autor-Stimme. Sollte neutralisiert werden.

**Remediation für v2:**
- Alle "(Name, Prozess)" Kommentare entfernen
- Autor-Anmerkungen in HTML-Kommentare verschieben: `<!-- Leo: ... -->`
- Quellenreferenzen auf andere Agenten in neutrale Labels umwandeln

**Timeline:** Das ist nicht blockierend für Darius-Sync (Darius hat den Text ja gelesen), aber VOR PDF-Export (Alpha-Snapshot) muss das weg sein.

---

## Interne Konsistenz — Emres Widerspruchs-Log

**Emre hat selbst 6 Widersprüche gelistet (WBB 01, Section 7).** Das ist ehrlich und hilfreich. Aber es sind KRITISCHE Lücken.

| # | Betrifft | Problem | Leo-Bewertung |
|---|----------|---------|---------------|
| W-001 | Schwellensubstrat | Ist es Substanz oder Bedingung? | **KRITISCH** — ändert die Kosmologie. Substanz = Spieler könnte es "sammeln". Bedingung = es ist um dich herum, du kannst nicht davonlaufen. |
| W-002 | Stufe-1-Reversibilität | Wenn vollständig reversibel, warum suchen manche es auf? | **MITTEL** — logisch, aber nicht spielmechanisch blockierend. Antwort: "Kippmoment basierend auf Dosierung/Zeit" würde reichen. |
| W-003 | Biotech-Flora/Fauna | Komplett undefiniert | **HOCH** — Vera braucht Reference für visuelle Entwicklung. Emre muss mindestens 5 Beispiele haben (für WBB Kap 2). |
| W-004 | Tiervolk | Kosmologischer Ursprung unklar | **KRITISCH** — Salva ist ein wichtiger NPC, Nami hat ihn skizziert, aber: wo kommt sein Volk HER? Mutation? Eigene Spezies? Relikt-Effekt? Das ändert Erzählung fundamental. |
| W-005 | Relikt-Physik | Stabilisierungsmechanismus zu vage | **MITTEL** — nicht spielmechanisch, aber: für Glaubhaftigkeit sollte Emre eine pseudophysikalische Erklärung haben (nicht Spieler-sichtbar, aber for consistency). |
| W-006 | Zeitlinie der Öffnung | "Vor einer Generation" unkonkretisiert | **HOCH** — Nami braucht das für NPC-Alterskonistenz und Zeugenfragen. |

**QA-Empfehlung:**
- W-001, W-004, W-006 müssen bis heute 14:00 geklärt sein (vor Nami's weitere Arbeit)
- W-003 muss bis morgen geklärt sein (Vera braucht Reference)
- W-002, W-005 können bis Ende dieser Woche offen bleiben

**Emre sollte dazu angemerkt werden:** "Dein Log ist hilfreich. Statt das offen zu lassen, kannst du eine Hypothese aufschreiben — auch wenn Spieler das nie erfährt. Das ist für interne Konsistenz genug."

---

## Vollständigkeit — Wolf-Checkliste vs. Briefing

**Emre hat eine Wolf-Checkliste (WBB 01, Section 8). Feedback:**

| Infrastruktur | Abgedeckt | Zu Beta | Anmerkung |
|---|---|---|---|
| Karten | Teilweise | Vera: Detailkarte + Level-Design Constraint-Points | |
| Zeitleisten | Teilweise | Emre + Nami: konkrete Jahreszahlen, Zeugenlisten | |
| Genealogien | Nein | Nami: Fraktion-Hierarchie für Beta | |
| Natur | Minimal | Emre: 5+ Flora/Fauna-Typen + Tiervolk-Herkunft | |
| Kultur | Ja | Nami: Optional — Alltagsleben, Spiritualität vertiefen | |
| Sprache | Minimal | Emre/Nami: Dialekt + Tiervolk-Namenssystem | |
| Mythologie | Ja | Keine Lücken | |
| Philosophie | Ja | Optional — Spieler-Ethik-Dilemmata ausarbeiten | |
| Verknüpfung | Ja | Keine Lücken | |

**Spieler-Perspektive: "Erste 30 Minuten"-Checkliste**

Nach Briefing-Anforderung ("Erste Stunde muss stehen") + Leo-Memory (Alpha-Erste-Stunde-Metriken):

- **Min 0–5: Material-Klasse erkennbar?** ✅ Ja (Darius Kap 01 + Nami Kap 04: Unterschicht-Ausrüstung für Spieler)
- **Min 5–10: Emotionale Hook am sterbenden NPC?** ⚠️ Nami hat Hieronymus ausgearbeitet (gut), aber: Replikations-Zeit? Animation? VO-Zeilen? Das ist nicht-GDD-Territory, aber muss stehen.
- **Min 10–15: Skill-by-Use erste Nutzungen sichtbar?** ❌ GDD Kap 02 (Kernmechaniken) fehlt. Das ist Darius-Aufgabe, blockiert aber Bewertung. Kann nicht QA-en, bis es existiert.
- **Min 15–30: Fraktions-Asymmetrie echte Wahl?** ✅ Nami hat drei Boten mit unterschiedlichen Angeboten (gut). Aber: Wie schnell muss Spieler wählen? Da sollte Zeitdruck sein.
- **Min 30–60: Relikt fühlt sich WOW an?** ⚠️ Tobi hat Shader definiert (WOW-Potential da), aber: Wann kriegt Spieler das erste Mal echten Kontakt mit Relikt-Aktivierung? Fragment ist inert, dann... was? Das ist eine Nami/Darius-Frage (in Kap 2/3).

**Blockierend für v2:** Kap 2 (Kernmechaniken) und Kap 3 (Erzählkonzept) müssen vor dem nächsten Alpha-Test existieren. Ohne die kann ich nicht "erste 30 Min" fully evaluieren.

---

## Briefing-Konsistenz

**Checklist gegen Briefing (`simulation-2/briefing.md`):**

| Punkt | Briefing | GDD-Status | Konsistenz |
|---|---|---|---|
| **Genre:** "Medieval Cyberpunk" | ✅ Kap 01 (Darius): "Medieval Cyberpunk: frühes Spätmittelalter + High-Tech-Materialien" | ✅ |
| **Keine Steampunk** | ✅ Kap 06 (Tobi): "Kein Zahnrad. Keine Dampfmaschine." | ✅ |
| **Keine High Fantasy** | ✅ Kap 01 (Darius): "Keine Magie → Alchemie, Schattenfieber-Fähigkeiten" | ✅ |
| **Schattenfieber = einziges Übernatürlich** | ✅ WBB 01 (Emre): "Das Schattenfieber ist das einzige Übernatürliche" | ✅ |
| **Spieler = Fremder, namenlos** | ✅ Kap 04 (Nami): "Der Fremde ist eine Frage in Menschengestalt" | ✅ |
| **Drei Fraktionen, keine ist gut/böse** | ✅ Kap 01 (Darius) + WBB 01 (Emre): alle drei mit Legitimitäts-Erzählungen | ✅ |
| **Materialsprache als Macht** | ✅ Kap 01 (Darius): Material-Hierarchie nach Schicht | ✅ |
| **Immersive Sim** | ✅ Kap 01 (Darius, Säule I) | ✅ |
| **Real-Time Action, Melee** | ✅ Kap 01 (Darius) + Kap 06 (Tobi): Combat-Architektur | ✅ |
| **Premium, keine Mikrotransaktionen** | ✅ Kap 01 (Darius) + Kap 06 (Tobi) | ✅ |
| **DLCs groß, kein Content-Drip** | ✅ Kap 06 (Tobi): "DLC-Content erweitert auf stabiler Basis" | ✅ |
| **Spieler darf Fragment ablehnen** | ✅ Briefing + Memory + Nami erwähnt "Ablehnung-Option heute als halbe Seite in Kap 5" | ⚠️ **Nicht in Kap 04.** Muss in Kap 5 (Erzählkonzept, noch nicht geschrieben) kommen |
| **Schwellenanker ist Relikt-Name** | ⚠️ Briefing sagt das, aber Kapitel konsistent nicht | ❌ **SIEHE TERMINOLOGIE-PROBLEM OBEN** |

**Fazit:** 11/12 Punkte konsistent. 1 offene Schuld (Fragment-Ablehnung in Kap 5), 1 Namenspolitik-Problem (Schwellenanker vs. Relikt).

---

## Zusammenfassung: Was gut, was schlecht

### ✅ Was funktioniert hervorragend

1. **Mythologische Struktur** (Emre, WBB 01) — die drei Schöpfungsmythen sind intelligent und asymmetrisch
2. **NPC-Stimmen** (Nami, Kap 04) — jede Figur hat eine Voice, die man sofort erkennt
3. **Fraktions-Design** (Darius + Emre) — alle drei Mächte sind plausibel und haben Anreize
4. **Material-Sprache** (Darius, Kap 01) — Status wird visuell lesbar, nicht abstrakt
5. **Technische Architektur** (Tobi, Kap 06) — Shader-Struktur für Relikt und Schattenfieber ist sauber und performant
6. **Gameplay-Philosophie** (Darius, vier Säulen) — das ist eine Orientierung, keine Checkliste
7. **Verwobene Kausalität** (alle) — Schwelle → Schattenfieber → Fraktionen → Quest → Spieler-Wahl ist eine logische Kette

### ⚠️ Was muss bis v2 geklärt sein (blockierend)

1. **Relikt-Namenspolitik** — "Die Wurzel" vs. "Das Relikt" vs. "Der Schwellenanker" (ENTSCHEIDUNG bis 14:00)
2. **Emres Widerspruchs-Log W-001, W-004, W-006** — Substanz-Definition, Tiervolk-Herkunft, konkrete Zeitlinie
3. **Autor-Namen in sichtbaren Texten** — muss bis PDF-Export weg sein

### ⚠️ Was braucht Ausarbeitung bis Beta

1. **Florenferenz für Vera** — konkrete Schwellenflora/Fauna-Beispiele
2. **Genealogie-Diagramm** — Fraktions-Hierarchie mit 3–5 NPCs pro Fraktion
3. **Detailkarte** — Vera's Level-Design mit Constraint-Points für Tobi
4. **Dialektsysteme** — Sprechen Unterschicht-NPCs anders?
5. **Spieler-Ethik-Dilemmata** — mehr als "Relikt ablehnen"

---

## Abschließende Einschätzung (Spieler-Perspektive)

Wenn ich als 47k-Follower-Streamer diese Alpha-Version spielen würde (ohne Kap 2 und 3 voraus):

**Minuten 0–15:**
- Material-Klasse erkenne ich sofort ✅
- Hieronymus-Scene: emotional, nicht übertrieben, gut ✅
- Relikt-Fragment sieht aus wie... was ist das? ⚠️ (Tobi hat den Shader, aber ich muss ihn sehen)
- Drei Boten: aha, politische Wahl — gut, aber ich weiß nicht, was ich tue

**Minuten 15–30:**
- Erste Quest-Gebiet: Schichtung sichtbar? JA (Materialsprache trägt) ✅
- NPCs: Brenn, Scherer, Kast haben unterschiedliche Stimmen ✅
- Fraktions-Zugehörigkeit hat Konsequenzen? *Noch nicht sichtbar* (hängt von Kap 2 ab)

**Retention-Prognose (ohne Kap 2/3):** 70% nach 60 Min. Das ist das Ziel. Reachbar. Aber der "WOW"-Moment muss in Kap 2 oder 3 sein (Relikt-Aktivierung oder erste Combat-Sequenz mit Skill-Feedback).

**Chat-Prognose:** Leute sind neugierig, nicht begeistert. Sagen: "This looks dense. Let's see where it goes." Das ist besser als "yo this is broken" oder "zzz", aber nicht das "oh damn" der ersten 8 Min, das Retention hält.

**Für v1 → v2:** Macht. Richtung ist richtig. Braucht nur Feinschliff + Kap 2/3 um zu wissen, ob "WOW" kommt.

---

## Action Items für Darius, Emre, Nami, Tobi

**Vor 14:00 Uhr heute (für Darius-Sync):**
- [ ] **Darius + Emre + Nami:** Relikt-Namenspolitik entscheiden (Wurzel vs. Relikt vs. Schwellenanker)
- [ ] **Emre + Nami:** W-001 (Substanz-Definition), W-004 (Tiervolk), W-006 (konkrete Zeitlinie) klären

**Bis morgen früh:**
- [ ] **Emre:** 5+ Schwellenflora-Typen mit Beschreibungen (für Vera)
- [ ] **Darius/Nami:** Kap 2 (Kernmechaniken) Entwurf — vorzeigen für QA

**Bis Ende dieser Woche (vor PDF-Export für Alpha):**
- [ ] **Darius/Nami/Tobi:** Alle Autor-Namen und Prozess-Kommentare aus sichtbaren Texten entfernen
- [ ] **Vera:** Detailkarte mit Constraint-Points
- [ ] **Nami:** Genealogie-Diagramm (Fraktions-Hierarchie)

---

**QA-Report Ende.** Bereit für Diskussion.

<!-- Leo: Dieser Report ist eine ehrliche Bewertung ohne "aber es ist gut genug"-Puffer. Der Grund: Alpha-Release ist in 6 Wochen. Jede Lücke wird größer, je näher wir kommen. Besser jetzt klar machen, was offen ist, als auf dem Stream "äh, daran haben wir nicht gedacht." -->
