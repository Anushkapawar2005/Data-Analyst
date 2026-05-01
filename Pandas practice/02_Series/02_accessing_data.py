import pandas as pd

data = [10,20,30,40,50]
s= pd.Series(data,index=['a','b','c','d','e'])
print(s['b'])     # O/P : 20

# position based indexing
print(s.iloc[2])  # o/p: 30

# accessing multiple elements
print(s[['a','c']])
#o/p:
# a    10
# c    30
# dtype: int64