# logo-wheel (A31)

A static wordmark and one line on the left; on the right, one slot where logos rotate in, hold and rotate out, forever. Built for looping README banners and "works with" / "integrates with" moments. The loop is seamless: the wheel position is periodic, so the last frame leads into the first.

Variables (`data-composition-variables`):
- `lead`: the wordmark text (uses `--font-display`, `--ink`).
- `line`: the supporting line under it.
- `items`: JSON array of `{ "src": "<logo svg/png>", "label": "<name>" }`, at least 2.
- `hold`: seconds each logo sits still (default 1.2).
- `turn`: seconds for each rotation between logos (default 1.2). Loop length = items x (hold + turn).

Motion: the slot turns on a wheel with motion blur and dips through dark on the turn, so flashcheck passes (a fast bright swap failed at 4 flashes/s). Logos fill >= 55 % of the banner height. Exact logo files only, with sources noted in the brand's `assets/logos/SOURCES.md`.

Formats: built for the `banner` preset (1920x600); 16:9 reuses the row layout, vertical stacks.

SFX: a soft tick or whoosh at the start of each turn if the film has sound; silent for README banners.
