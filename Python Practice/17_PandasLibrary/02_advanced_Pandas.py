import pandas as pd

# Load cleaned employee data
df = pd.read_csv("Employee_Data.csv")
print("---Data Loaded")
print(df.head())

#filtering

#Employee from Mumbai
df["City"]=df["City"].str.strip().str.title()
#mumbai_emp = df[df["City"] == "Mumbai"]
#print(mumbai_emp)

# High salary employees
#high_salary = df[df["Salary"]> 60000]
#print(high_salary)

#Multiple conditions
mumbai_high = df[(df["City"] == "Mumbai") & (df["Salary"] > 60000)]
print(mumbai_high)

mumbai_pune = df[(df["City"] == "Mumbai") | (df["City"] == "Pune")]
print(mumbai_pune)

#using isin()
IT_and_Finance = df[df["Department"].isin(["IT","Finance"])]
print(IT_and_Finance)


# Advanced Sorting

# sort by salary descending
#df_sorted_salary = df.sort_values("Salary",ascending=False)

# Sort by Department then Salary
df_sorted_multi = df.sort_values(["Department", "Salary"],ascending=[True,False])
print(df_sorted_multi)

# Multiple aggregations
salary_status = df.groupby("Department")["Salary"].agg(["min","max","mean","count"])
print("Salary Status: ")
print(salary_status)

# sort GROUPBY Result
avg_salary_dept = df.groupby("Department")["Salary"].mean()
sorted_avg_salary = avg_salary_dept.sort_values(ascending=False)
print("Department by Avg Salary:")
print(sorted_avg_salary)