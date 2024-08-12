from collections import deque
t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for _ in range(t):
    h,w,obstacles,force,start_x, start_y, end_x, end_y = map(int, input().split())
    field = [[0]*w for _ in range(h)]
    start_x, start_y, end_x, end_y = start_x - 1, start_y - 1, end_x - 1, end_y - 1
    for _ in range(obstacles):
        x, y, l = map(int, input().split())
        field[x-1][y-1] = l
    queue = deque()
    queue.append((start_x, start_y, force))
    visited = [[0]*w for _ in range(h)]
    visited[start_x][start_y] = 1
    while queue:
        x, y, f = queue.popleft()
        if x == end_x and y == end_y:
            print("잘했어!!")
            break
        if f <= 0:
            continue
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 범위를 벗어난 경우 or 이미 방문한 경우
            if new_x < 0 or new_x >= h or new_y < 0 or new_y >= w or visited[new_x][new_y]:
                continue
            # 장매물을 넘지 못하면 실격
            if f < field[new_x][new_y] - field[x][y]:
                continue
            queue.append((new_x, new_y, f-1))
            visited[new_x][new_y] = 1
    else:
        print("인성 문제있어??")

