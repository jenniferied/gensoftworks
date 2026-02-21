import Phaser from 'phaser';

const T = 48;
const MAP_W = 44;
const MAP_H = 28;
const CHAR_COLS = 56; // columns per combined row in 48×96 character sheets

// --- Room interiors (walkable bounds, inside walls) ---
const ROOMS = {
  '7a':        { x1: 1,  y1: 1,  x2: 7,  y2: 6  },
  '7b':        { x1: 9,  y1: 1,  x2: 15, y2: 6  },
  '7c':        { x1: 17, y1: 1,  x2: 23, y2: 6  },
  'conference': { x1: 25, y1: 1,  x2: 33, y2: 6  },
  'kitchen':   { x1: 35, y1: 1,  x2: 42, y2: 6  },
  'hallway':   { x1: 1,  y1: 9,  x2: 42, y2: 12 },
  '7d':        { x1: 1,  y1: 14, x2: 7,  y2: 18 },
  '7e':        { x1: 9,  y1: 14, x2: 15, y2: 18 },
  '7f':        { x1: 17, y1: 14, x2: 23, y2: 18 },
  'lounge':    { x1: 25, y1: 14, x2: 33, y2: 27 },
  'wc_damen':  { x1: 35, y1: 14, x2: 38, y2: 18 },
  'wc_herren': { x1: 40, y1: 14, x2: 42, y2: 18 },
  '7':         { x1: 1,  y1: 20, x2: 23, y2: 27 },
};


// --- Agent definitions ---
const AGENTS = [
  { key: 'emre',   name: 'Emre Kaya',       role: 'Worldbuilder',       room: '7a', sprite: 'char_05', deskX: 4,  deskY: 3,  facing: 'right' },
  { key: 'vera',   name: 'Vera Morozova',    role: 'Concept Artist',     room: '7b', sprite: 'char_01', deskX: 12, deskY: 3,  facing: 'left'  },
  { key: 'tobi',   name: 'Tobias Richter',   role: 'Tech Lead',          room: '7c', sprite: 'char_03', deskX: 20, deskY: 3,  facing: 'right' },
  { key: 'darius', name: 'Darius Varga',     role: 'Game Director',      room: '7d', sprite: 'char_04', deskX: 4,  deskY: 16, facing: 'right' },
  { key: 'nami',   name: 'Nami Osei',        role: 'Narrative Designer', room: '7e', sprite: 'char_02', deskX: 12, deskY: 16, facing: 'left'  },
  { key: 'leo',    name: 'Leo Ferretti',     role: 'Community Manager',  room: '7f', sprite: 'char_06', deskX: 20, deskY: 16, facing: 'right' },
  { key: 'finn',   name: 'Finn Calloway',    role: 'Producer',           room: '7',  sprite: 'char_07', deskX: 8,  deskY: 23, facing: 'right' },
];

const ZONES = [
  { name: 'Zimmer 7a\nEmre',     x: 0,  y: 0,  w: 8,  h: 8  },
  { name: 'Zimmer 7b\nVera',     x: 8,  y: 0,  w: 8,  h: 8  },
  { name: 'Zimmer 7c\nTobi',     x: 16, y: 0,  w: 8,  h: 8  },
  { name: 'Konferenz',           x: 24, y: 0,  w: 10, h: 8  },
  { name: 'Küche',               x: 34, y: 0,  w: 10, h: 8  },
  { name: 'Zimmer 7d\nDarius',   x: 0,  y: 13, w: 8,  h: 7  },
  { name: 'Zimmer 7e\nNami',     x: 8,  y: 13, w: 8,  h: 7  },
  { name: 'Zimmer 7f\nLeo',      x: 16, y: 13, w: 8,  h: 7  },
  { name: 'Lounge',              x: 24, y: 13, w: 10, h: 15 },
  { name: 'WC Damen',            x: 34, y: 13, w: 5,  h: 7  },
  { name: 'WC Herren',           x: 39, y: 13, w: 5,  h: 7  },
  { name: 'Flur',                x: 0,  y: 8,  w: 44, h: 5  },
  { name: 'Zimmer 7\nFinn + CD', x: 0,  y: 20, w: 24, h: 8  },
];

