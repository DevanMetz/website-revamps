# Build brief (common rules): speculative redesign of an outdated small-manufacturer website

You are building a modern static redesign of the company's current website (named in the SITE section below). It is a
speculative pitch: the finished site must look like a credible, finished replacement that the owner could launch as-is.

## Inputs already in this folder (read them first)
- `reference/crawl-page-text.txt` - visible text of every page of the current site (crawled today with a real browser).
- `reference/pages.tsv` - every old URL path, its HTTP status and title, and `reference/html/*.html` the rendered HTML of each page (use it to see which image sits next to which text, tables, link targets, image alt text).
- `reference/assets.tsv` - every image/document downloaded: original URL -> local file under `reference/img/` (plus alt text and natural size).
- `reference/crawl-notes.txt` - requests that failed (HTTP-only / mixed-content resources, dead third parties).
- `reference/*.pdf.txt` - text of their PDFs; the PDFs themselves are in `site/assets/docs/` (link to the ones that are real product literature; delete from site/assets/docs any you do not link).
- `reference/swf/` (only some sites) - Flash files from the old site. Do not embed Flash.

## Hard content rules
- NEVER invent facts, numbers, certifications, clients, testimonials, awards, years-in-business counts, capacities or claims. Use only copy from the reference files. You may lightly trim/merge their sentences, fix obvious typos and fix grammar. Keep part numbers, sizes, specs, tables and footnotes exactly as on the site.
- Dated or time-relative claims (e.g. "over 50 years", "celebrating our 20th anniversary", "2012 prices", a copyright year, "new!" from a decade ago) must NOT be restated as current. Prefer omitting them or converting to a fixed fact that is stated in the source (e.g. "Founded 1981" only if the source says 1981). Never compute a new number.
- Prices from old pages: omit them (replace with a "Request a quote" path) unless the SITE section says otherwise.
- Keep every real product / service / capability the site lists. Drop dead links, hit counters, "best viewed in", webmaster credits, Flash notices, search/register/guestbook pages and links to defunct third-party directories.
- Contact details: use only the exact address / phone / fax / email(s) shown on the site (listed in the SITE section). JSON-LD Organization (or LocalBusiness) with only those real values.

## Design rule from Devan (important)
Cut taglines, eyebrow labels, helper text and secondary labels that aren't needed. No "Learn more" spam, no marketing filler, no invented slogans, no stat counters, no icon soup. Let layout, type, whitespace and real photos do the work. Industrial and trustworthy: calm, solid, high-contrast, generous whitespace; one accent colour at most, chosen to suit their logo/brand colours if they have any. System font stack (no web font downloads). Photos from an old site are small and low-res: never upscale a photo beyond ~1.25x its natural width; place small photos in tidy grids/cards on white or light grey wells rather than stretching them into heroes. If no photo is good enough for a hero, use a strong typographic hero (h1 + one real sentence + CTAs) on a dark solid band instead.

