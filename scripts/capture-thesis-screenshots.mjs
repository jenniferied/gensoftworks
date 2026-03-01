#!/usr/bin/env node
/**
 * Capture screenshots for the master thesis and logbook export.
 *
 * Produces:
 *   1. Per-day office screenshots (game canvas only, first scene of each day)
 *   2. Two thesis figures:
 *      - "office-empty": Day 1 Scene 1 (most agents dimmed) — game canvas only
 *      - "office-full-sidebar": A busy scene with sidebar visible — full viewport
 *
 * Prerequisites:
 *   - simulation.json in frontend/public/data/
 *   - Vite dev or preview server running
 *
 * Usage:
 *   node scripts/capture-thesis-screenshots.mjs --port 5173 --out simulation-1/screenshots
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

const args = process.argv.slice(2);
const portIdx = args.indexOf('--port');
const port = portIdx >= 0 ? args[portIdx + 1] : '4173';
const outIdx = args.indexOf('--out');
const outDir = outIdx >= 0
  ? resolve(PROJECT_ROOT, args[outIdx + 1])
  : resolve(PROJECT_ROOT, 'screenshots');

const BASE_URL = `http://localhost:${port}`;
const SETTLE_MS = 1200;

async function navigateToScene(page, dayIdx, sceneIdx) {
  await page.evaluate(({ di, si }) => {
    const daySelect = document.getElementById('day-select');
    const sceneSelect = document.getElementById('scene-select');
    if (daySelect) {
      daySelect.value = di;
      daySelect.dispatchEvent(new Event('change'));
    }
    setTimeout(() => {
      if (sceneSelect) {
        sceneSelect.value = si;
        sceneSelect.dispatchEvent(new Event('change'));
      }
    }, 50);
  }, { di: dayIdx, si: sceneIdx });

  await page.evaluate(({ di, si }) => {
    window.dispatchEvent(new CustomEvent('viewer:scene-change', {
      detail: { dayIndex: di, sceneIndex: si },
    }));
  }, { di: dayIdx, si: sceneIdx });

  await page.waitForTimeout(SETTLE_MS);
}

async function main() {
  mkdirSync(outDir, { recursive: true });
  mkdirSync(resolve(outDir, 'thesis'), { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  console.log(`Navigating to ${BASE_URL}...`);
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  await page.waitForFunction(() => window.__simData != null, { timeout: 15000 });
  const simData = await page.evaluate(() => window.__simData);

  const totalScenes = simData.days.reduce((s, d) => s + d.scenes.length, 0);
  console.log(`Found ${simData.days.length} days, ${totalScenes} scenes total`);

  // --- 1. Per-day screenshots (office only, first scene of each day) ---
  console.log('\n--- Per-day office screenshots ---');
  for (let dayIdx = 0; dayIdx < simData.days.length; dayIdx++) {
    const day = simData.days[dayIdx];
    const dayNum = String(day.day).padStart(3, '0');

    // Use the last scene of the day for "busiest" state
    const lastSceneIdx = day.scenes.length - 1;
    await navigateToScene(page, dayIdx, lastSceneIdx);

    const gameContainer = await page.$('#game-container');
    if (gameContainer) {
      const filename = `day-${dayNum}-office.png`;
      await gameContainer.screenshot({ path: resolve(outDir, filename) });
      console.log(`  ${filename}`);
    }
  }

  // --- 2. Thesis figure: empty office (Day 1, Scene 1) ---
  console.log('\n--- Thesis figures ---');
  await navigateToScene(page, 0, 0);
  const gameContainer = await page.$('#game-container');
  if (gameContainer) {
    const filename = 'thesis/office-early.png';
    await gameContainer.screenshot({ path: resolve(outDir, filename) });
    console.log(`  ${filename} (Day 1, Scene 1 — mostly dimmed agents)`);
  }

  // --- 3. Thesis figure: full viewport with sidebar (busy scene) ---
  // Pick Day 4 (many artifacts accumulated), mid-scene
  const day4Idx = simData.days.findIndex(d => d.day === 4);
  if (day4Idx >= 0) {
    const day4 = simData.days[day4Idx];
    const midScene = Math.floor(day4.scenes.length / 2);
    await navigateToScene(page, day4Idx, midScene);
  } else {
    // Fallback: last day, last scene
    const lastDay = simData.days.length - 1;
    const lastScene = simData.days[lastDay].scenes.length - 1;
    await navigateToScene(page, lastDay, lastScene);
  }

  const fullFilename = 'thesis/office-full-sidebar.png';
  await page.screenshot({ path: resolve(outDir, fullFilename) });
  console.log(`  ${fullFilename} (full viewport with sidebar)`);

  await browser.close();
  console.log(`\nDone. Output: ${outDir}`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
