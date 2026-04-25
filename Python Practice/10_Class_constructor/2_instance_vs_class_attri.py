class Employee:
  language = "py"   # this is a class attribute
  salary = 12000

anu = Employee()
anu.language = "JavaScript"  # this is an object (instance) attribute
print( anu.language,anu.salary)

