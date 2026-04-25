# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]

for element in list(product(A,B)):
    print(element, end=' ')