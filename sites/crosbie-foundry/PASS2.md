# PASS 2 review (screenshots at 1440 and 390) - polish
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.
1. Home hero: remove the trailing period from the h1. At 1440 the hero is a large empty dark block - add one real casting photo on the right (the "187" golf plaque or valve castings image already in site/assets), max 1.25x native, no frame text. On mobile, hide the photo or show it below the buttons at max 1.25x native. Reduce hero vertical padding ~20%.
2. "Since 1956" section: the lead sentence "Crosbie Foundry has specialized in sand castings since 1956." repeats the heading. Rename the heading to "About the foundry" and keep the sentence as the lead, OR keep "Since 1956" and drop the lead - choose the first.
3. Applications list on /products/: flow all groups through balanced CSS columns (column-count 3 desktop, 2 tablet, 1 mobile, break-inside: avoid on each group heading + its first items) so the Bronze column isn't twice as long as the others.
4. Flask sizes section: the left column has only a heading and a link; put the "View alloys" link under the table and let the table sit next to the heading, or make the section a single column with the table at max-width 560px.
5. Check all internal links use → and only external links use ↗.
