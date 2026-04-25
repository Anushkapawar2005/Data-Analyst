class Employee:
  language = "py"   # this is a class attribute
  salary = 12000

  def __init__(self):    # dunder method which is automatically called
    print("I am crating an object")

  def __init__(self, name, salary):
    self.name = name
    self.salary= salary
    
    
anu = Employee("radha", 12000)
# anu.name = "anu"
print(anu.name,anu.salary)