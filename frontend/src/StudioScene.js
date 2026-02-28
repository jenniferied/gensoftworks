import Phaser from 'phaser';

const T = 48;
const MAP_W = 44;
const MAP_H = 28;
const CHAR_COLS = 56; // columns per combined row in 48×96 character sheets

// --- Room interiors (walkable bounds, inside walls) ---
const ROOMS = {
  '12a':       { x1: 1,  y1: 1,  x2: 7,  y2: 6  },
  '12b':       { x1: 9,  y1: 1,  x2: 15, y2: 6  },
  '12c':       { x1: 17, y1: 1,  x2: 23, y2: 6  },
  'conference': { x1: 25, y1: 1,  x2: 33, y2: 6  },
  'kitchen':   { x1: 35, y1: 1,  x2: 42, y2: 6  },
  'hallway':   { x1: 1,  y1: 9,  x2: 42, y2: 12 },
  '12d':       { x1: 1,  y1: 14, x2: 7,  y2: 18 },
  '12e':       { x1: 9,  y1: 14, x2: 15, y2: 18 },
  '12f':       { x1: 17, y1: 14, x2: 23, y2: 18 },
  'lounge':    { x1: 25, y1: 14, x2: 33, y2: 27 },
  'wc_damen':  { x1: 35, y1: 14, x2: 38, y2: 18 },
  'wc_herren': { x1: 40, y1: 14, x2: 42, y2: 18 },
  '12':        { x1: 1,  y1: 20, x2: 23, y2: 27 },
};


// --- Agent definitions ---
const AGENTS = [
  { key: 'emre',   name: 'Emre Kaya',       role: 'Worldbuilder',       room: '12a', sprite: 'char_05', deskX: 4,  deskY: 3,  facing: 'right', gender: '\u2642', flag: '\uD83C\uDDF9\uD83C\uDDF7\uD83C\uDDE9\uD83C\uDDEA' },
  { key: 'vera',   name: 'Vera Morozova',    role: 'Concept Artist',     room: '12b', sprite: 'char_01', deskX: 12, deskY: 3,  facing: 'left',  gender: '\u2640', flag: '\uD83C\uDDF5\uD83C\uDDF1\uD83C\uDDE9\uD83C\uDDEA' },
  { key: 'tobi',   name: 'Tobias Richter',   role: 'Tech Lead',          room: '12c', sprite: 'char_03', deskX: 20, deskY: 3,  facing: 'right', gender: '\u2642', flag: '\uD83C\uDDE9\uD83C\uDDEA' },
  { key: 'darius', name: 'Darius Varga',     role: 'Game Director',      room: '12d', sprite: 'char_04', deskX: 4,  deskY: 16, facing: 'right', gender: '\u2642', flag: '\uD83C\uDDE9\uD83C\uDDEA' },
  { key: 'nami',   name: 'Nami Osei',        role: 'Narrative Designer', room: '12e', sprite: 'char_02', deskX: 12, deskY: 16, facing: 'left',  gender: '\u2640', flag: '\uD83C\uDDF3\uD83C\uDDEC\uD83C\uDDE9\uD83C\uDDEA' },
  { key: 'leo',    name: 'Leo Ferretti',     role: 'Community Manager',  room: '12f', sprite: 'char_06', deskX: 20, deskY: 16, facing: 'right', gender: '\u2640', flag: '\uD83C\uDDE9\uD83C\uDDEA\uD83C\uDDEE\uD83C\uDDF7' },
  { key: 'finn',   name: 'Finn Calloway',    role: 'Producer',           room: '12',  sprite: 'char_07', deskX: 8,  deskY: 23, facing: 'right', gender: '\u2642', flag: '\uD83C\uDDE9\uD83C\uDDEA' },
];

const ZONES = [
  { name: '12a Lore-Ecke\nEmre',           x: 0,  y: 0,  w: 8,  h: 8  },
  { name: '12b Art Station\nVera',         x: 8,  y: 0,  w: 8,  h: 8  },
  { name: '12c Tech Corner\nTobi',         x: 16, y: 0,  w: 8,  h: 8  },
  { name: 'Konferenz',                    x: 24, y: 0,  w: 10, h: 8  },
  { name: 'Küche',                        x: 34, y: 0,  w: 10, h: 8  },
  { name: '12d Game Design Corner\nDarius', x: 0,  y: 13, w: 8,  h: 7  },
  { name: '12e Schreibstube\nNami',        x: 8,  y: 13, w: 8,  h: 7  },
  { name: '12f QA / Streaming\nLeo',       x: 16, y: 13, w: 8,  h: 7  },
  { name: 'Lounge',              x: 24, y: 13, w: 10, h: 15 },
  { name: 'Bibliothek',          x: 34, y: 20, w: 10, h: 8  },
  { name: 'WC Damen',            x: 34, y: 13, w: 5,  h: 7  },
  { name: 'WC Herren',           x: 39, y: 13, w: 5,  h: 7  },
  { name: 'Flur',                x: 0,  y: 8,  w: 44, h: 5  },
  { name: '12 Produktionsbüro\nFinn + CD',  x: 0,  y: 20, w: 24, h: 8  },
];

