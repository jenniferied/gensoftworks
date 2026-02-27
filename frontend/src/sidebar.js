/**
 * Sidebar controller — fetches simulation data, populates dropdowns,
 * dispatches viewer events, renders agent details for all participants.
 * Supports multiple simulations via manifest (data/index.json).
 */

const BASE = import.meta.env.BASE_URL;

const AGENT_META = {
  emre:   { name: 'Emre Kaya',       role: 'Worldbuilder',       room: 'Zimmer 12a', gender: '\u2642', flag: '\uD83C\uDDF9\uD83C\uDDF7\uD83C\uDDE9\uD83C\uDDEA' },
  vera:   { name: 'Vera Morozova',    role: 'Concept Artist',     room: 'Zimmer 12b', gender: '\u2640', flag: '\uD83C\uDDF5\uD83C\uDDF1\uD83C\uDDE9\uD83C\uDDEA' },
  tobi:   { name: 'Tobias Richter',   role: 'Tech Lead',          room: 'Zimmer 12c', gender: '\u2642', flag: '\uD83C\uDDE9\uD83C\uDDEA' },
  darius: { name: 'Darius Varga',     role: 'Game Director',      room: 'Zimmer 12d', gender: '\u2642', flag: '\uD83C\uDDE9\uD83C\uDDEA' },
  nami:   { name: 'Nami Osei',        role: 'Narrative Designer', room: 'Schreibstube (12e)', gender: '\u2640', flag: '\uD83C\uDDF3\uD83C\uDDEC\uD83C\uDDE9\uD83C\uDDEA' },
  leo:    { name: 'Leo Ferretti',     role: 'Community Manager',  room: 'Zimmer 12f', gender: '\u2640', flag: '\uD83C\uDDE9\uD83C\uDDEA\uD83C\uDDEE\uD83C\uDDF7' },
  finn:   { name: 'Finn Calloway',    role: 'Producer',           room: 'Zimmer 12 (CD-Büro)', gender: '\u2642', flag: '\uD83C\uDDE9\uD83C\uDDEA' },
};

let simData = null;
let currentDayIdx = 0;
let currentSceneIdx = 0;

// DOM refs
const simSelect = document.getElementById('sim-select');
const daySelect = document.getElementById('day-select');
const sceneSelect = document.getElementById('scene-select');
const sceneBadge = document.getElementById('scene-badge');
const sceneTime = document.getElementById('scene-time');
const sceneLocation = document.getElementById('scene-location');
const sceneParticipants = document.getElementById('scene-participants');
const sceneSummary = document.getElementById('scene-summary');
const keyMoment = document.getElementById('key-moment');
const artifactList = document.getElementById('artifact-list');
const daySummaryEl = document.getElementById('day-summary');
const agentList = document.getElementById('agent-list');
const btnPrev = document.getElementById('btn-prev');
const btnNext = document.getElementById('btn-next');

