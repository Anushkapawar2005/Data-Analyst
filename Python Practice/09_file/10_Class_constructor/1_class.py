class Employee:
  language = "py"   # this is a class attribute
  salary = 12000

anu = Employee()
anu.name = "Anushka"  # this is an object (instance) attribute
print(anu.name, anu.language,anu.salary)

radha = Employee()
radha.name = "Radha"
print(radha.name, radha.salary, radha.language)

# Here name is object (instance(. attribute)) attribute and salary and language are class attribute as they directly belong to the class