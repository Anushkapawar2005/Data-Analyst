# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
eng_roll = set(list(map(int,input().split())))
french = int(input())
french_roll = set(map(int,input().split()))

print(len(eng_roll.difference(french_roll)))