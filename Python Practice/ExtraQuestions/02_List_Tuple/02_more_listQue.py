# 1. Find largest and smallest element together
lst = [10,30,40,6,1]
max_val = lst[0]
min_val = lst[0]
for i in lst:
  if i > max_val:
    max_val= i
  if i < min_val:
    min_val = i
print("Max: ",max_val)       
print("Min: ",min_val)
# Max:  40
# Min:  1



# 2. Count positive and negative numbers
lst = [10, -5, 20, -3, 0]
pos = neg = 0

for i in lst:
  if i>0:
    pos+=1
  elif i<0:
    neg+=1
print("Positive:",pos)
print("Negative:",neg)
# Positive: 2
# Negative: 2


# 3. Remove duplicate elements
lst = [1, 2, 2, 3, 1]
unique = []
for i in lst:
  if i not in unique:
    unique.append(i)

print(unique)  # [1, 2, 3]


# 4. Find second largest element
lst = [10, 40, 20, 30]
largest= second=0
for i in lst:
  if i>largest:
    second=largest
    largest=i
  elif i> second and i != largest:
    second = i

print(second)


# 5. Check list is palindrome
lst = [1, 2, 3, 2, 1]
if lst == lst[::-1]:
  print("palindrome")
else:
  print("not palindrome")  
# palindrome


# 6. Find sum of even and odd numbers
lst = [1, 2, 3, 4, 5]
even_sum = odd_sum = 0
for i in lst:
  if i % 2 == 0:
    even_sum+=i
  else:
    odd_sum += i

print(even_sum, odd_sum)   # 6 9


# 7. Delete all occurrences of an element
lst = [1, 2, 3, 2, 4]
key = 2
while key in lst:
  lst.remove(key)

print(lst)     # [1, 3, 4]


# 8. Find index of element manually
lst = [10, 20, 30]
key = 30
for i in range(len(lst)):
  if lst[i] == key:
    print("Index:",i)    #Index: 2
    break


# 9. Merge two lists without using +
a = [1, 2]
b = [3, 4]
for i in b:
  a.append(i)
print(a)      # [1, 2, 3, 4]


# 10. Count frequency of each element
lst = [1, 2, 2, 3]
for i in set(lst):
  print(i,lst.count(i))
# 1 1
# 2 2
# 3 1

# 11. Find average of list elements
lst = [10, 20, 30]
total = 0
for i in lst:
  total+=i
avg = total/len(lst)
print(avg)     # 20.0


# 12. Replace negative numbers with 0
lst = [10, -5, 20, -3]
# lst = [0 if i < 0 else i for i in lst]
for i in range(len(lst)):
  if lst[i] < 0:
    lst[i]=0
print(lst)   # [10, 0, 20, 0]


# 13. Shift list left by o
lst = [1, 2, 3, 4]
first = lst.pop(0)
lst.append(first)
print(lst)        # [2, 3, 4, 1]

# 14. Find common elements in two lists
a = [1, 2, 3]
b = [2, 3, 4]
common = []
for i in a:
  if i in b:
    common.append(i)
print(common)     # [2, 3]


# 15. Find missing number in list
lst = [1, 2, 4, 5]
n = 5
for i in range(1, n+1):
  if i not in lst:
    print(i)     # 3


# 16. Check list is sorted or not
lst = [10, 20, 30]
flag=True
for i in range(len(lst)-1):
  if lst[i]>lst[i+1]:
    flag=False

if flag:
  print("Sorted")
else:
  print("Not sorted")       # Sorted



# 17. Move all zeros to end
lst = [0, 1, 0, 3, 5]
new = []
for i in lst:
  if i != 0:
    new.append(i)

zeros = [0]*(len(lst)-len(new))
new.extend(zeros)
print(new)         # [1, 3, 5, 0, 0]



# 18. Count prime numbers in list
lst = [2, 3, 4, 5, 6]
count =0
for num in lst:
  if num > 1:
    for i in range(2,num):
      if num%i == 0:
        break
      else:
        count += 1
print(count)       # 4


# 19. Reverse list using loop
lst = [1, 2, 3]
rev = []
for i in lst:
  rev= [i]+rev
print(rev)       # [3, 2, 1]


# 20. Find intersection and union
a = [1, 2, 3]
b = [3, 4, 5]
intersection = []
union = a.copy()

for i in b:
  if i in a:
    intersection.append(i)
  else:
    union.append(i)

print(intersection)        # [3]
print(union)               # [1, 2, 3, 4, 5]