// Character animation frame map (48×96 frames, 56 cols per combined row)
const CHAR_ANIMS = {
  // Walk animations (first row: frames 0–23)
  walk_down:  { start: 0,  count: 6 },
  walk_left:  { start: 6,  count: 6 },
  walk_right: { start: 12, count: 6 },
  walk_up:    { start: 18, count: 6 },
  // Idle animations (second row: frames 56+)
  idle_left:  { start: CHAR_COLS + 0,   count: 6 },
  idle_up:    { start: CHAR_COLS + 6,   count: 6 },
  idle_right: { start: CHAR_COLS + 12,  count: 6 },
  idle_down:  { start: CHAR_COLS + 18,  count: 6 },
};

// Room highlight color
const HIGHLIGHT_COLOR = 0x4488cc;
const HIGHLIGHT_ALPHA = 0.07;
const HIGHLIGHT_BORDER_ALPHA = 0.25;


export class StudioScene extends Phaser.Scene {
  constructor() {
    super({ key: 'StudioScene' });
  }

  preload() {
    this.load.image('floors', 'assets/tilesets/Room_Builder_Floors_48x48.png');
    this.load.image('walls', 'assets/tilesets/Room_Builder_Walls_48x48.png');
    this.load.tilemapTiledJSON('map', 'assets/map.json');

    // Furniture images — loaded as tilemap tilesets (placed in Tiled)
    this.load.image('furn_generic',    'assets/furniture/1_Generic_48x48.png');
    this.load.image('furn_livingroom', 'assets/furniture/2_LivingRoom_48x48.png');
    this.load.image('furn_bathroom',   'assets/furniture/3_Bathroom_48x48.png');
    this.load.image('furn_library',    'assets/furniture/5_Classroom_and_library_48x48.png');
    this.load.image('furn_art',        'assets/furniture/7_Art_48x48.png');
    this.load.image('furn_kitchen',    'assets/furniture/12_Kitchen_48x48.png');
    this.load.image('furn_conference', 'assets/furniture/13_Conference_Hall_48x48.png');
    this.load.image('furn_office',     'assets/furniture/Modern_Office_48x48.png');

    // Characters: 48×96 frames (two tiles tall)
    for (const agent of AGENTS) {
      this.load.spritesheet(agent.sprite, `assets/characters/${agent.sprite}.png`, {
        frameWidth: T, frameHeight: T * 2,
      });
    }

    // Bubble icons (shown above agents in v2 scenes)
    this.load.image('bubble_speech',     'assets/icons/bubble-speech.png');
    this.load.image('bubble_thought',    'assets/icons/bubble-thought.png');
    this.load.image('bubble_artifact',   'assets/icons/bubble-artifact.png');
    this.load.image('bubble_reflection', 'assets/icons/bubble-reflection.png');
    this.load.image('bubble_plan',       'assets/icons/bubble-plan.png');
  }

