class Employee:
  a= 1
  @classmethod   
  def show(cls):
    print(f"The class aattribute of a is {cls.a}")

  
  @property
  def name(Self):
    return f"{Self.fname} {Self.lname}"

  @name.setter             # abstraction - hide implementation details from users
  def name(Self,value):
    Self.fname = value.split(" ")[0]
    Self.lname = value.split(" ")[1]

e = Employee()
e.a = 45  # instance attribute
e.name = "Anushka Pawar"
print(e.name)   # Anushka Pawar
print(e.fname, e.lname)  # Anushka Pawar      # set fname and lname

e.show()