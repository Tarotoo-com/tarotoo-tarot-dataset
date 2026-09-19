# tarotoo-tarot

[![PyPI](https://img.shields.io/pypi/v/tarotoo-tarot)](https://pypi.org/project/tarotoo-tarot/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-dataset-yellow)](https://huggingface.co/datasets/Tarotoo/tarotoo-tarot-card-meanings)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21285777.svg)](https://doi.org/10.5281/zenodo.21285777)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://github.com/Tarotoo-com/tarotoo-tarot-dataset/blob/main/LICENSE)

All **78 tarot card meanings** (Rider–Waite–Smith tradition) as structured data with lookup helpers. This is the open [Tarotoo tarot dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset) — the same card meanings that ground the AI readings on [Tarotoo.com](https://tarotoo.com).

```bash
pip install tarotoo-tarot
```

## Usage

```python
from tarotoo_tarot import cards, get_card, list_cards, search_cards, yes_no

len(cards)                              # 78
get_card("The Fool")["meaning_upright"] # "New beginnings, spontaneity, innocence..."
get_card("fool")["yes_no"]              # "maybe" (name matching is forgiving)
list_cards(suit="cups")                 # ["Ace of Cups", ..., "King of Cups"]
search_cards("heartbreak", limit=3)     # [Three of Swords, ...]
yes_no("The Sun")                       # "yes"
```

Each card has: `id`, `name`, `arcana`, `suit`, `number_numerology`, `element`, `planet`, `zodiac`, `yes_no`, `yes_no_reversed`, `keywords_upright`, `keywords_reversed`, `meaning_upright`, `meaning_reversed`, `love`, `love_reversed`, `career`, `career_reversed`, `mood`, `mood_reversed`, `spiritual`, `spiritual_reversed`.

## Links

| Resource | Link |
| --- | --- |
| Dataset source and docs | [Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset) |
| Dataset homepage | [tarotoo.com/open-data](https://tarotoo.com/open-data) |
| npm package | [`tarotoo-tarot`](https://www.npmjs.com/package/tarotoo-tarot) |
| MCP server for AI assistants | [`tarotoo-mcp-server`](https://www.npmjs.com/package/tarotoo-mcp-server) |
| Hugging Face | [Tarotoo/tarotoo-tarot-card-meanings](https://huggingface.co/datasets/Tarotoo/tarotoo-tarot-card-meanings) |
| Kaggle | [tarotoo/tarotoo-tarot-card-meanings](https://www.kaggle.com/datasets/tarotoo/tarotoo-tarot-card-meanings) |
| Citable DOI | [10.5281/zenodo.21285777](https://doi.org/10.5281/zenodo.21285777) |

## License

Data and code released under the [MIT License](https://github.com/Tarotoo-com/tarotoo-tarot-dataset/blob/main/LICENSE). Attribution to Tarotoo (tarotoo.com) is appreciated. This dataset is intended for educational, research, creative, entertainment, and self-reflection purposes. It should not be used as a substitute for medical, legal, financial, mental-health, or other professional advice.
