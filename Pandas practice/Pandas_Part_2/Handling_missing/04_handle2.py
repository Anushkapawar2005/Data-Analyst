
#fillna()
#fillna(value,inplace=True)

import pandas as pd

data = {
  "Name":['Ram',None,'Radha','Aditi','Raj','Madhu','Simran','sanu'],
  "Age": [20,None,22,39,29,40,25,32],
  "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
  "Performance Score":[85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

# default value fill
#df.fillna(0,inplace=True)
print(df)

#calculate value fill
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)