# How Tarotoo integrates this dataset into its readings (technical overview)

Tarotoo's reading pipeline grounds card interpretations in this dataset using retrieval-augmented generation (RAG). Because the corpus is a fixed set of 78 records, retrieval is a **deterministic dictionary lookup by card name**, with no embeddings, semantic search, or vector database. This document explains how the integration works at a technical level. The code samples illustrate the method and are not Tarotoo's production source code.

## Where the data lives

A copy of the dataset (`cards.json`, pinned to a specific release) is deployed server-side with the application. During reading generation, it is loaded, parsed, and indexed in memory by normalized card name. Subsequent lookups within that process have average-case O(1) complexity, and no external request is required while a reading is generated. Moving the application to a newer dataset release involves reviewing and replacing the deployed data file.

```python
import json

with open("cards.json", encoding="utf-8") as f:
    cards = {
        card["name"].strip().lower(): card
        for card in json.load(f)
    }

def get_card(name):
    return cards.get(name.strip().lower())
```

## How a reading is grounded

When a user draws cards, the pipeline looks up each drawn card in the in-memory index, selects the fields relevant to the interpretation, and adds them to the model input as a structured grounding block. The same general mechanism is applied across Tarotoo's supported tarot reading types.

The fields used for a standard upright-card interpretation are:

- `name`
- `keywords_upright`
- `meaning_upright`
- `love`, `career`, `mood`, `spiritual`

Fields not required for the standard grounding block—including reversed keywords and meanings, `url`, and catalog fields such as `arcana`, `suit`, and `element`—are left out to keep the model input focused and token-efficient.

Each drawn card becomes one line of reference text:

```python
def card_context(name):
    card = get_card(name)

    if not card:
        return ""

    return (
        f"{card['name']}. "
        f"Keywords: {', '.join(card['keywords_upright'])}. "
        f"Meaning: {card['meaning_upright']} "
        f"Love: {card['love']} "
        f"Career: {card['career']} "
        f"Mood: {card['mood']} "
        f"Spiritual: {card['spiritual']}"
    )

def grounding_block(names):
    contexts = []

    for name in names:
        context = card_context(name)

        if context:
            contexts.append(context)

    if not contexts:
        return ""

    lines = [
        f"{index}. {context}"
        for index, context in enumerate(contexts, start=1)
    ]

    return (
        "\n\nCard meanings from the Tarotoo dataset "
        "(ground each interpretation in these):\n"
        + "\n".join(lines)
    )
```

The model's system prompt includes the instruction *"Ground each card interpretation in the provided card meanings from the Tarotoo dataset."* The user's question, selected spread, card positions, and retrieved card context are then provided as structured inputs. The retrieved meanings guide the symbolic framework of the interpretation, while the model generates a natural-language reading adapted to the user's question and the role of each card within the selected spread.

## Yes/no readings

For yes/no readings, the dataset's `yes_no` field (`yes`, `no`, or `maybe`) supplies the predefined result for each of the 78 cards, avoiding the need for a separate hand-maintained mapping:

```python
def yes_no(name):
    card = get_card(name)
    return card["yes_no"] if card else "maybe"
```

## Why it is built this way

Grounding readings in a published, versioned dataset makes Tarotoo's symbolic framework more consistent and inspectable. Developers and users can examine the published source meanings used to inform the readings.

Because retrieval is deterministic and performed against a locally deployed file, it adds negligible processing overhead, introduces no network latency, and creates no runtime dependency on an external data service. Updates remain deliberate: a newer dataset release is reviewed and deployed before its changes are used in live readings.
