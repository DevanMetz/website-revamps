# Polish pass 1 (reviewed screenshots at 1440 and 390 of every page)
Context: BRIEF.md rules still apply (no invented facts; cut unneeded taglines/labels; industrial/medical, calm). Chromium can't launch in your sandbox; I take screenshots myself, so skip browser checks. Edit src/build.py (and CSS/JS) and regenerate site/. Re-run your link/h1/img checker at the end.

## Copy fidelity
1. Home hero: use the HOME page's own copy, not the electrodes.php copy. Lead paragraph: "Taylor Industries is your premier source for monitoring ECG / EKG electrodes, TENS electrodes and Tab electrodes." Second short line: "Our latex free, hypoallergenic electrodes are manufactured here in the United States in a wide variety of shapes, sizes and materials." Keep h1 short (e.g. "ECG, TENS & Tab electrodes" or similar, no invented slogan). CTAs: "Electrodes" primary, "Production machines" secondary. Remove the "↗" glyph from the secondary CTA.
2. Home: add the home page's custom line under the Electrodes heading or on the Custom card: "we can also help develop and manufacture custom electrodes exclusive to your company" (lightly trimmed is fine).
3. Home machines section: use the home copy: "Bring production in-house with a custom-built electrode production machine from Taylor Industries. We can provide an easy-to-operate machine that is designed and built to address your specific needs."
4. Check every page against reference/crawl-page-text.txt once more for any paraphrase that drifted from the meaning; fix it.

## Visual hierarchy
5. Home category cards: remove the lone "↗" arrows. The whole card is the link; title only, with a subtle hover/focus state (border colour + slight image scale is fine, honour reduced motion). Tighten card padding; the image well should be ~1:1 with the 100px photo shown at its native size, centred.
6. ECG machine page: drop the duplicated headings ("ECG electrode production" h2 restates the h1; the video section h2 repeats the h1). Replace the full-width "Standard machine" checklist with a 3-up spec row: big value + small label: `4.46875"` / Standard foam & cloth width; `2"` / Maximum electrode width (standard machine); `1` / Operator. Under it one line: "If you need a larger size, we can design a machine to fit your needs." Put the video beside or directly below the intro, max-width ~900px, not edge-to-edge.
7. Packaging page: same spec-row treatment from their copy: `12 ft x 5 ft` typical footprint; `8.25"` poly/foil material width; `11"` max pouch length. Options (dual pouch, in-line thermal transfer printer) as a short two-item list. Pouches photo with caption "Samples of pouches produced on the same packaging system."
8. Machine Inquiry page: remove the "Information request" h2 (redundant). Use a two-column layout on desktop: form (max ~720px) left, sticky aside right with the intro sentence "These questions are very important and help us determine what type of system will best fit your needs.", phone, fax, email. Fieldset legends styled as clear section headers with a top rule.
9. Contact page: same pattern; page hero for pages with no intro text should be compact (less vertical padding). Add their intro sentence "Please fill out the following form with your questions or comments." above the form.
10. Sub-page heroes generally: reduce height ~25% on desktop; on mobile keep padding modest.

## Spacing / typography
11. ECG/TENS product grids: denser. Desktop 4 columns (>=1200px), 3 at tablet, 2 columns on mobile (390px) — the ECG page is currently ~12,000 CSS px tall on mobile, aim for under half. Card: image (native 100px, centred, on white) then part no. as the card title (bold, 1.05rem), then size line, then pouch/case, then cloth variant in muted text. Drop the repeated "Solid Gel - Foam Monitoring Electrode" line from every card and instead state it once above the grid ("All shapes: Solid Gel - Foam Monitoring Electrode."). Keep TL225 note.
12. Jump-link chips on ECG: make them smaller/lighter (outline chips, 32px tall desktop, 44px tap targets mobile via padding) or replace with a compact select on mobile; keep anchors.
13. Body copy size min 16px on mobile; card meta text min 14px; line-length max ~68ch.

## Responsiveness / a11y / performance
14. Verify no horizontal overflow at 320px (tables in TENS/Tab pages must scroll inside a focusable `role="region"` wrapper with aria-label, or stack).
15. Mobile menu: when open, nav links are full-width 48px rows; Esc closes and returns focus to the button; button label toggles Menu/Close.
16. Footer: tidy site-map columns (Electrodes / Production machines / Company groups) instead of a flat 3-column list.
17. Keep CSS < 25KB, JS < 5KB, all imgs with width/height, below-fold lazy.

Finish with a short report of what you changed.
