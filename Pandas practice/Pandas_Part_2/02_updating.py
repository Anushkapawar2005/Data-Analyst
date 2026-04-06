import pandas as pd

data = {
  "Name":['Ram','Shyam','Radha','Aditi','Raj','Madhu','Simran','sanu'],
  "Age": [20,34,22,39,29,40,25,32],
  "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
  "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

#.loc[] - specific cell access and modify
#df.loc[row_index,"Column Name"] = new_value
df.loc[0,'Salary'] = 55000
print(df)


#increasing salary by 5%
df['Salary'] = df['Salary']*1.05
print(df)