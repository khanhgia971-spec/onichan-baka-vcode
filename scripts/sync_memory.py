#!/usr/bin/env python3
"""
VibeCode Omni Enterprise - Universal Cross-Model Memory & Zero-Prompt Handoff Engine.
Manages .ai-memory/ state files and auto-generates cross-vendor bridge rules
(CLAUDE.md, AGENTS.md, .cursorrules, .windsurfrules, .gemini/GEMINI.md, .github/copilot-instructions.md)
so switching AI providers after quota exhaustion resumes seamlessly with zero handoff prompt.
"""

import argparse
import datetime
import json
import os
from pathlib import Path
from typing import Any, Dict

MEMORY_DIR_NAME = ".ai-memory"

BRIDGE_SNIPPET = """
<!-- VIBECODE-OMNI-ENTERPRISE-BRIDGE:START -->
## Universal Cross-Model Memory & Auto-Resume Protocol (VibeCode Omni Enterprise)

1. **Mandatory Startup Check**: Before responding to ANY user prompt (especially short prompts like "continue", "tiep tuc", "lam tiep", or new feature requests), you MUST read:
   - `.ai-memory/HANDOFF.md` (exact current checkpoint, active file/line cursor, and next immediate action)
   - `.ai-memory/STATE.json` (machine-readable task graph and progress state)
   - `.ai-memory/BUG_LEDGER.md` (immutable log of fixed bugs and root causes - NEVER re-introduce these bugs or repeat failed approaches)
   - `.ai-memory/DECISIONS.md` (locked product requirements and architectural decisions)
2. **Zero-Prompt Quota Handoff**: If the previous AI model hit its quota limit mid-task, resume immediately from `next_immediate_action` in `.ai-memory/HANDOFF.md` without asking the user to re-explain the project.
3. **Continuous Checkpoint Write**: After every completed sub-task, file edit, or bug fix, update `.ai-memory/HANDOFF.md`, `.ai-memory/STATE.json`, and `.ai-memory/BUG_LEDGER.md` (via `python3 scripts/sync_memory.py checkpoint ...` or direct file update).
<!-- VIBECODE-OMNI-ENTERPRISE-BRIDGE:END -->
""".strip()

DEFAULT_STATE: Dict[str, Any] = {
    "schema_version": "2.0.0",
    "project_name": "",
    "last_updated_utc": "",
    "last_active_model": "universal-agent",
    "Original_Prompt_Intent": "Pending initialization from first user request.",
    "current_phase": "THINK_AND_PLAN",
    "active_file_cursor": {
        "file_path": "",
        "function_or_section": "",
        "line_range": "",
        "uncommitted_notes": ""
    },
    "completed_milestones": [],
    "pending_milestones": [],
    "next_immediate_action": "Read project structure, expand user requirements, and lock architecture in .ai-memory/DECISIONS.md."
}

DEFAULT_HANDOFF_MD = """# Cross-Model Handoff & Live Checkpoint (`HANDOFF.md`)

> **AUTO-READ INSTRUCTION FOR ALL AI MODELS (Claude, Cursor, Codex, Gemini, Windsurf, OpenCode, Copilot)**:
> Read this file first on every session start. If the user says "continue" or "tiếp tục", execute **Next Immediate Action** below without asking the user to repeat context.

## 1. Project Intent & Locked Scope
- **Original User Goal**: {intent}
- **Current Sprint Phase**: `{phase}`
- **Last Active Agent / Model**: `{model}`
- **Last Updated (UTC)**: `{timestamp}`

## 2. Active File & Code Cursor (Where the Last AI Stopped)
- **Target File**: `{file_path}`
- **Function / Component**: `{function_name}`
- **Line Range**: `{line_range}`
- **State Notes**: {notes}

## 3. Next Immediate Action (Resume Here)
- [ ] {next_action}

## 4. Milestone Progress
### Completed (`[x]`)
{completed_list}

### Pending (`[ ]`)
{pending_list}
"""

DEFAULT_BUG_LEDGER_MD = """# Immutable Bug & Regression Ledger (`BUG_LEDGER.md`)

> **RULE**: Every AI agent MUST scan this ledger before editing code. Never re-introduce a bug listed here, never revert its regression test, and never retry an approach marked as failed.

| Bug ID | Date (UTC) | Affected File / Module | Symptom / Error | Root Cause | Verified Fix & Commit/Patch | Regression Test |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BUG-000` | `{timestamp}` | `N/A` | Ledger initialized | System bootstrap | Initialized `.ai-memory/BUG_LEDGER.md` | `N/A` |
"""

