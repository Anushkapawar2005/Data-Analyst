# Q1. Find the maximum and minimum element in a tuple
t = (10, 5, 20, 3)
print(max(t))  # 20
print(min(t))  # 3


# Q3. Find the length of a tuple without using len()
t = (1, 2, 3, 4)
count = 0
for _ in t:
    count += 1
print(count)  # 4


# Q4. Convert a tuple into a list
t = (10, 20, 30)
lst = list(t)
print(lst)     # [10, 20, 30]


# Q6. Check whether an element exists in a tuple
t = (10, 20, 30)
print(20 in t)   # True


# Q7. Reverse a tuple
t = (1, 2, 3, 4)
print(t[::-1])


# Q8. Find sum and average of tuple elements
t = (10, 20, 30)
total = sum(t)
avg = total / len(t)
print(total, avg)        # 60 20.0


# Q9. Find even and odd numbers in a tuple
t = (1, 2, 3, 4, 5)
even = [i for i in t if i % 2 == 0]
odd = [i for i in t if i % 2 != 0]
print(even, odd)        # [2, 4] [1, 3, 5]



# Q10. Remove an element from a tuple (logic)
t = (10, 20, 30)
lst = list(t)
lst.remove(20)
t = tuple(lst)
print(t)                # (10, 30)


# Q11. Check whether a tuple is empty
t=()
if len(t) == 0:
  print("Tuple is empty")
else:
  print("Tuple is not empty")       # Tuple is empty


# Q12. Search an element in tuple
t = (1, 2, 2, 3)
freq = {}
for i in t:
  freq[i]=freq.get(i,0)+1
print(freq)        # {1: 1, 2: 2, 3: 1}


# Q13. Convert tuple of characters into string
t = ('P', 'y', 't', 'h', 'o', 'n')
s = ""

for i in t:
    s += i

print(s)    # Python
