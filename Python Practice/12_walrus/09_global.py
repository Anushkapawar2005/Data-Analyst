
a = 67  # global var
def fun():
  # a=3  # local var

  #  But if you want to use global var then use global keyword
  global a
  a = 3
  print(a)  # 3



fun()
print(a) # 3