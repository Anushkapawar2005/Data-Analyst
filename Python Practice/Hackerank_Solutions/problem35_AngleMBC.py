# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

tita = (math.atan(AB/BC))
tita_to_degree = round(math.degrees(tita))
print(tita_to_degree,chr(176), sep='')