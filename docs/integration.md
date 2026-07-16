# Integrating the dataset into Tarotoo readings

Tarotoo's reading endpoints (`functions.php`, REST namespace `openai/v1`) currently send only card _names_ to the model and rely on its memorized "Rider Waite meanings". The integration grounds each reading in this dataset instead: look up the drawn cards, inject their published meanings into the prompt.

This is retrieval-augmented generation in its simplest, most reliable form — the corpus is 78 fixed records, so retrieval is a deterministic lookup, not a vector search.

## Plan

1. Store `cards.json` in the theme (e.g. `wp-content/themes/tarotoo/data/cards.json`) or load from this repo's release URL with caching.
2. Add a lookup helper in `functions.php`:

```php
function tarotoo_get_card_meaning( $card_name ) {
    static $cards = null;
    if ( $cards === null ) {
        $json  = file_get_contents( get_template_directory() . '/data/cards.json' );
        $list  = json_decode( $json, true );
        $cards = array();
        foreach ( $list as $card ) {
            $cards[ strtolower( $card['name'] ) ] = $card;
        }
    }
    return $cards[ strtolower( trim( $card_name ) ) ] ?? null;
}

function tarotoo_card_context( $card_name ) {
    $card = tarotoo_get_card_meaning( $card_name );
    if ( ! $card ) {
        return '';
    }
    return sprintf(
        "%s — keywords: %s. Meaning: %s Love: %s Career: %s",
        $card['name'],
        implode( ', ', $card['keywords_upright'] ),
        $card['meaning_upright'],
        $card['love'],
        $card['career']
    );
}
```

3. In each reading handler, append the retrieved context to the user message, e.g.:

```php
"content" => "My question: " . $data->mainQuestion . "? Selected cards: "
    . $data->card1 . ", " . $data->card2 . ", " . $data->card3
    . "\n\nCard meanings from the Tarotoo dataset (ground your interpretation in these):\n"
    . "1. " . tarotoo_card_context( $data->card1 ) . "\n"
    . "2. " . tarotoo_card_context( $data->card2 ) . "\n"
    . "3. " . tarotoo_card_context( $data->card3 )
```

4. Add one line to each system prompt: _"Ground each card interpretation in the provided card meanings from the Tarotoo dataset."_
5. The `yes_no` field replaces the hardcoded Major-Arcana-only mapping in `handle_openai_yesno_tarot` — it covers all 78 cards.

