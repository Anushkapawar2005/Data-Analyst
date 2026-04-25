# Enter your code here. Read input from STDIN. Print output to STDOUT
a= int(input())
b= int(input())

q,r = divmod(a,b)
print(q,r,(q,r),sep="\n")