export async function initSidebar() {
  // Try loading manifest for multi-sim support
  let manifest = null;
  try {
    const resp = await fetch(`${BASE}data/index.json`);
    if (resp.ok) manifest = await resp.json();
  } catch {
    // No manifest — fall back to single simulation.json
  }

  if (manifest && manifest.simulations.length > 0) {
    // Populate sim dropdown
    for (const sim of manifest.simulations) {
      const opt = document.createElement('option');
      opt.value = sim.file;
      opt.textContent = sim.label;
      if (sim.id === manifest.default) opt.selected = true;
      simSelect.appendChild(opt);
    }
    simSelect.style.display = '';
    simSelect.addEventListener('change', () => loadSimulation(simSelect.value));

    // Load default simulation
    const defaultSim = manifest.simulations.find(s => s.id === manifest.default) || manifest.simulations[0];
    await loadSimulation(defaultSim.file);
  } else {
    // Fallback: single simulation.json, hide sim dropdown
    simSelect.style.display = 'none';
    await loadSimulation('simulation.json');
  }

  daySelect.addEventListener('change', () => {
    currentDayIdx = parseInt(daySelect.value);
    currentSceneIdx = 0;
    populateScenes();
    selectScene();
  });

  sceneSelect.addEventListener('change', () => {
    currentSceneIdx = parseInt(sceneSelect.value);
    selectScene();
  });

  // Nav buttons
  btnPrev.addEventListener('click', () => navigate(-1));
  btnNext.addEventListener('click', () => navigate(1));

  // Listen for agent clicks from Phaser — open profile modal
  window.addEventListener('viewer:agent-click', (e) => {
    openAgentProfile(e.detail.agentKey);
  });

  // Close profile modal
  const overlay = document.getElementById('agent-profile-overlay');
  document.getElementById('profile-close').addEventListener('click', () => {
    overlay.classList.remove('open');
  });
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) overlay.classList.remove('open');
  });

  // Close document modal
  const docOverlay = document.getElementById('document-overlay');
  const closeDocModal = () => { docOverlay.classList.remove('open'); docModalState = null; };
  document.getElementById('doc-modal-close').addEventListener('click', closeDocModal);
  docOverlay.addEventListener('click', (e) => {
    if (e.target === docOverlay) closeDocModal();
  });

  // Document version arrow buttons
  document.getElementById('doc-ver-prev').addEventListener('click', () => docModalNavigate(-1));
  document.getElementById('doc-ver-next').addEventListener('click', () => docModalNavigate(1));

  // Keyboard: arrows left/right to switch version, Escape to close
  document.addEventListener('keydown', (e) => {
    if (!docOverlay.classList.contains('open') && !galOverlay.classList.contains('open')) return;
    if (docOverlay.classList.contains('open')) {
      if (e.key === 'ArrowLeft') { e.preventDefault(); docModalNavigate(-1); }
      if (e.key === 'ArrowRight') { e.preventDefault(); docModalNavigate(1); }
      if (e.key === 'Escape') { e.preventDefault(); closeDocModal(); }
    }
    if (galOverlay.classList.contains('open') && e.key === 'Escape') {
      e.preventDefault(); closeGallery();
    }
    if (galLightbox.classList.contains('open') && e.key === 'Escape') {
      e.preventDefault(); galLightbox.classList.remove('open');
    }
  });

  // Gallery button + close
  const galOverlay = document.getElementById('gallery-overlay');
  const galLightbox = document.getElementById('gallery-lightbox');
  const closeGallery = () => galOverlay.classList.remove('open');
  document.getElementById('btn-gallery').addEventListener('click', openGallery);
  document.getElementById('gallery-close').addEventListener('click', closeGallery);
  galOverlay.addEventListener('click', (e) => { if (e.target === galOverlay) closeGallery(); });
  galLightbox.addEventListener('click', () => galLightbox.classList.remove('open'));
}

async function loadSimulation(filename) {
  const resp = await fetch(`${BASE}data/${filename}`);
  simData = await resp.json();
  window.__simData = simData;

  // Reset state
  currentDayIdx = 0;
  currentSceneIdx = 0;

  // Populate day dropdown
  daySelect.innerHTML = '';
  for (let i = 0; i < simData.days.length; i++) {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `Tag ${simData.days[i].day}`;
    daySelect.appendChild(opt);
  }

  populateScenes();
  selectScene();
  renderDocumentBar();

  // Signal Phaser that data is ready
  window.dispatchEvent(new CustomEvent('viewer:data-ready'));
}

function navigate(dir) {
  const day = simData.days[currentDayIdx];
  const newIdx = currentSceneIdx + dir;
  if (newIdx >= 0 && newIdx < day.scenes.length) {
    currentSceneIdx = newIdx;
    sceneSelect.value = currentSceneIdx;
    selectScene();
  } else if (dir > 0 && currentDayIdx < simData.days.length - 1) {
    // Next day, first scene
    currentDayIdx++;
    currentSceneIdx = 0;
    daySelect.value = currentDayIdx;
    populateScenes();
    selectScene();
  } else if (dir < 0 && currentDayIdx > 0) {
    // Previous day, last scene
    currentDayIdx--;
    daySelect.value = currentDayIdx;
    populateScenes();
    currentSceneIdx = simData.days[currentDayIdx].scenes.length - 1;
    sceneSelect.value = currentSceneIdx;
    selectScene();
  }
}

function populateScenes() {
  sceneSelect.innerHTML = '';
  const day = simData.days[currentDayIdx];
  for (let i = 0; i < day.scenes.length; i++) {
    const s = day.scenes[i];
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `${s.type_label} — ${s.time_label}`;
    sceneSelect.appendChild(opt);
  }
  sceneSelect.value = currentSceneIdx;
}

