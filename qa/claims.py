#!/usr/bin/env python3
"""claims.py <project>: copy and style gate against the project's brand.json.   exit 0 PASS, 2 FAIL

Run: python3 claims.py <project>
Scans visible text of index.html + compositions/*.html (tags stripped; string literals inside <script> too)
and audio/vo/script.txt. Line numbers are file lines.
  banned_words (brand copy.banned_words)        text, script literals, VO
  never_claim (brand truths.never_claim)        keyword rules: lease, brief sent/pushed, reminder, photos sent, DocuSign by itself
  ALL CAPS words of 3+ letters                  visible text, and script literals that contain a space
                                                (allowed: SMS PM AM ID PDF USD + brand copy.allow_caps)
  emoji (unicode ranges, ticks U+2713..2718 allowed unless followed by U+FE0F)   whole file
  text-transform: uppercase / textTransform     CSS, inline style, JS
  italic serif, Instrument Serif                CSS rules with font-style italic + a serif family; any Instrument Serif
  VO only: em/en dashes, spaced or double hyphens, ellipses
"""
import html, json, re, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
ALLOW_CAPS = {"SMS", "PM", "AM", "ID", "PDF", "USD", "FAQ", "MLS", "HOA", "CRM", "NYC", "LLC"}
NEVER = [
    (r"\bleases?\b", "never claim a lease (say rental application)"),
    (r"\bbrief\b.{0,20}\b(sent|pushed|delivered)\b|\b(sent|pushed)\b.{0,20}\bbrief\b", "pre-showing brief is not pushed or sent"),
    (r"\breminders?\b", "reminders are paused in code"),
    (r"\bphotos?\b.{0,15}\b(sent|sends?)\b|\bsends?\b.{0,15}\bphotos?\b", "photos are not sent to leads"),
    (r"\bdocusign\b.{0,25}\b(automatically|on its own|by itself)\b|\b(automatically|on its own)\b.{0,25}\bdocusign\b", "the user sends the document, the product does not"),
    (r"\b(compliance|wait(s|ing)? for (a )?signed)\b", "tours do not wait for a signed document or compliance"),
]
EMOJI = [(0x1F000, 0x1FAFF), (0x2600, 0x27BF), (0x2B50, 0x2B55), (0x231A, 0x23FF), (0x2300, 0x2307), (0x1F1E6, 0x1F1FF), (0xFE0F, 0xFE0F), (0x200D, 0x200D), (0x2934, 0x2935), (0x3030, 0x3030), (0x00A9, 0x00AE)]
TICKS = range(0x2713, 0x2719)
SERIF = re.compile(r"serif(?!-)|instrument|playfair|georgia|times|garamond|cormorant|fraunces|dm serif", re.I)


def emoji_at(s):
    out = []
    for i, ch in enumerate(s):
        c = ord(ch)
        if c in TICKS and not s[i + 1:i + 2] == "️":
            continue
        if c in (0xA9, 0xAE):
            continue
        if any(a <= c <= b for a, b in EMOJI):
            out.append(f"U+{c:04X}")
    return out


def blank(m):
    return re.sub(r"[^\n]", " ", m.group(0))


def split_html(src):
    """-> (visible text with tags blanked, [(start_offset, script_body)], [(start_offset, css_body)])."""
    scripts, styles = [], []
    for m in re.finditer(r"<script\b[^>]*>(.*?)</script>", src, re.S | re.I):
        scripts.append((m.start(1), m.group(1)))
    for m in re.finditer(r"<style\b[^>]*>(.*?)</style>", src, re.S | re.I):
        styles.append((m.start(1), m.group(1)))
    t = re.sub(r"<!--.*?-->", blank, src, flags=re.S)
    t = re.sub(r"<(script|style|title)\b.*?</\1>", blank, t, flags=re.S | re.I)
    t = re.sub(r"<[^>]*>", blank, t, flags=re.S)
    return html.unescape(t), scripts, styles


def line_of(src, off):
    return src.count("\n", 0, off) + 1


