
def con_f_to_c(f):
  return 5*(f-32)/9

f = int(input("Enter tem in F: "))
c = con_f_to_c(f)
print(f"Conver far to cel: {round(c,2)} Degree C")