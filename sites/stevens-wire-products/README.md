# Stevens Wire Products preview

Preview: https://stevens-wire-products-redesign.metzdevan.workers.dev (Cloudflare Worker `stevens-wire-products-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

Pages: home, about, design and prototyping, products, material handling, conveyor, food service, medical, displays, shelving and guards, wire forms, careers, contact, and 404.

Edit product names, descriptions and image selections in `src/data.py`; edit shared templates and other page content in `src/build.py`. Run `python3 src/build.py` to regenerate the HTML and optimized images, then `python3 src/check.py` to check the output. Pillow is required for the build.

For hosting, configure a Cloudflare Worker with static assets pointing at `site/` in your own `wrangler.jsonc`, then run `npx wrangler deploy`. This preview deliberately contains no Wrangler configuration. The contact form opens a mailto draft; production alternatives include a Cloudflare Worker or Pages Function, Formspree, or the company's existing form handler. Remove the `noindex` meta tags and X-Robots-Tag header and update `robots.txt` at launch.

## Content sources

Content and photos come from `reference/crawl-page-text.txt`, the rendered HTML, and `reference/assets.tsv`; the brochure is the supplied PDF. Sentences are reproduced from the source. The career application and shift hours retain the source wording with typographic punctuation normalized.

Omitted dated or time-sensitive material: the jobs page's current openings and hourly wages; the old copyright year, page update year, and hiring banner; and “new information is coming soon” on wire forms. The founding year is retained as a fixed fact. The PDF filename contains a year but its link label does not. No failed or HTTP-only assets were listed in `reference/crawl-notes.txt`.
