from collections import deque
n, m, start = map(int,input().split())
data = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
for i in range(1, n+1):
    data[i].sort()
visited = [False]*(n+1)
def dfs(data, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in data[start]:
        if not visited[i]:
            dfs(data, i, visited)

def bfs(dta, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        start = q.popleft()
        print(start, end=' ')
        for i in data[start]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(data, start, visited)
visited = [False]*(n+1)
print()
bfs(data, start, visited)