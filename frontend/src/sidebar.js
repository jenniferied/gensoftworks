/**
 * Sidebar controller — fetches simulation.json, populates dropdowns,
 * dispatches viewer events, renders agent details for all participants.
 */

const AGENT_META = {
  emre:   { name: 'Emre Kaya',       role: 'Worldbuilder' },
  vera:   { name: 'Vera Morozova',    role: 'Concept Artist' },
  tobi:   { name: 'Tobias Richter',   role: 'Tech Lead' },
  darius: { name: 'Darius Varga',     role: 'Game Director' },
  nami:   { name: 'Nami Osei',        role: 'Narrative Designer' },
  leo:    { name: 'Leo Ferretti',     role: 'Community Manager' },
  finn:   { name: 'Finn Calloway',    role: 'Producer' },
};

let simData = null;
let currentDayIdx = 0;
let currentSceneIdx = 0;

// DOM refs
const daySelect = document.getElementById('day-select');
const sceneSelect = document.getElementById('scene-select');
const sceneBadge = document.getElementById('scene-badge');
const sceneTime = document.getElementById('scene-time');
const sceneLocation = document.getElementById('scene-location');
const sceneParticipants = document.getElementById('scene-participants');
const sceneSummary = document.getElementById('scene-summary');
const keyMoment = document.getElementById('key-moment');
const agentList = document.getElementById('agent-list');
const btnPrev = document.getElementById('btn-prev');
const btnNext = document.getElementById('btn-next');

export async function initSidebar() {
  const resp = await fetch('/data/simulation.json');
  simData = await resp.json();
  window.__simData = simData;

  // Populate day dropdown
  for (let i = 0; i < simData.days.length; i++) {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `Tag ${simData.days[i].day}`;
    daySelect.appendChild(opt);
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

  // Listen for agent clicks from Phaser — scroll to that agent card
  window.addEventListener('viewer:agent-click', (e) => {
    const card = document.getElementById(`agent-card-${e.detail.agentKey}`);
    if (card) card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  });

  populateScenes();
  selectScene();

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

  // Render all agent cards (participants first, then dimmed non-participants)
  renderAgentCards(scene);

  // Dispatch scene change to Phaser
  window.dispatchEvent(new CustomEvent('viewer:scene-change', {
    detail: { dayIndex: currentDayIdx, sceneIndex: currentSceneIdx },
  }));
}

function getCurrentScene() {
  if (!simData) return null;
  return simData.days[currentDayIdx]?.scenes[currentSceneIdx] || null;
}

function renderAgentCards(scene) {
  const participants = scene.participants;
  const allAgents = Object.keys(AGENT_META);
  // Participants first, then non-participants
  const ordered = [
    ...participants.filter(k => AGENT_META[k]),
    ...allAgents.filter(k => !participants.includes(k)),
  ];

  let html = '';
  for (const key of ordered) {
    const meta = AGENT_META[key];
    const isActive = participants.includes(key);
    const details = scene.agent_details?.[key];
    const mems = scene.memories?.[key];

    html += `<div class="agent-card${isActive ? '' : ' dimmed'}" id="agent-card-${key}">`;
    html += `<div class="agent-card-header">`;
    html += `<span class="agent-name">${meta.name}</span>`;
    html += `<span class="agent-role">${meta.role}</span>`;
    html += `</div>`;

    if (isActive && details) {
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
        html += `<div class="agent-influences">Einflüsse: ${details.influences.map(i => `<span>${i}</span>`).join(', ')}</div>`;
      }
    }

    if (isActive && mems?.length) {
      html += `<div class="memories-title">Erinnerungen</div>`;
      for (const m of mems) {
        html += `<div class="memory-item">`;
        html += `<span class="mem-type">${m.type}</span>`;
        html += `<span class="mem-importance">${m.importance}/10</span>`;
        html += m.description;
        html += `</div>`;
      }
    }

    html += `</div>`;
  }

  agentList.innerHTML = html;
}
