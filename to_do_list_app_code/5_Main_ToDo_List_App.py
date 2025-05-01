def main():
    todo_list = ToDoList()
    todo_list.load_tasks_from_file("tasks.txt")

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task_prompt(todo_list)
        elif choice == "2":
            edit_task_prompt(todo_list)
        elif choice == "3":
            delete_task_prompt(todo_list)
        elif choice == "4":
            view_tasks_prompt(todo_list)
        elif choice == "5":
            todo_list.save_tasks_to_file("tasks.txt")
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
main()
