# Q1. Find the most frequent element in a list
data = [1,2,2,3,3,3]
freq={}
for i in data:
  freq[i]=freq.get(i,0)+1

most_freq = max(freq,key=freq.get)
print(most_freq)    # 3