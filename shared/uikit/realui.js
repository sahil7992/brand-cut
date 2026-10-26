/* realui.js - HF.realui: builders for a generic messaging app components (dark). Every builder returns an HTMLElement (append it yourself).
 * 2nd arg `z` = {zoom, style, cls}: zoom scales the component (CSS zoom, stays crisp). Components never animate; you tween them with GSAP.
 *
 *   const RU = HF.realui;
 *   RU.thread({ name:"Jordan Reyes", face:"jordan", channel:"SMS"|"WhatsApp", phone:"+1 (201) 555-0109", messages:[{from:"in"|"out", text, meta:"Tidewell · 9s", typing:true, me:true}], composer:true })
 *   RU.notif({ name, face, channel:"SMS"|"WhatsApp", text, when:"now" })
 *   RU.homeHeader({ title:"Good evening", date:"Tuesday, October 13" })
 *   RU.nextShowing({ when:"Tomorrow", status:"Confirmed", name:"Jordan", time:"11:00 AM", address:"14 Aspen Ct" })
 *   RU.stats({ leads:1, replied:38, listings:5, waiting:0, median:"9s" })      // "Last 7 days" title + list
 *   RU.brief({ name, time, address, ... })     // the Showing brief sheet; use [[phrase]] in bullets for a highlight (.ru-hl)
 *   RU.calendar({ showNew:false })             // week time-grid; the new block is .ru-ev.new (hidden until showNew); the button is .ru-btn-new
 *   RU.listing({ photo, address, city, price, beds, baths, sqft, facts:[{k:"price"|"pets"|"parking", label, value}] })   // .ru-fact[data-k] ; add class "hl" to light one
 *   RU.application({ title:"Application form", status:"Signed", via:"DocuSign" })
 *   RU.payRequest({ client:"Jordan Reyes", amount:"75.00" })     RU.receipt({ amount:"$75.00", status:"Paid", client, face })
 *   RU.approval({ name, face, channel, ago, ask, draft })        // iOS "Approve and send" item
 *   RU.chip({ photo, address, price })                           // listing chip for aerial pins
 *   RU.screen.home() / .lock({notifs}) / .brief() / .thread() / .wrap(el, {zoom})   // full 393x852 phone screens (pass to HF.phone as content)
 *   RU.avatar("Jordan Reyes", 44)  RU.mark(size)
 */
