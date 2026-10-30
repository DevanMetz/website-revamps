# PASS 2 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.
1. Header: phone floats in the middle between logo and nav - move it to the right, just before the "Request a quote" button. On mobile, show it inside the open menu.
2. Footer: the right column (Products / Design & prototyping / Brochure) sits lower than the Contact column since its heading was removed - align the columns to the top (either both columns with headings or neither; prefer neither, Contact column without its heading too).
3. Home hero photo (building.jpg) is small and floating; make the hero a balanced 2-column grid with the photo in a thin border, vertically centred, at its max allowed size; on mobile place it below the buttons at full width only up to its allowed size.
4. Home product cards: text-only cards (Conveyor, Individual wire forms) - align their title to the bottom like the photo cards so the grid baseline is consistent.
5. Product galleries: images inside boxes have mixed sizes - use a fixed 4:3 box with object-fit: contain and 16px padding so every photo sits at a consistent size; click opens the large version.
6. Re-check About, Careers, Design & prototyping pages for paraphrased or invented sentences (compare against reference/crawl-page-text.txt and the brochure text) and fix.
7. Mobile 390: confirm no overflow and that the product list on product pages sits after the text.
