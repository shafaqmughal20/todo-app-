# CLI Interface Contract: Todo In-Memory Python Console App

**Feature**: 001-todo-console-app
**Date**: 2026-01-02
**Status**: Complete

## Overview

This document defines the contract for the command-line interface of the Todo In-Memory Python Console App. It specifies the user interactions, commands, input formats, and expected outputs.

## CLI Interface Definition

### Main Menu Options

The application presents users with a main menu with the following numbered options:

```
Todo Console App
================
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task as Done/Undone
6. Exit
```

### Command Specifications

#### 1. Add Task
- **User Action**: Select option 1 from main menu
- **Input Required**:
  - Title (string, required)
  - Description (string, optional)
- **User Prompts**:
  ```
  Enter task title:
  Enter task description (optional, press Enter to skip):
  ```
- **Success Response**:
  ```
  Task added successfully!
  ID: {id}
  Title: {title}
  Status: pending
  ```
- **Error Responses**:
  - Empty title: "Error: Title cannot be empty. Task not added."
  - Title too long: "Error: Title exceeds 200 characters. Task not added."

#### 2. List Tasks
- **User Action**: Select option 2 from main menu
- **Input Required**: None
- **Success Response**:
  ```
  Task List:
  --------
  ID  | Status | Title
  ----|--------|------------------
  1   | [ ]    | Buy groceries
  2   | [X]    | Write report
  3   | [ ]    | Schedule meeting
  ```
  - If no tasks exist: "No tasks found."
- **Error Responses**: None

#### 3. Update Task
- **User Action**: Select option 3 from main menu
- **Input Required**:
  - Task ID (integer, required)
  - New title (string, optional)
  - New description (string, optional)
- **User Prompts**:
  ```
  Enter task ID to update:
  Enter new title (leave blank to keep current):
  Enter new description (leave blank to keep current):
  ```
- **Success Response**:
  ```
  Task updated successfully!
  ID: {id}
  Title: {new_title}
  Description: {new_description}
  ```
- **Error Responses**:
  - Invalid ID: "Error: Task with ID {id} does not exist."
  - Empty title: "Error: Title cannot be empty."

#### 4. Delete Task
- **User Action**: Select option 4 from main menu
- **Input Required**: Task ID (integer, required)
- **User Prompts**:
  ```
  Enter task ID to delete:
  Are you sure you want to delete task '{title}'? (y/N):
  ```
- **Success Response**:
  ```
  Task deleted successfully!
  ```
- **Error Responses**:
  - Invalid ID: "Error: Task with ID {id} does not exist."
  - Confirmation denied: "Task deletion cancelled."

#### 5. Mark Task as Done/Undone
- **User Action**: Select option 5 from main menu
- **Input Required**: Task ID (integer, required)
- **User Prompts**:
  ```
  Enter task ID to toggle status:
  ```
- **Success Response**:
  ```
  Task status updated!
  ID: {id} is now {status}
  ```
- **Error Responses**:
  - Invalid ID: "Error: Task with ID {id} does not exist."

#### 6. Exit
- **User Action**: Select option 6 from main menu
- **Input Required**: None
- **Success Response**:
  ```
  Thank you for using Todo Console App!
  All tasks have been cleared from memory.
  Goodbye!
  ```
- **Error Responses**: None

## Input Validation Rules

### Task ID Validation
- Must be a positive integer
- Must correspond to an existing task
- Error message: "Invalid task ID. Please enter a valid task ID."

### Title Validation
- Must not be empty after whitespace trimming
- Must be 200 characters or less
- Error messages:
  - Empty: "Title cannot be empty."
  - Too long: "Title exceeds 200 characters."

### Description Validation
- Optional field
- Must be 1000 characters or less if provided
- Error message: "Description exceeds 1000 characters."

## Error Handling Contract

### General Error Format
```
Error: {specific_error_message}
```

### Validation Error Types
1. **InputError**: Invalid input format or values
2. **NotFoundError**: Requested resource does not exist
3. **ValidationError**: Input fails validation rules

## State Management Contract

### Session Lifecycle
1. **Start**: App initializes empty task storage
2. **Operations**: Tasks added/modified/deleted in memory
3. **End**: All tasks cleared from memory, session terminated

### Data Persistence
- No data persistence beyond session
- All data lost when application exits
- Confirmation required for destructive operations

## Exit Codes

- **0**: Normal exit
- **1**: Error occurred during operation
- **2**: Invalid user input

## User Experience Standards

### Response Time
- All operations should complete within 2 seconds
- Immediate feedback for user actions

### Error Messages
- Clear and actionable error messages
- Suggest corrective actions when possible
- Maintain consistent error message format

### Confirmation Prompts
- Required for destructive operations (delete)
- Optional to skip with default values
- Case-insensitive (accept Y/y/N/n)