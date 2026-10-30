# Fix pass 4b — the 4a fix flipped the bug

Measured in a browser at 1440px: on product cards `document.elementFromPoint` at the Compare label returns the <details> element. Cause: in `@media(min-width:641px)` the rule `.product details{margin-top:-44px;align-self:stretch}` pulls the full-width details box up over the action row, so the Compare checkbox can't be clicked (closed AND open state; in open state it still has margin -44px since only border-top is reset).

Fix in site/assets/css/site.css (min-width:641px block), no pointer-events hacks:
- closed: `.product details:not([open]){margin-top:-44px;align-self:flex-end;width:max-content}` so it only occupies the right-hand Details toggle area, and the summary width = its content.
- open: `.product details[open]{margin-top:0;align-self:stretch;width:auto}` (the open panel flows below the Compare/Details row; summary right-aligned `justify-content:flex-end`).
- Ensure .product is flex column (it is) so align-self works; check tab/strips 2-up cards too.
- Mobile (<=640px) currently works — do not change it.
Rebuild (`python3 src/build.py`), node --check, counts 27/14/2/2.
