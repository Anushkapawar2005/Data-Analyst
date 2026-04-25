# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
expression = r"([a-zA-Z0-9])\1+"
m=re.search(expression,input())
if m:
    print(m.group(1))
else:
    print(-1)