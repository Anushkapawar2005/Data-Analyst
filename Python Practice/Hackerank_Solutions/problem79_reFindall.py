# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
Storage =re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])',input().strip(),re.IGNORECASE)
if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)