/* phone.js - a REAL phone: a cut-out of a real photo (assets/phone/phone-front.png, screen = transparent hole) with the app UI mapped into
 * the screen by a corner-pinned DOM layer (CSS matrix3d from the 4 screen corners), a glass reflection, a screen glow and a contact shadow.
 *
 *   const ph = HF.phone(container, {
 *     photo: "front",            // key in HF.phone.photos
 *     content: HF.realui.screen.home(),   // element or html; ideally a 393x852 screen (HF.realui.screen.*)
 *     x: 960, y: 560, scale: 0.5, rotate: 0,   // centre of the phone in container px (scene design px), uniform scale, degrees
 *     glow: "rgba(247,237,228,.35)" | null, shadow: "float" | "contact" | "none", reflect: 1 })
 *   ph.el      outer wrapper: tween x, y, scale, rotation, rotationX/Y, opacity with GSAP (transformPerspective is preset to 1800)
 *   ph.body    inner wrapper: used by ph.buzz()
 *   ph.screen  the 393x852 content host (replace children with ph.setContent(elOrHtml))
 *   ph.sweep(tl, at, dur)   glass reflection band sweeps across (timeline position `at`)
 *   ph.buzz(tl, at, dur=0.5, amp=1)   physical jitter of the whole phone (deterministic keyframes)
 *   ph.W, ph.H   photo size in px at scale 1 (phone is 925 x 1868; scale ~0.5 fills a 1080p frame height)
 */
