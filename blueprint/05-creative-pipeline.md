# 05 — Creative Pipeline

> How agent work becomes real artifacts.

## The Problem

Generative Agents (Smallville) agents "do things" in text form only: "Isabella is cooking breakfast." Nothing actually gets cooked. For GenSoftworks, agents must produce **real creative artifacts** — Markdown text, generated images, design documents — that are useful outside the simulation.

## Artifact Types

| Agent | Artifact | Format | Mechanism |
|-------|----------|--------|-----------|
| Emre (Worldbuilder) | Lore entries, geography, naming tables | Markdown | Subagent writes to gallery/ |
| Vera (Concept Artist) | Concept sketches, mood boards, style refs | PNG via Fal.ai | Subagent generates prompt, Fal.ai MCP or manual |
| Darius (Game Director) | Mechanics specs, quest outlines, balance docs | Markdown | Subagent writes to gallery/ |
| Nami (Narrative Designer) | Dialogue drafts, quest narratives, character bios | Markdown | Subagent writes to gallery/ |
| Tobi (Tech Artist) | Lighting notes, pipeline specs, shader concepts | Markdown + diagrams | Subagent writes to gallery/ |
| Leo (QA/Community) | Playtest notes, player perspective docs, feature reviews | Markdown | Subagent writes to gallery/ |

## Production Flow

Artifacts are produced in **WORK scenes** (see `03-simulation-loop.md`):

```
1. Game Master selects a WORK scene for an agent with a creative task
2. Agent subagent is spawned with: persona, memories, task context, CD feedback
3. Subagent generates the artifact (writes Markdown to gallery/)
4. Artifact metadata enters agent's memory stream
5. Game Master adds observation memories to other agents present
6. If artifact is noteworthy → Game Master may schedule an ENCOUNTER scene
   where another agent reacts
```

## Creative Context (Subagent Prompt)

The WORK scene provides the agent subagent with:

```
You are {agent_name}, {role} at GenSoftworks.
{persona_summary}

Your relevant creative memories:
{recent_memories_about_task}

Recent team decisions:
{bulletin_board}

Creative Director's latest feedback:
{cd_feedback_if_any}

TASK: {specific_creative_task}
Write the artifact in German. Be specific, vivid, and consistent with
established lore/design decisions. Save it to gallery/{type}/.
```

The subagent has Write access to `gallery/` and produces the artifact directly as a file.

## Image Generation (Concept Artist)

Vera's WORK scenes produce image prompts, not images directly:

1. Vera subagent formulates a concept based on task + memories
2. Subagent writes a detailed Fal.ai prompt (in English) + concept brief (in German)
3. The Creative Director (or a hook) runs the prompt through Fal.ai
4. Results are saved to `gallery/concepts/` and added to Vera's memories

This keeps image generation in human hands (curation) while the creative thinking is Vera's.

## Library Integration

The `library/` folder contains reference materials (PDFs, artbooks, GDDs, WBBs). Agents can "consult the library" as a planned action:

1. Agent decides to research something
2. Relevant documents are retrieved (by filename/metadata match)
3. Key passages are summarized and added to agent memory
4. The research informs subsequent creative output

This models real creative professionals consulting references, artbooks, and competitor analysis.

## Quality Control

### Self-Critique
After creating an artifact, the agent evaluates it against:
- Established style decisions (from memory)
- Creative Director feedback (from memory)
- Internal quality standards (from persona)

### Peer Review (organic)
When another agent sees the artifact (proximity observation), they may spontaneously comment. If their memory contains relevant context, the comment is informed:
```
Kael sees Vera's bone-tower concept: "The proportions feel right,
but the base should show more erosion — the Ashen Wastes have
centuries of wind damage."
```

### Creative Director Review
The human can flag any artifact for revision, praise, or rejection. This enters all agents' memory streams as high-importance feedback.

## Output Organization

```
gallery/
├── concepts/                   # Vera's images
│   ├── day03_bone_towers_v1.png
│   ├── day03_bone_towers_v2.png
│   └── day05_darkelf_armor.png
├── lore/                       # Kael's worldbuilding
│   ├── day02_ashen_wastes_geography.md
│   └── day07_darkelf_society.md
├── designs/                    # Darius' game design
│   ├── day04_dungeon_ashen_wastes.md
│   └── day06_combat_system_notes.md
└── narratives/                 # Mira's writing
    ├── day05_darkelf_elder_dialogue.md
    └── day08_quest_bone_harvest.md
```

Each file includes YAML frontmatter:
```yaml
---
agent: vera
day: 3
task: "Concept art for Ashen Wastes bone-towers"
memories_referenced: [mem_042, mem_067, mem_089]
feedback_received: []
status: draft
---
```
