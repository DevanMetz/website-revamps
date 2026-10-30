# Live review

## Initial review

- **P1 — Product pages are dead ends and undersell the work.** The valves page uses small photos inside large fixed wells and offers no direct route to other families. See `/workspace/shots/rev2/crosbie-foundry/initial-1440-products-valves.png`.
- **P1 — Navigation labels run together.** The desktop Products and Services links appear joined; generated markup also has adjacent links without whitespace. See `/workspace/shots/rev2/crosbie-foundry/initial-1440-home.png`.
- **P2 — Hero photo meets the right edge abruptly.** Its offset makes it look accidentally clipped rather than composed within the page. See `/workspace/shots/rev2/crosbie-foundry/initial-1440-home.png`.
- **P2 — Product captions are difficult to read.** Small caps shrink their apparent size; dark wells around different shaped photos also draw attention away from the castings. See `/workspace/shots/rev2/crosbie-foundry/initial-1440-home.png`.
- **P2 — Mobile navigation and alloy table need a closer usability check.** The product list is nested visually but the rest of the navigation is not a list; the table scroll affordance is only a border. See `/workspace/shots/rev2/crosbie-foundry/initial-mobile-menu.png` and `/workspace/shots/rev2/crosbie-foundry/initial-390-alloys.png`.

## Loop 1

Fixed the hero alignment, legible product captions, separated navigation labels, sticky header, structured mobile navigation, and product family links. Replaced fixed gallery wells with larger uncropped photographs. Built and deployed; checked all routes at both widths, including the 404, image loading, overflow, menu close/Escape and the quote form. Live screenshots include `/workspace/shots/rev2/crosbie-foundry/loop1-1440-home.png`, `/workspace/shots/rev2/crosbie-foundry/loop1-1440-products-valves.png`, `/workspace/shots/rev2/crosbie-foundry/loop1-390-products-valves.png`, and `/workspace/shots/rev2/crosbie-foundry/loop1-mobile-menu.png`.

Remaining: the mobile family links wrap into a tall block before the photos; the alloy table needs a clearer scroll cue. Check that the smallest source images cannot be enlarged past their source limit.

## Loop 2

Made the mobile family row compact, kept the current family visible, added a visible cue for the scrollable alloys table, and let the gallery accommodate different photo proportions without cropping. Removed an old CSS override that enlarged the smallest photographs beyond their source size. Built, checked and deployed the final changes.

Verified the live routes at 1440 and 390, including the 404, no horizontal page overflow, loaded images, and the quote form's required fields and mailto address, subject and body. Clicked desktop and mobile navigation and every gallery image; checked keyboard opening, Escape, button closing, accessible navigation text, table scrolling, footer destinations and representative 301 redirects. The only failed browser request was the expected mailto handoff in headless Chromium. Built HTML has zero adjacent `</a><a` or `</a><button` sequences. See `/workspace/shots/rev2/crosbie-foundry/verified-1440-products-golf-plaques.png`, `/workspace/shots/rev2/crosbie-foundry/verified-1440-products-decorative-tiles.png`, `/workspace/shots/rev2/crosbie-foundry/verified-390-products-valves.png`, `/workspace/shots/rev2/crosbie-foundry/verified-390-alloys.png`, and `/workspace/shots/rev2/crosbie-foundry/verified-390-home.png`.

Remaining: the two original tile installation photos are very small and visibly softer than the other photographs; they are capped at 1.25 times their source width, so their uneven sizes leave some open space. The quote remains a mailto handoff and depends on the buyer having an email application configured.

## Round 2

- **P1 — Family navigation competes with the examples.** At desktop width the family links wrap into two uneven lines and push the gallery down; the quote action is below the pictures. See `/workspace/shots/rev2/crosbie-foundry/baseline-1440-products-valves-viewport.png`.
- **P2 — The hero feels unbalanced.** The valve photograph is small and low on the right, surrounded by a large empty patch. See `/workspace/shots/rev2/crosbie-foundry/baseline-1440-home-viewport.png`.
- **P2 — Navigation is too small for regular use.** The desktop menu uses 12px lettering; the flask table also has a distracting right-hand rule. See `/workspace/shots/rev2/crosbie-foundry/baseline-1440-home.png`.
- **P2 — Product photography lacks a clear rhythm.** Differing image proportions and sparse captions make some families feel thin; the source photographs constrain how large they can be shown. See `/workspace/shots/rev2/crosbie-foundry/baseline-1440-products-decorative-tiles.png`.

### Round 2 Loop 1

Rebuilt and deployed a larger hero photo, 15px navigation, a vertical desktop family rail, a compact mobile family row, an earlier quote action, and a clean flask table edge. Checked every route at both widths; no page overflow or script errors appeared. See `/workspace/shots/rev2/crosbie-foundry/round2-loop1-1440-sheet.jpg`, `/workspace/shots/rev2/crosbie-foundry/round2-loop1-390-sheet.jpg`, and `/workspace/shots/rev2/crosbie-foundry/round2-loop1-1440-products-valves-viewport.png`.

Remaining: the hero photo still sits a little low, and column-flow puts the tiny tile installation photos beside the first large photo rather than after the two large photographs. Lazy images below the initial viewport need a scroll before checking their load state.

### Round 2 Loop 2

Rebuilt and deployed the adjusted hero alignment, ordered gallery grid, and larger footer and form labels. The live pass covered every page at 1440 and 390, all main and mobile navigation links, family photo links, family navigation, footer links, keyboard menu controls, required form validation and the complete mailto URL. The alloys table scrolls at 390; representative old paths return 301; the actual missing-page response is 404. No page overflow or script errors were found at 390 or 1440, and the built HTML has no adjacent link/button sequences. Screenshots: `/workspace/shots/rev2/crosbie-foundry/round2-loop2-1440-sheet.jpg`, `/workspace/shots/rev2/crosbie-foundry/round2-loop2-390-sheet.jpg`, `/workspace/shots/rev2/crosbie-foundry/round2-loop2-1440-products-decorative-tiles.png`, and `/workspace/shots/rev2/crosbie-foundry/round2-loop2-390-menu.png`.

Remaining: an extra 320px check found that the footer email makes the two-column footer overflow. The two installation photos remain small and soft because the originals are only 150px and 197px wide. The quote still requires a configured email application.

### Round 2 Loop 3

Fixed the narrow footer by stacking its columns below 380px, rebuilt, checked and deployed. Revisited all pages at 1440 and 390 and checked the family and footer links, table scroll and 404 again; no horizontal overflow at 320, 390, 768, 1024 or 1440. See `/workspace/shots/rev2/crosbie-foundry/round2-loop3-320-footer.png`, `/workspace/shots/rev2/crosbie-foundry/round2-loop3-1440-sheet.jpg`, and `/workspace/shots/rev2/crosbie-foundry/round2-loop3-390-sheet.jpg`. Lazy golf images were separately scrolled into view and decoded in the interaction pass. The limitations on the small original tile photos and mailto handoff remain.
