# PASS 1 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.

## Content completeness (biggest issue)
The product pages are far thinner than the source. Rework src/data.py so each product page carries ALL factual content from its source pages (reference/crawl-page-text.txt + reference/html), minus marketing taunts and exclamation marks:
- Bench-top page currently shows one short paragraph and one spec table. pneumaticbt.htm alone has: 2-6 million cycles before replacing a part, hard-chromed internals, 100% safety factor design, Orbital/Twin-Spin/Multi-Spin/Spin-Press in one machine, typical cycle 0.5-1.5 s, 3 mm to 38 mm mild steel rivet capacity range, simple work-holding fixtures, lower tonnage than impact methods, a Key Benefits list (modular design, micrometer stroke adjustment, four processes, fast cycle, controlled forming, cost savings, hard-chromed components, hand-scraped surfaces) and the full pneumatic spec table. hydraulicbt.htm and servobt.htm have their own copy, benefits and spec tables. Give each variant (Pneumatic / Hydraulic / Servo-electric) its own section with intro, key benefits list, its own full spec table and its warranty sentence as worded on that page. Add in-page tabs-free anchor links (Pneumatic · Hydraulic · Servo-electric) under the h1.
- Do the same for power-head (pneumaticph, hydraulicph, servoph, prodph), Orbitfeed, double-ended, impact (prod03), squeeze (prod04), presses (prod05 + pneumaticpress + aostandardfeatures + aoproductoptions: features and options lists in full), riveting kits (prodrk), automation, process inspector (Process_Inspector PDF text too), services (contract riveting / prototyping / consulting each with full copy), riveting methods, history (full timeline).
- Where a PDF in reference/*.pdf.txt has clean spec data for a product (servo-riveters, Pneumatic_Riveters_2010, Pneumatic_Press_2010, Riveting_Kit_2010, Process_Inspector_2010, XYZ), link that PDF from the product page under "Literature".
- Every product page must show the product's real photo(s) from reference/img (the source product pages have them - check assets.tsv by page). Bench-top currently has no image at all.

## Bugs
- Bench-top page renders the old Information Request form fields (Name / Title / Company / Address / E-mail / Phone) as a data table. Remove any scraped form-as-table anywhere in the site.
- Bench-top spec table: "Overall Dimensions / Length" row is misaligned (label split into two cells, spills into an extra 7th column). Model it as rows "Overall length", "Overall width", "Overall height" with exactly one header column + one column per model. Check every spec table for the same problem.
- Tables on mobile: wrap in a scroll region (tabindex=0, role=region, aria-label), sticky first column, right-edge fade cue.

## Home
- Remove the decorative "G/R" letters in the hero (fake logo art). Replace with the best real machine photo from reference/img at native size max (no upscale) on a light panel, or leave the hero typographic only.
- Cut the hero subline (design rule) - make the h1 carry it: "Orbital, impact and squeeze riveting machines".
- The riveting machines grid shows only 4 items; show every product family (bench-top orbital, power-head orbital, Orbitfeed, double-ended, impact, hydraulic squeeze, pneumatic presses & cylinders, riveting kits, automation, Process Inspector) with photos in a 4-col (desktop) / 2-col (mobile) grid with consistent 4:3 contain media boxes.
- Add a single fact row from real copy: "Over 230,000 riveting systems installed worldwide" and "Founded on an 1860 invention" style only if worded from the source.
- Remove the "Orbital, Twin-Spin..." helper line under Riveting methods (put the four method names as linked list items instead), and rename "Discuss your application" band to "Request a quote" with phone 800-227-2150 + button.
