count = 0
def dfs(graph, v, visited):
    visited[v] = True
    #print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



n, m = map(int, input().split())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    if visited[i] == False:
        dfs(graph, i, visited)
        count +=1
print(count)
