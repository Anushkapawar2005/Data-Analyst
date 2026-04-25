marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))


total_per = (marks1+marks2+marks3)/3

if(total_per >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
  print("You are passed", total_per)
else:
  print("You failed, try again next year!",total_per)