/**
 * Minimal Phaser entry point for screenshot capture.
 * No sidebar, no audio, no bars — just the tilemap + agents.
 * Canvas = exact tileset dimensions (2112×1344), zoom 1.0.
 */
import Phaser from 'phaser';
import { StudioScene } from './StudioScene.js';

const BASE = import.meta.env.BASE_URL;
const T = 48, MAP_W = 44, MAP_H = 28;

// Load simulation data before starting Phaser
const resp = await fetch(`${BASE}data/simulation.json`);
window.__simData = await resp.json();

const config = {
  type: Phaser.AUTO,
  parent: 'game-container',
  width: MAP_W * T,   // 2112
  height: MAP_H * T,  // 1344
  backgroundColor: '#131317',
  scale: {
    mode: Phaser.Scale.NONE,
    autoCenter: Phaser.Scale.NO_CENTER,
  },
  scene: [StudioScene],
  pixelArt: true,
  roundPixels: true,
};

window.__phaserGame = new Phaser.Game(config);
