import pandas as pd
import numpy as np

df=pd.read_csv('data.csv')

df['Discount price']=df['Discount price'].str.replace('$','',regex=False).str.replace(',','',regex=False).str.replace('₹','',regex=False).str.strip()

df['Discount price'].replace('', np.nan, inplace=True)

#print(df['Discount price'])

df['Discount price']=df['Discount price'].astype(float)

df=df.dropna(subset=['Discount price'])
# print(df.head(3))
# print(df.tail(3))

print(df.info())

#for the data first word in the product name

df['company_name']=df['Product Name'].str.split().str[0]




# total_sale_company_each=(df.groupby('company_name')['Discount price'].sum()
#                          .sort_values(ascending=True).reset_index()
#                          .rename(columns={'Discount price': 'Total Sales'}))
# print(total_sale_company_each)

# range_price=df[(df['Discount price']>50000) & (df['Discount price']<80000)]
# print(range_price['Product Name'])

df['Rating']=df['Rating'].str.replace('Ratings','').str.replace(' ','')

df['Rating']=df['Rating'].astype(float)

# rating_range=(df['Rating']>=3000)
# counts=rating_range['Product Name']