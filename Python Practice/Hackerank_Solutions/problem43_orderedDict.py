# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
    word = input()
    if word not in od:
        od[word] = 1
    else:
        od[word] += 1
print(len(od))
print(*od.values())