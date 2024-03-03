from collections import deque
n = int(input())
field = [list(input()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0 for _ in range(n)] for _ in range(n)]


def bfs(count, x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for way in range(4):
            nx = x + dx[way]
            ny = y + dy[way]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 0 and field[nx][ny] == '1':
                visited[nx][ny] = 1
                count += 1
                queue.append((nx, ny))
    return count


total_count = 0
apartment = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and field[i][j] == '1':
            apartment.append(bfs(1, i, j))
            total_count += 1

print(total_count)
apartment.sort()
for ap in apartment:
    print(ap)
