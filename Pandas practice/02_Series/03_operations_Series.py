import pandas as pd

# 1. arithmetic operations = +, -, *, /, %
s1= pd.Series([10,20,30,40])
s2 = pd.Series([1,2,3,4])
print(s1+s2)

#o/p:
# 0    11
# 1    22
# 2    33
# 3    44
# dtype: int64

# 2. Aggregation operations : sum(), min(), max(), mean()
print(s1.sum())   # o/p: 100
print(s1.mean())  #o/p: 25.0


# 3. Elementwise operations: apply()
res=s1.apply(lambda x:x**2)
print(res)

# O/p:
# 0     100
# 1     400
# 2     900
# 3    1600
# dtype: int64