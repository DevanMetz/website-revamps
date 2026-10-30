# PASS 2 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.
1. The Control Valves card (home) uses valves_1.jpg, which shows stainless fittings / miniature valves, not plastic control valves. Use valves_1.jpg only for Fittings & Valves. For Control Valves, extract a real product photo from site/assets/docs/pcv.pdf (`pdfimages -png` or `pdftoppm -r 150 -png` and crop with Pillow to the valve photo) and use that on the card and on /control-valves/; if the PDF has no usable photo, use a cropped render of the PDF's valve drawing. Keep the Mv_003 drawing for Fittings & Valves only if nothing better; one image per card, no duplicates.
2. Section headings that read as slogans: rename "Control for corrosive applications" to "Overview" (or drop the heading and let the intro follow the h1). Keep "Valve options" and "Specifications and selection".
3. Drop the trailing period from the home h1.
4. Small source photos (137-250px wide) are shown much larger on mobile cards. Cap displayed image width at 1.25x native (use max-width in CSS per image via width/height attrs and `max-width: min(100%, Npx)`), centred in the media box.
5. Long spec tables on /control-valves/ at 390px: confirm each is inside a scroll region with sticky first column and fade cue; the trim table's long "Flow Coefficient" cells should wrap (white-space: normal, min column width ~16ch) rather than force very wide tables.
6. Custom machining page: show all three custom_machining photos as a small gallery (native size, linked).
