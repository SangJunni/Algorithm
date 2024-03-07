n, m, k = map(int, input().split())
result = []
for i in range(1,k+1):
    x, y = map(int, input().split())
    dist = x - 1 + m + 1 - y
    result.append((dist, i))
result.sort(key=lambda x: (x[0], x[1]))
print(result[0][1])