# Review

## Initial review

- P1: Desktop navigation is a line of ten tiny links beside the phone. It is difficult to scan, and mobile inner pages offer no clear route back to the wider site. Screenshot: `/workspace/shots/rev2/heat-transfer-systems/initial-1440-home.png` and `/workspace/shots/rev2/heat-transfer-systems/initial-1440-heat-exchangers.png`.
- P1: Adjacent links are emitted without whitespace, so text and assistive technology can run labels together. The mobile menu does not group pages or visibly identify the current page.
- P2: The hero photograph is visibly soft at desktop size, and its caption reads like an image description. The source banner is only 605px wide. Screenshot: `/workspace/shots/rev2/heat-transfer-systems/initial-1440-home.png`.
- P2: Numbered service labels add no information. Wide photo frames crop and enlarge the already small source banners, obscuring equipment.
- P2: Inner pages repeat labels or introductory statements and leave buyers to use the crowded header for context. Screenshot: `/workspace/shots/rev2/heat-transfer-systems/initial-1440-heat-exchangers.png`.

## Loop 1

- Replaced the crowded header links with grouped equipment, capabilities and company navigation, retained direct contact and phone access, and added Home links on inner pages. Removed the hero caption and service numbers. Kept banner photos in their original proportions in rows and galleries, with a 605px maximum width.
- Deployed and checked every route at 1440 and 390; no horizontal overflow, broken images, page errors or failed requests were reported. The visible header and home action can be seen in `/workspace/shots/rev2/heat-transfer-systems/loop1-1440-home.png` and `/workspace/shots/rev2/heat-transfer-systems/loop1-390-home.png`; inner navigation is visible in `/workspace/shots/rev2/heat-transfer-systems/loop1-1440-heat-exchangers.png`.
- Remaining: The hero is necessarily soft because the supplied banner is 605px wide. The menu button should explicitly say Close when open, and Escape should only move focus while the menu is open. A couple of inner introductions repeat their headings.

## Loop 2

- Made the menu control say Close when expanded and corrected Escape focus behavior; removed repeated introduction text on repairs and clients. Deployed and revisited all routes at desktop and mobile widths. Screenshots include `/workspace/shots/rev2/heat-transfer-systems/loop2-1440-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/loop2-390-montage.jpg`, and `/workspace/shots/rev2/heat-transfer-systems/loop2-390-menu.png`.
- Checked all ten navigation destinations by clicking at both widths, menu button and keyboard behavior, empty and completed contact form, 301 redirects, image loading, and overflow. The static checker passed and generated HTML contains no adjacent `</a><a` or `</a><button` pairs.
- Found a remaining mobile 404 defect: its inherited home header overlaps the title. Fixed in the next deployment. Hero source resolution remains the main visual limitation.

## Loop 3

- Corrected the 404 header and prioritized loading the home hero. Rebuilt, passed `src/check.py`, and deployed.
- Revisited all routes at 1440 and 390: one H1 per page, no horizontal overflow, broken images, page errors or failed requests observed. The repaired 404 is shown in `/workspace/shots/rev2/heat-transfer-systems/loop3-390-missing-page.png` and `/workspace/shots/rev2/heat-transfer-systems/loop3-1440-missing-page.png`; all first screens are recorded in the loop 3 montage screenshots.
- Captured the contact form's actual navigation: it addresses `andrew.kwong@heattransfersys.com`, has subject `Website inquiry`, and includes the entered name, email, phone and message. Empty submission is blocked by native validation. The accessibility snapshot separates header and footer link names. The tested old TEMA and cutting paths return 301 and the response retains noindex.
- Remaining: the full-bleed hero is visibly soft because the original banner is small. Better source photography would improve it. The inquiry still depends on a visitor having an email application configured.

## Round 2

