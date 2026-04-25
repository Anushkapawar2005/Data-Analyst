# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
result  = [(len(list(c)),int(k)) for k,c in groupby(input())]
print(*result)