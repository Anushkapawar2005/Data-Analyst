import csv

with open("Data.csv") as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)


with open("Data.csv") as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row["age"],row["Names"])


#filter
female=[]
with open("Data.csv") as f:
  reader = csv.DictReader(f)
  for row in reader:
    if row["Gender"]=="female":
      female.append(row)
print(female)