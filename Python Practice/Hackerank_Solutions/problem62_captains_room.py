# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
lst=list(map(int,input().split()))

s1=set() #unique row no
s2=set() #room no which appear more than once

for i in lst:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
    
s = s1.difference(s2)
print(*s)