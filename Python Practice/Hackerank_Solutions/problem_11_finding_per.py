if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
avg = sum(student_marks[query_name]) / len(student_marks[query_name])
# sum for add marks and len is len for number of sub

print(f"{avg:.2f}")  # 2f for 2 decimal point
