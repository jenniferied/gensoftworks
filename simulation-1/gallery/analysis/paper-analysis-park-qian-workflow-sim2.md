---
agent: game-master
day: pre-sim
task: "Workflow-Analyse Park et al. (2023) & Qian et al. (2024) für Simulation 2"
sources:
  - "Park et al. 2023 — Generative Agents: Interactive Simulacra of Human Behavior (UIST 2023)"
  - "Qian et al. 2024 — ChatDev: Communicative Agents for Software Development (ACL 2024)"
status: final
---

# Analyse: Generative Agents & ChatDev — Workflow-Optimierung für Simulation 2

## 1. Architektur-Vergleich

### Smallville (Park et al.): Sandbox-Loop
- **Takt**: Zeitbasiert (Sandbox-Ticks, ~15 min Intervalle). Jeder Tick: Perceive -> Retrieve -> Plan/React -> Act
- **Orchestrierung**: Zentraler Sandbox-Server steuert den Loop. Agenten sind reaktiv -- sie werden gepollt ("Was machst du jetzt?")
- **Emergenz**: Verhalten ist emergent. Kein Agent hat eine feste Pipeline. Valentine's-Day-Party entsteht aus einer einzigen Seed-Idee
- **Schwaeche**: Extrem token-teuer (~1M tokens/agent/tag). Viele Ticks erzeugen banale Beobachtungen ("Kuehlschrank ist leer")

### ChatDev (Qian et al.): Chat-Chain
- **Takt**: Aufgabenbasiert (Chat Chain = sequenzielle Phasen). Design -> Coding -> Code Complete -> Review -> Testing
- **Orchestrierung**: Instructor-Assistant-Dyaden pro Subtask. CEO instruiert CTO, CTO instruiert Programmer etc. Streng sequenziell
- **Produktion**: Deterministisch. Klar definierter Output pro Phase. Jede Phase hat Abbruchbedingung (Konsens oder max 10 Runden)
- **Schwaeche**: Starr. Kein emergentes Verhalten. Keine persistente Memory zwischen Tasks. Agenten sind stateless

### Was passt besser zu Claude Code?

**Weder noch in Reinform.** GenSoftworks hat mit dem Concordia-inspirierten Scene-basierten Ansatz bereits die richtige Synthese gefunden:

| Eigenschaft | Smallville | ChatDev | GenSoftworks (aktuell) |
|---|---|---|---|
| Taktung | Zeitbasiert (Ticks) | Aufgabenbasiert (Phases) | **Szenenbasiert (narrative Beats)** |
| Orchestrierung | Server-Loop | Chat Chain | **Game Master (Claude Session)** |
| Agenten-Autonomie | Hoch (reagieren frei) | Niedrig (folgen Instruktionen) | **Mittel (reagieren in Szenenkontext)** |
| Emergenz | Stark | Keine | **Moeglich, aber gerahmt** |
| Output-Kontrolle | Schwach | Stark | **Mittel (CD-Feedback)** |

**Kerninsight**: ChatDevs Chat-Chain loest ein Problem, das GenSoftworks nicht hat (Code generieren), aber sein Strukturierungs-Prinzip -- Phasen mit klaren Subtasks und Abbruchbedingungen -- ist uebertragbar auf die Game-Master-Orchestrierung.

---

## 2. Memory & State

### Park et al.: Memory Stream + Embedding-Retrieval
- **Speicherung**: SQLite + ChromaDB (Vektor-DB)
- **Retrieval**: `score = a_recency * recency + a_importance * importance + a_relevance * relevance` (Gewichte: 0.5, 3.0, 2.0)
- **Reflection**: Threshold-basiert (Summe der Importance-Scores >= 150). Generiert 3-5 Higher-Order-Insights aus den letzten ~100 Beobachtungen. Reflections werden selbst zu Memories (Depth+1)
- **Planning**: Top-down daily plan -> rekursive Dekomposition in 5-15-Min-Bloecke

