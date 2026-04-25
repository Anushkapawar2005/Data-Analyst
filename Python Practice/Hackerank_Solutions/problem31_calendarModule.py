# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
days_list = ['MONDAY', 'TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

m,d,y = map(int, input().split())
day_index = calendar.weekday(y,m,d)
print(days_list[day_index])