def average(array):
    # your code goes here
    s = set(array)
    l = len(s)
    s = sum(s)
    return round(s/l, 3)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)