from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List
import json


@dataclass
class Task:
    """
    Represents a todo task with ID, title, description, status, and timestamps.
    """
    id: int
    title: str
    description: str = ""
    status: str = "pending"  # Either "pending" or "done"
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title.strip():
            raise ValueError("Title cannot be empty or only whitespace")
        if len(self.title) > 200:
            raise ValueError("Title exceeds 200 characters")
        if len(self.description) > 1000:
            raise ValueError("Description exceeds 1000 characters")
        if self.status not in ["pending", "done"]:
            raise ValueError("Status must be either 'pending' or 'done'")


class InMemoryStorage:
    """
    Handles in-memory storage of tasks using dictionaries and lists.
    """

    def __init__(self):
        # Dictionary mapping task IDs to Task objects for O(1) lookup
        self._tasks: Dict[int, Task] = {}
        # List maintaining tasks in creation order for display
        self._task_list: List[Task] = []
        # Counter for auto-incrementing task IDs
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to storage.

        Args:
            title: The task title (required)
            description: The task description (optional)

        Returns:
            The created Task object with assigned ID
        """
        if not title.strip():
            raise ValueError("Title cannot be empty")

        task_id = self._next_id
        self._next_id += 1

        task = Task(
            id=task_id,
            title=title.strip(),
            description=description.strip(),
            status="pending"
        )

        self._tasks[task_id] = task
        self._task_list.append(task)

        return task

    def get_task(self, task_id: int) -> Task:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")
        return self._tasks[task_id]

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in creation order.

        Returns:
            List of all Task objects in creation order
        """
        return self._task_list.copy()

    def update_task(self, task_id: int, title: str = None, description: str = None) -> Task:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated Task object
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

        task = self._tasks[task_id]

        # Update title if provided
        if title is not None:
            if title.strip() == "":
                raise ValueError("Title cannot be empty")
            if len(title) > 200:
                raise ValueError("Title exceeds 200 characters")
            task.title = title.strip()

        # Update description if provided
        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description exceeds 1000 characters")
            task.description = description.strip()

        task.updated_at = datetime.now()
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if it didn't exist
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]
        del self._tasks[task_id]

        # Remove from task list while preserving order
        self._task_list.remove(task)

        return True

    def mark_task_done(self, task_id: int) -> Task:
        """
        Mark the status of a task as done.

        Args:
            task_id: The ID of the task to mark as done

        Returns:
            The updated Task object
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

        task = self._tasks[task_id]
        task.status = "done"
        task.updated_at = datetime.now()

        return task

    def toggle_task_status(self, task_id: int) -> Task:
        """
        Toggle the status of a task between pending and done.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task object
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")

        task = self._tasks[task_id]
        task.status = "done" if task.status == "pending" else "pending"
        task.updated_at = datetime.now()

        return task

    def get_next_id(self) -> int:
        """
        Get the next available task ID without consuming it.

        Returns:
            The next available task ID
        """
        return self._next_id