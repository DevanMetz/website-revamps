# PASS 1 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.

## 1. Service pages: captions are detached from their photos (biggest problem)
On the original pages (reference/html/*.html.html) the bold text lines are captions sitting in the same table cell / row as specific photos. Right now every service page shows all captions as a loose list on the left and the photos in a ragged column on the right, so the captions mean nothing. Example, pressbuild: 063.jpg "National 1000", 064.jpg "Ajax", 065.jpg "National 700"; 066.jpg + 067.jpg "National 2000 MaxiPress heading slide and wrist pin assembly."; 069.jpg "Complete rebuild and a triple kick-out installed"; 068.jpg "Waterbury Toolroom Press" / "Ready to deliver to the door".
- For EVERY service page (and its 2/3 continuation pages that were merged), re-parse the original table structure and pair each caption with the photo(s) in the same cell / the cell directly above or below it in the same column. Where one caption clearly spans several photos, group them in one figure. Photos with no caption get no caption (never invent one).
- Render as a uniform gallery grid of <figure>s: 3 columns at 1440, 2 at 768, 1 at 390; images object-fit: contain on a light neutral box with a consistent aspect ratio (4:3), never upscaled above 1.5x native (they are ~200px - keep the boxes about 300px wide max on desktop, so use 4 columns at 1440 if needed), with the caption below each image. Click opens the full image file.
- Any intro paragraph text on the page stays above the gallery.

## 2. Invented copy - remove (design rule: no taglines, helper text, secondary labels; never invent)
- Home: "Rebuilding, upgrades and precision machining." under Our services -> delete. Heading "Our services" -> "Services".
- Home: "Built for the work" -> "Shop". "Field service / Four equipped stake bed trucks" summary table: keep only if worded from source; simpler: replace that table with the real sentences from the source.
- Home: "Machine down?" band -> delete the band entirely (keep the phone in header/footer/contact).
- Home: "Talk with B.M. Rebuilders" + "Elyria, Ohio" band -> heading "Contact", button "Contact us".
- Service pages: "Discuss your machine" -> "Contact", button "Contact us" (not "Request an inquiry" unless source uses that).
- Shop page: hero subline "Rebuilding and repairing machinery in Elyria, Ohio." -> delete unless verbatim in source. "On your floor" heading -> "Field service" only if no better source term; "Our shop" -> "Shop".
- Grep the built HTML text against reference/crawl-page-text.txt and remove any other sentence not in the source (headings, nav, form labels and button text excepted).

## 3. Visual
- Home service cards: internal links use → not ↗. The phone "Call 1-888-686-6237 ↗" uses no arrow.
- Home hero is a flat dark block with empty right half: put one strong real photo there (pick the best-quality shop/machine photo from reference/img - e.g. the large Waterbury 068.jpg 371x207 or similar; do not upscale beyond 1.5x) or make the hero single-column and shorter.
- Shop page: add the real shop photos if the source has any; otherwise fine.
