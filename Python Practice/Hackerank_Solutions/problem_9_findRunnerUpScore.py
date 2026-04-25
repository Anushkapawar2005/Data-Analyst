if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(set(arr))  # remove duplicates and converts into list
    arr.sort()    # sort in ascending order
    print(arr[-2])
    
    # arr.sort(reverse=True)  #sort in descending order
    # print(arr[1])
