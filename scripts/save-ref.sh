#!/bin/zsh
# Save an Instagram/TikTok/YouTube reference for later study.
# Usage: save-ref.sh <url>   -> ${MOTION_LIBRARY:-./library}/ref-reel-<id>/{dl/reel.mp4, dl/reel.info.json, overview.png} + song id
url="$1"; id=$(echo "$url" | sed -E 's#.*/(reel|p|reels|tv)/([^/?]+).*#\2#')
d=${MOTION_LIBRARY:-./library}/ref-reel-$id; mkdir -p $d/dl; cd $d/dl || exit 1
uvx yt-dlp -o "reel.%(ext)s" --write-info-json "$url" 2>&1 | grep -E 'ERROR' 
[ -f reel.info.json ] && python3 -I -c "
import json; d=json.load(open('reel.info.json')); print(d.get('uploader'),'|',d.get('channel'),'|',(d.get('description') or '').replace(chr(10),' ')[:240])"
[ -f reel.mp4 ] || { echo "no video (image post or login wall): open in ego-browser"; exit 0; }
ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of compact reel.mp4 | tr '\n' ' '; echo
cd .. && ffmpeg -v error -y -i dl/reel.mp4 -vf "fps=2,scale=200:-1,tile=8x6:padding=3:color=gray" -frames:v 1 overview.png
uvx --python 3.12 --with shazamio python -I ~/.claude/skills/reel-to-motion-film/scripts/shazam.py dl/reel.mp4 2>&1 | grep -E '"title"|"subtitle"' | tr '\n' ' '; echo
echo "saved: $d"
