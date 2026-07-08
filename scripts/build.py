#!/usr/bin/env python3
"""Merge the per-suit source files into the canonical dataset artifacts.

Outputs:
    data/cards.json   - canonical full dataset (array of 78 card objects)
    data/cards.csv    - flat CSV mirror (keywords joined with "; ")
    data/cards.jsonl  - one card per line, for Hugging Face
    plus synced copies of cards.json into packages/npm and packages/python

Run: python3 scripts/build.py
"""

import csv
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "src"
OUT = ROOT / "data"

SOURCE_FILES = [
    "major_arcana.json",
    "wands.json",
    "cups.json",
    "swords.json",
    "pentacles.json",
]

REQUIRED_FIELDS = [
    "id", "name", "arcana", "suit", "number", "element", "astrology", "numerology", "primary_color",
    "yes_no", "keywords_upright", "keywords_reversed",
    "meaning_upright", "meaning_reversed", "love", "career", "mood", "spiritual", "url",
]

VALID_ARCANA = {"major", "minor"}
VALID_SUITS = {None, "wands", "cups", "swords", "pentacles"}
VALID_YES_NO = {"yes", "no", "maybe"}
VALID_ELEMENTS = {"Fire", "Water", "Air", "Earth"}


def validate(cards):
    errors = []
    ids = set()
    names = set()
    for card in cards:
        label = card.get("name", f"id={card.get('id', '?')}")
        for field in REQUIRED_FIELDS:
            if field not in card:
                errors.append(f"{label}: missing field '{field}'")
        extra = set(card) - set(REQUIRED_FIELDS)
        if extra:
            errors.append(f"{label}: unexpected fields {sorted(extra)}")
        if card.get("id") in ids:
            errors.append(f"{label}: duplicate id {card['id']}")
        ids.add(card.get("id"))
        if card.get("name") in names:
            errors.append(f"{label}: duplicate name")
        names.add(card.get("name"))
        if card.get("arcana") not in VALID_ARCANA:
            errors.append(f"{label}: bad arcana {card.get('arcana')!r}")
        if card.get("suit") not in VALID_SUITS:
            errors.append(f"{label}: bad suit {card.get('suit')!r}")
        if card.get("yes_no") not in VALID_YES_NO:
            errors.append(f"{label}: bad yes_no {card.get('yes_no')!r}")
        if card.get("element") not in VALID_ELEMENTS:
            errors.append(f"{label}: bad element {card.get('element')!r}")
        for kw_field in ("keywords_upright", "keywords_reversed"):
            kws = card.get(kw_field, [])
            if not isinstance(kws, list) or len(kws) < 3:
                errors.append(f"{label}: {kw_field} needs at least 3 keywords")
        for text_field in ("meaning_upright", "meaning_reversed", "love", "career", "mood", "spiritual", "url", "numerology", "primary_color"):
            if not str(card.get(text_field, "")).strip():
                errors.append(f"{label}: empty {text_field}")

    if len(cards) != 78:
        errors.append(f"expected 78 cards, got {len(cards)}")
    if ids and sorted(ids) != list(range(78)):
        errors.append("ids are not exactly 0..77")
    return errors


def main():
    cards = []
    for filename in SOURCE_FILES:
        path = SRC / filename
        with path.open(encoding="utf-8") as f:
            cards.extend(json.load(f))

    cards.sort(key=lambda c: c.get("id", -1))

    errors = validate(cards)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    json_path = OUT / "cards.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
        f.write("\n")

    jsonl_path = OUT / "cards.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as f:
        for card in cards:
            f.write(json.dumps(card, ensure_ascii=False) + "\n")

    csv_path = OUT / "cards.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=REQUIRED_FIELDS)
        writer.writeheader()
        for card in cards:
            row = dict(card)
            row["keywords_upright"] = "; ".join(card["keywords_upright"])
            row["keywords_reversed"] = "; ".join(card["keywords_reversed"])
            writer.writerow(row)

    package_copies = [
        ROOT / "packages" / "npm" / "data" / "cards.json",
        ROOT / "packages" / "python" / "src" / "tarotoo_tarot" / "cards.json",
    ]
    for dest in package_copies:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(json_path, dest)

    print(f"OK: {len(cards)} cards -> {json_path.name}, {jsonl_path.name}, {csv_path.name} (+ {len(package_copies)} package copies)")


if __name__ == "__main__":
    main()
