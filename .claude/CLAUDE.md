# GenSoftworks

Seven role-based AI agents produce a GDD and WBB for a fantasy CRPG (Park et al. 2023). Human user = Creative Director (CD).

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

**Thursday**: Scene 6 = D&D (Emre is DM).

## GM Checklist (per scene)

1. Read `world.json` → determine day + scene number
2. Read memory files for participating agents
3. Spawn agents with `model: "sonnet"`, scene type, participants, context from memory
4. After scene: append memory to **each participant** (from their perspective). Every scene type gets a memory — including PAUSE. Cover both **work** (decisions, artifacts, tasks) and **interpersonal** (who said what, mood, small talk, social dynamics, conflicts, bonding)
5. Write logbook entry → `logbook/dayDD-sceneS.json`
6. Update `world.json` (increment scene; after scene 6: increment day, reset scene to 0)
7. **After scene 6**: Write `logbook/dayDD-summary.json` (day overview for PDF/Phaser)
8. **Log metrics**: After each agent spawn, capture `total_tokens` + `duration_ms` from Task result. Write to logbook `metrics` field.

## Traces (mandatory per agent)

`traces/dayDD-sceneS-name/` — numbered files: `0-prompt.md`, `1-reasoning.md`, `2-output.md`. Meetings: `dayDD-sceneS-type/`. All raw, 1:1, no summarization.

## Conversation Scenes (BRIEFING, MEETING, REVIEW, PAUSE, DND)

Sequential turn-taking. NOT everyone speaks — Finn opens, 2-3 agents respond. Each agent spawned separately.

## Concept Art (Vera)

- Vera generates images via fal.ai in WORK scenes
- Daily budget: 5 images (Seedream $0.04 explore, Nano $0.15 refine)
- Other agents can request images → Vera writes prompt + generates
- All images: NEVER with text (negative_prompt enforced)
- Output: `gallery/concepts/{KK-kategorie}/{name}.png`
- Approved images → `pinwall/favorites/`

## Artifacts & Naming

**GDD** (`gallery/gdd/KK-titel-vN.md`): 01-spieluebersicht, 02-kernmechaniken, 03-erzaehlkonzept, 04-schluesselfiguren, 05-designsprache, 06-technik-produktion

**WBB** (`gallery/wbb/KK-titel-vN.md`): 01-mythos, 02-topos, 03-ethos

## Outputs (after each day)

- **Day summary**: `logbook/dayDD-summary.json` — phase, title, summary, cd_decisions, artifacts, key_moments
- **Logbook PDF**: `Meier_KIComputerRollenspiele_Sim2Test_Logbuch_2026.pdf` (via `scripts/export-logbook.py`)
- **Phaser viewer**: `scripts/build-viewer-data.py --sim-dir simulation-2-test` → `viewer-data/simulation.json`
- **GDD PDF**: `scripts/export-gdd.py --sim-dir simulation-2-test`
- **WBB PDF**: `scripts/export-wbb.py --sim-dir simulation-2-test`

## Guardrails

- **German content, English code** — agents speak German in-sim
- **Never invent citations** — if unsure, say so
- **Log everything** — every scene → logbook, every agent → traces
- **Briefing is the north star** — all artifacts align with `briefing.md`
- **Images: NEVER with text** — all concept art text-free
