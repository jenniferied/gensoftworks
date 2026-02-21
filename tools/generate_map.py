#!/usr/bin/env python3
"""
Generate the Gebäude 7 Obergeschoss tilemap as Tiled JSON.

Map: 44×28 tiles (2112×1344 px) at 48×48 per tile.

Tilesets used:
  - floors: Room_Builder_Floors_48x48.png  (720×1920 → 15 cols × 40 rows)
  - walls:  Room_Builder_Walls_48x48.png   (1536×1920 → 32 cols × 40 rows)

Tile IDs in Tiled JSON are 1-indexed (0 = empty).
  floors GID starts at 1
  walls  GID starts at 601 (15*40 = 600 floor tiles + 1)
"""

import json
import os

# --- Constants ---
MAP_W, MAP_H = 44, 28
TILE = 48

# Tileset dimensions (in tiles)
FLOOR_COLS = 15  # 720/48
FLOOR_ROWS = 40  # 1920/48
WALL_COLS = 32   # 1536/48
WALL_ROWS = 40   # 1920/48

FLOOR_COUNT = FLOOR_COLS * FLOOR_ROWS  # 600
WALL_GID_START = FLOOR_COUNT + 1       # 601


def floor_id(col, row):
    return row * FLOOR_COLS + col + 1


def wall_id(col, row):
    return WALL_GID_START + row * WALL_COLS + col


# --- Seamless floor tiles (verified: edgeDiff=0, no per-tile shadows) ---
WOOD_FLOOR   = floor_id(1, 17)   # warm brown wood planks with grain
HALL_FLOOR   = floor_id(5, 9)    # parquet pattern — RGB(192,168,141)
BATH_FLOOR   = floor_id(9, 27)   # clean grey — RGB(168,174,176)
KITCHEN_FLOOR = floor_id(2, 35)  # herringbone — RGB(153,140,128)

# --- Cream wall tiles (cols 4-7, row 6) ---
W_CREAM   = wall_id(5, 6)   # center fill — RGB(240,235,224)
W_CREAM_L = wall_id(4, 6)   # left edge
W_CREAM_R = wall_id(6, 6)   # right edge
W_CREAM_J = wall_id(7, 6)   # junction
W_ABOVE   = wall_id(5, 8)   # darker, for above-layer


def make_empty():
    return [0] * (MAP_W * MAP_H)


def idx(x, y):
    return y * MAP_W + x


def fill_rect(layer, x1, y1, w, h, tile_id):
    for y in range(y1, y1 + h):
        for x in range(x1, x1 + w):
            if 0 <= x < MAP_W and 0 <= y < MAP_H:
                layer[idx(x, y)] = tile_id


def h_wall(layer, x1, x2, y, tid):
    for x in range(x1, x2 + 1):
        layer[idx(x, y)] = tid


def v_wall(layer, x, y1, y2, tid):
    for y in range(y1, y2 + 1):
        layer[idx(x, y)] = tid


def door(layer, xs, y):
    """Clear wall tiles to create a doorway."""
    for x in xs:
        layer[idx(x, y)] = 0


