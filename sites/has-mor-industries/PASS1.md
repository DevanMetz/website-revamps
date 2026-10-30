# PASS 1 review (screenshots at 1440 and 390)
Keep all BRIEF.md rules; rebuild and make src/check.py pass. Do not ask questions.

1. MOBILE OVERFLOW (bug): on /product-information/ at 390 px the page is 520 px wide - the in-page `aside nav` (How they work / Advantages / ...) is wider than the viewport. Below 900 px render it as a wrapping list (flex-wrap) or a simple stacked list at full width; make sure `min-width: 0` is set on grid children. Check every page at 390 for any element wider than the viewport (body must not scroll horizontally).
2. NO IMAGES ARE USED, but real ones exist in reference/img/images/. Use them (re-encode, never upscale beyond 1.25x):
   - 1.2.jpg (red/black encapsulated o-rings) - home hero image to the right of the h1 on desktop, below the buttons on mobile; crop away the baked-in "Teflon Encapsulated O-Rings" text if possible (crop the left ~55% showing only rings), otherwise use as-is.
   - newesto-rings.gif (custom shape o-rings) - Products section card "Custom shapes and sizes" and on product information near custom shapes.
   - staticinst.gif / dynamicinst.gif - "Installation" section on product information (static and dynamic installation drawings, captions "Static" / "Dynamic" are part of the images; no extra captions).
   - table1.gif / table2.gif - groove dimension tables (radial dynamic/static and axial static). Transcribe both into real HTML tables (Part No., Cross section W, Groove depth, Groove width, Radius R1, Diametrical clearance Smax) exactly as printed, in the Sizes/Installation section. Do not show the GIFs.
   - callout.gif - part-number explanation (T V - 214: FEP encapsulated O-Ring / O-Ring material / O-Ring size) - rebuild as an HTML definition list or small styled figure on Ordering information; o_diss.gif (ID and W dimension drawing) next to the sizes/ordering text.
   - mechseal.jpg ("Typical Mechanical Seal") and valvestem2.jpg ("Typical Valve Stem") - applications figures on product information near the "used as static seals ... valve spindles, and mechanical seals" paragraph.
   - plaque.jpg (Viton official licensee certificate) - About page next to the Viton licence sentence.
   Use descriptive alt text. Do not use 1.1.gif (old logo) or the PayPal mark.
3. Home Products cards: remove the "01..05" numbers (secondary labels). Give each card a real image where one exists (solid/hollow/square: use crops of 1.2.jpg only if it is honest; otherwise text-only cards are fine).
4. Design rule: cut the hero subline on /product-information/ ("FEP and PFA encapsulated o-rings"), and the footer tagline "Manufacturer of encapsulated o-rings". "Discuss your requirements with Has-Mor." -> "Request a quote". The home "Encapsulated o-rings" section heading duplicates the h1 - rename to "About Has-Mor".
5. Header: add phone 570-383-0185 as a tel link on desktop.
