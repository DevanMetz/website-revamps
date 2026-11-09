# Vital Tone Chiropractic website redesign

A redesigned website for Vital Tone Chiropractic. All wording is carried over from https://www.vitaltonechiro.com/.

Live preview: https://vital-tone-chiro-redesign.metzdevan.workers.dev

## What's in this folder

- `site/` is the finished website: plain HTML, CSS, images and JavaScript, ready to host as is.
- `src/` is the build: `data.py` holds the facts, page meta and copy, `build.py` generates `site/`, and `check.py` checks the result. `src/assets/` holds source images, styles and scripts; `src/fonts/` holds the locally hosted fonts.
- `wrangler.jsonc` is the Cloudflare configuration used for the preview.

## Hosting it yourself

Upload the contents of `site/` to any static web host. No server-side code or database is needed.

To host on Cloudflare instead, run `npx wrangler deploy` in this folder. Change `name` in `wrangler.jsonc` first if you want a different Worker name.

While this is a preview, every page carries a `noindex` tag, `_headers` sends `X-Robots-Tag: noindex`, and `robots.txt` disallows crawling. Update all three in `src/build.py` and set `SITE_ORIGIN` in `src/data.py` before the site goes live on your own domain.

## Contact form

The form has no backend. Submitting it opens the visitor's email app with a message to info@vitaltonechiro.com containing the form fields. To collect submissions directly, replace the submit handler in `src/assets/js/site.js` with a form endpoint.

## Editing content

Edit `src/data.py`, then run this from the folder:

```
python3 src/build.py
python3 src/check.py
```

This needs Python 3 with Pillow and Beautiful Soup 4. When `reference/` is present, `check.py` also confirms that the titles, descriptions and page copy match the original site. Generated files in `site/` are overwritten by the build.

## License

The code is MIT licensed; see [LICENSE](../../LICENSE). The company's own text, logo, photos and trademarks remain the property of Vital Tone Chiropractic.
