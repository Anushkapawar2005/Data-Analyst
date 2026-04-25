# This program does not destroyed but if try block is gives error then execute except block

try:
  a = int(input("Hey, Enter a number: "))
  print(a) 


except Exception as e:
  print(e)

else:       # this is executed only if the try was successful
  print("I am inside else")

