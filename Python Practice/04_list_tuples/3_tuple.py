# tuple are immutable  - so tuples are not modify - 
# tuple faster than list - python don't need to manage changes to them like list elements are fixed

n = () # empty tuples
a = (1,2,5,6,False,"Anu")  
b = (1,) # only one element
c = (1, [1,5,6], (4,5,6))
d = 1, 2, 3, 4

Name, age = "Anushka", 75

print(a)  # (1, 2, 5, 6, False, 'Anu')
print(c)  # (1, [1, 5, 6], (4, 5, 6))


# accessing tuple items
print(c[2])     # (4, 5, 6)
print(a[-2])
print(type(a))  # <class 'tuple'>

# modify a tuple - raise error
#a[1] = 56  # error
# but, you can create new tuple with updated value
new_num = a + (76,)
print(new_num)  # (1, 2, 5, 6, False, 'Anu', 76)


# packingn - PUTTING MULTIPLE VALUes into a single tuple
name = "anu"
age = 20
pack_tuple = name,age 
print(pack_tuple)  # ('anu', 20)

# unpacking - extracting the value from a tuple 
person  = ("anu", 20)
name , age = person  
print(name)     # anu
print(age)      # 20


# type casting or add value in tuple
my_tuple = ("apple","mango","cherry")
# type cast tuple to list
y = list(my_tuple)
y.append("orange")
# type cast back list to tuple
my_tuple = tuple(y)
print(my_tuple)    # ('apple', 'mango', 'cherry', 'orange')