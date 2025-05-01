
class Budget:
    def __init__(self, total_budget):
        self.total_budget = total_budget
        self.balance = total_budget
        self.transactions = []

    def add_transaction(self, task):
        self.transactions.append(task)
        self.balance -= task.amount

    def get_summary(self):
        total_income = sum([t.amount for t in self.transactions if t.amount > 0])
        total_expenses = sum([t.amount for t in self.transactions if t.amount < 0])
        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": self.balance
        }
    