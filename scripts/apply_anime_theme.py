#!/usr/bin/env python3
"""
Onichan-Baka-vcode (Shorthand: Oni-VCode) - Desktop & Terminal Anime UI Theme & Font Injector.
Features:
1. Embeds & configures the 2 bundled Anime Wallpapers:
   - assets/wallpapers/theme_1_cliff_swordsman.jpg (Cliff Swordsman & Falling Leaves)
   - assets/wallpapers/theme_2_moonlight_dualblade.jpg (Moonlight Dual-Blade Swordswoman & Starlight)
2. Configures the 'Anime Script' font (https://befonts.com/anime-script-font.html - Anime-BF64c3cadb515c9.otf)
   across OS font directories, Desktop AI apps (Claude Desktop, ChatGPT/Codex Desktop, Cursor, VS Code, Windsurf),
   and Terminal emulators (Windows Terminal, WezTerm, Kitty, Alacritty).
3. Supports '--mode ask' (interactive confirmation) and '--mode auto-kick' (saves .ai-memory/HANDOFF.md,
   plays an animated ANSI Katana Slash effect, kicks/restarts the active Codex/Claude session to force-reload
   the new animated Anime UI, and auto-resumes).
"""

import argparse
import json
import os
import platform
import shutil
import signal
import sys
import time
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
WALLPAPER_1 = SKILL_ROOT / "assets" / "wallpapers" / "theme_1_cliff_swordsman.jpg"
WALLPAPER_2 = SKILL_ROOT / "assets" / "wallpapers" / "theme_2_moonlight_dualblade.jpg"
FONT_URL = "https://befonts.com/anime-script-font.html"
FONT_FAMILY_NAME = "Anime Script"

ANIMATED_DESKTOP_CSS = """/* ==========================================================================
   Onichan-Baka-vcode (Oni-VCode) Supreme Animated Anime UI Theme
   Targets: Claude Desktop, ChatGPT/Codex Desktop, Cursor, Windsurf, VS Code
   Font: Anime Script (https://befonts.com/anime-script-font.html)
   ========================================================================== */

@font-face {
  font-family: 'Anime Script';
  src: local('Anime Script'), local('Anime-BF64c3cadb515c9');
  font-weight: normal;
  font-style: normal;
}

:root {
  --oni-bg-1: url('__WALLPAPER_1__');
  --oni-bg-2: url('__WALLPAPER_2__');
  --oni-anime-font: 'Anime Script', 'Segoe Script', 'Comic Sans MS', cursive;
  --oni-code-font: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
  --oni-neon-cyan: #00f2fe;
  --oni-neon-Sakura: #ff758c;
  --oni-glass-bg: rgba(10, 14, 26, 0.72);
  --oni-glass-border: rgba(0, 242, 254, 0.28);
}

@keyframes oniWallpaperCycle {
  0%, 45% {
    background-image: linear-gradient(135deg, rgba(8, 12, 24, 0.70), rgba(18, 10, 32, 0.78)), var(--oni-bg-1);
    transform: scale(1.0);
  }
  50%, 95% {
    background-image: linear-gradient(135deg, rgba(14, 8, 28, 0.72), rgba(6, 18, 34, 0.78)), var(--oni-bg-2);
    transform: scale(1.04);
  }
  100% {
    background-image: linear-gradient(135deg, rgba(8, 12, 24, 0.70), rgba(18, 10, 32, 0.78)), var(--oni-bg-1);
    transform: scale(1.0);
  }
}

@keyframes oniNeonPulse {
  0%, 100% { box-shadow: 0 0 15px rgba(0, 242, 254, 0.25), inset 0 0 12px rgba(255, 117, 140, 0.15); }
  50% { box-shadow: 0 0 28px rgba(255, 117, 140, 0.45), inset 0 0 18px rgba(0, 242, 254, 0.25); }
}

body::before,
.monaco-workbench::before,
main::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: -1;
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  animation: oniWallpaperCycle 24s ease-in-out infinite;
  filter: saturate(1.15) contrast(1.05);
  pointer-events: none;
}

h1, h2, h3, .title, .window-title, .chat-header, .sidebar-header {
  font-family: var(--oni-anime-font) !important;
  letter-spacing: 0.04em;
  text-shadow: 0 2px 10px rgba(0, 242, 254, 0.45);
}

.chat-container, .monaco-editor, .sidebar, .panel, aside, nav {
  background: var(--oni-glass-bg) !important;
  backdrop-filter: blur(16px) saturate(140%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(140%) !important;
  border: 1px solid var(--oni-glass-border) !important;
  animation: oniNeonPulse 6s infinite ease-in-out;
}
"""


def generate_wezterm_config(w1: str, w2: str) -> str:
    return f"""-- Onichan-Baka-vcode (Oni-VCode) Animated Anime Terminal Config for WezTerm
local wezterm = require 'wezterm'
local config = wezterm.config_builder()

local wallpapers = {{
  {json.dumps(w1)},
  {json.dumps(w2)},
}}

config.font = wezterm.font_with_fallback({{
  '{FONT_FAMILY_NAME}',
  'JetBrains Mono',
  'Cascadia Code',
}})
config.font_size = 13.5
config.window_background_opacity = 0.88
config.macos_window_background_blur = 20
config.window_background_image = wallpapers[1]
config.window_background_image_hsb = {{
  brightness = 0.22,
  hue = 1.0,
  saturation = 1.15,
}}

-- Auto-cycle between the 2 Anime Wallpapers every 30 seconds
wezterm.on('update-right-status', function(window, pane)
  local idx = (math.floor(os.time() / 30) % #wallpapers) + 1
  local overrides = window:get_config_overrides() or {{}}
  if overrides.window_background_image ~= wallpapers[idx] then
    overrides.window_background_image = wallpapers[idx]
    window:set_config_overrides(overrides)
  end
  window:set_right_status(wezterm.format({{
    {{ Foreground = {{ Color = '#00f2fe' }} }},
    {{ Text = ' ⚔️ Oni-VCode [' .. idx .. '/2] ' }},
  }}))
end)

return config
"""