  create() {
    // --- Tilemap ---
    const map = this.make.tilemap({ key: 'map' });
    const floorTiles = map.addTilesetImage('floors', 'floors');
    const wallTiles = map.addTilesetImage('walls', 'walls');

    // Furniture tilesets
    const furnGeneric    = map.addTilesetImage('furn_generic',    'furn_generic');
    const furnLivingroom = map.addTilesetImage('furn_livingroom', 'furn_livingroom');
    const furnBathroom   = map.addTilesetImage('furn_bathroom',   'furn_bathroom');
    const furnLibrary    = map.addTilesetImage('furn_library',    'furn_library');
    const furnArt        = map.addTilesetImage('furn_art',        'furn_art');
    const furnKitchen    = map.addTilesetImage('furn_kitchen',    'furn_kitchen');
    const furnConference = map.addTilesetImage('furn_conference', 'furn_conference');
    const furnOffice     = map.addTilesetImage('furn_office',     'furn_office');
    const allFurn = [furnGeneric, furnLivingroom, furnBathroom, furnLibrary, furnArt, furnKitchen, furnConference, furnOffice].filter(Boolean);

    const allTilesets = [floorTiles, wallTiles, ...allFurn].filter(Boolean);

    map.createLayer('floor', allTilesets).setDepth(-10);
    map.createLayer('walls', allTilesets).setDepth(-5);

    // Furniture & decoration layers (painted in Tiled, stacked bottom→top)
    for (const [name, depth] of [['misc4', -3], ['furniture', -2], ['misc', -1], ['misc2', 0], ['misc3', 1], ['misc5', 2]]) {
      const layer = map.createLayer(name, allTilesets);
      if (layer) layer.setDepth(depth);
    }

    // --- Room highlight (between floor and furniture) ---
    this.roomHighlight = this.add.graphics();
    this.roomHighlight.setDepth(-8);

    // --- Zone labels (HTML overlay — always sharp, behind characters) ---
    const overlay = document.getElementById('zone-overlay');
    this.zoneLabels = ZONES.map(zone => {
      const el = document.createElement('div');
      el.className = 'zone-label';
      el.textContent = zone.name;
      overlay.appendChild(el);
      return { el, wx: (zone.x + zone.w / 2) * T, wy: (zone.y + zone.h / 2) * T };
    });

    // --- Agent tooltip (HTML, stays sharp over pixelArt canvas) ---
    this.tooltip = document.getElementById('agent-tooltip');
    this.tooltipGender = this.tooltip.querySelector('.tt-gender');
    this.tooltipLabel = this.tooltip.querySelector('.tt-label');
    this.tooltipFlag = this.tooltip.querySelector('.tt-flag');
    this.tooltipRole = this.tooltip.querySelector('.tt-role');

    // --- Agents ---
    this.agentSprites = {};
    for (const agent of AGENTS) {
      this.createAgentAnims(agent.sprite);
      const px = agent.deskX * T + T / 2;
      const py = agent.deskY * T + T / 2;
      const sprite = this.add.sprite(px, py, agent.sprite, 0)
        .setOrigin(0.5, 0.8)
        .setDepth(py)
        .setInteractive({ useHandCursor: true });
      sprite.play(`${agent.sprite}_idle_down`);

      // Hover → show tooltip
      sprite.on('pointerover', () => {
        this.tooltipGender.textContent = agent.gender;
        this.tooltipLabel.textContent = agent.name;
        this.tooltipFlag.textContent = agent.flag;
        this.tooltipRole.textContent = agent.role;
        this.tooltip.classList.add('visible');
      });
      sprite.on('pointerout', () => {
        this.tooltip.classList.remove('visible');
      });

      // Click → dispatch agent-click event (opens profile modal)
      sprite.on('pointerdown', (pointer) => {
        pointer.event.stopPropagation();
        this.tooltip.classList.remove('visible');
        window.dispatchEvent(new CustomEvent('viewer:agent-click', {
          detail: { agentKey: agent.key },
        }));
      });

      this.agentSprites[agent.key] = { sprite, agent, bubble: null };
    }

    // --- Camera ---
    const cam = this.cameras.main;
    cam.setBounds(0, 0, MAP_W * T, MAP_H * T);
    const zoomX = this.scale.width / (MAP_W * T);
    const zoomY = this.scale.height / (MAP_H * T);
    this.fitZoom = Math.min(zoomX, zoomY);
    cam.setZoom(this.fitZoom);
    cam.centerOn((MAP_W * T) / 2, (MAP_H * T) / 2);


    // --- Listen for scene changes from sidebar ---
    window.addEventListener('viewer:scene-change', (e) => {
      this.loadScene(e.detail.dayIndex, e.detail.sceneIndex);
    });

    // If data is already loaded, apply first scene
    if (window.__simData) {
      this.loadScene(0, 0);
    } else {
      window.addEventListener('viewer:data-ready', () => {
        this.loadScene(0, 0);
      }, { once: true });
    }
  }

