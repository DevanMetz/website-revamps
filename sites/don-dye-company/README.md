# Don Dye Company redesign

A speculative redesign preview of https://dondyeco.com/. The static site lives in `site/`.

Pages: home, single row idler pulleys, double row idler pulleys, industrial drive pulleys, unground ball bearings, contact and quotes, and a 404 page. The catalog is linked directly from the site.

Edit table data in `src/data.py` and page content and templates in `src/build.py`, then run `python3 src/build.py`. Pillow is required. Styles and behavior are in `site/assets/css/site.css` and `site/assets/js/site.js`. Run `python3 src/check.py` to check the generated site.

Preview: https://don-dye-company-redesign.metzdevan.workers.dev (Cloudflare Worker `don-dye-company-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

The contact form opens a mailto draft; it does not transmit data itself. For production, connect a Cloudflare Worker or Pages Function, Formspree, or the company's existing form handler if available. Remove the noindex meta tags and `X-Robots-Tag` header at launch.

## Content sources

Source: the supplied crawl, rendered HTML, and catalog. Product descriptions were lightly trimmed and edited for grammar: the home construction introduction and five feature bullets; single-row bearing, seal, compression ring and mounting descriptions; double-row load, mounting, bearing and compression ring descriptions; drive pulley construction, standard hubs and specials descriptions; and bearing application, construction and seal descriptions. Product headings and navigation use corrected “groove” spelling. The contact prompt and form labels are functional interface copy. The source's subjective comparative claims and test claims were omitted. Table values are transcribed from the rendered HTML; no dimension table exists only as an image.

Omitted dated or time-relative material: Copyright 2004, foreign patents pending, and the claim that additional sizes are continually being tooled. The patent number is retained as written. No missing or HTTP-only images were reported in `reference/crawl-notes.txt`.

### Edited source wording used on the site

**index.html**

- Don Dye pressed steel pulleys are designed as a complete, self-contained unit for either the flat or V side of a belt.
- Riveted for strength and durability; no spot welding
- Smoothly rolled edges help eliminate belt chafing and scuffing
- Weep holes allow water drainage when mounted horizontally
- Zinc plated
- Compression ring · USA Patent No. 4518372

**idler-pulleys/single-row/index.html**

- Don Dye pressed steel pulleys are designed to make a complete, economical, self-contained unit for either the flat or V side of a belt. They are furnished with a single-row, radial-type precision ground, pre-lubricated ball bearing made of 52100 bearing steel, with contact-type seals to retain lubricant and protect against dirt, dust or foreign matter.
- These bearings contain a 60% fill of high temperature grease; no re-lubrication is required. The inner ring is extended on both sides to provide clearance for abutting parts and greater support on the shaft. A compression ring (USA Patent No. 4518372) between the bearing and pulley bearing pocket provides a firm fit and helps distribute loads evenly to the outer bearing race.
- Accurately bore sized for mounting on standard 1/2" or 5/8" bolts. A 1/2" bore removable sleeve is standard in all pulleys; a 3/8" sleeve is available on request.

**idler-pulleys/double-row/index.html**

- This line of heavy duty double row ball bearing flat, flanged, and V-groove idlers was developed to handle heavier loads that exceed the capacity of single row ball bearing idlers. The double row idlers are more stable when side loads or off-center loads occur.
- Available with 3/8", 1/2", 5/8" and 3/4" bolt mounting, these riveted idlers are constructed from 13 gauge material. Precision bearings made of 52100 bearing steel are pre-lubricated with high temperature lubricant and have contact-type seals. No re-lubrication is required. A compression ring (USA patent 4518372) provides a firm fit and helps distribute loads to the outer bearing race.

**drive-pulleys/index.html**

- Drive pulleys are listed for OEMs as they are built to order and require minimum volumes per part number.
- The pulleys are formed on compound dies designed and built in our plant. The halves are riveted together and the hubs welded in by MIG welders on turning and holding fixtures designed and built in our plant. They require no balancing and are easily adapted to standard or special uses.
- The standard sheave is 14 gauge and has the same part number regardless of hub design. Standard hubs have a keyway and two set screw holes tapped with N.C. threads. Please order pulley number with hub number.
- Other hubs are available, including special bore sizes, splines and tapers.
- Specials are produced in 14 gauge, 13 gauge and 11 gauge with combinations of hub lengths and bores to 1 1/2" diameter. Hubs are machined from 2", 2 1/8" and 2 1/2" diameter steel bar stock. Bores can be tapered with keyways, tapered keyways, broached splines, hex bores, metric bores or dimensions, pin holes or other special shapes and combinations. Pulleys can be trimmed and mounted on the same hub for step cone effect or speed change, also with double row ball bearing hubs.
- Most of these pulleys are available with a 6 1/2" diameter flat area in the center for punching a bolt hole arrangement to bolt on a customer's hub.

**bearings/index.html**

- These bearings are used in a wide range of applications, including grain augers, farm equipment, wheels, conveyors, lawn mowers and idler pulleys. They have been used at speeds up to and exceeding 2500 RPM in uses such as V-belt tightener pulleys.
- They are made primarily for straight radial service; due to deep ball grooves they are also used for thrust loads. Ball raceways are machine formed to a smooth finish, and outer races are stamped and coined from cold rolled steel, then heat treated. They contain a full complement of balls and are furnished either shielded and grease packed or shielded and grease packed with neoprene seals.


The supplied rendered unground bearings page and asset inventory contain no bearing-specific photo or drawing, so the bearings page has no source image to reproduce.
