import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));

/** All 78 cards, ordered by id (0-21 Major Arcana, then Wands, Cups, Swords, Pentacles). */
export const cards = JSON.parse(
  readFileSync(join(here, "data", "cards.json"), "utf8"),
);

const byName = new Map(cards.map((c) => [c.name.toLowerCase(), c]));

/**
 * Get one card by name (case-insensitive, tolerates a missing/extra leading "The").
 * @param {string} name e.g. "The Fool" or "Ace of Cups"
 * @returns {object|null}
 */
export function getCard(name) {
  const key = String(name).trim().toLowerCase();
  if (byName.has(key)) return byName.get(key);
  if (byName.has(`the ${key}`)) return byName.get(`the ${key}`);
  return null;
}

/**
 * List card names, optionally filtered.
 * @param {{arcana?: "major"|"minor", suit?: "wands"|"cups"|"swords"|"pentacles"}} [filter]
 * @returns {string[]}
 */
export function listCards(filter = {}) {
  let result = cards;
  if (filter.arcana) result = result.filter((c) => c.arcana === filter.arcana);
  if (filter.suit) result = result.filter((c) => c.suit === filter.suit);
  return result.map((c) => c.name);
}

/**
 * Search cards by theme or keyword across names, keywords, and meaning texts.
 * @param {string} query
 * @param {number} [limit=10]
 * @returns {object[]} matching cards, best match first
 */
export function searchCards(query, limit = 10) {
  const q = String(query).trim().toLowerCase();
  const terms = q.split(/\s+/).filter(Boolean);
  return cards
    .map((c) => {
      const haystack = [
        c.name,
        ...c.keywords_upright,
        ...c.keywords_reversed,
        c.meaning_upright,
        c.meaning_reversed,
        c.love,
        c.career,
        c.mood,
        c.spiritual,
      ]
        .join(" ")
        .toLowerCase();
      let score = 0;
      if (c.name.toLowerCase().includes(q)) score += 10;
      for (const t of terms) {
        if (c.keywords_upright.some((k) => k.includes(t))) score += 3;
        if (c.keywords_reversed.some((k) => k.includes(t))) score += 2;
        if (haystack.includes(t)) score += 1;
      }
      return { card: c, score };
    })
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, limit)
    .map((s) => s.card);
}

/**
 * The yes/no/maybe value of a card for yes-or-no readings.
 * @param {string} name
 * @returns {"yes"|"no"|"maybe"|null}
 */
export function yesNo(name) {
  const card = getCard(name);
  return card ? card.yes_no : null;
}
