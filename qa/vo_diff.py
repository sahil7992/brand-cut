#!/usr/bin/env python3
"""vo_diff.py <project> <take> [--force] [--pause 0.35]: did the voice say the script?   exit 0 clean, 1 problems

Run: python3 vo_diff.py <project> <take>
Takes audio/vo/<take>/lines.json (rows {file, text, at, dur}; text falls back to audio/vo/script.txt line i),
transcribes each line wav with whisper (npx -y hyperframes@0.8.183 transcribe <wav> --json -d <dir>, cached in
audio/vo/<take>/whisper/<L>/transcript.json), normalises case, punctuation and numbers (11 = eleven, "11 AM"
= eleven am, $2,450 = two thousand four hundred fifty), word-level difflib per line.
FAIL (exit 1): missing words, extra words, filler words (um uh er ah hmm), pauses longer than 0.35 s between
words inside a line. NOTE only: the brand word heard as Astria/Estrea/Estrya.
"""
import argparse, difflib, json, re, subprocess, sys
from pathlib import Path

FILLERS = {"um", "uh", "uhm", "erm", "er", "ah", "aah", "hmm", "mm", "mhm", "huh", "eh"}
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def num_words(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if n < 1000:
        return ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + num_words(n % 100))
    if n < 1_000_000:
        return num_words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + num_words(n % 1000))
    return str(n)


def norm(text, brand=None):
    t = text.lower().replace("’", "'")
    t = re.sub(r"\b(\d{1,3}(?:,\d{3})+)\b", lambda m: m.group(1).replace(",", ""), t)
    t = re.sub(r"\b([ap])\.m\.?", r"\1m", t)
    t = re.sub(r"\$(\d+)", r"\1 dollars", t)
    t = re.sub(r"(\d+)%", r"\1 percent", t)
    t = re.sub(r"\d+", lambda m: num_words(int(m.group(0))), t)
    t = re.sub(r"[-/]", " ", t)
    t = re.sub(r"'s\b", "s", t)
    t = re.sub(r"[^a-z ]", "", t)
    return t.split()


def transcribe(wav, d, force):
    tj = d / "transcript.json"
    if tj.exists() and not force and tj.stat().st_mtime >= wav.stat().st_mtime:
        return json.loads(tj.read_text())
    d.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["npx", "-y", "hyperframes@0.8.183", "transcribe", str(wav), "--json", "-d", str(d)], capture_output=True, text=True)
    if not tj.exists():
        sys.exit(f"transcribe failed for {wav}:\n{r.stderr[-400:]}{r.stdout[-400:]}")
    return json.loads(tj.read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("take")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--pause", type=float, default=0.35)
    a = ap.parse_args()
    project = Path(a.project).expanduser().resolve()
    td = project / "audio" / "vo" / a.take
    rows = json.loads((td / "lines.json").read_text())
    script = [l for l in (project / "audio" / "vo" / "script.txt").read_text().split("\n") if l.strip() and not l.lstrip().startswith("#")] \
        if (project / "audio" / "vo" / "script.txt").exists() else []
    bad = 0
    for i, row in enumerate(rows):
        wav = project / row["file"]
        exp_text = row.get("text") or (re.sub(r"^@[\d.]+\s+", "", script[i]) if i < len(script) else "")
        words = transcribe(wav, td / "whisper" / wav.stem, a.force)
        notes, probs = [], []
        raw = [re.sub(r"[^a-z]", "", w["text"].lower()) for w in words]
        for w, r in zip(words, raw):
            if r in FILLERS:
                probs.append(f"filler '{w['text']}' at {w['start']:.2f}s")
        got, gt = [], []
        for w in words:
            for tok in norm(w["text"]):
                if tok in FILLERS:
                    continue
                got.append(tok)
                gt.append(w["start"])
        exp = norm(exp_text)
        sm = difflib.SequenceMatcher(None, exp, got, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            if op == "replace" and "".join(exp[i1:i2]) == "".join(got[j1:j2]):
                continue  # same letters, only spacing differs (whisper writes 9.41 for "nine forty one")
            if op in ("delete", "replace"):
                probs.append(f"missing/changed: {' '.join(exp[i1:i2])}" + (f" -> heard '{' '.join(got[j1:j2])}'" if op == "replace" else ""))
            if op == "insert":
                probs.append(f"extra: {' '.join(got[j1:j2])} at {gt[j1]:.2f}s")
        for w0, w1 in zip(words, words[1:]):
            if w1["start"] - w0["end"] > a.pause and raw[words.index(w0)] not in FILLERS:
                probs.append(f"pause {w1['start'] - w0['end']:.2f}s after '{w0['text']}' at {w0['end']:.2f}s")
        status = "FAIL" if probs else "ok  "
        bad += bool(probs)
        print(f"{status} L{row.get('i', i + 1):02d} {wav.name}: {exp_text[:60]}")
        for p in probs:
            print(f"       - {p}")
        for n in sorted(set(notes)):
            print(f"       note: {n}")
    print(f"{len(rows)} lines, {bad} with problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
