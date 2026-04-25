def merge_the_tools(string, k):
    # your code goes here
    str = ''
    count = 0
    for i in string:
        if i not in str:
            str=str+i
        count+=1
        if count == k:
            count=0
            print(str)
            str=''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)