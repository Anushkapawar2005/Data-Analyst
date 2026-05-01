count = 0
with open("file.txt","r") as f:
  for _ in f:
    count+=1
print("Total lines:",count)