#!/usr/bin/env python3
"""
GenAI Image Pipeline — fal.ai batch image generation.

Generates images from text prompts using multiple models via fal.ai.
Supports text-to-image and image-to-image (edit) workflows.

Dependencies: fal-client, httpx, Pillow (pip install fal-client httpx Pillow)
Auth: Set FAL_KEY in .env.local at the repo root.
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime

# Load .env.local from repo root (no python-dotenv needed)
env_path = Path(__file__).parent.parent / ".env.local"
if env_path.exists():
    for line in env_path.read_text().strip().split("\n"):
        if "=" in line and not line.startswith("#"):
            key, val = line.split("=", 1)
            os.environ[key.strip()] = val.strip()

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = Path(__file__).parent.parent / "simulation-2" / "gallery" / "concepts"
RESULTS_FILE = OUTPUT_DIR / "results.json"
INPUTS_DIR = SCRIPT_DIR / "inputs"

# Allow external repos to redirect outputs via --output-dir
_custom_output_dir = None

# ---------------------------------------------------------------------------
# Model configs — add/remove models without code changes.
# For image-to-image (edit) models, set "mode": "edit" and provide image_key.
# ---------------------------------------------------------------------------
MODELS = [
    {
        "name": "flux-2-pro",
        "endpoint": "fal-ai/flux-2-pro",
        "cost": "$0.03",
        "mode": "text2img",
        "prompt_style": "hex-colors camera-settings",
        "extra_args": {"image_size": "landscape_16_9"},
    },
    {
        "name": "seedream-4-5",
        "endpoint": "fal-ai/bytedance/seedream/v4.5/text-to-image",
        "cost": "$0.04",
        "mode": "text2img",
        "prompt_style": "structured-4k",
        "extra_args": {"image_size": "landscape_16_9"},
    },
    {
        "name": "nano-banana-pro",
        "endpoint": "fal-ai/nano-banana-pro",
        "cost": "$0.15",
        "mode": "text2img",
        "prompt_style": "conversational",
        "extra_args": {},
        "aspect_ratio_key": "aspect_ratio",  # uses "16:9" format, not image_size
    },
    {
        "name": "nano-banana-2",
        "endpoint": "fal-ai/nano-banana-2",
        "cost": "$0.08",
        "mode": "text2img",
        "prompt_style": "conversational",
        "extra_args": {},
        "aspect_ratio_key": "aspect_ratio",
    },
    {
        "name": "gpt-image-1-5",
        "endpoint": "fal-ai/gpt-image-1.5",
        "cost": "$0.20",
        "mode": "text2img",
        "prompt_style": "layered-reasoning",
        "extra_args": {"size": "1536x1024", "quality": "high"},
    },
    # --- Image-to-image (edit) models ---
    # {
    #     "name": "gpt-image-1-5-edit",
    #     "endpoint": "fal-ai/gpt-image-1.5/edit",
    #     "cost": "$0.08",
    #     "mode": "edit",
    #     "image_key": "image_urls",  # expects list
    #     "prompt_style": "layered-reasoning",
    #     "extra_args": {"quality": "high", "size": "auto"},
    # },
    # {
    #     "name": "nano-banana-pro-edit",
    #     "endpoint": "fal-ai/nano-banana-pro/edit",
    #     "cost": "$0.15",
    #     "mode": "edit",
    #     "image_key": "image_urls",
    #     "prompt_style": "conversational",
    #     "extra_args": {"aspect_ratio": "16:9"},
    # },
]

# ---------------------------------------------------------------------------
# Scenes — empty; use --scenes-file for Vera's concept art pipeline.
# ---------------------------------------------------------------------------
SCENES = []

# ---------------------------------------------------------------------------
# Core utilities — battle-tested patterns from everything-machine pipeline
# ---------------------------------------------------------------------------
results = []
uploaded_urls = {}  # cache: path -> URL (upload once, reuse)


def load_existing_results():
    """Load previous results for resumable runs."""
    global results
    if RESULTS_FILE.exists():
        results = json.loads(RESULTS_FILE.read_text())
        print(f"  Loaded {len(results)} existing results")


def already_done(tag: str) -> bool:
    """Check if this model+scene combo already succeeded."""
    return any(r["test"] == tag and not r.get("error") for r in results)


def _ensure_deps():
    """Lazy-import fal_client and httpx (not needed for --dry-run)."""
    global fal_client, httpx
    import fal_client as _fal
    import httpx as _httpx
    fal_client = _fal
    httpx = _httpx


def upload(path: Path) -> str:
    """Upload image to fal.ai with caching (same file uploaded once)."""
    key = str(path)
    if key not in uploaded_urls:
        print(f"  Uploading {path.name}...")
        uploaded_urls[key] = fal_client.upload_file(str(path))
        print(f"  -> {uploaded_urls[key]}")
    return uploaded_urls[key]


def save_image(url: str, model_name: str, scene_name: str,
               category: str = None, run_name: str = None,
               prompt: str = None, negative_prompt: str = None) -> Path:
    """Download result image with dimension verification and metadata embedding.

    Output structure:
      With category:  outputs/{run_name}/{category}/{scene_name}_{model}.ext
      Without:        outputs/{run_name}/{model}/{scene_name}.ext

    Metadata written into the image:
      PNG: tEXt chunks (prompt, negative_prompt, model)
      JPEG: EXIF UserComment (JSON with prompt, model)
    """
    from PIL import Image
    if category:
        out_dir = OUTPUT_DIR / run_name / category if run_name else OUTPUT_DIR / category
        filename = f"{scene_name}_{model_name}"
    else:
        out_dir = OUTPUT_DIR / run_name / model_name if run_name else OUTPUT_DIR / model_name
        filename = scene_name
    out_dir.mkdir(parents=True, exist_ok=True)
    ext = ".jpg" if (".jpg" in url or "jpeg" in url) else ".png"
    out_path = out_dir / f"{filename}{ext}"
    resp = httpx.get(url, timeout=60)
    out_path.write_bytes(resp.content)

    # Embed metadata into the saved image
    try:
        img = Image.open(out_path)
        if ext == ".png":
            from PIL.PngImagePlugin import PngInfo
            meta = PngInfo()
            meta.add_text("model", model_name)
            if prompt:
                meta.add_text("prompt", prompt)
            img.save(out_path, pnginfo=meta)
        else:
            # JPEG: write metadata as JSON in EXIF UserComment
            import piexif
            exif_dict = piexif.load(img.info.get("exif", b"")) if img.info.get("exif") else {"0th": {}, "Exif": {}}
            comment = json.dumps({"model": model_name, "prompt": prompt or ""}, ensure_ascii=False)
            exif_dict["Exif"][piexif.ExifIFD.UserComment] = b"UTF-8\x00\x00\x00" + comment.encode("utf-8")
            img.save(out_path, exif=piexif.dump(exif_dict))
    except Exception as e:
        print(f"    WARNING: Could not embed metadata: {e}")

    size_kb = out_path.stat().st_size // 1024
    print(f"    Saved: {out_path.name} ({size_kb}KB)")
    return out_path


def log(test, model, prompt, elapsed, cost, urls, error=None,
        scene_meta=None, api_args=None, dimensions=None):
    """Append result and write incrementally (no data loss on crash)."""
    entry = {
        "test": test, "model": model, "prompt": prompt,
        "elapsed_s": round(elapsed, 1), "cost_est": cost,
        "images": urls, "error": error, "timestamp": datetime.now().isoformat(),
    }
    if scene_meta:
        entry["category"] = scene_meta.get("category", "")
        entry["tier"] = scene_meta.get("tier", "")
        entry["aspect_ratio"] = scene_meta.get("aspect_ratio", "")
        entry["name_de"] = scene_meta.get("name_de", "")
    if api_args:
        # Save the actual API args sent (minus the prompt, which is already logged)
        entry["api_args"] = {k: v for k, v in api_args.items() if k != "prompt"}
    if dimensions:
        entry["dimensions"] = dimensions
    results.append(entry)
    RESULTS_FILE.write_text(json.dumps(results, indent=2, ensure_ascii=False))


def on_queue(update):
    """Progress callback for fal.ai queue."""
    if isinstance(update, fal_client.InProgress):
        for entry in update.logs:
            print(f"      [{entry.get('message', '')}]")


def extract_image_urls(result: dict) -> list[str]:
    """Extract image URLs from various response formats."""
    # Most models: result["images"][*]["url"]
    if "images" in result:
        return [img["url"] for img in result["images"] if isinstance(img, dict) and "url" in img]
    # Some models: result["output"]["url"]
    if "output" in result and isinstance(result["output"], dict):
        url = result["output"].get("url", "")
        return [url] if url else []
    # Fallback: result["data"][*]["url"]
    if "data" in result and isinstance(result["data"], list):
        return [d["url"] for d in result["data"] if isinstance(d, dict) and "url" in d]
    return []


# ---------------------------------------------------------------------------
# Run logic
# ---------------------------------------------------------------------------
def run_model(model_cfg: dict, scene: dict, input_image_url: str = None,
              run_name: str = None):
    """Run a single model x scene combination."""
    name = model_cfg["name"]
    tag = f"{name}_{scene['name']}"

    if already_done(tag):
        print(f"\n  {name} x {scene['name']} | SKIP (already done)")
        return

    print(f"\n  {name} x {scene['name']} | {model_cfg['endpoint']}")

    args = {"prompt": scene["prompt"]}
    args.update(model_cfg.get("extra_args", {}))

    # Per-scene aspect ratio override (from wbb-scenes.json)
    if "aspect_ratio" in scene:
        ar = scene["aspect_ratio"]
        if name == "gpt-image-1-5":
            # GPT uses "size" param with pixel dimensions
            size_map = {
                "landscape_16_9": "1536x1024",
                "square": "1024x1024",
                "portrait_9_16": "1024x1536",
            }
            args["size"] = size_map.get(ar, "1536x1024")
        elif model_cfg.get("aspect_ratio_key"):
            # Models like Nano use "aspect_ratio" with "16:9" format
            ar_map = {
                "landscape_16_9": "16:9",
                "square": "1:1",
                "portrait_9_16": "9:16",
                "landscape_4_3": "4:3",
                "portrait_3_4": "3:4",
            }
            args[model_cfg["aspect_ratio_key"]] = ar_map.get(ar, "1:1")
        else:
            args["image_size"] = ar

    # Per-scene negative prompt (from wbb-scenes.json)
    if scene.get("negative_prompt"):
        args["negative_prompt"] = scene["negative_prompt"]

    # For edit models, inject the input image
    if model_cfg.get("mode") == "edit" and input_image_url:
        image_key = model_cfg.get("image_key", "image_url")
        if image_key == "image_urls":
            args[image_key] = [input_image_url]
        else:
            args[image_key] = input_image_url

    category = scene.get("category")

    t0 = time.time()
    try:
        result = fal_client.subscribe(
            model_cfg["endpoint"], arguments=args,
            with_logs=True, on_queue_update=on_queue,
        )
        elapsed = time.time() - t0
        urls = extract_image_urls(result)
        if urls:
            dims = None
            for url in urls:
                out_path = save_image(
                    url, name, scene["name"],
                    category=category, run_name=run_name,
                    prompt=scene["prompt"],
                    negative_prompt=args.get("negative_prompt"),
                )
                from PIL import Image
                img = Image.open(out_path)
                dims = f"{img.size[0]}x{img.size[1]}"
            log(tag, model_cfg["endpoint"], scene["prompt"], elapsed,
                model_cfg["cost"], urls, scene_meta=scene, api_args=args,
                dimensions=dims)
            print(f"    OK in {elapsed:.1f}s")
        else:
            print(f"    WARNING: No image URL found. Keys: {list(result.keys())}")
            log(tag, model_cfg["endpoint"], scene["prompt"], elapsed,
                model_cfg["cost"], [], f"No image URL in response: {list(result.keys())}",
                scene_meta=scene, api_args=args)
    except Exception as e:
        elapsed = time.time() - t0
        print(f"    ERROR ({elapsed:.1f}s): {e}")
        log(tag, model_cfg["endpoint"], scene["prompt"], elapsed,
            model_cfg["cost"], [], str(e), scene_meta=scene, api_args=args)


def parse_args():
    """Parse CLI arguments (manual parsing to stay dependency-free)."""
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    scenes_file = None
    category = None
    tier = None
    run_name = None
    output_dir = None
    only_models = []

    i = 0
    while i < len(args):
        if args[i] == "--scenes-file" and i + 1 < len(args):
            scenes_file = args[i + 1]
            i += 2
        elif args[i] == "--category" and i + 1 < len(args):
            category = args[i + 1]
            i += 2
        elif args[i] == "--tier" and i + 1 < len(args):
            tier = int(args[i + 1])
            i += 2
        elif args[i] == "--run-name" and i + 1 < len(args):
            run_name = args[i + 1]
            i += 2
        elif args[i] == "--output-dir" and i + 1 < len(args):
            output_dir = args[i + 1]
            i += 2
        elif args[i] == "--dry-run":
            i += 1
        elif not args[i].startswith("--"):
            only_models.append(args[i])
            i += 1
        else:
            i += 1

    return dry_run, scenes_file, category, tier, run_name, output_dir, only_models


def load_scenes_from_file(scenes_file: str, model_filter: list,
                          category: str = None, tier: int = None) -> tuple:
    """Load scenes from JSON file with filtering. Returns (scenes, models_used)."""
    path = Path(scenes_file)
    if not path.is_absolute():
        path = SCRIPT_DIR / path
    if not path.exists():
        print(f"ERROR: Scenes file not found: {path}")
        sys.exit(1)

    all_scenes = json.loads(path.read_text())

    # Filter by model(s)
    if model_filter:
        all_scenes = [s for s in all_scenes if s.get("model") in model_filter]

    # Filter by category
    if category:
        all_scenes = [s for s in all_scenes if s.get("category") == category]

    # Filter by tier
    if tier:
        all_scenes = [s for s in all_scenes if s.get("tier", 3) <= tier]

    # Group scenes by model, find matching MODELS config
    models_used = {}
    for scene in all_scenes:
        model_name = scene.get("model")
        if model_name and model_name not in models_used:
            cfg = next((m for m in MODELS if m["name"] == model_name), None)
            if cfg:
                models_used[model_name] = cfg

    return all_scenes, models_used


def main():
    global RESULTS_FILE, OUTPUT_DIR
    dry_run, scenes_file, category, tier, run_name, output_dir, only_models = parse_args()

    # Redirect outputs to external directory (e.g. gensoftworks gallery)
    if output_dir:
        OUTPUT_DIR = Path(output_dir)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Use run-specific results file if --run-name is set
    if run_name:
        if output_dir:
            RESULTS_FILE = OUTPUT_DIR / f"results-{run_name}.json"
        else:
            RESULTS_FILE = SCRIPT_DIR / f"results-{run_name}.json"

    # --- WBB mode: load scenes from JSON file ---
    if scenes_file:
        scenes, models_used = load_scenes_from_file(
            scenes_file, only_models, category, tier
        )
        if not scenes:
            print("ERROR: No scenes match the given filters.")
            print(f"  --scenes-file={scenes_file}")
            if only_models:
                print(f"  models={only_models}")
            if category:
                print(f"  --category={category}")
            if tier:
                print(f"  --tier={tier}")
            return

        print("=" * 60)
        print("GenAI Image Pipeline — WBB Mode")
        if dry_run:
            print("MODE: DRY RUN (no API calls)")
        print(f"Scenes file: {scenes_file}")
        if only_models:
            print(f"Model filter: {', '.join(only_models)}")
        if category:
            print(f"Category: {category}")
        if tier:
            print(f"Max tier: {tier}")
        print(f"{len(scenes)} scenes across {len(models_used)} model(s)")
        print(f"Time: {datetime.now().isoformat()}")
        print("=" * 60)

        if dry_run:
            by_cat = {}
            for scene in scenes:
                cat = scene.get("category", "unknown")
                by_cat[cat] = by_cat.get(cat, 0) + 1
                model_name = scene.get("model", "?")
                cost = models_used.get(model_name, {}).get("cost", "?")
                print(f"  [DRY] {model_name} x {scene['name']} | {cost} | tier {scene.get('tier', '?')}")
            est_cost = sum(
                float(models_used.get(s.get("model"), {}).get("cost", "$0").replace("$", ""))
                for s in scenes
            )
            print(f"\nBy category: {by_cat}")
            print(f"Estimated cost: ${est_cost:.2f}")
            return

        if not os.environ.get("FAL_KEY"):
            print("ERROR: FAL_KEY not set. Add it to .env.local at repo root.")
            return

        _ensure_deps()
        load_existing_results()

        for scene in scenes:
            model_name = scene.get("model")
            model_cfg = models_used.get(model_name)
            if not model_cfg:
                print(f"\n  SKIP {scene['name']} — model '{model_name}' not configured")
                continue
            print(f"\n{'—' * 60}")
            print(f"SCENE: {scene['name']} ({scene.get('category', '?')} / tier {scene.get('tier', '?')})")
            print(f"{'—' * 60}")
            run_model(model_cfg, scene, run_name=run_name)

    # --- Legacy mode: use hardcoded SCENES ---
    else:
        active_models = MODELS
        if only_models:
            active_models = [m for m in MODELS if m["name"] in only_models]
            if not active_models:
                print(f"ERROR: No matching models for {only_models}")
                print(f"Available: {[m['name'] for m in MODELS]}")
                return

        scenes = SCENES
        if not scenes:
            print("No scenes defined. Use --scenes-file to load from JSON.")
            return

        total_runs = len(scenes) * len(active_models)
        print("=" * 60)
        print("GenAI Image Pipeline")
        if dry_run:
            print("MODE: DRY RUN (no API calls)")
        if only_models:
            print(f"FILTER: {', '.join(only_models)}")
        print(f"{len(scenes)} scenes x {len(active_models)} models = {total_runs} images")
        print(f"Time: {datetime.now().isoformat()}")
        print("=" * 60)

        if dry_run:
            for scene in scenes:
                for model in active_models:
                    print(f"  [DRY] {model['name']} x {scene['name']} | {model['cost']}")
            est_cost = sum(
                float(m["cost"].replace("$", ""))
                for m in active_models for _ in scenes
            )
            print(f"\nEstimated cost: ${est_cost:.2f}")
            return

        if not os.environ.get("FAL_KEY"):
            print("ERROR: FAL_KEY not set. Add it to .env.local at repo root.")
            return

        _ensure_deps()
        load_existing_results()

        # Check for edit models needing input images
        edit_models = [m for m in active_models if m.get("mode") == "edit"]
        input_image_url = None
        if edit_models:
            input_files = list(INPUTS_DIR.glob("*.png")) + list(INPUTS_DIR.glob("*.jpg"))
            if input_files:
                input_image_url = upload(input_files[0])
            else:
                print(f"WARNING: Edit models configured but no input images in {INPUTS_DIR}/")

        for scene in scenes:
            print(f"\n{'—' * 60}")
            print(f"SCENE: {scene['name']}")
            print(f"{'—' * 60}")
            for model_cfg in active_models:
                run_model(model_cfg, scene, input_image_url, run_name=run_name)

    # Summary
    print(f"\n{'=' * 60}\nCOMPLETE\n{'=' * 60}")
    total = len(results)
    errors = sum(1 for r in results if r.get("error"))
    print(f"Total: {total}, OK: {total - errors}, Errors: {errors}")
    for r in results:
        s = "FAIL" if r.get("error") else "OK"
        print(f"  [{s}] {r['test']} — {r['elapsed_s']}s — {r['cost_est']}")


if __name__ == "__main__":
    main()
