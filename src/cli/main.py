from typing import Optional
from src.services.todo_service import TodoService
from src.lib.utils import (
    validate_task_title, validate_task_description,
    format_task_display, format_task_details,
    handle_input_error, confirm_action
)


class TodoConsoleApp:
    """Main console application for the Todo app."""

    def __init__(self, service: TodoService = None):
        """
        Initialize the console app.

        Args:
            service: TodoService instance (optional, creates new if not provided)
        """
        self.service = service if service is not None else TodoService()
        self.running = True

    def display_menu(self):
        """Display the main menu options."""
        print("\n---Todo Console App---")
        print("=================================")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")
        print("=================================")
    def handle_add_task(self):
        """Handle adding a new task."""
        print("\nEnter task details:")
        title = input("Enter task title: ").strip()

        if not validate_task_title(title):
            print(handle_input_error("Title cannot be empty and must be 200 characters or less"))
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()

        if not validate_task_description(description):
            print(handle_input_error("Description exceeds 1000 characters"))
            return

        try:
            task = self.service.add_task(title, description)
            print("\nTask added successfully!")
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Status: {task.status}")
        except ValueError as e:
            print(handle_input_error(str(e)))

    def handle_list_tasks(self):
        """Handle listing all tasks."""
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\nTask List:")
        print("--------")
        print("ID  | Status | Title")
        print("----|--------|------------------")

        for task in tasks:
            formatted_task = format_task_display(task)
            print(formatted_task)

    def handle_update_task(self):
        """Handle updating an existing task."""
        try:
            task_id_input = input("\nEnter task ID to update: ").strip()
            if not task_id_input.isdigit():
                print(handle_input_error("Task ID must be a number"))
                return

            task_id = int(task_id_input)
            task = self.service.get_task(task_id)

            print(f"\nCurrent task: {format_task_details(task)}")

            new_title = input(f"\nEnter new title (leave blank to keep '{task.title}'): ").strip()
            new_description = input(f"Enter new description (leave blank to keep current): ").strip()

            # Use None to indicate no change, or the new value if provided
            title_to_update = new_title if new_title != "" else None
            description_to_update = new_description if new_description != "" else None

            # If title is provided, validate it
            if title_to_update is not None and not validate_task_title(title_to_update):
                print(handle_input_error("Title cannot be empty and must be 200 characters or less"))
                return

            # If description is provided, validate it
            if description_to_update is not None and not validate_task_description(description_to_update):
                print(handle_input_error("Description exceeds 1000 characters"))
                return

            updated_task = self.service.update_task(task_id, title_to_update, description_to_update)
            print("\nTask updated successfully!")
            print(f"ID: {updated_task.id}")
            print(f"Title: {updated_task.title}")
            print(f"Description: {updated_task.description}")
        except KeyError as e:
            print(handle_input_error(str(e)))
        except ValueError as e:
            print(handle_input_error(str(e)))

    def handle_delete_task(self):
        """Handle deleting a task."""
        try:
            task_id_input = input("\nEnter task ID to delete: ").strip()
            if not task_id_input.isdigit():
                print(handle_input_error("Task ID must be a number"))
                return

            task_id = int(task_id_input)
            task = self.service.get_task(task_id)

            if confirm_action(f"Are you sure you want to delete task '{task.title}'?"):
                result = self.service.delete_task(task_id)
                if result:
                    print("\nTask deleted successfully!")
                else:
                    print(handle_input_error(f"Task with ID {task_id} does not exist"))
            else:
                print("\nTask deletion cancelled.")
        except KeyError as e:
            print(handle_input_error(str(e)))

    def handle_mark_done(self):
        """Handle marking a task as done."""
        try:
            task_id_input = input("\nEnter task ID to mark as done: ").strip()
            if not task_id_input.isdigit():
                print(handle_input_error("Task ID must be a number"))
                return

            task_id = int(task_id_input)
            task = self.service.mark_task_done(task_id)
            print(f"\nTask marked as done!")
            print(f"ID: {task.id} is now {task.status}")
        except KeyError as e:
            print(handle_input_error(str(e)))

    def handle_exit(self):
        """Handle exiting the application."""
        print("\nThank you for using Todo Console App!")
        print("All tasks have been cleared from memory.")
        print("Goodbye!")
        self.running = False

    def run(self):
        """Run the main application loop."""
        print("Welcome to Todo Console App!")

        while self.running:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.handle_add_task()
            elif choice == "2":
                self.handle_list_tasks()
            elif choice == "3":
                self.handle_update_task()
            elif choice == "4":
                self.handle_delete_task()
            elif choice == "5":
                self.handle_mark_done()
            elif choice == "6":
                self.handle_exit()
            else:
                print(handle_input_error("Invalid choice. Please enter a number between 1-6."))


def main():
    """Main entry point for the application."""
    app = TodoConsoleApp()
    app.run()


if __name__ == "__main__":
    main()