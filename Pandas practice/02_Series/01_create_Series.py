import pandas as pd


# 1. creating series from a list
data = [10,20,30,40]
s= pd.Series(data)
print(s)    # default index 0, 1, 2, 3...

# O/P:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 2. Ex: creating series with custom Index
cus_idx = pd.Series([50,60,70,80],index=['a','b','c','d'])
print(cus_idx)

# O/P:
# a    50
# b    60
# c    70
# d    80
# dtype: int64

# 3. Creating series from dictionary
dic= {'a':10,'b':20,'c':30,'d':40}
dic_ser = pd.Series(dic)
print(dic_ser)

#O/P:
# a    10
# b    20
# c    30
# d    40
# dtype: int64

# 4. Creating series with scalar values
s = pd.Series(5,index=['a','b','c'])
print(s)

# O/P:
# a    5
# b    5
# c    5
# dtype: int64


# 5. Creating empty series
s=pd.Series()
print(s)

#O/P:
# Series([], dtype: object)