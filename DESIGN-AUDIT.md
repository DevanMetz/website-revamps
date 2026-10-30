# Design audit: why all eleven sites looked the same

The sites do not import a shared CSS file. Each one has its own `site/assets/css/site.css`, written by its own `src/build.py`. They were all made from the same mental template, though, so they share this fingerprint:

- **Type:** every site used `system-ui, -apple-system, "Segoe UI", sans-serif` at `16px/1.6`. Headings were the same system font with tight negative tracking (about −.03 to −.055em). No webfonts.
- **Header:** a white bar 90–104px tall. On the left was a text wordmark: a bold uppercase name above a tiny letter-spaced subline, with no real logo. On the right were plain text links (hover or current page shown with an underline or color) and a phone number, with one outline "Request a quote" button. Below 900px the links collapsed into a "Menu" button.
- **Hero:** a full-width dark slate or navy band (`#1d2a30`-ish) with a white h1 at `clamp(2.8rem, 6vw, 6rem)`, a grey lead paragraph and two buttons (one solid accent, one outline or text link). An optional cut-out image sat at the right.
- **Palette:** dark blue-grey ink `#17-20 2a-2e 30-36`, line `#d8e0de`, pale `#f1f5f4`, and one accent per site (red, green, teal, orange, amber, yellow, blue). The neutrals were essentially identical across sites.
- **Layout:** a `.wrap` of `min(1180–1200px, 100% − 48px)`, sections padded 80px, product cards as bordered white boxes on a grid of 4 across, an alternating two-column "feature" rhythm, a stats row with left-border dividers, and a dark contact band followed by a dark footer.
- **Buttons:** square-cornered, solid accent, 48–54px tall, bold system font.

Each site now has its own art direction in `sites/<slug>/DESIGN.md`. No two sites share a font pairing, hero composition or nav pattern:

| Site | Fonts (display / text) | Hero | Nav |
|---|---|---|---|
| taylor-industries | Instrument Serif / Instrument Sans | light split, electrode collage on a pale tray | three zones: logo, centered links, CTA |
| grant-riveters | Barlow Semi Condensed (italic heavy) / Barlow | machine line-up standing on a baseline | two rows: masthead, then product-family tabs |
| don-dye-company | Bricolage Grotesque / Atkinson Hyperlegible | centered pulley on a pedestal under a centered headline | classic right links over a thick green rule |
| collins-instrument | IBM Plex Sans / IBM Plex Mono | engineering-drawing title block | numbered mono cells |
| fontana-machine | Big Shoulders Display / Work Sans | full-width condensed poster type over a photo band | pager utility strip above the main bar |
| crosbie-foundry | Zilla Slab / Public Sans | editorial slab headline on sand, casting photo overlapping the fold | small caps with the phone at left |
| has-mor-industries | Red Hat Display / Red Hat Text | o-ring photo in a circular crop bleeding off the right | left-packed links; scrolling link row on mobile |
| heat-transfer-systems | Chivo / Chivo Mono | full-bleed fabrication photo, copy at bottom left | transparent over the photo, solid on scroll |
| garzo-products | DM Serif Display / DM Sans | framed catalog cover, centered | centered masthead, oval logo, nav below |
| bm-rebuilders | Archivo Narrow / Karla | mosaic of real shop photos | fixed left rail on desktop |
| stevens-wire-products | Jost / Lora | type-only centered headline with one drawn wire line, photo strip below | links divided by hairlines |
