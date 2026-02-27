#!/usr/bin/env python3
"""Repair ASCII-encoded umlauts (ae→ä, oe→ö, ue→ü) in simulation data.

Processes logbook JSONs, trace MDs, agent memories, and gallery files.
Uses a word-boundary-aware approach with an exception list for words
where the digraph is NOT an umlaut (e.g. Abenteuer, Quest, Feuer).

Usage:
    python scripts/repair-umlauts.py --sim-dir simulation-2-test [--dry-run]
"""
import argparse
import json
import re
import sys
from pathlib import Path

# ── Exception fragments ──────────────────────────────────────────────
# Words/substrings where "ue" is NOT ü, "ae" is NOT ä, "oe" is NOT ö.
# Checked case-insensitively. Order doesn't matter.

# "ue" exceptions — the digraph is a genuine "u·e" boundary
UE_EXCEPTIONS = [
    # German words where u+e is not ü
    "abenteuer", "feuer", "steuer", "heuer", "ungeheuer", "geheuer",
    "teuer", "euer", "treue", "reue",
    "neue", "neuem", "neuen", "neuer", "neues", "neuest", "erneuer",
    "baue", "bauen", "erbaue", "aufbaue", "einbaue", "ausbaue", "umbaue",
    "anbaue", "abbaue", "vorbeibaue", "aufzubaue", "nachbaue",
    "schaue", "schauen", "hinschaue", "anschaue", "zuschaue", "vorausschaue",
    "braue", "brauen",
    "traue", "trauen", "vertraue", "misstraue", "zutraue",
    "freue", "freuen",
    "daue", "dauern", "dauert", "dauerhaft", "dauerbrenner",
    "statue", "statuen",
    "mauer", "mauern", "mauerwerk", "zugemauert",
    "lauer", "lauert",
    "trauer", "trauert", "trauern",
    "schauer", "graue", "grauen", "grauer",
    "rauer", "fraue", "frauen",
    "blaue", "blauen", "blauer", "blaues",
    "genaue", "genauem", "genauer", "genaues",
    "ungenaue",
    # English / loan words
    "quest", "blue", "blueprint", "dialogue", "rogue", "virtue",
    "silhouette", "masquerade", "unique", "issue", "issues",
    "sequel", "sequence", "sequenz", "sequentiell", "sequenziell",
    "sequencer", "consequence", "konsequen", "eloquen",
    "cue", "cues", "queue", "rescue", "residue", "revenue",
    "mcqueen", "sue", "true", "untrue",
    "eventuell", "individuell", "intellektuell", "kontextuell",
    "konzeptuell", "manuell", "punktuell", "rituell", "textuell",
    "virtuell", "aktuell", "graduell", "prozeduer",
    "duell", "fuel", "bequem",
    # Compound fragments that should NOT be converted
    "questbog", "questfort", "questgeb", "questline", "questlog",
    "questmark", "questreihe", "queststraeng", "queststrang",
    "queststruktur", "questtext", "questveraend", "questverlaeu",
    "questverweis", "questziel", "questzustaend", "questmoeg",
    "hauptquest", "nebenquest", "seitenquest", "heilquest",
    "charakterquest", "fraktionsquest", "staedtequest",
    "questlinien",
    # "quelle/quellen/quer" — these contain "ue" but it IS ü → keep them
    # WAIT: "Quelle" = Qülle? No! Quelle has real ue. Add to exceptions.
    "quelle", "quellen", "quellenlage", "quelldokument",
    "primaerquelle", "kanonquelle", "infektionsquelle",
    "lichtquelle", "steigerungsquelle", "marktluecke",
    "hauptquelle",
    "quer", "querlesen", "quergelesen", "querzulesen",
    "querschnitt", "querverbind", "querverweis",
]

# "ae" exceptions
AE_EXCEPTIONS = [
    "aero", "israel", "michael",
    "rafael",
]

# "oe" exceptions
OE_EXCEPTIONS = [
    "poem", "poet", "poesie", "poetisch",
    "koexist", "coefficient",
    "phoenix", "aloe", "shoe", "joe", "canoe", "oboe", "toe",
    "goes", "does", "foe",
]

def _build_exception_set(raw):
    """Lowercase all exception fragments."""
    return {w.lower() for w in raw}

UE_EXC = _build_exception_set(UE_EXCEPTIONS)
AE_EXC = _build_exception_set(AE_EXCEPTIONS)
OE_EXC = _build_exception_set(OE_EXCEPTIONS)


def _word_contains_exception(word_lower, digraph, exc_set):
    """Check if any exception fragment appears in the word."""
    for exc in exc_set:
        if exc in word_lower:
            return True
    return False


