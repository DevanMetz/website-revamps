# Polish pass 3 (reviewed pass-2 screenshots at 1440 and 390; still no overflow/console errors)
BRIEF.md rules still apply. No browser in your sandbox; edit src/build.py + CSS/JS, regenerate site/, re-run your static checker. Do NOT run wrangler or deploy.

## Responsiveness (mobile 390)
1. Product cards on mobile (<=600px): the 2-column cards wrap every line ("1.61 x 1.61" (41mm / x 41mm)") and the ECG page is ~7,700 CSS px. Switch to a single-column horizontal row layout on mobile: image 80x80 on the left, text on the right (part no. bold, size, pouch/case, cloth variant muted), 12px padding, 1px dividers or 8px gaps. Size strings must not break mid-value: wrap the mm part in a span with white-space:nowrap. Target ECG mobile page height under ~5,500 CSS px. Apply the same component to TENS, Tab, strips.
2. Spec rows on mobile: the 3 narrow columns force labels to wrap to 4 lines. Below 600px, render each spec as a row: value left (min-width ~7rem), label right, divider between rows.
3. Home hero mobile: the collage is large and pushes the categories far down; cap it at ~300px tall on mobile (object-fit: contain) or hide the lower third with tighter padding.

## Visual hierarchy
4. Home features section: remove the two tiny thumbnails added last pass (they look like broken images). Instead make the section a compact band: heading + one line + link on the left, the features list on the right, 56px vertical padding.
5. Home machines section: the "View machines →" link floats bottom-right detached from content. Place it directly under the paragraph on the left (same as other text links). Make the machine image card and the video the same height on desktop (both 16:9 wells; machine photo object-fit: contain on white).
6. Packaging page: add 32px space between the spec row and "Options"; style the Options list with the same check-list style used for ECG features instead of plain bullets.
7. Machine Inquiry aside: order = intro sentence first ("These questions are very important..."), then a divider, then company/address, phone, fax, email.

## Copy fidelity
8. The original inquiry form shows example answers; add them as `placeholder` text (they are not label repeats): largest size "e.g. 30mm x 25mm", smallest "e.g. 22mm x 25mm", raw materials "e.g. foam, cloth or a special material", largest pouch "e.g. 8 inches x 8 inches", smallest pouch "e.g. 6 inches x 4 inches", packaging material "e.g. poly paper". Use the exact example wording in reference/crawl-page-text.txt if it differs. Also make sure the final textarea label is their sentence: "Along with the answers to the above questions, please let us know any added functions you would like your machine to perform, or any other special requests or questions you may have."
9. Grep the built site for any text not traceable to the reference files (taglines, labels like "Overview" are fine as nav). Remove anything invented.

## Accessibility / performance
10. Make sure every product card image alt is meaningful ("1000ZT ECG electrode") and that the jump-link nav has aria-label; checkbox groups are in fieldsets with legends; required fields have `aria-required` implied by `required` and a visually-hidden "(required)" or the asterisk explained once at top of each form ("* Required").
11. Add `<link rel="preload" as="image" href="/assets/img/brand/electrodes-collage.webp" fetchpriority="high">` on the home page only.

## Hosting files
12. The preview will be hosted as a Cloudflare Worker with static assets (not Pages). Add `wrangler.jsonc` at the project root: name "taylor-industries-redesign", compatibility_date "2026-10-01", assets { directory: "./site", not_found_handling: "404-page", html_handling: "auto-trailing-slash" }, workers_dev true, no main script needed. Keep site/_redirects and site/_headers (Workers static assets support both; make sure _redirects uses only formats supported there: static 301s). Update README hosting section: `npx wrangler deploy` from the project root serves it on workers.dev; Pages drag-and-drop of site/ also still works.

Finish with a short report of what you changed.
