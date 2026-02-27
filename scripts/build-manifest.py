#!/usr/bin/env python3
"""Generate data/index.json manifest from sim-*.json files."""

import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "frontend" / "public" / "data"


def main():
    sims = []
    for f in sorted(DATA_DIR.glob("sim-*.json")):
        data = json.loads(f.read_text())
        sim_id = f.stem  # e.g. "sim-2-test"
        label = sim_id.replace("-", " ").title()
        days = len(data.get("days", []))
        sims.append({
            "id": sim_id,
            "label": label,
            "file": f.name,
            "days": days,
        })

    if not sims:
        print("No sim-*.json files found in", DATA_DIR, file=sys.stderr)
        sys.exit(1)

    # Default to the last (most recent) simulation
    manifest = {"simulations": sims, "default": sims[-1]["id"]}
    out = DATA_DIR / "index.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"Manifest: {len(sims)} simulations → {out}")


if __name__ == "__main__":
    main()
