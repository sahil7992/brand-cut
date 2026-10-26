/* hf.js - tiny shared runtime for brandcut scenes (loaded by index.html before any scene).
 * window.HF: BW/BH (canvas px), fmt ("16x9"|"9x16"|"1x1"|"4x5"), vert/land/square flags, pick({"16x9":a,"9x16":b,...,def}),
 * clamp/lerp/ramp/smooth, rng(seed) (mulberry32: the only randomness allowed). Brand data lives in window.BRAND.
 */
(function () {
  const F = (window.BRAND && window.BRAND.format) || { id: "16x9", w: 1920, h: 1080 };
  const HF = (window.HF = window.HF || {});
  Object.assign(HF, {
    fmt: F.id, BW: F.w, BH: F.h, ZOOM: 1, DPR: 1,
    land: F.w > F.h, vert: F.h > F.w * 1.4, square: F.w === F.h, feed: F.id === "4x5",
    pick: (o) => (o[F.id] !== undefined ? o[F.id] : o.def),
    clamp: (x, a = 0, b = 1) => Math.min(b, Math.max(a, x)),
    lerp: (a, b, x) => a + (b - a) * x,
    ramp: (x, a, b) => HF.clamp((x - a) / (b - a)),
    smooth: (x) => x * x * (3 - 2 * x),
    rng(seed) {
      let a = seed >>> 0;
      return () => {
        a = (a + 0x6d2b79f5) >>> 0;
        let t = Math.imul(a ^ (a >>> 15), 1 | a);
        t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
      };
    },
  });
})();
