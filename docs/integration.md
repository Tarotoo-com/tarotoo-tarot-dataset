# How Tarotoo integrates this dataset into its readings (technical overview)

Tarotoo's reading pipeline grounds every interpretation in this dataset using retrieval-augmented generation (RAG). Because the corpus is a fixed set of 78 records, retrieval is a **deterministic dictionary lookup by card name**, with no embeddings and no vector search. This document explains how the integration works at a technical level. The code samples are illustrative of the method, not the production source.

## Where the data lives

A copy of the dataset (`cards.json`, pinned to a specific release) is deployed server-side with the application. It is read once, parsed, and indexed in memory by lowercased card name, so lookups are O(1) and no external request is made while a reading is generated. Moving the readings to a newer release of the dataset is a matter of swapping the data file.

```python
import json

with open("cards.json", encoding="utf-8") as f:
    cards = {c["name"].lower(): c for c in json.load(f)}

def get_card(name):
    return cards.get(name.strip().lower())
```

## How a reading is grounded

When a reader draws cards, the pipeline looks up each drawn card in the in-memory index, pulls the fields that inform an interpretation, and adds them to the model prompt as a grounding block. The same mechanism is applied across the reading types (single card, three-card, love, daily).

The fields used per card:

- `name`
- `keywords_upright`
- `meaning_upright`
- `love`, `career`, `mood`, `spiritual`

Fields that do not affect a standard reading (reversed keywords and meanings, `url`, and catalog fields such as `arcana`, `suit`, and `element`) are left out to keep the prompt focused and token-efficient.

Each drawn card becomes one line of reference text:

```python
def card_context(name):
    c = get_card(name)
    if not c:
        return ""
    return (f"{c['name']}. keywords: {', '.join(c['keywords_upright'])}. "
            f"Meaning: {c['meaning_upright']} Love: {c['love']} "
            f"Career: {c['career']} Mood: {c['mood']} Spiritual: {c['spiritual']}")

def grounding_block(names):
    lines = [f"{i+1}. {card_context(n)}" for i, n in enumerate(names) if card_context(n)]
    return ("\n\nCard meanings from the Tarotoo dataset "
            "(ground each interpretation in these):\n" + "\n".join(lines))
```

The model's system prompt carries one added instruction, *"Ground each card interpretation in the provided card meanings from the Tarotoo dataset"*, and the reader's message carries the question plus this grounding block. The retrieved meanings steer the interpretation while the model still writes naturally around the reader's specific question.

## Yes/no readings

For yes/no spreads, the dataset's `yes_no` field (`yes`, `no`, or `maybe`) supplies the verdict for all 78 cards directly, replacing any hand-maintained mapping:

```python
def yes_no(name):
    c = get_card(name)
    return c["yes_no"] if c else "maybe"
```

## Why it is built this way

Grounding readings in a published, versioned dataset makes them consistent and inspectable: anyone can open this dataset and see the exact meanings a reading was based on. Because the lookup is deterministic and served from local memory, grounding adds no measurable latency and no runtime dependency on an external service. And because the site draws from the same source released here, any improvement to the published meanings flows straight through to the live readings.
