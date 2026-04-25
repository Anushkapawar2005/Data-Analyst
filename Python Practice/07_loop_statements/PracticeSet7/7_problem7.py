'''
for n=3
   *
  ***
 *****
'''

n= int(input("Enter the num: "))

for i in range(1, n+1):
  print(" " * (n-i), end="")  # end for no create new line
  print("*" * (2*i-1), end="")
  print("")   # new line