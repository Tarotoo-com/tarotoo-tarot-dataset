# Tarotoo Tarot Card Meanings Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21268290.svg)](https://doi.org/10.5281/zenodo.21268290)

A complete, structured dataset of all **78 tarot cards** (22 Major Arcana + 56 Minor Arcana), based on the classic Rider–Waite–Smith tradition. Published by [Tarotoo](https://tarotoo.com) as part of its AI transparency initiative: these are the card meanings that ground the AI-generated readings on Tarotoo.com.

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
| `meaning_upright`   | string       | Two-sentence upright interpretation                                              |
| `meaning_reversed`  | string       | Two-sentence reversed interpretation                                             |
| `love`              | string       | One-sentence love/relationships context                                          |
| `career`            | string       | One-sentence career/work context                                                 |
| `mood`              | string       | One-sentence mood/emotional-tone context                                         |
| `spiritual`         | string       | One-sentence spiritual-growth context                                            |
| `url`               | string       | Card meaning page on tarotoo.com                                                 |

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

Interpretations are grounded in the Rider–Waite–Smith tradition (A. E. Waite, _The Pictorial Key to the Tarot_, 1911, public domain) and written in Tarotoo's editorial voice. Astrological attributions follow the Golden Dawn system. Yes/no values follow the mapping used in Tarotoo's readings. The dataset text is original writing, not copied from other contemporary sources.

## References

Card meanings follow the Rider–Waite–Smith tradition as codified in these public-domain works:

1. Waite, A. E. (1911). *The Pictorial Key to the Tarot*. William Rider & Son. — primary source for card meanings
2. Hermetic Order of the Golden Dawn (c. 1888–1897). *Book T: The Tarot*. — astrological and elemental attributions
3. Mathers, S. L. MacGregor (1888). *The Tarot: Its Occult Signification, Use in Fortune-Telling, and Method of Play*.
4. Papus (1889). *The Tarot of the Bohemians*.
5. Ouspensky, P. D. (1913). *The Symbolism of the Tarot*.
6. Thierens, A. E. (1930). *General Book of the Tarot*.

All referenced works are in the public domain. The dataset text itself is original writing and is not copied from any of these works.

## How Tarotoo uses this dataset

When a reading is generated on Tarotoo.com, the meanings of the drawn cards are retrieved from this dataset and included in the model prompt, so interpretations are anchored to these published meanings rather than left entirely to the model. See [`docs/integration.md`](docs/integration.md).

## License

Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to use, share, and adapt this dataset, including commercially, with attribution to Tarotoo (tarotoo.com).

## Citation

> Tarotoo (2026). *Tarotoo Tarot Card Meanings: A Complete 78-Card Structured Dataset* (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.21268291

Concept DOI (always resolves to the latest version): [10.5281/zenodo.21268290](https://doi.org/10.5281/zenodo.21268290). See also [`CITATION.cff`](CITATION.cff); a new DOI is issued for each tagged release.

## For entertainment and self-reflection purposes

Tarot readings are for entertainment and self-reflection only — not medical, legal, financial, or mental-health advice.
