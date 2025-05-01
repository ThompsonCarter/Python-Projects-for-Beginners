
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
