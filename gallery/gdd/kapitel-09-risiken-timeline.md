---
agent: finn
day: 3
task: "GDD Kapitel 9: Risiken, Entscheidungen & Timeline"
memories_referenced: [finn-014, finn-018, finn-022, finn-025]
feedback_received: [cd-day2-kernvision, cd-day3-morning, cd-day3-biotech]
status: draft
---

# Kapitel 9 — Risiken, Entscheidungen & Timeline

> *Das hier ist das Kapitel, das niemand gern schreibt und das alle brauchen. Ich bin Producer. Das IST mein Job.*
> *— F. Bergmann, Tag 3*

---

## 1. Offene Entscheidungen

Dinge, die noch nicht geklärt sind. Nicht vergessen — bewusst offen. Jede braucht eine Entscheidung, bevor wir in die Produktion gehen.

### 1.1 Endgültige Fraktionsnamen (deutsch)

**Status**: OFFEN
**Verantwortlich**: Emre + Nami
**Deadline**: GDD v0.2

"Höhlenvolk", "Küstenvolk", "Siedlervolk", "Innenvolk" sind Arbeitstitel. Für das GDD reicht das. Für die Weltenbau-Bibel nicht. Emre braucht ein linguistisches Fundament — er hat das selbst angemerkt. Nami hat angeboten, Sprachpaletten pro Fraktion zu entwickeln, aus denen sich dann Eigennamen ableiten lassen.

**Risiko bei Verzögerung**: Gering. Arbeitstitel funktionieren intern. Wird erst kritisch bei Concept Art (Vera braucht Namen für Asset-Ordner) und bei der WBB.

### 1.2 Festungs-Herkunft

**Status**: OFFEN
**Verantwortlich**: Emre
**Deadline**: WBB v0.1

Wer hat die Festung in der Startregion gebaut? Siedlervolk? Eine ältere Zivilisation? Die Titanen selbst? Das beeinflusst die gesamte Architektur-Sprache der Startregion und damit Veras Concept Art.

**Risiko bei Verzögerung**: Mittel. Vera kann mit Platzhalter-Architektur arbeiten, aber nicht ewig.

### 1.3 Vampir/Werwolf-Integration

**Status**: VERSCHOBEN (CD-Entscheidung)
**Verantwortlich**: CD + Darius
**Deadline**: Nach Vertical Slice

CD hat klar gesagt: Phase 2, lowkey. Das heißt: Nicht im Vertical Slice, nicht im GDD v0.1 als Kernsystem. Aber wir müssen die Welt so bauen, dass es PASST, wenn es kommt. Emre und Nami sollten in der WBB zumindest einen Platzhalter haben — eine Legende, ein Gerücht, ein verschlossenes Kapitel.

**Risiko bei Verzögerung**: Gering, solange die Weltarchitektur erweiterbar bleibt.

### 1.4 Konkrete Fähigkeitenbäume pro Nervensystem-Zweig

**Status**: OFFEN
**Verantwortlich**: Darius
**Deadline**: GDD v0.2

Das Nervensystem-Leveling ist konzeptionell stark (Tag 2, CD-Briefing). Aber: Welche konkreten Fähigkeiten hängen an welchem Zweig? Sensorisch, Motorisch, Kognitiv — das sind Kategorien, keine Skill-Trees. Darius muss das mit Leo durchspielen: Fühlt es sich gut an? Versteht ein Spieler intuitiv, was "Ich investiere in meinen Sehnerv" bedeutet?

**Risiko bei Verzögerung**: Hoch. Das ist DAS Alleinstellungsmerkmal. Ohne konkrete Bäume kann Tobi keinen UI-Prototyp bauen.

### 1.5 Map-Größe und Traversal-Systeme

**Status**: OFFEN
**Verantwortlich**: Darius + Tobi
**Deadline**: Vertical Slice Design

Wie groß ist die Startregion? Wie bewegt sich der Spieler? Reittiere? Schnellreise? Die Antwort bestimmt, wie viel Content Emre und Nami für die Startregion schreiben müssen und wie viele Assets Vera braucht.

