s1= {1,4,5,3}
s2 = {6, 1, 19, 4}

print(s1.union(s2))  #{1, 3, 4, 5, 6, 19}
print(s1 | s2) #{1, 3, 4, 5, 6, 19}


print(s1.intersection(s2))  # {1, 4}
print(s1 & s2) # {1, 4}

print(s1.difference(s2))  # {3, 5}
print(s1-s2)  # {3, 5}

print(s1.symmetric_difference(s2)) #{3, 5, 6, 19}
print(s1^s2) # {3, 5, 6, 19}



# modify existing set
s1= {1,5,3,6}
s2 = {6, 1, 19, 4,3}
# s1.intersection_update(s2)
# print(s1.intersection_update(s2)) # none
# print(s1)   # {1, 3, 6}

# s1.difference_update(s2)
# print(s1) # {5}

# s1.symmetric_difference_update(s2)
# print(s1)  #{19, 4, 5}



# Relationship methods

print({1,2}.issubset({1,2,3})) # True
print({1,2,3}.issuperset({1,2})) # True
print({1,2}.isdisjoint({3,4}))  # True


# Additional mathod
n1 = {1,2}
n2 = n1.copy()
print(n2) # {1, 2}


# Iteration loop
numbers = {1,3,2,7,8}
for i in numbers:
  print(i)

# set comprehension
squares = {x**2 for x in range(1,6)}
print(squares) # {1, 4, 9, 16, 25}

# Removing duplicates elements from a list
numbers1 = [1,2,3,2,4,4,5]
unique_numbers = set(numbers1) 
print(unique_numbers)  # {1, 2, 3, 4, 5}