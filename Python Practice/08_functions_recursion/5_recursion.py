'''
factorial(1)=1
factorial(2)=2X1
factorial(3)=3X2X1

factorial(n) = nX n-1 X.....3X2X1

factorial(n) = n * factorial(n-1)

'''

def factorial(n):
  if(n==1 or n==0):
    return 1
  return n* factorial(n-1)


n= int(input("Enter a num: "))
print(f"The factorial of this num is: {factorial(n)}")