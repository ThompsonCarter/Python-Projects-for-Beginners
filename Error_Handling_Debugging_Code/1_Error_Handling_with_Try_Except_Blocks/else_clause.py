
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
except ValueError as e:
    print(f"Invalid input. Please enter a valid number: {e}")
else:
    print(f"Result: {result}")