function selectScene() {
  const scene = getCurrentScene();
  if (!scene) return;

  // Update nav button states
  const isFirst = currentDayIdx === 0 && currentSceneIdx === 0;
  const isLast = currentDayIdx === simData.days.length - 1 &&
    currentSceneIdx === simData.days[currentDayIdx].scenes.length - 1;
  btnPrev.disabled = isFirst;
  btnNext.disabled = isLast;

  // Update sidebar content
  sceneBadge.textContent = scene.type_label;
  sceneBadge.className = `badge ${scene.type.replace(/\+/g, '_')}`;
  sceneTime.textContent = scene.time_label;
  sceneLocation.textContent = scene.location_label;

  const names = scene.participants.map(k => AGENT_META[k]?.name || k);
  sceneParticipants.innerHTML = names.map(n => `<span>${n}</span>`).join(', ');

  sceneSummary.textContent = scene.summary;

  if (scene.key_moment) {
    keyMoment.textContent = scene.key_moment;
    keyMoment.style.display = 'block';
  } else {
    keyMoment.style.display = 'none';
  }

  // Render day summary bubble
  renderDaySummary();

  // Render artifacts
  renderArtifacts(scene.artifacts || []);

  // Render all agent cards (participants first, then dimmed non-participants)
  renderAgentCards(scene);

  // Update document bar for current time
  renderDocumentBar();

  // Dispatch scene change to Phaser
  window.dispatchEvent(new CustomEvent('viewer:scene-change', {
    detail: { dayIndex: currentDayIdx, sceneIndex: currentSceneIdx },
  }));
}

function getCurrentScene() {
  if (!simData) return null;
  return simData.days[currentDayIdx]?.scenes[currentSceneIdx] || null;
}

function renderDaySummary() {
  const day = simData.days[currentDayIdx];
  const summary = day?.summary;
  if (!summary) {
    daySummaryEl.style.display = 'none';
    return;
  }

  let html = '';
  html += `<div class="day-summary-header" id="day-summary-toggle">`;
  html += `<span class="arrow">&#9654;</span>`;
  html += `<span class="day-summary-icon">&#128203;</span>`;
  html += `ZUSAMMENFASSUNG — Tag ${summary.day || day.day}`;
  html += `</div>`;

  html += `<div class="day-summary-body" id="day-summary-body">`;
  if (summary.phase) {
    html += `<span class="day-summary-phase">${summary.phase}</span> `;
  }
  html += `<div class="day-summary-title">${summary.title || ''}</div>`;
  html += `<div class="day-summary-text">${summary.summary || ''}</div>`;

  // CD decisions
  if (summary.cd_decisions?.length) {
    html += `<div class="day-summary-decisions">`;
    html += `<div class="day-summary-decisions-label">CD-Entscheidungen</div>`;
    for (const d of summary.cd_decisions) {
      html += `<div class="day-summary-decision">${d}</div>`;
    }
    html += `</div>`;
  }

  // Key moments
  if (summary.key_moments?.length) {
    html += `<div class="day-summary-moments">`;
    for (const m of summary.key_moments) {
      html += `<div class="day-summary-moment">${m}</div>`;
    }
    html += `</div>`;
  }
  html += `</div>`;

  daySummaryEl.innerHTML = html;
  daySummaryEl.style.display = 'block';

  // Wire up toggle
  document.getElementById('day-summary-toggle').addEventListener('click', () => {
    const body = document.getElementById('day-summary-body');
    const arrow = document.querySelector('#day-summary-toggle .arrow');
    body.classList.toggle('open');
    arrow.classList.toggle('open');
  });
}

function renderArtifacts(artifacts) {
  if (!artifacts || artifacts.length === 0) {
    artifactList.style.display = 'none';
    return;
  }

  artifactList.style.display = 'block';
  let html = '<div class="artifacts-title">ARTEFAKTE</div>';
  for (const path of artifacts) {
    const filename = path.split('/').pop();
    const isImage = /\.(png|jpg|jpeg|gif|webp)$/i.test(filename);
    const icon = isImage ? '[img]' : '[doc]';
    html += `<div class="artifact-item">`;
    html += `<span class="artifact-icon">${icon}</span>`;
    html += `<span class="artifact-name" title="${path}">${filename}</span>`;
    html += `</div>`;
  }
  artifactList.innerHTML = html;
}

const TRACE_FILES = [
  { key: '0-prompt.md', label: 'Prompt' },
  { key: '1-reasoning.md', label: 'Reasoning' },
  { key: '2-output.md', label: 'Output' },
];

