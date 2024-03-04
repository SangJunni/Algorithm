from collections import deque
n = int(input())
m = int(input())
connection = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
distance = [-1]*(n+1)
distance[1] = 0
q = deque([1])
while q:
    current = q.popleft()
    for node in connection[current]:
        if distance[node] == -1:
            distance[node] = distance[current] + 1
            q.append(node)
#print(distance)
print(n - distance.count(-1))
