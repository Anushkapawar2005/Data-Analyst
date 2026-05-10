import pandas as pd
from datetime import datetime

# Step 1: Load CSV file
df = pd.read_csv("Employee_Data.csv")

# --------------------------------------------------
# 1. Clean Employee_Name and City columns
# --------------------------------------------------

# Remove extra spaces and standardize capitalization
df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# --------------------------------------------------
# 2. Remove duplicate records
# --------------------------------------------------

# Remove full duplicate rows
df = df.drop_duplicates()

# (Optional) Remove duplicates based on Employee_ID only
# df = df.drop_duplicates(subset="Employee_ID")

# --------------------------------------------------
# 3. Add Experience column
# --------------------------------------------------

current_year = datetime.now().year
df["Experience"] = current_year - df["Joining_Year"]

# --------------------------------------------------
# Display Result
# --------------------------------------------------
print(df)

# Save cleaned dataset
df.to_csv("Employee_Data_Cleaned.csv", index=False)