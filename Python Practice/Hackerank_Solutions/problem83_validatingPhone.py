# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(0,int(input())):
    string  = input()
    if(re.search(r"^[7,8,9][0-9]{9}$",string)):
        print("YES")
    else:
        print("NO")