function renderTraceBlock(idPrefix, tracePath) {
  let html = '<div class="trace-block">';
  html += '<div class="trace-block-label">TRACES</div>';
  for (const tf of TRACE_FILES) {
    const bodyId = `${idPrefix}-${tf.key.replace('.', '-')}`;
    const url = `${BASE}${tracePath}${tf.key}`;
    html += `<button class="trace-toggle" data-target="${bodyId}" data-url="${url}">`;
    html += `<span class="arrow">&#9654;</span> ${tf.label}`;
    html += `</button>`;
    html += `<div class="trace-body" id="${bodyId}"><span class="loading">Laden...</span></div>`;
  }
  html += '</div>';
  return html;
}

function renderAgentCards(scene) {
  const participants = scene.participants;
  const allAgents = Object.keys(AGENT_META);
  const ordered = [
    ...participants.filter(k => AGENT_META[k]),
    ...allAgents.filter(k => !participants.includes(k)),
  ];

  // Detect schema: v2 has scene.mood as object, v1 has scene.agent_details
  const isV2 = scene.mood && typeof scene.mood === 'object' && !Array.isArray(scene.mood);

  let html = '';

  // Shared trace block for conversation scenes (BRIEFING, MEETING, etc.)
  if (scene.traces?._shared) {
    html += renderTraceBlock('trace-shared', scene.traces._shared);
  }

  for (const key of ordered) {
    const meta = AGENT_META[key];
    const isActive = participants.includes(key);

    html += `<div class="agent-card${isActive ? '' : ' dimmed'}" id="agent-card-${key}">`;
    html += `<div class="agent-card-header">`;
    html += `<span class="agent-name">${meta.name}</span>`;
    html += `<span class="agent-role">${meta.role}</span>`;
    html += `</div>`;

    if (isActive) {
      if (isV2) {
        // --- v2 rendering ---
        const mood = scene.mood?.[key];
        if (mood) {
          html += `<div class="mood-row">`;
          html += `<span class="mood-label">Stimmung:</span> `;
          html += `<span class="mood-value">${mood.before || '—'}</span> `;
          html += `<span class="mood-arrow">&rarr;</span> `;
          html += `<span class="mood-value">${mood.after || '—'}</span>`;
          html += `</div>`;
        }

        // Dialogue lines for this agent
        const agentDialogue = (scene.dialogue || []).filter(d => d.who === key);
        if (agentDialogue.length) {
          html += `<div class="dialogue-section">`;
          for (const d of agentDialogue) {
            html += `<div class="dialogue-line">"${d.says}"</div>`;
          }
          html += `</div>`;
        }

        // Thoughts for this agent
        const agentThoughts = (scene.thoughts || []).filter(t => t.who === key);
        if (agentThoughts.length) {
          for (const t of agentThoughts) {
            html += `<div class="agent-thought">${t.thinks}</div>`;
          }
        }

        // Feedback given/received
        const fbGiven = (scene.feedback || []).filter(f => f.from === key);
        const fbReceived = (scene.feedback || []).filter(f => f.to === key);
        if (fbGiven.length) {
          for (const fb of fbGiven) {
            const toName = AGENT_META[fb.to]?.name || fb.to;
            html += `<div class="agent-feedback given">&rarr; ${toName}: ${fb.text}</div>`;
          }
        }
        if (fbReceived.length) {
          for (const fb of fbReceived) {
            const fromName = AGENT_META[fb.from]?.name || fb.from;
            html += `<div class="agent-feedback received">&larr; ${fromName}: ${fb.text}</div>`;
          }
        }

        // Memories inline
        const agentMems = (scene.memories?.[key]) || [];
        if (agentMems.length) {
          html += `<div class="memories-title">Erinnerungen</div>`;
          for (const m of agentMems) {
            html += `<div class="memory-item">`;
            html += `<span class="mem-importance">${m.importance}/10</span>`;
            html += m.description;
            html += `</div>`;
          }
        }
      } else {
        // --- v1 rendering ---
        const details = scene.agent_details?.[key];
        const mems = scene.memories?.[key];

        if (details) {
          html += `<div class="mood-row">`;
          html += `<span class="mood-label">Stimmung:</span> `;
          html += `<span class="mood-value">${details.mood_before || '—'}</span> `;
          html += `<span class="mood-arrow">&rarr;</span> `;
          html += `<span class="mood-value">${details.mood_after || '—'}</span>`;
          html += `</div>`;

          if (details.key_reaction) {
            html += `<div class="agent-reaction">${details.key_reaction}</div>`;
          }
          if (details.influences?.length) {
            html += `<div class="agent-influences">Einfl\u00fcsse: ${details.influences.map(i => `<span>${i}</span>`).join(', ')}</div>`;
          }
        }

        if (mems?.length) {
          html += `<div class="memories-title">Erinnerungen</div>`;
          for (const m of mems) {
            html += `<div class="memory-item">`;
            html += `<span class="mem-type">${m.type}</span>`;
            html += `<span class="mem-importance">${m.importance}/10</span>`;
            html += m.description;
            html += `</div>`;
          }
        }
      }

      // Per-agent trace block (WORK scenes)
      if (scene.traces?.[key]) {
        html += renderTraceBlock(`trace-${key}`, scene.traces[key]);
      }
    }

    html += `</div>`;
  }

  agentList.innerHTML = html;

  // Wire up trace toggle buttons with lazy fetch
  agentList.querySelectorAll('.trace-toggle').forEach(btn => {
    btn.addEventListener('click', async () => {
      const target = document.getElementById(btn.dataset.target);
      const arrow = btn.querySelector('.arrow');
      if (target.classList.contains('open')) {
        target.classList.remove('open');
        arrow.classList.remove('open');
        return;
      }
      arrow.classList.add('open');
      // Lazy fetch on first open
      if (target.dataset.loaded !== 'true') {
        try {
          const resp = await fetch(btn.dataset.url);
          if (resp.ok) {
            const md = await resp.text();
            target.innerHTML = renderMarkdownFull(md);
          } else {
            target.innerHTML = '<span class="loading">Nicht gefunden.</span>';
          }
        } catch {
          target.innerHTML = '<span class="loading">Fehler beim Laden.</span>';
        }
        target.dataset.loaded = 'true';
      }
      target.classList.add('open');
    });
  });
}

