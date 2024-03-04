from collections import deque
n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
queue = deque()
queue.append((0, 0, 0))
field[0][0] = '0'
while queue:
    x, y, count = queue.popleft()
    if x == n-1 and y == m-1:
        print(count+1)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if field[nx][ny] != '0':
            field[nx][ny] = '0'
            queue.append((nx, ny, count+1))