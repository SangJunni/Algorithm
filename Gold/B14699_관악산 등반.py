n, m = map(int, input().split())
shelter = [0] + list(map(int, input().split()))
sorted_shelter = [[num,height] for num, height in enumerate(shelter)]
sorted_shelter.sort(key=lambda x: x[1], reverse=True)

max_visit = [0]*(n+1)
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if shelter[a] > shelter[b]:
        graph[b].add(a)
    else:
        graph[a].add(b)

for i in range(n):
    start = sorted_shelter[i][0]
    visit = 0
    for node in graph[start]:
        visit = max(visit, max_visit[node])
    max_visit[start] = visit + 1

for i in range(1,n+1):
    print(max_visit[i])

