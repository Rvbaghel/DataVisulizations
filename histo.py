import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sma.csv")

# plt.figure(figsize=(8,5))
# plt.hist(df['sales'], bins=8, color='orange', edgecolor='black')
# plt.title("Distribution of Sales")
# plt.xlabel("Sales Value")
# plt.ylabel("Count")
# plt.show()

# plt.figure(figsize=(8,5))
# plt.hist(df['visitors'], bins=6, color='purple', edgecolor='black')
# plt.title("Distribution of Visitors")
# plt.xlabel("Visitors Count")
# plt.ylabel("Frequency")
# plt.show()


plt.figure(figsize=(10,5))

# Plot two histograms on same chart
plt.hist(df['price'], bins=5, alpha=0.5, label='Price', color='blue',edgecolor='black')
# plt.hist(df['cost'], bins=10, alpha=0.5, label='Cost', color='orange')

plt.title("Price")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
