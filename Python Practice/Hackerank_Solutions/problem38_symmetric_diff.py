# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_set = set(map(int,input().split()))
n = int(input())
n_set = set(map(int,input().split()))

m_diff_n = m_set.difference(n_set)
n_diff_m = n_set.difference(m_set)

result = list(m_diff_n) + list(n_diff_m)

sorted_res = sorted(result)
print(*sorted_res,sep = '\n')