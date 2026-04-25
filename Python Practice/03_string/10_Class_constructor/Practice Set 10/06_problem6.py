from random import randint

class Train:
   
  def __init__(slf,trainNo):     # instead of writing self you can write anything like anu, slf, r, p ...
    slf.trainNo = trainNo

  def book(slf, fro, to):
    print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

  

t = Train(1239)
t.book("Rampur","Delhi")
