# Count consonants in a string

str = "Python"
count = 0
for ch in str:
  if ch.isalpha() and (ch.lower() not in "aeiou"):
    count += 1

print(count)