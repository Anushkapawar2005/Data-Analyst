import pandas as pd

# -------------------------------
# 1. LOAD DATA
# -------------------------------
file_path = "raw_sales_data.csv"

df = pd.read_csv(file_path)

# -------------------------------
# 2. DATA CLEANING
# -------------------------------

# Clean text columns
df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()
df['State'] = df['State'].str.strip().str.title()

# -------------------------------
# 3. REMOVE DUPLICATES
# -------------------------------
df.drop_duplicates(subset='Order_ID', inplace=True)

# -------------------------------
# 4. CONVERT NUMERIC COLUMNS
# -------------------------------
numeric_cols = ['Quantity', 'Unit_Price', 'Discount']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Handle missing numeric values
df[numeric_cols] = df[numeric_cols].fillna(0)

# -------------------------------
# 5. CALCULATE TOTAL SALES
# -------------------------------
df['Total_Sales'] = (df['Quantity'] * df['Unit_Price']) - df['Discount']

# -------------------------------
# 6. ORDER VALUE CATEGORIZATION
# -------------------------------
def categorize_order(value):
    if value >= 10000:
        return "High"
    elif value >= 5000:
        return "Medium"
    else:
        return "Low"

df['Order_Value_Category'] = df['Total_Sales'].apply(categorize_order)

# -------------------------------
# 7. SUMMARY REPORTS
# -------------------------------

# Total Sales by City
sales_by_city = (
    df.groupby('City')['Total_Sales']
    .sum()
    .reset_index()
    .sort_values(by='Total_Sales', ascending=False)
)

# Total Sales by Product Category
sales_by_category = (
    df.groupby('Product_Category')['Total_Sales']
    .sum()
    .reset_index()
    .sort_values(by='Total_Sales', ascending=False)
)

# -------------------------------
# 8. EXPORT OUTPUT FILES
# -------------------------------

df.to_csv("cleaned_sales_data.csv", index=False)
sales_by_city.to_csv("sales_summary_by_city.csv", index=False)
sales_by_category.to_csv("sales_summary_by_category.csv", index=False)

print("✅ Data pipeline executed successfully!")