// --- Document Bar ---

// Paper sound — place paper-turn.mp3 in public/audio/
const paperSound = new Audio(`${BASE}audio/paper-turn.mp3`);
paperSound.preload = 'auto';
paperSound.volume = 0.7;

function playPaperSound() {
  paperSound.currentTime = 0;
  paperSound.play().catch(() => {});
}

// Active modal state for keyboard nav
let docModalState = null; // {docType, chapter, versionIdx}

/** Check if a timestamp is at or before the current day/scene. */
function isBeforeOrAtCurrent(ap) {
  if (!ap) return false;
  const curDay = simData.days[currentDayIdx]?.day || 1;
  const curScene = simData.days[currentDayIdx]?.scenes[currentSceneIdx]?.scene || 1;
  return ap.day < curDay || (ap.day === curDay && ap.scene <= curScene);
}

/** Check if a chapter exists at the current point (uses first_appeared). */
function chapterVisible(ch) {
  return isBeforeOrAtCurrent(ch.first_appeared);
}

/** Get versions visible at current time. Falls back to all versions if chapter is visible. */
function getVisibleVersions(ch) {
  if (!chapterVisible(ch)) return [];
  const filtered = ch.versions.filter(v => isBeforeOrAtCurrent(v.appeared));
  // If chapter appeared but no specific version has timeline data, show all available
  return filtered.length > 0 ? filtered : ch.versions;
}

function renderDocumentBar() {
  const bar = document.getElementById('document-bar-content');
  const chapters = simData?.chapters;
  if (!chapters || (!chapters.gdd?.length && !chapters.wbb?.length)) {
    bar.innerHTML = '';
    return;
  }

  let html = '';
  for (const docType of ['gdd', 'wbb']) {
    const list = chapters[docType];
    if (!list?.length) continue;
    // Filter to chapters that exist at current point in time
    const visible = list.filter(chapterVisible);
    if (!visible.length) continue;
    html += `<div class="doc-group">`;
    html += `<span class="doc-group-label">${docType.toUpperCase()}</span>`;
    for (const ch of visible) {
      const visVers = getVisibleVersions(ch);
      const latest = visVers[visVers.length - 1];
      const pageCount = Math.min(visVers.length + 1, 4);
      html += `<div class="doc-stack" data-doc-type="${docType}" data-chapter-id="${ch.id}" title="${ch.title}">`;
      html += `<div class="doc-pages">`;
      for (let i = 0; i < pageCount; i++) {
        html += `<div class="doc-page" style="left:${i * 2}px;bottom:${i}px;"></div>`;
      }
      html += `</div>`;
      html += `<div class="doc-label">${ch.id.slice(0, 2)} v${latest.version}</div>`;
      html += `</div>`;
    }
    html += `</div>`;
  }

  bar.innerHTML = html;

  bar.querySelectorAll('.doc-stack').forEach(el => {
    el.addEventListener('click', () => {
      openDocumentModal(el.dataset.docType, el.dataset.chapterId);
    });
  });

  // Update gallery icon state + counter
  const artCount = getVisibleArt().length;
  const galBtn = document.getElementById('btn-gallery');
  const galCount = document.getElementById('gallery-count');
  if (galBtn) galBtn.classList.toggle('has-art', artCount > 0);
  if (galCount) galCount.textContent = artCount > 0 ? artCount : '';
}