## Tech
- Plain static HTML/CSS/JS only, no framework, no build step needed to host. The deployable site is `site/` (served as Cloudflare Workers static assets; do not create wrangler/package files, I handle deploy).
- Generate pages with a small Python script `src/build.py` (templates, shared header/footer) reading content from `src/data.py`; run it to write `site/**/index.html`. Commit-ready output in `site/` must be complete, static and working. Use Pillow (installed) in the build script or a one-off step to copy the images you use from `reference/img/` into `site/assets/img/` with clean lowercase names, re-encoded/optimised (JPEG q~82 or WebP; keep PNG/GIF line drawings as PNG), never upscaled. Only images actually used go into `site/`.
- One CSS file `site/assets/css/site.css` (< ~25 KB), one small JS `site/assets/js/site.js` (< ~6 KB: mobile nav toggle, form handling, any lightbox/video facade). No external requests on load (no CDNs, no Google Fonts, no analytics, no hotlinked images).
- Clean URLs as folders with index.html. Sensible IA per the SITE section; merge thin pages; every real piece of content from the old site must have a home.
- Contact: a contact page with the real address / phone (tel: links) / fax / email (mailto) and a contact form, plus a quote/inquiry form if the old site had one (reproduce their questions). Forms: real `<form>` with labels, required attrs, autocomplete, and a JS submit handler that composes a `mailto:` to the company email with a subject and all answers in the body (static hosting fallback). Add an HTML comment where a real endpoint would go. Show an inline status after submit. No placeholder text that repeats the label. Never post anywhere.
- `site/_redirects` (Cloudflare format, `/old /new 301`) mapping EVERY old URL in reference/pages.tsv (and old PDF/document paths you moved) to the best new URL. Include case variants that appear in links. Skip `/` itself. Do not redirect a path to itself.
- `site/_headers`: long cache for /assets/*, basic security headers (X-Content-Type-Options, Referrer-Policy, frame-ancestors via CSP or X-Frame-Options), and `X-Robots-Tag: noindex` for /*.
- `<meta name="robots" content="noindex">` on every page (preview build; README says to remove at launch). `site/robots.txt`, `site/sitemap.xml` (use the company's real production domain). `site/404.html`.
- Per-page `<title>` and meta description from their own wording; Open Graph tags; favicon (simple SVG monogram or their logo).
- Accessibility: semantic landmarks, skip link, one h1 per page, visible focus, colour contrast AA, alt text on every content image (decorative = alt=""), `aria-current` in nav, mobile menu button with aria-expanded and Esc to close, forms fully labelled, tables with th/scope and wrapped in a focusable scroll region on mobile, reduced-motion respected, tap targets >= 44px on mobile.
- Performance: width/height on every img, lazy-load below the fold, hero image eager + fetchpriority high, no layout shift.
- Responsive: must look great at 1440px and 390px (and fine at 320, 768, 1024). No horizontal scroll on mobile.

## Deliverables in this folder
- `site/` complete static site, `src/build.py`, `src/data.py`.
- `README.md`: what it is (speculative redesign preview of <their domain>), page list, how to edit (data + build script), how to host (`npx wrangler deploy` with wrangler.jsonc, Worker + static assets), forms note (mailto fallback; production options: Cloudflare Worker/Pages Function, Formspree, or the company's existing form handler if any), the noindex note, a "Content sources" section listing every lightly edited sentence and every dated claim you omitted, and any HTTP-only / missing images noted in reference/crawl-notes.txt.
- Do NOT deploy, do not touch Cloudflare/wrangler, do not run git commands, do not send email, do not access the network.

## Verify before finishing
You cannot launch a browser in your sandbox; I take screenshots myself. Write and run a quick static checker (e.g. `src/check.py`): every internal href/src resolves to a file in site/, every page has exactly one h1, every img has alt + width + height, no external requests in HTML/CSS, redirects file well-formed and every old path covered, CSS/JS sizes. Print a short report at the end: pages created, checks run and results, anything unresolved or any content decision I should know about.

Make reasonable decisions yourself; do not ask questions; work until done.
## SITE: Collins Instrument Company, Inc. (https://collinsinst.com/)
Angleton, Texas. Plastic (PVDF/PP) control valves and valve trim for corrosive service, flareless tube fittings / miniature valves in exotic alloys, isolating flanges, grounding rings, and custom precision machining (plastics and exotic alloys, certified TIG/MIG welding).

Contact (exact): Collins Instrument Company, Inc., P.O. Box 938, Angleton, TX 77516. Tel (979) 849-8266. Fax: the site shows two numbers - (979) 848-0783 (header and contact page) and (979) 848-0733 (footer); use (979) 848-0783 and flag the discrepancy in README. Email cic@collinsinst.com (mailto forms go here).

IA:
- `/` Home: typographic hero on a dark band (h1 like "Plastic control valves and precision machining", taken from their wording) + intro paragraph from the home copy, product cards (Control Valves, Fittings & Valves, Isolating Flanges, Grounding Rings, Valve Parts & Trim, Custom Machining) with real photos, capabilities list, contact band.
- `/control-valves/` (home/pcv.pdf content + any control valve page; link the PDF), `/fittings-valves/` (+ min_valves content), `/isolating-flanges/` (+ flange_specs tables), `/grounding-rings/`, `/valve-parts-trim/`, `/custom-machining/`, `/contact/` with form.
- Reproduce every spec table exactly as accessible HTML tables.
Content decisions: "Over 50 Years" / "For over 50 years" and "more than 20 years" are 2003-era relative claims: omit them (do not convert to a founding year unless the source states one). Drop the live date widget, "Site Designed by", copyright year. Palette: industrial navy or slate with a single safety-orange or teal accent.
