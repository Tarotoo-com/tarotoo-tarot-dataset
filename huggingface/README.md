---
license: mit
language:
  - en
task_categories:
  - text-generation
  - question-answering
tags:
  - tarot
  - tarot-cards
  - card-meanings
  - rider-waite-smith
  - divination
  - symbolism
pretty_name: Tarotoo Tarot Card Meanings
size_categories:
  - n<1K
configs:
  - config_name: default
    data_files:
      - split: train
        path: cards.jsonl
---

# Tarotoo Tarot Card Meanings

A complete, structured dataset of all **78 tarot cards** (22 Major Arcana + 56 Minor Arcana) in the Rider–Waite–Smith tradition. Published by [Tarotoo](https://tarotoo.com) as part of its AI transparency initiative: these are the card meanings that ground the AI-generated readings on Tarotoo.com.

## Dataset structure

One record per card with the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | int | Stable identifier, 0–77 (0–21 Major Arcana, then Wands, Cups, Swords, Pentacles) |
| `name` | string | Card name, e.g. `"The Fool"`, `"Ace of Cups"` |
| `arcana` | string | `"major"` or `"minor"` |
| `suit` | string/null | `null` for Major Arcana; `"wands"`, `"cups"`, `"swords"`, `"pentacles"` |
| `number_numerology` | int | Card number for numerology (courts: Page=11, Knight=12, Queen=13, King=14) |
| `element` | string | Classical element association |
| `planet` | string/null | Planetary association (Golden Dawn; decan planet for pips) |
| `zodiac` | string/null | Zodiac association (sign, decan sign, or element's signs for courts) |
| `yes_no` | string | `"yes"`, `"no"`, or `"maybe"` — for yes/no readings |
| `keywords_upright` | list[string] | Upright keywords |
| `keywords_reversed` | list[string] | Reversed keywords |
| `meaning_upright` | string | Upright meaning as concise keyword phrases |
| `meaning_reversed` | string | Reversed meaning as concise keyword phrases |
| `love` | string | Love/relationships context |
| `career` | string | Career/work context |
| `mood` | string | Mood/emotional-tone context |
| `spiritual` | string | Spiritual-growth context |
| `url` | string | Card meaning page on tarotoo.com |

## Usage

```python
from datasets import load_dataset

cards = load_dataset("Tarotoo/tarotoo-tarot-card-meanings", split="train")
fool = next(c for c in cards if c["name"] == "The Fool")
print(fool["meaning_upright"])
```

## Methodology

Interpretations are grounded in the Rider–Waite–Smith tradition (A. E. Waite, *The Pictorial Key to the Tarot*, 1911, public domain) and written in Tarotoo's editorial voice. Astrological attributions follow the Golden Dawn system. The dataset text is original writing.

## References

Card meanings follow the Rider–Waite–Smith tradition as codified in these public-domain works:

1. Waite, A. E. (1911). *The Pictorial Key to the Tarot*. William Rider & Son. — primary source for card meanings
2. Hermetic Order of the Golden Dawn (c. 1888–1897). *Book T: The Tarot*. — astrological and elemental attributions
3. Mathers, S. L. MacGregor (1888). *The Tarot: Its Occult Signification, Use in Fortune-Telling, and Method of Play*.
4. Papus (1889). *The Tarot of the Bohemians*.
5. Ouspensky, P. D. (1913). *The Symbolism of the Tarot*.
6. Thierens, A. E. (1930). *General Book of the Tarot*.

All referenced works are in the public domain. The dataset text itself is original writing and is not copied from any of these works.

## Related resources

- **Source repository:** [github.com/Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset)
- **MCP server** (query the meanings from AI assistants): [github.com/Tarotoo-com/tarotoo-mcp-server](https://github.com/Tarotoo-com/tarotoo-mcp-server)
- **Kaggle mirror:** [kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings](https://www.kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings)
- **npm / PyPI packages:** [`tarotoo-tarot`](https://www.npmjs.com/package/tarotoo-tarot) · [`tarotoo-tarot`](https://pypi.org/project/tarotoo-tarot/)
- **Website:** [tarotoo.com](https://tarotoo.com) · [transparency page](https://tarotoo.com/card-meanings-dataset)

## License and citation

Released under the MIT License — free to use, copy, modify, and redistribute, including commercially. Attribution to Tarotoo (tarotoo.com) is appreciated. A citable DOI is issued via Zenodo for each tagged release; see the source repository's `CITATION.cff`.

Tarot readings are for entertainment and self-reflection only — not medical, legal, financial, or mental-health advice.
