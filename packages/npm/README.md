# tarotoo-tarot

All **78 tarot card meanings** (Rider–Waite–Smith tradition) as structured data with lookup helpers. This is the open [Tarotoo tarot dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset) — the same card meanings that ground the AI readings on [Tarotoo.com](https://tarotoo.com).

```bash
npm install tarotoo-tarot
```

## Usage

```js
import { cards, getCard, listCards, searchCards, yesNo } from "tarotoo-tarot";

cards.length;                        // 78
getCard("The Fool").meaning_upright; // "The Fool signals a fresh start..."
getCard("fool").yes_no;              // "maybe" (name matching is forgiving)
listCards({ suit: "cups" });         // ["Ace of Cups", ..., "King of Cups"]
searchCards("heartbreak", 3);        // [Three of Swords, ...]
yesNo("The Sun");                    // "yes"
```

Or import the raw data directly:

```js
import cards from "tarotoo-tarot/cards.json" with { type: "json" };
```

Each card has: `id`, `name`, `arcana`, `suit`, `number_numerology`, `element`, `planet`, `zodiac`, `primary_color`, `yes_no`, `keywords_upright`, `keywords_reversed`, `meaning_upright`, `meaning_reversed`, `love`, `career`, `mood`, `spiritual`, `url`.

## Related

- Dataset source: [github.com/Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset)
- MCP server for AI assistants: [github.com/Tarotoo-com/tarotoo-mcp-server](https://github.com/Tarotoo-com/tarotoo-mcp-server)
- Python package: `pip install tarotoo-tarot`

## License

Data and code released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution to Tarotoo (tarotoo.com). For entertainment and self-reflection purposes only — not medical, legal, financial, or mental-health advice.
