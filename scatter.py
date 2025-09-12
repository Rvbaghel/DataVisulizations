import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sma.csv")

# plt.scatter(df['rating'], df['conversion_rate'], color='purple', alpha=0.6)
# plt.title("Rating vs Conversion Rate")
# plt.xlabel("Rating")
# plt.ylabel("Conversion Rate")
# plt.show()

plt.scatter(df['sales'], df['profit'], color='green', alpha=0.6)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