def generate():
    fl = make_empty()
    wl = make_empty()
    al = make_empty()

    # ========================================
    # FLOORS
    # ========================================
    fill_rect(fl, 0, 0, MAP_W, MAP_H, WOOD_FLOOR)
    fill_rect(fl, 0, 8, MAP_W, 5, HALL_FLOOR)       # hallway
    fill_rect(fl, 34, 0, 10, 8, KITCHEN_FLOOR)       # kitchen
    # Bathrooms side by side: Damen (left), Herren (right)
    fill_rect(fl, 34, 13, 5, 7, BATH_FLOOR)          # WC Damen
    fill_rect(fl, 39, 13, 5, 7, BATH_FLOOR)          # WC Herren

    # ========================================
    # WALLS
    # ========================================

    # --- Outer walls ---
    h_wall(wl, 0, MAP_W - 1, 0, W_CREAM)
    h_wall(wl, 0, MAP_W - 1, MAP_H - 1, W_CREAM)
    v_wall(wl, 0, 0, MAP_H - 1, W_CREAM_L)
    v_wall(wl, MAP_W - 1, 0, MAP_H - 1, W_CREAM_R)
    # Corners
    for cx, cy in [(0, 0), (MAP_W-1, 0), (0, MAP_H-1), (MAP_W-1, MAP_H-1)]:
        wl[idx(cx, cy)] = W_CREAM_J

    # --- Hallway walls ---
    h_wall(wl, 0, MAP_W - 1, 7, W_CREAM)    # north side
    h_wall(wl, 0, MAP_W - 1, 13, W_CREAM)   # south side

    # --- Top room dividers (y=0..7) ---
    for x in [8, 16, 24, 34]:
        v_wall(wl, x, 0, 7, W_CREAM_R)

    # --- Bottom room dividers ---
    # Offices 7d/7e/7f (y=13..19)
    for x in [8, 16]:
        v_wall(wl, x, 13, 19, W_CREAM_R)
    # 7f | Lounge divider
    v_wall(wl, 24, 13, MAP_H - 1, W_CREAM_R)
    # Lounge | Bathrooms divider
    v_wall(wl, 34, 13, 19, W_CREAM_R)

    # Bottom of offices 7d/7e/7f
    h_wall(wl, 0, 23, 19, W_CREAM)

    # --- Bathrooms: side by side ---
    # Vertical wall between WC Damen (x:34-38) and WC Herren (x:39-43)
    v_wall(wl, 39, 13, 19, W_CREAM_R)
    # Bottom of bathrooms
    h_wall(wl, 34, MAP_W - 1, 19, W_CREAM)

    # --- Doorways (2 tiles wide) ---
    # Top rooms → hallway (y=7)
    door(wl, [3, 4], 7)       # 7a
    door(wl, [11, 12], 7)     # 7b
    door(wl, [19, 20], 7)     # 7c
    door(wl, [28, 29], 7)     # Conference
    door(wl, [38, 39], 7)     # Kitchen

    # Bottom rooms → hallway (y=13)
    door(wl, [3, 4], 13)      # 7d
    door(wl, [11, 12], 13)    # 7e
    door(wl, [19, 20], 13)    # 7f
    door(wl, [28, 29], 13)    # Lounge
    door(wl, [36, 37], 13)    # WC Damen (own door)
    door(wl, [41, 42], 13)    # WC Herren (own door)

    # Zimmer 7 door (from 7e area down)
    door(wl, [10, 11], 19)

    # ========================================
    # ABOVE LAYER — wall tops rendered over agents
    # ========================================
    h_wall(al, 0, MAP_W - 1, 0, W_ABOVE)
    h_wall(al, 0, MAP_W - 1, 7, W_ABOVE)
    h_wall(al, 0, MAP_W - 1, 13, W_ABOVE)
    h_wall(al, 0, 23, 19, W_ABOVE)
    h_wall(al, 34, MAP_W - 1, 19, W_ABOVE)

    # Clear doorways on above layer too
    door(al, [3, 4], 7)
    door(al, [11, 12], 7)
    door(al, [19, 20], 7)
    door(al, [28, 29], 7)
    door(al, [38, 39], 7)
    door(al, [3, 4], 13)
    door(al, [11, 12], 13)
    door(al, [19, 20], 13)
    door(al, [28, 29], 13)
    door(al, [36, 37], 13)
    door(al, [41, 42], 13)
    door(al, [10, 11], 19)

    # ========================================
    # Tiled JSON
    # ========================================
    def make_layer(name, lid, data):
        return {
            "data": data, "height": MAP_H, "width": MAP_W,
            "id": lid, "name": name, "opacity": 1,
            "type": "tilelayer", "visible": True, "x": 0, "y": 0,
        }

    tilemap = {
        "compressionlevel": -1,
        "height": MAP_H, "width": MAP_W, "infinite": False,
        "orientation": "orthogonal", "renderorder": "right-down",
        "tilewidth": TILE, "tileheight": TILE,
        "tiledversion": "1.10.2", "type": "map", "version": "1.10",
        "nextlayerid": 4, "nextobjectid": 1,
        "tilesets": [
            {
                "columns": FLOOR_COLS, "firstgid": 1,
                "image": "tilesets/Room_Builder_Floors_48x48.png",
                "imageheight": 1920, "imagewidth": 720,
                "margin": 0, "name": "floors", "spacing": 0,
                "tilecount": FLOOR_COUNT, "tileheight": TILE, "tilewidth": TILE,
            },
            {
                "columns": WALL_COLS, "firstgid": WALL_GID_START,
                "image": "tilesets/Room_Builder_Walls_48x48.png",
                "imageheight": 1920, "imagewidth": 1536,
                "margin": 0, "name": "walls", "spacing": 0,
                "tilecount": WALL_COLS * WALL_ROWS,
                "tileheight": TILE, "tilewidth": TILE,
            },
        ],
        "layers": [
            make_layer("floor", 1, fl),
            make_layer("walls", 2, wl),
            make_layer("above", 3, al),
        ],
    }
    return tilemap


if __name__ == "__main__":
    out_path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "frontend", "public", "assets", "map.json"
    ))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    tilemap = generate()
    with open(out_path, "w") as f:
        json.dump(tilemap, f, indent=2)
    total = sum(1 for l in tilemap["layers"] for t in l["data"] if t != 0)
    print(f"Generated {out_path}")
    print(f"  {MAP_W}×{MAP_H} tiles ({MAP_W*TILE}×{MAP_H*TILE} px)")
    print(f"  {total} non-empty tiles across 3 layers")