function openDocumentModal(docType, chapterId) {
  const chapters = simData?.chapters?.[docType];
  if (!chapters) return;
  const chapter = chapters.find(c => c.id === chapterId);
  if (!chapter) return;
  const visVers = getVisibleVersions(chapter);
  if (!visVers.length) return;

  playPaperSound();

  document.getElementById('doc-modal-badge').textContent = docType.toUpperCase();
  document.getElementById('doc-modal-badge').className = `badge doc-modal-badge ${docType}`;
  document.getElementById('doc-modal-title').textContent = chapter.title;

  // Start at highest visible version
  docModalState = { docType, chapter, versions: visVers, versionIdx: visVers.length - 1 };
  renderDocModalVersion();

  document.getElementById('document-overlay').classList.add('open');
}

function renderDocModalVersion() {
  if (!docModalState) return;
  const { versions, versionIdx } = docModalState;
  const v = versions[versionIdx];
  const total = versions.length;

  const contentEl = document.getElementById('doc-modal-content');
  const navEl = document.getElementById('doc-modal-nav');
  const versionEl = document.getElementById('doc-modal-version');
  const prevBtn = document.getElementById('doc-ver-prev');
  const nextBtn = document.getElementById('doc-ver-next');
  const labelEl = document.getElementById('doc-ver-label');

  contentEl.innerHTML = renderMarkdownFull(v.content);
  versionEl.textContent = `V${v.version}`;

  if (total > 1) {
    navEl.style.display = 'flex';
    labelEl.textContent = `V${v.version} von ${versions[total - 1].version}`;
    prevBtn.disabled = versionIdx === 0;
    nextBtn.disabled = versionIdx === total - 1;
  } else {
    navEl.style.display = 'none';
  }

  // Scroll to top
  document.getElementById('document-modal').scrollTop = 0;
}

function docModalNavigate(dir) {
  if (!docModalState) return;
  const newIdx = docModalState.versionIdx + dir;
  if (newIdx < 0 || newIdx >= docModalState.versions.length) return;
  docModalState.versionIdx = newIdx;
  playPaperSound();
  renderDocModalVersion();
}

// --- Concept Art Gallery ---

function getVisibleArt() {
  const art = simData?.concept_art;
  if (!art?.length) return [];
  const curDay = simData.days[currentDayIdx]?.day || 1;
  const curScene = simData.days[currentDayIdx]?.scenes[currentSceneIdx]?.scene || 1;
  return art.filter(a => {
    const ap = a.appeared;
    if (!ap) return false; // no timeline → hidden until referenced
    return ap.day < curDay || (ap.day === curDay && ap.scene <= curScene);
  });
}

function renderGalleryBoard() {
  const visible = getVisibleArt();
  const grid = document.getElementById('gallery-grid');
  const empty = document.getElementById('gallery-empty');
  const btn = document.getElementById('btn-gallery');

  // Toggle icon highlight
  btn.classList.toggle('has-art', visible.length > 0);

  if (!visible.length) {
    empty.style.display = 'block';
    grid.innerHTML = '';
    return;
  }
  empty.style.display = 'none';

  // Adaptive thumb size: fewer images → bigger
  const thumbSize = visible.length <= 4 ? 260 : visible.length <= 12 ? 180 : 130;
  grid.style.setProperty('--gallery-thumb', `${thumbSize}px`);

  let html = '';
  for (const img of visible) {
    html += `<div class="gallery-card" data-path="${img.path}">`;
    html += `<img src="${BASE}${img.path}" alt="${img.filename}" loading="lazy">`;
    html += `<div class="gallery-card-label">`;
    html += `<span class="gallery-card-category">${img.category}</span> ${img.filename}`;
    html += `</div></div>`;
  }
  grid.innerHTML = html;

  // Click → lightbox
  grid.querySelectorAll('.gallery-card').forEach(card => {
    card.addEventListener('click', () => {
      const lb = document.getElementById('gallery-lightbox');
      document.getElementById('gallery-lightbox-img').src = `${BASE}${card.dataset.path}`;
      lb.classList.add('open');
    });
  });
}

