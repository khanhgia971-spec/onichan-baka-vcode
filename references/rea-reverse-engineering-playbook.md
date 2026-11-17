# REA (Reverse Engineer Anything) Integration Playbook

Integrated from [morluto/rea](https://github.com/morluto/rea) (`rea-agents`). REA connects your AI coding agent via MCP and CLI to inspect software, binaries, mobile apps, game archives, and web applications with verifiable evidence.

## 1. Setup & MCP Registration

Run the official setup command in your terminal (requires Node.js >=22.23.4, >=24.22.1, or >=26.12.1):

```bash
npx rea-agents@latest setup
```

Or install globally for continuous CLI + MCP access:

```bash
npm install --global rea-agents
rea --help
```

## 2. Target Analysis Matrix (36+ Supported Artifact Classes)

| Target Category | REA Inspection Capabilities | Command / Tool Workflow |
| :--- | :--- | :--- |
| **JavaScript & Electron Apps** | Recovers readable modules, imports, source maps, routes, Electron IPC boundaries, native add-ons, and release exposure audits. | `npx -y rea-agents@latest analyze-javascript-application /abs/path/to/app --json` |
| **Websites & Live DOM/Network** | Extracts page structure, bundled scripts, network observations, HAR/Fiddler `.saz` captures, and screenshots. | REA Browser MCP tools + HAR/SAZ capture inspector |
| **Native Binaries (ELF / PE / Mach-O)** | Extracts pseudocode, assembly, strings, symbols, cross-references, PE imports/certificates, and binary hardening flags (PIE, NX, RELRO, CFG). | REA MCP connected to Ghidra, IDA, Hopper, or Kuna |
| **Go & Rust Binaries** | Recovers embedded Go compiler settings/modules and Rust `cargo-auditable` dependency graphs without source code. | Built-in static ELF/PE/Mach-O inspection |
| **Game Engines (Unity IL2CPP & Godot)** | Decodes Unity `global-metadata.dat` (versions 24, 27, 29, 31, 39) assembly/type/method tables and extracts Godot `.pck` (v2-v4) archives. | Built-in static game artifact decoders |
| **Android APKs & Flutter Apps** | Inspects AndroidManifest, v1-v3.1 APK signatures, decompiled JADX classes/methods, and Flutter Dart snapshot hashes. | Headless JADX + ADB bridge + static APK parser |
| **WASM & EVM Bytecode** | Validates WASM sections/exports into WAT and dispatches EVM bytecode selectors, offsets, and mutability. | `inspect_wasm_artifact` & offline EVM inspector |
| **AI Model Files & SQLite Databases** | Reads GGUF / `safetensors` tensor declarations and inspects local SQLite / WAL database schemas, triggers, and rows. | Built-in static header and SQLite snapshot readers |

## 3. Evidence-Backed Reverse Engineering Rules

1. **Evidence First, Code Second**: Never guess how a proprietary or compiled feature works. Run REA inspection first, record exact symbol names, IPC channels, API routes, or byte offsets, and cite them in `.ai-memory/DECISIONS.md`.
2. **State Limitations Explicitly**: When binaries are stripped, obfuscated, or VM-protected, report both what REA proved with certainty and which regions remain unknown.
3. **Clean-Room Re-Implementation**: Use the architectural findings and behavioral evidence from REA to write clean, maintainable, well-tested code tailored to the user's stack.
