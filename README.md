# Tarotoo Tarot Card Meanings Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21268290.svg)](https://doi.org/10.5281/zenodo.21268290)
[![CI](https://github.com/Tarotoo-com/tarotoo-tarot-dataset/actions/workflows/validate.yml/badge.svg)](https://github.com/Tarotoo-com/tarotoo-tarot-dataset/actions)
[![PyPI](https://img.shields.io/pypi/v/tarotoo-tarot)](https://pypi.org/project/tarotoo-tarot/)
[![npm](https://img.shields.io/npm/v/tarotoo-tarot)](https://www.npmjs.com/package/tarotoo-tarot)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-dataset-yellow)](https://huggingface.co/datasets/Tarotoo/tarotoo-tarot-card-meanings)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

A complete, structured dataset of all **78 tarot cards** (22 Major Arcana + 56 Minor Arcana), based on the classic Rider–Waite–Smith tradition. Published by [Tarotoo](https://tarotoo.com). These are the card meanings that ground the AI-generated readings on Tarotoo.com.

## Contents

| File               | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `data/cards.json`  | Canonical dataset — array of 78 card objects           |
| `data/cards.jsonl` | One card per line (Hugging Face-friendly)              |
| `data/cards.csv`   | Flat CSV mirror                                        |
| `data/src/`        | Per-suit source files (edit these, then run the build) |
| `scripts/build.py` | Merges, validates, and regenerates the artifacts       |
| `packages/npm/`    | `tarotoo-tarot` npm package (data + lookup helpers)    |
| `packages/python/` | `tarotoo-tarot` PyPI package (data + lookup helpers)   |
| `huggingface/`     | Dataset card for the Hugging Face mirror               |
| `kaggle/`          | Metadata for the Kaggle mirror                         |

## Schema

Each card record has the following fields:

| Field               | Type         | Description                                                                      |
| ------------------- | ------------ | -------------------------------------------------------------------------------- |
| `id`                | int          | Stable identifier, 0–77 (0–21 Major Arcana, then Wands, Cups, Swords, Pentacles) |
| `name`              | string       | Card name, e.g. `"The Fool"`, `"Ace of Cups"`                                    |
| `arcana`            | string       | `"major"` or `"minor"`                                                           |
| `suit`              | string\|null | `null` for Major Arcana; `"wands"`, `"cups"`, `"swords"`, `"pentacles"`          |
| `number_numerology` | int          | Card number for numerology (courts: Page=11, Knight=12, Queen=13, King=14)      |
| `element`           | string       | Classical element association                                                    |
| `planet`            | string/null  | Planetary association (Golden Dawn; decan planet for pips)                       |
| `zodiac`            | string/null  | Zodiac association (sign, decan sign, or element's signs for courts)             |
| `yes_no`            | string       | `"yes"`, `"no"`, or `"maybe"` — for yes/no readings                              |
| `keywords_upright`  | string[]     | 4–5 upright keywords                                                             |
| `keywords_reversed` | string[]     | 4–5 reversed keywords                                                            |
| `meaning_upright`   | string       | Upright meaning as concise keyword phrases                                       |
| `meaning_reversed`  | string       | Reversed meaning as concise keyword phrases                                      |
| `love`              | string       | Love/relationships context (short phrase)                                        |
| `career`            | string       | Career/work context (short phrase)                                               |
| `mood`              | string       | Mood/emotional tone (short phrase)                                               |
| `spiritual`         | string       | Spiritual-growth context (short phrase)                                          |
| `url`               | string       | Card meaning page on tarotoo.com                                                 |

## Where to get it

- **Hugging Face:** [Tarotoo/tarotoo-tarot-card-meanings](https://huggingface.co/datasets/Tarotoo/tarotoo-tarot-card-meanings)
- **Kaggle:** [tarotoo/tarotoo-tarot-card-meanings](https://www.kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings)
- **npm:** [`tarotoo-tarot`](https://www.npmjs.com/package/tarotoo-tarot)
- **PyPI:** [`tarotoo-tarot`](https://pypi.org/project/tarotoo-tarot/)
- **MCP server** for AI assistants: [`tarotoo-mcp-server`](https://github.com/Tarotoo-com/tarotoo-mcp-server) (official registry: `io.github.Tarotoo-com/tarotoo-mcp-server`)
- **Tarotoo website:** [tarotoo.com/open-data](https://tarotoo.com/open-data)
- **Dataset paper (Zenodo):** [10.5281/zenodo.21285778](https://doi.org/10.5281/zenodo.21285778)

## Installation & quick start

**Python** (PyPI):

```bash
pip install tarotoo-tarot
```

```python
from tarotoo_tarot import cards, get_card, search_cards, yes_no
get_card("The Fool")["meaning_upright"]   # "New beginnings, spontaneity, innocence..."
```

**JavaScript / Node** (npm):

```bash
npm install tarotoo-tarot
```

```js
import { cards, getCard, searchCards, yesNo } from "tarotoo-tarot";
getCard("The Fool").meaning_upright;      // "New beginnings, spontaneity, innocence..."
```

**Hugging Face** (`datasets`):

```python
from datasets import load_dataset
cards = load_dataset("Tarotoo/tarotoo-tarot-card-meanings", split="train")
```

**Kaggle**:

```bash
kaggle datasets download tarotoo/tarotoo-tarot-card-meanings
```

**Raw files** (no dependencies):

```bash
curl -O https://raw.githubusercontent.com/Tarotoo-com/tarotoo-tarot-dataset/main/data/cards.json
```

**AI assistants** (MCP — Claude Desktop, Claude Code, Cursor, etc.):

```json
{
  "mcpServers": {
    "tarotoo-tarot": { "command": "npx", "args": ["-y", "tarotoo-mcp-server"] }
  }
}
```

## Usage

```python
import json

with open("data/cards.json") as f:
    cards = json.load(f)

fool = next(c for c in cards if c["name"] == "The Fool")
print(fool["meaning_upright"])
```

Regenerate artifacts after editing the source files:

```bash
python3 scripts/build.py
```

## Methodology

All interpretive text was created by Tarotoo within the Rider–Waite–Smith tradition, drawing on established tarot sources — primarily A. E. Waite's _The Pictorial Key to the Tarot_ (1911). Planet and zodiac correspondences follow classical rulerships and the decan system documented in the Golden Dawn's _Book T_. Yes/no values follow the mapping used in Tarotoo's readings. Each card was reviewed for consistency in tone, terminology, and structure across the complete deck.

## References

Card meanings and correspondences are informed by established works associated with the Rider–Waite–Smith tradition and related Western esoteric systems:

1. Waite, A. E. (1911). *The Pictorial Key to the Tarot*. William Rider & Son. — primary source for card meanings
2. Hermetic Order of the Golden Dawn (c. 1888–1897). *Book T: The Tarot*. — astrological and elemental attributions
3. Mathers, S. L. MacGregor (1888). *The Tarot: Its Occult Signification, Use in Fortune-Telling, and Method of Play*.
4. Papus (1889). *The Tarot of the Bohemians*.
5. Ouspensky, P. D. (1913). *The Symbolism of the Tarot*.
6. Thierens, A. E. (1930). *General Book of the Tarot*.

These works were selected for their historical importance and continuing influence on modern tarot interpretation.

## How Tarotoo uses this dataset

When a reading is generated on Tarotoo.com, the meanings of the drawn cards are retrieved from this dataset and included in the model prompt, so interpretations are anchored to these published meanings rather than left entirely to the model. See [`docs/integration.md`](docs/integration.md).

## License

Released under the [MIT License](LICENSE) — free to use, copy, modify, and redistribute, including commercially. Attribution to Tarotoo (tarotoo.com) is appreciated.

## Citation

> Tarotoo (2026). *Tarotoo Tarot Card Meanings: A Complete 78-Card Structured Dataset* (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.21268291

Concept DOI (always resolves to the latest version): [10.5281/zenodo.21268290](https://doi.org/10.5281/zenodo.21268290). The accompanying dataset paper is published separately: [10.5281/zenodo.21285778](https://doi.org/10.5281/zenodo.21285778). See also [`CITATION.cff`](CITATION.cff); a new DOI is issued for each tagged release.

## Intended Use

This dataset is intended for educational, research, creative, entertainment, and self-reflection purposes. It should not be used as a substitute for medical, legal, financial, mental-health, or other professional advice.
