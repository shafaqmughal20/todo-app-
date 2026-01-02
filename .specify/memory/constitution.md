# Todo In-Memory Python Console App Constitution
<!-- SYNC IMPACT REPORT:
Version change: N/A -> 1.0.0
Modified principles: N/A (new constitution)
Added sections: All sections (new constitution)
Removed sections: N/A
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .claude/commands/*.md ⚠ pending
Follow-up TODOs: None
-->
# Todo In-Memory Python Console App Constitution

## Core Principles

### Language & Environment
Python 3.x, in-memory data structures, console interface only.

### Data Storage
Only in-memory (lists, dicts, sets). No external databases or files.

### Architecture
Modular, clean, single responsibility per function/class.

### Coding Standards
PEP8 compliant, type hints mandatory, comments linking code to Task IDs.

### Testing
Each function must have clear testable behavior; implement simple console-based verification.

### Error Handling
No crashes allowed. Gracefully handle invalid inputs, empty lists, duplicates, etc.

## Non-Negotiables

- No external dependencies beyond Python standard library.
- No data persistence outside memory.
- All features must have linked Tasks in speckit.tasks.
- Every module must map to architecture in speckit.plan.
- Stop immediately if a required spec, plan, or task is missing.

## Development Workflow

- Task Alignment: Every code piece must reference a Task ID and must map back to speckit.tasks.
- No Vibe-Coding: Cannot write code unless a Task is explicitly defined.
- Iterative Development: Implement, test, review, and only then proceed to the next Task.
- Output & UX: Console output must be clear, formatted, and user-friendly.

## Governance

- Follow SDD methodology: Constitution → Specify → Plan → Tasks → Implement.
- Cross-check Task ID and Plan before writing code.
- Do not add extra features or modify architecture without explicit instructions.
- Always link code output to Task, Plan, and Specify sections.
- Verify all inputs and outputs in the console before marking a Task complete.
- Golden Rule: No Task → No Code. No Spec → No Implementation.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
