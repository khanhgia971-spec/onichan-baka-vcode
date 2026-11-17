# 2026 Web MCP Orchestration Playbook (Search -> Multi-Page Crawl -> Browser Actuation)

This guide defines the **Passive 3-Stage Web Intelligence Pipeline** embedded in `vibecode-omni-enterprise`. Every server name in `assets/mcp-config.json` maps directly to the `allowed-tools` wildcard prefixes in `SKILL.md` (`mcp__<server_name>__*`) so AI coding agents execute web workflows without interrupting the user for permission on each URL.

## 1. 2026 Recommended MCP Stack (100% Free Default + Optional API Tier)

| Stage | Role | Default 100% Free / Keyless MCP Servers (2026) | Optional API-Key Servers | `allowed-tools` Prefix |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1: Broad Search** | Real-time multi-engine query & URL discovery | [Aas-ee/open-webSearch](https://github.com/aas-ee/open-websearch) (`npx -y open-websearch@latest`), [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) (`uvx duckduckgo-mcp-server`), [sweetcornna/free-search-mcp](https://github.com/sweetcornna/free-search-mcp) | `tavily-mcp`, `@modelcontextprotocol/server-brave-search` | `mcp__open-websearch__*`, `mcp__duckduckgo__*`, `mcp__tavily__*`, `mcp__brave-search__*` |
| **Stage 2: Multi-Page Deep Read (5-10x Faster)** | Parallel HTML-to-Markdown extraction across 3-5 pages | Official [modelcontextprotocol/servers Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) (`uvx mcp-server-fetch`), [jina-ai/MCP](https://github.com/jina-ai/MCP) (`npx -y jina-mcp-tools` / `https://r.jina.ai/`), [unclecode/crawl4ai](https://github.com/unclecode/crawl4AI) ([sadiuysal/crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)) | `firecrawl-mcp` | `mcp__fetch__*`, `mcp__jina__*`, `mcp__crawl4ai__*`, `mcp__firecrawl__*` |
| **Stage 3: Live Browser Interaction** | Accessibility-tree browser automation (click, form fill, login, SPA) | Official Microsoft [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) (`npx -y @playwright/mcp@latest`), [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) | Cloudflare Playwright MCP | `mcp__playwright__*` |

## 2. Strict 3-Step Execution Protocol

### Step 1: Broad Multi-Source Search
- Query 1-3 focused search strings via `mcp__open-websearch__*`, `mcp__duckduckgo__*`, `mcp__tavily__*`, or `mcp__brave-search__*`.
- Select the **3 to 5 highest-authority URLs** (official docs, GitHub source files/issues, RFCs, or target web apps).

### Step 2: Parallel Multi-Page Markdown Extraction & Cross-Verification
- Never launch a full Playwright browser just to read static documentation, blog posts, or API references.
- Call `mcp__fetch__*`, `mcp__jina__*`, `mcp__crawl4ai__*`, or `mcp__firecrawl__*` in parallel on all 3-5 selected URLs to obtain clean Markdown in milliseconds (5-10x faster and 80% fewer tokens than raw DOM dumps).
- Cross-check version numbers, breaking API changes, and code patterns across the retrieved pages before synthesizing.

### Step 3: Interactive Browser Actuation (Only When Required)
- Invoke `mcp__playwright__*` (`@playwright/mcp`) strictly when the page requires real browser interaction:
  - Clicking tabs, dropdowns, modals, or pagination (`browser_click`)
  - Filling forms, search bars, or login flows (`browser_fill_form`, `browser_type`)
  - Executing client-side JavaScript or inspecting network/console errors on SPAs
- **Mandatory Snapshot Verification**: Call `browser_snapshot` (accessibility tree snapshot) **before** acting to locate exact element refs, and **after** acting to verify the state change succeeded.
