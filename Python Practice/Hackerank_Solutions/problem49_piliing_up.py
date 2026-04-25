# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def piling(d):
    while d:
        larger =None
        if d[-1] > d[0]:
            larger = d.pop()
        else:
            larger = d.popleft()
            
        if len(d) == 0:
            return "Yes"
            
        if d[-1] >larger or d[0] > larger:
            return "No"
            
for i in range(int(input())):
    no_of_cubes = int(input())
    d = deque(map(int, input().split()))
    print(piling(d))