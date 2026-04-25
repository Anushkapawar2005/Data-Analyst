import pandas as pd

data = {
  "Name":['Ram','Shyam','Radha','Aditi','Raj','Madhu','Simran','sanu'],
  "Age": [20,34,22,39,29,40,25,32],
  "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
  "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

# single condition
high_salary = df[df['Salary']> 50000]
print('Employee with salary > 50000')
print(high_salary)

# filtering rows salary > 50k & age>30
filtered = df[(df['Age']> 30) & (df['Salary']>50000)]
print(f'Employee list Age>30 + salary>50000')
print(filtered)

#using or condition
filtered_or = df[(df['Age']>35) | (df['Performance Score']>90)]
print('Employees older than 35 OR performancr score > 90')
print(filtered_or)