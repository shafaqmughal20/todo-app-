---
id: 1
title: Update Python Console App Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: 002-docusaurus-ui-transform
user: Claude Code
command: /sp.constitution
labels: ["constitution", "spec-driven-development", "python", "todo-app"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
# SP.Constitution Prompt for Agents

## Project Title
**Todo In-Memory Python Console App** (Phase I)

---

## Objective
You are an expert software agent. Your goal is to ensure that **every line of code, design, and workflow** strictly follows the **Spec-Driven Development (SDD)** methodology for this project. **No improvisation allowed.**

You must strictly follow the **Spec-KitPlus hierarchy**:

1. **Constitution** → Project Principles, Tech Standards, Non-negotiables
2. **Specify** → Requirements, Acceptance Criteria, User Journeys
3. **Plan** → Architecture, Components, Interfaces
4. **Tasks** → Atomic, Testable Work Units
5. **Implement** → Code only what is defined in Tasks

> Always stop and request clarification if anything is missing.

---

## Core Principles (Constitution)
1. **Language & Environment:** Python 3.x, in-memory data structures, console interface only.
2. **Data Storage:** Only in-memory (lists, dicts, sets). No external databases or files.
3. **Architecture:** Modular, clean, single responsibility per function/class.
4. **Coding Standards:** PEP8 compliant, type hints mandatory, comments linking code to Task IDs.
5. **Testing:** Each function must have clear testable behavior; implement simple console-based verification.
6. **Error Handling:** No crashes allowed. Gracefully handle invalid inputs, empty lists, duplicates, etc.
7. **Task Alignment:** Every code piece must reference a `Task ID` and must map back to `speckit.tasks`.
8. **No Vibe-Coding:** You cannot write code unless a Task is explicitly defined.
9. **Iterative Development:** Implement, test, review, and only then proceed to the next Task.
10. **Output & UX:** Console output must be clear, formatted, and user-friendly.

---

## Non-Negotiables
- **No external dependencies** beyond Python standard library.
- **No data persistence** outside memory.
- **All features** must have linked Tasks in `speckit.tasks`.
- **Every module** must map to architecture in `speckit.plan`.
- **Stop immediately** if a required spec, plan, or task is missing.

---

## Agent Instructions
1. **Read and obey Constitution before implementing anything.**
2. **Cross-check Task ID and Plan before writing code.**
3. **Do not add extra features or modify architecture without explicit instructions.**
4. **Always link code output to Task, Plan, and Specify sections.**
5. **Verify all inputs and outputs** in the console before marking a Task complete.

> **Golden Rule:** No Task → No Code. No Spec → No Implementation.

---

## Memory & Reference
- Constitution is **primary source of truth** for all coding and architecture decisions.
- Always store and recall project rules in memory before executing.
- Verify alignment with `speckit.specify` and `speckit.plan` before implementing.

---

**End of SP.Constitution Prompt**
> Agents using this prompt will follow strict SDD, produce clean Python console code, and fully respect Phase I rules for **Todo In-Memory Python Console App**.
```

## Response snapshot

Updated the project constitution file (.specify/memory/constitution.md) to reflect the Todo In-Memory Python Console App principles as specified in the user input. The new constitution includes sections for Core Principles, Non-Negotiables, Development Workflow, and Governance with specific rules for Python console app development following Spec-Driven Development methodology.

## Outcome

- ✅ Impact: Updated project constitution with specific principles for Python console app development
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with new constitution content
- 🔁 Next prompts: Continue with spec, plan, and task creation based on new constitution
- 🧠 Reflection: Constitution now properly defines the development constraints and principles for the Todo In-Memory Python Console App project

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS - Constitution properly updated with all required principles
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create feature specification based on new constitution