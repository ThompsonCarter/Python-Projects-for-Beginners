class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def edit_task(self, old_name, new_name, new_due_date):
        for task in self.tasks:
            if task.name == old_name:
                task.name = new_name
                task.due_date = new_due_date
                return True
        return False

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.name},{task.due_date},{task.status}
")

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, due_date, status = line.strip().split(',')
                    task = Task(name, due_date)
                    if status == "Completed":
                        task.mark_as_completed()
                    self.add_task(task)
        except FileNotFoundError:
            print("No previous tasks found.")
