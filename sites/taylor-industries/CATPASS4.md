# Catalog fix pass 4 (bug found in browser test)

Bug: on product cards the Details <summary> cannot be clicked/tapped. `.action-row{position:absolute;bottom:16px;left:16px;right:16px}` overlays the full-width summary, so `document.elementFromPoint` at the summary centre returns the action-row / its children, not the summary (Playwright: "<div class=action-row> intercepts pointer events"). Fix it properly in site.css (and markup in src/build.py if needed) so that:
- Details summary is fully clickable at 1440, 1024, 768 and 390 px, in both closed and open state; Compare checkbox and Quote button stay clickable too.
- Layout stays as now visually: Compare at left, Details toggle at right on one row (desktop); mobile layout unchanged.
- Preferred approach: don't absolutely position over the summary. E.g. make the summary itself the right-hand item (width:max-content; margin-left:auto) and position the compare control so it doesn't cover it, or put the compare control inside a flex row with the summary using order/grid. No pointer-events hacks unless nothing else works.
- Remove duplicate/contradictory .action-row rules in site.css (there are several: margin-left:auto, margin:0, position:absolute...), leaving one coherent set.
- Also in the compare dialog there are two close buttons ("✕ Close" in header and a footer "Close"); keep the footer one only if it sits next to the primary quote button — otherwise remove it.
Run python3 src/build.py; verify counts 27/14/2/2, node --check catalog.js.
