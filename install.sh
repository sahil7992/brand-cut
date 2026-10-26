#!/bin/sh
# Installs brand-cut as an Agent Skill (agentskills.io) by symlinking this folder,
# so `git pull` updates every agent at once.
#   ./install.sh            Claude Code + Codex/OpenCode/other agents (~/.agents/skills)
#   ./install.sh claude     only ~/.claude/skills        (Claude Code)
#   ./install.sh agents     only ~/.agents/skills        (Codex, OpenCode, any agent reading .agents)
#   ./install.sh opencode   only ~/.config/opencode/skills
#   ./install.sh <dir>      any other skills directory
set -e
NAME=brand-cut
SRC="$(cd "$(dirname "$0")" && pwd)"

link() {
  dest="$1/$NAME"
  mkdir -p "$1"
  if [ -e "$dest" ] && [ ! -L "$dest" ]; then
    echo "skip: $dest exists and is not a symlink" >&2; return
  fi
  ln -sfn "$SRC" "$dest"
  echo "installed: $dest"
}

case "${1:-default}" in
  default)  link "$HOME/.claude/skills"; link "$HOME/.agents/skills" ;;
  claude)   link "$HOME/.claude/skills" ;;
  agents|codex) link "$HOME/.agents/skills" ;;
  opencode) link "$HOME/.config/opencode/skills" ;;
  *)        link "$1" ;;
esac

for c in node ffmpeg python3 uvx; do
  command -v "$c" >/dev/null || echo "missing: $c (see README requirements)"
done
echo "Restart your agent, then ask: make a 15 second launch film for <company, URL or repo>"
