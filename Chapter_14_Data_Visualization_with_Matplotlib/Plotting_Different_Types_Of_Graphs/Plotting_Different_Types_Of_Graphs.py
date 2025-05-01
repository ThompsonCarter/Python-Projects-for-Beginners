import matplotlib.pyplot as plt

# Data for Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

# Create a bar chart
plt.bar(categories, values, color='purple')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Data for Histogram
import numpy as np
data = np.random.randn(1000)  # Generate random data
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Data for Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()