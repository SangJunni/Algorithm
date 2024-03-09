import heapq
INF = int(1e9)
t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(t):
    #입력 설정과정
    n = int(input())
    distance = [[INF]*n for _ in range(n)]
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        x, y = 0, 0
        q = [(graph[x][y], x, y)]

        while q:
            dist, x, y = heapq.heappop(q)
            if distance[x][y] < dist:
                continue
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                cost = graph[nx][ny] + dist
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])