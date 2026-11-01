# Crosbie Foundry website redesign

A redesigned website for Crosbie Foundry.

Live preview: https://crosbie-foundry-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is.
- `src/` is the build: `data.py` holds product and alloy data, `build.py` contains the page templates and other copy and generates `site/`, and `check.py` checks the result. `src/assets/` holds the shared CSS, JavaScript, fonts, and original images and text that the build draws on. `keep.py` generates the preview upgrade page.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Hosting it yourself

Upload the contents of `site/` to any static web host. No server-side code or database is needed.

To host on Cloudflare instead, run `npx wrangler deploy` in this folder. Change `name` in `wrangler.jsonc` first if you want a different Worker name.

While this is a preview, every page carries a `noindex` tag, `_headers` sends `X-Robots-Tag: noindex`, and `robots.txt` disallows crawling. Remove those preview restrictions before the site goes live on your own domain.

The floating "Upgrade my website" button and the `/keep/` page it opens are preview-only: set `PREVIEW_SUBSCRIBE_URL = ''` in `src/data.py` and rebuild to remove both.

## Editing content

Edit content in `src/data.py` or `src/build.py`, styles in `src/assets/css/site.css`, and interactions in `src/assets/js/site.js`. Do not edit generated files in `site/`. Then run this from the folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow and beautifulsoup4. The updated site is written to `site/`.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of Crosbie Foundry.

## Contact

Hosting and ongoing management are available for $20/month. Contact Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