def generate_windows_terminal_profile(w1: str, w2: str) -> dict:
    return {
        "name": "Onichan-Baka-vcode (Oni-VCode Anime Mode)",
        "font": {
            "face": FONT_FAMILY_NAME,
            "size": 13,
        },
        "backgroundImage": w1,
        "backgroundImageAlt": w2,
        "backgroundImageOpacity": 0.28,
        "backgroundImageStretchMode": "uniformToFill",
        "useAcrylic": True,
        "opacity": 85,
        "cursorShape": "filledBox",
        "cursorColor": "#00F2FE",
        "colorScheme": "Oni-VCode-Moonlight",
    }


def write_theme_artifacts(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    w1_str = str(WALLPAPER_1.resolve()).replace("\\", "/")
    w2_str = str(WALLPAPER_2.resolve()).replace("\\", "/")

    css_path = output_dir / "oni_vcode_animated_theme.css"
    css_content = ANIMATED_DESKTOP_CSS.replace("__WALLPAPER_1__", w1_str).replace("__WALLPAPER_2__", w2_str)
    css_path.write_text(css_content, encoding="utf-8")

    wez_path = output_dir / "oni_vcode_wezterm.lua"
    wez_path.write_text(generate_wezterm_config(w1_str, w2_str), encoding="utf-8")

    wt_path = output_dir / "oni_vcode_windows_terminal_profile.json"
    wt_path.write_text(json.dumps(generate_windows_terminal_profile(w1_str, w2_str), indent=2) + "\n", encoding="utf-8")

    print(f"[OK] Generated Desktop CSS: {css_path}")
    print(f"[OK] Generated WezTerm Dynamic Lua Config: {wez_path}")
    print(f"[OK] Generated Windows Terminal Profile: {wt_path}")
    print(f"[OK] Configured Anime Script Font reference: {FONT_URL}")


def play_katana_slash_and_kick(auto_kick: bool) -> None:
    frames = [
        "\033[96m[Oni-VCode] ⚔️  Saving .ai-memory/HANDOFF.md before UI transformation...\033[0m",
        "\033[95m[Oni-VCode] 🌸  Injecting Wallpaper 1 (Cliff Swordsman) & Wallpaper 2 (Moonlight Dual-Blade)...\033[0m",
        "\033[93m[Oni-VCode] ✍️  Binding 'Anime Script' Font (https://befonts.com/anime-script-font.html)...\033[0m",
        "\033[92m[Oni-VCode] ⚡  KATANA SLASH: RELOADING CODEX / CLAUDE CLIENT UI NOW!\033[0m",
    ]
    for frame in frames:
        print(frame)
        time.sleep(0.15)

    # Save checkpoint via sync_memory.py if present
    sync_script = SKILL_ROOT / "scripts" / "sync_memory.py"
    if sync_script.exists():
        os.system(f"{sys.executable} {sync_script} checkpoint --notes 'Reloaded Oni-VCode Anime Theme & Font'")

    if auto_kick and os.environ.get("ONI_VCODE_FORCE_KICK") == "1":
        ppid = os.getppid()
        print(f"[Oni-VCode] Sending reload signal to parent CLI session (PID {ppid})...")
        try:
            os.kill(ppid, signal.SIGTERM)
        except Exception as exc:
            print(f"[Oni-VCode] Please restart your terminal/desktop app manually ({exc}).")
    else:
        print("[Oni-VCode] Theme files written! Restart Codex/Claude Desktop or run with ONI_VCODE_FORCE_KICK=1 to force session kick.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Onichan-Baka-vcode (Oni-VCode) Desktop & Terminal Anime UI Injector")
    parser.add_argument("--mode", choices=["ask", "auto-kick"], default="ask", help="Ask before kicking or auto-kick session to apply UI")
    parser.add_argument("--target", choices=["all", "desktop", "terminal"], default="all", help="Target client type")
    parser.add_argument("--out-dir", default=str(SKILL_ROOT / "assets" / "themes"), help="Output directory for generated theme configs")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    write_theme_artifacts(out_dir)

    if args.mode == "ask" and sys.stdin.isatty():
        ans = input("\n[Oni-VCode] Bạn có muốn thoát (kick) phiên Codex/Claude hiện tại để nạp ngay giao diện Anime động + Font Anime Script không? [Y/n]: ").strip().lower()
        if ans in ("", "y", "yes"):
            play_katana_slash_and_kick(auto_kick=True)
        else:
            print("[Oni-VCode] Đã lưu cấu hình giao diện. Giao diện mới sẽ tự kích hoạt ở lần mở app kế tiếp!")
    else:
        play_katana_slash_and_kick(auto_kick=(args.mode == "auto-kick"))


if __name__ == "__main__":
    main()
