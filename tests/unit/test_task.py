import pytest
from datetime import datetime
from src.models.task import Task


class TestTask:
    """Unit tests for the Task model."""

    def test_task_creation_with_valid_data(self):
        """Test creating a task with valid data."""
        task = Task(id=1, title="Test Task", description="Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status == "pending"
        assert isinstance(task.created_at, datetime)
        assert isinstance(task.updated_at, datetime)

    def test_task_creation_with_defaults(self):
        """Test creating a task with minimal required data."""
        task = Task(id=1, title="Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.status == "pending"

    def test_task_creation_with_status_done(self):
        """Test creating a task with 'done' status."""
        task = Task(id=1, title="Test Task", status="done")

        assert task.status == "done"

    def test_task_title_validation_empty(self):
        """Test that creating a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty or only whitespace"):
            Task(id=1, title="")

    def test_task_title_validation_whitespace_only(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty or only whitespace"):
            Task(id=1, title="   ")

    def test_task_title_validation_too_long(self):
        """Test that creating a task with title exceeding 200 chars raises ValueError."""
        long_title = "x" * 201
        with pytest.raises(ValueError, match="Title exceeds 200 characters"):
            Task(id=1, title=long_title)

    def test_task_description_validation_too_long(self):
        """Test that creating a task with description exceeding 1000 chars raises ValueError."""
        long_description = "x" * 1001
        with pytest.raises(ValueError, match="Description exceeds 1000 characters"):
            Task(id=1, title="Test Task", description=long_description)

    def test_task_status_validation_invalid(self):
        """Test that creating a task with invalid status raises ValueError."""
        with pytest.raises(ValueError, match="Status must be either 'pending' or 'done'"):
            Task(id=1, title="Test Task", status="invalid")