**Risiko bei Verzögerung**: Hoch. Ohne Map-Scope kann niemand sauber planen.

---

## 2. Risikomatrix

| # | Risiko | Schwere | Wahrscheinlichkeit | Bewertung | Verantwortlich |
|---|--------|---------|---------------------|-----------|----------------|
| R1 | Skyrim-Kamera FP/TP | Hoch | Mittel | **HIGH** | Tobi + Darius |
| R2 | MetaHuman Fellträger Kopf-Swap | Mittel | Mittel | **MEDIUM** | Tobi + Vera |
| R3 | Nervensystem-Leveling UI | Hoch | Hoch | **HIGH** | Darius + Tobi |
| R4 | Scope: Vollständige Insel vs. Region | Mittel | Hoch | **MEDIUM** | Finn + CD |
| R5 | Biotech/Drogen-Thematik: USK | Mittel | Niedrig | **LOW-MEDIUM** | Leo + Finn |

### R1 — Skyrim-Kamera FP/TP (HIGH)

**Was**: RELICS soll wie Skyrim zwischen First Person und Third Person wechselbar sein. Das klingt einfach. Es ist es nicht.

**Warum HIGH**: Jedes Feature, jedes UI-Element, jeder Kampfmove muss in BEIDEN Perspektiven funktionieren und getestet werden. Das verdoppelt nicht den Aufwand — aber es erhöht ihn um geschätzt 30-40% bei allem, was mit Kamera, Animation und UI zu tun hat.

**Mitigation**:
- Tobi erstellt einen Kamera-Prototyp als erstes technisches Deliverable
- Fallback-Option: Eine Perspektive als "primär" definieren, die andere als eingeschränkt (z.B. FP nur in Interiors, TP in Open World)
- CD-Entscheidung nötig, falls Fallback greift

### R2 — MetaHuman Fellträger Kopf-Swap (MEDIUM)

**Was**: Die Tiermenschen (Höhlenvolk) sollen MetaHuman-Körper mit nicht-menschlichen Köpfen haben. Fellträger mit Tier-Features. Das ist kein Standard-MetaHuman-Workflow.

**Warum MEDIUM**: Technisch machbar (Mesh-Swap, Custom-Bones), aber es gibt keine fertige Pipeline dafür. Tobi braucht R&D-Zeit, und Vera braucht die technischen Constraints, bevor sie Concept Art finalisiert.

**Mitigation**:
- Tobi: 2-Tage-Spike für Head-Swap-Prototyp
- Vera: Concept Art in zwei Varianten (mit/ohne technische Einschränkungen)
- Fallback: Subtilere Tiermenschen (Ohren, Augen, Zähne statt voller Tierkopf)

### R3 — Nervensystem-Leveling UI (HIGH)

**Was**: Das Nervensystem als Skill-Tree-Visualisierung ist ein völlig neues UI-Paradigma. Es gibt keine Referenz, die man nachbauen kann. Kein Spiel hat das gemacht.

**Warum HIGH**: Kein Referenzdesign bedeutet: Trial and Error. Spieler müssen intuitiv verstehen, was sie tun. Wenn die UI nicht sofort klar ist, stirbt das ganze System — egal wie gut die Mechanik dahinter ist.

**Mitigation**:
- Darius: Papier-Prototyp des Nervensystem-UI bis Ende Woche
- Leo: Spielertest mit dem Papier-Prototyp (sie hat Zugang zu ihrer Community)
- Tobi: Technischer Prototyp erst NACH positivem Spielertest
- Vera: Art Direction für die UI parallel zur Mechanik-Definition

### R4 — Scope: Vollständige Insel vs. Region (MEDIUM)

**Was**: Bauen wir die gesamte Insel für den Vertical Slice — oder nur eine Region? Die CD hat von einer Startregion gesprochen, aber die Ambitionen im Team tendieren zur ganzen Insel.

**Warum MEDIUM**: Eine ganze Insel ist Monate mehr Arbeit. Eine Region ist in Wochen machbar. Die Entscheidung bestimmt den gesamten Zeitplan.

