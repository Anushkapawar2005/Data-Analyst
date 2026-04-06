#df["Column_name"].mean()
# sum(),max(),min(),count(), std()
import pandas as pd
data = {
  "Name":['Arun','Varun','Karun'],
  "Age":[28,34,22],
  "Salary":[10000,20000,30000]
}
df= pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(avg_salary)