DEFAULT_DECISIONS_MD = """# Architectural Decision Records & Prompt Expansion (`DECISIONS.md`)

## 1. 360-Degree Prompt Expansion
- **Explicit User Request**: Recorded on first prompt.
- **Implicit UX & Edge Cases**: Loading states, empty states, error boundaries, offline/retry handling, accessibility.
- **Security & Rate-Limiting Constraints**: Input validation, auth boundaries, injection protection.
- **Performance Targets**: Sub-100ms API response / 60fps UI or 3D viewport budget.

## 2. Locked Tech Stack & Conventions
- Document framework versions, folder layout, naming conventions, and state management rules here so all AI providers write identical-style code.
"""


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def render_handoff(state: Dict[str, Any]) -> str:
    completed = state.get("completed_milestones", [])
    pending = state.get("pending_milestones", [])
    completed_str = "\n".join(f"- [x] {m}" for m in completed) if completed else "- *(None yet)*"
    pending_str = "\n".join(f"- [ ] {m}" for m in pending) if pending else "- *(None queued)*"
    cursor = state.get("active_file_cursor", {})
    return DEFAULT_HANDOFF_MD.format(
        intent=state.get("Original_Prompt_Intent", "Not set"),
        phase=state.get("current_phase", "THINK_AND_PLAN"),
        model=state.get("last_active_model", "universal-agent"),
        timestamp=state.get("last_updated_utc", utc_now()),
        file_path=cursor.get("file_path") or "None",
        function_name=cursor.get("function_or_section") or "None",
        line_range=cursor.get("line_range") or "N/A",
        notes=cursor.get("uncommitted_notes") or "Clean working state.",
        next_action=state.get("next_immediate_action", "Inspect project and continue."),
        completed_list=completed_str,
        pending_list=pending_str,
    )


def init_memory(root: Path) -> None:
    mem_dir = root / MEMORY_DIR_NAME
    mem_dir.mkdir(parents=True, exist_ok=True)
    now = utc_now()

    state_file = mem_dir / "STATE.json"
    if not state_file.exists():
        state = dict(DEFAULT_STATE)
        state["project_name"] = root.resolve().name
        state["last_updated_utc"] = now
        state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        state = json.loads(state_file.read_text(encoding="utf-8"))

    handoff_file = mem_dir / "HANDOFF.md"
    if not handoff_file.exists():
        handoff_file.write_text(render_handoff(state), encoding="utf-8")

    bug_file = mem_dir / "BUG_LEDGER.md"
    if not bug_file.exists():
        bug_file.write_text(DEFAULT_BUG_LEDGER_MD.format(timestamp=now), encoding="utf-8")

    decisions_file = mem_dir / "DECISIONS.md"
    if not decisions_file.exists():
        decisions_file.write_text(DEFAULT_DECISIONS_MD, encoding="utf-8")

    print(f"[OK] Initialized persistent cross-model memory in {mem_dir}")


def upsert_bridge_file(file_path: Path) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    start_tag = "<!-- VIBECODE-OMNI-ENTERPRISE-BRIDGE:START -->"
    end_tag = "<!-- VIBECODE-OMNI-ENTERPRISE-BRIDGE:END -->"

    if file_path.exists():
        content = file_path.read_text(encoding="utf-8")
        if start_tag in content and end_tag in content:
            pre = content.split(start_tag)[0]
            post = content.split(end_tag)[1]
            updated = pre.rstrip() + "\n\n" + BRIDGE_SNIPPET + "\n" + post.lstrip()
            file_path.write_text(updated, encoding="utf-8")
        else:
            file_path.write_text(content.rstrip() + "\n\n" + BRIDGE_SNIPPET + "\n", encoding="utf-8")
    else:
        file_path.write_text(BRIDGE_SNIPPET + "\n", encoding="utf-8")


def sync_bridges(root: Path) -> None:
    init_memory(root)
    targets = [
        root / "CLAUDE.md",
        root / "AGENTS.md",
        root / ".cursorrules",
        root / ".windsurfrules",
        root / ".gemini" / "GEMINI.md",
        root / ".github" / "copilot-instructions.md",
    ]
    for target in targets:
        upsert_bridge_file(target)
    print(f"[OK] Synced cross-model auto-handoff bridges across {len(targets)} AI provider rule files.")


