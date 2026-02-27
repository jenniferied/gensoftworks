#!/usr/bin/env bash
# Build all simulation data and deploy to docs/ for GitHub Pages.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPTS="$REPO_ROOT/scripts"
DATA_DIR="$REPO_ROOT/frontend/public/data"
ARCHIVE="$HOME/Documents/GitHub/gensoftworks-archive/simulation-1/viewer-data/simulation.json"

mkdir -p "$DATA_DIR"

echo "=== Building sim-2-test data ==="
python3 "$SCRIPTS/build-viewer-data.py" --sim-dir simulation-2-test --out "$DATA_DIR/sim-2-test.json"

echo "=== Copying sim-1 from archive ==="
if [ -f "$ARCHIVE" ]; then
  cp "$ARCHIVE" "$DATA_DIR/sim-1.json"
  echo "Copied sim-1.json"
else
  echo "WARNING: sim-1 archive not found at $ARCHIVE — skipping"
fi

echo "=== Building manifest ==="
python3 "$SCRIPTS/build-manifest.py"

echo "=== Vite build ==="
cd "$REPO_ROOT/frontend"
npx vite build

echo "=== Deploying to docs/ ==="
rm -rf "$REPO_ROOT/docs"
cp -r "$REPO_ROOT/frontend/dist" "$REPO_ROOT/docs"

echo "=== Done ==="
echo "Deploy output: $REPO_ROOT/docs/"
echo "Push to main and enable GitHub Pages (Settings → Pages → main branch, /docs folder)"
