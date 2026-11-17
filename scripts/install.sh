#!/usr/bin/env bash
set -euo pipefail

# VibeCode Omni Enterprise - Universal Installer for All AI Coding Agents
# Installs skill into Claude Code, Cursor, Codex, Gemini CLI, Antigravity, OpenCode, and Windsurf

SKILL_NAME="onichan-baka-vcode"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "============================================================"
echo " Installing ${SKILL_NAME} Across AI Coding Agents..."
echo "============================================================"

TARGET_DIRS=(
  "${HOME}/.claude/skills/${SKILL_NAME}"
  "${HOME}/.cursor/skills/${SKILL_NAME}"
  "${HOME}/.codex/skills/${SKILL_NAME}"
  "${HOME}/.gemini/skills/${SKILL_NAME}"
  "${HOME}/.gemini/antigravity-cli/skills/${SKILL_NAME}"
  "${HOME}/.config/opencode/skills/${SKILL_NAME}"
  "${HOME}/.kiro/skills/${SKILL_NAME}"
)

for dir in "${TARGET_DIRS[@]}"; do
  mkdir -p "${dir}"
  cp -R "${SKILL_ROOT}/SKILL.md" "${SKILL_ROOT}/scripts" "${SKILL_ROOT}/references" "${SKILL_ROOT}/assets" "${dir}/"
  echo "[OK] Installed skill to: ${dir}"
done

# Initialize Cross-Model Memory & Auto-Handoff Bridges in current working project
if command -v python3 >/dev/null 2>&1; then
  python3 "${SKILL_ROOT}/scripts/sync_memory.py" sync --root "$(pwd)"
fi

echo ""
echo "============================================================"
echo " Optional Ecosystem Setup Commands (Run as needed):"
echo " 1. REA Reverse Engineering MCP : npx rea-agents@latest setup"
echo " 2. Blender 3D MCP Addon        : uvx mcp-for-blender setup"
echo " 3. GStack Full Browser Suite   : git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup --host auto"
echo "============================================================"
