# Garzo Products website redesign

A redesigned website for Garzo Products.

Live preview: https://garzo-products-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is.
- `src/` is the build: `data.py` holds the content, `build.py` generates `site/`, and `check.py` checks the result. `src/assets/` holds source images, text, styles and scripts; `src/transparent/` holds prepared product images and `src/fonts/` holds the locally hosted fonts.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Hosting it yourself

Upload the contents of `site/` to any static web host. No server-side code or database is needed.

To host on Cloudflare instead, run `npx wrangler deploy` in this folder. Change `name` in `wrangler.jsonc` first if you want a different Worker name.

While this is a preview, every page carries a `noindex` tag, `_headers` sends `X-Robots-Tag: noindex`, and `robots.txt` disallows crawling. Update all three in `src/build.py` before the site goes live on your own domain.

The floating "Upgrade my website" button and the `/keep/` page it opens are preview-only: set `PREVIEW_SUBSCRIBE_URL = ''` in `src/data.py` and rebuild to remove both.

## Editing content

Edit `src/data.py`, then run this from the folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow and Beautiful Soup 4. The updated site is written to `site/`. Edit styles and scripts in `src/assets/css/site.css` and `src/assets/js/site.js`; generated files in `site/` are overwritten by the build.

The build also generates `_headers`: CSS and JavaScript revalidate on each visit, while images and fonts keep their one-year immutable cache.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of Garzo Products.

## Contact

Hosting and ongoing management are available for $20/month. Contact Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
