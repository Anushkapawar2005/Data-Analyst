# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z = complex(input())
r, phi = cmath.polar(z)

print(r,phi,sep = '\n')