- P1: At desktop width the menu hides every capability, making a buyer open a menu just to discover what the company makes. The inner pages have a Home link but no nearby routes to related capabilities. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r2initial-1440-home-viewport.png`, `/workspace/shots/rev2/heat-transfer-systems/r2initial-390-heat-exchangers-viewport.png`.
- P1: The original 605 × 120 banners are composite strips. The home rows and fabrication links display these as tiny strips in expansive rows, while the hero blows one up until it is soft and cuts off the equipment. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r2initial-1440-home.png`, `/workspace/shots/rev2/heat-transfer-systems/r2initial-390-home.png`.
- P2: Product and material lists are divided into three narrow columns on desktop and two on mobile; the small items are hard to scan. The heat exchanger product photo is another strip detached from the list. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r2initial-1440-heat-exchangers.png`, `/workspace/shots/rev2/heat-transfer-systems/r2initial-390-heat-exchangers.png`.
- P2: Several inner introductions restate their heading or the following section, and the large title bands delay useful content. Screenshot: `/workspace/shots/rev2/heat-transfer-systems/r2initial-390-waste-heat-recovery-viewport.png`.
- All routes loaded with one H1, no measured horizontal overflow or broken images at either width. The full route first screens are recorded in `/workspace/shots/rev2/heat-transfer-systems/r2initial-1440-montage.jpg` and `/workspace/shots/rev2/heat-transfer-systems/r2initial-390-montage.jpg`.

### Round 2 Loop 1

- Deployed primary desktop links, grouped related links on inner pages, larger list type with fewer columns, and individual scenes cut from the source composites. Removed the redundant strip above the heat exchanger list.
- Revisited all routes at 1440 and 390: no overflow, broken images, page errors or failed requests; screenshots: `/workspace/shots/rev2/heat-transfer-systems/r2loop1-1440-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/r2loop1-390-montage.jpg`.
- Remaining: the new scene images still render at natural width and appear too small, two product links repeat the same scene, and the hero still enlarges and crops the tiny original excessively. Address these in the next loop.

### Round 2 Loop 2

- Deployed larger individual equipment and fabrication scenes, removed the repeated scene and repeated introductory copy, and sized the hero panorama within 1.5 times its source width. The hero now shows the complete vessel, although the limited source resolution means it cannot fill a tall screen as a sharp photo.
- Revisited every page at both sizes; no broken images, horizontal overflow, page errors, or failed requests. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r2loop2-1440-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/r2loop2-390-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/r2loop2-1440-home.png`, and `/workspace/shots/rev2/heat-transfer-systems/r2loop2-390-menu-check.png`.
- Clicked internal page, footer and menu links at both sizes; tested mobile menu keyboard focus, Escape and close button. The form blocked empty submission and produced the correct mailto with all four entered fields. Accessibility snapshot separated navigation labels; generated HTML had zero adjacent link/button pairs. TEMA, WHRU and cutting redirects returned 301 with noindex headers.
- Remaining: source photography is small and several gallery images are composite strips. The inquiry depends on a configured email application. During the content review, the original construction list was found missing and is restored in the next loop.

### Round 2 Loop 3

- Restored the original ASME Section VIII and Section I, TEMA, and customer specification construction list on the heat exchanger page. Rebuilt, passed the static checker, and deployed.
- Revisited all pages live at 1440 and 390, including the 404; no broken images, horizontal overflow, page errors or failed requests. The restored list is visible in `/workspace/shots/rev2/heat-transfer-systems/r2loop3-1440-heat-exchangers.png` and `/workspace/shots/rev2/heat-transfer-systems/r2loop3-390-heat-exchangers.png`. The other first screens are in `/workspace/shots/rev2/heat-transfer-systems/r2loop3-1440-montage.jpg` and `/workspace/shots/rev2/heat-transfer-systems/r2loop3-390-montage.jpg`.
- Remaining: Better original photographs would allow a truly large, sharp photo-led hero and gallery. The static inquiry requires an email application.

## Round 3

- P1: The home hero's banner is stranded above the headline at desktop and leaves a large empty band on mobile; the small source image cannot support a large hero. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r3initial-1440-home.png`, `/workspace/shots/rev2/heat-transfer-systems/r3initial-390-home.png`.
- P2: The heat exchanger subtitle simply repeats the heading, while the waste heat subtitle delays the useful list on mobile. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r3initial-390-heat-exchangers.png`, `/workspace/shots/rev2/heat-transfer-systems/r3initial-390-waste-heat-recovery.png`.
- P2: At desktop the Menu repeats the visible equipment links, making its additional destinations less obvious. Screenshot: `/workspace/shots/rev2/heat-transfer-systems/r3initial-1440-home.png`.
- P3: Gallery photographs are very shallow composite strips; the original material limits their clarity. Screenshot: `/workspace/shots/rev2/heat-transfer-systems/r3initial-390-photos.png`.

### Round 3 Loop 1

- Replaced the composite hero strip and its empty dark band with a compact typographic hero; removed the repeated heat-exchanger subtitle, moved the waste-heat detail into its content, and limited desktop More to destinations not already in the primary bar.
- Built, passed the static checker, deployed, and viewed every route at 1440 and 390. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r3loop1-1440-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/r3loop1-390-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/r3loop1-390-home.png`, and the corresponding full-page montages. The mobile menu, close button and Escape worked; empty inquiry validation blocked submission, and a completed inquiry generated the expected mailto. No broken images, overflow, page errors or failed HTTP requests were observed.
- Remaining: Clients repeats its page title immediately as a section heading. The gallery is still constrained by the original shallow composite photographs; mailto requires an email application.

### Round 3 Loop 2

- Removed the repeated Clients heading and unused hero image/observer code. Rebuilt, passed all static checks, and deployed.
- Revisited all pages including the 404 at 1440 and 390, checked full-page and viewport screenshots, clicked the primary and menu destinations, and checked the menu with keyboard, close and Escape. Screenshots: `/workspace/shots/rev2/heat-transfer-systems/r3loop2-1440-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/r3loop2-390-montage.jpg`, `/workspace/shots/rev2/heat-transfer-systems/r3loop2-390-clients.png`, and the corresponding full-page montages. No overflow, broken images, page errors or failed HTTP resources were reported. Body text and header accessibility snapshots show distinct labels; the generated HTML has no adjacent link/button pairs.
- Empty inquiry validation and completed mailto were checked again at both widths. The facilities PDF returned 200; TEMA, WHRU and cutting redirects returned 301 and noindex. The original phone formatting was checked against the crawl.
- Remaining: Gallery photos are small composite strips from the original site, and inquiries require an email application. An additional automated attempt to click every content and footer link was interrupted by a navigation abort, so that particular exhaustive click pass was not completed; the route and menu passes succeeded.
