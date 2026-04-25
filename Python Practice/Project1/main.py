import random
'''
1 - snake
-1 - water
0 - gun

'''

computer = random.choice([-1,0,1])  # random() - computer chose random num
user = input("Enter your choice: ")
userDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
usernum = userDict[user]
# By now we have 2 numbers(variables), user and computer

print(f"You chose: {reverseDict[usernum]}\nComputer chose: {reverseDict[computer]}")
if(computer == usernum):
  print("It's draw")
else:
  # if((computer-usernum)== -1 or (computer - usernum) == 2):
  #   print("You lose")
  # else:
  #   print("you win")

  if(computer == -1 and usernum == 1):
    print("you(user) win!")
  elif(computer == -1 and usernum == 0):
    print("You lose!")

  elif(computer == 1 and usernum == -1):
    print("you lose!")
  elif(computer == 1 and usernum == 0):
    print("You win!")

  elif(computer == 0 and usernum == -1):
    print("you win!")
  elif(computer == 0 and usernum == 1):
    print("You lose!")
  else:
    print("Something went wrong!")




