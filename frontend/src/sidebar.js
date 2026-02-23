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

// Autoplay state
let autoplayTimer = null;
const AUTOPLAY_INTERVAL = 4000; // ms between scenes

// DOM refs
const daySelect = document.getElementById('day-select');
const sceneSelect = document.getElementById('scene-select');
const sceneBadge = document.getElementById('scene-badge');
const sceneTime = document.getElementById('scene-time');
const sceneLocation = document.getElementById('scene-location');
const sceneParticipants = document.getElementById('scene-participants');
const sceneSummary = document.getElementById('scene-summary');
const keyMoment = document.getElementById('key-moment');
const artifactList = document.getElementById('artifact-list');
const agentList = document.getElementById('agent-list');
const btnPrev = document.getElementById('btn-prev');
const btnNext = document.getElementById('btn-next');
const btnPlay = document.getElementById('btn-play');

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

  // Autoplay button
  btnPlay.addEventListener('click', toggleAutoplay);

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

function toggleAutoplay() {
  if (autoplayTimer) {
    // Stop
    clearInterval(autoplayTimer);
    autoplayTimer = null;
    btnPlay.textContent = '\u25B6'; // ▶
    btnPlay.title = 'Autoplay';
    btnPlay.classList.remove('playing');
  } else {
    // Start
    btnPlay.textContent = '\u2016'; // ‖ (pause)
    btnPlay.title = 'Pause';
    btnPlay.classList.add('playing');
    autoplayTimer = setInterval(() => {
      const day = simData.days[currentDayIdx];
      const isLast = currentDayIdx === simData.days.length - 1 &&
        currentSceneIdx === day.scenes.length - 1;
      if (isLast) {
        toggleAutoplay(); // stop at end
        return;
      }
      navigate(1);
    }, AUTOPLAY_INTERVAL);
  }
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

  // Render artifacts
  renderArtifacts(scene.artifacts || []);

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
    }

    html += `</div>`;
  }

  agentList.innerHTML = html;
}
