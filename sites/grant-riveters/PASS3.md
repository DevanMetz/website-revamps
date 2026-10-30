# PASS 3 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.
Product content is now clean - good. Remaining:
1. Spec tables lost rows. The pneumatic bench-top source also lists Throat depth, Shut height, Adjustable time, Overall length, Overall width, Overall height (and similar rows exist for other variants/families). Restore every spec row present in the source table for every model on every product page (check reference/html for each page's tables; rows only, no marketing). Keep units exactly as printed.
2. Mobile tables (390 px): data columns are too narrow, causing 5-line cells. Give the table min-width so each model column is at least 13ch, keep the sticky first column at ~11ch, and put the metric value on its own line (e.g. "0.118\" DIA.<br>3 mm") instead of wrapping mid-value; never break inside a number+unit (use &nbsp; between number and unit).
3. Variant layout on desktop: photo (max 1.25x native) to the left of the intro + key benefits, two columns from 900 px; table full width below. Stack on mobile, photo centred.
4. Literature links: show human labels, e.g. "Pneumatic riveters (PDF, 2.1 MB)", "Servo riveters (PDF, x MB)" - compute sizes from the files; never show raw filenames.
5. Internal "Request a quote" links use ↗ (external icon). Use → for internal links site-wide; ↗ only for links that leave the site.
6. Variant anchor links (Pneumatic / Hydraulic / Servo-electric) at top: style as a compact segmented row of buttons, sticky under the header on scroll is NOT needed.
