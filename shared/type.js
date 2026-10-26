/* type.js - kinetic display type. General Sans 500/600, sentence case, accent word = COLOUR only (never another font, never italic).
 *
 *   const T = HF.type.line(parentEl, "Meet *Tidewell.*\nYour assistant.", {
 *     size: 190, weight: 600, color: "#F7EDE4", accent: "#FFB38A",   // accent = colour of every *starred* word
 *     tl, at: S.at(11.5),            // timeline + TIMELINE position (S.at(rootSec))
 *     dur: 0.9, stagger: 0.09, from: "up" | "down" | "left" | "right", depth: 260, blur: 18,
 *     drift: 6,                      // seconds the whole block keeps drifting (scale 1 -> 1.05, y -14) after the entrance
 *     align: "left" | "center", lh: 0.98, track: -0.045 })
 *   -> { el, words: [spans], lines: [divs] }
 *   HF.type.out(tl, T.words, S.at(17.9), { dur: .35 })      blur/slide out
 * The container is position:relative; place it with your own wrapper (left/top/width). Text is sentence case: never pass uppercase.
 */
(function () {
  function build(parent, text, o) {
    const root = document.createElement("div");
    root.className = "ty";
    Object.assign(root.style, {
      position: "relative", fontFamily: "var(--font-display)", fontWeight: String(o.weight ?? 600), fontSize: (o.size ?? 120) + "px",
      lineHeight: String(o.lh ?? 1), letterSpacing: (o.track ?? -0.04) + "em", color: o.color ?? "#F7EDE4", textAlign: o.align ?? "left",
      perspective: (o.persp ?? 1400) + "px", perspectiveOrigin: "50% 50%", fontStyle: "normal", textTransform: "none", whiteSpace: "nowrap",
    });
    root.setAttribute("data-layout-allow-overlap", "");
    root.setAttribute("data-layout-allow-overflow", "");
    const words = [], lines = [];
    let acc = false;
    text.split("\n").forEach((ln) => {
      const row = document.createElement("div");
      row.className = "ty-ln"; row.style.display = "block"; row.style.transformStyle = "preserve-3d";
      ln.split(" ").forEach((w, i, arr) => {
        const open = w.startsWith("*"), close = w.endsWith("*") && w.length > 0;
        if (open) acc = true;
        const core = w.replace(/^\*/, "").replace(/\*$/, "");
        const sp = document.createElement("span");
        sp.className = "ty-w"; sp.textContent = core;
        sp.setAttribute("data-layout-allow-overlap", ""); sp.setAttribute("data-layout-allow-overflow", "");
        Object.assign(sp.style, { display: "inline-block", willChange: "transform, filter, opacity", marginRight: i < arr.length - 1 ? "0.26em" : "0", ...(acc ? { color: o.accent ?? "#FFB38A" } : {}) });
        if (close) acc = false;
        row.appendChild(sp); words.push(sp);
      });
      root.appendChild(row); lines.push(row);
    });
    parent.appendChild(root);
    return { el: root, words, lines };
  }
  const FROM = { up: { y: 1 }, down: { y: -1 }, left: { x: 1 }, right: { x: -1 } };
  HF.type = {
    line(parent, text, o = {}) {
      const T = build(parent, text, o), tl = o.tl, at = o.at ?? 0;
      if (!tl) return T;
      const dir = FROM[o.from ?? "up"], d = o.dur ?? 0.9, dist = (o.dist ?? 0.55) * (o.size ?? 120);
      const fromVars = { opacity: 0, filter: `blur(${o.blur ?? 18}px)`, z: -(o.depth ?? 260), rotationX: dir.y ? 14 * dir.y : 0, x: (dir.x || 0) * dist, y: (dir.y || 0) * dist };
      T.words.forEach((w, i) => {
        tl.fromTo(w, fromVars, { opacity: 1, filter: "blur(0px)", z: 0, rotationX: 0, x: 0, y: 0, duration: d, ease: "expo.out" }, at + i * (o.stagger ?? 0.09));
      });
      if (o.drift) tl.fromTo(T.el, { scale: 1, y: 0 }, { scale: 1.05, y: -14, duration: o.drift, ease: "none" }, at);
      return T;
    },
    out(tl, words, at, o = {}) {
      tl.to(words, { opacity: 0, filter: `blur(${o.blur ?? 14}px)`, y: o.y ?? -24, z: o.z ?? 120, duration: o.dur ?? 0.4, ease: "power2.in", stagger: o.stagger ?? 0.03 }, at);
    },
  };
})();
