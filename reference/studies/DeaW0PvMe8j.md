# DeaW0PvMe8j: ElevenLabs "One click install" (static story/post)

- Creator: @elevenlabs (Instagram). URL: https://www.instagram.com/p/DeaW0PvMe8j/ . Posted October 12, 2026.
(frames not redistributed; see the original reel)
- Source type: native graphic, no crop needed.

## Summary
A product announcement for the ElevenLabs MCP ("Eleven Agents"). Three stacked bands: a quiet off-white header with the wordmark, a headline band ("One click install" + a two-line subhead + a black "Install now" pill), and a lower half of soft, grainy plum-to-blush gradient on which a black parent pill ("ElevenLabs MCP") branches with thin rounded-elbow lines into four white child pills carrying real partner logos (Claude, ChatGPT, Hermes, Cursor), stepped diagonally down to the right.

## Layout (px on 1080x1920)
| element | rect / position | notes |
|---|---|---|
| wordmark "Eleven Agents" | x 88, y 180-225 | ~2.4% of frame height, bold "Eleven" + regular "Agents" |
| headline "One click install" | x 90, y 525-605 | ~4.2% of H cap-to-baseline 80 px, tight negative tracking (~ -3%), sentence case, black #000 |
| subhead | x 90, y 635-710 | 2 lines, ~2% of H, regular weight |
| "Install now" pill | x 877-1037, y 646-706 | black, white text, fully rounded |
| gradient field | y 824-1920 | starts at a hard horizontal edge, no feather |
| parent pill | x 104-475, y 894-982 | black, 88 px tall, radius = h/2 |
| child pills | 4 steps, each +121 px down and +120-150 px right | white, 88 px tall, logo + name |
| connector lines | 1 px, #e1c2d1 to #c08fa5 at ~60% opacity | orthogonal with ~16 px rounded elbows, one trunk per child |

Safe zone note: everything important sits between y 180 and y 1470 and x 88 to 1040. The bottom 450 px is empty gradient, which is exactly where IG/TikTok put the caption and the action column. That is a native vertical layout, not a crop.

## Palette (sampled)
- Paper: #F4F3F1 (header), #F2F1ED (headline band). The two bands differ by ~2 levels, a quiet structural seam.
- Gradient: deep plum #510B2D, mid mauve #BC98A6, pink #C18AA1, light blush-grey #C7B9B6. Visible film grain over it.
- Ink: #000000 pills and type, #FFFFFF child pills. Partner accent only from the real logos (Claude coral #D97857).

## Typography
- A neo-grotesk (ElevenLabs uses its own Eleven font family; it reads like an Inter/Suisse-class grotesk). Headline regular weight, very tight tracking, big. Subhead regular. Pills medium.
- All sentence case except the partner's own logotype (CURSOR is its real wordmark, not a styling choice).

## Why this does not look AI-generated
1. Real partner logos in their true brand form (Claude spark in coral, the OpenAI knot, Cursor's cube wordmark), not generic icons.
2. The connector lines are a real diagram language (orthogonal, consistent 1 px, consistent elbow radius), drawn by a system, not wobbly decorative curves.
3. Strict grid: one left margin (88-104 px) for wordmark, headline and the parent pill; a constant step for the children.
4. The gradient has optical grain and a soft photographic falloff, like a defocused light photo, not a clean CSS two-stop gradient.
5. Huge restraint: four elements of hierarchy, one CTA, nothing glowing, nothing sparkling.
6. The hard top edge of the gradient field is a deliberate graphic seam; AI images feather everything.
7. Copy says exactly what the product does ("Manage your voice and chat agents where you already work").

## What would make it look AI
1. Neon glowing lines or animated particles running along the connectors.
2. Invented "logo-like" icons or a purple-to-cyan gradient instead of the brand's own plum.
3. Glassmorphism on every pill with drop shadows and inner glows.
4. Centered everything, uneven steps, or text in ALL CAPS for emphasis.

## Archetypes
- **Branch connector tree (parent pill -> partner pills).** A parent pill fans out into child pills via orthogonal 1 px lines with rounded elbows, stepped diagonally. Motion version: the parent pill lands (power3.out, 0.5 s), then each trunk draws (stroke-dashoffset, 0.35 s, power2.inOut) and its child pill pops on arrival (scale 0.92 -> 1, back.out(1.4), 0.3 s), 0.12 s stagger. Flash risk: none. HyperFrames: SVG paths with `pathLength=1` and a GSAP dashoffset tween, pills as HTML. Tidewell fit: "Tidewell" pill branching into the channels and tools it already works with: SMS, WhatsApp, Calendar, DocuSign, Stripe (real logos). Strong fit for the "connected" beat and the hero end section.
- **Banded editorial layout for vertical.** Paper header + headline band + photographic gradient field, with the action in the middle third and the bottom 450 px left empty for platform UI. Use as the default 9:16 layout grammar.
- **Grain gradient field.** A defocused-light gradient with grain as a background instead of a flat colour. Build as a WebGL or layered radial-gradient canvas plus a static grain PNG at 6-10% opacity (no animated noise flicker, which reads as cheap and can add luminance flicker).

## Frames
(frames not redistributed; see the original reel)