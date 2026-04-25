a = 1
b=2
c=3

def greatest(a, b, c):
  if(a>b and a>c):
    return a
  elif(b>a and b>c):
    return a
  elif(c>a and c>a):
    return c

print(f"gratest num: {greatest(a,b,c)}")