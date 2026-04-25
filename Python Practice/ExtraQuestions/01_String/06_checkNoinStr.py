# Check if string contains number
str = input("Enter str: ")
found = any(ch.isdigit() for ch in str)
print(found)