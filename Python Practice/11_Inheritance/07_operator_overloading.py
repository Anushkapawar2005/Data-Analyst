class Number:
  def __init__(Self,n):
    Self.n = n

  def __add__(self,num):
    return self.n + num.n



n = Number(1)
m = Number(2)

print(n + m)