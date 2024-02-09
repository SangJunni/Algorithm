n = int(input())
data = list(map(int, input().split()))
data.sort()
total = 0
for i in range(len(data), 0, -1):
    total += i*data[(i-len(data))*-1]
print(total)