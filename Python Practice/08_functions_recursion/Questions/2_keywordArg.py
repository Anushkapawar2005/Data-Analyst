
# keyword arguments - argument passed using parameter names


def divide(a,b):
  return  a/b
res = divide(b=10, a=20)
print(res)
res = divide(10, 20)  # positional arg
print(res)