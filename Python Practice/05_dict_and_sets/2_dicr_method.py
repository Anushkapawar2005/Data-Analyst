marks = {
  "Anu":87,
  "Ram":98,
  "Seeta":78,
  0: "Anu"
}

print(marks.items())  # in tuples format in list 
# dict_items([('Anu', 87), ('Ram', 98), ('Seeta', 78), (0, 'Anu')])

print(marks.keys())  #print keys (left) 
# dict_keys(['Anu', 'Ram', 'Seeta', 0])

print(marks.values())  #print values (right)
marks.update({"Anu":80, "Renuka":99})
print(marks)

# print(marks.get("Ram2"))  #print None
# print(marks.["Ram2"])  #returns error

data = {'name':'Anushka','age' : 20}
print(data['name'])  # Anushka
print(data.get('city','NA'))  # NA
8
# Removing items

# print(data.pop('age'))  # 20
# print(data.popitem()) # remove last item  ('age', 20)
# del data['name']  # delete name
# data.clear()    # empties dict


print(data.setdefault('age',21))  # if age is exists, return it's value else sets 21
keys = ['a','b','c']
new_dict = dict.fromkeys(keys,0)
print(new_dict)     # {'a': 0, 'b': 0, 'c': 0}


# Dict Iteration
my_dict = {'a':1, 'b':2, 'c':3}
#iterate keys
for key in my_dict:
  print(key)
#iterate values
for value in my_dict.values():
  print(value)
#iterate items(key - value pairs)
for key, value in my_dict.items():
  print(key, value)