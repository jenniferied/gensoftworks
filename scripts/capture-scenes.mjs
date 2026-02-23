#!/usr/bin/env node
/**
 * Capture Phaser viewer screenshots for every scene.
 *
 * Prerequisites:
 *   - `npm run build:data` (or --sim-dir equivalent) to populate simulation.json
 *   - Vite preview running on http://localhost:4173 (or dev on 5173)
 *
 * Usage:
 *   node scripts/capture-scenes.mjs                          # default port 4173
 *   node scripts/capture-scenes.mjs --port 5173              # dev server
 *   node scripts/capture-scenes.mjs --out simulation-1/screenshots
 */

import { chromium } from 'playwright';
import { mkdirSync, existsSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '..');

// Parse args
const args = process.argv.slice(2);
const portIdx = args.indexOf('--port');
const port = portIdx >= 0 ? args[portIdx + 1] : '4173';
const outIdx = args.indexOf('--out');
const outDir = outIdx >= 0
  ? resolve(PROJECT_ROOT, args[outIdx + 1])
  : resolve(PROJECT_ROOT, 'screenshots');

const BASE_URL = `http://localhost:${port}`;
const SETTLE_MS = 800; // wait for agent tweens

async function main() {
  mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

  console.log(`Navigating to ${BASE_URL}...`);
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });

  // Wait for simulation data to load
  await page.waitForFunction(() => window.__simData != null, { timeout: 15000 });
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

      // Dispatch scene change event
      await page.evaluate(({ di, si }) => {
        window.dispatchEvent(new CustomEvent('viewer:scene-change', {
          detail: { dayIndex: di, sceneIndex: si },
        }));
      }, { di: dayIdx, si: sceneIdx });

      // Also update sidebar selects
      await page.evaluate(({ di, si }) => {
        const daySelect = document.getElementById('day-select');
        const sceneSelect = document.getElementById('scene-select');
        if (daySelect) {
          daySelect.value = di;
          daySelect.dispatchEvent(new Event('change'));
        }
        // Wait a tick for scene select to populate
        setTimeout(() => {
          if (sceneSelect) {
            sceneSelect.value = si;
            sceneSelect.dispatchEvent(new Event('change'));
          }
        }, 50);
      }, { di: dayIdx, si: sceneIdx });

      // Wait for tweens to settle
      await page.waitForTimeout(SETTLE_MS);

      // Screenshot the game container only (not sidebar)
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
