---
name: onichan-baka-vcode
description: Supreme always-on engineering company skill (Onichan-Baka-vcode, shorthand Oni-VCode) that passively expands prompts with 30-50 year principal engineer judgment, maintains cross-model memory (.ai-memory/) for zero-prompt quota handoff, orchestrates 3-stage 2026 MCP web search, multi-page Markdown extraction, and Playwright browser interaction, runs GStack multi-agent quality/security gates and Blender 3D pipelines passively, injects animated Anime UI themes and Anime Script Font into AI Desktop/Terminal apps (with ask or auto-kick reload for Codex/Claude), and keeps REA reverse engineering strictly on-demand. Trigger whenever the user types Oni-VCode, Onichan-Baka-vcode, or works on any coding, 3D, web, UI theme, or reverse engineering task.
allowed-tools: google web_browser_agent execute_bash view_file write_to_file mcp__open-websearch__* mcp__duckduckgo__* mcp__fetch__* mcp__jina__* mcp__crawl4ai__* mcp__firecrawl__* mcp__tavily__* mcp__brave-search__* mcp__playwright__* mcp__blender__* mcp__rea__*
---

# Onichan-Baka-vcode (Shorthand: `Oni-VCode`)

## Summary

**Onichan-Baka-vcode** (invokable via shorthand **`Oni-VCode`** or `/oni-vcode`) transforms any AI coding agent (Claude Code, OpenAI Codex, Cursor, Gemini CLI, OpenCode, Windsurf, Antigravity, Kiro) into a supreme, self-driving 50-year Principal Engineering Organization with an animated Anime Desktop & Terminal UI engine. Steps 1 through 5 run **100% passively and automatically** on every turn without requiring slash commands. Step 6 (**REA Reverse Engineering**) and Step 7 (**Anime Desktop/Terminal UI & Auto-Kick Theme Injector**) activate whenever requested or configured.

## Execution Mode Matrix (Passive vs. Active)

| Module | Shorthand / Alias | Trigger Mode | Behavior |
| :--- | :--- | :--- | :--- |
| **1. Cross-Model Memory & Zero-Prompt Handoff (`.ai-memory/`)** | `Oni-VCode Memory` | **PASSIVE (Always-On)** | Auto-reads `HANDOFF.md`, `STATE.json`, and `BUG_LEDGER.md` on turn start; auto-saves checkpoints after every step. |
| **2. 3-Stage 2026 Web MCP Orchestration** | `Oni-VCode Web` | **PASSIVE (Always-On)** | Auto-runs Broad Search -> Parallel Markdown Crawl (5-10x faster) -> Playwright Accessibility Snapshot Interaction. |
| **3. 360-Degree Prompt Expansion & 50-Year Principal Mindset** | `Oni-VCode Architect` | **PASSIVE (Always-On)** | Auto-expands short user prompts into full architecture, edge cases, UX states, validation, and zero-slop code. |
| **4. GStack Virtual Company & CSO Security/Load Gate** | `Oni-VCode GStack` | **PASSIVE (Always-On)** | Passively runs CEO framing, Eng architecture, Anti-Slop Design, Staff Bug Hunt, QA, and CSO OWASP/STRIDE + local stress tests. |
| **5. Blender 3D Creation, Asset Fetch & Render (`mcp-for-blender`)** | `Oni-VCode 3D` | **PASSIVE (Context-Auto)** | Auto-activates whenever the request involves 3D models, shaders, scenes, WebGL/Three.js, or rendering. |
| **6. REA Reverse Engineering (`morluto/rea`)** | `Oni-VCode REA` / `/rea` | **ACTIVE ONLY (On-Demand)** | **Dormant by default.** Activates ONLY when the user explicitly requests reverse engineering, binary/APK/app inspection, or types `/rea`. |
| **7. Anime Desktop & Terminal UI Modder (`apply_anime_theme.py`)** | `Oni-VCode UI` / `/oni-theme` | **ACTIVE / AUTO-KICK** | Injects the 2 bundled anime wallpapers, particle animations, and **Anime Script Font** into Claude/ChatGPT/Codex Desktop & Terminal (with `ask` or `auto-kick` session reload). |

## Steps

### Step 1: Passive Cross-Model Memory and Zero-Prompt Quota Handoff (Always-On)

Maintain `.ai-memory/` in the project root automatically so switching AI providers after quota exhaustion requires zero handoff prompting:

