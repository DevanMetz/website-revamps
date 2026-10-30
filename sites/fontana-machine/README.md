# Fontana Machine preview

A speculative redesign preview of https://www.fontanamachine.com/. The static site includes Home, Directions, Contact, Privacy Policy, and a 404 page.

Edit content and templates in `src/data.py` and `src/build.py`, then run `python3 src/build.py`. The build uses Pillow to optimize the source images. Run `python3 src/check.py` to check the output.

Preview: https://fontana-machine-redesign.metzdevan.workers.dev (Cloudflare Worker `fontana-machine-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

Home presents machining capabilities in a responsive three-column grid with native-size photos, direct contact and directions links, and a shared emergency and business-hours strip. Contact places the emergency pager first and, on mobile, the inquiry form before the remaining contact details. Directions retains all five driving routes. The inquiry form opens a prefilled email using a mailto fallback. For production, replace it with a Cloudflare Worker or Pages Function, Formspree, or the company's existing form handler if available. Remove the noindex meta tags and `X-Robots-Tag` header and update `robots.txt` at launch.

## Content sources

Content comes from `reference/crawl-page-text.txt` and the corresponding rendered HTML. Light edits: the home hero uses the source sentence “Heavy machining and fabrication for aerospace and industry is our specialty.” The machining paragraph removes direct address and combines the source sentences about production, prototypes, weights, CNC, and close tolerances. The refurbishing paragraph combines the two source sentences, removing “not only” and “they have.” The training paragraph removes the rhetorical questions and merges the statements about vocational training and industry involvement. The location sentence removes “We are” and “the” before Ontario International Airport. The emergency paragraph combines the source sentences and removes “all your.” The map and photo alt text is shortened or clarified from the original page context. Titles and descriptions use source wording and location. The privacy text and routes are retained.

Omitted dated claims: the 2003 copyright notices. Defunct external directory links and resources were removed. `reference/crawl-notes.txt` records a failed third-party image, `https://www.aerospacemall.com/ambanner/4blk.gif` (404); it was not used. No other failed assets were listed.
