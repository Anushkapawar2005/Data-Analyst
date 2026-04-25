# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

n = int(input())

for _ in range(n):
    name, addr = email.utils.parseaddr(input())
    
    if re.match(r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$', addr):
        print(email.utils.formataddr((name, addr)))