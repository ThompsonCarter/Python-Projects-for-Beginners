import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
        'Sales': [100, 150, 200, 180, 220]}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot the data
plt.plot(df['Date'], df['Sales'], color='green', marker='o', label='Sales')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.grid(True)
plt.legend()
plt.show()