### Qian et al.: Short-Term + Long-Term Memory
- **Short-Term**: Aktuelle Phase-Utterances (Instructor-Assistant-Paare)
- **Long-Term**: Nur *Solutions* frueherer Phasen, nicht die vollen Dialoge. Wird als komprimierter Kontext an die naechste Phase weitergegeben
- **Kein Reflection**: Kein Mechanismus fuer Selbst-Synthese
- **Kein Importance-Scoring**: Alles wird gleich behandelt

### Was ist in JSONL ohne Vektordatenbank realistisch?

GenSoftworks' bestehender Ansatz (blueprint/02) ist bereits gut designed. Konkrete Optimierungen fuer Sim 2:

**Beibehalten:**
- JSONL Memory Streams (skaliert fuer Monate bei ~10-20 Memories/Agent/Tag)
- Claude als Retrieval-Engine (kein Embedding noetig bei der Datenmenge)
- Tag-basiertes Pre-Filtering
- Importance-Scoring durch den Agenten selbst (kein Extra-Call)

**Vereinfachen:**
- **Weg mit dem `importance_accumulator` als separatem State-Feld.** Stattdessen: Game Master prueft nach jedem Tag, ob ein Agent seit der letzten Reflection genug hochwertige Memories gesammelt hat. Einfacher `jq`-Einzeiler statt State-Tracking
- **Planning radikal kuerzen**: Park et al.s rekursive 5-Min-Dekomposition ist Overkill. ARRIVAL-Szene mit 2-3 Saetzen pro Agent reicht (so wie in Sim 1 bereits praktiziert)

**Hinzufuegen:**
- **ChatDevs Long-Term-Memory-Prinzip**: Zwischen Tagen nur *Conclusions* (Reflections + Artifacts) weiterreichen, nicht den vollen Szenen-Kontext. Das haelt den Prompt fuer Tag N+1 schlank

---

## 3. Kommunikationsprotokolle

### Park et al.: Peer-to-Peer mit Proximity-Trigger
- Agenten bemerken einander wenn sie raeumlich nah sind
- Bilateral: Agent A und B generieren Dialog abwechselnd
- Jeder Agent bedingt seine Aeusserungen auf eigene Memories ueber den Gespraechspartner
- Kein Mediator -- der Sandbox-Server macht nur das Matching, nicht den Inhalt

### Qian et al.: Instructor-Assistant-Dyaden
- Immer genau 2 Rollen pro Subtask
- Instructor stellt Aufgabe, Assistant antwortet
- **Inception Prompting**: Beide erhalten symmetrische System-Prompts mit Rolleninfo, Aufgabe, und Kommunikationsprotokoll
- **Communicative Dehallucination**: Assistant fragt aktiv nach Details zurueck bevor er antwortet (Role Reversal)
- Max 10 Kommunikationsrunden pro Subtask

### Empfehlung fuer GenSoftworks

**Aktuelles Problem**: In Sim 1 generierte der Game Master Dialog, indem er Agenten parallel spawnte und dann deren Antworten "verwebte" (blueprint/04: Pattern A). Das funktioniert, hat aber zwei Schwaechen:
1. Agenten antworten ins Leere -- sie wissen nicht, was der andere sagt
2. Der Game Master muss alles reconcilen

**Empfohlenes Protokoll fuer Sim 2 -- Hybrid aus beiden Papers:**

- **Fuer ENCOUNTER (2 Agenten)**: ChatDevs Dyaden-Prinzip. Agent A wird gespawnt -> Antwort. Agent B wird mit A's Antwort als Input gespawnt -> Antwort. 2-3 Runden. Game Master moderiert, aber die Agenten reden *miteinander*, nicht *parallel ins Nichts*
- **Fuer MEETING (3+ Agenten)**: Moderierter Round-Robin. Game Master als Moderator stellt Fragen, Agenten antworten sequenziell mit Kontext der vorherigen Antworten
- **Fuer WORK (1-2 Agenten)**: Einfacher Single-Agent-Call. Kein Dialog noetig
- **Fuer ARRIVAL**: Parallel Spawn wie bisher -- hier ist Dialog nicht noetig, nur Deklarationen

**Token-Effizienz**: Sequenzieller Dialog kostet mehr Tokens als Parallel-Spawn, liefert aber wesentlich natuerlichere Interaktionen. Der Tradeoff lohnt sich bei 2-3 Encounter-Szenen pro Tag.

