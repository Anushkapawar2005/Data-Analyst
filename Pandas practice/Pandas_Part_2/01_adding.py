import pandas as pd

data = {
  "Name":['Ram','Shyam','Radha','Aditi','Raj','Madhu','Simran','sanu'],
  "Age": [20,34,22,39,29,40,25,32],
  "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
  "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

#square brackets d["Column_Name"] = same data
df['Bonus'] = df['Salary'] * 0.1   # add at the end
print(df)

#using insert()
#df.insert(loc, "Column_Name",some_data)
df.insert(0,"Employee_ID",[10,20,30,40,50,60,70,80])   # specific position
print(df)