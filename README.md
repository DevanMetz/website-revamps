# Website revamps

Redesigned websites for 11 small manufacturers, one folder per company.

| Company | Folder | Live preview |
|---|---|---|
| B.M. Rebuilders, Inc. | [sites/bm-rebuilders](sites/bm-rebuilders) | https://bm-rebuilders-redesign.metzdevan.workers.dev |
| Collins Instrument Company, Inc. | [sites/collins-instrument](sites/collins-instrument) | https://collins-instrument-redesign.metzdevan.workers.dev |
| Crosbie Foundry | [sites/crosbie-foundry](sites/crosbie-foundry) | https://crosbie-foundry-redesign.metzdevan.workers.dev |
| Don Dye Company, Inc. | [sites/don-dye-company](sites/don-dye-company) | https://don-dye-company-redesign.metzdevan.workers.dev |
| Fontana Machine & Engineering Co. | [sites/fontana-machine](sites/fontana-machine) | https://fontana-machine-redesign.metzdevan.workers.dev |
| Garzo Products | [sites/garzo-products](sites/garzo-products) | https://garzo-products-redesign.metzdevan.workers.dev |
| Grant Riveters | [sites/grant-riveters](sites/grant-riveters) | https://grant-riveters-redesign.metzdevan.workers.dev |
| Has-Mor Industries, Inc. | [sites/has-mor-industries](sites/has-mor-industries) | https://has-mor-industries-redesign.metzdevan.workers.dev |
| Heat Transfer Systems, Inc. | [sites/heat-transfer-systems](sites/heat-transfer-systems) | https://heat-transfer-systems-redesign.metzdevan.workers.dev |
| Stevens Wire Products, Inc. | [sites/stevens-wire-products](sites/stevens-wire-products) | https://stevens-wire-products-redesign.metzdevan.workers.dev |
| Taylor Industries Inc. | [sites/taylor-industries](sites/taylor-industries) | https://taylor-industries-redesign.metzdevan.workers.dev |

## How each folder is built

Each folder in `sites/` is self-contained. `site/` is the finished static website and can be uploaded to any static host. `src/` holds the Python build: `data.py` is the content, `build.py` writes `site/`, and `check.py` checks the output. To rebuild, run `python3 src/build.py` and `python3 src/check.py` from inside the folder. Each preview runs as a Cloudflare Worker serving `site/` as static assets, deployed with `npx wrangler deploy` from the folder.

## License

The code (build scripts, templates and styles) is MIT licensed; see `LICENSE`. Each company's own text, logos, photos and trademarks remain theirs.

Contact: Devan Metz, GitHub [DevanMetz](https://github.com/DevanMetz).