1. Read `.ai-memory/HANDOFF.md`, `.ai-memory/STATE.json`, `.ai-memory/BUG_LEDGER.md`, and `.ai-memory/DECISIONS.md` silently at the start of every turn.
2. When the user types `"continue"`, `"tiep tuc"`, `"Oni-VCode tiep tuc"`, or switches AI vendors mid-project, immediately resume from `next_immediate_action` in `.ai-memory/HANDOFF.md` without asking the user to repeat context.
3. Initialize or sync cross-vendor instruction bridges (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `.windsurfrules`, `.gemini/GEMINI.md`, `.github/copilot-instructions.md`) via `python3 scripts/sync_memory.py sync`.
4. Audit `.ai-memory/BUG_LEDGER.md` before touching any file so solved bugs are never re-introduced and failed approaches are never repeated.
5. Update `.ai-memory/HANDOFF.md` and `.ai-memory/STATE.json` after every completed milestone with exact file paths, line ranges, and the next immediate action.

### Step 2: Passive 3-Stage Web MCP Orchestration (Search -> Multi-Page Crawl -> Browser Actuation)

Whenever a task requires up-to-date facts, library docs, multi-site synthesis, or live web interaction, automatically execute this 3-stage pipeline using pre-authorized `mcp__<server>__*` prefixes:

1. **Stage 2.1 - Broad Multi-Engine Search**:
   - Call `mcp__open-websearch__*`, `mcp__duckduckgo__*`, `mcp__tavily__*`, or `mcp__brave-search__*` to search across DuckDuckGo, Startpage, Bing, and Google.
   - Select the top 3 to 5 most authoritative URLs and filter out SEO noise.
2. **Stage 2.2 - High-Speed Multi-Page Markdown Extraction (5-10x Faster than Browser)**:
   - Call `mcp__fetch__*` (`uvx mcp-server-fetch`), `mcp__jina__*` (`jina-mcp-tools` / `r.jina.ai`), `mcp__crawl4ai__*` (`uvx crawl4ai-mcp`), or `mcp__firecrawl__*` in parallel across the 3 to 5 URLs to convert HTML into clean Markdown.
   - Cross-verify API signatures, versions, and facts across all pages before coding.
3. **Stage 2.3 - Interactive Browser Actuation via Microsoft Playwright MCP**:
   - Call `mcp__playwright__*` (`npx -y @playwright/mcp@latest`) ONLY when real UI interaction is required (clicking buttons, switching tabs, logging in, filling forms, or testing dynamic SPAs).
   - Capture an Accessibility Snapshot (`browser_snapshot`) **before** and **after** every interaction to verify state changes deterministically.

### Step 3: Passive 360-Degree Prompt Expansion & 50-Year Principal Fellow Mindset (Always-On)

Adopt the judgment of a 30-50 year Principal Fellow in the project's exact domain and automatically expand every user request across 6 dimensions:

1. Deep Functional Intent: Solve the underlying workflow problem completely, including unspoken edge cases.
2. Production UX Completeness: Build loading skeletons, empty states, error boundaries, offline retry logic, keyboard shortcuts, and responsive layouts automatically.
3. Defensive Data & Concurrency Integrity: Enforce runtime schema validation (Zod, Pydantic, TypeBox), idempotency keys, and atomic database transactions (`SELECT ... FOR UPDATE`).
4. High-Performance Engineering: Prevent N+1 queries, memory leaks, main-thread blocking, and bundle bloat.
5. Zero AI Slop: Never emit `// TODO` placeholders, mock stubs in production paths, or silent `catch {}` blocks.
6. Self-Healing Verification Loop: Run `typecheck`, `lint`, `build`, and automated test suites until 100% green before responding.

### Step 4: Passive GStack Virtual Engineering Company & CSO Security/Load Gate (Always-On)