---

## 4. Rollen & Spezialisierung

### ChatDev: Feste Rollen, Aufgaben-gebunden
- CEO, CTO, Programmer, Reviewer, Tester
- Jede Rolle hat einen fixen System-Prompt
- Rollen sind **funktional**: Die Rolle bestimmt, *was* der Agent tut
- Ablation zeigt: Ohne Rollenbezeichnung faellt Output-Qualitaet massiv (Quality von 0.3953 auf 0.2212)

### Smallville: Emergente soziale Rollen
- Nur Persona-Beschreibung (1 Paragraph), keine funktionale Rolle
- Rollen emergieren: "Isabella organisiert die Party" war nicht programmiert
- **Sozialer Kontext**, nicht funktionaler: "John Lin is a pharmacy shopkeeper who loves to help people"

### GenSoftworks: Hybrid -- und das ist richtig

GenSoftworks hat 7 Agenten mit:
- **Starker Persona** (Alter, Persoenlichkeit, Gewohnheiten, Referenzen -- a la Smallville)
- **Funktionaler Spezialisierung** (Worldbuilder, Game Designer, etc. -- a la ChatDev)
- **Kein Instructor/Assistant-Split**: Jeder Agent ist autonom

**Was ChatDevs Ablation beweist und was wir daraus lernen**:
- Die Rollenzuweisung in System-Prompts ist der wichtigste Hebel fuer Output-Qualitaet (8 Standardabweichungen Effekt!)
- GenSoftworks hat das bereits gut geloest -- die Agent-Definitionen in `.claude/agents/` sind detailreicher als ChatDevs Rollen-Prompts

**Konkreter Verbesserungsvorschlag**: ChatDevs **Communicative Dehallucination** in die Agent-Prompts aufnehmen. Agenten sollten instruiert werden, bei Unsicherheit *nachzufragen* statt zu fabrizieren. Beispiel: Wenn Vera ein Konzeptbild erstellen soll, aber die Beschreibung unklar ist, soll sie Emre explizit nach Details fragen -- innerhalb der Szene, nicht als Meta-Eskalation.

---

## 5. Schluesselmechanismen zum Uebernehmen

### 1. Sequenzieller Dialog statt Parallel-Spawn (ChatDev -> GenSoftworks)
**Warum**: In Sim 1 waren Dialoge oft generisch, weil Agenten nicht aufeinander reagierten. ChatDevs Instructor-Assistant-Muster zeigt: Sequenzielle Runden mit echtem Informationsaustausch erzeugen besseren Output. Die Ablation zeigt, dass jede zusaetzliche Review-Runde die Quality steigert.
**Implementierung**: ENCOUNTER-Szenen auf 2-3 sequenzielle Agent-Calls umstellen.

### 2. Long-Term-Memory als Conclusion-Bridge (ChatDev -> GenSoftworks)
**Warum**: ChatDevs Ansatz, nur *Solutions* zwischen Phasen weiterzugeben (nicht den vollen Dialog), ist ein exzellentes Prinzip fuer Tag-zu-Tag-Uebergaenge. Statt allen 50 letzten Memories den Agenten-Prompt vollzupacken, koennten Tages-Summaries als komprimierte Eingabe dienen.
**Implementierung**: Am Ende jedes Tags generiert der Game Master ein 5-10-Zeilen "Tages-Digest" pro Agent, das am naechsten Tag als Kontext-Bridge dient. Memories bleiben in JSONL fuer Deep-Retrieval, aber der Standard-Kontext wird schlank.

### 3. Reflection beibehalten, aber fixer takten (Park et al. -> GenSoftworks)
**Warum**: Park et al.s Ablation beweist: Reflection ist der zweitwichtigste Mechanismus nach Memory selbst (TrueSkill 26.88 ohne Reflection vs. 29.89 mit). Der Importance-Accumulator-Mechanismus ist allerdings unnoetig komplex fuer 7 Agenten.
**Implementierung**: Fixe Reflection alle 2-3 Tage statt dynamischem Threshold. Einfacher, vorhersagbarer, gleicher Effekt.

