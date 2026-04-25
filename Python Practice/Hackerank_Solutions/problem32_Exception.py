# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)