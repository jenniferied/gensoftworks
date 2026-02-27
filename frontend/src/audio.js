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

const FADE_MS = 600;

function randomInterval() {
  return 2000 + Math.random() * 6000; // 2-8s
}

function fadeIn(audio, target, ms) {
  audio.volume = 0;
  audio.play().catch(() => {});
  const steps = 20;
  const step = target / steps;
  const dt = ms / steps;
  let i = 0;
  const id = setInterval(() => {
    i++;
    audio.volume = Math.min(step * i, target);
    if (i >= steps) clearInterval(id);
  }, dt);
}

function fadeOut(audio, ms) {
  const start = audio.volume;
  const steps = 20;
  const step = start / steps;
  const dt = ms / steps;
  let i = 0;
  const id = setInterval(() => {
    i++;
    audio.volume = Math.max(start - step * i, 0);
    if (i >= steps) { clearInterval(id); audio.pause(); }
  }, dt);
}

function playRandomTyping() {
  if (muted || !started || typingSounds.length === 0) return;
  const sound = typingSounds[Math.floor(Math.random() * typingSounds.length)];
  const clone = sound.cloneNode();
  const targetVol = Math.min(volume * 3.5, 1.0);
  fadeIn(clone, targetVol, FADE_MS);
  // Fade out before clip ends
  const dur = sound.duration || 8;
  setTimeout(() => fadeOut(clone, FADE_MS), Math.max((dur - 0.8) * 1000, 1000));
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
