# B.M. Rebuilders redesign preview

Preview: https://bm-rebuilders-redesign.metzdevan.workers.dev (Cloudflare Worker `bm-rebuilders-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

## Pages

Home, shop, contact, eight service pages, and a 404 page. The services cover fastener equipment rebuilding, upgrades and electrical upgrades; thread rolling and tapping; precision machining and new parts; wire drawers and compactors; press rebuilding; and tool room and production machine rebuilding. Each service page has a direct contact link above its original machine photo gallery and a compact phone and contact row below it.

## Editing and hosting

Edit the service list in `src/data.py` and the shared templates and page content in `src/build.py`. The build reads the archived source text and HTML in `reference/`, and uses Beautiful Soup and Pillow. Run `python3 src/build.py` to regenerate the static pages and images, and `python3 src/check.py` to check them. CSS and JavaScript live directly in `site/assets/`.

Host `site/` as Cloudflare Workers static assets. Configure a Worker and static assets in `wrangler.jsonc`, then run `npx wrangler deploy`. No deployment configuration is included in this preview.

The contact form opens the visitor's email application using a mailto fallback; it does not submit to a server. For production, connect a Cloudflare Worker or Pages Function, Formspree, or the company's existing form handler if available.

The preview uses noindex meta tags and an `X-Robots-Tag` header, and `robots.txt` disallows crawling. Remove these preview restrictions before launch.

## Content sources

Content and imagery come from the archived pages in `reference/`. The service pages merge the numbered original pages; original technical language, models, specifications, and warranty statements are retained. Gallery images are grouped by original page and given descriptive service-level alt text; original captions appear below the photos, with consecutive identical captions shown once.

Light edits and adaptations:

- Home: “B.M. Rebuilders, Inc. is a family-owned business, established in 1981 for rebuilding and repairing machinery used in the cold forming and wire drawing industry.” The original says “family owned” and “for the purpose of”.
- Home: “Our 20,000 square foot facility under crane has a fully equipped machine shop.” This trims the original sentence; the mill and lathe specifications appear alongside it.
- Home: “Rebuilding, upgrades and precision machining.” This condenses the original service list, which follows as individual cards.
- Shop: “Rebuilding and repairing machinery in Elyria, Ohio.” This combines the original business description and location.
- Shop: “We have four stake bed trucks, each equipped with its own toolbox, to handle repairs and mini or full rebuilds on your floor.” This corrects and trims the original sentence.
- Headings and navigation are short labels derived from the original services and contact details.

The dated “Celebrating Our 20th. Anniversary” claim was omitted. The fixed establishment year 1981 is retained. No failed or HTTP-only images were reported in `reference/crawl-notes.txt`.
