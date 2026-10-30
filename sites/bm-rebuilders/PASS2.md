# PASS 2 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.
Note: I removed the hard-coded caption overrides for 066/068 in src/build.py - the CAPTIONS dict was correct (066 = Waterbury Toolroom Press, 067 = National 2000 MaxiPress..., 068 = Ready to deliver to the door). Do not re-add overrides.
1. Re-verify every caption pairing on every service page against the original table layout (caption cell directly above/below the image in the same column, or a rowspan text cell beside it). Fix any mismatches in CAPTIONS; leave a photo uncaptioned when the pairing is genuinely unclear.
2. Home hero still has an empty right half - make the hero single column and shorter (padding ~72px), or add one real photo as asked in PASS1 (pick 068.jpg 371x207 at native size or another photo of decent quality). Pick one; do not leave the empty half.
3. Home: the Shop band's right-hand sentence "We also have four stake bed trucks..." floats on its own - put both shop sentences in one column with a "Shop →" link, or a 2-column with a small label above each ("Machine shop" / "Field service") only if those are source terms; otherwise no labels.
4. Service page gallery: image boxes are good; make captions regular weight 15px (not bold), and ensure figures with no caption align.
5. Footer: "Elyria, Ohio" - add the full street address if the source has it; otherwise keep.
6. Mobile 390: check hero buttons and gallery (1 column, image boxes max 360px tall).
