n = int(input())
case = [0, 1, 2, 4]
for i in range(n):
    find = int(input())
    if find <=3:
        print(case[find])
    else:
        for j in range(len(case), find+1):
            case.append(case[j-1] + case[j-2] + case[j-3])
        print(case[find])