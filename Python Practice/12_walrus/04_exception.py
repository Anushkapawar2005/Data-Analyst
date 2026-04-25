# This program does not destroyed but if try block is gives error then execute except block

try:
  a = int(input("Hey, Enter a number: "))
  print(a) 

except ValueError as v:  # thow an error
  print("hey")
  print(v)

except Exception as e:
  print(e)


print("Thank you")