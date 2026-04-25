class Employee:
  def __init__(self):
    print("Constructor of Employee")
  a = 1


class Programmer(Employee):
  def __init__(self):
    print("Constructor of Programmer")
  b=2

class Manager(Programmer):
  def __init__(self):
    super().__init__()   # calls the parent class constructor
    print("Constructor of MAnager")
  c = 3

# o = Employee()
# print(o.a)

# x = Programmer()
# print(x.a, x.b)

z = Manager()
print(z.a, z.b, z.c)