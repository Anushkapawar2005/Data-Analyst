name = "Anushka"
nameshort = name[0:4] # start from 0 (index) to 3 (exclude 4)
print(nameshort)
character1 = name[1]
print(character1)
# strings are immutable i.e main str not change

# string format
name = "Anu"
age = 20

# old format - % opr
print("My name is %s and I'm %d."%(name,age))
# str format()
print("My name is {} and I'm {}".format(name,age))
print("My name is {0} and I'm {1}".format(name,age))
print("My name is {name} and I'm {age}".format(name="Anushka",age=20))

# f - strings
print(f"My name is {name} and I'm {age}")