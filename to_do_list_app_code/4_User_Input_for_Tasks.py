def add_task_prompt(todo_list):
    name = input("Enter the task name: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    task = Task(name, due_date)
    todo_list.add_task(task)
    print("Task added successfully.")

def edit_task_prompt(todo_list):
    old_name = input("Enter the name of the task to edit: ")
    new_name = input("Enter the new task name: ")
    new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
    if todo_list.edit_task(old_name, new_name, new_due_date):
        print("Task updated successfully.")
    else:
        print("Task not found.")

def delete_task_prompt(todo_list):
    name = input("Enter the name of the task to delete: ")
    if todo_list.remove_task(name):
        print("Task deleted successfully.")
    else:
        print("Task not found.")

def view_tasks_prompt(todo_list):
    todo_list.display_tasks()
