n, k = map(int, input().split())
teams = []
for _ in range(n):
    temp = list(map(int, input().split()))
    if temp[0] == k:
        target = temp
    teams.append(temp)
teams.sort(key=lambda x: (-x[1], - x[2], -x[3]))
idx = teams.index(target)
for i in range(n):
    if teams[idx][1:] == teams[i][1:]:
        print(i+1)
        break