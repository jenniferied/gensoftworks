# 06 — Visualization

> The 2D view of GenSoftworks. Pygame + Tiled.

## Tech Choice

**Pygame + PyTMX + Tiled** — 100% Python, proven pattern (Stanford's Generative Agents used Phaser.js + Django; we stay in Python for tighter LLM integration).

**Upgrade path**: Phaser.js + FastAPI web frontend for shareable demos (Phase 7+).

## Map Design (Tiled)

The studio floorplan is designed in **Tiled** (free, visual tilemap editor) and exported as `.tmx`. This gives us:

- **Tile layer**: Floor, walls, furniture (visual)
- **Collision layer**: Where agents can/can't walk
- **Zone layer**: Named rectangles defining rooms and interaction areas
- **Object layer**: Spawn points, desks, meeting table, kitchen, bulletin board

### Studio Layout Zones

```
┌─────────────────────────────────────────────────────┐
│  ENTRANCE                                            │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐ │
│  │ LORE     │  │ ART      │  │ CONFERENCE ROOM   │ │
│  │ CORNER   │  │ STATION  │  │                   │ │
│  │ desk,    │  │ desk,    │  │ table, whiteboard │ │
│  │ bookshelf│  │ tablet,  │  │ projector         │ │
│  │          │  │ ref wall │  │                   │ │
│  │ [Kael]   │  │ [Vera]   │  │                   │ │
│  └──────────┘  └──────────┘  └───────────────────┘ │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │ KITCHEN  │  │ TECH     │  │ LIBRARY  │         │
│  │          │  │ CORNER   │  │          │         │
│  │ coffee,  │  │ monitors,│  │ shelves, │         │
│  │ fridge,  │  │ LED panel│  │ reading  │         │
│  │ table    │  │          │  │ nook     │         │
│  │          │  │ [Tobi]   │  │ [Mira]   │         │
│  └──────────┘  └──────────┘  └──────────┘         │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │ GAME     │  │ QA /     │  │ CREATIVE         │  │
│  │ DESIGN   │  │ STREAMING│  │ DIRECTOR         │  │
│  │ desk,    │  │ desk,    │  │ desk, monitor,   │  │
│  │ whiteboard│ │ 2nd mon, │  │ bulletin board   │  │
│  │          │  │ mic, cam │  │                  │  │
│  │ [Darius] │  │ [Leo]    │  │ [You]            │  │
│  └──────────┘  └──────────┘  └──────────────────┘  │
│                                                      │
│  ┌──────────────────────────────────────────────┐   │
│  │ LOUNGE / D&D TABLE                            │   │
│  │ couch, table, snacks, dice, minis, map        │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

## Tileset Art

**Option A**: Use free RPG Maker / LPC tilesets (16x16 or 32x32), modern office themed. Many free sets available on itch.io and OpenGameArt.

**Option B**: Generate custom tileset with Fal.ai (pixel art mode), ensuring consistent style.

**Option C**: Minimal geometric style (colored rectangles, clear but not pixel-art). Fastest to implement.

**Recommendation**: Start with Option C for prototyping, upgrade to A or B for polish.

## Agent Sprites

Each agent needs:
- 4-direction walk animation (up, down, left, right × 3–4 frames)
- Idle pose
- Working pose (sitting at desk)
- Talking indicator (speech bubble icon)
- Thinking indicator (thought bubble icon)

**Sprite size**: 32x32 or 48x48 pixels. Can be simple colored figures with distinct silhouettes (Kael: tall/thin, Vera: ponytail, Darius: broad, etc.)

## UI Overlay

```
┌─────────────────────────────────────────┐
│ Day 5 — Wednesday 14:30  [1x] [5x] [▶▶]│  ← Clock + speed controls
├─────────────────────────────────────────┤
│                                         │
│          [ STUDIO MAP VIEW ]            │
│                                         │
│     Agent sprites moving around         │
│     Speech bubbles on conversations     │
│     Thought bubbles on reflections      │
│     ★ icons on new artifacts            │
│                                         │
├─────────────────────────────────────────┤
│ KAEL: Writing Ashen Wastes geography    │  ← Agent status bar
│ VERA: Sketching bone-tower concepts     │
│ DARIUS: In meeting with Mira            │
│ MIRA: In meeting with Darius            │
│ TOBI: Testing lighting setup            │
│ LEO: Browsing r/crpg for feedback       │
├─────────────────────────────────────────┤
│ [Post Feedback] [Call Meeting] [View Log]│  ← CD controls
└─────────────────────────────────────────┘
```

## Speech & Thought Bubbles

- **Speech bubble**: White rounded rectangle with text, appears above agent during conversation (shows last line, fades after 3 seconds)
- **Thought bubble**: Cloud-shaped, appears during reflection (shows condensed insight)
- **Artifact bubble**: Star icon with thumbnail, appears when agent creates something

## Camera

- Default: full studio view (fits in window)
- Mouse scroll: zoom in/out
- Click agent: follow mode (camera tracks that agent)
- Click room: zoom to room

## Performance

The visualization runs on a separate thread from the simulation. The sim produces state snapshots per tick, the renderer interpolates between them for smooth animation.

At 6 agents with simple sprites, Pygame handles this trivially — no performance concerns.
