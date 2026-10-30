# Stevens Wire Products: art direction

**Read:** a family-owned wire forming and fabricating company in Richmond, Indiana since 1960 (founded by W. Ray Stevens Jr.). It makes baskets, racks, displays, shelving and medical wire products. It should feel linear, airy and drawn with wire: thin strokes, geometric 1960s type and lots of space.

- **Type:** Jost (display and UI, 300/500 with a light, large h1) with Lora (body copy and captions).
- **Palette** (from the old header art and building sign): Stevens navy `#233a7a` (action), wire steel `#9aa3ab`, paper `#fbfbf9`, sky `#e3eaf4`, ink `#1a2030`.
- **Hero:** type only, centered. A large light-weight Jost h1, centered, on paper, with "Request a quote" (navy) plus "Products" (text link) centered below. One continuous inline-SVG wire line (1.5px wire-steel stroke) enters from the left edge, bends around the headline block with right-angle and radius bends like formed wire, and exits right. Below the hero is a full-width strip of 4 real product photos.
- **Nav:** links separated by hairline vertical dividers (1px wire-steel), Jost uppercase 500 at 13px with 0.08em tracking. The logo is at left; the "Request a quote" outline button sits at the end. Mobile: Menu button.
- **Grid and rhythm:** 1200px max, a 3-column product grid (photo cards before the two text-only lines, per PURPOSE), 112px sections.
- **Cards:** photo on sky tint, name in Jost, and a 1px wire-steel border that turns navy on hover.
- **Signature detail:** the drawn wire line. Optional stroke-dashoffset draw-in once on load (900ms), disabled under prefers-reduced-motion.
- **Must fix:** the 390px home photo grid must have no empty slot (5 photo cards in 2 columns left a hole). Make the odd last card span both columns, or use a layout that fills evenly at every width.
