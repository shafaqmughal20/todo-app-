# Quickstart Guide: Todo In-Memory Python Console App

**Feature**: 001-todo-console-app
**Date**: 2026-01-02
**Status**: Complete

## Overview

This guide provides a quick start for using and developing the Todo In-Memory Python Console App. The application allows users to manage todo tasks through a console interface with all data stored in memory during the session.

## Prerequisites

- Python 3.8 or higher
- No external dependencies required (uses only Python standard library)
- Cross-platform compatible (Windows, macOS, Linux)

## Getting Started

### Running the Application

1. **Clone or access the repository**
   ```bash
   # If using a repository
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the console application**
   ```bash
   python src/cli/main.py
   ```

3. **Follow the on-screen menu options**
   - Use number keys to select options
   - Follow prompts for required input
   - Press Enter to confirm selections

### Basic Usage

#### Adding a Task
1. Select option `1` from the main menu
2. Enter a title for your task (required, max 200 characters)
3. Optionally enter a description (max 1000 characters)
4. The system will assign a unique ID and set status to "pending"

#### Viewing Tasks
1. Select option `2` from the main menu
2. All tasks will be displayed in creation order
3. Tasks show ID, status (pending/done), and title

#### Updating a Task
1. Select option `3` from the main menu
2. Enter the ID of the task you want to update
3. Optionally provide a new title or description
4. Leave blank to keep current values

#### Deleting a Task
1. Select option `4` from the main menu
2. Enter the ID of the task you want to delete
3. Confirm deletion when prompted

#### Marking Task as Done
1. Select option `5` from the main menu
2. Enter the ID of the task to toggle its status
3. Status will switch between "pending" and "done"

#### Exiting the Application
1. Select option `6` from the main menu
2. All tasks will be cleared from memory
3. Application will terminate

## Development Setup

### Project Structure
```
src/
├── models/
│   └── task.py          # Task entity and in-memory storage
├── services/
│   └── todo_service.py  # Business logic for todo operations
├── cli/
│   └── main.py          # Console interface and menu system
└── lib/
    └── utils.py         # Utility functions
```

### Running Tests
```bash
# Install pytest if not already available
pip install pytest

# Run all tests
python -m pytest tests/

# Run specific test files
python -m pytest tests/unit/test_task.py
python -m pytest tests/unit/test_todo_service.py
python -m pytest tests/integration/test_cli_flow.py
```

### Key Components

#### Task Model (`src/models/task.py`)
- Defines the Task class structure
- Handles in-memory storage using dictionary and list
- Manages auto-incrementing IDs

#### Todo Service (`src/services/todo_service.py`)
- Implements business logic for task operations
- Validates inputs according to defined rules
- Manages task creation, retrieval, update, and deletion

#### CLI Interface (`src/cli/main.py`)
- Provides console-based user interface
- Handles user input and menu navigation
- Displays formatted output to the user

## Common Operations

### Adding Multiple Tasks
```text
Todo Console App
================
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task as Done/Undone
6. Exit

Choice: 1
Enter task title: Complete project proposal
Enter task description (optional, press Enter to skip): Write up the project proposal for review
Task added successfully!
ID: 1
Title: Complete project proposal
Status: pending

Choice: 1
Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, bread
Task added successfully!
ID: 2
Title: Buy groceries
Status: pending
```

### Updating Task Status
```text
Choice: 2
Task List:
--------
ID  | Status | Title
----|--------|------------------
1   | [ ]    | Complete project proposal
2   | [ ]    | Buy groceries

Choice: 5
Enter task ID to toggle status: 1
Task status updated!
ID: 1 is now done

Choice: 2
Task List:
--------
ID  | Status | Title
----|--------|------------------
1   | [X]    | Complete project proposal
2   | [ ]    | Buy groceries
```

## Error Handling

### Common Error Messages
- `Error: Title cannot be empty.` - When trying to add a task without a title
- `Error: Task with ID {id} does not exist.` - When referencing a non-existent task
- `Error: Title exceeds 200 characters.` - When title is too long

### Troubleshooting
1. **Application won't start**: Ensure Python 3.8+ is installed and accessible
2. **Invalid menu choices**: Use only the number options shown in the menu
3. **Task operations failing**: Verify task IDs exist before attempting operations

## Data Lifecycle

### In-Memory Storage
- All tasks are stored only in memory during the session
- Data is lost when the application exits
- No file or database persistence
- Efficient O(1) lookup using dictionary structure

### Session Behavior
- Starts with empty task list
- Tasks accumulate in memory during session
- All data cleared upon exit
- No data shared between sessions

## Next Steps

1. **Explore the source code** in the `src/` directory
2. **Run the tests** to understand expected behavior
3. **Try all menu options** to familiarize yourself with the interface
4. **Review the contracts** in the `contracts/` directory for interface specifications
5. **Check the data model** in `data-model.md` for entity definitions