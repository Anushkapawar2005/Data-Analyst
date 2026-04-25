# count vowels in a string
s = input("Enter str: ")
count = 0
for ch in s:
  if ch.lower() in "aeiou":
    count += 1
print(count)