### 4. Communicative Dehallucination (ChatDev -> GenSoftworks)
**Warum**: Agenten neigen dazu, unscharfe Briefs zu "halluzinieren" statt nachzufragen. ChatDevs Mechanismus -- der Assistant fragt aktiv zurueck -- reduziert dieses Problem signifikant.
**Implementierung**: Satz in die Agent-System-Prompts: "Wenn dir Informationen fehlen, frage explizit nach -- erfinde nichts."

### 5. Game-Master-gesteuerte Scene-Selection (Concordia/Park -> beibehalten)
**Warum**: Sowohl Park et al.s Sandbox als auch ChatDevs Chat Chain haben einen Nachteil: die Orchestrierung ist mechanisch. GenSoftworks' Game Master mit narrativem Urteil ist die wichtigste architektonische Staerke. Beibehalten und staerken.
**Implementierung**: Game Master bekommt am Tagesbeginn ein explizites "Scene Menu" mit bewerteten Optionen, waehlt begruendet.

---

## 6. Was weglassen

### Aus Park et al. (Smallville)

- **Tick-basierte Simulation**: Irrelevant. 36-96 Ticks/Tag waere Token-Selbstmord. Scene-basiert ist korrekt
- **Spatial Movement / Pathfinding**: GenSoftworks braucht keine echte Raum-Navigation. Positionen sind dekorativ fuer den Viewer, nicht funktional
- **Embedding-basiertes Retrieval**: Bei 7 Agenten und ~100 Memories/Woche ist Claude-as-Search-Engine voellig ausreichend. ChromaDB waere Over-Engineering
- **Recursively decomposed Plans** (5-15 Min Bloecke): Unsere Agenten brauchen keine minutengenauen Plaene. Ein ARRIVAL mit 2-3 Bullet Points reicht
- **Environment Tree / Object States**: "Kuehlschrank ist leer", "Kaffeemaschine brueht" -- fuer ein kreatives Studio unnoetiges Mikro-Detail

### Aus Qian et al. (ChatDev)

- **Waterfall-Pipeline (Design -> Coding -> Testing)**: GenSoftworks ist kein sequenzieller Prozess. Creative Work ist iterativ, nicht linear
- **Stateless Agenten**: Diametral entgegengesetzt zu unserem Kern-Design. Unsere Agenten *muessen* sich erinnern
- **"Communicative Dehallucination" als separate Phase**: Der Mechanismus ist gut, aber als explizite Phase mit Role-Reversal zu komplex. Besser als Instruktion im System-Prompt
- **5 Subtasks pro Phase**: Zu granular fuer kreative Arbeit. Unsere Scene-Types (ARRIVAL, ENCOUNTER, WORK, MEETING, REFLECTION) sind die richtige Granularitaet
- **Double-Agent pro Subtask** (immer Instructor + Assistant): Bei WORK-Szenen arbeitet ein Agent allein. Den Zwang zu Dyaden brauchen wir nicht

### Grundsaetzlich irrelevant

- **Code-Generierung / Compilation / Testing**: ChatDevs Kern-Use-Case (Software schreiben) ist nicht unserer
- **25 Agenten**: Smallvilles Skala ist fuer uns Overhead. 7 spezialisierte Agenten > 25 generische
- **Benchmarking-Metriken** (Completeness, Executability): Nicht auf kreative Artefakte uebertragbar

---

## 7. Konkreter Workflow-Vorschlag: Simulation 2 -- Streamlined Day

