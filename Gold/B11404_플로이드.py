n = int(input())
m = int(input())
INF = int(1e9)
cost = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n + 1):
    for j in range(1, n+1):
        if i == j:
            cost[i][j] = 0
for i in range(m):
    x, y, c = map(int, input().split())
    if c < cost[x][y]:
        cost[x][y] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()