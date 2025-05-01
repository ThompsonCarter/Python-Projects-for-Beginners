# Saving tasks to a file
with open('tasks.txt', 'w') as file:
    for task in self.tasks:
        file.write(f"{task.name},{task.due_date},{task.status}
")

# Loading tasks from a file
with open('tasks.txt', 'r') as file:
    for line in file:
        name, due_date, status = line.strip().split(',')
        task = Task(name, due_date)
        if status == "Completed":
            task.mark_as_completed()
        self.add_task(task)
