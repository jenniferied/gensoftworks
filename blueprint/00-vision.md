# 00 — Vision

## What This Is

GenSoftworks is a **multi-agent creative simulation** where AI characters work together in a virtual game studio to produce a dark fantasy CRPG's worldbuilding bible and game design document. Unlike task pipelines (ChatDev, MetaGPT, CrewAI), this system is inspired by **social simulation research** — agents develop organically over time through casual encounters, shared experiences, and accumulated memory.

The human user takes the role of **Creative Director** — observing, guiding, and occasionally intervening, but never micromanaging. The studio runs on simulated time. Ideas emerge from water-cooler conversations, not assigned tickets.

## Why This Exists

Most multi-agent AI systems treat agents as **stateless task executors**: receive prompt, produce output, reset. This misses what makes real creative teams work — shared context, evolving relationships, aesthetic disagreements that sharpen the work, inside jokes that become design motifs.

GenSoftworks asks: **What if AI agents had memory, personality, and time?**

## Academic Grounding

| Concept | Source | How We Use It |
|---------|--------|---------------|
| Memory Stream | Park et al. 2023 — "Generative Agents" | Per-agent chronological memory with recency/importance/relevance retrieval |
| Reflection | Park et al. 2023 | Agents synthesize higher-order insights when importance threshold is reached |
| Planning | Park et al. 2023 | Daily plans decomposed into hourly tasks, reactive re-planning on events |
| Emergent Culture | Altera 2024 — "Project Sid" | Studio develops shared aesthetics, in-jokes, creative principles over time |
| Experiential Learning | Qian et al. 2024 — ChatDev Co-Learning | Agents improve at their craft by accumulating successful patterns |
| Inception Prompting | Li et al. 2023 — CAMEL | Role-specific system prompts constraining agent behavior |

See `08-research-foundations.md` for full bibliography.

## The Studio

A small, state-funded game studio in Germany. Seven passionate developers building a dark fantasy CRPG. No publisher backing. Their livelihood depends on making this work. They use Unreal Engine 5, Houdini, and Blender.

They play D&D together every Thursday.

## The Output

The simulation produces **real artifacts** that flow into the master-thesis repository:

- **Worldbuilding Bible entries** — lore, factions, geography, naming systems
- **Game Design Document sections** — mechanics, quests, level concepts
- **Concept art** — generated via Fal.ai, curated by the Concept Artist agent
- **Design decisions** — documented reasoning for creative choices
- **A living logbook** — every observation, conversation, reflection, exportable as PDF/HTML

## Design Principles

1. **Organic over orchestrated** — Casual encounters produce ideas. Scheduled meetings refine them.
2. **Memory makes personality** — An agent's accumulated experience IS their character.
3. **Research-grounded, not research-bound** — Every system cites its source, but we adapt freely.
4. **Observable** — The human can watch the simulation unfold in real-time (2D visualization) or review logs afterward.
5. **Productive** — This isn't just a tech demo. The output feeds a real thesis project.
6. **Affordable** — Tiered model usage (Haiku for routine, Sonnet for reflection) keeps costs manageable.
