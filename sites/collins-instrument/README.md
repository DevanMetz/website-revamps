# Collins Instrument Company preview

A speculative redesign preview of https://collinsinst.com/. Pages: home, control valves, fittings and valves, isolating flanges, grounding rings, valve parts and trim, custom machining, and contact.

Edit content in `src/data.py` and templates and page copy in `src/build.py`, and control valve tables in `src/valve_tables.py`, then run `python3 src/build.py`. Pillow is required. Run `python3 src/check.py` to check the generated site. The complete static output is in `site/`.

Preview: https://collins-instrument-redesign.metzdevan.workers.dev (Cloudflare Worker `collins-instrument-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

Forms compose an email in the visitor's mail application; they do not post data. For production, connect a Cloudflare Worker or Pages Function, Formspree, or the company's existing form handler if available.

## Content sources

Content is derived from the crawled pages and `reference/pcv.pdf.txt`. Sentences were lightly edited for grammar, clarity and length, including the home introduction and stock paragraph; product card descriptions; valve configuration and application descriptions; flange insert, stock and application descriptions; grounding ring materials, sizes and stock descriptions; valve trim inventory and finish descriptions; and machining capability, materials and applications descriptions. Trademark notes retain the source wording. The flange table was transcribed from `flangespec.gif`; the original dimensional drawing is also provided. The control valve specification, selection and dimension tables are reproduced as HTML from the brochure; the brochure remains linked for the accompanying drawings and ordering information. No specification or selection table is left exclusively in the PDF.

Omitted dated claims: “Over 50 Years”, “For over 50 years”, “more than 20 years”, the 2003 copyright year, and the live date widget. The old footer lists fax (979) 848-0733, while the header and contact page list (979) 848-0783; this preview uses the latter. The crawl notes report no failed asset downloads. The PDF's historical response-time promise and pricing references were omitted.
