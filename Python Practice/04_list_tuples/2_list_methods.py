friends = ["Apple", "orange", 5, 345.06,False,"Aakash","Rohan"]
print(friends)
friends.append("Anushka") # add elements at the end
print(friends)


l1 = [1,56,3,89,24,24]

# l1.extend(90)  # error because extend add multiple element(list, tuple)

l1.sort()
print(len(l1)) # 6
print(l1.index(24))  # o/p: 2  # return the index of first matching element 
# l1.reverse()
l1.insert(3,3333) #insert 3333 such that its in the list is 3
#l1.pop(2)

print(l1.pop(2)) # 24  # delete element specified index by default last element
l1.remove(24) #[1, 3, 3333, 56, 89]  remove first occurrence of element
print(l1)

del friends[1]
print(friends) # ['Apple', 5, 345.06, False, 'Aakash', 'Rohan', 'Anushka']

l3  = [3,5,2]
del l3    # delete complete list

# l1.clear()
# print(l1) # []

sorted_num = sorted(l1)  # returns new sorted list
print(sorted_num)

sorted_num.sort(reverse = True)  # sorted list in descending order
print(sorted_num)

print(56 in l1)  # in check if an item exist or not
print( 56 not in l1)

print(sum(l1)) 
print(min(l1))
print(max(l1))
print(l1.count(3))

l1.reverse()
print(l1)


# copy the list
l4 = [45,89,34]
print(l4.copy())
new = list(l4)
print(new)

# list concatenation (+)
print(l1+l4)

# list repetition (*)
print(l4 * 2)

# list slicing
print(l1[1:4])