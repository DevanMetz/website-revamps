# PASS 1 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.

## Real photos and video now available
I extracted the media from the old Flash files into reference/media/:
- banner-0.jpg ... banner-6.jpg (605x120 each; real shop photos from the old site's hts-banner.swf): 0 = machinists / tube sheet drilling, 1 = long white vessel on a flatbed, 2 = shell section + painting, 3 = white and black vessels outdoors, 4 = welders, 5 = crane lift + exchanger on trailer, 6 = tube-to-tubesheet welds close-ups.
- viper-drilling.mp4 (H.264, 520x290, 74 s, no audio) + viper-drilling-poster.jpg - "Viper 2 drilling" video from the old Cutting & material processing page.
Use them (copy into site/assets/; JPEGs may be re-encoded but never upscaled beyond 1.25x native width = ~756px; these are wide strips, so show them as full-content-width strips up to 756px or crop sensible panels):
1. Home: put banner-1.jpg (or banner-5) as a framed strip directly under the hero, and a 2x2/3-up photo strip (banner-0, banner-4, banner-6) in the Fabrication section.
2. Fabrication pages: cutting & material processing -> banner-0 + the Viper video; welding & assembly -> banner-4 + banner-6; testing & inspection -> banner-2 or banner-3. Heat exchangers -> banner-5; special products -> banner-3; repairs -> banner-2; photos page -> all seven strips in a gallery plus the Flickr link.
3. Video: native <video controls preload="none" playsinline poster=...> with width/height set, muted not required (no audio). Caption "Viper 2 drilling" only if that name is from the source (it is the original file name - use it as the accessible title, not a visible caption).

## Design rule fixes
4. Remove the decorative concentric-circle art in the hero.
5. Invented headings: "Built around your requirements" -> "About"; "Areas of expertise" -> "Products and services"; "Discuss your project with Heat Transfer Systems." -> "Contact". Cut the hero subline only if it is not real copy (keep it if it is the site's own sentence).
6. Remove the 01/02/03 numbers in the Fabrication row and the ↗ icons on internal cards (use → or make the whole card the link with no icon).
7. Header: 11 nav items at small size is crowded. Group the three fabrication sub-pages under a "Fabrication" item (fabrication overview page links to them), keep Engineering, Heat exchangers, Waste heat recovery, Special products, Repairs, Facility, Clients, Photos, Contact; put the phone (314) 631-3311 in the top-right. If it still does not fit at 1440 at a readable 15px, move Facility/Clients/Photos into an "About" dropdown-free overview page.
8. Mobile: hero buttons, check every page has no horizontal overflow at 390.
