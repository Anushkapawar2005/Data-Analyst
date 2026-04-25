n = int(input("Enter the num: "))
product=1
for i in range(1, n+1):
  product*=i

print(f"The factorial of {n} is {product}")