(function () {
  const photos = {
    front: { src: "assets/phone/phone-front.png", w: 925, h: 1868, quad: [[44, 41], [881, 41], [881, 1831], [44, 1831]], radius: 125, cr: 55, cw: 393, ch: 852 },
  };
  /* homography: unit rect (0,0)-(w,h) -> quad q[tl,tr,br,bl]; returns a CSS matrix3d() string */
  function matrix3d(w, h, q) {
    const s = [[0, 0], [w, 0], [w, h], [0, h]], A = [], b = [];
    for (let i = 0; i < 4; i++) {
      const [x, y] = s[i], [X, Y] = q[i];
      A.push([x, y, 1, 0, 0, 0, -x * X, -y * X]); b.push(X);
      A.push([0, 0, 0, x, y, 1, -x * Y, -y * Y]); b.push(Y);
    }
    const n = 8; // gaussian elimination
    for (let c = 0; c < n; c++) {
      let p = c; for (let r = c + 1; r < n; r++) if (Math.abs(A[r][c]) > Math.abs(A[p][c])) p = r;
      [A[c], A[p]] = [A[p], A[c]]; [b[c], b[p]] = [b[p], b[c]];
      for (let r = c + 1; r < n; r++) { const f = A[r][c] / A[c][c]; for (let k = c; k < n; k++) A[r][k] -= f * A[c][k]; b[r] -= f * b[c]; }
    }
    const x = new Array(n);
    for (let r = n - 1; r >= 0; r--) { let v = b[r]; for (let k = r + 1; k < n; k++) v -= A[r][k] * x[k]; x[r] = v / A[r][r]; }
    const [a, bb, c, d, e, f, g, hh] = x;
    return `matrix3d(${a},${d},0,${g},${bb},${e},0,${hh},0,0,1,0,${c},${f},0,1)`;
  }
  function phone(container, o = {}) {
    const P = photos[o.photo || "front"], W = P.w, H = P.h;
    const el = document.createElement("div"); el.className = "ph";
    el.setAttribute("data-layout-allow-overlap", ""); el.setAttribute("data-layout-allow-overflow", "");
    const x = o.x ?? HF.BW / 2, y = o.y ?? HF.BH / 2;
    Object.assign(el.style, { position: "absolute", left: x - W / 2 + "px", top: y - H / 2 + "px", width: W + "px", height: H + "px", transformOrigin: "50% 50%" });
    const body = document.createElement("div");
    Object.assign(body.style, { position: "absolute", inset: 0, transformOrigin: "50% 50%" });
    const q = P.quad, sx = q[0][0], sy = q[0][1], sw = q[1][0] - q[0][0], sh = q[2][1] - q[1][1];
    const sh_ = o.shadow ?? "float";
    const glow = o.glow === undefined ? "rgba(255,236,226,0.28)" : o.glow;
    body.innerHTML =
      (sh_ === "none" ? "" : `<div style="position:absolute;left:6%;right:6%;top:5%;bottom:-2%;border-radius:150px;background:rgba(0,0,0,${sh_ === "float" ? 0.5 : 0.32});filter:blur(${sh_ === "float" ? 90 : 60}px);transform:translateY(${sh_ === "float" ? 110 : 40}px)"></div><div style="position:absolute;left:12%;right:12%;bottom:-60px;height:120px;border-radius:50%;background:rgba(0,0,0,0.55);filter:blur(34px)"></div>`) +
      (glow ? `<div class="ph-glow" style="position:absolute;left:-14%;right:-14%;top:-6%;bottom:-6%;border-radius:200px;background:radial-gradient(closest-side,${glow},rgba(0,0,0,0));filter:blur(50px);opacity:${o.glowOpacity ?? 1}"></div>` : "") +
      `<div class="ph-screen" style="position:absolute;left:0;top:0;width:${P.cw}px;height:${P.ch}px;transform-origin:0 0;transform:${matrix3d(P.cw, P.ch, q)};background:#000;overflow:hidden;border-radius:${P.cr}px"></div>` +
      `<img class="ph-bezel" src="${P.src}" width="${W}" height="${H}" style="position:absolute;left:0;top:0;width:${W}px;height:${H}px" />` +
      `<div class="ph-glass" style="position:absolute;left:${sx}px;top:${sy}px;width:${sw}px;height:${sh}px;border-radius:${P.radius}px;overflow:hidden;pointer-events:none;box-shadow:inset 0 0 70px rgba(0,0,0,0.28)">
         <div style="position:absolute;inset:0;background:linear-gradient(160deg,rgba(255,255,255,0.10) 0%,rgba(255,255,255,0.03) 22%,rgba(255,255,255,0) 40%)"></div>
         <div class="ph-refl" style="position:absolute;top:-30%;bottom:-30%;left:-70%;width:55%;transform:skewX(-18deg);background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,${0.16 * (o.reflect ?? 1)}) 45%,rgba(255,255,255,${0.24 * (o.reflect ?? 1)}) 52%,rgba(255,255,255,0));filter:blur(14px)"></div>
       </div>`;
    el.appendChild(body); container.appendChild(el);
    const screen = body.querySelector(".ph-screen");
    const api = {
      el, body, screen, W, H, refl: body.querySelector(".ph-refl"), glow: body.querySelector(".ph-glow"),
      setContent(c) { screen.innerHTML = ""; if (typeof c === "string") screen.innerHTML = c; else if (c) screen.appendChild(c); return api; },
      sweep(tl, at, dur = 1.6) { tl.fromTo(api.refl, { x: 0 }, { x: sw * 2.6, duration: dur, ease: "power2.inOut" }, at); return api; },
      buzz(tl, at, dur = 0.5, amp = 1) {
        const n = Math.max(4, Math.round(dur / 0.04)), r = HF.rng(7);
        for (let i = 0; i < n; i++) { const k = 1 - i / n; tl.to(body, { x: (r() - 0.5) * 16 * amp * k, y: (r() - 0.5) * 8 * amp * k, rotation: (r() - 0.5) * 1.4 * amp * k, duration: dur / n, ease: "none" }, at + (i * dur) / n); }
        tl.to(body, { x: 0, y: 0, rotation: 0, duration: 0.05, ease: "none" }, at + dur);
        return api;
      },
    };
    if (o.content) api.setContent(o.content);
    gsap.set(el, { scale: o.scale ?? 0.5, rotation: o.rotate ?? 0, transformPerspective: 1800 });
    return api;
  }
  phone.photos = photos; phone.matrix3d = matrix3d;
  HF.phone = phone;
})();
