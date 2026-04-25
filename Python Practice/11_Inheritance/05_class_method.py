class Employee:
  a= 1
  @classmethod   # it shows the class attribute not a instance attribute
  def show(cls):
    print(f"The class aattribute of a is {cls.a}")

e = Employee()
e.a = 45  # instance attribute

e.show()