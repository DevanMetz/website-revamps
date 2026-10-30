# Taylor Industries redesign preview

A speculative static redesign preview of taylor-ind.com. The deployable site is `site/`.

Pages: Home, Electrodes, ECG, TENS, Tab, Adhesive Strips, Custom Electrodes, Production Machines, ECG Electrode Production Machine, Packaging Systems, Machine Information Request, Contact, Links, and 404.

Edit product data in `src/data.py` and page templates in `src/build.py`, then run `python3 src/build.py` (requires Pillow). CSS and JavaScript are in `site/assets/`. The generated HTML is committed and needs no build step to host.

Run `npx wrangler deploy` from the project root to serve the static site on workers.dev. Cloudflare Pages drag-and-drop of `site/` also works. Forms use a mailto fallback and open the visitor's email application. For direct submission, use a Cloudflare Pages Function, Formspree, or point form actions back at the existing `/cgi-bin/contMEact.pl` and `/cgi-bin/contMCHNact.pl` scripts.

Every page has a `noindex` meta tag for this preview; remove it before launch. The sitemap uses the intended production domain.

PDF-only content included: TENS parts 532204152 and 53101152, grounding pad GP96, and Tab part number TITAB. Dated 2009-era experience claims were omitted and should be confirmed before use.

## Content sources

Visible product and company copy was checked against `reference/crawl-page-text.txt` and `reference/electrode-reference-guide.txt`; the home page also follows `reference/old-home.html`. Product specifications and claims come from these references; no claims were invented. Navigation, form status, and page-not-found text are functional interface copy.

Light edits to source wording include:

- Adhesive strips: “These 3\" x .5\" adhesive strips are ideal for securing lead wires to a patient and are made using the same medical grade, Latex Free, Hypoallergenic materials used in our ECG electrodes.” Corrects “srips.”
- Custom electrodes: “Do you see a unique need in the market that could be filled by an innovative electrode design?” Corrects “inovated.”
- Packaging systems: “With the optional dual pouch configuration, two smaller pouches can be made side-by-side giving you added packaging flexibility.” Corrects “flexability.”
- The 5CS product's “5 strips per card” corrects “5 strips per cards”; product quantity labels also correct “electrods” to “electrodes.”
- Introductory and machine copy is lightly trimmed or combined from the referenced sentences, including the home custom-electrode and production-machine paragraphs and the ECG machine description.

The 2009-era “17 years” and “fourteen years” experience claims were omitted pending confirmation. The © year was dropped. The forms are mailto fallbacks. Remove the preview `noindex` tags at launch. Hosting uses `npx wrangler deploy` with the Worker and static assets configured in `wrangler.jsonc`.

Electrode category pages show all products and specifications directly, with stable part-number anchors and a category-level quote or samples link. Product data remains in `src/data.py`; transparent image variants are selected by the build when available, with originals backed up in `img-originals/`.

Catalog products use open, aligned image wells with two columns on mobile; the ECG options follow the product list. Category tiles share a compact layout on home and the electrode index, where the reference guide sits alongside the categories.
