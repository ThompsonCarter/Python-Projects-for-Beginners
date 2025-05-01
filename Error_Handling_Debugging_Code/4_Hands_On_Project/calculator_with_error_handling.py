
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    print("Welcome to the calculator!")
    
    while True:
        try:
            print("
Operations: Add, Subtract, Multiply, Divide")
            operation = input("Choose an operation (or type 'exit' to quit): ").lower()

            if operation == 'exit':
                print("Exiting calculator.")
                break
            
            if operation not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation. Please try again.")
                continue

            num1 = get_number_input("Enter the first number: ")
            num2 = get_number_input("Enter the second number: ")

            if operation == 'add':
                result = add(num1, num2)
            elif operation == 'subtract':
                result = subtract(num1, num2)
            elif operation == 'multiply':
                result = multiply(num1, num2)
            elif operation == 'divide':
                result = divide(num1, num2)

            print(f"The result is: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

calculator()
