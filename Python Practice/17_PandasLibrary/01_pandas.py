import pandas as pd

# 1. Load CSV File

df = pd.read_csv("Employee_Data.csv")
print("\n--- Raw Data ---")
#print(df.head())
print(df.head(10))
#print("\n--- Output ---")

print("\n--- Botom 5 rows ---")
print(df.tail())

#2. Basic information
print("\nShape:",df.shape)
print("Columns:",df.columns)
print(df.info())
print(df.describe())
#3. Clean text data

#clean employee name
df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
print(df.head())

#clean city names
df["City"] = df["City"].str.strip().str.title()
print(df.head())

#clean department
df["Department"] = df["Department"].str.strip().str.title()
print(df.head())

print("--- Cleaned text Columns ---")
print(df[["Employee_Name","City","Department"]].head())


#4.Remove duplicates
print("Duplicate Rows:",df.duplicated().sum())
df = df.drop_duplicates()
#print(df)

#5. Filter data

#Employee from Mumbai
df["City"] = df["City"].str.strip().str.title()
mumbai_emp = df[df["City"] == "Mumbai"]
print(mumbai_emp)
print("Employee from Mumbai:",mumbai_emp.shape[0])  # 0 - row, 1 - column

# Employee with salary > 6000
hight_salary = df[df["Salary"]>60000]
print(hight_salary.head())
print("EMployee with Salary > 60000:",hight_salary.shape[0])

# Sort data
#sort by salary (descending)
df_sorted_salary = df.sort_values("Salary",ascending=False)
print(df_sorted_salary.head())

# sort by joining year
df_sorted_salary=df.sort_values("Joining_Year")
print(df_sorted_salary.head())

#7. Add new columns
# salary category
df["Salary_Category"] = df["Salary"].apply(
  lambda x:"High" if x>=60000 else "Medium" if x>= 50000 else "Low"
)
print(df.head())

#Experience (Years)
df["Experience"] = 2025 - df["Joining_Year"]
print(df.head())

# 8. GROUP By operations

#Average salary by department
avg_salary_dept = df.groupby("Department")["Salary"].mean()
print(avg_salary_dept.head())

# Total salary by city
total_salary_city = df.groupby("City")["Salary"].sum()
print(total_salary_city.head())

#Employee count by Department 
count_dept = df.groupby("Department")["Employee_ID"].count()
print(count_dept.head())

#9. Export cleaned data. sort by salary (Descending)
df_sorted_salary = df.sort_values("Salary",ascending=False)
df_sorted_salary.to_csv("employee_sorted_by_salary.csv",index=False)
