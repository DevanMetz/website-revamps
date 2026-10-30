# Live review

## Initial findings

- P1: The emergency pager is squeezed into a 10px mobile strip with a small target, undermining the most urgent way to reach the shop. The contact heading and large emergency block push the inquiry form down. `/workspace/shots/rev2/fontana-machine/initial-contact-390-viewport.png`
- P1: The 404 page labels its privacy link “Page not found” because its generator replaces every occurrence of the title. `/workspace/shots/rev2/fontana-machine/initial-404-1440.png`
- P2: The tiny original photos are enlarged around twice their native size and surrounded by thick grey, navy and white frames; the result is blurry, isolated pictures alongside oversized copy. `/workspace/shots/rev2/fontana-machine/initial-home-1440.png`
- P2: The mobile headline consumes most of the first screen, and the inner-page headings are oversized. Navigation omits Privacy on mobile and offers no explicit return link on inner pages. `/workspace/shots/rev2/fontana-machine/initial-home-390-viewport.png`, `/workspace/shots/rev2/fontana-machine/initial-privacy-390-viewport.png`
- P3: The home capacity strip is supported by the original copy (50 tons, over 30,000 square feet, 5 acres, CNC), but its small secondary labels are hard to read. `/workspace/shots/rev2/fontana-machine/initial-home-1440.png`
- P3: Directions and the map work, but the oversized heading delays the five routes on mobile. `/workspace/shots/rev2/fontana-machine/initial-directions-390-viewport.png`

## Loop 1

- Reduced the mobile headings, made both phone links larger targets, added a home link on inner pages, included Privacy in the menu, fixed the 404 footer label, and removed the thick frames while limiting photo enlargement to 1.5×. Kept all four capacity facts, which are supported by the original copy.
- Rebuilt and deployed. Live checks at both sizes found no horizontal overflow, missing images or page errors; empty inquiry is blocked and a filled inquiry composes the expected mailto. Menu opens and closes with the button and Escape. See `/workspace/shots/rev2/fontana-machine/loop1-home-1440.png`, `/workspace/shots/rev2/fontana-machine/loop1-home-390.png`, `/workspace/shots/rev2/fontana-machine/loop1-contact-390-viewport.png`, `/workspace/shots/rev2/fontana-machine/loop1-directions-390-viewport.png`.
- Remaining: originals are tiny and visibly low-resolution; the mobile strip now takes two rows. Check navigation and link details more thoroughly in the second pass.

## Loop 2

- Made the open menu's button say Close, removed the incorrect current-page marker from the 404, and separated the adjacent home actions in generated HTML. Rebuilt, checked and deployed; an additional deployment corrected the action whitespace found during verification.
- Revisited every live page at 1440×900 and 390×844, including the 404, and inspected the images and layout. Clicked every desktop and mobile navigation item; keyboard opening, tabbing, Escape, button closing and current-page markers worked. The form rejected empty submission and generated the expected address, subject and all six answers on filled submission. Browser navigation to the mailto is aborted by headless Chromium as expected; no email was sent. All five old paths returned 301. There was no horizontal overflow, missing image or page error, and the built HTML contains zero adjacent `</a><a` or `</a><button` pairs. See `/workspace/shots/rev2/fontana-machine/final-home-1440-viewport.png`, `/workspace/shots/rev2/fontana-machine/final-home-390-viewport.png`, `/workspace/shots/rev2/fontana-machine/final-contact-390.png`, `/workspace/shots/rev2/fontana-machine/final-directions-1440.png`, and `/workspace/shots/rev2/fontana-machine/final-404-390-viewport.png`.
- Remaining: the original photographs and map are low resolution; a future launch would benefit from new shop photography. The static inquiry depends on the visitor having a mail application configured.

## Round 2

- P1: At 390px the emergency strip takes two rows and the contact page puts a large repeated emergency block ahead of the inquiry; a buyer must scroll to start writing and the business phone is below the form. `/workspace/shots/rev2/fontana-machine/r2initial-contact-390.png`
- P2: At 1440px the three source photos sit isolated in wide rows beside much larger headings. The originals are only 114–192px wide, so enlarging them further would make them visibly worse. `/workspace/shots/rev2/fontana-machine/r2initial-home-1440.png`
- P2: The capacity strip reads like a generic dashboard and repeats the 50-ton and CNC details in the first section. All four facts are present in `reference/crawl-page-text.txt`. `/workspace/shots/rev2/fontana-machine/r2initial-home-1440.png`
- P3: The map precedes all five written routes on mobile, delaying the directions the visitor came for. `/workspace/shots/rev2/fontana-machine/r2initial-directions-390.png`

