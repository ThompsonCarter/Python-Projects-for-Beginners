
def main():
    budget = load_data()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction_prompt(budget, 'income')
        elif choice == "2":
            add_transaction_prompt(budget, 'expense')
        elif choice == "3":
            summary = budget.get_summary()
            print(f"Total Income: {summary['total_income']}")
            print(f"Total Expenses: {summary['total_expenses']}")
            print(f"Remaining Balance: {summary['balance']}")
        elif choice == "4":
            save_data(budget)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
main()
    