# sorting data

# sorting DATA 1 column sort_values()

#df.sort_value(by="column_name",True/false,inplace=True)

import pandas as pd
data = {
  "Name":['Arun','Varun','Karun'],
  "Age":[28,34,22],
  "Salary":[10000,20000,30000]
}
df= pd.DataFrame(data)
df.sort_values(by='Age',ascending=False,inplace=True)
print('Sorted age by descending')
print(df)