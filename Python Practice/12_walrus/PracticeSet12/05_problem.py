n = int(input("Enter a num: "))

table = [n+i for i in range(1,10)]
with open("table.txt", "a")as f:
  f.write(f"Table of {n}: {str(table)} \n")