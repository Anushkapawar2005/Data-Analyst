import pandas as pd

df = pd.read_json("sample_Data.json")
print("Displaying  the info of data set")

print(df.info())