function openGallery() {
  playPaperSound();
  renderGalleryBoard();
  document.getElementById('gallery-overlay').classList.add('open');
}

/** Extended markdown → HTML for document chapters. */
function renderMarkdownFull(md) {
  const lines = md.split('\n');
  let html = '';
  let inList = false;
  let listType = 'ul';
  let inBlockquote = false;

  for (const line of lines) {
    const trimmed = line.trim();

    // Empty line
    if (!trimmed) {
      if (inList) { html += `</${listType}>`; inList = false; }
      if (inBlockquote) { html += '</blockquote>'; inBlockquote = false; }
      continue;
    }

    // Horizontal rule
    if (/^[-*_]{3,}$/.test(trimmed)) {
      if (inList) { html += `</${listType}>`; inList = false; }
      html += '<hr>';
      continue;
    }

    // Headings
    if (trimmed.startsWith('### ')) {
      if (inList) { html += `</${listType}>`; inList = false; }
      html += `<h3>${inlineFormat(trimmed.slice(4))}</h3>`;
      continue;
    }
    if (trimmed.startsWith('## ')) {
      if (inList) { html += `</${listType}>`; inList = false; }
      html += `<h2>${inlineFormat(trimmed.slice(3))}</h2>`;
      continue;
    }
    if (trimmed.startsWith('# ')) {
      if (inList) { html += `</${listType}>`; inList = false; }
      html += `<h1>${inlineFormat(trimmed.slice(2))}</h1>`;
      continue;
    }

    // Blockquote
    if (trimmed.startsWith('> ')) {
      if (inList) { html += `</${listType}>`; inList = false; }
      if (!inBlockquote) { html += '<blockquote>'; inBlockquote = true; }
      html += `<p>${inlineFormat(trimmed.slice(2))}</p>`;
      continue;
    }
    if (inBlockquote) { html += '</blockquote>'; inBlockquote = false; }

    // Unordered list
    if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
      if (inList && listType !== 'ul') { html += `</${listType}>`; inList = false; }
      if (!inList) { html += '<ul>'; inList = true; listType = 'ul'; }
      html += `<li>${inlineFormat(trimmed.slice(2))}</li>`;
      continue;
    }

    // Ordered list
    const olMatch = trimmed.match(/^(\d+)\.\s+(.+)/);
    if (olMatch) {
      if (inList && listType !== 'ol') { html += `</${listType}>`; inList = false; }
      if (!inList) { html += '<ol>'; inList = true; listType = 'ol'; }
      html += `<li>${inlineFormat(olMatch[2])}</li>`;
      continue;
    }

    if (inList) { html += `</${listType}>`; inList = false; }

    // Paragraph
    html += `<p>${inlineFormat(trimmed)}</p>`;
  }

  if (inList) html += `</${listType}>`;
  if (inBlockquote) html += '</blockquote>';
  return html;
}

/** Lightweight markdown → HTML for profile sections. */
function renderMarkdownLight(md) {
  const lines = md.split('\n');
  let html = '';
  let inList = false;
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      if (inList) { html += '</ul>'; inList = false; }
      continue;
    }
    // List items
    if (trimmed.startsWith('- ')) {
      if (!inList) { html += '<ul style="margin:2px 0 2px 14px;padding:0;list-style:disc;">'; inList = true; }
      html += `<li>${inlineFormat(trimmed.slice(2))}</li>`;
      continue;
    }
    if (inList) { html += '</ul>'; inList = false; }
    // Paragraph
    html += `<p>${inlineFormat(trimmed)}</p>`;
  }
  if (inList) html += '</ul>';
  return html;
}

function inlineFormat(text) {
  return text
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/_(.+?)_/g, '<em>$1</em>');
}

