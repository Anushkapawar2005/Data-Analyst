# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = list(map(int,input().split()))
# print(k,m)

lines=[]
for item in range(k):
    lines.append(list(map(int,input().split()))[1:])   # create 3 lists  & append in lines
    
# print(lines)

result_list = list(product(*lines))  # all possible combinations
# print(result_list)

result = []
for tup in result_list:
    total = 0
    for item in tup:
        total = total + (item**2)
        
    result.append(total%m)
    
print(max(result))