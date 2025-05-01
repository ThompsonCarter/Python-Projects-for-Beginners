
def display_menu():
    print("Personal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Save and Exit")

def add_transaction_prompt(budget, transaction_type):
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    task = Task(description, amount, category, date)
    if transaction_type == 'income':
        budget.add_transaction(task)
    elif transaction_type == 'expense':
        task.amount = -task.amount  # Make the amount negative for expenses
        budget.add_transaction(task)
    