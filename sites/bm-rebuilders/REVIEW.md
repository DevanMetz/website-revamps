# Live review

## Initial review

- P1: The mobile menu contains only the four top-level links; a buyer cannot choose a service from it. The desktop rail has the same limitation, and service pages have no direct route to another service. See `/workspace/shots/rev2/bm-rebuilders/baseline-390-services-fastener-equipment-rebuilding.png` and `baseline-1440-services-fastener-equipment-rebuilding.png`.
- P1: On mobile the contact form precedes the actual phone and email details, burying the fastest contact method below a long form. See `baseline-390-contact.png`.
- P2: The hero stretches 200-pixel source photos into large desktop tiles, making the images visibly soft and cropping machinery. Gallery images also use fixed crops that can remove parts of a machine. See `baseline-1440-home.png` and `baseline-1440-services-fastener-equipment-rebuilding.png`.
- P2: Gallery captions are 14px and the rail contact links are 14px, both too small for comfortable reading. The red “No.” labels are source image filenames, not documented job numbers. See `baseline-1440-services-fastener-equipment-rebuilding.png`.
- P2: Adjacent links in generated markup have no separating whitespace, causing labels to run together in text-only output. The 404 and shop pages lack an explicit way back near the top.
- P3: The source site's small images constrain gallery quality; enlarging them cannot recover detail. The fifth hero photo is hidden but still included in the page.

## Loop 1

- Added all eight services to the desktop and mobile navigation, with the current service marked; added Home links to shop, contact and 404. Contact details now come before the form on mobile. Gallery photos retain their proportions and use source-sized columns; captions and rail contact details are larger. Removed misleading filename numbers and the hidden fifth hero image. Separated adjacent links in generated HTML.
- Built and checked successfully, deployed, and opened every route at 1440 and 390. No document overflow or failed visible images; the menu opened and Escape closed it, and empty form submission was blocked. See `loop1-1440-home.png`, `loop1-390-contact.png`, and `loop1-390-services-fastener-equipment-rebuilding.png` in `/workspace/shots/rev2/bm-rebuilders/`.
- Remaining: the newly added sibling list is too tall on mobile and repeats the complete navigation. Menu toggle still says Menu when open. Address these in the next loop.

## Loop 2

- Removed the redundant sibling list that crowded the service pages; the complete nested service navigation and the top “All services” link remain. The mobile toggle now says Close when open, and Escape returns focus to it. Versioned CSS and JavaScript URLs so returning visitors receive the changes.
- Rebuilt and checked all 12 HTML pages and 18 redirects, then deployed. Revisited all pages at 1440×900 and 390×844, including 404; inspected screenshots in `/workspace/shots/rev2/bm-rebuilders/loop2-1440-sheet.jpg` and `loop2-390-sheet.jpg`, plus individual viewport shots. The mobile tool-room and 404 pages were retried after one network-idle timeout and loaded successfully.
- Clicked all 12 main navigation links at both widths; tested the mobile toggle, keyboard tab, close button and Escape; checked the nested navigation accessibility tree. All 92 gallery image URLs returned images at both widths. Checked the form's required fields and captured the composed mailto address, subject and all seven values; no message was sent. The mailto navigation produces the expected browser `ERR_ABORTED` in this headless environment because no email client is installed. No page errors, broken loaded images or horizontal overflow were found. Checked three old paths live: each returned 301. Built HTML contains zero adjacent `</a><a` or `</a><button` patterns.
- Remaining: the original photos are low resolution, and their different proportions make some gallery rows uneven; source-sized images preserve the full machinery rather than enlarging or cropping it. Mailto still depends on a visitor having an email application configured.

## Round 2

- P1: The press gallery spreads 200px photographs across four widely separated columns. Portraits and landscapes leave large holes, and image links only open the same small file. See `/workspace/shots/rev2/bm-rebuilders/round2-baseline-1440-services-press-rebuilding.png`.
- P2: The home hero occupies only 300px of height, making its photo mosaic feel like a strip next to the oversized dark block. Service cards are similarly restricted to 200px. See `/workspace/shots/rev2/bm-rebuilders/round2-baseline-1440-home.png`.
- P2: The fixed rail is useful for moving between services, but its dense service list needs a more obvious current state and enough space to remain readable. See `/workspace/shots/rev2/bm-rebuilders/round2-baseline-1440-services-press-rebuilding.png`.
- P3: Mobile service pages have a clear contact action and an All services link, but the original images remain intrinsically small and differ greatly in shape. See `/workspace/shots/rev2/bm-rebuilders/round2-baseline-390-services-press-rebuilding.png`.

### Round 2 Loop 1

- Enlarged the home mosaic and service card photos, changed desktop galleries to a three-column work board with source-proportion images capped at 1.5× their original width, removed links to identical image files, and strengthened the selected service in the rail.
- Built and checked successfully, deployed, and revisited all 12 routes at both widths. No page errors, failed requests, broken images or horizontal overflow were reported. See `/workspace/shots/rev2/bm-rebuilders/round2-loop1-1440-home.png`, `round2-loop1-1440-services-press-rebuilding.png`, and `round2-loop1-390-services-press-rebuilding.png`.
- Remaining: some home card crops cut into portrait machinery; mobile gallery rows still leave uneven gaps around portrait images. Source photos remain small and soft at their enlarged sizes.

### Round 2 Loop 2

- Selected landscape source photos for service cards where available, avoiding the worst portrait crops. Changed the mobile galleries to compact two-column work boards and made the current mobile service more visible.
- Rebuilt and checked all 12 pages and 18 redirects, deployed, and revisited all routes at 1440×900 and 390×844. See `/workspace/shots/rev2/bm-rebuilders/round2-loop2-1440-home.png`, `round2-loop2-1440-services-press-rebuilding.png`, `round2-loop2-390-services-press-rebuilding.png`, and the two `round2-loop2-*-sheet.jpg` overview files. No page errors, failed page requests, broken images, or horizontal overflow appeared in the page sweep.
- Clicked all 12 main navigation links at both widths; checked mobile tab focus, close button and Escape. Empty inquiry submission was blocked; a completed submission produced the correct mailto address, subject and seven answers at both widths. Footer contact targets were checked, three old URLs returned 301, and generated HTML contains no adjacent `</a><a` or `</a><button` patterns. The navigation accessibility snapshot presents separate nested links.
- Remaining: original photos are low resolution, so some look soft even within the 1.5× limit. The mailto form requires an email application. Gallery columns follow vertical reading order and have naturally uneven bottoms.
