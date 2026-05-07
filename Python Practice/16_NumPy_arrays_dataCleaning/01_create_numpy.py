import numpy as np

print("Creating Arrays: ")
arr = np.array([10,20,30,40,50,60,70])
print(arr)

print("\nIndexing & Slicing: ")
print(arr[1])
print(arr[0:2])

print("\nVectorized Operations: ")
print(arr + 10)  # In python use loop but with the help of numpy it is easy
print(arr * 2)
print(arr ** 2)

print("\nNumPy functions: ")
print(arr.sum())
print(arr.min())
print(arr.max())


print("\nData Cleaning Ex: ")
data = np.array([10,-20,30,-40,50])
clean = data[data>=0]
print("Cleaned:",clean)


print("\nMissing value: ")
marks = np.array([80,90,-1,75,-1,60])
marks[marks==-1]=marks[marks!= -1].mean()  # Replacing average of non negative values
print("Filled missing: ",marks)

cities = np.array([" mumbai ","PUNE","Delhi "," mUmBaI"])
cities = np.char.strip(cities)
cities=np.char.title(cities)
print(cities)