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

**Thursday**: Scene 6 = D&D (Emre is DM). Location: Bibliothek.

## GM Checklist (per scene)

1. Read `world.json` → determine day + scene number
2. Read memory files for participating agents
3. Read `schemas/scene.json` — every logbook entry MUST match this structure exactly
4. Spawn agents with `model: "sonnet"`, scene type, participants, context from memory
5. Write traces → `traces/dayDD-sceneS-name/` with exactly `0-prompt.md`, `1-reasoning.md`, `2-output.md` (no extra files)
6. After scene: append memory to **each participant**. Every scene type — including PAUSE. Cover both **work** and **interpersonal**.
7. Write logbook → `logbook/dayDD-sceneS.json` — dialogue **1:1 from trace `2-output.md`**, NICHT kürzen. Siehe Schema Rules.
8. Update `world.json`
9. **After scene 6**: Write `logbook/dayDD-summary.json` per `schemas/day-summary.json`
10. **After scene 6**: Run `python scripts/validate-sim.py --sim-dir simulation-2` — fix any errors before continuing.
11. **Log metrics**: capture `total_tokens` + `duration_ms` per agent → logbook `metrics` field.

## Traces (mandatory per agent)

`traces/dayDD-sceneS-name/` — numbered files: `0-prompt.md`, `1-reasoning.md`, `2-output.md`. Meetings: `dayDD-sceneS-type/`. All raw, 1:1, no summarization.

## Schema Rules (mandatory)

Every logbook file MUST match `schemas/scene.json`. No extra fields, no missing fields.

**Fixed locations:** WORK → `"alle-stationen"`, BRIEFING/MEETING/REVIEW/PAUSE → `"küche"`, DND → `"bibliothek"`

**Dialogue — conversation scenes (BRIEFING, MEETING, REVIEW, PAUSE, DND):**
- Copy full dialogue from trace `2-output.md` → `dialogue` array. `**Name**: text` → `{"who": "name", "says": "text"}`.
- Do NOT shorten, summarize, or edit. 1:1 from trace.
- `summary` is the only place for GM condensation.

**Dialogue — WORK scenes:** `dialogue: []`. Output lives in traces.

**Traces — exactly 3 files per dir:** `0-prompt.md`, `1-reasoning.md`, `2-output.md`. No extra files. Prompt header: `# {Name} — Tag {DD}, Szene {S} ({TYPE}) — Prompt`

**Artifacts (GDD/WBB):** Every `.md` in `gallery/gdd/` and `gallery/wbb/` MUST have YAML frontmatter per `schemas/artifact-header.md`. `version` integer must match filename `-vN`.

**`trace_dirs`:** Conversation → `["dayDD-sceneS-type"]`. WORK → `["dayDD-sceneS-agent1", ...]`.

**Day summaries:** `weekday` always German proper-cased. Field name: `artifacts` (not `artifacts_produced`).

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
- **Echte Umlaute (ä ö ü ß)** — NIEMALS ae/oe/ue/ss. Agent-Prompts müssen enthalten: "Schreibe echte deutsche Umlaute (ä, ö, ü, ß), NICHT ae, oe, ue, ss."
- **Never invent citations** — if unsure, say so
- **Log everything** — every scene → logbook, every agent → traces
- **Briefing is the north star** — all artifacts align with `briefing.md`
- **Images: NEVER with text** — all concept art text-free
