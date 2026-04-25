students  = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # extract scores
    scores = []
    for s in students:
        scores.append(s[1])
    # scores = [s[1] for s in students]

    first_lowest = min(scores)       # first lowest
    
    # make a list excluding first lowest
    new_list = []
    for s in scores:
        if s != first_lowest:
            new_list.append(s)

    second_lowest = min(new_list)
    # second_lowest = min([s for s in scores if s != first_lowest])

    # print students with second lowest score
    for name, score in sorted(students):
        if score == second_lowest:
            print(name)
