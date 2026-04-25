f = open("file.txt")

# lines = f.readlines()   # type - list
# print(lines,type(lines))     # type - list


# line1 = f.readline() 
# print(line1,type(line1))   # type - str
# line2 = f.readline() 
# print(line2,type(line2))
# line3 = f.readline() 
# print(line1,type(line3))
# line4 = f.readline() 
# print(line1,type(line4))
  

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()