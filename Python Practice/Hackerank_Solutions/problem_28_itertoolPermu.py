# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

data, k = input().split()
k = int(k)

data = list(permutations(sorted(data), k ))
for item in data:
    print("".join(item))  # o/p is in string so use join