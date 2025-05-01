class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.status = "Pending"  # Default status is "Pending"
        self.due_date = due_date

    def mark_as_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"Task: {self.name}, Due Date: {self.due_date}, Status: {self.status}"
