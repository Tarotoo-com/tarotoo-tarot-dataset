# How Tarotoo grounds its readings in this dataset (technical overview)

Tarotoo's readings use retrieval-augmented generation (RAG). Because the corpus is a fixed set of 78 records, retrieval is a **deterministic dictionary lookup by card name**, with no embeddings and no vector search. This document describes the technique so the same grounding can be reproduced from the published data. The examples are illustrative (they are not the production code); the point is the method, which works in any language or stack.

## 1. Load the data into a lookup

The dataset is small enough to load once and index in memory, keyed by lowercased card name:

```python
import json

with open("cards.json", encoding="utf-8") as f:
    cards = {c["name"].lower(): c for c in json.load(f)}

def get_card(name):
    return cards.get(name.strip().lower())
```

You can also install the helper package (`pip install tarotoo-tarot` or `npm i tarotoo-tarot`), which ships the same data with lookup functions built in.

## 2. Select the interpretation fields

Only the fields that inform an interpretation are pulled for each drawn card:

- `name`
- `keywords_upright`
- `meaning_upright`
- `love`, `career`, `mood`, `spiritual`

Fields that do not affect a standard reading (reversed keywords and meanings, `url`, and catalog fields such as `arcana`, `suit`, and `element`) are deliberately left out to keep the prompt focused and token-efficient.

## 3. Build a grounding block and add it to the prompt

Each drawn card becomes one line of reference text, appended to the reader's message:

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

The model's system prompt carries one added instruction, *"Ground each card interpretation in the provided card meanings from the Tarotoo dataset"*, and the user message carries the question plus this grounding block. The retrieved meanings steer the interpretation, while the model still writes naturally around the reader's specific question.

## 4. Yes/no readings

For yes/no spreads, the dataset's `yes_no` field (`yes`, `no`, or `maybe`) supplies the verdict for all 78 cards directly, replacing any hand-maintained lookup:

```python
def yes_no(name):
    c = get_card(name)
    return c["yes_no"] if c else "maybe"
```

## Performance

Because the corpus is a fixed 78-record file, it is read and indexed once per process and served from memory: each lookup is O(1), adds no measurable latency to a reading, and needs no external call at read time. Updating the readings to a new release of the dataset is a matter of swapping the data file.