def main(project):
    project = Path(project).expanduser().resolve()
    brand_id = "demo"
    try:
        brand_id = json.loads((project / "film.json").read_text()).get("brand", "demo")
    except Exception:
        pass
    brand = json.loads((SKILL / "brands" / brand_id / "brand.json").read_text())
    copy = brand.get("copy", {})
    banned = [w.lower() for w in copy.get("banned_words", [])]
    allow = ALLOW_CAPS | set(copy.get("allow_caps", []))
    fails = []

    def add(f, ln, rule, detail):
        fails.append((f, ln, rule, detail))

    def text_rules(f, ln, txt, caps=True, vo=False):
        low = txt.lower()
        for w in banned:
            if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
                add(f, ln, "banned word", f"'{w}' in: {txt.strip()[:70]}")
        for rx, why in NEVER:
            if re.search(rx, low):
                add(f, ln, "never claim", f"{why}: {txt.strip()[:70]}")
        e = emoji_at(txt)
        if e:
            add(f, ln, "emoji", " ".join(sorted(set(e))))
        if caps:
            for w in re.findall(r"(?<![A-Za-z0-9#_-])[A-Z]{3,}(?![A-Za-z0-9_-])", txt):
                if w not in allow:
                    add(f, ln, "ALL CAPS", f"{w} in: {txt.strip()[:70]}")
        if vo:
            if re.search(r"[—–]| - |--", txt):
                add(f, ln, "VO dash", txt.strip()[:70])
            if "..." in txt or "…" in txt:
                add(f, ln, "VO ellipsis", txt.strip()[:70])

    files = [p for p in [project / "index.html", *sorted((project / "compositions").glob("*.html"))] if p.exists()]
    for f in files:
        rel = str(f.relative_to(project))
        src = f.read_text()
        vis, scripts, styles = split_html(src)
        for i, line in enumerate(vis.split("\n"), 1):
            if line.strip():
                text_rules(rel, i, line)
        for off, body in scripts:
            if body.lstrip().startswith("window.BRAND"):
                continue  # generated brand block (brand-css.py), not film copy
            base = line_of(src, off) - 1
            idents = set(re.findall(r"\b([A-Z][A-Z0-9_]{2,})\b(?=\s*(?:[=,;)+\]]|\.|$))", body)) & set(re.findall(r"(?:const|let|var|,|\{)\s*([A-Z][A-Z0-9_]{2,})\b", body))
            for m in re.finditer(r"'((?:[^'\\\n]|\\.)*)'|\"((?:[^\"\\\n]|\\.)*)\"|`((?:[^`\\]|\\.)*)`", body, re.S):
                lit = next(g for g in m.groups() if g is not None)
                lit = html.unescape(re.sub(r"<[^>]*>|\$\{[^}]*\}", " ", lit))
                lit = re.sub(r"\b(" + "|".join(map(re.escape, idents)) + r")\b", " ", lit) if idents else lit
                if not re.search(r"[A-Za-z]{3}", lit):
                    continue
                ln = base + body.count("\n", 0, m.start()) + 1
                text_rules(rel, ln, lit, caps=" " in lit.strip())
        # copy carried in attributes: composition variable defaults, per-scene variable values, alt/aria-label/title
        spans = [(m.start(), m.end()) for m in re.finditer(r"<script\b[^>]*>.*?</script>", src, re.S | re.I)]
        for m in re.finditer(r"\b(data-composition-variables|data-variable-values|alt|aria-label|title|placeholder)\s*=\s*(?:'([^']*)'|\"([^\"]*)\")", src, re.S):
            if any(a <= m.start() < b for a, b in spans):
                continue  # attribute text built inside a script is covered by the literal scan
            body = html.unescape(m.group(2) if m.group(2) is not None else m.group(3))
            ln = line_of(src, m.start())
            if m.group(1) == "data-composition-variables":  # only the shipped defaults are copy, not the field labels
                try:
                    lits = [str(d.get("default", "")) for d in json.loads(body)]
                except ValueError:
                    lits = []
            else:
                lits = re.findall(r'"((?:[^"\\]|\\.)*)"', body) if body.lstrip()[:1] in "[{" else [body]
            for lit in lits:
                for part in lit.split("|"):
                    if re.search(r"[A-Za-z]{3}", part):
                        text_rules(rel, ln, part, caps=" " in part.strip())
        # style: whole file (CSS blocks, inline style attrs, JS style assignments)
        for m in re.finditer(r"text-transform\s*:\s*uppercase|textTransform\s*=\s*['\"]uppercase|font-variant(-caps)?\s*:\s*(all-)?(small-caps|all-small-caps)", src, re.I):
            add(rel, line_of(src, m.start()), "uppercase style", m.group(0))
        for m in re.finditer(r"instrument[\s_-]*serif", src, re.I):
            add(rel, line_of(src, m.start()), "italic serif", "Instrument Serif is banned")
        rules = [(off + m.start(), m.group(0)) for off, css in styles for m in re.finditer(r"[^{}]*\{[^{}]*\}", css)]
        rules += [(m.start(), m.group(1)) for m in re.finditer(r"style=\"([^\"]*)\"", src)]
        for off, r in rules:
            if re.search(r"font-style\s*:\s*(italic|oblique)", r, re.I) and SERIF.search(r):
                add(rel, line_of(src, off), "italic serif", r.strip()[:80].replace("\n", " "))
    vo = project / "audio" / "vo" / "script.txt"
    if vo.exists():
        for i, line in enumerate(vo.read_text().split("\n"), 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            text_rules("audio/vo/script.txt", i, re.sub(r"^@[\d.]+\s+", "", line), caps=False, vo=True)
    if not files and not vo.exists():
        print("claims: nothing to scan")
        return 2
    seen = set()
    for f, ln, rule, d in fails:
        k = (f, ln, rule, d)
        if k in seen:
            continue
        seen.add(k)
        print(f"FAIL {f}:{ln}  {rule}: {d}")
    print(f"scanned {len(files)} html file(s){' + VO script' if vo.exists() else ''}: {'FAIL (%d)' % len(seen) if seen else 'PASS'}")
    return 2 if seen else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
