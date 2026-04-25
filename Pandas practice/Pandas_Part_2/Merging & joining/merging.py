import pandas as pd

#pd.merge(df1,df2,on="Column_Name",how="type of join")
# inner ,outer, left, right

# customer dataframes
df_customers = pd.DataFrame( {
  'CustomerID':[1,2,3],
  'Name':['Ramesh','Suresh','kalpesh']
})

#Order dataframe
df_orders = pd.DataFrame({
  'CustomerID':[1,2,4],
  'OrderAmount':[250,450,350]
})

#merge
df_mearge = pd.merge(df_customers,df_orders,on='CustomerID',how='cross')
print("Inner join")

print(df_mearge)

"""
1df = m rows
2df = n rows
m*n rows
"""