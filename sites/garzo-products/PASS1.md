# PASS 1 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.
Home, catalog form and products index look good. Product pages need structure:
1. /products/oil-level-regulators/108/ (and check 101, 211, 213, linear diaphragm operators, low flow meters for the same problems):
   - A paragraph is split mid-sentence ("...including" / "engine or compressor lubricating oil...") - join broken paragraphs everywhere (grep built HTML for <p> ending without terminal punctuation).
   - The sentence "This feature will allow the controller to operate with adequate oil supply pressures." appears twice in a row - remove the duplicate.
   - The page is one long wall of text. Give it sub-headings drawn from the content itself (e.g. "Oil supply", "Gauge glass", "Level alarms", "Mounting", "Valve and seat", "Construction", "Installation kits") - plain nouns, no slogans - and keep each paragraph as written.
   - The feature list ("A Complete System", "High Allowable Supply Pressures", ...) renders as loose unstyled lines - make it a real <ul> styled as a compact 2-column checklist on desktop under a "Features" heading, placed right after the intro.
   - Photo: keep in a right column on desktop, sticky is not needed; on mobile place it after the first paragraph.
   - "How to order" image is a tall ordering-code chart: keep it as an image but cap its display width at 1.25x native, put it in a bordered figure, and link it to the full-size file ("Open full size"); on mobile allow it to be tapped to open full size.
2. Product cards on home and /products/: replace the ↗ icon on internal links with → (↗ only for external links / PDFs opening elsewhere).
3. Home: remove the decorative yellow bar under the hero (the stripe at the bottom right) - decorative noise.
4. Catalog request page: hero subline is real copy - keep. Product registration: check the same.
5. Header: add (800) 729-8807 as a tel link on desktop.
