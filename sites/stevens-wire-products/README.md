# Stevens Wire Products, Inc. website redesign

A redesigned website for Stevens Wire Products, Inc..

Live preview: https://stevens-wire-products-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is. It also contains the brochure, fonts and favicon used by the build.
- `src/` is the build: `data.py` holds product content, `build.py` generates the pages and images, `keep.py` generates the preview funnel, and `check.py` checks the result. `src/assets/` holds the styles, JavaScript, original images and redirect inventory; `src/logo.png` and `src/transparent/` supply the logo and image cutout.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Hosting it yourself

Upload the contents of `site/` to any static web host. No server-side code or database is needed.

To host on Cloudflare instead, run `npx wrangler deploy` in this folder. Change `name` in `wrangler.jsonc` first if you want a different Worker name.

While this is a preview, every page carries a `noindex` tag, `_headers` sends `X-Robots-Tag: noindex`, and `robots.txt` disallows crawling. Update all three in the build source before launching on your own domain.

The floating "Upgrade my website" button and the `/keep/` page it opens are preview-only: set `PREVIEW_SUBSCRIBE_URL = ''` in `src/data.py` and rebuild to remove both.

## Editing content

Edit `src/data.py`, then run this from the folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow. The updated site is written to `site/`.

Edit layouts and generated hosting rules in `src/build.py`, and styles and scripts in `src/assets/`. The brochure in `site/assets/docs/`, fonts in `site/assets/fonts/`, and `site/assets/favicon.svg` are maintained directly and retained by the build. CSS and JavaScript URLs use content hashes and revalidate on each visit; images, fonts and documents keep their long-lived cache.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of Stevens Wire Products, Inc..

## Contact

Hosting and ongoing management are available for $20/month. Contact Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
