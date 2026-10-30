# Don Dye Company, Inc. website redesign

A redesigned website for Don Dye Company, Inc..

Live preview: https://don-dye-company-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is.
- `src/` is the build: `data.py` holds the content, `build.py` generates `site/`, and `check.py` checks the result. `src/assets/` holds the original images and text from the current website that the build draws on.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Hosting it yourself

Upload the contents of `site/` to any static web host. No server-side code or database is needed.

To host on Cloudflare instead, run `npx wrangler deploy` in this folder. Change `name` in `wrangler.jsonc` first if you want a different Worker name.

While this is a preview, every page carries a `noindex` tag so search engines skip it. That tag should come out before the site goes live on your own domain.

The floating "Keep this site · $20/mo" button is preview-only: set `PREVIEW_SUBSCRIBE_URL = ''` in `src/data.py` and rebuild to remove it.

## Editing content

Edit `src/data.py`, then run this from the folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow and numpy. The updated site is written to `site/`.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of Don Dye Company, Inc..

## Contact

Hosting and ongoing management are available for $20/month. Contact Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
