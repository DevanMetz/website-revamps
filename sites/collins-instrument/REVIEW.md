# Review

## Initial live inspection

- P1: The seven desktop navigation cells use tiny type, and mobile hides the phone number. Product pages have no nearby route back to the product list or their siblings. See `/workspace/shots/rev2/collins-instrument/initial-1440-home.png` and `/workspace/shots/rev2/collins-instrument/initial-390-grounding-rings.png`.
- P1: The 404 page is a copy of the contact form, with no explanation or obvious route back. See `/workspace/shots/rev2/collins-instrument/initial-1440-missing-page.png`.
- P2: The home grid gives small, mixed-size original photos large empty boxes and adds meaningless numbers. See `/workspace/shots/rev2/collins-instrument/initial-1440-home.png`.
- P2: Five miniature valve drawings are squeezed into one desktop row, making the line work hard to inspect. See `/workspace/shots/rev2/collins-instrument/initial-1440-fittings-valves.png`.
- P2: Wide specification tables scroll on mobile without a visible indication. See `/workspace/shots/rev2/collins-instrument/initial-390-isolating-flanges.png`.
- P3: Some supporting text and table typography is undersized; adjacent generated links have no text whitespace. See `/workspace/shots/rev2/collins-instrument/initial-1440-control-valves.png`.

Both forms validated required fields and generated mailto requests with the expected recipient and subjects. Images loaded and no page-level overflow was detected in the initial pass.

## Loop 1

Deployed the compact product index, larger desktop navigation, mobile call link, product return link, table-scroll cue, larger supporting type and a useful 404. Live checks at both sizes found all images loaded, no page overflow, working required-field validation and expected mailto requests. Screenshots: `/workspace/shots/rev2/collins-instrument/loop1-1440-home.png`, `/workspace/shots/rev2/collins-instrument/loop1-1440-fittings-valves.png`, `/workspace/shots/rev2/collins-instrument/loop1-390-home.png`, `/workspace/shots/rev2/collins-instrument/loop1-390-fittings-valves.png`.

Remaining: two tall images overflow their cells; mobile header order is awkward; the menu button does not say Close when open.

## Loop 2

Deployed constraints that keep the tall photos and drawings inside their cells, corrected mobile header order, and changed the menu label to Close while expanded. Live screenshots at both sizes show the corrections: `/workspace/shots/rev2/collins-instrument/loop2-390-home.png`, `/workspace/shots/rev2/collins-instrument/loop2-390-fittings-valves.png`, `/workspace/shots/rev2/collins-instrument/loop2-1440-fittings-valves.png`, and `/workspace/shots/rev2/collins-instrument/loop2-390-menu.png`. Revisited all pages at both widths: images loaded, page widths fit, required form validation worked, and each form produced a mailto with the correct recipient, subject and entered fields. The menu opened and closed by button and Escape. Its accessibility snapshot presents separate links and nested valve sections. Four sampled legacy URLs returned 301. Static build and checks passed; generated HTML contains no adjacent `</a><a` or `</a><button` sequences.

Remaining: the original photos and drawings are small and some are soft, especially the parts and machining images; the long valve specification page still requires substantial scrolling and wide tables require horizontal scrolling on phones. Mailto submission depends on the visitor having an email application configured.

A further live click pass exercised 113 desktop and 140 mobile links, including menu links and document/image targets. The automated pointer pass could not click the deliberately off-screen skip link; it is intended to appear on keyboard focus. Tab moved from the open menu button to the first navigation link, and Escape returned focus to the button.

## Round 2

### Initial critique

- P1: The desktop navigation is small and several product names wrap; it is difficult to scan for a specific product. `/workspace/shots/rev2/collins-instrument/initial2-1440-home.png`.
- P1: The mobile title block puts the drawing and company facts between the main action and products, consuming nearly the entire first screen. `/workspace/shots/rev2/collins-instrument/initial2-390-home.png`.
- P1: Product pages have a return link but no nearby sibling product links; buyers must reopen the menu or return home to compare. `/workspace/shots/rev2/collins-instrument/initial2-390-grounding-rings.png`.
- P2: Product thumbnails are confined to short horizontal rows, especially the tall control valve, making the products harder to identify. `/workspace/shots/rev2/collins-instrument/initial2-1440-home.png`.
- P2: The desktop product page split leaves substantial empty space around small source images. The original images are low resolution, so they cannot simply be enlarged indefinitely. `/workspace/shots/rev2/collins-instrument/initial2-1440-valve-parts-trim.png`.

### Round 2 Loop 1

Rebuilt and deployed larger product images in a ruled grid, a shorter title block, single-line 15px desktop navigation, and sibling links on product pages. The live browser pass at 1440 and 390 found no page overflow or JavaScript errors, and the menu closed with Escape. See `/workspace/shots/rev2/collins-instrument/round2loop1-1440-sheet.jpg` and `/workspace/shots/rev2/collins-instrument/round2loop1-390-sheet.jpg`. The mobile home drawing is intentionally hidden; the image check reported it as unloaded because the browser deferred that hidden image. Remaining: sibling links at the foot of the long valve page are too remote, and desktop image columns leave too much unused space.

### Round 2 Loop 2

Moved the sibling product links immediately below each product title and narrowed the desktop image column. Rebuilt, passed the static checker and deployed. Live inspection at 1440 and 390 showed the sibling links and the contact actions on each product page, with no page overflow or JavaScript errors. See `/workspace/shots/rev2/collins-instrument/round2loop2-1440-sheet.jpg` and `/workspace/shots/rev2/collins-instrument/round2loop2-390-sheet.jpg`. A subsequent intermediate-width check found that the wider desktop navigation overflowed at 768 and 1024 pixels; that required another fix.

### Round 2 Loop 3

Switched to the complete mobile navigation at intermediate widths and made sibling links at least 44px high on mobile. Rebuilt, passed checks and deployed. Live viewport checks show no page overflow at 320, 390, 768, 1024 or 1440. Revisited every page at 390 and 1440, including the 404; screenshots are `/workspace/shots/rev2/collins-instrument/round2loop3-1440-sheet.jpg` and `/workspace/shots/rev2/collins-instrument/round2loop3-390-sheet.jpg`. The detailed product, drawing and table views are `/workspace/shots/rev2/collins-instrument/round2loop3-1440-details.jpg`, `/workspace/shots/rev2/collins-instrument/round2loop3-390-details.jpg`, and the loaded drawing views `/workspace/shots/rev2/collins-instrument/round2loop3-1440-models-loaded.png` and `/workspace/shots/rev2/collins-instrument/round2loop3-390-models-loaded.png`. The first detail screenshots were captured before lazy images finished loading; the loaded drawing views confirm they appear.

The menu closes by button and Escape, and Tab reaches its first link. The sibling navigation accessibility snapshot has separate list items; body text checks and generated HTML show no joined adjacent links. Both forms rejected empty submissions and generated mailto navigation with the expected recipient, subject and entered values. The valve tables fit on desktop and scroll within their labelled regions on mobile. Four sampled old paths returned 301. A desktop link pass exercised 149 links; the off-screen skip link cannot be pointer-clicked until focused. The mobile link pass reached every page but its script timed out on the final form click; a separate browser test successfully submitted that form. No email was sent.

Remaining: original photos and drawings are small and soft; machining and trim images in particular cannot be made much larger without quality loss. Wide specification tables require horizontal scrolling on phones, and mailto forms depend on an email application.
