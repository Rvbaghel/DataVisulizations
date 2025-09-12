import pandas as pd 
import numpy as np

df=pd.read_csv('data.csv')
df2=pd.read_csv('data2.csv')

df.head(5)


# 1.         Write a Pandas program to
# sort the DataFrame first by 'name' in descending order, then by 'score' in
# ascending order.


sort_name=df['name'].sort_values(ascending=False)
sort_score=df['score'].sort_values()


# 2.         Write a Pandas program to
# change the name 'James' to 'Suresh' in name column of the data frame.
if df['name']=='James':
    df['name']='Suresh'


# 3.         Write a Pandas program to
# insert a new column in existing DataFrame.
df['new_column']=pd.DataFrame(['that','is','java','values',1])


# 5.         Write a Pandas program to
# count city wise number of people from a given of data set (city, name of the
# person).    

counts=df.groupby('city')['name'].value_counts().reindex().rename('name','citywisecount')

# 6.         Write a Pandas program to
# join the two given dataframes along rows and assign all data.
# new df name is df2

df.combine(df2)

#     Write a Pandas program to
# append rows to an existing DataFrame and display the combined data.
df.loc[len(df)]=['name','value','data']

# 9.         Write a Pandas program to
# split the following dataframe by school code and get mean, min, and max value
# of age for each school.

school_code=df['school_code']
means=df.groupby('school_code')['age'].mean()
mins=df.groupby('school_code')['age'].min()
maxs=df.groupby('school_code')['age'].max()

#       Using the following
# dataset find the mean, min, and max values of purchase amount (purch_amt) group
# by customer id (customer_id).

means=df.groupby('purch_amt')['customer_id'].mean()
mins=df.groupby('purch_amt')['customer_id'].min()
maxs=df.groupby('purch_amt')['customer_id'].max()