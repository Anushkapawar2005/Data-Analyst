
a = (1,2,5,6,False,"Anu")  
print(len(a))  # 6
print(a.count(6)) # 1
print(a.index(5)) # 2

T1 = (2,6,7,5)
T2 = (4,3,1,3)
print(sum(T1))  # 20
print(max(T1))  # 7
print(min(T1))  # 2

sorted_NUM = sorted(T1)
print(sorted_NUM)  # [2, 5, 6, 7]


combined = T1 + T2
print(combined)

t3 = ("hello",) * 3
print(t3)     # ('hello', 'hello', 'hello')

# in - checking for an item 
print(3 in T1)  # False

# slicing
print(a[1:4])   # (2, 5, 6)