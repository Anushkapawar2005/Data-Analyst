# 1 Find all positions of a character  **
s = "banana"
positions = [i for i, ch in enumerate(s) if ch == 'a']
print(positions)  #  [1, 3, 5]


# 2 Check anagram
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))  # True


# 3 Remove duplicate characters
s3 = "banana"
res = "".join(sorted(set(s), key=s3.index))
print(res)    # ban


# 4 Find longest word in a string
s4 = "Python is fun programming"
words = s.split()
longest = max(words, key=len)
print(longest)  # programming


# 5 Count digits in string
s5 = "Python123"
count = 0
for ch in s5:
  if ch.isdigit():
    count+=1

# count = sum(ch.isdigit() for ch in s5)
print(count)


# 6 Extract digits from string
digits=""
for ch in s5:
  if ch.isdigit():
    digits = digits + ch 
# digits = "".join(ch for ch in s5 if ch.isdigit())
print(digits)


# 7 Check if string is palindrome ignoring case and spaces
s6 = "A man a plan a canal Panama"
s_clean = "".join(s.lower().split())
print(s_clean == s_clean[::-1])  #False


# 8 Alternate character uppercase
s7 = "python"
alt=""
count=1
for ch in s7:
  if count % 2==0:
    alt= alt+ch
    count+=1
  print(alt)
# result = "".join(ch.upper() if i % 2 == 0 else ch for i, ch in enumerate(s))
# print(result)


# 10. Count frequency of each word
s8 = "python is easy and python is powerful"
words = s8.split()   # convert into a list of individual words
frequency = {}
for word in words:
  if word in frequency:
    frequency[word]+=1
  else:
    frequency[word] = 1
print(frequency)  #{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

# frequency = {w: words.count(w) for w in set(words)}
# print(frequency)



# 11. Remove vowels from string
s9 = "Python"
NewStr = ""
for ch in s9:
  if ch not in "aeiou":
    NewStr= NewStr+ch
#result = "".join(ch for ch in s if ch.lower() not in "aeiou")
print(NewStr)  #Pythn



# 12. First non-repeating character
s10 = "swiss"
for ch in s10:
  if s10.count(ch) == 1:
    print(ch)  # w
    break


# 13. Count uppercase and lowercase letters
s11 = "PyTHon"
upper = sum(ch.isupper() for ch in s11)
lower = sum(ch.islower() for ch in s11)

print(upper,lower) # 3 3

# Met 2
countUpper=0
countLower =0
for ch in s11:
  if ch.isupper():
    countUpper+=1
  elif ch.islower():
    countLower+=1
print(countLower,countUpper) # 3 3



# 14. Find all substrings of length 2
s12 = "Python"
# subs = [s[i:i+2] for i in range(len(s)-1)]
res=[]
for i in range(len(s12)-1):
    sub = s12[i:i+2]
    res.append(sub)
print(res)  #['Py', 'yt', 'th', 'ho', 'on']

# 15. Count special characters
s13 = "Python@123!"
# count = sum(not ch.isalnum() for ch in s)
count = 0
for ch in s13:
  if not ch.isalnum():
    count+=1
print(count)  # 2

# 16. Reverse words in sentence
s14 = "Python is fun"
# print(" ".join(word[::-1] for word in s.split()))
words = s14.split()
rev = ""
for word in words:
  rev +=" " +word[::-1]
print(rev)  #nohtyP si nuf


# 18. Find second largest word by length
s15 = "Python is fun programming"
words = s15.split()
sorted_word = sorted(words,key=len,reverse=True)
print(sorted_word[1]) # Python

# 19. Replace multiple spaces with underscore
s16 = "Python   is   fun"
print("_".join(s16.split()))  # Python_is_fun


# 21. Remove characters at even positions
s17 = "Python"
print("".join(ch for i, ch in enumerate(s17) if i % 2 != 0)) # yhn

# 22. Convert string to list of integers (digits only)
s18 = "a1b2c3"
# numbers = [int(ch) for ch in s18 if ch.isdigit()]
# print(numbers)
num=[]
for ch in s18:
  if ch.isdigit():
    num.append(int(ch))
print(num)  # [1, 2, 3]