n = int(input())
goal = [0] + list(map(int, input().split()))
problems = {1:[],2:[],3:[],4:[],5:[]}
for _ in range(n):
    diff, time = map(int, input().split())
    problems[diff].append(time)
total = 0
for i in range(1,6):
    problems[i].sort()
    total += problems[i][0]
    for j in range(1,goal[i]):
        total += 2*problems[i][j] - problems[i][j-1]
    total += 60
print(total-60)