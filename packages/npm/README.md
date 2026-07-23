# tarotoo-tarot

All **78 tarot card meanings** (Rider–Waite–Smith tradition) as structured data with lookup helpers. This is the open [Tarotoo tarot dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset) — the same card meanings that ground the AI readings on [Tarotoo.com](https://tarotoo.com).

```bash
npm install tarotoo-tarot
```

## Usage

```js
import { cards, getCard, listCards, searchCards, yesNo } from "tarotoo-tarot";

cards.length;                        // 78
getCard("The Fool").meaning_upright; // "New beginnings, spontaneity, innocence..."
getCard("fool").yes_no;              // "maybe" (name matching is forgiving)
listCards({ suit: "cups" });         // ["Ace of Cups", ..., "King of Cups"]
searchCards("heartbreak", 3);        // [Three of Swords, ...]
yesNo("The Sun");                    // "yes"
```

Or import the raw data directly:

```js
import cards from "tarotoo-tarot/cards.json" with { type: "json" };
```

Each card has: `id`, `name`, `arcana`, `suit`, `number_numerology`, `element`, `planet`, `zodiac`, `yes_no`, `yes_no_reversed`, `keywords_upright`, `keywords_reversed`, `meaning_upright`, `meaning_reversed`, `love`, `love_reversed`, `career`, `career_reversed`, `mood`, `mood_reversed`, `spiritual`, `spiritual_reversed`.

## Related

- Dataset source: [github.com/Tarotoo-com/tarotoo-tarot-dataset](https://github.com/Tarotoo-com/tarotoo-tarot-dataset)
- MCP server for AI assistants: [github.com/Tarotoo-com/tarotoo-mcp-server](https://github.com/Tarotoo-com/tarotoo-mcp-server)
- Python package: `pip install tarotoo-tarot`

## License

Data and code released under the [MIT License](https://github.com/Tarotoo-com/tarotoo-tarot-dataset/blob/main/LICENSE). Attribution to Tarotoo (tarotoo.com) is appreciated. This dataset is intended for educational, research, creative, entertainment, and self-reflection purposes. It should not be used as a substitute for medical, legal, financial, mental-health, or other professional advice.