```
GAME MASTER: TAG STARTEN
  1. state/ lesen (world.json, agents/*.json)
  2. Letzte Tages-Digests lesen (state/digests/)
  3. bulletin.json pruefen (CD-Feedback?)
  4. Scene Menu generieren:
     "Heute relevant: Emre schuldet Vera Feedback,
      CD-Brief zu Tiervolk-Design unbeantwortet,
      Nami hat Reflection-Threshold erreicht"
         |
         v
SZENE 1: ARRIVAL (obligatorisch)
  Parallel-Spawn aller 7 Agenten:
  Input: Persona + Tages-Digest + Bulletin
  Output: today_plan (2-3 Saetze), mood

  Game Master: Plaene reconcilen, Synergien/
  Konflikte notieren, restliche Szenen planen
         |
         v
SZENEN 2-4: KERN-LOOP (variabel)
  Game Master waehlt Scene Type + Teilnehmer:

  ENCOUNTER (2 Agenten):
    Sequenzieller Dialog (ChatDev-Prinzip):
    A wird gespawnt -> Antwort
    B wird mit A's Antwort gespawnt -> Antwort
    Optional: A reagiert auf B -> Abschluss
    2-3 Runden, dann Game Master fasst zusammen

  WORK (1-2 Agenten):
    Single-Agent-Call:
    Input: Persona + relevante Memories + Task
    Output: Artefakt-Entwurf + Memories
    -> Artefakt in gallery/ speichern

  MEETING (3+ Agenten):
    Moderierter Round-Robin:
    GM stellt Frage/Thema
    Agent 1 antwortet
    Agent 2 antwortet (sieht Agent 1's Antwort)
    Agent 3 antwortet (sieht 1+2)
    Optional: 2. Runde fuer Reaktionen

  Nach jeder Szene:
  -> v2-Schema-Eintrag in logbook/
  -> Memories in state/memories/ appenden
  -> Agent-State aktualisieren
  -> [Interaktiv] CD-Input anbieten
         |
         v
SZENE 5+: NACHMITTAG/ABEND
  Gleicher Loop. Game Master priorisiert:
  - Unerledigte Threads von heute morgen
  - Artefakt-Reviews (Feedback auf WORK-Output)
  - Reflection wenn faellig (alle 2-3 Tage)
  - CD-Brief beantworten wenn noch offen
         |
         v
TAGES-ABSCHLUSS
  1. Game Master generiert Tages-Digest pro Agent
     (5-10 Zeilen: Was passiert, was gelernt,
      was morgen ansteht)
     -> state/digests/day-XXX/{agent}.md

  2. world.json aktualisieren
     (day++, scenes_total++, threads)

  3. Zusammenfassung fuer CD:
     "Heute: 6 Szenen. Highlights: ..."
     Artifacts: [Liste neuer Dateien in gallery/]
     Offene Threads: [Was morgen ansteht]
```

### Konkrete Verbesserungen vs. Sim 1

| Problem in Sim 1 | Loesung in Sim 2 | Quelle |
|---|---|---|
| Dialoge generisch (parallel spawned) | Sequenzielle Dyaden in ENCOUNTER | ChatDev |
| Agenten-Kontext vollgepackt mit 50 Memories | Tages-Digest als Bridge, Memories nur bei Bedarf | ChatDev Long-Term Memory |
| Reflection-Trigger inkonsistent | Fixe Reflection alle 2-3 Tage | Park et al. (vereinfacht) |
| Agenten halluzinieren statt nachzufragen | "Frage nach wenn unklar" in System-Prompts | ChatDev CDH |
| Zu viel manuelles State-Management | Game Master schreibt State inline nach jeder Szene | Concordia |
| Schema-Drift (v1 -> v2 Chaos) | v2 strikt enforced, kein Fallback | Lessons Learned |
| Tages-Uebergaenge verlieren Kontext | Digest-Files als explizite Tages-Bridge | ChatDev LTM |

### Manuelle Schritte die wegfallen

1. **Kein manuelles Memory-Management** mehr -- Game Master appendet Memories automatisch nach jeder Szene
2. **Kein separater Reflection-Trigger-Check** -- fixe Kadenz statt Accumulator-Tracking
3. **Kein manuelles Scene-Type-Picking** durch CD -- Game Master schlaegt Scene Menu vor, CD bestaetigt nur (oder ueberschreibt)
4. **Kein Post-hoc Logbook-Schreiben** -- Szenen-Log wird inline generiert, nicht nachtraeglich zusammengesetzt

---

## Zusammenfassung

Smallvilles Memory-Architektur (Reflection + Planning) mit ChatDevs Strukturierungs-Prinzipien (sequenzielle Dyaden, Conclusion-Bridges, Dehallucination) in GenSoftworks' bestehendem Scene-basierten Framework -- orchestriert durch den Game Master als narrativen Regisseur.
