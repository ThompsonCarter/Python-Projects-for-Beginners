
# Hands-On Project: Simple Calculator

# Step 1: Define the function that will perform the calculation
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

# Step 2: Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Step 3: Call the calculator function and print the result
result = calculator(num1, num2, operator)
print(f"The result is: {result}")
    