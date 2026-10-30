# PASS 2 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.
1. Breadcrumbs show only "Home /" with nothing after it. Either render the full trail (Home / Idler Pulleys / Single Row, current page as aria-current text) or remove breadcrumbs entirely. Prefer the full trail.
2. Technical drawings sit tiny in full-width grey panels with lots of empty space. On desktop (>=1024px) lay each section out as: drawing figure (native size, linked to full size, thin border, no big panel) in a narrow left column (~260px) and the intro/notes for that groove/series next to it; the table goes full-width below. On mobile, drawing centred at native size, no panel.
3. Bearings page has no image. Add the real bearing photo/drawing used on the old ubb.htm page (see reference/assets.tsv / reference/html/ubb*) in the same figure style.
4. Make sure every spec table has a <caption> (visually hidden is fine) and <th scope="col">; first column cells as <th scope="row">.
5. Home product cards: the Single Row card image (a long row of pulleys) is tiny; use the card media box full width with object-fit: contain and less padding so it reads; keep all four cards same height.
6. Footer: label the right column links plainly ("Catalog (PDF, 4.6 MB)", "Contact") - no "Contact & quotes".
