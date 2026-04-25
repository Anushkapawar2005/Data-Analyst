a = int(input("Enter your age: "))

# If elif else ladder
if(a>18):
  print("Your are above the age of concent")  # before print space is indentation
elif(a<0):
  print("You are entering invalid age")
elif(a==0):
  print("You are entering 0 which is not a valid age")
else:
  print("you are below the age of concent")
 

print("End of program")