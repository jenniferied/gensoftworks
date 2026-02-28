# GenSoftworks

Seven role-based AI agents produce a GDD and WBB for a fantasy Computer-Rollenspiel (Park et al. 2023). Human user = Creative Director (CD).

## Models

- **Game Master (GM)**: Opus 4.6 — orchestrates scenes, writes logbook, updates memories
- **Agents**: Sonnet 4.6 — all seven role agents use `model: "sonnet"` in Task calls

## Daily Schedule (6 scenes)

| # | Time | Type | Who | What |
|---|------|------|-----|------|
| 1 | 09:00 | BRIEFING | all 7 | CD feedback + daily goals. Finn moderates. |
| 2 | 10:00 | WORK | alle 7 | Parallel: Mo/Di Recherche+Konzeption, Mi-Fr Produktion |
| 3 | 11:30 | MEETING | all 7 | Standup: results, questions, alignment |
| 4 | 12:30 | PAUSE | 2-3 | Social/spontaneous — no deliverables |
| 5 | 14:00 | WORK | alle 7 | Parallel: Mo/Di Recherche+Konzeption, Mi-Fr Produktion |
| 6 | 16:00 | REVIEW | all 7 | Present results, open questions for CD |

**Thursday**: Scene 6 = D&D (Emre is DM, + 2 players). Location: Bibliothek.

## Scene Execution

**WORK scenes**: Spawn all 7 agents parallel. Each writes own trace in `dayDD-sceneS-name/`.

**Conversation scenes (BRIEFING, MEETING, REVIEW, PAUSE, DND)**: Sequential subagent turns — each speaker is a separate Sonnet Task receiving all prior dialogue as context.
1. GM decides participants + turn order (who opens, who reacts)
2. Per turn: spawn agent (`model: "sonnet"`) with scene context + own memory + **all accumulated dialogue so far**
3. Agent writes own trace in `dayDD-sceneS-tT-name/` (T = turn number, name = agent)
4. GM collects output → appends to accumulated dialogue → spawns next agent
5. Repeat until conversation reaches natural end

- BRIEFING/MEETING/REVIEW: Finn opens, 3-5 agents react (not all 7 every turn)
- PAUSE: 2-3 agents, 5-8 turns total
- DND: 3 agents (Emre as DM + 2 players), 6-10 turns

## GM Checklist (per scene)

1. Read `world.json` → determine day + scene number
2. Read memory files for participating agents
3. Execute scene: parallel (WORK) or sequential turn loop (conversation)
4. After scene: append memory to **each participant**. Every scene type — including PAUSE. Cover both **work** and **interpersonal**.

**After scene 6 (end of day):**
5. Write `logbook/dayDD.json` per `schemas/day-index.json` (1 file per day, only metadata + summaries)
6. Update `world.json` (day +1, scene 0)
7. Run `python scripts/validate-sim.py --sim-dir simulation-2` — fix any errors before continuing.

## Traces (mandatory per agent)

`traces/dayDD-sceneS-name/` — numbered files: `0-prompt.md`, `1-reasoning.md`, `2-output.md`. No extra files.
- **WORK**: one dir per agent: `dayDD-sceneS-name/`
- **Conversation turns**: one dir per turn: `dayDD-sceneS-tT-name/` (e.g. `day06-scene4-t1-vera/`)
- **GM trace**: `dayDD-sceneS-type/` (e.g. `day06-scene4-pause/`)

Transcripts auto-recorded as JSONL. Extract: `python3 scripts/extract-transcripts.py --sim-dir simulation-2` (`--local` to regenerate).

## Logbook Format (v5)

One file per day: `logbook/dayDD.json`. Contains only metadata + summaries — no dialogue. Agent output lives in `transcript.md` (auto-extracted from JSONL recordings).

**Day summaries:** `weekday` always German proper-cased. Field name: `artifacts` (not `artifacts_produced`).

## Concept Art (Vera)

- Vera generates images via fal.ai in WORK scenes (Budget + Modelle: siehe `vera-conceptartist.md`)
- Other agents can request images → Vera writes prompt + generates
- All images: NEVER with text. Seedream: `negative_prompt` setzen. Nano/GPT: Text im Prompt gar nicht erwähnen (auch nicht negativ)
- Output: `gallery/concepts/{KK-kategorie}/{name}.png`
- CD-approved images → copy to `pinwall/favorites/` immediately

## Artifacts & Naming

**GDD** (`gallery/gdd/KK-titel-vN.md`): 01-spieluebersicht, 02-kernmechaniken, 03-erzaehlkonzept, 04-schluesselfiguren, 05-designsprache, 06-technik-produktion

**WBB** (`gallery/wbb/KK-titel-vN.md`): 01-mythos, 02-topos, 03-ethos

## Outputs

**After each day (mandatory):**
- `logbook/dayDD.json` — metadata + summaries per scene + day-level summary
- `python3 scripts/extract-transcripts.py --sim-dir simulation-2 --overwrite`

**On demand (CD requests):**
- Logbook PDF: `scripts/export-logbook.py --sim-dir simulation-2`
- Phaser viewer: `scripts/build-viewer-data.py --sim-dir simulation-2`
- GDD PDF: `scripts/export-gdd.py --sim-dir simulation-2`
- WBB PDF: `scripts/export-wbb.py --sim-dir simulation-2`

## Guardrails

- **German content, English code** — agents speak German in-sim
- **Echte Umlaute (ä ö ü ß)** — NIEMALS ae/oe/ue/ss. Agent-Prompts müssen enthalten: "Schreibe echte deutsche Umlaute (ä, ö, ü, ß), NICHT ae, oe, ue, ss."
- **Never invent citations** — if unsure, say so
- **Log everything** — every scene → logbook, every agent → traces
- **Briefing is the north star** — all artifacts align with `briefing.md`
- **Genre ist Fantasy** — NICHT "dark fantasy"
- **Images: NEVER with text** — all concept art text-free
- **Licensed assets** (tilesets, characters) in `frontend/.gitignore` — not committed
