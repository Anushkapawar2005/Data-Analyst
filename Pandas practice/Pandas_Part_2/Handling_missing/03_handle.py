# dropna()

# axis = 0 means remove rows(missing value)
# axis = 1 means remove columns(missing value)

#df.dropna(axis=0,inplace=True)

# inplace=True modifies the original DataFrame instead of returning a new DataFrame.

import pandas as pd

data = {
  "Name":['Ram',None,'Radha','Aditi','Raj','Madhu','Simran','sanu'],
  "Age": [20,None,22,39,29,40,25,32],
  "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
  "Performance Score":[85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

#df.dropna(axis=1,inplace=True)
df.dropna(inplace=True)
print(df)