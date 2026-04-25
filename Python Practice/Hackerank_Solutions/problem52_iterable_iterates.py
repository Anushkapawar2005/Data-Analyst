# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
l = input().split(" ")
n = int(input())
count = 0
for i in combinations(l,n):
    if 'a' in i:
        count+=1
print(count/len(list(combinations(l,n))))