  /** Move agents to scene positions with walk animations, dim non-participants. */
  loadScene(dayIndex, sceneIndex) {
    const data = window.__simData;
    if (!data) return;
    const scene = data.days[dayIndex]?.scenes[sceneIndex];
    if (!scene) return;

    // Update room highlight
    this.updateRoomHighlight(scene.active_room);

    // Kill pending walk tweens (prevents stale onComplete from spawning bubbles)
    for (const { sprite } of Object.values(this.agentSprites)) {
      this.tweens.killTweensOf(sprite);
    }

    // Clear existing bubbles
    this.clearBubbles();

    for (const [key, { sprite, agent }] of Object.entries(this.agentSprites)) {
      const pos = scene.positions[key];
      if (!pos) continue;

      const targetX = pos.x * T + T / 2;
      const targetY = pos.y * T + T / 2;
      const targetAlpha = pos.state === 'active' ? 1.0 : 0.3;

      // Determine movement direction
      const dx = targetX - sprite.x;
      const dy = targetY - sprite.y;
      const absDx = Math.abs(dx);
      const absDy = Math.abs(dy);
      const isMoving = absDx > T / 2 || absDy > T / 2;

      let walkDir = 'down';
      if (absDx > absDy) {
        walkDir = dx > 0 ? 'right' : 'left';
      } else if (absDy > 0) {
        walkDir = dy > 0 ? 'down' : 'up';
      }

      const spriteKey = agent.sprite;

      // Play walk animation if moving a meaningful distance
      if (isMoving) {
        sprite.play(`${spriteKey}_walk_${walkDir}`);
      }

      this.tweens.add({
        targets: sprite,
        x: targetX,
        y: targetY,
        alpha: targetAlpha,
        duration: isMoving ? 800 : 300,
        ease: 'Power2',
        onUpdate: () => {
          sprite.setDepth(sprite.y);
        },
        onComplete: () => {
          sprite.play(`${spriteKey}_idle_${walkDir}`);
          // Show bubble icon after agent settles (v2 scenes)
          if (pos.state === 'active') {
            this.showBubble(key, scene, sprite);
          }
        },
      });
    }
  }

  /** Determine and show the appropriate bubble icon above an agent. */
  showBubble(agentKey, scene, sprite) {
    // Pick bubble type based on scene type
    const convTypes = ['BRIEFING', 'MEETING', 'REVIEW', 'PAUSE', 'DND'];
    let bubbleKey = null;
    if (convTypes.includes(scene.type)) {
      bubbleKey = 'bubble_speech';
    } else if (scene.artifacts?.length > 0 && scene.participants?.includes(agentKey)) {
      bubbleKey = 'bubble_artifact';
    } else {
      bubbleKey = 'bubble_thought';
    }

    if (!bubbleKey || !this.textures.exists(bubbleKey)) return;

    const bubble = this.add.image(sprite.x, sprite.y - T * 1.5, bubbleKey)
      .setScale(0.5)
      .setAlpha(0)
      .setDepth(9999);

    // Float animation
    this.tweens.add({
      targets: bubble,
      alpha: 0.9,
      y: bubble.y - 4,
      duration: 400,
      ease: 'Power2',
      yoyo: true,
      repeat: -1,
      hold: 2000,
    });

    this.agentSprites[agentKey].bubble = bubble;
  }

  /** Remove all bubble sprites. */
  clearBubbles() {
    for (const entry of Object.values(this.agentSprites)) {
      if (entry.bubble) {
        entry.bubble.destroy();
        entry.bubble = null;
      }
    }
  }

  /** Draw highlight rectangle on the active room. */
  updateRoomHighlight(roomKey) {
    this.roomHighlight.clear();
    if (!roomKey || !ROOMS[roomKey]) return;

    const r = ROOMS[roomKey];
    const x = r.x1 * T;
    const y = r.y1 * T;
    const w = (r.x2 - r.x1 + 1) * T;
    const h = (r.y2 - r.y1 + 1) * T;

    // Semi-transparent fill
    this.roomHighlight.fillStyle(HIGHLIGHT_COLOR, HIGHLIGHT_ALPHA);
    this.roomHighlight.fillRect(x, y, w, h);

    // Glow border
    this.roomHighlight.lineStyle(2, HIGHLIGHT_COLOR, HIGHLIGHT_BORDER_ALPHA);
    this.roomHighlight.strokeRect(x, y, w, h);
  }

  update() {
    const cam = this.cameras.main;
    for (const { el, wx, wy } of this.zoneLabels) {
      el.style.left = `${(wx - cam.worldView.x) * cam.zoom}px`;
      el.style.top = `${(wy - cam.worldView.y) * cam.zoom}px`;
    }

    // Position tooltip near pointer
    if (this.tooltip.classList.contains('visible')) {
      const pointer = this.input.activePointer;
      const container = document.getElementById('game-container');
      const rect = container.getBoundingClientRect();
      this.tooltip.style.left = `${rect.left + pointer.x + 14}px`;
      this.tooltip.style.top = `${rect.top + pointer.y - 10}px`;
    }
  }

  createAgentAnims(spriteKey) {
    for (const [name, { start, count }] of Object.entries(CHAR_ANIMS)) {
      const rate = name.startsWith('idle') ? 6 : 8;
      this.anims.create({
        key: `${spriteKey}_${name}`,
        frames: this.anims.generateFrameNumbers(spriteKey, {
          start, end: start + count - 1,
        }),
        frameRate: rate, repeat: -1,
      });
    }
  }
}