### Round 2 Loop 1

- Deployed a single-line mobile pager, smaller inner headings, an immediately visible business phone and inquiry, routes before the map on mobile, and a narrower alternating service layout. Replaced the generic stat strip with the original capacity facts in the capability paragraph.
- Revisited all five pages at both widths; screenshots include `/workspace/shots/rev2/fontana-machine/r2loop1-home-1440.png`, `/workspace/shots/rev2/fontana-machine/r2loop1-contact-390-viewport.png`, and `/workspace/shots/rev2/fontana-machine/r2loop1-directions-390.png`. Images loaded, no page errors or horizontal overflow appeared.
- Remaining: the inquiry is visually first on mobile but follows contact information in document order; correct this for keyboard and screen-reader users. Photos remain limited by the source files.

### Round 2 Loop 2

- Reordered the inquiry ahead of the contact details in the HTML, matching the mobile visual and keyboard order, and removed unused stat-band CSS. Rebuilt, passed `src/check.py`, and deployed again.
- Revisited every page including 404 at 1440 and 390; see `/workspace/shots/rev2/fontana-machine/r2final-home-1440.png`, `/workspace/shots/rev2/fontana-machine/r2final-contact-390.png`, `/workspace/shots/rev2/fontana-machine/r2final-directions-1440.png`, and `/workspace/shots/rev2/fontana-machine/r2final-404-390.png`. No overflow, missing images, failed requests or page errors were found.
- Clicked all four navigation links at both sizes, checked current markers and the mobile menu's button, tab and Escape behavior, reviewed text and navigation aria snapshots, checked footer/contact link targets and all five redirects (301). No adjacent anchor/button patterns in built HTML. Empty inquiry fails validation; filled inquiry displays its status. The mailto was captured by instrumenting the live handler and verified for address, subject and all six answers; no email was sent.
- Remaining: original photos and map are small and dated. They cannot be made substantially larger without degrading quality; new photography would materially improve the site. The inquiry requires a configured email app.

## Round 3

- P1: The contact page repeats the business phone in the header, heading, details and footer, and repeats the pager and fax as well. The inquiry separates the heading from the actual contact details on mobile. `/workspace/shots/rev2/fontana-machine/r3initial-contact-390.png`
- P2: The home headline repeats the first section heading, while a full screen of black typography hides the shop photos. The three pictures alternate positions and sizes, making the services feel scattered. `/workspace/shots/rev2/fontana-machine/r3initial-home-1440.png`
- P3: The source photographs are small and dated; the smallest has limited detail even at the current size. `/workspace/shots/rev2/fontana-machine/r3initial-home-1440.png`

### Round 3 Loop 1

- Replaced the repeated service heading with the original's production and prototype subject, shortened the poster enough to reveal the first photo, aligned the photos, and consolidated contact numbers. Rebuilt, checked and deployed.
- Live checks covered all pages at both widths, navigation, current markers, menu controls, empty and filled inquiry, images and overflow; see `/workspace/shots/rev2/fontana-machine/r3loop1-home-1440.png` and `/workspace/shots/rev2/fontana-machine/r3loop1-contact-390.png`.
- Remaining: the single pager item on the contact page is accidentally hidden by the mobile rule that hid the second strip item. The contact details also take too much vertical space before the form.

### Round 3 Loop 2

- Restored the mobile pager on Contact, compacted the contact details, and made their document order match the visual order. Rebuilt, passed `src/check.py`, and deployed.
- Revisited all five pages at 1440 and 390, including the 404. The pager, main phone and fax each appear once on Contact; the inquiry begins in the first mobile screen. Screenshots: `/workspace/shots/rev2/fontana-machine/r3loop2-home-1440.png`, `/workspace/shots/rev2/fontana-machine/r3loop2-contact-390.png`, `/workspace/shots/rev2/fontana-machine/r3loop2-directions-1440.png`, and `/workspace/shots/rev2/fontana-machine/r3loop2-sheet-390.png`.
- Clicked every navigation item at both widths; checked mobile keyboard opening, tab, Escape, close button and current marker. Checked contact and footer targets, the menu's aria snapshot, and visible text. Empty inquiry was blocked; the live handler, instrumented to capture its navigation, produced the expected mailto address, subject and six fields. No email was sent. All five old paths returned 301, and generated HTML has zero adjacent anchor/anchor or anchor/button patterns. No overflow, missing images, failed requests or page errors appeared in the browser checks.
- Remaining: the original photographs and map are small and dated; new shop photography would make the site stronger. The inquiry still relies on a configured mail app.
