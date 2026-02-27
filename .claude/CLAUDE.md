# GenSoftworks

Seven role-based AI agents produce a GDD and WBB for a dark fantasy CRPG (Park et al. 2023). Human user = Creative Director (CD).

## Daily Schedule (6 scenes)

| # | Time | Type | Who | What |
|---|------|------|-----|------|
| 1 | 09:00 | BRIEFING | all 7 | CD feedback + daily goals. Finn moderates. |
| 2 | 10:00 | WORK | alle 7 | Parallel: Mo/Di Recherche+Konzeption, Mi-Fr Produktion |
| 3 | 11:30 | MEETING | all 7 | Standup: results, questions, alignment |
| 4 | 12:30 | PAUSE | 2-3 | Social/spontaneous — no deliverables |
| 5 | 14:00 | WORK | alle 7 | Parallel: Mo/Di Recherche+Konzeption, Mi-Fr Produktion |
| 6 | 16:00 | REVIEW | all 7 | Present results, open questions for CD |

**Thursday**: Scene 6 = D&D (Emre is DM).

## GM Checklist (per scene)

1. Read `world.json` → determine day + scene number
2. Read memory files for participating agents
3. Spawn agents with: scene type, participants, context from memory
4. After scene: append summary to each participant's memory (from their perspective)
5. Write logbook entry → `simulation-2/logbook/dayDD-sceneS.json`
6. Update `world.json` (increment scene; after scene 6: increment day, reset scene to 0)

## Artifacts & Naming

**GDD** (`gallery/gdd/KK-titel.md`) — Schell (2010): 01-spieluebersicht (Darius), 02-kernmechaniken (Darius+Leo), 03-erzaehlkonzept (Nami+Darius), 04-schluesselfiguren (Nami), 05-designsprache (Vera), 06-technik-produktion (Tobi+Finn)

**WBB** (`gallery/wbb/KK-titel.md`) — Klastrup/Tosca (2004): 01-mythos (Emre), 02-topos (Emre), 03-ethos (Emre+Nami). Wolf (2013) checklist → `briefing.md`

## Memory & Logbook

**Memory**: `simulation-2/agents/{name}-memory.md` — GM appends after each scene from agent's perspective. Agents can also read `library/`, `gallery/`, other agents' artifacts.

**Traces**: `simulation-2/traces/dayDD-sceneS-name/` — each agent writes `prompt.md`, `reasoning.md`, `output.md` (all raw, 1:1, no summarization). Meetings: `dayDD-sceneS-type/`.

**Logbook**: `simulation-2/logbook/dayDD-sceneS.json` (e.g. `day01-scene3.json`)
```json
{"scene":1,"type":"BRIEFING|WORK|MEETING|PAUSE|REVIEW|DND",
 "time":"morning|afternoon","location":"kueche|lore-ecke|art-station|...",
 "participants":["vera","emre"],"summary":"...","dialogue":[{"who":"vera","says":"..."}],
 "artifacts":[],"cd_feedback":null}
```

## Guardrails

- **German content, English code** — agents speak German in-sim
- **Never invent citations** — if unsure, say so
- **Log everything** — every scene → logbook
- **Briefing is the north star** — all artifacts align with `briefing.md`
