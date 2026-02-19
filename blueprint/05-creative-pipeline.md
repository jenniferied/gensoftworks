# 05 — Creative Pipeline

> How agent work becomes real artifacts.

## The Problem

Generative Agents (Smallville) agents "do things" in text form only: "Isabella is cooking breakfast." Nothing actually gets cooked. For GenSoftworks, agents must produce **real creative artifacts** — Markdown text, generated images, design documents — that are useful outside the simulation.

## Artifact Types

| Agent | Artifact | Format | Tool |
|-------|----------|--------|------|
| Kael (Worldbuilder) | Lore entries, geography, naming tables | Markdown | Claude API |
| Vera (Concept Artist) | Concept sketches, mood boards, style refs | PNG via Fal.ai | Fal.ai API |
| Darius (Game Director) | Mechanics specs, quest outlines, balance docs | Markdown | Claude API |
| Mira (Narrative Designer) | Dialogue drafts, quest narratives, character bios | Markdown | Claude API |
| Tobi (Tech Artist) | Lighting notes, pipeline specs, shader concepts | Markdown + diagrams | Claude API |
| Leo (QA/Community) | Playtest notes, player perspective docs, feature reviews | Markdown | Claude API |

## Production Flow

```
1. Agent decides to create (from daily plan or inspiration)
2. Agent retrieves relevant memories (past work, feedback, style decisions)
3. Agent generates artifact via LLM call with full creative context
4. Artifact is saved to gallery/{type}/
5. Artifact metadata enters agent's memory stream
6. Nearby agents observe the creation event
7. If artifact triggers feedback from another agent → conversation
```

## Creative Context Prompt (for text artifacts)

```
You are {agent_name}, {role} at GenSoftworks.
{persona_summary}

Your relevant creative memories:
{top_15_retrieved_memories}

Recent team decisions:
{shared_bulletin_board_items}

Creative Director's latest feedback:
{most_recent_cd_feedback}

Reference material you've reviewed:
{recent_library_references}

TASK: {specific_creative_task}
Write in German. Be specific, vivid, and consistent with
established lore/design decisions.
```

## Image Generation (Concept Artist)

Vera's creative process:
1. She formulates a concept based on her current task + memories
2. The LLM generates a detailed Fal.ai prompt (in English, for model quality)
3. Fal.ai generates 2–4 variations
4. The LLM (as Vera) selects the best and explains why
5. Selected image saved, rejected ones logged as "sketches"

```python
# Simplified
concept_brief = vera.generate_concept_brief(task, memories)
fal_prompt = vera.translate_to_image_prompt(concept_brief)
images = fal_ai.generate(fal_prompt, num_images=3)
selection = vera.evaluate_and_select(images, concept_brief)
save_artifact(selection, "gallery/concepts/")
```

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
