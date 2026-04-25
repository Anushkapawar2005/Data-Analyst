# 1. Prime Number
def isPrime(n):
  if n<=1:
    return False
  for i in range(2,n):
    if n%i==0:
      return False
  return True

print(isPrime(7))    # True


# 2. Factorial
def factorial(n):
  fact=1
  for i in range(1,n+1):
    fact*=i
  return fact

print(factorial(5)) # 120


# 3. Fibonacci Series
def fibonacci(n):
  a,b=0,1
  for _ in range(n):  # _ because var not use in loop
    print(a,end=" ") 
    a,b=b,a+b

fibonacci(5)


# 4. Palindrome Number
def palindrome(n):
    return str(n) == str(n)[::-1]

print(palindrome(121))  # True


# 8. Armstrong Number
def armstrong(n):
  total=0
  temp=n
  while temp>0:
    d=temp%10
    total+=d**3
    temp//=10
  return total==n

print(armstrong(153))     # True

# sum of digits
def sum(n):
  total=0
  while n>0:
    d=n%10
    total+=d
    n//=10
  return total

print(sum(144))   # 9

# reverse no
def rev(n):
  rev=0
  temp=n
  while temp>0:
    d=temp%10
    rev=rev*10+d
    temp//=10
  return rev

print(rev(176))


# 33. Menu-Driven Program
lst =[]
while True:
  print("1.Add 2.view 3.Exit")
  ch = int(input())
  if ch == 1:
    lst.append(int(input("Enter nm: ")))
  elif ch == 2:
    print(lst)
  else:
    break


# Simple Login System

users = ["admin"]
pwd = ["123"]
u = input("User: ")
p = input("Pass: ")
print("Login Successful" if u in users and p == pwd[0] else "Invalid")
