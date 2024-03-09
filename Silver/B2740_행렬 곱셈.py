n, m = map(int, input().split())
matrixA = []
for _ in range(n):
    matrixA.append(list(map(int, input().split())))
m, k = map(int, input().split())
matrixB = [[] for _ in range(k)]
for _ in range(m):
    row = list(map(int, input().split()))
    for i in range(k):
        matrixB[i].append(row[i])
result = [[] for _ in range(n)]
for i in range(n):
    for j in range(k):
        temp = sum([matrixA[i][x] * matrixB[j][x] for x in range(m)])
        result[i].append(temp)
for i in range(n):
    print(*result[i])