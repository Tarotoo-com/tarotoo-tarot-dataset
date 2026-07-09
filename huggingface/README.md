---
license: mit
language:
  - en
task_categories:
  - text-generation
  - question-answering
  - text-retrieval
annotations_creators:
  - expert-generated
language_creators:
  - expert-generated
multilinguality:
  - monolingual
source_datasets:
  - original
tags:
  - tarot
  - tarot-cards
  - card-meanings
  - rider-waite-smith
  - divination
  - symbolism
  - esoteric
  - rag
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

## Dataset details

- **Curated by:** Tarotoo (tarotoo.com)
- **Language:** English
- **License:** [MIT](https://github.com/Tarotoo-com/tarotoo-tarot-dataset/blob/main/LICENSE)
- **Rows:** 78 (one per card) · **Fields:** 18
- **DOI:** [10.5281/zenodo.21268290](https://doi.org/10.5281/zenodo.21268290)
- **Source repository:** [github.com/Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset)

## Uses

- **Retrieval-augmented generation:** ground AI tarot readings in published meanings (this is how Tarotoo.com uses it)
- **Lookup / API backends:** card-meaning services, bots, and apps
- **Analysis:** symbolism, keyword, and correspondence studies across the full deck
- **Live querying from AI assistants** via the [MCP server](https://github.com/Tarotoo-com/tarotoo-mcp-server)

## Dataset structure

One record per card:

| Field | Type | Description |
|---|---|---|
| `id` | int | Stable identifier, 0–77 (0–21 Major Arcana, then Wands, Cups, Swords, Pentacles) |
| `name` | string | Card name, e.g. `"The Fool"`, `"Ace of Cups"` |
| `arcana` | string | `"major"` or `"minor"` |
| `suit` | string/null | `null` for Major Arcana; `"wands"`, `"cups"`, `"swords"`, `"pentacles"` |
| `number_numerology` | int | Card number for numerology (courts: Page=11, Knight=12, Queen=13, King=14) |
| `element` | string | Classical element: Fire, Water, Air, Earth |
| `planet` | string/null | Planetary association (`null` where not applicable, e.g. Aces) |
| `zodiac` | string/null | Zodiac sign(s); the element's three signs for Aces and Pages |
| `yes_no` | string | `"yes"`, `"no"`, or `"maybe"` — for yes/no readings |
| `keywords_upright` | list[string] | Upright keywords |
| `keywords_reversed` | list[string] | Reversed keywords |
| `meaning_upright` | string | Upright meaning as concise keyword phrases |
| `meaning_reversed` | string | Reversed meaning as concise keyword phrases |
| `love` | string | Love/relationships context (short phrase) |
| `career` | string | Career/work context (short phrase) |
| `mood` | string | Mood/emotional tone (short phrase) |
| `spiritual` | string | Spiritual-growth context (short phrase) |
| `url` | string | Card meaning page on tarotoo.com |

### Example instance

```json
{
  "id": 0,
  "name": "The Fool",
  "arcana": "major",
  "suit": null,
  "number_numerology": 0,
  "element": "Air",
  "planet": "Uranus",
  "zodiac": "Aquarius",
  "yes_no": "maybe",
  "keywords_upright": ["new beginnings", "spontaneity", "innocence", "leap of faith", "free spirit"],
  "meaning_upright": "New beginnings, spontaneity, innocence, leap of faith, and free spirit.",
  "mood": "Light, curious, playful.",
  "url": "https://tarotoo.com/tarot-card-meanings/the-fool"
}
```

## Quick start

```python
from datasets import load_dataset

cards = load_dataset("Tarotoo/tarotoo-tarot-card-meanings", split="train")
fool = next(c for c in cards if c["name"] == "The Fool")
print(fool["meaning_upright"])
```

Also available as installable packages: `pip install tarotoo-tarot` · `npm install tarotoo-tarot`.

## Dataset creation

**Curation rationale:** make the exact card meanings behind Tarotoo's AI readings publicly inspectable, verifiable, and reusable — and give AI systems a clean, structured source for tarot meanings.

**Source data:** all card texts are original writing by Tarotoo in the Rider–Waite–Smith tradition, grounded exclusively in public-domain works. Planet and zodiac attributions follow classical rulerships and the Golden Dawn's decan system. Every card was reviewed for consistency across the full deck; validation (78 unique cards, complete fields, valid enums) runs in CI on the source repository.

## References

1. Waite, A. E. (1911). *The Pictorial Key to the Tarot*. William Rider & Son. — primary source for card meanings
2. Hermetic Order of the Golden Dawn (c. 1888–1897). *Book T: The Tarot*. — astrological attributions
3. Mathers, S. L. MacGregor (1888). *The Tarot: Its Occult Signification, Use in Fortune-Telling, and Method of Play*.
4. Papus (1889). *The Tarot of the Bohemians*.
5. Ouspensky, P. D. (1913). *The Symbolism of the Tarot*.
6. Thierens, A. E. (1930). *General Book of the Tarot*.

All referenced works are in the public domain. The dataset text itself is original writing and is not copied from any of these works.

## Considerations

Tarot readings are for entertainment and self-reflection only — not medical, legal, financial, or mental-health advice. The dataset encodes one (widely used) interpretive tradition; other tarot traditions assign different meanings and correspondences.

## Related resources

- **Source repository:** [github.com/Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset)
- **MCP server** (query the meanings from AI assistants): [github.com/Tarotoo-com/tarotoo-mcp-server](https://github.com/Tarotoo-com/tarotoo-mcp-server) — `npx -y tarotoo-mcp-server`
- **Kaggle mirror:** [kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings](https://www.kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings)
- **npm / PyPI packages:** [`tarotoo-tarot`](https://www.npmjs.com/package/tarotoo-tarot) · [`tarotoo-tarot`](https://pypi.org/project/tarotoo-tarot/)
- **Website:** [tarotoo.com](https://tarotoo.com) · [transparency page](https://tarotoo.com/open-data)

## Citation

```bibtex
@dataset{tarotoo_tarot_card_meanings,
  author    = {Tarotoo},
  title     = {Tarotoo Tarot Card Meanings: A Complete 78-Card Structured Dataset},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21268290},
  url       = {https://doi.org/10.5281/zenodo.21268290}
}
```
