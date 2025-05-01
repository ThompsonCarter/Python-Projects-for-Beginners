
class Task:
    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.description}: {self.amount} on {self.date}"
    