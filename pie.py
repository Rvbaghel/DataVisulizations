import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sma.csv")



# print(df.head(3))
# region_sale=df.groupby('region')['sales'].sum()
# ex=[0.1 if val==region_sale.max() else 0 for val in region_sale]
# plt.pie(region_sale,labels=region_sale.index,autopct='%1.1f%%',startangle=90,shadow=True,explode=ex)
# plt.title('Sales Of region')
# plt.show()

# sales_by_cat = df.groupby("category")["sales"].sum()

# plt.figure(figsize=(7,7))
# explode = [0.1 if val == sales_by_cat.max() else 0 for val in sales_by_cat]  # highlight biggest slice

# plt.pie(
#     sales_by_cat,
#     labels=sales_by_cat.index,
#     autopct="%1.1f%%",
#     startangle=90,
#     explode=explode,
#     shadow=True
# )

# plt.title("Sales Share by Category (Highlighting Largest)")
# plt.show()

# Group sales by category
sales_by_cat = df.groupby("category")["sales"].sum()

# # Find the category with maximum sales
# top_category = sales_by_cat.idxmax()     # gives category name
# top_value = sales_by_cat.max()           # gives value
# top_percent = (top_value / sales_by_cat.sum()) * 100  # percentage

# print(f"Highest Sales: {top_category} with {top_value:.2f} sales ({top_percent:.1f}%)")

# # Pie chart with highlight
# explode = [0.1 if val == sales_by_cat.max() else 0 for val in sales_by_cat]

# plt.figure(figsize=(7,7))
# plt.pie(
#     sales_by_cat,
#     labels=sales_by_cat.index,
#     autopct="%1.1f%%",
#     startangle=90,
#     explode=explode,
#     shadow=True
# )
# plt.title("Sales Share by Category (Highlighting Largest)")
# plt.show()
