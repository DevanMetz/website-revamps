# Heat Transfer Systems: art direction

**Read:** a St. Louis ASME Code fabricator of heat exchangers, pressure vessels and waste-heat recovery equipment, founded 1980. Real fabrication photography (banners) and a drilling video exist. It should feel like an industrial photo essay: big real photos and terse captions.

- **Type:** Chivo (display and body, 800 for h1/h2, 400 body) with Chivo Mono (photo captions, data plates, small labels).
- **Palette** (from the logo and banners): carbon `#231f20`, steel `#6d686a`, mill white `#f3f2f2`, warm silver `#d8d2d4` (primary action and focus).
- **Hero:** a full-bleed photo. A real banner photo fills the viewport width at about 78vh with a bottom-weighted dark scrim (a solid-to-transparent black scrim, not a colored gradient). The h1 and actions sit bottom-left, with a mono caption plate bottom-right naming what the photo shows (only if it is known from the source; otherwise omit it).
- **Nav:** transparent over the photo, with the original dark logo on a white field and links in white. It becomes a solid carbon sticky bar after scrolling past the hero (small JS with IntersectionObserver; respect reduced motion). Inner pages start solid.
- **Grid and rhythm:** 1240px max. Capabilities alternate full-bleed photo rows with narrow text columns. 120px sections.
- **Cards:** none. Use photo-led rows with mono index numbers.
- **Signature detail:** mono data-plate captions on photos, like a stamped equipment nameplate (1px warm silver border, uppercase mono).

## Logo

The original site displays the graphic monogram and stacked name from https://heattransfersys.com/img/HTS-square.png (108 × 120 pixels). The unmodified transparent original is saved at `img-originals/logo/original.png`; the displayed copy is upscaled 2× with Lanczos, preserving the full artwork and its transparency. The opaque artwork is `#231f20`; white is the display field, not a logo color. The carbon palette uses that exact ink, with warm silver derived from its neutral hue for actions and rules.
