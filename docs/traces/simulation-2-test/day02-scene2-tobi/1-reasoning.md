# Reasoning — Tobi Richter, Tag 2 Szene 2 (WORK)

## Ausgangslage

Ich habe gestern zwei substantielle Dokumente produziert: die Machbarkeitsanalyse und die Pipeline-Architektur V0.1. Beides waren Arbeits-Dokumente für interne Abstimmung. Heute geht es darum, das in eine GDD-taugliche Struktur zu giessen.

Der Unterschied: Ein GDD-Kapitel ist kein internes Arbeitsdokument. Es muss für alle Stakeholder lesbar sein — auch für Leute, die keine Engine-Terminologie kennen. Gleichzeitig muss es technisch präzise genug sein, dass ein Programmer damit arbeiten kann.

## Strukturentscheidungen

**Warum diese Reihenfolge:**

1. **Engine & Rendering** zürst — das ist das Fundament, auf dem alles andere steht. Ü5 ist bestätigt, also kann ich hier konkret werden.

2. **Kamerasystem** direkt danach — weil es das Interface zwischen Spieler und Welt ist. Es beeinflusst Combat, Level Design, UI, Animation. Alle müssen wissen, was die Kamera kann und was nicht.

3. **Combat-Architektur** — das technisch riskanteste Subsystem. Muss früher stehen, weil Entscheidungen hier alles Nachfolgende beeinflussen (Animation-Budget, Performance-Budget, Programmer-Bedarf).

4. **Asset-Pipeline** — wie wir Inhalte produzieren. Betrifft Vera direkt, aber auch jeden, der Content anfordert.

5. **Schattenfieber-Tech** — Querschnittsthema. Betrifft Rendering, VFX, Gameplay, Narrative. Eigener Abschnitt, weil es das Alleinstellungsmerkmal ist.

6. **Performance-Ziele** — konkrete Zahlen. Ohne die ist alles andere Wunschdenken.

7. **Produktions-Pipeline** — Workflow, Tools, Versionskontrolle. Der "langweilige" Teil, der darüber entscheidet, ob wir effizient arbeiten oder im Chaos versinken.

8. **Meilensteine** — Zeitachse. Hängt an Scope-Entscheidungen, die noch nicht alle gefallen sind. Trotzdem braucht das Dokument einen zeitlichen Rahmen.

## Offene Punkte, die ich ehrlich markiere

- Combat-Middleware vs. Custom: noch nicht evaluiert
- Schattenfieber-Effekte: abhängig von Emre/Darius-Input
- Audio-Pipeline: nicht mein Gebiet, aber muss ins GDD
- Meilensteine: abhängig von Teamkapazität und Freelancer-Timing
- Konsolen-Port: als Stretch Goal erwähnt, aber technisch noch nicht analysiert

## Was ich NICHT tü

- Ich erfinde keine Performance-Zahlen, die ich nicht messen kann
- Ich verspreche keine Features, die vom Gameplay-Programmer abhängen
- Ich schreibe kein ausformuliertes Kapitel — das ist eine Outline für V1, die in der Produktionsphase (Mi-Fr) gefuellt wird
- Ich entscheide nichts allein, was Finns Bereich (Produktion, Meilensteine) betrifft — ich liefere die technische Seite, er den Produktionsplan

## Abstimmungsbedarf

- Finn: Meilensteine, Produktions-Pipeline, Team-Aufteilung
- Vera: Asset-Pipeline-Standards, Houdini-Workflow
- Darius: Combat-Architektur, GAS-Setup
- Emre: Schattenfieber-Effekte, Terrain-Biome
- Nami: Dialog-System-Anforderungen
