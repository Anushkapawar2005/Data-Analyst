# Split and reverse words

s = "Python is fun"
words = s.split()
# print(words)
words.reverse()
print(" ".join(words))


# Count occurrences of each character

s1 = "banana"
for ch in set(s1):
    print(ch, s1.count(ch))


# o/p:-
# b 1
# n 2
# a 3


import string
s3 = "Python, is fun"
clean = "".join(ch for ch in s if ch not in string.punctuation)
print(clean)