**Mitigation**:
- Vertical Slice = EINE Region. Punkt.
- Die Region muss repräsentativ sein: mindestens drei Fraktionen sichtbar, ein Knochenturm, eine Siedlung, ein Dungeon
- Emre und Nami planen die Welt so, dass sie modular erweiterbar ist
- CD-Entscheidung: Ist der Vertical Slice eine Stunde Gameplay oder drei?

### R5 — Biotech/Drogen-Thematik: USK (LOW-MEDIUM)

**Was**: Das Innenvolk arbeitet mit Giften, Drogen, Amphetaminen, Körpermodifikation. Die CD hat das bewusst als Feature gesetzt. Aber: USK-Rating.

**Warum LOW-MEDIUM**: In Deutschland ist Drogenkonsum in Spielen ein Rating-Thema. Nicht verboten, aber es kann den Unterschied zwischen USK 16 und USK 18 machen. Das beeinflusst Marketing und Zielgruppe.

**Mitigation**:
- Leo: Recherche zu USK-Präzedenzfällen (Cyberpunk 2077, Disco Elysium)
- Narrativ: Drogen als Konsequenz zeigen, nicht als Verherrlichung — das ist ohnehin Namis und Emres Ansatz
- Fallback: "Substanzen" statt "Drogen", abstrakte Darstellung statt grafische
- Frühzeitig USK-Beratung einholen (kostet nichts, spart Überraschungen)

---

## 3. Entscheidungsmatrix

### Von der CD entschieden (fix)

| Entscheidung | Tag | Kontext |
|-------------|-----|---------|
| Dark Fantasy CRPG als Genre | Tag 1 | Kernbriefing |
| Skyrim-Kamera FP/TP | Tag 1 | Kernbriefing |
| Titanen als Weltfundament | Tag 1 | Kernbriefing |
| Fünf Fraktionen (statt drei) | Tag 3 | CD-Feedback zu Namis v1 |
| Tiermenschen = Händler & Diebe, nicht Handwerker | Tag 3 | CD-Korrektur |
| Biotech/Chemie statt Steampunk | Tag 3 | CD-Briefing |
| Nervensystem-Leveling als Skill-System | Tag 2 | CD-Briefing |
| Vampir/Werwolf = Phase 2, lowkey | Tag 3 | CD-Klarstellung |
| Kein GaaS, Premium-Modell | Tag 2 | CD-Vorgabe |
| MetaHuman + UE5 als Tech-Basis | Tag 1 | Kernbriefing |

### Noch offen (braucht CD-Input)

| Frage | Wer braucht die Antwort? | Dringlichkeit |
|-------|--------------------------|---------------|
| Vertical Slice Scope (1h oder 3h Gameplay?) | Alle | HOCH |
| FP/TP: Gleichwertig oder eine Perspektive primär? | Tobi, Darius | HOCH |
| Wie explizit darf Biotech/Drogen sein? | Nami, Leo | MITTEL |
| Companion-Limit (wie viele gleichzeitig?) | Darius, Nami | MITTEL |
| Ton des Spiels: Düster-ernst oder mit Humor? | Nami | MITTEL |
| Endgame-Vision: Was passiert im letzten Akt? | Darius, Emre | NIEDRIG (noch) |

---

## 4. Meilensteine

| Meilenstein | Deliverable | Zieldatum | Status |
|-------------|-------------|-----------|--------|
| **MS0** | GDD v0.1 — Alle Kapitel als Entwurf | Tag 4 (morgen, Donnerstag) | In Arbeit |
| **MS1** | WBB v0.1 — Weltenbau-Bibel erster Entwurf | Tag 5 (Freitag) | Geplant |
| **MS2** | Vertical Slice Prototype — Spielbare Startregion | TBD (nach GDD-Review) | Nicht begonnen |
| **MS3** | Streamer-Alpha — Erste externe Spieler | TBD | Nicht begonnen |

### MS0: GDD v0.1 (morgen)

