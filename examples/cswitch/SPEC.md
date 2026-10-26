# cswitch sample film (silent, 16:9, 12 s, 1080p60)

Brand: brands/cswitch (near-black #0B0D0C, accent green #5BE38A, Geist Mono + Geist). Silent: no VO, music or SFX.
Viewer must understand: cswitch swaps Claude Code to another saved account before the quota wall, with no restart.

| # | Time | Archetype basis | Product moment (real UI) | On-screen words | Targets |
|---|---|---|---|---|---|
| 1 | 0.0-3.4 | word-blur-in + terminal | Claude Code session stops at the limit | "Out of quota. Again." / "Claude usage limit reached." | headline 88 px, terminal text 36 px |
| 2 | 3.4-7.7 | status-stack + counter-pill | `cswitch ls` table (README output), active row slides work -> personal, `cswitch auto` output, status meter 91% -> 14% | "Rotates before the wall." | headline 88 px, table 31 px mono |
| 3 | 7.7-10.1 | terminal | Hook message `[cswitch] account rotated ...`, session keeps working | "Same session. No restart." | text 36 px |
| 4 | 10.1-12.0 | logo-sting | Wordmark + url | "cswitch", "github.com/sahil7992/cswitch" | wordmark 230 px |

Transitions: soft crossfades only, no flood frames. Truths: macOS-only, no dependencies, rotates at a threshold (default 90%), swap needs no restart. Table values are the README's own example data.
