
# Hands-On Project: Create a To-Do List App That Saves and Loads Tasks from a File
Let’s put our file handling knowledge into practice by building a to-do list app that saves and loads tasks from a file. In this project, we’ll use file handling to persistently store tasks, so the app’s data isn’t lost when the program ends.

## Step 1: Plan the To-Do List App
Our to-do list app will have the following features:
- Add a task: Users can add a new task to the list.
- View all tasks: Users can view all the tasks in the list.
- Delete a task: Users can delete tasks that are no longer needed.
- Save and load tasks: Tasks will be saved to a file when the program ends and loaded when the program starts.

## Step 2: Write the Code
```python
def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks found.")

def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
```
