from functools import reduce

a = [2, 13, 65, 567, 45,4]

def greater(a, b):
  if(a>b):
    return a
  return b

print(reduce(greater, a))