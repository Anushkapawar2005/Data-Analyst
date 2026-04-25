# Enter your code here. Read input from STDIN. Print output to STDOUT

def updateit(setA,s,command):
    if command=="update":
        setA.update(s)
    elif command == "difference_update":
        setA.difference_update(s)
    elif command == "intersection_update":
        setA.intersection_update(s)
    else:
        setA.symmetric_difference_update(s)
    return setA



a=int(input())
setA=set(map(int,input().split()))

for i in range(int(input())):
    command,len_of_set = input().split()
    s = set(map(int,input().split()))
    setA = updateit(setA,s,command)
print(sum(setA))