n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
result = []
for i in range(n):
    count = 0
    for j in range(n):
        if i != j and data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    result.append(count+1)
print(*result)
            