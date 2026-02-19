# Library

> The reference shelf. What the agents consult when they need inspiration or grounding.

## Structure

```
library/
├── papers/      # Academic papers (PDFs from master-thesis literature review)
├── artbooks/    # Art reference books, style guides, visual inspiration
├── gdds/        # Game Design Documents (published or reference GDDs)
└── wbbs/        # Worldbuilding Bibles (reference examples)
```

## How It Gets Used

In the simulation, agents can "visit the library" as a planned action. When they do:

1. The system matches their current task/interest to relevant documents
2. Key passages are summarized and added to the agent's memory stream
3. The research informs subsequent creative output

This models how real creative professionals consult references.

## Contents

### Artbooks (6)

| File | Source |
|------|--------|
| art-of-skyrim.pdf | The Elder Scrolls V: Skyrim |
| dark-souls-design-works.pdf | Dark Souls Design Works |
| dragon-age-inquisition-artbook.pdf | Dragon Age: Inquisition |
| ff16-artbook.pdf | Final Fantasy XVI |
| ffxiv-2.0-concept-specs.pdf | FFXIV: A Realm Reborn concept specs |
| witcher-3-artbook.pdf | The Witcher 3: Wild Hunt |

### GDDs (8)

| File | Source |
|------|--------|
| chop-socky-chooks-gdd.pdf | Chop Socky Chooks |
| deus-ex-design-document-annotated.pdf | Deus Ex (annotated) |
| diablo-pitch-document-1994.pdf | Diablo (1994 pitch) |
| fallout-bos2-design-document.pdf | Fallout: Brotherhood of Steel 2 |
| grim-fandango-puzzle-document-1996.pdf | Grim Fandango (1996 puzzle doc) |
| monaco-gdd-2003.pdf | Monaco (2003) |
| planescape-torment-vision-statement-1997.pdf | Planescape: Torment (1997 vision) |
| wasteland-2-vision-document.pdf | Wasteland 2 |

### WBBs (4)

| File | Source |
|------|--------|
| doom-bible-tom-hall-1992.pdf | Doom Bible (Tom Hall, 1992) |
| fallout-bible-complete.pdf | Fallout Bible (complete) |
| vtm-2nd-edition.pdf | Vampire: The Masquerade 2nd Edition |
| world-of-cyberpunk-2077.pdf | The World of Cyberpunk 2077 |

### Papers

Pending migration from `master-thesis/literature-review/papers/` (180 files, 12 categories). See roadmap.

## Zotero Integration

`bibliography.bib` is symlinked from `master-thesis/references/bibliography.bib`. To keep it current:

1. In Zotero → Preferences → Better BibTeX → Automatic Export
2. Set export path to `master-thesis/references/bibliography.bib`
3. The symlink in `library/` picks up changes automatically

Agents parse `bibliography.bib` for citation metadata when consulting references.

## Not Committed

All PDFs and the bibliography symlink are in `.gitignore`. The `library/` structure is committed; the contents are local.
