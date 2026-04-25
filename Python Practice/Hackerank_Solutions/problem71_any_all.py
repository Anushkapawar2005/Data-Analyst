# Enter your code here. Read input from STDIN. Print output to STDOUT
siz = int(input())
lst = list(input().split())
pos = all([int(i)>0 for i in lst])
pal = any([st == st[::-1] for st in lst])
print(pos and pal)