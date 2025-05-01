
import json

def save_data(budget, filename="budget_data.json"):
    with open(filename, 'w') as file:
        data = {
            "total_budget": budget.total_budget,
            "transactions": [{"description": t.description, "amount": t.amount, "category": t.category, "date": t.date} for t in budget.transactions]
        }
        json.dump(data, file)

def load_data(filename="budget_data.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            budget = Budget(data["total_budget"])
            for transaction in data["transactions"]:
                task = Task(transaction["description"], transaction["amount"], transaction["category"], transaction["date"])
                budget.add_transaction(task)
            return budget
    except FileNotFoundError:
        return Budget(0)  # Start with zero budget if no data exists
    