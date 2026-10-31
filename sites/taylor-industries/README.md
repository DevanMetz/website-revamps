# Taylor Industries Inc. website redesign

A redesigned website for Taylor Industries Inc.

Live preview: https://taylor-industries-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is. `site/assets/css/site.css` and `site/assets/js/site.js` are edited by hand; the HTML pages are generated.
- `src/` is the build: `data.py` holds the content, `build.py` generates the pages in `site/`, `keep.py` builds the `/keep/` page, and `check.py` checks the result. `make_logo.py` and `make_transparent.py` regenerate the header logo and the cut-out product photos in `src/transparent/`; they only need running when those images change.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Build and check

Edit `src/data.py` (or `build.py`), then run this from this folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow. `check.py` confirms internal links, assets, product anchors and `noindex` tags are in place.

## Preview locally

```
cd site && python3 -m http.server 8765
```

Then open http://localhost:8765.

## Deploy

Run `npx wrangler deploy` in this folder to publish `site/` to the Cloudflare Worker `taylor-industries-redesign`. Change `name` in `wrangler.jsonc` first if you want a different Worker name. The contents of `site/` can also be uploaded to any static web host; no server-side code or database is needed.

While this is a preview, every page carries a `noindex` tag so search engines skip it. That tag should come out before the site goes live on your own domain. At the same time, set `SITE_ORIGIN` in `src/data.py` to the real domain (it sets the canonical, social-share and breadcrumb URLs) and rebuild.

The floating "Upgrade my website" button and the `/keep/` page it opens are preview-only: set `PREVIEW_SUBSCRIBE_URL = ''` in `src/data.py` and rebuild to remove both.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of Taylor Industries Inc.

## Contact

Hosting and ongoing management are available for $20/month. Contact Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
