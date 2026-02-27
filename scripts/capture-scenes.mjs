#!/usr/bin/env node
/**
 * Capture Phaser viewer screenshots for every scene.
 *
 * Pixel-perfect: viewport sized so game-container = exactly 1056×672
 * (half of 44×28 tiles @ 48px = 2112×1344). Zoom = exactly 0.5.
 * After capture, PIL crops dark exterior from the bottom.
 *
 * Prerequisites:
 *   - simulation.json built via build-viewer-data.py
 *   - Vite preview running (npm run preview in frontend/)
 *
 * Usage:
 *   node scripts/capture-scenes.mjs                          # default port 4173
 *   node scripts/capture-scenes.mjs --port 5173              # dev server
 *   node scripts/capture-scenes.mjs --out simulation-1/screenshots
 */

import { createRequire } from 'module';
import { mkdirSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '..');

// Playwright is installed in frontend/node_modules
const require = createRequire(resolve(PROJECT_ROOT, 'frontend', 'package.json'));
const { chromium } = require('playwright');

// Parse args
const args = process.argv.slice(2);
const portIdx = args.indexOf('--port');
const port = portIdx >= 0 ? args[portIdx + 1] : '4173';
const outIdx = args.indexOf('--out');
const outDir = outIdx >= 0
  ? resolve(PROJECT_ROOT, args[outIdx + 1])
  : resolve(PROJECT_ROOT, 'screenshots');

const BASE_URL = `http://localhost:${port}`;
const SETTLE_MS = 1500;

// Map dimensions
const T = 48, MAP_W = 44, MAP_H = 28;
const HALF_W = (MAP_W * T) / 2; // 1056
const HALF_H = (MAP_H * T) / 2; // 672

// Layout offsets: sidebar=340px, bars=51px
const SIDEBAR_W = 340;
const BARS_H = 51;

async function main() {
  mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch();

  // Viewport sized so game-container = 1056×672 CSS px → zoom 0.5.
  // deviceScaleFactor: 2 → screenshot at 2112×1344 device px = native tileset res.
  const page = await browser.newPage({
    viewport: { width: HALF_W + SIDEBAR_W, height: HALF_H + BARS_H },
    deviceScaleFactor: 2,
  });

  console.log(`Navigating to ${BASE_URL}...`);
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });

  // Wait for simulation data to load
  await page.waitForFunction(() => window.__simData != null, { timeout: 15000 });

  // Log actual game-container size for debugging
  const containerSize = await page.evaluate(() => {
    const c = document.getElementById('game-container');
    return { w: c.clientWidth, h: c.clientHeight };
  });
  console.log(`Game container: ${containerSize.w}×${containerSize.h} (target: ${HALF_W}×${HALF_H})`);

  // Wait for initial scene to fully render
  await page.waitForTimeout(2000);

  const simData = await page.evaluate(() => window.__simData);
  console.log(`Found ${simData.days.length} days, ${simData.days.reduce((s, d) => s + d.scenes.length, 0)} scenes total`);

  for (let dayIdx = 0; dayIdx < simData.days.length; dayIdx++) {
    const day = simData.days[dayIdx];
    for (let sceneIdx = 0; sceneIdx < day.scenes.length; sceneIdx++) {
      const scene = day.scenes[sceneIdx];
      const dayNum = String(day.day).padStart(3, '0');
      const sceneNum = String(scene.scene).padStart(3, '0');
      const sceneType = scene.type.replace(/[+]/g, '-');
      const filename = `day-${dayNum}-scene-${sceneNum}-${sceneType}.png`;

      // Dispatch scene change
      await page.evaluate(({ di, si }) => {
        window.dispatchEvent(new CustomEvent('viewer:scene-change', {
          detail: { dayIndex: di, sceneIndex: si },
        }));
      }, { di: dayIdx, si: sceneIdx });

      await page.waitForTimeout(SETTLE_MS);

      // Screenshot game container only
      const gameContainer = await page.$('#game-container');
      if (gameContainer) {
        const filepath = resolve(outDir, filename);
        await gameContainer.screenshot({ path: filepath });
        console.log(`  ${filename}`);
      }
    }
  }

  await browser.close();
  console.log(`\nDone. ${outDir}`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