def replace_umlauts_in_word(word):
    """Replace ae→ä, oe→ö, ue→ü in a single word, respecting exceptions."""
    wl = word.lower()

    # ue → ü
    if "ue" in wl and not _word_contains_exception(wl, "ue", UE_EXC):
        word = _replace_digraph(word, "ue", "ü")
        word = _replace_digraph(word, "Ue", "Ü")

    # ae → ä
    wl = word.lower()
    if "ae" in wl and not _word_contains_exception(wl, "ae", AE_EXC):
        word = _replace_digraph(word, "ae", "ä")
        word = _replace_digraph(word, "Ae", "Ä")

    # oe → ö
    wl = word.lower()
    if "oe" in wl and not _word_contains_exception(wl, "oe", OE_EXC):
        word = _replace_digraph(word, "oe", "ö")
        word = _replace_digraph(word, "Oe", "Ö")

    return word


def _replace_digraph(word, digraph, replacement):
    """Replace a digraph preserving case of the first letter."""
    result = []
    i = 0
    dg_lower = digraph.lower()
    while i < len(word):
        if i + 1 < len(word) and word[i:i+2].lower() == dg_lower:
            if word[i].isupper() and digraph[0].isupper():
                result.append(replacement.upper())
            elif word[i].isupper():
                result.append(replacement.upper())
            else:
                result.append(replacement)
            i += 2
        else:
            result.append(word[i])
            i += 1
    return "".join(result)


# Word boundary regex: sequences of word-like chars (including umlauts already present)
WORD_RE = re.compile(r'([A-Za-zÄÖÜäöüß]+)')


def repair_text(text):
    """Repair all umlauts in a text string."""
    def replacer(match):
        return replace_umlauts_in_word(match.group(0))
    return WORD_RE.sub(replacer, text)


def repair_json_value(obj):
    """Recursively repair umlauts in JSON string values only (not keys, not bools)."""
    if isinstance(obj, str):
        return repair_text(obj)
    elif isinstance(obj, list):
        return [repair_json_value(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: repair_json_value(v) for k, v in obj.items()}
    else:
        return obj


def repair_json_file(path, dry_run=False):
    """Repair umlauts in JSON string values, preserving keys and structure."""
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    try:
        data = json.loads(original)
    except json.JSONDecodeError:
        print(f"  WARNING: Cannot parse {path}, skipping", file=sys.stderr)
        return False

    repaired_data = repair_json_value(data)
    repaired = json.dumps(repaired_data, ensure_ascii=False, indent=2) + "\n"

    if original == repaired:
        return False

    if dry_run:
        return True

    with open(path, "w", encoding="utf-8") as f:
        f.write(repaired)
    return True


def repair_text_file(path, dry_run=False):
    """Repair umlauts in a markdown/text file."""
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    repaired = repair_text(original)

    if original == repaired:
        return False

    if dry_run:
        return True

    with open(path, "w", encoding="utf-8") as f:
        f.write(repaired)
    return True


def main():
    parser = argparse.ArgumentParser(description="Repair ASCII umlauts in simulation data")
    parser.add_argument("--sim-dir", required=True, help="Simulation directory (e.g. simulation-2-test)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without writing")
    args = parser.parse_args()

    sim = Path(args.sim_dir)
    if not sim.exists():
        print(f"Error: {sim} not found", file=sys.stderr)
        sys.exit(1)

    changed = 0
    total = 0

    # 1. Logbook JSONs
    for p in sorted(sim.glob("logbook/*.json")):
        total += 1
        if repair_json_file(p, args.dry_run):
            changed += 1
            print(f"  {'[DRY] ' if args.dry_run else ''}Repaired: {p}")

    # 2. Trace files (markdown)
    for p in sorted(sim.glob("traces/**/*.md")):
        total += 1
        if repair_text_file(p, args.dry_run):
            changed += 1
            print(f"  {'[DRY] ' if args.dry_run else ''}Repaired: {p}")

    # 3. Agent memory files
    for p in sorted(sim.glob("agents/*.md")):
        total += 1
        if repair_text_file(p, args.dry_run):
            changed += 1
            print(f"  {'[DRY] ' if args.dry_run else ''}Repaired: {p}")

    # 4. Gallery markdown files
    for p in sorted(sim.glob("gallery/**/*.md")):
        total += 1
        if repair_text_file(p, args.dry_run):
            changed += 1
            print(f"  {'[DRY] ' if args.dry_run else ''}Repaired: {p}")

    # 5. Briefing
    briefing = sim / "briefing.md"
    if briefing.exists():
        total += 1
        if repair_text_file(briefing, args.dry_run):
            changed += 1
            print(f"  {'[DRY] ' if args.dry_run else ''}Repaired: {briefing}")

    # 6. State files
    for p in sorted(sim.glob("state/*.json")):
        total += 1
        if repair_json_file(p, args.dry_run):
            changed += 1
            print(f"  {'[DRY] ' if args.dry_run else ''}Repaired: {p}")

    action = "Would repair" if args.dry_run else "Repaired"
    print(f"\n{action} {changed}/{total} files.")


if __name__ == "__main__":
    main()
