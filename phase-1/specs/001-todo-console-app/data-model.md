# Data Model: Todo In-Memory Python Console App

**Feature**: 001-todo-console-app
**Date**: 2026-01-02
**Status**: Complete

## Overview

This document defines the data model for the Todo In-Memory Python Console App, specifying the structure of data entities, their relationships, and validation rules based on the feature specification.

## Entity Definitions

### Task Entity

**Description**: Core entity representing a todo item that users can create, read, update, and delete.

**Attributes**:
- `id` (int, required): Unique identifier for the task, auto-incremented
  - Validation: Must be a positive integer
  - Constraints: Unique across all tasks in memory
- `title` (str, required): Title or subject of the task
  - Validation: Must not be empty or only whitespace
  - Constraints: Maximum 200 characters
- `description` (str, optional): Detailed description of the task
  - Validation: Optional field, can be empty
  - Constraints: Maximum 1000 characters
- `status` (str, required): Current status of the task
  - Values: "pending" or "done"
  - Default: "pending"
  - Validation: Must be one of the allowed values
- `created_at` (datetime, required): Timestamp when the task was created
  - Format: ISO 8601 datetime string
  - Default: Current timestamp when task is created
- `updated_at` (datetime, required): Timestamp when the task was last updated
  - Format: ISO 8601 datetime string
  - Default: Same as created_at initially, updated on any modification

### Task Collection

**Description**: In-memory storage structure for all tasks during the session.

**Structure**:
- `tasks` (dict): Dictionary mapping task IDs to Task objects for O(1) lookup
  - Key: task ID (int)
  - Value: Task object
- `task_list` (list): List maintaining tasks in creation order for display
  - Items: Task objects in chronological order of creation
- `next_id` (int): Counter for auto-incrementing task IDs
  - Starts at 1 and increments with each new task

## Validation Rules

### Task Creation Validation
1. Title must be provided and not empty after trimming whitespace
2. Title must be 200 characters or less
3. Description, if provided, must be 1000 characters or less
4. Status must be either "pending" or "done" (default: "pending")
5. ID must be unique across all existing tasks

### Task Update Validation
1. Task with given ID must exist
2. If title is provided, it must not be empty after trimming whitespace
3. If title is provided, it must be 200 characters or less
4. If description is provided, it must be 1000 characters or less
5. If status is provided, it must be either "pending" or "done"

### Task Deletion Validation
1. Task with given ID must exist

### Task Status Toggle Validation
1. Task with given ID must exist
2. Status must be a valid toggle (from "pending" to "done" or vice versa)

## State Transitions

### Task Status Transitions
- From "pending" → "done" (when marking task as completed)
- From "done" → "pending" (when marking task as incomplete)

### Valid Transitions
- New Task → Status: "pending" (initial state)
- Any Status → Updated Status (on explicit status change)
- Any State → Deleted (on task deletion)

## Relationships

### Task-to-Task Relationships
- No direct relationships between tasks
- Tasks are ordered by creation order (maintained in task_list)

## Data Constraints

### Memory Constraints
- All data stored only in memory during session
- No persistence to files or databases
- Data lost when session ends

### Performance Constraints
- O(1) lookup for tasks by ID using dictionary
- O(n) for operations that require iteration through all tasks
- Maximum recommended task count: 1000 tasks per session

## Error Conditions

### Invalid Task Creation
- Empty title after whitespace trimming
- Title exceeding 200 characters
- Description exceeding 1000 characters

### Invalid Task Operations
- Attempting operations on non-existent task ID
- Invalid status values
- Invalid ID format (non-integer)

## Sample Data Structure

```python
# Example of how data would be structured in memory
tasks = {
    1: {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread, fruits",
        "status": "pending",
        "created_at": "2026-01-02T10:30:00Z",
        "updated_at": "2026-01-02T10:30:00Z"
    },
    2: {
        "id": 2,
        "title": "Write report",
        "description": "Complete monthly sales report",
        "status": "done",
        "created_at": "2026-01-02T11:15:00Z",
        "updated_at": "2026-01-02T12:45:00Z"
    }
}

task_list = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread, fruits",
        "status": "pending",
        "created_at": "2026-01-02T10:30:00Z",
        "updated_at": "2026-01-02T10:30:00Z"
    },
    {
        "id": 2,
        "title": "Write report",
        "description": "Complete monthly sales report",
        "status": "done",
        "created_at": "2026-01-02T11:15:00Z",
        "updated_at": "2026-01-02T12:45:00Z"
    }
]

next_id = 3
```