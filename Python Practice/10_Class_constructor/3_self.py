class Employee:
  language = "py"   # this is a class attribute
  salary = 12000

  def getInfo(self):   # accept object as self
    print(f"The language is {self.language}. This salary is {self.salary}")

  
  def greet(p):
    print("Good morning")

  @staticmethod   # it is not necessary to get self argument
  def greet():
    print("Good morning")


anu = Employee()
anu.language = "JavaScript"  # this is an object (instance) attribute
print( anu.language,anu.salary)

anu.getInfo()  # pass object to fun
# Employee.getInfo(anu)    # this is same as anu.getInfo()

anu.greet()
