# Purpose

Visitors are buyers and OEMs selecting pressed-steel idler pulleys, drive pulleys, or unground bearings for a belt-driven application.

1. Find the right family, dimensions and part number.
2. Request a quote or contact Don Dye with part numbers and quantities.
3. Download the catalog for reference.

## Findings and decisions

- On the live preview, home → Single Row → Flat Idler → Request a quote took three clicks; the table contains 21 parts. The same route worked at 1440 and 390 pixels. The mobile menu opened and closed with Escape, and the form prepared an email draft.
- Single and double row pages placed several paragraphs before the first dimensions table; on mobile this delayed the main selection task. Keep the specifications and drawings, but put the product details after the tables.
- Repeated quote links appeared beside each table. Use one quote action after the product tables instead; keep Contact in the navigation and the home quote action.
- Keep the family links and catalog on home, the mobile table scroll cue and sticky part number, and all existing dimension data. Remove the repeated home catalog link and quote band.
- Drive pulleys are built to order for OEMs with minimum volumes, so retain that context and the hub information before their groove tables.

## Images

- 12 used images were converted from white to transparency: three product photos (hero, single row, drive) by edge removal, and nine technical drawings by color-to-alpha in src/build.py, which keeps every dimension line and label.
- 0 used images were transparent in the source.
- 0 product, drawing or logo images remain on a white box.
- No photographs are used. The bearing family has no supplied bearing image, so its card is set as type.
- Originals are in img-originals/assets/img/ and reference/img/images/.
