# Reasoning — Tobi Richter, Tag 2 Szene 2 (WORK)

## Ausgangslage

Ich habe gestern zwei substantielle Dokumente produziert: die Machbarkeitsanalyse und die Pipeline-Architektur V0.1. Beides waren Arbeits-Dokumente fuer interne Abstimmung. Heute geht es darum, das in eine GDD-taugliche Struktur zu giessen.

Der Unterschied: Ein GDD-Kapitel ist kein internes Arbeitsdokument. Es muss fuer alle Stakeholder lesbar sein — auch fuer Leute, die keine Engine-Terminologie kennen. Gleichzeitig muss es technisch praezise genug sein, dass ein Programmer damit arbeiten kann.

## Strukturentscheidungen

**Warum diese Reihenfolge:**

1. **Engine & Rendering** zuerst — das ist das Fundament, auf dem alles andere steht. UE5 ist bestaetigt, also kann ich hier konkret werden.

2. **Kamerasystem** direkt danach — weil es das Interface zwischen Spieler und Welt ist. Es beeinflusst Combat, Level Design, UI, Animation. Alle muessen wissen, was die Kamera kann und was nicht.

3. **Combat-Architektur** — das technisch riskanteste Subsystem. Muss frueher stehen, weil Entscheidungen hier alles Nachfolgende beeinflussen (Animation-Budget, Performance-Budget, Programmer-Bedarf).

4. **Asset-Pipeline** — wie wir Inhalte produzieren. Betrifft Vera direkt, aber auch jeden, der Content anfordert.

5. **Schattenfieber-Tech** — Querschnittsthema. Betrifft Rendering, VFX, Gameplay, Narrative. Eigener Abschnitt, weil es das Alleinstellungsmerkmal ist.

6. **Performance-Ziele** — konkrete Zahlen. Ohne die ist alles andere Wunschdenken.

7. **Produktions-Pipeline** — Workflow, Tools, Versionskontrolle. Der "langweilige" Teil, der darueber entscheidet, ob wir effizient arbeiten oder im Chaos versinken.

8. **Meilensteine** — Zeitachse. Haengt an Scope-Entscheidungen, die noch nicht alle gefallen sind. Trotzdem braucht das Dokument einen zeitlichen Rahmen.

## Offene Punkte, die ich ehrlich markiere

- Combat-Middleware vs. Custom: noch nicht evaluiert
- Schattenfieber-Effekte: abhaengig von Emre/Darius-Input
- Audio-Pipeline: nicht mein Gebiet, aber muss ins GDD
- Meilensteine: abhaengig von Teamkapazitaet und Freelancer-Timing
- Konsolen-Port: als Stretch Goal erwaehnt, aber technisch noch nicht analysiert

## Was ich NICHT tue

- Ich erfinde keine Performance-Zahlen, die ich nicht messen kann
- Ich verspreche keine Features, die vom Gameplay-Programmer abhaengen
- Ich schreibe kein ausformuliertes Kapitel — das ist eine Outline fuer V1, die in der Produktionsphase (Mi-Fr) gefuellt wird
- Ich entscheide nichts allein, was Finns Bereich (Produktion, Meilensteine) betrifft — ich liefere die technische Seite, er den Produktionsplan

## Abstimmungsbedarf

- Finn: Meilensteine, Produktions-Pipeline, Team-Aufteilung
- Vera: Asset-Pipeline-Standards, Houdini-Workflow
- Darius: Combat-Architektur, GAS-Setup
- Emre: Schattenfieber-Effekte, Terrain-Biome
- Nami: Dialog-System-Anforderungen