(function () {
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
  const first = (n) => String(n).trim().split(/\s+/)[0].toLowerCase();
  const I = {
    userplus: (c) => `<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="9.5" cy="8" r="3.6"/><path d="M2.8 19.5c.6-3.3 3.3-5.3 6.7-5.3 1.5 0 2.8.4 3.9 1.1"/><path d="M18 11v6M15 14h6"/></svg>`,
    bars: (c) => `<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2.4" stroke-linecap="round"><path d="M4 8h7M4 12.5h16M4 17h11"/></svg>`,
    building: (c) => `<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V8l8-4 8 4v13M2.5 21h19"/><path d="M8.5 12h1.4M14 12h1.4M8.5 16h1.4M14 16h1.4M11 21v-3h2v3"/></svg>`,
    checks: (c) => `<svg width="28" height="26" viewBox="0 0 28 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13l4.5 4.5L15 8M11 17.5 13 19.5 24 8"/></svg>`,
    clock: (c, s = 17) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>`,
    chev: (c = "#6b6a66") => `<svg width="12" height="18" viewBox="0 0 12 18" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3l6 6-6 6"/></svg>`,
    arrow: (c = "currentColor", s = 20) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>`,
    send: (c = "currentColor", s = 20) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M21 3 3 10.5l7 3 3 7z"/></svg>`,
    bell: (c = "#ededea") => `<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 17V11a6 6 0 0 1 12 0v6l1.5 2h-15zM10 21h4"/></svg>`,
    check: (c, s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>`,
    pin: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>`,
    cal: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4"/></svg>`,
    user: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4.5 20c.8-4 3.8-6 7.5-6s6.700 2 7.500 6"/></svg>`,
    phone: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.500 1.500a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>`,
    bed: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18V6M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.6"/></svg>`,
    bath: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18v2a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5zM6 12V6a2 2 0 0 1 4 0M7 19l-1 2M17 19l1 2"/></svg>`,
    ruler: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 16 16 4l4 4L8 20zM8 12l2 2M11 9l2 2M14 6l2 2"/></svg>`,
    doc: (c = "#ededea", s = 22) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l5 5v13H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/></svg>`,
    home: (c, s = 28) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11 12 4l8 7v9H4z"/><path d="M9.500 20v-6h5v6"/></svg>`,
    calt: (c, s = 28) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4M8.500 14h1M12 14h1M15.500 14h1M8.500 17h1M12 17h1"/></svg>`,
    ask: (s = 30) => `<svg width="${s}" height="${s}" viewBox="0 0 32 32"><defs><linearGradient id="rug" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3f1ee"/><stop offset=".5" stop-color="#8d8a88"/><stop offset="1" stop-color="#d8756f"/></linearGradient></defs><path d="M4 21c5-2 8-12 13-12 4 0 4 5 1 8s-1 8 5 6c-6 3-12 1-11-3 .6-2 5-6 2.500-7C11 12 11 24 4 21z" fill="url(#rug)"/></svg>`,
    inbox: (c, s = 28) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4a8 8 0 0 0-6.900 12L4 20l4.200-1.100A8 8 0 1 0 12 4z"/></svg>`,
    more: (c, s = 28) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="${c}"><circle cx="5" cy="12" r="1.700"/><circle cx="12" cy="12" r="1.700"/><circle cx="19" cy="12" r="1.700"/></svg>`,
    doc2: (c) => `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 20c3-1 4-8 7-8s1 6 4 6c1 0 2-1 3-3"/><path d="M4 21h16"/></svg>`,
    link: (c = "currentColor") => `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M10 14a4 4 0 0 0 5.700 0l3-3a4 4 0 0 0-5.700-5.700l-1 1M14 10a4 4 0 0 0-5.700 0l-3 3a4 4 0 0 0 5.700 5.700l1-1"/></svg>`,
    search: (c = "#93928e") => `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.9" stroke-linecap="round"><circle cx="11" cy="11" r="6.500"/><path d="m20 20-4-4"/></svg>`,
    cal2: (c = "currentColor") => `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4"/></svg>`,
    car: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 16V11l2-5h10l2 5v5zM3 16h18v3H3zM7 13h.01M17 13h.01"/></svg>`,
    paw: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6.500" cy="10" r="1.800"/><circle cx="10" cy="6" r="1.800"/><circle cx="14.500" cy="6" r="1.800"/><circle cx="18" cy="10" r="1.800"/><path d="M12 12c-3 0-5 3-5 5 0 2 2 2.500 5 1.500 3 1 5 .5 5-1.500 0-2-2-5-5-5z"/></svg>`,
    tag: (c = "#93928e", s = 18) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3h8v8L11 20 3 12z"/><circle cx="16" cy="8" r="1.200"/></svg>`,
  };
  const statusBar = (time = "9:41") => `<div class="ru-status"><span>${time}</span><span class="rt"><svg width="19" height="12" viewBox="0 0 19 12" fill="#fff"><rect x="0" y="8" width="3.400" height="4" rx="1"/><rect x="5" y="5.500" width="3.400" height="6.500" rx="1"/><rect x="10" y="3" width="3.400" height="9" rx="1"/><rect x="15" y="0" width="3.400" height="12" rx="1"/></svg><svg width="17" height="12" viewBox="0 0 24 17" fill="none" stroke="#fff" stroke-width="2.600" stroke-linecap="round"><path d="M2 6.500a14 14 0 0 1 20 0M6 10.500a8.500 8.500 0 0 1 12 0"/><circle cx="12" cy="15" r="1.600" fill="#fff" stroke="none"/></svg><svg width="27" height="13" viewBox="0 0 27 13"><rect x=".5" y=".5" width="22" height="12" rx="3.500" fill="none" stroke="#fff" opacity=".4"/><rect x="2" y="2" width="19" height="9" rx="2.200" fill="#fff"/><rect x="24" y="4.300" width="2" height="4.400" rx="1" fill="#fff" opacity=".45"/></svg></span></div>`;

  function mk(html, cls, z = {}) {
    const d = document.createElement("div");
    d.className = "ru " + cls + (z.cls ? " " + z.cls : "");
    d.innerHTML = html;
    if (z.zoom) d.style.zoom = z.zoom;
    if (z.style) Object.assign(d.style, z.style);
    d.setAttribute("data-layout-allow-overflow", ""); d.setAttribute("data-layout-allow-overlap", ""); d.setAttribute("data-layout-allow-occlusion", "");
    return d;
  }
  const avatarHTML = (name, size = 44, face) => `<div class="ru-av" style="width:${size}px;height:${size}px;font-size:${Math.round(size * 0.4)}px">${esc(String(name).trim()[0] || "")}<i style="position:absolute;inset:0;background:url('assets/faces/${face || first(name)}.jpg') center / cover no-repeat"></i></div>`;
  const markHTML = (s = 22) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" fill="#c96169"/><path d="M6 13c2-3 4-3 6 0s4 3 6 0" stroke="#f7ede4" stroke-width="2" stroke-linecap="round"/></svg>`;
  const hl = (s) => esc(s).replace(/\[\[(.+?)\]\]/g, '<span class="ru-hl">$1</span>');

  const RU = (HF.realui = { icons: I, statusBar, avatar: (n, s, f) => mk(avatarHTML(n, s, f), "ru-avwrap", { style: { display: "inline-block" } }).firstElementChild, mark: (s) => mk(markHTML(s), "", { style: { display: "inline-block" } }), screen: {} });

  /* ---------------- thread ---------------- */
  RU.thread = (o = {}, z) => {
    const ch = o.channel || "SMS", name = o.name || "Jordan Reyes";
    const msgs = o.messages || [
      { from: "in", text: "Hi, is 14 Aspen Court still available?", meta: "9:04 PM" },
      { from: "out", text: "Yes, it is. $2,450 a month, dogs welcome, 2-car garage. Want to see it Saturday?", meta: "Tidewell · 9s" },
    ];
    const body = msgs.map((m, i) => {
      const inner = m.typing ? '<span class="ru-typing"><i></i><i></i><i></i></span>' : hl(m.text);
      const meta = m.meta ? `<div class="ru-meta">${m.from === "out" && /Tidewell/.test(m.meta) ? markHTML(15) : ""}${esc(m.meta)}</div>` : "";
      return `<div class="ru-msg ${m.from}${m.me ? " me" : ""}" data-i="${i}"><div class="ru-b">${inner}</div>${meta}</div>`;
    }).join("");
    return mk(`<div class="hd">${avatarHTML(name, 40, o.face)}<div><div class="nm">${esc(name)}</div><div class="ch"><b>${esc(ch)}</b>${o.phone ? " · " + esc(o.phone) : ""}</div></div>${o.ai === false ? "" : `<div class="ai">${I.bars("#c8c7c3").replace('width="26" height="26"', 'width="14" height="14"')}AI on</div>`}</div><div class="bd">${body}</div>${o.composer ? '<div class="ru-composer"><span>Reply as yourself</span>' + I.arrow("#93928e", 18) + "</div>" : ""}`, "ru-thread", z);
  };
  /* ---------------- lock-screen notification ---------------- */
  RU.notif = (o = {}, z) => mk(`${avatarHTML(o.name || "Jordan Reyes", 46, o.face)}<div class="tx"><div class="top"><span class="who">${esc(o.name || "Jordan Reyes")}</span><span class="when">${esc(o.when || "now")}</span></div><div class="ch">${esc(o.channel || "SMS")}</div><div class="msg">${esc(o.text || "Is the apartment still available?")}</div></div>`, "ru-notif", z);
  /* ---------------- Home ---------------- */
  RU.homeHeader = (o = {}, z) => mk(`<div><div class="t">${esc(o.title || "Good evening")}</div><div class="s">${esc(o.date || "Tuesday, October 13")}</div></div>${I.bell()}`, "ru-homehd", z);
  RU.nextShowing = (o = {}, z) => mk(`<div class="lbl"><span>Next showing · ${esc(o.when || "Tomorrow")}</span><span class="st">${esc(o.status || "Confirmed")}</span></div><div class="nm">${esc(o.name || "Jordan")}</div><div class="wh">${esc(o.time || "11:00 AM")} · ${esc(o.address || "14 Aspen Ct")}</div><div class="row"><span class="ru-btn cream" data-k="brief">Showing brief ${I.arrow("#2e1014", 20)}</span><span class="ru-btn ghost">${I.send("#f7ede4", 20)} Directions</span></div>`, "ru-next", z);
  RU.stats = (o = {}, z) => {
    const n = (k, d) => (o[k] ?? d);
    const rows = `<div class="r" data-k="leads"><div class="ic">${I.userplus("#4299dc")}</div><div class="n num">${n("leads", 1)}</div><div class="l rose">new lead</div>${I.chev()}</div>
    <div class="r" data-k="replied"><div class="ic">${I.bars("#2dc08e")}</div><div class="n num">${n("replied", 38)}</div><div class="l">${n("replied", 38) == 1 ? "person" : "people"} Tidewell replied to<small>${I.clock("#b987e8")} Median reply <b>${esc(n("median", "9s"))}</b></small></div>${I.chev()}</div>
    <div class="r" data-k="listings"><div class="ic">${I.building("#e5b568")}</div><div class="n num">${n("listings", 5)}</div><div class="l">live listings</div>${I.chev()}</div>
    <div class="r" data-k="waiting"><div class="ic">${I.checks("#c8c7c3")}</div><div class="n num">${n("waiting", 0)}</div><div class="l">waiting on your approval</div>${I.chev()}</div>`;
    return mk(`<div class="ru-sect" style="margin-bottom:12px">Last 7 days</div><div class="ru-stats">${rows}</div>`, "ru-statswrap", z);
  };
  RU.tabbar = (o = {}, z) => {
    const on = o.on || "Home", t = (n, ic) => `<div class="tb${on === n ? " on" : ""}">${ic(on === n ? "#ededea" : "#93928e")}<span>${n}</span></div>`;
    return mk(t("Home", I.home) + t("Calendar", I.calt) + `<div class="tb${on === "Ask Tidewell" ? " on" : ""}">${I.ask(28)}<span>Ask Tidewell</span></div>` + t("Inbox", I.inbox) + t("More", I.more), "ru-tabbar", z);
  };
  /* ---------------- Showing brief ---------------- */
  RU.brief = (o = {}, z) => {
    const sec = (t, a) => `<h3>${esc(t)}</h3><ul>${a.map((x) => `<li>${hl(x)}</li>`).join("")}</ul>`;
    const S = o.sections || {
      "Who you're meeting": ["[[Relocating from Boston]] for a new job.", "Works from home three days a week."],
      "What they need": ["[[Two bedrooms]], under $2,500 a month.", "Wants to move in by [[November 1]]."],
      "Little details": ["Has a [[dog, about 40 lb]].", "Needs [[parking for one car]].", "Prefers texts after 6 PM."],
    };
    return mk(`<div class="grab"></div><div class="ttl"><h2>${esc(o.name || "Jordan Reyes")}</h2><span>Done</span></div><div class="ok">${I.check("#2dc08e", 20)} Confirmed</div><div class="big">${esc(o.time || "11:00 AM")}</div><div class="sub">${esc(o.address || "14 Aspen Ct")} · ${esc(o.rent || "$2,450/mo")} · ${esc(o.facts || "2 bd · 2 ba")}</div>${Object.entries(S).map(([k, v]) => sec(k, v)).join("")}<div class="fn">From their conversation (12 messages). Only what they actually said.</div><div class="acts"><span class="ru-btn cream">Open conversation</span><span class="ru-btn out">Directions</span></div>`, "ru-sheet", z);
  };
  /* ---------------- Calendar (web) ---------------- */
  const HUES = ["#8a5cf0", "#17a58f", "#d9487a", "#d6a021", "#34a853", "#e07a2e", "#3b82e6", "#7a8f1f", "#c04ad4", "#2aa6c9"];
  RU.calendar = (o = {}, z) => {
    const days = [["Sun", 27], ["Mon", 28], ["Tue", 29], ["Wed", 30], ["Thu", 1], ["Fri", 2], ["Sat", 3]];
    const E = [ // [day, start hour, name, address, state c|a, hue idx, side l|r]
      [1, 9, "Maya Ortiz", "18 Willow", "a", 0, "l"], [1, 9.75, "Jonah Lee", "7 Ash St", "c", 1, "r"], [1, 10.5, "Lena Olsen", "44 Grove", "c", 2, "l"], [1, 11.25, "Priya Shah", "210 River", "c", 3, "r"], [1, 12, "Theo Bell", "30 Bay St", "c", 4, "l"], [1, 12.75, "Nia Carter", "8 Bloom", "a", 5, "r"], [1, 13.5, "Sam Park", "2 Willow", "c", 6, "l"],
      [2, 9, "Ava Kim", "101 New St", "c", 6, "l"], [2, 9.75, "Leo Grant", "70 Mont", "c", 7, "r"], [2, 10.5, "Zoe Park", "12 Hamil", "c", 6, "l"], [2, 11.25, "Eli Moss", "18 Willow", "a", 9, "r"], [2, 12, "Iris Wang", "7 Ash St", "c", 2, "l"], [2, 12.75, "Noah Price", "44 Grove", "c", 3, "r"], [2, 13.5, "Rosa Vega", "210 River", "c", 4, "l"],
      [3, 9, "Felix Hart", "30 Bay St", "c", 5, "l"], [3, 9.75, "Omar Diaz", "8 Bloom", "a", 9, "r"], [3, 10.5, "Ruby Lane", "2 Willow", "c", 6, "l"], [3, 11.25, "Kai Brooks", "101 New St", "c", 7, "r"], [3, 12, "Ella Stone", "70 Mont", "c", 6, "l"], [3, 12.75, "Ivan Cole", "12 Hamil", "c", 0, "r"],
      [4, 9, "Maya Ortiz", "18 Willow", "a", 2, "l"], [4, 9.75, "Jonah Lee", "7 Ash St", "c", 3, "r"], [4, 10.5, "Lena Olsen", "44 Grove", "c", 4, "l"], [4, 11.25, "Priya Shah", "210 River", "c", 5, "r"], [4, 12, "Theo Bell", "30 Bay St", "c", 4, "l"], [4, 12.75, "Nia Carter", "8 Bloom", "a", 6, "r"], [4, 13.5, "Sam Park", "2 Willow", "c", 7, "l"],
      [5, 9, "Ava Kim", "101 New St", "c", 6, "l"], [5, 9.75, "Leo Grant", "70 Mont", "c", 0, "r"], [5, 10.5, "Zoe Park", "12 Hamil", "c", 1, "l"], [5, 11.25, "Eli Moss", "18 Willow", "a", 6, "r"], [5, 12, "Iris Wang", "7 Ash St", "c", 0, "l"], [5, 12.75, "Noah Price", "44 Grove", "c", 1, "r"], [5, 13.5, "Ivan Cole", "12 Hamil", "c", 3, "l"],
      [6, 9, "Rosa Vega", "210 River", "c", 2, "l"], [6, 9.75, "Felix Hart", "30 Bay St", "c", 3, "r"], [6, 12, "Kai Brooks", "101 New St", "c", 4, "l"], [6, 12.75, "Ella Stone", "70 Mont", "c", 6, "r"], [6, 13.5, "Ivan Cole", "12 Hamil", "c", 7, "l"],
    ];
    const HH = 86, H0 = 8, ev = (e, cls = "") => `<div class="ru-ev ${e[4] === "a" ? "aw" : ""} ${cls}" style="--c:${HUES[e[5]]};top:${(e[1] - H0) * HH + 2}px;height:66px;${e[6] === "l" ? "right:42%;left:3px" : "left:42%;right:3px"}"><div class="tm"><span>${hm(e[1])}</span><i>${e[4] === "a" ? I.clock("#fff", 11) + " Awaiting" : "Confirmed"}</i></div><b>${esc(e[2])}</b><span class="ad">${esc(e[3])}</span></div>`;
    const hm = (h) => { const hr = Math.floor(h), m = Math.round((h - hr) * 60); return `${hr > 12 ? hr - 12 : hr}:${String(m).padStart(2, "0")}`; };
    const newBlock = `<div class="ru-ev new big" style="--c:#2aa6c9;top:${(11 - H0) * HH + 4}px;height:82px;left:5px;right:5px;opacity:${o.showNew ? 1 : 0}"><div class="tm"><span>11:00 AM</span><i>Confirmed</i></div><b>Jordan Reyes</b><span class="ad">14 Aspen Ct</span></div>`;
    const dayCol = (d, i) => `<div style="display:flex;flex-direction:column"><div class="dh${i === 2 ? " today" : ""}"><span>${d[0]}</span><b>${d[1]}</b></div><div class="col${i === 0 ? " off" : ""}${i === 2 ? " today" : ""}" style="height:${7 * HH}px">${i === 0 ? "" : E.filter((e) => e[0] === i).map((e) => ev(e)).join("")}${i === 6 ? newBlock : ""}</div></div>`;
    const bodyCols = days.map(dayCol).join("");
    const tcol = `<div class="tc" style="display:flex;flex-direction:column"><div class="dh" style="border-left:0"></div><div style="position:relative;height:${7 * HH}px">${[0, 1, 2, 3, 4, 5, 6].map((k) => `<span class="h" style="top:${k * HH + 14}px">${H0 + k > 12 ? H0 + k - 12 : H0 + k}${H0 + k >= 12 ? "pm" : "am"}</span>`).join("")}</div></div>`;
    return mk(`<div class="top"><div><h1>Calendar</h1><div class="sub">Every showing in one place. Moving or confirming a showing booked from a client's thread texts them the time and asks if it works.</div></div></div>
      <div class="bar"><span class="chip rose ru-btn-new">${I.cal2("#2a1215")} New showing</span><span class="chip">Block time</span><span class="chip"><span class="mut">7</span> today <span class="mut" style="margin-left:6px">6</span> to confirm</span><div class="seg"><span>Day</span><span class="on">Week</span><span>Month</span></div></div>
      <div class="range"><span class="sq">${I.chev("#c8c7c3").replace('width="12" height="18"', 'width="9" height="13" style="transform:scaleX(-1)"')}</span><span class="sq">${I.chev("#c8c7c3").replace('width="12" height="18"', 'width="9" height="13"')}</span><span class="chip" style="height:30px">Today</span><span>Sep 27 to Oct 3, 2026</span></div>
      <div class="ru-grid">${tcol}${bodyCols}</div>`, "ru-cal", z);
  };
  /* ---------------- Listing detail panel ---------------- */
  RU.listing = (o = {}, z) => {
    const f = o.facts || [{ k: "price", label: "Rent", value: "$2,450 / mo", icon: "tag" }, { k: "pets", label: "Pets", value: "Dogs welcome", icon: "paw" }, { k: "parking", label: "Parking", value: "2-car garage", icon: "car" }];
    return mk(`<div class="ph" style="background-image:url('${o.photo || "assets/photos/home-1.jpg"}')"></div><div class="hdr"><div class="act"><i></i>Active</div><h2>${esc(o.address || "14 Aspen Court")}</h2><div class="loc">${esc(o.city || "Rutherford, NJ 07070")} · <b>${esc(o.price || "$2,450/mo")}</b></div></div><div class="facts"><div>${I.bed("#93928e")} ${o.beds || 3} beds</div><div>${I.bath("#93928e")} ${o.baths || 2} baths</div><div>${I.ruler("#93928e")} ${o.sqft || "1,800"} sqft</div></div><h4>Listing details</h4><div class="rows">${f.map((x) => `<div class="ru-fact" data-k="${x.k}"><span>${esc(x.label)}</span><b>${I[x.icon || "tag"]("#c8c7c3")}${esc(x.value)}</b></div>`).join("")}</div><div class="foot"><span class="ru-btn green">${I.cal2("#04271c")} Propose a visit</span></div>`, "ru-listing", z);
  };
  /* ---------------- Application / payment / receipt / approval ---------------- */
  RU.application = (o = {}, z) => mk(`<div class="ic">${I.doc("#ededea")}</div><div><div class="t">${esc(o.title || "Application form")}</div><div class="s">${esc(o.sub || "Sent for signature")} · ${esc(o.via || "DocuSign")}</div></div><div class="st">${I.check("#2dc08e", 18)}${esc(o.status || "Signed")}</div>`, "ru-doc", z);
  RU.payRequest = (o = {}, z) => mk(`<div class="hd"><h2>Request a payment</h2><p>Paid straight into your Stripe account. Up to $500.</p></div><div class="bd"><label>Client</label><div class="fld">${avatarHTML(o.client || "Jordan Reyes", 24)}${esc(o.client || "Jordan Reyes")}</div><label>What it is for</label><div class="opts"><div class="opt on" data-k="app"><span class="rd"></span><div><div class="t">Application fee</div><div class="s">Rental application</div></div><span class="p">$75</span></div><div class="opt"><span class="rd"></span><div><div class="t">Processing fee</div><div class="s">Paperwork and screening</div></div><span class="p">$100</span></div><div class="opt"><span class="rd"></span><div><div class="t">Initial deposit</div><div class="s">Never earnest money</div></div><span class="p">$250</span></div></div><label>Amount</label><div class="fld"><span class="mut">$</span><span class="amt">${esc(o.amount || "75.00")}</span></div></div><div class="ft"><span class="ru-btn link">${I.link("#111")} Create link</span></div>`, "ru-pay", z);
  RU.receipt = (o = {}, z) => {
    const paid = (o.status || "Paid") === "Paid";
    return mk(`<div class="k"><span>Application fee</span><span class="st" style="color:${paid ? "var(--app-green)" : "var(--app-amber)"}">${paid ? I.check("#2dc08e", 17) : I.clock("#e5b568")}${esc(o.status || "Paid")}</span></div><div class="amt num">${esc(o.amount || "$75.00")}</div><div class="who">${avatarHTML(o.client || "Jordan Reyes", 28, o.face)}${esc(o.client || "Jordan Reyes")} · 14 Aspen Court</div><div class="tl"><div><span class="dot" style="background:var(--app-text)"></span>Requested<small>Sat 11:42 AM</small></div><div><span class="dot" style="background:${paid ? "var(--app-green)" : "var(--app-dim)"}"></span>${paid ? "Paid via Stripe" : "Waiting for payment"}<small>${paid ? "Sat 11:44 AM" : ""}</small></div></div>`, "ru-rcpt", z);
  };
  RU.approval = (o = {}, z) => mk(`<div class="who">${avatarHTML(o.name || "Jordan Reyes", 54, o.face)}<b>${esc(o.name || "Jordan Reyes")}</b><small>${esc(o.channel || "SMS")} · asked ${esc(o.ago || "1h")} ago</small></div><div class="ask">${esc(o.ask || "Can I see 14 Aspen Court on Saturday at 11?")}</div><div class="lab">Tidewell's reply · edit before sending</div><div class="draft">${esc(o.draft || "Saturday at 11:00 AM works. I'll meet you out front at 14 Aspen Court.")}</div><div class="acts"><span class="dec">Decline</span><span class="ru-btn cream" data-k="approve">${I.check("#2e1014", 18)} Approve and send</span></div>`, "ru-appr", z);
  RU.chip = (o = {}, z) => mk(`<div class="th" style="background-image:url('${o.photo || "assets/photos/home-1.jpg"}')"></div><div><div class="a">${esc(o.address || "14 Aspen Court")}</div><div class="p"><b>${esc(o.price || "$2,450")}</b>/mo</div></div>`, "ru-chip", z);

  /* ---------------- full phone screens (393x852) ---------------- */
  const screen = (inner, cls = "", z) => mk(`${inner}<div class="ru-home-ind"></div>`, "ru-screen " + cls, z);
  RU.screen.wrap = (el, o = {}) => { const s = screen(statusBar(o.time || "9:41"), "", o); const w = document.createElement("div"); Object.assign(w.style, { position: "absolute", left: 0, right: 0, top: (o.top ?? 70) + "px", display: "flex", justifyContent: "center", ...(o.zoom ? { zoom: o.zoom } : {}) }); w.appendChild(el); s.appendChild(w); return s; };
  RU.screen.home = (o = {}) => {
    const s = screen(statusBar(o.time || "9:47"), "", o), col = document.createElement("div");
    Object.assign(col.style, { position: "absolute", left: "17px", right: "18px", top: "64px", display: "flex", flexDirection: "column", gap: "22px" });
    col.append(RU.homeHeader(o), RU.nextShowing(o.next), RU.stats(o.stats));
    const quiet = mk(`<div class="ru-sect" style="display:flex;justify-content:space-between;margin-bottom:6px">Gone quiet<span style="font-size:17px;font-family:var(--font-ui);font-weight:600">3</span></div><div class="r"><div><b>Rakesh Sanghvi</b><p>Hi Rakesh, I just sent you Buyer Agreement (S...</p></div><span class="mut">37d</span></div>`, "ru-gone");
    col.append(quiet); s.append(col);
    const tb = RU.tabbar({ on: "Home" }); Object.assign(tb.style, { position: "absolute", left: "17px", bottom: "26px", zIndex: 4 }); s.append(tb);
    return s;
  };
  RU.screen.lock = (o = {}) => {
    const s = screen(statusBar(o.time || "9:04"), "ru-lock", o);
    s.insertAdjacentHTML("beforeend", `<div class="date">${esc(o.date || "Tuesday, October 13")}</div><div class="time">${esc(o.clock || "9:04")}</div>`);
    const st = document.createElement("div"); st.className = "stack";
    (o.notifs || []).forEach((n) => { const e = RU.notif(n); e.style.width = "100%"; st.append(e); });
    s.append(st); return s;
  };
  RU.screen.brief = (o = {}) => {
    const s = RU.screen.home(o); const dim = document.createElement("div"); Object.assign(dim.style, { position: "absolute", inset: 0, background: "rgba(0,0,0,.55)", zIndex: 8 }); s.append(dim);
    const sh = RU.brief(o.brief); Object.assign(sh.style, { position: "absolute", left: 0, bottom: 0, zIndex: 9, top: (o.sheetTop ?? 100) + "px", width: "393px", overflow: "hidden" }); sh.className += " ru-sheet-abs"; s.append(sh); return s;
  };
  RU.screen.thread = (o = {}) => {
    const s = screen(statusBar(o.time || "9:04"), "", o); const t = RU.thread({ ...o, ai: o.ai ?? false }); Object.assign(t.style, { position: "absolute", left: "14px", top: "70px", width: "365px", zoom: 1 });
    s.append(t); return s;
  };
})();
