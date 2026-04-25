# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
    item_name,blank,price = input().rpartition(' ')
    if item_name not in od:
        od[item_name] = int(price)
    else:
        od[item_name] += int(price)
        
for i in od.items():
    print(*i)