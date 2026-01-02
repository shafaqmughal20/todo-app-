from typing import List
from src.models.task import Task, InMemoryStorage


class TodoService:
    """
    Business logic layer for todo operations.
    """

    def __init__(self, storage: InMemoryStorage = None):
        """
        Initialize the TodoService.

        Args:
            storage: In-memory storage instance (optional, creates new if not provided)
        """
        self.storage = storage if storage is not None else InMemoryStorage()

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task.

        Args:
            title: Task title (required)
            description: Task description (optional)

        Returns:
            The created Task object

        Raises:
            ValueError: If title is invalid
        """
        return self.storage.add_task(title, description)

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
        return self.storage.get_task(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in creation order.

        Returns:
            List of all Task objects in creation order
        """
        return self.storage.get_all_tasks()

    def update_task(self, task_id: int, title: str = None, description: str = None) -> Task:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated Task object

        Raises:
            KeyError: If task with given ID doesn't exist
            ValueError: If new values are invalid
        """
        return self.storage.update_task(task_id, title, description)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if it didn't exist
        """
        return self.storage.delete_task(task_id)

    def mark_task_done(self, task_id: int) -> Task:
        """
        Mark the status of a task as done.

        Args:
            task_id: The ID of the task to mark as done

        Returns:
            The updated Task object

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        return self.storage.mark_task_done(task_id)

    def toggle_task_status(self, task_id: int) -> Task:
        """
        Toggle the status of a task between pending and done.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task object

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        return self.storage.toggle_task_status(task_id)

    def get_next_task_id(self) -> int:
        """
        Get the next available task ID.

        Returns:
            The next available task ID
        """
        return self.storage.get_next_id()