**Was fertig sein muss**:
- Alle 9 Kapitel als Entwurf vorhanden (nicht perfekt, aber vollständig)
- Jedes Kapitel beantwortet die Kernfragen seines Bereichs oder dokumentiert sie als offen
- CD-Review am Donnerstagnachmittag
- Kapitel 1 und 3 sind am weitesten — Darius und Nami/Emre haben vorgearbeitet

**Was NICHT fertig sein muss**:
- Finales Layout, Grafiken, Concept Art im GDD
- Vollständige Skill-Trees oder Item-Listen
- Technische Spezifikation im Detail (Tobi: "Gebt mir die Design-Entscheidungen, dann geb ich euch die Specs")

### MS1: WBB v0.1 (Freitag)

**Was das ist**: Die Weltenbau-Bibel. Emres und Namis Domäne. Kosmogonie, Fraktionen, Geographie, Sprachen, Geschichte. Alles, was der Vertical Slice braucht, um sich wie eine echte Welt anzufühlen.

**Abhängigkeit**: Baut auf dem GDD auf. Kapitel 2 und 3 des GDD werden die Basis.

### MS2: Vertical Slice Prototype (TBD)

**Was das ist**: Die erste spielbare Stunde. Startregion, erster Knochenturm, erste Fraktionsbegegnung. Keine finale Grafik, aber spielbare Mechaniken.

**Warum TBD**: Weil wir den Scope noch nicht definiert haben (siehe R4). Ohne CD-Entscheidung zur Map-Größe kann ich keinen realistischen Termin setzen.

### MS3: Streamer-Alpha (TBD)

**Was das ist**: Leos Idee. Eine Version, die ausgewählte Streamer spielen können. Kein öffentliches Early Access — gezieltes Seeding für Community-Aufbau.

**Warum TBD**: Hängt von MS2 ab. Frühestens 4-6 Wochen nach dem Vertical Slice.

---

## 5. Nächste Schritte (nach dem GDD)

### Sofort (Tag 4-5)
1. **Alle**: GDD-Kapitel-Entwürfe abgeben (Deadline: Donnerstag Abend)
2. **CD**: GDD v0.1 Review (Donnerstag Nachmittag/Freitag Morgen)
3. **Emre + Nami**: WBB v0.1 parallel starten (Freitag als Ziel)
4. **Darius**: Nervensystem-Papierprototyp
5. **Finn**: GDD zusammenführen, Formatierung, Lücken markieren

### Nächste Woche
6. **Tobi**: Kamera-Spike (FP/TP-Prototyp in UE5)
7. **Vera**: Concept Art für Startregion (basierend auf Emres Geographie)
8. **Leo**: USK-Recherche + Vertical Slice Walkthrough (mit Darius)
9. **Finn**: Timeline für MS2 aufsetzen (nach CD-Scope-Entscheidung)

### Entscheidungen, die wir DIESE Woche noch brauchen
- [ ] Vertical Slice Scope (CD)
- [ ] FP/TP Priorisierung (CD + Darius + Tobi)
- [ ] Map-Größe Startregion (CD + Emre)

---

## 6. Was dieses Kapitel nicht ist

Dieses Kapitel ist kein Pessimismus. Die Risiken sind real, aber keines davon ist ein Showstopper. Wir haben ein Team, das seine Arbeit versteht. Wir haben eine Creative Director, die klare Entscheidungen trifft. Und wir haben einen Zeitplan, der ambitioniert ist, aber nicht unmöglich.

Mein Job ist es, die Probleme zu sehen, bevor sie Probleme werden. Dieses Kapitel ist mein Werkzeug dafür. Wenn in drei Wochen jemand fragt "Hat uns niemand vor dem Kamera-Problem gewarnt?" — dann schlage ich Seite 1 auf und sage: Doch. Haben wir.

---

*Karteikarte ans Kanban-Board: "RISIKEN SIND KEINE AUSREDEN. RISIKEN SIND ARBEIT, DIE NOCH KEINEN TERMIN HAT."*

*Zweite Karteikarte, kleiner: "Emre, dein Kapitel ist morgen fällig. Ich meine es ernst. Mit Liebe, aber ernst."*

— Finn
