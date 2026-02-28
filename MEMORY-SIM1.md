# GenSoftworks Memory

## Workflow Patterns
- **Pinwall favorites**: Always copy CD-approved concept art to `pinwall/favorites/`. When Jennifer says an image is successful/loved, copy it there immediately.
- **fal.ai pipeline**: Use master-thesis generate-images.py with scenes JSON. FAL_KEY in master-thesis/.env.local. Models: seedream-4-5 ($0.04), nano-banana-pro ($0.15), nano-banana-2 ($0.08), gpt-image-1-5 ($0.20).
- **Vera image gen**: In WORK scenes, Vera writes `3-image-prompts.json` (scenes format) in her trace dir. GM runs generate-images.py with that file. Output → `gallery/concepts/`. Budget: 5/day.
- **Language**: All in-sim content in German. Agents speak German.
- **Zotero**: DB at `~/Zotero/zotero.sqlite`, queryable via sqlite3. Add papers via Zotero's identifier field (arXiv ID is cleanest).
- **Prompting-Prinzipien**: Reference doc at `library/prompting-prinzipien.md` (Lost in the Middle, Halluzination, Bildgen-Tipps).

## RELICS Core Design Decisions (CD-confirmed Day 3)
- **Camera**: Skyrim FP/TP nahtlos umschaltbar, zoombar. Customizable Ruestung/Kleidung.
- **Combat**: Real-time action (Skyrim-Referenz). Schwerter, Boegen, Armbrueste, Schilde.
- **Futuristisch**: Biotech/Chemie, NICHT Steampunk. Echtes Gift, Drogen, Amphetamine. High Fashion Mittelalter.
- **Character Leveling**: Halbtransparente Nervensystem-Sicht (Cardio/Atmung, Muskel/Skelett, Lymph).
- **Tiermenschen**: Haendler und Diebe, NICHT Handwerker. Leicht alien vs. menschlich clean.
- **Mythologie**: Germanisch, Low Fantasy GoT-Level, 3-6 Fraktionen. Nah an der Quelle bleiben.
- **Monetarisierung**: Klassisch Premium. Alpha free fuer Streamer, Beta Steam 1 Jahr, DLCs + HIGH QUALITY Merch.
- **Vertical Slice**: Hauptquest + 2 Nebenquests in einer Region.
- **GDD**: Vollstaendiges Dokument, kein Skeleton.
- **Art Direction**: Mehr futuristisch, weniger heruntergekommen. Tiervolk weniger tribal.

## Simulation Architecture (Sim 2)
- **Simulation 1**: `simulation-1/` im Repo (abgeschlossen, read-only Referenz)
- **Active sim data**: `simulation-2/` (logbook/, gallery/, state/, pinwall/, briefing.md)
- **Memory system**: Per-agent memory files in `simulation-2/agents/{name}-memory.md`. GM updates after each scene. Memories cover BOTH work (decisions, artifacts, tasks) AND interpersonal (social dynamics, mood, bonding, small talk). ALL scene types get memories — including PAUSE.
- **6 scene types**: BRIEFING, WORK, MEETING, PAUSE, REVIEW, DND (Thursday exception)
- **DND location**: Bibliothek (CD-Entscheidung)
- **6 scenes per day** — see CLAUDE.md daily schedule
- **Logbook schema (v5)**: `logbook/dayDD.json` — one file per day, metadata + summaries only. No dialogue (lives in transcript.md).
- **Migration**: `scripts/migrate-to-day-index.py` converts old per-scene JSONs to v5 format.
- **Artifact naming**: `KK-titel-vN.md` (e.g. `01-spieluebersicht-v2.md`). Scripts pick highest `-vN` per chapter.
- **Traces**: Automatic via Claude Code JSONL recording. After sim: `python3 scripts/extract-transcripts.py --sim-dir simulation-2` copies raw JSONL + generates readable markdown. No agent self-tracing needed.
- **Weekly rhythm**: Mo/Di = Recherche+Konzeption, Mi-Fr = Produktion (V1→V2→V3)
- **WORK scenes**: All 7 agents work parallel. PAUSE: 2-3 random meet.
- **Conversation scenes**: Sequential turn-taking, NOT everyone speaks. Finn opens, 2-3 respond.
- **Agent model**: Sonnet 4.6 (`model: "sonnet"` in Task calls). GM stays Opus 4.6.
- **Schema detection in build-viewer-data.py**: v5=`dayDD.json`, v4=`dayDD-sceneS.json`, v2=`mood` dict, v1=`agent_details`
- **Scripts support `--sim-dir`** for targeting sim data (build-viewer-data.py, export-logbook.py, export-gdd.py, export-wbb.py)
- **GDD/WBB PDFs**: `export-gdd.py` and `export-wbb.py` scan gallery, pick highest `-vN`, concat + Pandoc → PDF
- **Screenshots**: `capture-scenes.mjs` uses Playwright. `npm run capture` in frontend/ doesn't pass `--out` correctly (kill %1 issue). Run `node scripts/capture-scenes.mjs --out <path>` directly instead. Screenshots auto-embed in logbook PDF.
- **Metrics**: Logbook `metrics` field tracks `total_tokens`, `duration_ms`, `tool_uses` per agent per scene. GM captures from Task result.
- **Genre**: Fantasy (NOT "dark fantasy") — CD-Korrektur
- **Images**: NEVER with text. All concept art text-free.

## Phaser.js Viewer
- **pixelArt: true is all-or-nothing** — sets CSS `image-rendering: pixelated` on canvas. Use HTML overlays for text that needs to stay sharp.
- **Character spritesheet direction order**: left, up, right, down (NOT down first). Verified via PIL pixel analysis.
- **CHAR_COLS = 56** (cols per combined row). CombRow 1 (frame 56+) = idle, CombRow 2 (112+) = walk.
- **Map layers** (bottom->top): floor, walls, misc4, furniture, misc, misc2, misc3, misc5. Note: Tiled may export duplicate layer names — Phaser `createLayer` only finds the first match, so duplicates must be renamed.
- Licensed assets (tilesets, furniture, characters) in frontend/.gitignore — not committed
- Sidebar/HUD are pure HTML, not Phaser overlays. sidebar.js handles scene nav + agent detail.
- **Bubble icons**: speech, thought, artifact — scene-type-based: conversation → speech, WORK → artifact (if artifacts) or thought.
