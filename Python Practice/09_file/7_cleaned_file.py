

# cleaning data in file
cleaned=[]
with open("file.txt","r") as f:
  for line in f:
    cleaned.append(line.strip().title())
 
with open("cleaned_output.txt","w") as f:
  for city in cleaned:
    f.write(city+"\n")