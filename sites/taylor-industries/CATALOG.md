# Catalog upgrade — electrode pages

Scope: /electrodes/, /electrodes/ecg/, /electrodes/tens/, /electrodes/tab/, /electrodes/adhesive-strips/, /electrodes/custom/ (plus small hooks in /contact/). Edit src/data.py, src/build.py, site/assets/css/site.css, site/assets/js/*, then run `python3 src/build.py` to regenerate site/. Do not touch other pages except shared header/footer if needed. No network, no deploy, no browser checks (sandbox can't). Make all decisions yourself; do not ask questions. Commit nothing (I commit).

## Hard rules
- NEVER invent specs, shape names, materials, certifications, prices, lead times or copy. Every value must come from src/data.py, reference/crawl-page-text.txt or reference/electrode-reference-guide.txt. Where the website and the PDF disagree (9000ZT/9200ZT diameter vs square dims, D2625 per pouch), keep the website value already in data.py.
- Derived values are allowed only when computed mechanically from real data: mm numbers parsed from the size strings (for sorting and size-band filters), "Round" for ECG items whose size says "diameter", the TENS shape word already in the TENS title (Square / Rectangle / Round / Oval), cloth-variant code presence.
- Do not name ECG shapes otherwise (the site gives no shape names for them). Do not add marketing taglines, helper sentences or decorative labels. Minimal UI labels only (e.g. "Search", "Filters", "Clear", "Details", "Request quote / samples", "Compare").
- Light stack: plain HTML + CSS + one small vanilla JS file `site/assets/js/catalog.js` (target < 8 KB unminified-ish, deferred, only on electrode pages). No frameworks, no build tools, no external requests.
- Progressive enhancement: full product list and every spec must be server-rendered in HTML and usable with JS off. JS only adds search/filter/sort/compare/view toggles. Elements that only work with JS start `hidden` and are revealed by JS.

## Data
- Move ALL catalog data into src/data.py as one list of dicts (category, code, alt codes, size_in, size_mm, parsed width/height mm, material/element/laminate, also-available text, pack fields, image, note, source = "site" or "guide"). Include TAB (code shown as "TAB / TITAB"), GP96 grounding pad, 5FS, 5CS, all ECG, all TENS incl. the two guide-only TENS items (532204152, 53101152) marked "Listed in the Electrode Reference Guide" with no photo (use a neutral empty frame with the code, not a fake image).
- ECG material line stays verbatim: "Solid Gel - Foam Monitoring Electrode"; cloth version shown as "Also available in Cloth (2300SW)". The TL225 note and its wire photo stay.
- Emit `site/assets/catalog.json` (code, category, url#anchor, size text, mm, material summary) for the index-page search; on category pages the JS reads the rendered DOM (data-* attributes), not JSON.

## Product row/card (same component on every category page)
- Each product = `<article id="{CODE}" class="product" data-code data-alt data-w data-h data-filters...>` with: image (bigger than now: at least 112px square on desktop cards, 72px on mobile rows; real photos only), code (h3), size in + mm, material/element line, pack line, "Also available in …" line when real.
- Expandable detail: a `<details>` inside each product ("Details") revealing the full spec list as a `<dl>` (every field we have, incl. footnote-marked pouch/case info, cloth code, source) and a larger image. Opening via URL hash (/electrodes/ecg/#2300ZT) scrolls to and opens that product and highlights it briefly (respect prefers-reduced-motion).
- Actions on every product: primary "Request quote / samples" = `mailto:sales@taylor-ind.com?subject=Quote / sample request: {CODE} {Category}&body=` prefilled with code, size and a blank "Quantity:" / "Company:" lines; secondary "Contact form" link to `/contact/?product={CODE}` (see Contact). Plus a "Compare" checkbox (ECG and TENS only).
- Desktop: grid of cards, 4 per row at 1440 (3 at 1024, 2 at 768). Mobile (≤600px): one compact horizontal row per product (image left, text right), actions in one line below; the whole list must be no longer than the current mobile ECG page (≈6,500 CSS px) with details closed.

## Catalog toolbar (ECG and TENS pages; sticky under the header on desktop only)
- Search input with visible label "Search by product code", type=search, inputmode none special; matches code and alt codes case-insensitively and ignoring spaces/dashes (e.g. "2300", "2300zt", "2300SW" → 2300ZT; "9719" → 971904152). Enter jumps to the single match if only one.
- Filter chips as real checkbox inputs inside `<fieldset>`s with `<legend>`s, styled as chips with visible checked + focus state:
  - ECG: Size (largest dimension, parsed mm): "Up to 25 mm", "26–40 mm", "41–50 mm", "Over 50 mm" — compute band membership in build.py and only render bands that have items; Material: "Cloth version available"; Outline: "Round" (diameter items) only; Pack: "30 per pouch", "20 per pouch".
  - TENS: Conductive element (Tin / Black Carbon), Shape (Square / Rectangle / Round / Oval), Also available in (White Cloth / Foam, from the real availability strings), Per pouch (4 / 2 / 1).
  - OR within a group, AND across groups. Show counts per chip (e.g. "Round (2)").
- Sort select: "Product code" (default, site order) / "Size: small to large" / "Size: large to small" (by parsed area).
- Result count in an aria-live="polite" region ("12 of 27 electrodes"), "Clear" button, empty state "No electrodes match." with a Clear button and a link to Custom Electrodes + contact.
- Persist search/filters to the URL query (?q=&size=…) via history.replaceState so filtered views are shareable; restore on load.
- View toggle "Cards / Table" (aria-pressed buttons). Table view = one real `<table>` (rendered server-side, hidden until chosen; with JS off it shows below the cards inside a `<details>` "Spec table") with caption, scope headers, columns: Code, Size (in), Size (mm), Material/element, Also available, Per pouch, Per case; same filters apply. Table scrolls horizontally inside a focusable region on mobile.
- Mobile: toolbar collapses: search always visible, filters behind a "Filters (n)" disclosure button (aria-expanded), sort + view inline.
- Remove the old 27-code jump-chip wall (search replaces it).
- Keep the "Download reference guide (PDF)" link visible in the catalog header row on both pages.

## Compare (ECG + TENS)
- Up to 4 products via the Compare checkbox. A small fixed tray at bottom (role=region, aria-label="Compare") shows selected codes as removable chips, "Compare (n)" button, and "Request quote for selected" mailto listing all selected codes+sizes.
- "Compare" opens a native `<dialog>` with a side-by-side table of the selected products (image, size in/mm, material, also available, pack). Esc/close button closes; focus returns. 5th selection is prevented with a status message.

## Print
- @media print on catalog pages: hide header nav, toolbar, tray, actions, images in table; force table view (all rows, or the filtered rows if a filter is active), keep footnote and contact line. Add a "Print spec table" button next to the view toggle (calls window.print()).

## Electrodes index (/electrodes/)
- Keep intro copy. Add a site-wide "Search by product code" box at the top of the categories section; results list (from catalog.json, fetched on first focus/typing) shows code, category, size and links to the product anchor; keyboard: ↑/↓ through results, Enter opens; use a listbox/combobox pattern correctly or a simple list of links in an aria-live region (simpler is fine).
- Category cards show the real product count (e.g. "27 products") from data, computed, nothing else.
- Reference guide block: keep, label the link "Electrode reference guide (PDF, 1.1 MB)" — the site states 1.1MB; verify against the real file size and use the real size of site/assets/Electrode_Reference_Guide.pdf if different.

## Tab, Adhesive strips, Custom
- Tab and Adhesive strips use the same product component (cards + details + quote/contact actions), no toolbar (too few items). Adhesive strips keep "(not a monitoring electrode)".
- Custom: keep copy (verbatim minus the 17-years claim, as now). Primary action "Request a custom electrode quote" → mailto subject "Custom electrode inquiry"; secondary "Contact form" → /contact/?product=Custom%20electrode. Add the reference guide link.
- Every category page ends with a small row linking the other electrode categories (existing names only).

## Contact hook
- /contact/: if `?product=` is present, prefill Questions & Comments with "Product: {value}\n" and set the form subject to "Quote / sample request: {value}". Sanitize (text only, max 60 chars).

## Accessibility & performance
- All controls keyboard-operable with visible :focus-visible; chips are checkboxes; toggles use aria-pressed; disclosure uses aria-expanded; dialog uses <dialog> with labelled heading. Contrast ≥ 4.5:1 for text, 3:1 for chip borders/checked states. Touch targets ≥ 44px on mobile. Respect prefers-reduced-motion.
- Hidden products use the `hidden` attribute. No layout shift: images keep width/height attributes. No new web fonts. Keep total CSS growth modest.

## Report
- At the end, print a short summary of files changed and list any data you could NOT place without guessing.
