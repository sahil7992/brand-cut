#!/bin/sh
# Installs brandcut as a Claude Code skill (symlink, so `git pull` updates it).
set -e
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/brandcut"
SRC="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$(dirname "$DEST")"
if [ -e "$DEST" ] && [ ! -L "$DEST" ]; then
  echo "$DEST exists and is not a symlink; move it first." >&2; exit 1
fi
ln -sfn "$SRC" "$DEST"
command -v ffmpeg >/dev/null || echo "note: install ffmpeg (brew install ffmpeg)"
command -v node >/dev/null || echo "note: install Node 18+ (HyperFrames runs via npx)"
echo "Installed: $DEST -> $SRC"
echo "In Claude Code, try: make a 15 second launch film for <company or repo>"
