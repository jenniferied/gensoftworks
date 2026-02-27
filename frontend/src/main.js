import Phaser from 'phaser';
import { StudioScene } from './StudioScene.js';
import { initSidebar } from './sidebar.js';
import { initAudio } from './audio.js';

const container = document.getElementById('game-container');
const config = {
  type: Phaser.AUTO,
  parent: 'game-container',
  width: container.clientWidth,
  height: container.clientHeight,
  backgroundColor: '#131317',
  scale: {
    mode: Phaser.Scale.RESIZE,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
  scene: [StudioScene],
  pixelArt: true,
  roundPixels: true,
};

window.__phaserGame = new Phaser.Game(config);
initSidebar();
initAudio();
