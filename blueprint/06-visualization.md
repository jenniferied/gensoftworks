# 06 — Visualization

> The 2D view of GenSoftworks. Phaser.js + Tiled in the browser.

## Tech Choice

**Phaser.js + Tiled** — Browser-based, same stack as Stanford's Generative Agents (Apache 2.0). The visualization reads `state/` files and renders independently from the simulation. No tight coupling needed — the simulation (Claude Code) writes state, the viz reads it.

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

**Decision**: Purchased tileset (16x16, modern interior — e.g., LimeZu Modern Interiors or similar).

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

## State Connection

The viz reads from `state/` (file polling or WebSocket bridge):

```
state/world.json      → Clock display, day counter
state/agents/*.json   → Agent positions, current actions, status
logbook/day-XXX.jsonl → Speech/thought bubbles from recent scenes
```

Since scenes are discrete (not continuous ticks), the viz shows the **last known state** and animates transitions when state files update. Between scenes, agents are at their positions doing their declared tasks — a static but living tableau.

## Performance

Phaser.js handles 7 sprites on a tile map trivially. The bottleneck is scene processing speed (Claude thinking time), not rendering.
