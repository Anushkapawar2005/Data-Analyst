from functools import reduce

# Map ex - map used for elements
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter ex
def even(n):
  if(n%2 == 0):
    return True
  return False

onlyEven = filter(even, l)
print(list(onlyEven))


# Reduce Ex - 
def sum(a, b):
  return a+b

print(reduce(sum, l))  # 1 2 3 4
                       # 3 3 4
                       # 6 4
                       # 15

def mul(a,b):
  return a*b

print(reduce(mul,l))