function openAgentProfile(agentKey) {
  const meta = AGENT_META[agentKey];
  if (!meta) return;

  // Header with icons
  document.getElementById('profile-name').textContent = meta.name;
  document.getElementById('profile-role').textContent = meta.role;
  document.getElementById('profile-room').textContent = meta.room;
  document.getElementById('profile-icons').textContent = `${meta.gender} ${meta.flag}`;

  const memSection = document.getElementById('profile-memory');
  let html = '';

  // --- Memory section (top, open by default) ---
  const agentMems = simData?.agent_memories?.[agentKey] || [];
  const currentDay = simData.days[currentDayIdx]?.day || 1;
  const currentScene = simData.days[currentDayIdx]?.scenes[currentSceneIdx]?.scene || 1;
  const filtered = agentMems.filter(m =>
    m.day < currentDay || (m.day === currentDay && m.scene <= currentScene)
  );

  html += `<button class="section-toggle" data-target="mem-list">`;
  html += `<span class="arrow open">\u25B6</span> Erinnerungen (${filtered.length})`;
  html += `</button>`;
  html += '<div class="section-body" id="mem-list">';
  if (filtered.length === 0) {
    html += '<div class="memory-empty">Noch keine Erinnerungen bis zu dieser Szene.</div>';
  } else {
    for (const m of filtered.slice().reverse()) {
      html += '<div class="memory-entry">';
      html += `<div class="memory-entry-header">Tag ${m.day}, Szene ${m.scene} (${m.type})</div>`;
      html += `<div>${m.text}</div>`;
      html += '</div>';
    }
  }
  html += '</div>';

  // --- Profile section (below, closed by default) ---
  const roster = simData?.roster?.[agentKey];
  html += `<button class="section-toggle" data-target="bio-list">`;
  html += `<span class="arrow">\u25B6</span> Steckbrief`;
  html += `</button>`;
  html += '<div class="section-body" id="bio-list" style="display: none;">';
  if (roster) {
    // Color dot + basic info
    if (roster.color) {
      html += `<div class="bio-row"><span class="profile-color-dot" style="background:${roster.color}"></span><span class="bio-value">${roster.name}</span></div>`;
    }
    const rows = [
      ['Alter', roster.age],
      ['Pronouns', roster.pronouns],
      ['Arbeitsplatz', roster.workspace],
      ['Hintergrund', roster.background],
      ['Adresse', roster.address],
      ['Arbeitsweg', roster.commute],
    ];
    for (const [label, value] of rows) {
      if (value) {
        html += `<div class="bio-row"><span class="bio-label">${label}:</span><span class="bio-value">${value}</span></div>`;
      }
    }
  } else {
    html += '<div class="memory-empty">Kein Profil verfügbar.</div>';
  }
  html += '</div>';

  // --- Rich profile sections from roster markdown ---
  if (roster?.sections) {
    const sectionIcons = {
      'Identität': '\u2726',
      'Herkunft & Bildung': '\uD83C\uDF93',
      'Persönlichkeit': '\u2665',
      'Lieblingsspiele': '\uD83C\uDFAE',
      'Privatleben': '\uD83C\uDFE0',
      'D&D': '\uD83C\uDFB2',
      'Arbeitsstil': '\u23F0',
      'Werkzeuge': '\uD83D\uDEE0',
      'Schlüsselbeziehungen': '\uD83E\uDD1D',
    };
    let secIdx = 0;
    for (const [title, content] of Object.entries(roster.sections)) {
      const icon = sectionIcons[title] || '\u25CB';
      const secId = `profile-sec-${secIdx++}`;
      html += `<button class="section-toggle" data-target="${secId}">`;
      html += `<span class="arrow">\u25B6</span> ${icon} ${title}`;
      html += `</button>`;
      html += `<div class="section-body" id="${secId}" style="display: none;">`;
      html += `<div class="profile-section-content">${renderMarkdownLight(content)}</div>`;
      html += `</div>`;
    }
  }

  memSection.innerHTML = html;

  // Wire up toggle buttons
  memSection.querySelectorAll('.section-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = document.getElementById(btn.dataset.target);
      const arrow = btn.querySelector('.arrow');
      if (target.style.display === 'none') {
        target.style.display = 'block';
        arrow.classList.add('open');
      } else {
        target.style.display = 'none';
        arrow.classList.remove('open');
      }
    });
  });

  document.getElementById('agent-profile-overlay').classList.add('open');

  // Also scroll sidebar to this agent's card
  const card = document.getElementById(`agent-card-${agentKey}`);
  if (card) card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
