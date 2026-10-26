# Rebuild $MOTION_LIBRARY/REFERENCES.md from every $MOTION_LIBRARY/ref-reel-<id>/ (oldest first). Default library: ./library
import json, os, glob
H = os.path.expanduser(os.environ.get("MOTION_LIBRARY", "./library"))
dirs = sorted(glob.glob(f"{H}/ref-reel-*"), key=os.path.getctime)
rows = []
for d in dirs:
    i = d.split("ref-reel-", 1)[1]
    info, mp4 = f"{d}/dl/reel.info.json", f"{d}/dl/reel.mp4"
    who = desc = url = dur = ""
    if os.path.exists(info):
        j = json.load(open(info))
        who = j.get("channel") or j.get("uploader") or ""
        desc = (j.get("description") or "").split("\n")[0][:70].replace("|", "/")
        url = j.get("webpage_url") or ""
    url = url or f"https://www.instagram.com/p/{i}/"
    rows.append(f"| {len(rows)+1} | {i} | {url} | @{who} | {'yes' if os.path.exists(mp4) else 'NO (open in a browser)'} | {desc} |")
md = ("# Reference library (motion films)\n\nEvery reel saved for study, oldest first. Local copies: `$MOTION_LIBRARY/ref-reel-<id>/` "
      "(dl/reel.mp4, dl/reel.info.json, overview.png). "
      "Add: `scripts/save-ref.sh <url>` then `python3 .../index-refs.py`.\n\n"
      "| # | id | url | creator | video saved | caption |\n|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
open(f"{H}/REFERENCES.md", "w").write(md)
print(f"{len(rows)} references indexed")
