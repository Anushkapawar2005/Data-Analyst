import pandas as pd

data = {
  "Name":['Ram','Shyam','Radha','Aditi','Raj','Madhu','Simran','sanu'],
  "Age": [20,34,22,39,29,40,25,32],
  "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
  "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

#df.drop[Columns = ["ColumnName"],inplace=True]

print("Modified Data: ")
#df.drop(columns=["Performance Score"],inplace=True)
print(df)

# remove multiple columns
df.drop(columns=["Performance Score","Age"],inplace=True)
print(df)