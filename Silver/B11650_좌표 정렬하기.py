n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort(key = lambda x: (x[0], x[1]))
for a, b in data:
    print(a, b)