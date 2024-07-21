n = int(input())
travel = list(map(int, input().split()))
cities = max(travel) + 1
visited = [-2]*cities
visited[travel[0]] = -1
for i in range(1,n):
    if visited[travel[i]] == -2:
        visited[travel[i]] = travel[i-1]
print(cities)
for i in range(cities):
    print(visited[i], end=' ')
