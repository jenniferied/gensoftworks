/**
 * Audio module — lo-fi background music + typing sounds.
 * Audio bar with play/pause, volume slider, CC attribution.
 * Respects browser autoplay policy via first-click gate.
 */

const BASE = import.meta.env.BASE_URL;
let bgMusic = null;
let typingSounds = [];
let typingTimer = null;
let muted = false;
let started = false;
let volume = 0.15;

function randomInterval() {
  return 4000 + Math.random() * 10000; // 4-14s
}

function playRandomTyping() {
  if (muted || !started || typingSounds.length === 0) return;
  const sound = typingSounds[Math.floor(Math.random() * typingSounds.length)];
  const clone = sound.cloneNode();
  clone.volume = Math.min(volume * 2, 1.0);
  clone.play().catch(() => {});
  typingTimer = setTimeout(playRandomTyping, randomInterval());
}

function startAudio() {
  if (started) return;
  started = true;

  bgMusic = new Audio(`${BASE}audio/lofi-ambient.mp3`);
  bgMusic.loop = true;
  bgMusic.volume = volume;
  bgMusic.play().catch(() => {});

  // Preload typing sounds
  for (let i = 1; i <= 3; i++) {
    const a = new Audio(`${BASE}audio/typing-0${i}.mp3`);
    a.preload = 'auto';
    typingSounds.push(a);
  }

  typingTimer = setTimeout(playRandomTyping, randomInterval());
  updateToggleState();
}

function updateToggleState() {
  const btn = document.getElementById('btn-audio-toggle');
  if (!btn) return;
  if (muted) {
    btn.classList.remove('active');
    btn.textContent = '\u266B'; // ♫ (muted indicator)
  } else {
    btn.classList.add('active');
    btn.textContent = '\u266A'; // ♪
  }
}

function toggleAudio() {
  muted = !muted;
  if (muted) {
    if (bgMusic) bgMusic.pause();
    if (typingTimer) clearTimeout(typingTimer);
  } else {
    if (!started) startAudio();
    if (bgMusic) { bgMusic.volume = volume; bgMusic.play().catch(() => {}); }
    typingTimer = setTimeout(playRandomTyping, randomInterval());
  }
  updateToggleState();
}

function setVolume(val) {
  volume = val;
  if (bgMusic) bgMusic.volume = volume;
}

export function initAudio() {
  const btn = document.getElementById('btn-audio-toggle');
  const slider = document.getElementById('audio-volume');

  if (btn) btn.addEventListener('click', toggleAudio);
  if (slider) {
    slider.addEventListener('input', () => {
      const val = parseInt(slider.value) / 100;
      setVolume(val);
      if (val === 0 && !muted) toggleAudio();
      if (val > 0 && muted) toggleAudio();
    });
  }

  // First-click gate: start audio on any user interaction
  const gate = () => {
    if (!started && !muted) startAudio();
    document.removeEventListener('click', gate);
    document.removeEventListener('keydown', gate);
  };
  document.addEventListener('click', gate);
  document.addEventListener('keydown', gate);
}
