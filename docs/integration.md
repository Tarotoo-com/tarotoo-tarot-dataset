# How Tarotoo grounds its readings in this dataset

Tarotoo's AI readings do not rely on the model's memorized tarot knowledge alone. Each reading is grounded in this published dataset, so the interpretation of every card is anchored to the meanings released here rather than improvised.

## The approach

This is retrieval-augmented generation in its simplest, most dependable form. Because the corpus is a fixed set of 78 records — one per card — retrieval is a direct, deterministic lookup by card name, not a similarity search over embeddings. A given card always maps to the same published record, so the meaning behind a reading is never left to chance.

## What happens during a reading

1. The reader draws one or more cards.
2. For each drawn card, its record is looked up in this dataset.
3. The fields needed for interpretation — keywords, the core meaning, and the love, career, mood, and spiritual contexts — are provided to the model as reference material alongside the reader's question.
4. The model is asked to base each card's interpretation on those provided meanings.

For yes/no readings, the dataset's `yes_no` field supplies the answer for all 78 cards directly, rather than leaving the verdict to the model.

## Why it matters

Grounding readings this way makes them consistent and inspectable: anyone can open this dataset and see the exact meanings a reading was based on. It also means any improvement to the published meanings flows straight through to the live readings, because the site draws from the same source that is released here.

Only the fields useful for interpretation are used; other columns in the dataset are not part of the prompt.
