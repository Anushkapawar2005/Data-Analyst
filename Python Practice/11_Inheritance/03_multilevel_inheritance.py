class Employee:
  a = 1


class Programmer(Employee):
  b=2

class Manager(Programmer):
  c = 3

o = Employee()
print(o.a)
# print(o.b)  # it gives error beacause there is no b attribute in employee class

x = Programmer()
print(x.a, x.b)

z = Manager()
print(z.a, z.b, z.c)