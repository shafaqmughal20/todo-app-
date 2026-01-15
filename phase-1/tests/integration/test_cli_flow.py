import sys
from io import StringIO
from unittest.mock import patch
from src.models.task import InMemoryStorage
from src.services.todo_service import TodoService
from src.cli.main import TodoConsoleApp


class TestCLIIntegration:
    """Integration tests for CLI flows."""

    def setup_method(self):
        """Set up a fresh app for each test."""
        self.storage = InMemoryStorage()
        self.service = TodoService(self.storage)
        self.app = TodoConsoleApp(self.service)

    def test_add_task_flow(self):
        """Test the complete add task flow."""
        # Simulate user input for adding a task
        user_inputs = [
            "1",  # Add task option
            "Test Task",  # Title
            "Test Description",  # Description
            "6"   # Exit option
        ]

        with patch('builtins.input', side_effect=user_inputs):
            # Capture printed output
            captured_output = StringIO()
            sys.stdout = captured_output

            self.app.run()

            # Restore stdout
            sys.stdout = sys.__stdout__

            output = captured_output.getvalue()

            # Verify the task was added successfully
            assert "Task added successfully!" in output
            assert "Test Task" in output

            # Verify the task exists in storage
            tasks = self.service.get_all_tasks()
            assert len(tasks) == 1
            assert tasks[0].title == "Test Task"
            assert tasks[0].description == "Test Description"

    def test_list_tasks_flow(self):
        """Test the complete list tasks flow."""
        # Add a task first
        self.service.add_task("Test Task", "Test Description")

        # Simulate user input for listing tasks
        user_inputs = [
            "2",  # List tasks option
            "6"   # Exit option
        ]

        with patch('builtins.input', side_effect=user_inputs):
            # Capture printed output
            captured_output = StringIO()
            sys.stdout = captured_output

            self.app.run()

            # Restore stdout
            sys.stdout = sys.__stdout__

            output = captured_output.getvalue()

            # Verify tasks are listed
            assert "Test Task" in output
            assert "[ ]" in output  # Pending status

    def test_update_task_flow(self):
        """Test the complete update task flow."""
        # Add a task first
        task = self.service.add_task("Original Task", "Original Description")

        # Simulate user input for updating task
        user_inputs = [
            "3",  # Update task option
            str(task.id),  # Task ID
            "Updated Task",  # New title
            "Updated Description",  # New description
            "6"   # Exit option
        ]

        with patch('builtins.input', side_effect=user_inputs):
            # Capture printed output
            captured_output = StringIO()
            sys.stdout = captured_output

            self.app.run()

            # Restore stdout
            sys.stdout = sys.__stdout__

            output = captured_output.getvalue()

            # Verify the task was updated successfully
            assert "Task updated successfully!" in output
            assert "Updated Task" in output

            # Verify the task was updated in storage
            updated_task = self.service.get_task(task.id)
            assert updated_task.title == "Updated Task"
            assert updated_task.description == "Updated Description"

    def test_delete_task_flow(self):
        """Test the complete delete task flow."""
        # Add a task first
        task = self.service.add_task("Test Task", "Test Description")

        # Simulate user input for deleting task
        user_inputs = [
            "4",  # Delete task option
            str(task.id),  # Task ID
            "y",  # Confirm deletion
            "6"   # Exit option
        ]

        with patch('builtins.input', side_effect=user_inputs):
            # Capture printed output
            captured_output = StringIO()
            sys.stdout = captured_output

            self.app.run()

            # Restore stdout
            sys.stdout = sys.__stdout__

            output = captured_output.getvalue()

            # Verify the task was deleted successfully
            assert "Task deleted successfully!" in output

            # Verify the task no longer exists in storage
            tasks = self.service.get_all_tasks()
            assert len(tasks) == 0

    def test_mark_task_done_flow(self):
        """Test the complete mark task as done flow."""
        # Add a task first
        task = self.service.add_task("Test Task", "Test Description")

        # Simulate user input for marking task as done
        user_inputs = [
            "5",  # Mark task as done option
            str(task.id),  # Task ID
            "6"   # Exit option
        ]

        with patch('builtins.input', side_effect=user_inputs):
            # Capture printed output
            captured_output = StringIO()
            sys.stdout = captured_output

            self.app.run()

            # Restore stdout
            sys.stdout = sys.__stdout__

            output = captured_output.getvalue()

            # Verify the task status was updated
            assert "Task marked as done!" in output
            assert "is now done" in output

            # Verify the task status was updated in storage
            updated_task = self.service.get_task(task.id)
            assert updated_task.status == "done"