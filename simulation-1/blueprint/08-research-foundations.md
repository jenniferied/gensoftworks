# 08 — Research Foundations

> Every design decision in GenSoftworks is grounded in published research. This document maps our systems to their academic sources.

## Core Papers

### 1. Generative Agents: Interactive Simulacra of Human Behavior
- **Authors**: Park, J.S., O'Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S.
- **Venue**: UIST 2023 / arXiv:2304.03442
- **What they did**: 25 AI agents in a virtual town ("Smallville") with persistent memory streams, reflection, and daily planning. Agents formed relationships, spread information, coordinated a Valentine's Day party — all emergent from a single seed.
- **What we borrow**:
  - Memory stream architecture (observation → retrieval → reflection → planning)
  - Retrieval scoring: `0.5 * recency + 3.0 * relevance + 2.0 * importance`
  - Reflection trigger via importance accumulation threshold (150)
  - Exponential decay for recency (0.995/hour)
  - Subject-predicate-object triplets for structured memory
- **What we change**:
  - Setting: game studio instead of village
  - Purpose: creative production, not social simulation
  - Agents produce artifacts (text, images) that enter the memory stream
  - Human (Creative Director) actively participates

### 2. Project Sid: Many-Agent Simulations Toward AI Civilization
- **Authors**: Altera Research
- **Venue**: arXiv:2411.00114 (November 2024)
- **What they did**: 1,000 agents in Minecraft with no predefined tasks. Emergent economy (gem currency), governance (constitutional voting), religion (Pastafarianism spread via bribery), parallel civilizations.
- **What we borrow**:
  - Concept of emergent culture from agent interaction
  - Agents developing shared norms without programming
  - The idea that agents can form a "studio culture" organically
- **What we change**:
  - Scale: 6 agents, not 1,000
  - Environment: 2D studio, not Minecraft
  - Focus: creative output quality, not civilizational emergence

### 3. ChatDev: Communicative Agents for Software Development
- **Authors**: Qian, C., et al.
- **Venue**: ACL 2024 / arXiv:2307.07924
- **What they did**: Virtual software company with CEO, CTO, Programmer, etc. "Chat chain" pipeline: requirements → design → coding → review → testing.
- **What we borrow**:
  - Role specialization with distinct system prompts
  - The concept of instructor/assistant dyads for structured phases
  - Experiential co-learning across tasks (from the follow-up paper)
- **What we explicitly reject**:
  - Rigid sequential pipeline (we use organic interaction instead)
  - Stateless agents (our agents have persistent memory)
  - No human in the loop (we have the Creative Director)
  - 1-turn code generation (our creative work is iterative)

### 4. CAMEL: Communicative Agents for "Mind" Exploration
- **Authors**: Li, G., et al.
- **Venue**: NeurIPS 2023 / arXiv:2303.17760
- **What they did**: Inception prompting for role-playing between AI agent pairs.
- **What we borrow**:
  - Inception prompting technique: both agents receive symmetric system prompts
  - Role-constrained conversation (agents stay in character)

### 5. Affordable Generative Agents
- **Venue**: arXiv:2402.02053
- **What they did**: Optimized the Generative Agents architecture for cost. Reduced token usage to 31–43% of the original.
- **What we borrow**:
  - Token usage benchmarks (baseline: ~1M tokens/agent/day)
  - Optimization strategies: tiered model usage, prompt caching
  - Cost estimation methodology

### 6. Concordia (Google DeepMind)
- **Repository**: github.com/google-deepmind/concordia
- **What it is**: Pure Python agent simulation library using a "Game Master" pattern from tabletop RPGs.
- **What we borrow** (heavily — this is our closest architectural ancestor):
  - **Game Master as narrator/arbiter** — our main Claude Code session IS the Game Master
  - **Scene-based progression** — not clock ticks, but narrative beats selected by the Game Master
  - **Text-only simulation with separate visualization** — Claude writes state, Phaser.js renders it
  - Entity-component architecture for agent state (our `state/agents/*.json`)

## Research Mapping

| GenSoftworks System | Academic Source | Paper Section / Code Reference |
|---------------------|----------------|-------------------------------|
| Memory stream | Park et al. 2023 | `associative_memory.py` |
| Retrieval scoring | Park et al. 2023 | `retrieve.py` — weights 0.5/3.0/2.0 |
| Importance scoring (1–10) | Park et al. 2023 | `poignancy_event_v1.txt` |
| Reflection trigger | Park et al. 2023 | `scratch.py` — threshold 150 |
| Reflection synthesis | Park et al. 2023 | `insight_and_evidence_v1.txt` |
| Daily planning | Park et al. 2023 | `daily_planning_v6.txt` |
| Reactive re-planning | Park et al. 2023 | `plan.py` — `_should_react()` |
| Emergent culture | Altera 2024 | Project Sid — civilization emergence |
| Role prompting | Li et al. 2023 | CAMEL — inception prompting |
| Cost optimization | AGA 2024 | Tiered model usage |
| Experiential learning | Qian et al. 2024 | ChatDev Co-Learning |
| Scene-based progression | DeepMind 2024 | Concordia — Game Master selects narrative beats |
| Game Master pattern | DeepMind 2024 | Concordia — `game_master.py` |
| Text-only sim + separate viz | DeepMind 2024 | Concordia — decoupled rendering |

## Further Reading

- **A-Mem** (NeurIPS 2025): Zettelkasten-inspired agent memory with networked knowledge graphs. Could replace linear memory stream in future versions.
- **AgentSociety** (Tsinghua 2025): Large-scale (30K agents) social simulation. Infrastructure patterns for scaling.
- **Voyager** (2023): Single-agent lifelong learning in Minecraft. Skill library accumulation pattern.
- **Mem0**: Production memory layer for AI agents. Vector + summarization + graph storage.
- **Letta** (formerly MemGPT): LLM context as operating system memory. Context window management.

## Key Metrics from Literature

| Metric | Value | Source |
|--------|-------|--------|
| Tokens per agent per simulated day (baseline) | ~1.0M | AGA 2024 |
| Tokens per agent per simulated day (optimized) | ~0.4M | AGA 2024 |
| Recency decay rate | 0.995/hour | Park et al. 2023 |
| Reflection threshold | 150 importance points | Park et al. 2023 |
| Average reflections per agent per day | 1–2 | Park et al. 2023 |
| Conversations per agent per day | 2–5 | Park et al. 2023 |
| Memory nodes per agent per day | ~30 | Park et al. 2023 |
