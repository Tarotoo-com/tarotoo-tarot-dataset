# Tarotoo Tarot Card Meanings Dataset & Developer Tools

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
| `yes_no_reversed`   | string       | `"yes"`, `"no"`, or `"maybe"` for a reversed card                                |
| `keywords_upright`  | string[]     | 4–5 upright keywords                                                             |
| `keywords_reversed` | string[]     | 4–5 reversed keywords                                                            |
| `meaning_upright`   | string       | Upright meaning as concise keyword phrases                                       |
| `meaning_reversed`  | string       | Reversed meaning as concise keyword phrases                                      |
| `love`              | string       | Love/relationships context (short phrase)                                        |
| `love_reversed`     | string       | Reversed love/relationships context (keyword phrases)                            |
| `career`            | string       | Career/work context (short phrase)                                               |
| `career_reversed`   | string       | Reversed career/work context (keyword phrases)                                   |
| `mood`              | string       | Mood/emotional tone (short phrase)                                               |
| `mood_reversed`     | string       | Reversed mood/emotional tone (keyword phrases)                                   |
| `spiritual`         | string       | Spiritual-growth context (short phrase)                                          |
| `spiritual_reversed`| string       | Reversed spiritual-growth context (keyword phrases)                              |

## Access the Dataset and Tools

- **Hugging Face:** [huggingface.co/datasets/Tarotoo/tarotoo-tarot-card-meanings](https://huggingface.co/datasets/Tarotoo/tarotoo-tarot-card-meanings)
- **Kaggle:** [kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings](https://www.kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings)
- **Kaggle Notebook:** [kaggle.com/code/tarotoo/tarotoo-tarot-dataset-eda-validation-examples](https://www.kaggle.com/code/tarotoo/tarotoo-tarot-dataset-eda-validation-examples)
- **npm:** [`tarotoo-tarot`](https://www.npmjs.com/package/tarotoo-tarot)
- **PyPI:** [`tarotoo-tarot`](https://pypi.org/project/tarotoo-tarot/)
- **MCP server** for AI assistants: [`tarotoo-mcp-server`](https://github.com/Tarotoo-com/tarotoo-mcp-server) (official registry: `io.github.Tarotoo-com/tarotoo-mcp-server`)
- **Dataset homepage:** [tarotoo.com/open-data](https://tarotoo.com/open-data)
- **Research paper:** [ssrn.com/abstract=7217458](https://ssrn.com/abstract=7217458)
- **Zenodo — dataset** (concept DOI, always resolves to the latest dataset version; dataset + dataset paper): [10.5281/zenodo.21285777](https://doi.org/10.5281/zenodo.21285777)
- **Zenodo — full repository/archive of this repo** (dataset, source files, build scripts, automated validation, software packages, documentation): [10.5281/zenodo.21514519](https://doi.org/10.5281/zenodo.21514519)
- **Zenodo — full repository/archive of this repo** (Concept DOI): [10.5281/zenodo.21268290](https://doi.org/10.5281/zenodo.21268290)

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

The dataset's interpretive text was initially generated by Tarotoo using generative AI. The generation process was guided by the historical tarot sources listed below and Tarotoo's earlier static card interpretations. All 78 card records were subsequently reviewed and edited by Tarotoo for consistency in meaning, terminology, tone, structure, and the distinction between upright and reversed interpretations.

A. E. Waite's *The Pictorial Key to the Tarot* provides the principal historical reference for Rider–Waite–Smith symbolism and conventional card meanings. Major Arcana base attributions, suit elements, and planet–sign correspondences for numbered Minor Arcana cards follow the Golden Dawn system documented in *Book T*. Additional planet and zodiac values are simplified mappings created by Tarotoo from elemental triplicities and classical or commonly used modern planetary rulerships.

The love, career, mood, and spiritual fields are contemporary contextual extensions of traditional card meanings. Their upright and reversed values were generated from each card's established symbolism and interpretive orientation. The upright and reversed yes/no values are simplified classifications based on the meaning of each orientation. These categories are not presented as distinct fields in the historical works.

Automated validation checks confirm that the dataset contains 78 unique cards, all required fields are complete, and enumerated values follow the defined schema.

## References

The dataset's principal historical references are:

1. Waite, A. E. (1911). [*The Pictorial Key to the Tarot*](https://en.wikisource.org/wiki/The_Pictorial_Key_to_the_Tarot). William Rider & Son. — Historical reference for Rider–Waite–Smith card meanings and symbolism.
2. Mathers, S. L. MacGregor, and Felkin, H. (late nineteenth century). [*Book T: The Tarot*](https://benebellwen.com/wp-content/uploads/2013/02/mathers-and-felkin-golden-dawn-book-t-the-tarot-1888.pdf). — Historical reference for Major Arcana base attributions, suit elements, and planet–sign decan correspondences for numbered Minor Arcana cards.

## How Tarotoo uses this dataset

When a reading is generated on Tarotoo.com, the meanings of the drawn cards are retrieved from this dataset and included in the model prompt, so interpretations are anchored to these published meanings rather than left entirely to the model. See [`docs/integration.md`](docs/integration.md) for how this works.

## License

Released under the [MIT License](LICENSE) — free to use, copy, modify, and redistribute, including commercially. Attribution to Tarotoo (tarotoo.com) is appreciated.

## Citation

> Tarotoo. (2026). Tarotoo Tarot Card Meanings: Complete Dataset Repository and Infrastructure (Version 2.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21514519

**DOI guide:**

- [10.5281/zenodo.21514519](https://doi.org/10.5281/zenodo.21514519) — full repository/archive of this repo (dataset, source files, build scripts, automated validation, software packages, documentation)
- [10.5281/zenodo.21268290](https://doi.org/10.5281/zenodo.21268290) — Concept DOI: not a specific version; always resolves to the latest repository archive
- [10.5281/zenodo.21285777](https://doi.org/10.5281/zenodo.21285777) — dataset only, concept DOI (data files + dataset paper; always resolves to the latest dataset version)


See also [`CITATION.cff`](CITATION.cff); a new DOI is issued for each tagged release.

## Intended Use

This dataset is intended for educational, research, creative, entertainment, and self-reflection purposes. It should not be used as a substitute for medical, legal, financial, mental-health, or other professional advice.
