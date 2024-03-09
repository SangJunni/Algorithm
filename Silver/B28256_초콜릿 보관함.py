from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
t = int(input())
for _ in range(t):
    field = [list(input()) for _ in range(3)]
    info = list(map(int, input().split()))
    result = []
    visited = [[0]*3 for _ in range(3)]
    visited[1][1] = 1
    for i in range(3):
        for j in range(3):
            if field[i][j] == 'O' and visited[i][j] == 0:
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                cnt = 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >=3 or ny >= 3 or visited[nx][ny] == 1 or field[nx][ny] == 'X':
                            continue
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        cnt += 1
                result.append(cnt)
    result.sort()
    if result == info[1:]:
        print(1)
    else:
        print(0)