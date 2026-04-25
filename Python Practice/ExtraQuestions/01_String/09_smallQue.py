
# Check if string is title case

str = input("Enter str: ")
print(str.istitle())  


# Make string title case
print(str.title())

# Count words in a sentence
print(len(str.split()))

# Replace multiple spaces with single space
s = "Python   is   fun"
# print(s.replace("  ",""))
print(" ".join(s.split()))   # Python is fun

# Format string with variable
name = "Anushka"
age = 20
print(f"My name is {name} and age is {age}")   # My name is Anushka and age is 20


# Check substring existence
print("tho" in str)   # true

# Remove last character
print(s[:-1])

# Count uppercase letters
s1 = "PyThOn"
count = sum(1 for ch in s if ch.isupper())
print(count)
