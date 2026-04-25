
# 1. Create a list and print it
my_list = [10,20,30]
print(my_list)    # [10, 20, 30]

#2. Add one element at the end
my_list.append(40)
print(my_list)        #[10, 20, 30, 40]

#3. Insert element at specific position
my_list.insert(1,15)
print(my_list)       # [10, 15, 20, 30, 40]

# 4. Take 5 numbers from user and store in list
my_list1 = []
for i in range(5):
  num= int(input("Enter num: "))
  my_list1.append(num)

print(my_list1)       # [5, 4, 3, 7, 8]


# 5. Find length of list
print(len(my_list))

# 6. Access first and last element
print(my_list[0])      # 10
print(my_list[-1])     # 40

# 7. Find maximum element
max_val = my_list[0]
for i in my_list:
  if i>max_val:
    max_val = i

print(max_val)     # 40

# 9. Sum of list elements
total =0
for i in my_list:
  total+=i
print(total)    #115

# 10. Count even numbers in list
my_list2 = [1,2,3,4,5,6]
count=0
for i in my_list2:
  if i % 2== 0:
    count += 1

print(count)  # 3

# 11. Separate even and odd numbers
even =[]
odd =[]
for i in my_list2:
  if i % 2==0:
    even.append(i)
  else:
    odd.append(i)

print(even)   # [2, 4, 6]
print(odd)    # [1, 3, 5]

# 12. Search an element in list
my_list3 = [10,20,30]
key = 20
if key in my_list3:
  print("Found")
else:
  print("Not found")    # Found

# 13. Reverse a list
print(my_list2[::-1])    # [6, 5, 4, 3, 2, 1]

# 15. Sort list
my_list4 = [30, 10, 20]
my_list4.sort()
print(my_list4)

# 16. Copy one list into another
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)        # [1, 2, 3]

# 17. Count frequency of an element
my_list5 = [1, 2, 2, 3]
print(my_list5.count(2)) #2

# 18. Merge two lists
a = [1,2]
b = [5,6]
print(a+b)       # [1, 2, 5, 6]

# 19. Clear all elements
my_list6 = [1,2,3]
my_list6.clear()
print(my_list6)    #[]

# 20. Check list is empty or not
my_list7 = []
if len(my_list7) == 0:
  print("List is empty")
else:
  print("List is not empty")    # List is empty