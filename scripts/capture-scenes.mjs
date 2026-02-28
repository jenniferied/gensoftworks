#!/usr/bin/env node
/**
 * Capture Phaser viewer screenshots for every scene.
 *
 * Uses capture.html — a minimal Phaser page (no sidebar/bars).
 * Phaser canvas = exact tileset dimensions (2112×1344), zoom 1.0.
 * Viewport = same size → pixel-perfect native resolution screenshots.
 *
 * Prerequisites:
 *   - simulation.json built via build-viewer-data.py
 *   - Vite dev/preview running (npm run preview in frontend/)
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

// Native tileset resolution
const T = 48, MAP_W = 44, MAP_H = 28;
const NATIVE_W = MAP_W * T; // 2112
const NATIVE_H = MAP_H * T; // 1344

// Capture page (minimal Phaser, no sidebar/bars)
const CAPTURE_PATH = '/gensoftworks/capture.html';

async function main() {
  mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch();

  // Viewport = exact tileset dimensions → pixel-perfect capture
  const page = await browser.newPage({
    viewport: { width: NATIVE_W, height: NATIVE_H },
  });

  console.log(`Navigating to ${BASE_URL}${CAPTURE_PATH}...`);
  await page.goto(`${BASE_URL}${CAPTURE_PATH}`, { waitUntil: 'networkidle' });

  // Wait for simulation data to load
  await page.waitForFunction(() => window.__simData != null, { timeout: 15000 });

  // Log canvas size for debugging
  const canvasSize = await page.evaluate(() => {
    const canvas = document.querySelector('canvas');
    return canvas ? { w: canvas.width, h: canvas.height } : null;
  });
  console.log(`Canvas: ${canvasSize?.w}×${canvasSize?.h} (target: ${NATIVE_W}×${NATIVE_H})`);

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

      // Screenshot the Phaser canvas directly
      const canvas = await page.$('canvas');
      if (canvas) {
        const filepath = resolve(outDir, filename);
        await canvas.screenshot({ path: filepath });
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
