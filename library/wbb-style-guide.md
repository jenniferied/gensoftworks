# WBB Visual Style Guide

Visual direction for all Worldbuilding Bible illustrations.

## Core Aesthetic

**Skyrim meets Kingdom Come: Deliverance meets The Witcher.**

- Late medieval (~1300 CE), Central/Northern European
- Dark fantasy grounded in historical realism
- No high fantasy: no glowing runes, no elven filigree, no anime
- Grim, weathered, lived-in — nothing pristine or clean
- Desaturated palette with selective warm accents (firelight, forge glow)

## Color Palettes by Region

| Region | Primary | Secondary | Accent |
|--------|---------|-----------|--------|
| Kronmark | Muted golds, warm browns | Stone greys, faded ochre | Deep burgundy |
| Grenzwald | Deep forest greens, blacks | Grey mist, moss green | Cold blue-white |
| Moorlande | Slate greys, blue-greys | Peat brown, sickly green | Will-o'-wisp blue-green |
| Hochfeste | Ice blue, granite grey | Snow white, dark stone | Warm amber (interior) |
| Handelsaue | Warm ochre, soft greens | River blue, timber brown | Market-stall colors |

## Lighting Rules

- **Exteriors:** Overcast sky, volumetric fog, diffused light. No direct sunlight unless specifically needed.
- **Interiors:** Candlelight, torchlight, forge glow. Warm pools of light in dark spaces.
- **Horror scenes:** Cold moonlight, deep shadows, bioluminescence.
- **Market/trade scenes:** Slightly warmer, more ambient light. Still overcast.

## Character Direction

- **Pose:** Standing upright, front-facing, neutral to dignified pose
- **Background:** Clean white or contextual (forge, forest, etc.)
- **Expression:** Composed, serious — not action poses, not smiling
- **Anatomy:** Realistic proportions, no exaggerated musculature
- **Clothing:** Historically plausible fabrics and construction
- **Skin:** Weathered, scarred, sun-damaged where appropriate — not smooth

## Anti-Patterns (Always Avoid)

- Anime/manga influence (Seedream tendency — use negative prompt)
- High fantasy glow, magic particles, ethereal effects
- Clean/pristine surfaces — everything should show age and use
- Modern fabrics or construction (no zippers, no machine stitching)
- Oversized weapons or armor (keep proportions realistic)
- Text or watermarks in the image
- Overly dramatic poses or action shots (prefer stillness and dignity)
- Fantasy races (no elves, dwarves, orcs — all subjects are human or folklore creatures)

## Model-Specific Keywords

### Seedream 4.5 (Explore)

Works well: "dark fantasy", "medieval", "gritty", "weathered", "Skyrim-inspired"
Negative prompt: "anime, cartoon, manga, cel-shading, bright colors, clean, pristine, glowing, fantasy magic, text, watermark"

### Flux 2 Pro (Explore)

Works well: Camera settings ("f/2.8", "85mm lens"), hex color references, natural language
Avoid: Structured JSON API (degrades quality)

### Nano Banana Pro (Refine)

Works well: Conversational tone, "Imagine a...", ending with ground rules
Avoid: Over-specification, technical jargon

### GPT Image 1.5 (Final)

Works well: Layered reasoning (Background → Subject → Details → Constraints), explaining "why"
Example: "Both figures must be standing ON the bridge, not in the water, because the bridge is the focal point"
