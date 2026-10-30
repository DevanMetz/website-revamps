# Website revamps

Redesign previews for small-manufacturer websites. Each site lives in `sites/<slug>/` (`site/` static output, `src/` build scripts, `wrangler.jsonc`, `README.md`) and deploys as its own Cloudflare Worker (`<slug>-redesign`) on workers.dev. All previews are `noindex`; old `.html` paths 301 to the new pages; contact forms use `mailto:`.

| Company | Original site | Preview | Contact email |
|---|---|---|---|
| Grant Riveters | https://www.grantriveters.com/ | https://grant-riveters-redesign.metzdevan.workers.dev | sales@grantriveters.com |
| Don Dye Company, Inc. | https://dondyeco.com/ | https://don-dye-company-redesign.metzdevan.workers.dev | info@dondyeco.com |
| Collins Instrument Company, Inc. | https://collinsinst.com/ | https://collins-instrument-redesign.metzdevan.workers.dev | cic@collinsinst.com |
| Fontana Machine & Engineering Co. | https://www.fontanamachine.com/ | https://fontana-machine-redesign.metzdevan.workers.dev | info@FontanaMachine.com |
| Crosbie Foundry | https://www.crosbiefoundry.com/ | https://crosbie-foundry-redesign.metzdevan.workers.dev | crosbiefoundry@aol.com |
| Has-Mor Industries, Inc. | https://has-mor.com/ | https://has-mor-industries-redesign.metzdevan.workers.dev | Info@Has-Mor.com |
| Heat Transfer Systems, Inc. | https://heattransfersys.com/ | https://heat-transfer-systems-redesign.metzdevan.workers.dev | andrew.kwong@heattransfersys.com |
| Garzo Products | https://garzoproducts.com/ | https://garzo-products-redesign.metzdevan.workers.dev | info@garzoproducts.com |
| B.M. Rebuilders, Inc. | https://bmrebuildersinc.com/ | https://bm-rebuilders-redesign.metzdevan.workers.dev | bmrebuild@aol.com |
| Stevens Wire Products, Inc. | https://stevenswire.com/ | https://stevens-wire-products-redesign.metzdevan.workers.dev | office@stevenswire.com |
| Taylor Industries Inc. | https://www.taylor-ind.com/ | https://taylor-industries-redesign.metzdevan.workers.dev | sales@taylor-ind.com |

Build a site: `cd sites/<slug> && python3 src/build.py && python3 src/check.py`. Deploy: `npx wrangler deploy` from the site folder.

## License

The code (build scripts, templates and styles) is MIT licensed; see `LICENSE`. Each company's own text, photos, logos and trademarks remain theirs.
