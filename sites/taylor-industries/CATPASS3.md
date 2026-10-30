# Catalog polish pass 3 (data rules from CATALOG.md still apply; never invent text or specs)

Edit sources (src/build.py, site/assets/js/catalog.js, site/assets/css/site.css), run `python3 src/build.py`. Consolidate duplicated CSS rules you touch (site.css has repeated .category-card rules — merge them). Keep catalog.js <= 10 KB.

1. /electrodes/ reference guide section: remove the invented helper line "Explore electrode specifications and options." Heading + button only.
2. Desktop cards: put the Compare checkbox and the Details toggle on ONE row (Compare left, Details right) under the quote button, to shorten cards.
3. Mobile cards (<=640px): reduce vertical padding so each ECG card is ~130px tall; line-height of the meta lines ~1.35. Target ECG page height at 390px <= 6,600 CSS px (now 7,348). Keep 44px tap targets.
4. Mobile compare dialog (<=640px): hide the Image row; first column (row labels) sticky left with background, width ~88px; data columns min-width ~110px, font-size .9rem; "All selected:" summary rendered as a small definition list (label: value per line), not one run-on sentence. Desktop: keep image row.
5. Mobile table view: reduce cell padding to ~8px 10px and font-size .9rem so the Code + Size (in) + Size (mm) columns fit at 390px where possible; keep sticky Code column and Scroll hint only when overflowing.
6. Print stylesheet (@media print) for catalog pages: hide header nav, toolbar, tray, buttons, checkboxes, images in table; print the spec table (force table view content visible) with the footnote, page title, and company contact line from the footer. Ensure "Print spec table" switches to table view then calls window.print().
7. Verify product counts unchanged (27/14/2/2), no duplicate ids, node --check catalog.js, report size.
