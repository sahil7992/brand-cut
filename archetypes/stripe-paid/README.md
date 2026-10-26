# stripe-paid (A27)

## What it is
The real Tidewell receipt component (HF.realui.receipt) on a glass slab with the Stripe mark. The amount rolls for 0.6 s with jitter and locks, a card row slides in, the receipt crosses from "Requested" to "Paid" and a green Paid badge strokes its check in. Copy: Application fee, payer, card ending 4242, "Paid via Stripe".

## Sources
- Our v2 s10-fee (`videos/tidewell-motion-reel-v2-2026-10-20/compositions/s10-fee.html`: glass receipt, amount count, Processing to Paid pill, tick).
- Pulse DeOxEFsItr5 10.7-12.1 (dashboard settle with counters) and Holo Deq1nUPMqtr 39.6-41.3 (digits roll with blur): geometric-decay roll then lock to the round value (PATTERNS section 3, Counters).
- Real UI: `RU.receipt`, `RU.payRequest` copy ("Paid straight into your Stripe account").

## Duration and easing
4.2 s. Slab rise power3.out 0.9 s then sine settle; roll 0.95 to 1.55 s (power3.out curve plus seeded jitter that decays to zero, locks exactly on the value); card row expo.out 0.55 s; Requested to Paid cross 0.18 s; badge back.out(1.6) 0.5 s (small living object); tick power2.out 0.35 s; optional blur-out 0.4 s.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| label | string | "" (BRAND.story.sampleFee.label, Application fee) | fee name; keep to the real Stripe-request names |
| amount | string | "" ($50.00) | amount shown and rolled to; max $500 in the real product |
| payer | string | "" (Marcus Lee) | payer name; a BRAND.cast lead name also gets the face |
| card | string | Card ending 4242 | card row text (test number, never a real card) |
| fadeOut | boolean | true | blur out at 3.8 s |

## Formats
- 16x9: slab scaled to the frame height (about 1.6x), centred slightly low.
- 9x16 / 4x5: scaled to the safe width (x 70-940); sits inside y 270-1240.
- 1x1: min of safe width and height.
The receipt content is the same in every format (it is one real component), the slab just scales.

## Flash risk
None. No flood; the Paid badge glow is local (under 3% of the frame) and ramps over 0.5 s.

## SFX cues (local time: kind)
- 0.00: soft whoosh (slab rises)
- 0.95 to 1.55: fast digit ticks (rolling amount), decaying
- 1.55: lock tick (amount lands)
- 1.75: card slide (soft tap)
- 2.27: payment chime / ka-ching (Paid)
- 2.45: check stroke tick

## Hand-off
First frame: empty. Last frame (fadeOut false, 4.2 s): Paid receipt with badge, card row below; centred, camera settled at scale 1.0. A follow-up scene can match the badge as a shared element.

## Verified
Lint 0 errors. Snapshots 16x9 at 0.6/1.2/2.5/3.6 s (roll shows $36.99 mid-jitter at 1.2 s), 9x16 and 1x1 at 3.6 s (slab inside safe insets, nothing clipped). Demo brand (Tidewell) at 3.6 s: label, amount, payer (face and clinic address), glass tint and fonts re-theme (with payer Sam Okafor, amount $25.00). Limits: the receipt timeline strings ("Sat 11:42 AM", "Paid via Stripe") and the address come from the kit component; the demo brand's address comes from BRAND.cast.listing.
- Reviewer pass 2026-10-21: lint 0 errors; 16x9 and 9x16 snapshots plus 4x5 and 1x1 at 3.9 s; 60 fps draft renders in 16x9 and 9x16 pass flashcheck (0 flashes/s, 0 floods) and safezone PASS. Fixed: 9x16 badge overhung the right unsafe band (x over 940), slab shrunk to 0.92 and badge inset in vertical; preview.png regenerated.
