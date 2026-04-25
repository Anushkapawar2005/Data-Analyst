# Enter your code here. Read input from STDIN. Print output to STDOUT
en = int(input())
english = set(map(int,input().split()))

fr = int(input())
french = set(map(int,input().split()))

print(len(english.union(french)))