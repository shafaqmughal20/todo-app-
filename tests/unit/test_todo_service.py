import pytest
from src.services.todo_service import TodoService
from src.models.task import InMemoryStorage, Task


class TestTodoService:
    """Unit tests for the TodoService."""

    def setup_method(self):
        """Set up a fresh service for each test."""
        self.storage = InMemoryStorage()
        self.service = TodoService(self.storage)

    def test_add_task_success(self):
        """Test adding a task successfully."""
        task = self.service.add_task("Test Task", "Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status == "pending"

    def test_add_task_without_description(self):
        """Test adding a task without description."""
        task = self.service.add_task("Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""

    def test_add_task_empty_title_error(self):
        """Test that adding a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.add_task("")

    def test_add_task_whitespace_title_error(self):
        """Test that adding a task with whitespace title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.add_task("   ")

    def test_get_task_success(self):
        """Test getting an existing task."""
        added_task = self.service.add_task("Test Task")
        retrieved_task = self.service.get_task(added_task.id)

        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title

    def test_get_task_not_found(self):
        """Test that getting a non-existent task raises KeyError."""
        with pytest.raises(KeyError, match="Task with ID 999 does not exist"):
            self.service.get_task(999)

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when none exist."""
        tasks = self.service.get_all_tasks()

        assert len(tasks) == 0

    def test_get_all_tasks_with_tasks(self):
        """Test getting all tasks when some exist."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")

        tasks = self.service.get_all_tasks()

        assert len(tasks) == 2
        assert tasks[0].id == task1.id
        assert tasks[1].id == task2.id

    def test_update_task_success(self):
        """Test updating an existing task."""
        original_task = self.service.add_task("Original Task", "Original Description")
        updated_task = self.service.update_task(
            original_task.id,
            title="Updated Task",
            description="Updated Description"
        )

        assert updated_task.id == original_task.id
        assert updated_task.title == "Updated Task"
        assert updated_task.description == "Updated Description"

    def test_update_task_partial(self):
        """Test updating only title of a task."""
        original_task = self.service.add_task("Original Task", "Original Description")
        updated_task = self.service.update_task(
            original_task.id,
            title="Updated Task"
        )

        assert updated_task.id == original_task.id
        assert updated_task.title == "Updated Task"
        assert updated_task.description == "Original Description"  # Should remain unchanged

    def test_update_task_not_found(self):
        """Test that updating a non-existent task raises KeyError."""
        with pytest.raises(KeyError, match="Task with ID 999 does not exist"):
            self.service.update_task(999, title="Updated Task")

    def test_delete_task_success(self):
        """Test deleting an existing task."""
        task = self.service.add_task("Test Task")
        result = self.service.delete_task(task.id)

        assert result is True
        assert len(self.service.get_all_tasks()) == 0

    def test_delete_task_not_found(self):
        """Test deleting a non-existent task."""
        result = self.service.delete_task(999)

        assert result is False

    def test_toggle_task_status(self):
        """Test toggling task status."""
        task = self.service.add_task("Test Task")
        assert task.status == "pending"

        toggled_task = self.service.toggle_task_status(task.id)
        assert toggled_task.status == "done"

        toggled_task2 = self.service.toggle_task_status(task.id)
        assert toggled_task2.status == "pending"

    def test_toggle_task_status_not_found(self):
        """Test that toggling status of non-existent task raises KeyError."""
        with pytest.raises(KeyError, match="Task with ID 999 does not exist"):
            self.service.toggle_task_status(999)

    def test_mark_task_done(self):
        """Test marking a task as done."""
        task = self.service.add_task("Test Task")
        assert task.status == "pending"

        done_task = self.service.mark_task_done(task.id)
        assert done_task.status == "done"

        # Marking again should still be done
        done_task_again = self.service.mark_task_done(task.id)
        assert done_task_again.status == "done"

    def test_mark_task_done_not_found(self):
        """Test that marking status of non-existent task raises KeyError."""
        with pytest.raises(KeyError, match="Task with ID 999 does not exist"):
            self.service.mark_task_done(999)