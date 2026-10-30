# Polish pass 2 (reviewed pass-1 screenshots at 1440 and 390; no overflow at 320-1440, no console errors - keep it that way)
BRIEF.md rules still apply. No browser in your sandbox; edit src/build.py + CSS/JS and regenerate site/, re-run your static checker.

## Visual hierarchy / layout
1. Packaging Systems page is unbalanced: the spec row is jammed at the top of the left column with no body copy, and "Options" h2 is huge. Rebuild as: split section (left: their packager copy paragraph(s) from crawl text — standard packager runs a poly/foil material 8.25 wide, pouches up to 11 long, dual pouch, printer; right: Packager.jpg). Then the same full-width spec row component used on the ECG machine page (rule above, 3 equal columns). Then "Options" as an h3-sized heading with the two items. Then a 2-column media row: pouches.jpg figure (caption centred under the image: "Samples of pouches produced on the same packaging system.") + the video facade.
2. Video facades on both machine pages are left-aligned at ~640px with empty space to the right. Make them span the content width in a 2-column media row (with a photo/figure) or centre them at max 880px. Same 16:9 ratio. Play button: 64px circle with visible focus ring, accessible name "Play video: ECG Electrode Production Machine".
3. ECG machine page: the intro paragraphs and photo look light; increase intro text to the lead size (1.125rem) and vertically centre the photo with the text.
4. Home contact band: currently only a big heading + button. Make it a 3-part row: "Contact Taylor Industries" heading, phone (tel link) + email (mailto link) in white, and the "Contact us" button. Stack on mobile.
5. Home "ECG electrode features" section: left column has a lot of dead space under the link. Add the two real Options images (misc/cloth.jpg alt "Cloth material electrode", misc/2000ZT-with_logo.jpg alt "2000ZT electrode with logo tape") as a small pair under the link, or reduce the section's vertical padding so it reads as a compact band.
6. Machine Inquiry + Contact aside: put the aside in a light panel (pale background, 24px padding), sticky on desktop (top: header height + 24px), aligned with the top of the form's first fieldset. Add "Taylor Industries Inc., 2704 Industrial Drive, Jefferson City, MO 65109" to the aside.

## Spacing / typography
7. Base paragraph size is reading small on desktop (~15px). Set body 1.0625rem (17px) desktop / 1rem mobile, line-height 1.6; card meta 0.875rem minimum; headings use a consistent scale (h1 clamp(2.25rem,4vw,3.5rem), h2 clamp(1.6rem,2.6vw,2.25rem), h3 1.125rem).
8. Product cards (ECG/TENS/strips/tab): tighten — image well 120px tall, 16px padding, 4px gap between meta lines. Part no. title 1.0625rem bold.
9. Consistent section vertical rhythm: 72px desktop / 48px mobile; heading-to-content gap 24px.

## Responsiveness
10. Home hero mobile: CTAs stack with different widths. On <=480px make both buttons full-width, equal height 48px, 12px gap. Make sure the collage image still shows on mobile (below the copy, max-width 100%).
11. Forms on mobile: checkbox/radio controls 20px with each option row >= 44px tall; inputs 48px tall, 16px font (prevents iOS zoom).

## Accessibility / performance
12. Verify palette contrast with a quick script (WCAG AA 4.5:1 for text incl. muted text, link colour on pale backgrounds, white on accent buttons). Adjust any failing colour.
13. Ensure :focus-visible outline (3px, offset 2px) on all links/buttons/inputs/cards, including on the navy hero and blue band (use a light outline colour there).
14. Add `decoding="async"` to all non-hero images; hero collage keep eager + fetchpriority="high".

## Copy fidelity
15. Packaging copy: ensure "With a typical foot print of 12 feet x 5 feet, our simple to operate packaging system can be placed at the end of our production machine allowing the operator to inspect and package product while running the machine." and the standard-packager sentence appear essentially verbatim somewhere on the page (hero or body), not only as spec numbers.

Finish with a short report of what you changed.
