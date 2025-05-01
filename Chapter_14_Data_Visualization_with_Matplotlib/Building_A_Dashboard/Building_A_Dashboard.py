import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
        'Sales': [100, 150, 200, 180, 220],
        'Expenses': [80, 120, 160, 140, 180]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting Sales and Expenses on two different axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plotting sales on ax1
ax1.plot(df['Date'], df['Sales'], color='green', marker='o')
ax1.set_title("Sales Trend")
ax1.set_xlabel("Date")
ax1.set_ylabel("Sales")

# Plotting expenses on ax2
ax2.plot(df['Date'], df['Expenses'], color='red', marker='x')
ax2.set_title("Expenses Trend")
ax2.set_xlabel("Date")
ax2.set_ylabel("Expenses")

plt.tight_layout()  # Adjusts spacing between plots
plt.show()