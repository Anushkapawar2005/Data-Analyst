# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
data = namedtuple("data",input())
marks_list = []
for i in range(n):
    marks = int(data(*input().split()).MARKS)
    marks_list.append(marks)
print(sum(marks_list)/n)