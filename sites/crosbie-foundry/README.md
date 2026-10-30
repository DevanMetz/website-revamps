# Crosbie Foundry preview

A speculative static redesign preview of https://www.crosbiefoundry.com/. It includes Home, Products, eight product galleries (decorative tiles, golf plaques, corner castings, decorative hardware, clamps, cash register hardware, miscellaneous castings, valves), Services, Alloys, About, History, Contact, and a 404 page.

Preview: https://crosbie-foundry-redesign.metzdevan.workers.dev (Cloudflare Worker `crosbie-foundry-redesign`, static assets from `site/`, configured in `wrangler.jsonc`). Deploy with `npx wrangler deploy` from this folder; the local `package.json` keeps wrangler's cache inside this folder.

For hosting, configure a `wrangler.jsonc` for a Cloudflare Worker with static assets pointing to `site/`, then run `npx wrangler deploy`. This preview has not been deployed. Forms use a mailto fallback, which requires the visitor to send the composed email in their email app. For production, connect a Cloudflare Worker or Pages Function, Formspree, or the company's existing form handler if available.

The preview sends noindex headers and includes noindex metadata and a disallow rule in robots.txt. Remove those at launch and update the robots policy.

## Content sources

Content and product images come from the supplied `reference/` crawl. Light edits include: the home introduction combines the source's nonferrous green-sand casting sentences; the production paragraph combines the short-run and part-weight sentences; the service descriptions combine the listed capabilities, tooling and consultation statements; family introductions condense the corresponding gallery descriptions; the about introduction removes the relative age claim; and the history paragraphs fix capitalization and recast the Obama key as a past fact. Gallery titles describe the source product family rather than asserting a specific identity for each image. The applications and alloy table are retained from the source.

Omitted dated or time-relative material: “For over half of a century,” “many years of experience,” the historical 2–4 week average lead time, “recently” for the Obama key, the 2006 copyright and old site credits. The fixed 1956 founding date, 1991 and 2001 customer relationships, and 2009 British Open remain as past facts. The old site's links directory and navigation instructions were omitted. The crawl notes report no failed or missing image downloads.
