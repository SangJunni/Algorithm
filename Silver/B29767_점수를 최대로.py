n, k = map(int, input().split())
rooms = list(map(int, input().split()))
info = [(0, rooms[0])]
for i in range(1,n):
    rooms[i] += rooms[i-1]
    info.append((i, rooms[i]))
info.sort(key = lambda x: (-x[1], -x[0]))
total = 0
for i in range(1,k+1):
    total += info[i-1][1]
print(total)