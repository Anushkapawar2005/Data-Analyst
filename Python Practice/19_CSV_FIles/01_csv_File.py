import pandas as pd
import os

# ----------------------------------
# Ask user for folder path
# ----------------------------------
folder_path = input("Paste the folder path containing CSV files and press Enter:\n").strip()

# Validate folder path
if not os.path.isdir(folder_path):
    print("❌ Invalid folder path. Please check and try again.")
    exit()

# Output Excel file path
output_file = os.path.join(
    folder_path,
    "All_CSV_Converted_Into_Sheets.xlsx"
)

# ----------------------------------
# Read CSV files and write to Excel
# ----------------------------------
csv_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".csv")]

if not csv_files:
    print("❌ No CSV files found in the folder.")
    exit()

with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    for csv_file in csv_files:
        csv_path = os.path.join(folder_path, csv_file)

        # Read CSV
        df = pd.read_csv(csv_path)

        # Sheet name = CSV file name (without .csv)
        sheet_name = os.path.splitext(csv_file)[0][:31]  # Excel sheet name limit

        # Write to Excel
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("✅ All CSV files successfully combined into:")
print(output_file)