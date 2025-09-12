import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sma.csv")


# plt.figure(figsize=(8,6))  # chart size
# plt.bar(
#     df['category'],
#     df['sales'],
#     color='red',           # bar color
#     edgecolor='green',     # border color
#     width=0.6,             # bar width
#     alpha=0.8,             # transparency
# )

# plt.title("Category Wise Sales", fontsize=16, fontweight="bold", color="blue")
# plt.xlabel("Category", fontsize=12)
# plt.ylabel("Sales", fontsize=12)
# plt.xticks(rotation=50)
# plt.grid(axis='y', linestyle=':', alpha=0.7)
# plt.show()

# df = pd.read_csv("sma.csv")

# # Group sales by category
# sales_by_cat = df.groupby("category")["sales"].sum()

# plt.figure(figsize=(8,6))
# plt.bar(sales_by_cat.index, sales_by_cat.values, color="skyblue", edgecolor="black")
# plt.title("Total Sales by Category")
# plt.xlabel("Category")
# plt.ylabel("Total Sales")
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.show()

# # Example dataset has: category, region, sales
# sales_region = df.groupby(["region","category"])["sales"].sum().unstack()

# sales_region.plot(kind="bar", figsize=(10,6))
# plt.title("Sales by Region and Category")
# plt.xlabel("Region")
# plt.ylabel("Sales")
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.show()
# sales_region = df.groupby(["region","category"])["sales"].sum().unstack()

# region_sale=df.groupby('category')['profit'].sum()
# region_sale.plot(kind="bar",figsize=(10,6))
# plt.title("Sales by Region and Category")
# plt.xlabel("Region")
# plt.ylabel("Sales")
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.show()

# plt.figure(figsize=(12,6))
# plt.plot(df['date'], df['price'], marker='o', linestyle='-', color='green')

# plt.title("Price Trend Over Time")
# plt.xlabel("Date")
# plt.ylabel("Price")

# # Show every 10th label only
# plt.xticks(df['date'][::10], rotation=30)

# plt.figure(figsize=(12,6))
# plt.plot(df['date'], df['temperature_c'], marker='D', linestyle=':', color='orange')
# plt.title("Temperature Trend Over Time")
# plt.xlabel("Date")
# plt.ylabel("Temperature (°C)")
# plt.xticks(df['date'][::10],rotation=45)
# plt.show()

df['date']=pd.to_datetime(df['date'],dayfirst=True)
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month

print(df.info())