// Character animation frame map (48×96 frames, 56 cols per combined row)
const CHAR_ANIMS = {
  idle_left:  { start: CHAR_COLS + 0,   count: 6 },
  idle_up:    { start: CHAR_COLS + 6,   count: 6 },
  idle_right: { start: CHAR_COLS + 12,  count: 6 },
  idle_down:  { start: CHAR_COLS + 18,  count: 6 },
};


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
    for (const [name, depth] of [['misc4', -3], ['furniture', -2], ['misc', -1], ['misc2', 0], ['misc3', 1]]) {
      const layer = map.createLayer(name, allTilesets);
      if (layer) layer.setDepth(depth);
    }

    // --- Zone labels (HTML overlay — always sharp, behind characters) ---
    const overlay = document.getElementById('zone-overlay');
    this.zoneLabels = ZONES.map(zone => {
      const el = document.createElement('div');
      el.className = 'zone-label';
      el.textContent = zone.name;
      overlay.appendChild(el);
      return { el, wx: (zone.x + zone.w / 2) * T, wy: (zone.y + zone.h / 2) * T };
    });

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

      // Click → dispatch agent-click event to DOM sidebar
      sprite.on('pointerdown', (pointer) => {
        pointer.event.stopPropagation();
        window.dispatchEvent(new CustomEvent('viewer:agent-click', {
          detail: { agentKey: agent.key },
        }));
      });

      this.agentSprites[agent.key] = { sprite, agent };
    }

    // --- Camera ---
    const cam = this.cameras.main;
    cam.setBounds(0, 0, MAP_W * T, MAP_H * T);
    const zoomX = this.scale.width / (MAP_W * T);
    const zoomY = this.scale.height / (MAP_H * T);
    this.fitZoom = Math.min(zoomX, zoomY);
    cam.setZoom(this.fitZoom);
    cam.centerOn((MAP_W * T) / 2, (MAP_H * T) / 2);

    this.input.on('wheel', (_p, _go, _dx, dy) => {
      cam.setZoom(Phaser.Math.Clamp(cam.zoom - dy * 0.001, this.fitZoom * 0.5, 3));
    });
    this.input.on('pointermove', (p) => {
      if (p.isDown && p.button === 0) {
        cam.scrollX -= (p.x - p.prevPosition.x) / cam.zoom;
        cam.scrollY -= (p.y - p.prevPosition.y) / cam.zoom;
      }
    });

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

  /** Move agents to scene positions with tweens, dim non-participants. */
  loadScene(dayIndex, sceneIndex) {
    const data = window.__simData;
    if (!data) return;
    const scene = data.days[dayIndex]?.scenes[sceneIndex];
    if (!scene) return;

    for (const [key, { sprite, agent }] of Object.entries(this.agentSprites)) {
      const pos = scene.positions[key];
      if (!pos) continue;

      const targetX = pos.x * T + T / 2;
      const targetY = pos.y * T + T / 2;
      const targetAlpha = pos.state === 'active' ? 1.0 : 0.3;

      // Tween position
      this.tweens.add({
        targets: sprite,
        x: targetX,
        y: targetY,
        alpha: targetAlpha,
        duration: 500,
        ease: 'Power2',
        onUpdate: () => {
          // Keep depth sorted by Y position during movement
          sprite.setDepth(sprite.y);
        },
      });
    }
  }

  update() {
    const cam = this.cameras.main;
    for (const { el, wx, wy } of this.zoneLabels) {
      el.style.left = `${(wx - cam.worldView.x) * cam.zoom}px`;
      el.style.top = `${(wy - cam.worldView.y) * cam.zoom}px`;
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
