a,b,c = map(int, input().split())
n = int(input())
status = [2]*(a+b+c+1)
analyze = []
for _ in range(n):
    result = list(map(int, input().split()))
    if result[-1] == 1:
        for i in range(3):
            status[result[i]] = 1
    else:
        analyze.append(result)
for i in range(len(analyze)):
    normal_status = 0
    for j in range(3):
        if status[analyze[i][j]] == 1:
            normal_status += 1
    if normal_status == 2:
        for j in range(3):
            if status[analyze[i][j]] == 2:
                status[analyze[i][j]] = 0

for i in range(1,a+b+c+1):
    print(status[i])