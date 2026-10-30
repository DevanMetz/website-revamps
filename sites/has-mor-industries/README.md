# Has-Mor Industries preview

A speculative static redesign preview of https://has-mor.com/. Pages: Home, About, Product information, Ordering information, Request a quote, Contact, and a 404 page. The home page links directly to product types and the quote form, with compact company and materials sections. Product links lead to the size list; the technical pages retain the specifications, installation tables and ordering call-out; mobile tables keep their first column visible while scrolling.

Preview: https://has-mor-industries-redesign.metzdevan.workers.dev (Cloudflare Worker `has-mor-industries-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

Forms open the visitor's email application using a mailto fallback. For production, connect a Cloudflare Worker/Pages Function, Formspree, or the company's existing form handler if available. The preview uses noindex metadata, an X-Robots-Tag header, and a disallow rule in robots.txt; remove these at launch.

## Content sources

Content comes from the crawled home page and the Product Information and Ordering Information PDFs. The live About Us, Product Info, Ordering Info and Quote pages returned HTTP 500; Contact rendered empty. The plaque page had no substantive text. The product and ordering PDFs remain linked as original literature.

Light edits: the home introduction combines the original manufacturing and engineering sentences and removes “premier” and the relative experience claim; the about page trims the customer care sentence and combines the original company and quality assurance copy. The home materials sentence summarizes the PDF's explanation of the jacket and core. The custom shapes paragraph shortens the PDF's invitation to discuss feasibility and minimum requirements. The temperature note shortens “This means that” to “The”. Headings and list capitalization were standardized; numerical specifications and material codes are retained. The quote band and form labels are functional navigation and fields based on the brief.

Omitted dated claims: “over 34 years,” “more than 34 years,” and © 2007. The old third-party translator script and HTTP-only stylesheet were blocked as mixed content; no image downloads failed. Legacy navigation graphics were omitted from the redesign.

## Editing

Edit content and templates in `src/data.py` and `src/build.py`, then run `python3 src/build.py` and `python3 src/check.py`. Transparent image assets are kept in `site/assets/img/`; their prior versions are in `img-originals/`.