Run the internal multi-agent company pipeline adapted from [garrytan/gstack](https://github.com/garrytan/gstack) (`references/gstack-multi-agent-playbook.md`) passively on every build (while also honoring explicit commands `/office-hours`, `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/review`, `/qa`, `/cso`, `/ship`):

1. **Passive CEO & Eng Architecture**: Lock the 10-star product wedge, ASCII architecture diagram, state machine, and failure matrix in `.ai-memory/DECISIONS.md`.
2. **Passive Designer & Staff Reviewer**: Enforce visual hierarchy, WCAG >=4.5:1 contrast, and zero concurrency/production bugs.
3. **Passive CSO Red-Team & Local Load Audit (`references/security-redteam-resilience.md`)**: Proactively audit and patch OWASP Top 10 + STRIDE flaws (IDOR, SQLi, XSS, SSRF, TOCTOU races) and run bounded local stress tests (`autocannon`, `k6`, `locust` strictly on `localhost`/staging) to verify rate limiting and anti-DoS resilience.

### Step 5: Passive Context-Aware Blender 3D Pipeline (Auto-Triggered on 3D Tasks)

When the request involves 3D models, scenes, shaders, or WebGL/Three.js, automatically orchestrate [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) (`mcp__blender__*` via `uvx mcp-for-blender`) and `scripts/blender_render_pipeline.py`:

1. Inspect scenes via `get_scene_info` and execute modular `bpy` scripts via `execute_blender_code`.
2. Fetch free CC0 3D models, HDRIs, and PBR textures via `search_assets` and `import_asset` from **Poly Haven** (`source="polyhaven"`), **Poly Pizza** (`source="polypizza"`, `licence="CC0"`), or **Sketchfab**.
3. Generate AI 3D meshes via `generate_3d` (Tripo, Meshy, Hyper3D Rodin, Hunyuan3D) or Gaussian-splat worlds via `generate_gaussian_world` (World Labs).
4. Visually verify every step with `look` (`viewport`, `camera`, `angles`, `wireframe`, `rendered`) and export Draco-compressed `.glb` assets.

### Step 6: Active On-Demand Reverse Engineering with REA (Explicit Trigger Only)

Activate [morluto/rea](https://github.com/morluto/rea) (`references/rea-reverse-engineering-playbook.md`) **ONLY** when the user explicitly asks to reverse engineer a binary, app, APK, game archive, or network capture, or types `/rea`:

1. Run `mcp__rea__*` tools or `npx -y rea-agents@latest analyze-javascript-application <path> --json`.
2. Inspect ELF/PE/Mach-O binaries (Ghidra/IDA/Hopper), Electron ASARs, Android APKs, Unity IL2CPP metadata, Godot `.pck` files, WASM, or HAR/SAZ captures with verifiable evidence.

### Step 7: Desktop & Terminal Anime UI Theme & Font Injector (`Oni-VCode UI`)

When the user wants to customize or upgrade the visual interface of their AI Desktop client (Claude Desktop, ChatGPT/Codex Desktop, Cursor, VS Code, Windsurf) or AI Terminal client (Codex CLI, Claude Code CLI, Windows Terminal, WezTerm, Kitty, Alacritty), run `scripts/apply_anime_theme.py`:

1. **Dual Bundled Anime Wallpapers & Dynamic Particles**:
   - Uses the 2 bundled high-resolution anime artworks in `assets/wallpapers/` (`theme_1_cliff_swordsman.jpg` and `theme_2_moonlight_dualblade.jpg`) with smooth Ken Burns parallax crossfading, animated falling leaves, glowing starlight/sakura canvas particles, and glassmorphism panels.
2. **Anime Script Font Installation ([BeFonts Anime Script Font](https://befonts.com/anime-script-font.html))**:
   - Installs and binds `"Anime Script"` (`Anime-BF64c3cadb515c9.otf` by `andikastudio` from `https://befonts.com/anime-script-font.html`) for headers, agent titles, and badges alongside crisp ligature monospace fonts for code blocks.
3. **Ask Mode vs. Auto-Kick Hot-Reload Mode (`--mode ask` | `--mode auto-kick`)**:
   - In `ask` mode, prompt the user before restarting the terminal/desktop client.
   - In `auto-kick` mode (`python3 scripts/apply_anime_theme.py --mode auto-kick --target all`), automatically save the current task state into `.ai-memory/HANDOFF.md`, display the animated Katana Slash transition banner, kick/restart the active `codex` / `claude` CLI or desktop process so the new Anime UI + Anime Script font takes effect immediately, and auto-resume from `.ai-memory/HANDOFF.md`.

## Gotchas

- Never break the `---` YAML frontmatter at the top of `SKILL.md`.
- Keep Steps 1-5 completely passive; keep Step 6 (REA) strictly on-demand; always save `.ai-memory/HANDOFF.md` before executing Step 7 `--mode auto-kick` so kicking the user out of Codex/Claude to reload the Anime UI never loses a single line of progress.
- Never run stress tests or security probes on external domains; restrict `/cso` load testing strictly to `localhost` or user-owned staging environments.
