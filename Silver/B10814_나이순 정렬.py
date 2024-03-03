n = int(input())
data = []
for i in range(n):
    age, name = map(str, input().split())
    data.append((int(age), name))
data.sort(key = lambda x: x[0])
for i in range(n):
    print(data[i][0], end=' ')
    print(data[i][1])