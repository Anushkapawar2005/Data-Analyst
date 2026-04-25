class Demo:
  a = 4

o = Demo()
print(o.a)  # 4  prints the class attribute because instance attribute is not present
o.a = 0  # Instance attribute is set
print(o.a)  # 0   print instance attribute because instance attribute is present
print(Demo.a)  # 4  class attribute not change. Print class attribute