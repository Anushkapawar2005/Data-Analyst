# clean customer names (strip + title)

import csv
cleaned_rows = []
with open("Data2.csv") as f:
  reader = csv.DictReader(f)

  for row in reader:
    row['Customer_Name'] = row['Customer_Name'].strip().title()
    cleaned_rows.append(row)

#print(cleaned_rows)

with open("cleaned_customers.csv","w",newline="") as f:
  writer = csv.DictWriter(f,fieldnames=reader.fieldnames)
  writer.writeheader()
  writer.writerows(cleaned_rows)

print("Cleaned CSV created : cleaned_customers.csv")
