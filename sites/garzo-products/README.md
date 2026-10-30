# Garzo Products preview

Preview: https://garzo-products-redesign.metzdevan.workers.dev (Cloudflare Worker `garzo-products-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

## Pages

- Home and products index, with direct links to product families and Model 213
- Oil level regulators 101B and 108B, including the 108B installation guide
- Low flow meter 300B
- Lubricator box controls 211 and 213
- Linear diaphragm operators 501-4, 501-6, 501-12, 501-18 and 501-25
- Catalog request, product registration, contact, and 404

## Editing and hosting

Edit `src/data.py` and `src/build.py` (transparent line drawings are in `src/transparent/`), then run `python3 src/build.py`. The build reads the supplied reference text and images and writes static pages and optimized images to `site/`. Run `python3 src/check.py` to check links, markup, redirects, external requests and asset sizes.

For Cloudflare Workers static assets, configure a Worker and `wrangler.jsonc` to serve the `site` directory, then deploy with `npx wrangler deploy`. No deployment configuration is included in this preview.

Forms prepare an email in the visitor's email application; they do not submit to a server. For production, connect a Cloudflare Worker or Pages Function, Formspree, or the company's existing form handler. Remove the noindex meta tags and `X-Robots-Tag` header and update `robots.txt` before launch.

## Content sources

Content and product diagrams come from the supplied crawl and downloaded assets. The home product list removes “Today” and “much, much more”; the products index merges that list into “Oil level regulators, shut down devices, low flow meters, lubricator box controls, oil reservoirs and linear diaphragm operators.” The catalog delivery note removes “Please” in the introductory banner. The 213 page replaces the source's “Coming Soon!” with a contact direction; the shut-down device and oil reservoir contact direction is likewise navigational copy. The registration form adds full name because the original instructions request it. The contact form adds name, email, phone and message fields for inquiries. Page titles and navigation labels are shortened from source product names.

The auto date widget, “Quality Products since 1939” tagline, and © 2000–11 were omitted. The fixed “Since 1939” statement is retained as specified in the brief. The original duplicated 108B sentence and source typography remain in the extracted product text; the installation guide contains an incomplete vent-line dimension in the source, so no dimension was inferred. Product specifications and ordering information embedded in source images remain as images.

The crawl notes report a blocked HTTP Google Analytics script and a missing `images/mount5018.jpg` (404). Neither is used. No product PDFs were supplied in the reference or site assets.

Product details place their existing actions beside the introduction and use the adjacent column for available ordering charts and diagrams. The 501 model sections group each model's images above its specification chart; full-size links appear when charts are reduced to fit.
