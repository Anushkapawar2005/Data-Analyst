s= {1, 5, 32, 5,5,5,78, "Anu"}

print(s,type(s))

s.add(566)
print(s,type(s))

#s.update(['99','seeta'])  # add multiple elements
# s.update('99')  # without  []
s.update(['99'])
print(s)    #{32, 1, 5, 566, '99', 'Anu', 78}

s.remove(1)  
print(s,type(s)) # {32, 5, 566, '99', 'Anu', 78} <class 'set'>

n = {1,2,7,4}
# n.pop()  #  {2, 4, 7} # first element delete
print(n.pop())
# n.clear()  # set()
n.discard(5) # no error if it is not exist  # {1, 2, 4, 7}
print(n) 


# membership test in, not in
print(20 in n)   # False

# loop - print single element
for i in n:
  print(i) 

# list comprohension
squares = {x*x for x in range(1,6)}
print(squares)  # {1, 4, 9, 16, 25}