---
description: "Task list for Todo In-Memory Python Console App implementation"
---

# Tasks: Todo In-Memory Python Console App

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Unit tests will be included for all core functionality to ensure reliability.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python project with basic configuration
- [X] T003 [P] Configure linting and formatting tools (flake8, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 [P] Create base Task model in src/models/task.py
- [X] T005 [P] Implement in-memory storage in src/models/task.py
- [X] T006 Create base TodoService in src/services/todo_service.py
- [X] T007 Create utility functions in src/lib/utils.py
- [X] T008 Configure error handling infrastructure in src/lib/utils.py
- [X] T009 Setup type hints configuration in pyproject.toml

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Task (Priority: P1) 🎯 MVP

**Goal**: User can input a new todo task with title and description, which gets stored in memory with a unique Task ID.

**Independent Test**: User can run the console app, enter a task title and description, and see the task successfully added with a unique ID. The task remains accessible during the current session.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Unit test for Task creation in tests/unit/test_task.py
- [X] T011 [P] [US1] Unit test for TodoService add_task in tests/unit/test_todo_service.py
- [X] T012 [P] [US1] Integration test for add task flow in tests/integration/test_cli_flow.py

### Implementation for User Story 1

- [X] T013 [P] [US1] Implement Task entity with ID, title, description, status in src/models/task.py
- [X] T014 [P] [US1] Implement add_task method in src/services/todo_service.py
- [X] T015 [US1] Implement add task functionality in src/cli/main.py
- [X] T016 [US1] Add validation for task creation in src/lib/utils.py
- [X] T017 [US1] Add error handling for empty title in src/lib/utils.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - List All Todo Tasks (Priority: P1)

**Goal**: User can view all stored tasks in a structured, numbered list format.

**Independent Test**: User can run the console app, add some tasks, then view the complete list of all tasks with their IDs, titles, descriptions, and completion status.

### Tests for User Story 2 ⚠️

- [X] T018 [P] [US2] Unit test for TodoService get_all_tasks in tests/unit/test_todo_service.py
- [X] T019 [P] [US2] Integration test for list tasks flow in tests/integration/test_cli_flow.py

### Implementation for User Story 2

- [X] T020 [P] [US2] Implement get_all_tasks method in src/services/todo_service.py
- [X] T021 [US2] Implement list tasks functionality in src/cli/main.py
- [X] T022 [US2] Format task display in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo Task (Priority: P2)

**Goal**: User can select a task by Task ID and update its title or description.

**Independent Test**: User can run the console app, select a task by ID, update its title or description, and see the changes reflected in the system.

### Tests for User Story 3 ⚠️

- [X] T023 [P] [US3] Unit test for TodoService update_task in tests/unit/test_todo_service.py
- [X] T024 [P] [US3] Integration test for update task flow in tests/integration/test_cli_flow.py

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement update_task method in src/services/todo_service.py
- [X] T026 [US3] Implement update task functionality in src/cli/main.py
- [X] T027 [US3] Add validation for task updates in src/lib/utils.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Delete Todo Task (Priority: P2)

**Goal**: User can delete a task by Task ID.

**Independent Test**: User can run the console app, select a task by ID, delete it, and confirm it's no longer in the system.

### Tests for User Story 4 ⚠️

- [X] T028 [P] [US4] Unit test for TodoService delete_task in tests/unit/test_todo_service.py
- [X] T029 [P] [US4] Integration test for delete task flow in tests/integration/test_cli_flow.py

### Implementation for User Story 4

- [X] T030 [P] [US4] Implement delete_task method in src/services/todo_service.py
- [X] T031 [US4] Implement delete task functionality in src/cli/main.py
- [X] T032 [US4] Add confirmation prompt for deletion in src/cli/main.py

**Checkpoint**: User Stories 1, 2, 3, and 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task as Done (Priority: P2)

**Goal**: User can mark a task's completion status as done.

**Independent Test**: User can run the console app, select a task by ID, mark it as done, and see the updated status reflected in the system.

### Tests for User Story 5 ⚠️

- [X] T033 [P] [US5] Unit test for TodoService mark_task_done in tests/unit/test_todo_service.py
- [X] T034 [P] [US5] Integration test for mark task done flow in tests/integration/test_cli_flow.py

### Implementation for User Story 5

- [X] T035 [P] [US5] Implement mark_task_done method in src/services/todo_service.py
- [X] T036 [US5] Implement mark task done functionality in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T037 [P] Add comprehensive documentation in README.md
- [ ] T038 Add command-line argument support in src/cli/main.py
- [ ] T039 [P] Additional unit tests in tests/unit/
- [ ] T040 Performance optimization for large task lists
- [ ] T041 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence