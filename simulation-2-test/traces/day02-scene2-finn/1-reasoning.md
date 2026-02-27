# Finn — Reasoning (Tag 2, Szene 2, WORK)

## Ausgangslage

Morgen ist Mittwoch, erster Produktionstag. Alle haben heute ihre V1-Outlines vorbereitet. Die Frage ist: Wie orchestriere ich morgen sieben Leute so, dass am Ende des Tages echte V1-Dokumente stehen — und nicht sieben Leute parallel im Vakuum schreiben?

## Abhaengigkeitsanalyse

Die Roadmap hat die Kette klar:

1. **Emre: WBB-01 Mythos** ist das Fundament. Nami (GDD-03), Vera (GDD-05) und indirekt Darius (GDD-02 Schattenfieber-Mechanik) brauchen Emres Lore.
2. **Darius: GDD-01 Spieluebersicht** ist relativ unabhaengig — Briefing + eigene Referenzanalyse reichen.
3. **Darius + Leo: GDD-02 Kernmechaniken** haengt an Leos Marktdaten (liegen vor) und Emres Schattenfieber-Lore (Grundstruktur steht).
4. **Nami: GDD-03 Erzaehlkonzept** braucht WBB-01 Grundgeruest. Emre muss morgens liefern.
5. **Vera: GDD-05 Designsprache** braucht WBB-02 Topos (noch nicht da) und Fraktionsbeschreibungen (liegen vor von gestern). Vera kann mit dem starten, was sie hat — Topos-Details koennen in V2 einfliessen.
6. **Tobi: Machbarkeitsanalyse V1** ist unabhaengig.
7. **Leo: Spielerperspektiv-Check** ist nachgelagert — er braucht Darius' Entwurf.

## Zeitplanung

Der Tag hat zwei Arbeitsslots:
- Vormittag (10:00-11:30): 1,5h konzentriert
- Nachmittag (14:00-16:00): 2h konzentriert

Dazwischen Standup (11:30) und Pause (12:30).

### Kritischer Pfad

Emres WBB-01 Outline muss bis zum Standup (11:30) in einer Form vorliegen, die Nami und Vera nachmittags nutzen koennen. Nicht fertig — aber strukturiert genug als Arbeitsgrundlage.

Darius kann GDD-01 vormittags fertig schreiben (kompaktes Dokument) und nachmittags auf GDD-02 wechseln.

Leo ist vormittags unterbeschaeftigt, wenn Darius' Outline noch nicht reviewbar ist. Loesung: Leo macht vormittags den finalen Marktanalyse-Bericht fertig und steigt nachmittags als Peer-Reviewer ein.

### Peer-Review-Rhythmus

Ich will keine Endlos-Feedbackschleifen. Regel fuer morgen:
- V1-Entwurf schreiben (vormittags oder erster Nachmittagsblock)
- Ein Peer liest gegen (zweiter Nachmittagsblock oder Review-Szene)
- Korrekturen fliessen in V2 (Donnerstag)

Feste Paarungen:
- Darius <-> Leo (GDD-01 + GDD-02)
- Emre <-> Nami (WBB-01 <-> GDD-03)
- Vera bekommt Feedback von Tobi (technische Machbarkeit der visuellen Vorschlaege)
- Tobi bekommt Feedback von mir (Scope vs. Ambition)

## Freelancer-Budget

CD hat gesagt: Freelancer-Budget vorbereiten. Tobi hat identifiziert: Kein Gameplay-Programmer im Team.

Was brauchen wir?
- Jemand, der Combat-Prototyp in UE5/C++ bauen kann
- Schattenfieber-Gameplay-System (Infektionswert, Stufeneffekte)
- GAS (Gameplay Ability System) Spezialist waere ideal

Marktrecherche (grobe Schaetzung, Erfahrungswerte):
- Senior UE5 Gameplay-Programmer Freelance: 80-120 EUR/h (Deutschland)
- Geschaetzte Stunden fuer Combat-Prototyp: 160-240h (4-6 Wochen Vollzeit)
- Geschaetzte Stunden fuer Schattenfieber-System: 80-120h (2-3 Wochen)
- Gesamtschaetzung: 240-360h x 100 EUR/h (Mittelwert) = 24.000-36.000 EUR
- Puffer (+20%): 28.800-43.200 EUR

Empfehlung: Budgetrahmen 30.000-45.000 EUR einplanen. Erst ab Woche 3-4 relevant, wenn GDD-02 V2+ steht und die Mechanik-Specs klar genug fuer ein Briefing sind.

## Risiken fuer morgen

1. Emre liefert WBB-01 nicht rechtzeitig -> Nami und Vera blockiert nachmittags. Massnahme: Emre kriegt klare Deadline (11:30 Standup = Outline muss stehen).
2. Darius versucht GDD-01 und GDD-02 gleichzeitig -> beides wird halb. Massnahme: Sequenziell. GDD-01 vormittags fertig, GDD-02 nachmittags anfangen.
3. Vera hat noch keine Topos-Grundlage -> GDD-05 wird unvollstaendig. Akzeptabel: V1 deckt Fraktions-Designsprachen ab (Material liegt vor), Topos-Integration ist V2.
