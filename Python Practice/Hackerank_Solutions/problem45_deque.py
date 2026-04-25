# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()

for i in range(int(input())):
    inp = input()
    if inp == "pop":
        d.pop()
    elif inp == "popleft":
        d.popleft()
    else:
        command, value = inp.split()
        value = int(value)
        if command == "append":
            d.append(value)
        else:
            d.appendleft(value)
print(*d)

