"""Tarotoo tarot card meanings: all 78 Rider-Waite-Smith cards as structured data.

The open Tarotoo dataset (github.com/Tarotoo-com/tarotoo-tarot-dataset) - the
same card meanings that ground the AI readings on tarotoo.com. CC BY 4.0.
"""

import json
from importlib.resources import files
from typing import Optional

__version__ = "1.5.0"

#: All 78 cards, ordered by id (0-21 Major Arcana, then Wands, Cups, Swords, Pentacles).
cards = json.loads(files(__package__).joinpath("cards.json").read_text(encoding="utf-8"))

_by_name = {c["name"].lower(): c for c in cards}


def get_card(name: str) -> Optional[dict]:
    """Get one card by name (case-insensitive, tolerates a missing leading "The")."""
    key = str(name).strip().lower()
    if key in _by_name:
        return _by_name[key]
    if f"the {key}" in _by_name:
        return _by_name[f"the {key}"]
    return None


def list_cards(arcana: Optional[str] = None, suit: Optional[str] = None) -> list:
    """List card names, optionally filtered by arcana ("major"/"minor") or suit."""
    result = cards
    if arcana:
        result = [c for c in result if c["arcana"] == arcana]
    if suit:
        result = [c for c in result if c["suit"] == suit]
    return [c["name"] for c in result]


def search_cards(query: str, limit: int = 10) -> list:
    """Search cards by theme or keyword across names, keywords, and meanings."""
    q = str(query).strip().lower()
    terms = [t for t in q.split() if t]
    scored = []
    for c in cards:
        haystack = " ".join(
            [
                c["name"],
                *c["keywords_upright"],
                *c["keywords_reversed"],
                c["meaning_upright"],
                c["meaning_reversed"],
                c["love"],
                c["career"],
                c["mood"],
                c["spiritual"],
            ]
        ).lower()
        score = 0
        if q in c["name"].lower():
            score += 10
        for t in terms:
            if any(t in k for k in c["keywords_upright"]):
                score += 3
            if any(t in k for k in c["keywords_reversed"]):
                score += 2
            if t in haystack:
                score += 1
        if score > 0:
            scored.append((score, c))
    scored.sort(key=lambda s: -s[0])
    return [c for _, c in scored[:limit]]


def yes_no(name: str) -> Optional[str]:
    """The yes/no/maybe value of a card for yes-or-no readings."""
    card = get_card(name)
    return card["yes_no"] if card else None
