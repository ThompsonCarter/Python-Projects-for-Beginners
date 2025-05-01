import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a line plot
plt.plot(x, y)
plt.title("Square Numbers")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()