def update_checkpoint(
    root: Path,
    intent: str | None,
    phase: str | None,
    model: str | None,
    file_path: str | None,
    func_name: str | None,
    line_range: str | None,
    notes: str | None,
    next_action: str | None,
    complete_milestone: str | None,
    add_pending: str | None,
) -> None:
    init_memory(root)
    state_file = root / MEMORY_DIR_NAME / "STATE.json"
    state = json.loads(state_file.read_text(encoding="utf-8"))
    state["last_updated_utc"] = utc_now()

    if intent:
        state["Original_Prompt_Intent"] = intent
    if phase:
        state["current_phase"] = phase
    if model:
        state["last_active_model"] = model
    if file_path is not None:
        state["active_file_cursor"]["file_path"] = file_path
    if func_name is not None:
        state["active_file_cursor"]["function_or_section"] = func_name
    if line_range is not None:
        state["active_file_cursor"]["line_range"] = line_range
    if notes is not None:
        state["active_file_cursor"]["uncommitted_notes"] = notes
    if next_action:
        state["next_immediate_action"] = next_action
    if complete_milestone:
        if complete_milestone not in state["completed_milestones"]:
            state["completed_milestones"].append(complete_milestone)
        if complete_milestone in state["pending_milestones"]:
            state["pending_milestones"].remove(complete_milestone)
    if add_pending and add_pending not in state["pending_milestones"]:
        state["pending_milestones"].append(add_pending)

    state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    handoff_file = root / MEMORY_DIR_NAME / "HANDOFF.md"
    handoff_file.write_text(render_handoff(state), encoding="utf-8")
    print("[OK] Updated .ai-memory/STATE.json and .ai-memory/HANDOFF.md")


def log_bug(
    root: Path,
    bug_id: str,
    module: str,
    symptom: str,
    root_cause: str,
    fix: str,
    test: str,
) -> None:
    init_memory(root)
    bug_file = root / MEMORY_DIR_NAME / "BUG_LEDGER.md"
    row = f"| `{bug_id}` | `{utc_now()}` | `{module}` | {symptom} | {root_cause} | {fix} | `{test}` |\n"
    with bug_file.open("a", encoding="utf-8") as f:
        f.write(row)
    print(f"[OK] Recorded {bug_id} in .ai-memory/BUG_LEDGER.md")


def main() -> None:
    parser = argparse.ArgumentParser(description="VibeCode Omni Enterprise Memory & Cross-Model Handoff Manager")
    parser.add_argument("action", choices=["init", "sync", "checkpoint", "log-bug"], help="Action to run")
    parser.add_argument("--root", default=".", help="Project root directory")
    parser.add_argument("--intent", help="Original prompt intent")
    parser.add_argument("--phase", help="Current sprint phase")
    parser.add_argument("--model", help="Current AI model identifier")
    parser.add_argument("--file", help="Active file path")
    parser.add_argument("--func", help="Active function or component")
    parser.add_argument("--lines", help="Active line range")
    parser.add_argument("--notes", help="Uncommitted state notes")
    parser.add_argument("--next", dest="next_action", help="Next immediate action for handoff")
    parser.add_argument("--done", help="Mark a milestone completed")
    parser.add_argument("--todo", help="Add a pending milestone")
    parser.add_argument("--bug-id", default="BUG-001", help="Bug identifier")
    parser.add_argument("--module", default="", help="Affected file or module")
    parser.add_argument("--symptom", default="", help="Observed bug symptom")
    parser.add_argument("--cause", default="", help="Verified root cause")
    parser.add_argument("--fix", default="", help="Fix summary")
    parser.add_argument("--test", default="", help="Regression test command or file")

    args = parser.parse_args()
    root_path = Path(args.root)

    if args.action == "init":
        init_memory(root_path)
    elif args.action == "sync":
        sync_bridges(root_path)
    elif args.action == "checkpoint":
        update_checkpoint(
            root=root_path,
            intent=args.intent,
            phase=args.phase,
            model=args.model,
            file_path=args.file,
            func_name=args.func,
            line_range=args.lines,
            notes=args.notes,
            next_action=args.next_action,
            complete_milestone=args.done,
            add_pending=args.todo,
        )
    elif args.action == "log-bug":
        log_bug(
            root=root_path,
            bug_id=args.bug_id,
            module=args.module,
            symptom=args.symptom,
            root_cause=args.cause,
            fix=args.fix,
            test=args.test,
        )


if __name__ == "__main__":
    main()
