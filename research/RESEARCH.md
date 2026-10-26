# Stage 0: research a brand into a kit

Input: a company name, a URL or a codebase. Output: `brands/<id>/brand.json` (valid against `brand.schema.json`), `brands/<id>/assets/ui/*.png` (real captures), a truths list, and 5-8 product moments for SPEC.md section 2.
Rule: marketing copy is not the product. A film written only from a marketing site was rejected once. Prefer docs, the changelog, and the real app. Every truth needs a source (URL or file:line).

Setup: `ID=tidewell; mkdir -p brands/$ID/assets/{ui,brand,fonts} research/$ID; cp brands/demo/brand.json brands/$ID/brand.json`

## Mode A: website (name or URL only)
1. Name only: search for the official site and its docs/changelog/press URLs. Do not guess URLs.
2. Fetch home, product, pricing, docs index, changelog/blog (your agent's web fetch tool or curl; for JS-rendered sites use Playwright):
   `npx playwright screenshot --full-page --device-scale-factor=2 https://site.com research/$ID/home.png`
3. Logo as SVG: inline `<svg>` in the header (`document.querySelector('header svg').outerHTML`), `/logo.svg`, `/favicon.svg`, or the press/brand page. Save to `assets/brand/mark.svg`. Never redraw or approximate it; copy exact colours.
4. Fonts: `curl -s https://site.com | grep -oE 'https://[^"]+\.css'`, then read the CSS for `@font-face` and Google Fonts `family=` links. Download only fonts with an open licence (OFL, Apache); otherwise pick the closest open font and note it in `design.look`.
5. Colours: count hex frequency in the site CSS and prefer custom properties:
   `curl -s <css-url> | grep -oiE '#[0-9a-f]{6}\b' | tr A-F a-f | sort | uniq -c | sort -rn | head -15`
   `curl -s <css-url> | grep -oE '\-\-[a-z0-9-]+:\s*[^;]+' | head -40`
   Map to bg, ink, accent, paper, brand in `palettes`.
6. Voice and tone: read 10 headlines and button labels. Note sentence vs title case, banned or favoured words, emoji use. Fill `copy` and `design.never`.
7. Truths: list what the product actually does, one line each with a source URL, taken from docs and changelog first. Put what you are sure of in `truths.may_claim`; put pricing, integrations or features you could not confirm in `never_claim`.
8. Real UI: take docs screenshots, public product pages, or the live app if there is a demo or free tier (Playwright, 2x). Save as `assets/ui/<screen>.png`. Do not use stock mockups from the marketing hero as "the app".

## Mode B: codebase (most accurate)
1. Features: read `README`, `docs/`, `CHANGELOG`, and the tests (tests name real behaviour). Write the truths list with `file:line` sources.
2. Screens: list routes. Next.js: `find app pages -name 'page.*' -o -name '*.tsx' -path '*pages*'`; React Router: `grep -rn "path=" src`; others: the router file. Pick the 5-8 screens a customer sees most.
3. Design tokens: `tailwind.config.*`, `globals.css`, `theme.*`, `:root` custom properties (`grep -rn "^\s*--" src/**/*.css`). Copy exact values into `palettes` and `fonts`; font files usually sit in `public/fonts` or come from `next/font`.
4. Logo: the brand/logo component or `public/*.svg`. Copy the SVG verbatim to `assets/brand/mark.svg` and take colours from the file.
5. Run the app locally with seed data (`docker compose up`, `npm run seed`, or the repo's dev script). Use fictional data only: no real customer names, emails or messages.
6. Capture every key screen at 2x with Playwright into `assets/ui/`:
   ```bash
   npx playwright screenshot --device-scale-factor=2 --viewport-size=430,932 --wait-for-timeout=1500 http://localhost:3000/inbox brands/$ID/assets/ui/inbox.png
   ```
   Use a phone viewport for mobile screens, 1440x900 for desktop. Dark and light modes if both exist.
7. CLI tool: run the real commands and record the output (`asciinema rec`, or `cmd 2>&1 | tee research/$ID/run.txt` and render that text in a styled terminal component). Never invent output.

## Finish (both modes)
1. Fill `brands/$ID/brand.json`: id, name, tagline, palettes, fonts, logo, cast (fictional people only), story (beats, sampleThread, sampleAsk), truths, voice, copy, design, ui.
2. Validate: `python3 -c "import json,jsonschema;jsonschema.validate(json.load(open('brands/$ID/brand.json')),json.load(open('brand.schema.json')));print('ok')"` (`pip install jsonschema`).
3. Check every `ui` path exists: `python3 -c "import json,os;b=json.load(open('brands/$ID/brand.json'));[print('missing',v) for v in b['ui'].values() if isinstance(v,str) and not os.path.exists('brands/$ID/'+v)]"`.
4. Write 5-8 product moments. Each is one real screen plus one on-screen line, e.g. `inbox.png: "Every message, answered."`. The line must be a claim from your truths list. These feed SPEC.md section 2.
5. Start the film: `scripts/new-film.sh $ID ./work/<film> 16x9`.
