# Testlog — Simulation 2 Testdurchlauf

## Übersicht
- **Zeitraum**: Tag 1 (Mo) – Tag 5 (Fr)
- **Modus**: Autonom, Claude als CD
- **Ordner**: `simulation-2-test/`

## Tag 1 (Montag — Recherche)
- 6 Szenen, alle 7 Agenten aktiv
- Aufgabenverteilung: Emre=Mythologie, Darius=Referenzspiele, Nami=Narrative Strukturen, Vera=Visuelle Referenzen, Tobi=Technik, Leo=Markt, Finn=Roadmap
- CD-Entscheidungen: Hypothese C (kosmologische Erosion), nordische Quellen akzeptiert, Semi-Open-World, TP Primärmodus, UE5 bestätigt
- Keine Artefakte (planmäßig)

## Tag 2 (Dienstag — Konzeption)
- 6 Szenen. Outlines und Strukturen entstehen
- Emre entwickelt eigenes Namenssystem (Galt, Emer, Hohlicht/Mittelgrund/Stillfeld)
- Darius liefert Schattenfieber-5-Stufen-Konzept
- CD-Entscheidungen: Schattenfieber nicht heilbar, Tiervolk=Nomaden, Replay-Erfahrung gewollt, PC first
- Erste Artefakt-Strukturen in Gallery

## Tag 3 (Mittwoch — Produktion V1)
- 6 Szenen. Erster Produktionstag
- 6 V1-Dokumente fertig: WBB-01 Mythos, GDD-01 Spielübersicht, GDD-02 Kernmechaniken, GDD-03 Erzählkonzept, GDD-05 Designsprache, GDD-06 Technik
- Cross-Referenzen funktionieren (Emres Namen → Nami/Vera, Darius' Mechaniken → Tobi)
- Leo QA-Kommentare in allen Dokumenten

## Strukturanalyse (nach Tag 3)

### Was funktioniert
- Logbook: 18/18 Einträge, Schema v3 100% konform
- Artifact-Naming: alle korrekt (`KK-titel.md`)
- Wochenrhythmus: Recherche → Konzeption → Produktion sauber eingehalten
- Agent-Kohärenz: Namenssystem durchgängig, Fraktionslogik konsistent
- CD-Feedback in BRIEFINGs und REVIEWs

### Defizite (behoben ab Tag 4)
1. **Traces unvollständig ab Tag 2**: Context-Druck führte zu Zusammenfassungen statt Einzel-Spawns. Fix: Alle Agenten immer einzeln spawnen.
2. **Memories lückenhaft**: Nicht nach jeder Szene aktualisiert. Fix: GM-Checklist streng einhalten, auch PAUSE-Memories.
3. **Konversationsszenen**: Ein Agent schrieb alle Stimmen. Fix: Option A — sequentielles Turn-Taking, nicht alle müssen reden.
4. **Trace-Dateien unsortiert**: `prompt.md` statt `0-prompt.md`. Fix: Nummerierung eingeführt.

## Tag 4 (Donnerstag — Peer-Review + V2)
- 6 Szenen. Peer-Review-Tag.
- Szene 2: Alle 7 Agenten machen Cross-Reviews (Finn→GDD-01, Darius→GDD-05, Nami→GDD-02, Leo→Cross-Doc-Konsistenz, Vera→GDD-06, Tobi→WBB-01, Emre→GDD-03)
- Szene 3: Standup — Leo findet Schattenfieber-Stufengrenzen-Divergenz. CD entscheidet: Rauschen 1-40, Risse 41-75, Schwelle 76-100.
- Szene 5: V2-Überarbeitungen. GDD-02 V2 (Darius), GDD-05 V2 (Vera), GDD-06 V2 (Tobi), WBB-01 V2 Updates (Emre), GDD-03 V2 Updates (Nami), GDD-04 Outline (Nami), WBB-02 Outline (Emre)
- Szene 6: D&D One-Shot "Die Scherbe von Veld" (Emre als DM). NPC Toves = fraktionsloser Ungefüge-Prototyp.
- Neue Artefakte: WBB-02 Topos V1 Outline, GDD-04 Schlüsselfiguren Outline

## Tag 5 (Freitag — V2-Finalisierung + Wochen-Review)
- 6 Szenen. Letzter Tag.
- Szene 2: V2-Finalisierung. GDD-01 V2 (Darius), GDD-03 V2 + GDD-04 V1 (Nami), WBB-01 V2 + WBB-02 V1 (Emre), GDD-05 V2 (Vera), GDD-06 V2 (Tobi), Konsistenz-Check (Leo)
- Szene 3: Standup — Stufenzahl 75 vs. 80 diskutiert, Nami akzeptiert 75. Ymir→Emer-Fix (Leo).
- Szene 4: Pause — Vera+Tobi entwickeln Schweigehaus-Konzept ("Fehler-als-Weltaussage") und Rho-Design (Raptor-Balancepunkt, Passform als Fremdheit).
- Szene 5: Review-Vorbereitung. Leo fixt Ymir→Emer in GDD-02. QA-Abschlussbericht.
- Szene 6: Wochen-Review. Emre pitcht Emer-Anatomie, Nami pitcht 5 Schlüsselfiguren. Zwei CD-Fragen: Figur-3-Status, Emer-Anatomie.

## Endergebnis

### Artefakte (End-Stand Woche 1)
| Artefakt | Version | Autor |
|----------|---------|-------|
| GDD-01 Spielübersicht | V2 | Darius |
| GDD-02 Kernmechaniken | V2 | Darius |
| GDD-03 Erzählkonzept | V2 | Nami |
| GDD-04 Schlüsselfiguren | V1 | Nami |
| GDD-05 Designsprache | V2 | Vera |
| GDD-06 Technik/Produktion | V2 | Tobi |
| WBB-01 Mythos | V2 | Emre |
| WBB-02 Topos | V1 Outline | Emre |

### Statistiken
- **30 Logbook-Einträge** (5 Tage × 6 Szenen)
- **5 Day Summaries** (day01 bis day05)
- **~100 Trace-Dateien** (3 pro Agent pro Szene)
- **7 Agent-Memories** (kontinuierlich aktualisiert)
- **Logbook PDF**: `Meier_KIComputerRollenspiele_Sim2Test_Logbuch_2026.pdf` (85 KB)
- **Viewer Data**: `simulation.json` (5 Tage, 30 Szenen)

### Fixes umgesetzt (ab Tag 4)
1. Traces nummeriert: `0-prompt.md`, `1-reasoning.md`, `2-output.md`
2. Sequenzielles Turn-Taking in Konversationsszenen
3. Memories nach jeder Szene (work + interpersonal)
4. GM = Opus 4.6, Agents = Sonnet 4.6
5. Day Summaries nach jedem Tag
6. build-viewer-data.py: v4-Format, Agent-Memories
7. export-logbook.py: v4-Szenetypen

### Offene Punkte für nächsten Durchlauf
- fal.ai Konzeptbild-Generierung (Pipeline ready, nicht ausgeführt)
- Token/Timing-Tracking pro Agent/Szene
- Phaser-Screenshots pro Szene
- "dark fantasy" → "fantasy"
