# Heat Transfer Systems preview

A speculative redesign preview of https://heattransfersys.com/. The static site is in `site/`.

Pages: home, engineering and design, heat exchangers, waste heat recovery, special products, fabrication (cutting, welding and testing), replacements and repairs, facility, clients, photos, contact, and a 404 page. The facility page links to the original facilities survey.

Edit lists in `src/data.py` and page content and shared markup in `src/build.py`; run `python3 src/build.py` to regenerate HTML and the sitemap. Styles and interaction live in `site/assets/css/site.css` and `site/assets/js/site.js`. Run `python3 src/check.py` for static verification. Pillow is required to regenerate the logo.

Preview: https://heat-transfer-systems-redesign.metzdevan.workers.dev (Cloudflare Worker `heat-transfer-systems-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

## Content sources

Content comes from `reference/crawl-page-text.txt`, the rendered HTML and the facilities survey PDF. The TEMA and WHRU URLs returned 404, so their pages use only the home, engineering and survey descriptions. The photo gallery contained an external Flickr link and no downloadable gallery images; it retains the original photo-set link. No fabrication images were available for a local grid. The logo is the only downloaded image used.

Light edits and combinations: the home hero combines the original focus and specialty; the introduction trims the original engineering and fabrication sentences; the expertise cards condense the original expertise list; the clients teaser combines the client-list introduction and industries list. Engineering trims “quickly” and “wealth of.” Heat exchanger construction combines the home construction list and engineering sentence. Waste heat recovery combines the home expertise and survey product lists. Special products trims the original introduction. Fabrication trims scheduling and quality language, removes the elapsed-time reference from the welding sentence, and retains the original equipment and inspection specifications. Repairs combines and lightly trims the original two sentences. Facility introduces the linked survey by describing its sections and changes “have sported” to “have had.” Contact trims the original invitation. Headings and navigation labels are shortened for the new layout.

Omitted dated or time-relative claims: “Over the past 30+ years” in welding; the 2012 copyright; the old Flash update notices; and the current-sounding “continue to serve” client wording. The fixed 1980 founding and December 2013 solar installation dates are retained. The “Save Energy for Tomorrow” slogan and the “thousands of units” sentence were omitted. The energy monitoring link was omitted.

The crawl notes report blocked HTTP-only Google jQuery and an unavailable Adobe Flash Player image (403). Neither is needed by the static site. Flash files were not embedded.
