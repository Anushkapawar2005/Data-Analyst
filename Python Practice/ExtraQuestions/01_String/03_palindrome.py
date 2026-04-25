# check palindrome

str = input("Enter str: ")
if str == str[::-1]:    # str[::-1] - reverse string
  print("Palindrome")
else:
  print("Not Palindrome")