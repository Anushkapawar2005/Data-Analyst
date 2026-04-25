# Reverse string using loop

str = input("Enter str: ")
#print(str[::-1])

rev = ""
for ch in str:
  rev = ch + rev
print(rev) 
