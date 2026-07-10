# tarotoo-tarot

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

Each card has: `id`, `name`, `arcana`, `suit`, `number_numerology`, `element`, `planet`, `zodiac`, `yes_no`, `keywords_upright`, `keywords_reversed`, `meaning_upright`, `meaning_reversed`, `love`, `career`, `mood`, `spiritual`, `url`.

## Related

- Dataset source: [github.com/Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset)
- MCP server for AI assistants: [github.com/Tarotoo-com/tarotoo-mcp-server](https://github.com/Tarotoo-com/tarotoo-mcp-server)
- npm package: `npm install tarotoo-tarot`

## License

Data and code released under the [MIT License](https://github.com/Tarotoo-com/tarotoo-tarot-dataset/blob/main/LICENSE). Attribution to Tarotoo (tarotoo.com) is appreciated. This dataset is intended for educational, research, creative, entertainment, and self-reflection purposes. It should not be used as a substitute for medical, legal, financial, mental-health, or other professional advice.
