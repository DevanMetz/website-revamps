# Grant Riveters website redesign

A redesigned website for Grant Riveters.

Live preview: https://grant-riveters-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is.
- `src/` is the build: `data.py` holds the content, `build.py` generates `site/`, and `check.py` checks the result. `src/assets/` holds source images, archived page content, CSS and JavaScript. The existing `site/assets/docs/` PDFs and `site/assets/fonts/` font files are also build inputs and must remain in place.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Hosting it yourself

Upload the contents of `site/` to any static web host. No server-side code or database is needed.

To host on Cloudflare instead, run `npx wrangler deploy` in this folder. Change `name` in `wrangler.jsonc` first if you want a different Worker name.

While this is a preview, every page carries a `noindex` tag, `_headers` sends `X-Robots-Tag: noindex`, and `robots.txt` disallows crawling. Remove all three preview restrictions in the source build before going live on your own domain.

The floating "Upgrade my website" button and the `/keep/` page it opens are preview-only: set `PREVIEW_SUBSCRIBE_URL = ''` in `src/data.py` and rebuild to remove both.

## Editing content

Edit page data in `src/data.py`, product content in `src/content/products.py`, templates in `src/build.py`, and styles or scripts in `src/assets/`. Do not edit the generated HTML, CSS or JavaScript in `site/`. Then run this from the folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow, beautifulsoup4 and numpy. The updated site is written to `site/`.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of Grant Riveters.

## Contact

Hosting and ongoing management are available for $20/month. Contact Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
