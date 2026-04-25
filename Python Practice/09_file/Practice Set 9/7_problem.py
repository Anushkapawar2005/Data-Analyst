# Method 1
# lineno = 1
# with open("log.txt") as f:
#   line = f.readline()

# if("python" in line):
#   print(f"Yes python present. Line no: {lineno}")
# else:
#   print("No python is not present")




with open("log.txt") as f:
  lines = f.readlines()

lineno = 1

for line in lines:
  if("python" in line):
   print(f"Yes python present. Line no: {lineno}")
   break
  lineno += 1

else:
  print("No python is not present")