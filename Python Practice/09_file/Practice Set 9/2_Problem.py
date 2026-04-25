import random

def game():
  print("You are playing the game...")
  score = random.randint(1,62)  # randint(1, 62) it is used to get the random number bet 1 to 62

  # Fetch the hiscore
  with open("hiscore.txt") as f:
    hiscore = f.read()
    if(hiscore != ""):
      hiscore=int(hiscore)   # f.read() is in str form so its need to convert int
    else:
      hiscore = 0

  print(f"Your Score: {score}")


 # write this high score to the file
  if(score > hiscore):
   
    with open("hiscore.txt","w") as f:
      f.write(str(score))  # write() is write in str
    return score  

game()
