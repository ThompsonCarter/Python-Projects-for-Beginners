
try:
    file = open("file.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
finally:
    file.close()  # Ensures the file is closed even if an error occurs
