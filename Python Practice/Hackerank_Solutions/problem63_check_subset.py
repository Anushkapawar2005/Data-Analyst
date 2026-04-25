# Enter your code here. Read input from STDIN. Print output to STDOUT
num= int(input())

for _ in range(num):
    a_size=int(input())
    set_A= set(map(int,input().split()))
    b_size=int(input())
    set_B=set(map(int,input().split()))
    
    print(set_A.issubset(set_B))