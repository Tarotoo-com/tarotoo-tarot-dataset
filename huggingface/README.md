---
license: cc-by-4.0
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
| `number` | int | Card number (courts: Page=11, Knight=12, Queen=13, King=14) |
| `element` | string | Classical element association |
| `astrology` | string | Astrological association (Golden Dawn attributions; decans for pips) |
| `yes_no` | string | `"yes"`, `"no"`, or `"maybe"` — for yes/no readings |
| `keywords_upright` | list[string] | Upright keywords |
| `keywords_reversed` | list[string] | Reversed keywords |
| `meaning_upright` | string | Upright interpretation |
| `meaning_reversed` | string | Reversed interpretation |
| `love` | string | Love/relationships context |
| `career` | string | Career/work context |

## Usage

```python
from datasets import load_dataset

cards = load_dataset("REPLACE-HF-USERNAME/tarotoo-tarot-card-meanings", split="train")
fool = next(c for c in cards if c["name"] == "The Fool")
print(fool["meaning_upright"])
```

## Methodology

Interpretations are grounded in the Rider–Waite–Smith tradition (A. E. Waite, *The Pictorial Key to the Tarot*, 1911, public domain) and written in Tarotoo's editorial voice. Astrological attributions follow the Golden Dawn system. The dataset text is original writing.

## Related resources

- **Source repository:** [github.com/Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset)
- **MCP server** (query the meanings from AI assistants): [github.com/Tarotoo-com/tarotoo-mcp-server](https://github.com/Tarotoo-com/tarotoo-mcp-server)
- **Website:** [tarotoo.com](https://tarotoo.com)

## License and citation

Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use, share, and adapt, including commercially, with attribution to Tarotoo (tarotoo.com). A citable DOI is issued via Zenodo for each tagged release; see the source repository's `CITATION.cff`.

Tarot readings are for entertainment and self-reflection only — not medical, legal, financial, or mental-health advice.
