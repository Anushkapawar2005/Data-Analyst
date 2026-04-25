# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
sizes = [ int(i) for i in input().split()]
N = int(input())

sizes = Counter(sizes)
money = 0
for i in range(N):
    size, price = [ int(j) for j in input().split()]
    if size in sizes and sizes[size] > 0:
        money = money + price
        sizes[size] = sizes[size] - 1

print(money)