import matplotlib.pyplot as plt
import numpy as np

# Input two arrays
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 25, 30, 35])

# (a) Line Chart
plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o', color='blue')
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# (b) Bar Chart
plt.figure(figsize=(6,4))
plt.bar(x, y, color='green')
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# (c) Pie Chart
plt.figure(figsize=(6,6))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()

# (d) Scatter Chart
plt.figure(figsize=(6,4))
plt.scatter(x, y, color='red')
plt.title("Scatter Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# (e) Histogram
plt.figure(figsize=(6,4))
plt.hist(y, bins=5, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()
