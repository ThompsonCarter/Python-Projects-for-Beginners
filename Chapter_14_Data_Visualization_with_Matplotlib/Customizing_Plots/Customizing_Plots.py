import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a customized line plot
plt.plot(x, y, color="green", linestyle="--", marker="o")
plt.title("Customized Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()