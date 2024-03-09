n, m = map(int, input().split())
data1 = []
data2 = []
for _ in range(n):
    data1.append(list(map(int, input().split())))
for i in range(n):
    data2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        print(data1[i][j] + data2[i][j], end = ' ')
    print()