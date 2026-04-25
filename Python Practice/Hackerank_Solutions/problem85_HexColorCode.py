import re

n = int(input())
inside = False

for _ in range(n):
    line = input()
    
    if '{' in line:
        inside = True
        continue
    if '}' in line:
        inside = False
        continue
    
    if inside:
        matches = re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', line)
        for m in matches:
            print(m)