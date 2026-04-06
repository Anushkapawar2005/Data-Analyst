import pandas as pd
data = {
  "Name":['Arun','Varun','Karun','Narun','harun'],
  "Age":[28,34,22,34,28],
  "Salary":[50000,60000,45000,52000,48000]
}
df= pd.DataFrame(data)
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)
