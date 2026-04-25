s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# in python  1==1.0   - data types diff but it return true in py because value same

# problem 5
s = {}  # type dictionary not set
print(type(s))