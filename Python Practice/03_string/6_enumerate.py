# enumerate(iterable,start =0)  #start optional

names = ["Anushka","Pooja","Madhu"]
for index, name in enumerate(names):
  print(index,name)

# o/p:
# 0 Anushka
# 1 Pooja
# 2 Madhu

# custome index staring point

for index , name in enumerate(names,start=1):
  print(index,name)

# 1 Anushka
# 2 Pooja
# 3 Madhu

# Enumerate with conditional logic
marks = [46,87,35,68]
for index, mark in enumerate(marks):
  if mark < 40:
    print("Fail at index",index)

#o/p
# Fail at index 2


#Enumerate with string
word = "Python"
for index, char in enumerate(word):
  print(index,char)