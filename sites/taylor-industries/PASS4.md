# Polish pass 4 (final; reviewed pass-3 screenshots + interaction test: menu, Esc, video facade, form validation all work)
BRIEF.md rules still apply. No browser in your sandbox; edit src/build.py + CSS/JS, regenerate site/, re-run your static checker. Do NOT deploy.

1. Mobile menu (open state): rows have no separation and the phone number is missing. Give each nav row a 1px divider and 52px height, add the phone (tel link "573.893.5412") as the last row styled as a secondary action, and add a subtle bottom shadow under the open panel. Swap the ☰ icon to ✕ when open (icon aria-hidden). Lock body scroll is NOT needed.
2. Packaging page: increase space between the spec row and the "Options" heading to 40px, and between the Options list and the media row to 56px.
3. Home ECG features band (desktop): the left column is short against the 5-item list; vertically centre the left column content against the list (align-items:center) so there is no dead block bottom-left.
4. Footer: add the fax line format consistently ("Fax 573.893.3647") everywhere it appears (header aside, contact, inquiry, footer) and make footer link hit areas >= 32px tall on desktop, 44px on mobile.
5. Header on desktop: add aria-label "Call 573.893.5412" to the header phone link.
6. Print stylesheet: hide header nav, video facades and contact band; show URLs after external links. Keep it small.
7. Final copy audit: compare every visible sentence to reference/crawl-page-text.txt and reference/electrode-reference-guide.txt; list in README under "Content sources" any sentence that is a lightly edited version (typo fixes) and confirm no invented claims. Make sure README mentions: the "17 years" and "fourteen years" claims from the 2009-era copy were omitted pending confirmation; the © year was dropped; forms are mailto fallbacks; noindex must be removed at launch; hosting via `npx wrangler deploy` (Worker + static assets) using wrangler.jsonc.

Finish with a short report of what you changed.
