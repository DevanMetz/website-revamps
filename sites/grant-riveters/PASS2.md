# PASS 2 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.

Home is now good. Product pages are not: the automatic extraction from the nested source tables produces duplicated and garbled content. Decision: STOP extracting product content programmatically. Instead, hand-author clean structured content for each product page in src/content/ (one Python module per page, or one data file) by reading the page text yourself in reference/crawl-page-text.txt and the tables in reference/html/*. Every sentence and number must come from the source; you are only cleaning, de-duplicating and structuring it.

Problems seen on /riveters/orbital/bench-top/ (fix here and check every product page for the same):
1. The benefit list appears twice (above "Pneumatic" and again inside it) - show it once per variant.
2. Scraped form text "Select the items that apply, and then let us know how to contact you. Send product literature Require a quotation Have a salesperson contact me" appears in the page body - remove all scraped form text site-wide (grep the built HTML for "Select the items", "Send product literature", "salesperson contact" and make sure they appear only in the real /contact/ form).
3. After the spec table, raw table cell text spills out as loose paragraphs ("Rivet Diameter Capacity in Mild 1018 Steel", "480 lbs @ 80 psi 216 @ 5.5 Kg/Cm²", ...). Remove all such leftovers.
4. Marketing taunts survive ("Now this is a guarantee!", "The other guys try to compete with this but, fall short", "Do not settle for anything less", "Let us quote your next riveting system and we will prove it to you!", "CALL TODAY"). Remove them; keep the facts.
5. Intro paragraph is one wall of text. Split into short paragraphs: durability (2-6 million cycles, hard chrome, bearings, 100% safety factor), processes (Orbital, Twin-Spin, Multi-Spin, Spin-Press; 0.5-1.5 s cycle), capacity (3 mm-38 mm mild steel), fixturing/tonnage, warranty sentence.
6. Spec table "Standard Features" row: keep, but as a separate small list per model only if it is real per-model data; otherwise drop the row.

Page template for each product family: h1; variant anchor links; per variant: photo (native size max 1.25x, light panel, not a full-width grey band), short paragraphs, "Key benefits" list, spec table (one header column + one column per model), warranty sentence as worded on that page; "Literature" links to the matching PDFs; "Request a quote" link.

Also: hero sublines on inner pages (e.g. "Pneumatic, hydraulic and servo-electric bench-top riveters.") - cut per the design rule. Verify at 390 px that the bench-top page is not absurdly long because of duplication (it is currently 25,000 px tall at 390).
Finish by grepping site/ for the strings in items 2-4 and for any paragraph longer than 900 characters; fix all hits.
