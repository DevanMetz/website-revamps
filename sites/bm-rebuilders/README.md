# B.M. Rebuilders, Inc. website redesign

A redesigned website for B.M. Rebuilders, Inc..

Live preview: https://bm-rebuilders-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is.
- `src/` is the build: `data.py` holds the content, `build.py` generates `site/`, and `check.py` checks the result. `src/assets/` holds the source images, archived page HTML, styles, scripts, and fonts that the build draws on.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Hosting it yourself

Upload the contents of `site/` to any static web host. No server-side code or database is needed.

To host on Cloudflare instead, run `npx wrangler deploy` in this folder. Change `name` in `wrangler.jsonc` first if you want a different Worker name.

While this is a preview, every page carries a `noindex` tag so search engines skip it. Before launching on the real domain, remove the preview noindex meta tag and `X-Robots-Tag` header, and replace the `robots.txt` crawl block. These are generated in `src/build.py`.

The floating "Upgrade my website" button and the `/keep/` page it opens are preview-only: set `PREVIEW_SUBSCRIBE_URL = ''` in `src/data.py` and rebuild to remove both.

## Editing content

Edit content and templates in `src/data.py` and `src/build.py`, and styles or scripts in `src/assets/`. Do not edit generated files in `site/`. Then run this from the folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow and beautifulsoup4. The updated site is written to `site/`.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of B.M. Rebuilders, Inc..

## Contact

Hosting and ongoing management are available for $20/month. Contact Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
