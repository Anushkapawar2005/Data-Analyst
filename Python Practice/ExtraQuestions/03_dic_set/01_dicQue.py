# 1. Create dictionary from two lists
keys = ["name","age","city"]
values = ["Anushka",20,"Pune"]
d=dict(zip(keys,values))    
print(d)         # {'name': 'Anushka', 'age': 20, 'city': 'Pune'}

# Q2. Count frequency of elements in a list using dictionary
lst =[1,2,2,3,3,3]
freq={}
for i in lst:
  freq[i]=freq.get(i,0)+1
print(freq)     # {1: 1, 2: 2, 3: 3}

# Q3. Count frequency of characters in a string
s1="python"
freq={}
for ch in s1:
  freq[ch]=freq.get(ch,0)+1
print(freq)    # {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}


# Q4. Merge two dictionaries
d1= {"a":1,"b":2}
d2= {"c":3,"d":4}

d1.update(d2)
print(d1)     # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Q5. Remove duplicate values from dictionary
d= {"a":10,"b":20,"c":10}
result={}
for key,value in d.items():
  if value not in result.values():
    result[key]=value

print(result)      # {'a': 10, 'b': 20}


# Q6. Sort dictionary by keys
d = {"b": 2, "a": 1, "c": 3}
sorted_d = dict(sorted(d.items()))
print(sorted_d)       # {'a': 1, 'b': 2, 'c': 3}


# Q7. Sort dictionary by values
d = {"a": 30, "b": 10, "c": 20}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)     # {'b': 10, 'c': 20, 'a': 30}


# Q8. Find key with maximum value
d = {"Math": 80, "Science": 90, "English": 85}
print(max(d, key=d.get))   # Science

# Q9. Convert dictionary keys to list
d={"a":1,"b":2}
keys_list=list(d.keys())
print(keys_list)