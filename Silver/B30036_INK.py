dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
I,N,K = map(int, input().split())
ink = input()
field = []
for i in range(N):
    line = list(input())
    for j in range(N):
        if line[j] == '@':
            box = (i,j)
    field.append(line)
command = list(input())
ink_idx = 0
ink_charge = 0
for c in command:
    # 잉크 충전
    if c == 'U':
        nx = box[0] + dx[0]
        ny = box[1] + dy[0]
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == '.':
            field[box[0]][box[1]] = '.'
            box = (nx, ny)
            field[box[0]][box[1]] = '@'
    elif c == 'D':
        nx = box[0] + dx[2]
        ny = box[1] + dy[2]
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == '.':
            field[box[0]][box[1]] = '.'
            box = (nx, ny)
            field[box[0]][box[1]] = '@'
    elif c == 'L':
        nx = box[0] + dx[1]
        ny = box[1] + dy[1]
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == '.':
            field[box[0]][box[1]] = '.'
            box = (nx, ny)
            field[box[0]][box[1]] = '@'
    elif c == 'R':
        nx = box[0] + dx[3]
        ny = box[1] + dy[3]
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == '.':
            field[box[0]][box[1]] = '.'
            box = (nx, ny)
            field[box[0]][box[1]] = '@'
    elif c == 'j':
        ink_charge += 1
    elif c == 'J':
        min_x, max_x = max(0, box[0] - ink_charge), min(N, box[0] + ink_charge+1)
        min_y, max_y = max(0, box[1] - ink_charge), min(N, box[1] + ink_charge+1)
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if abs(box[0] - i) + abs(box[1]-j) <= ink_charge and field[i][j] not in ['.', '@']:
                    field[i][j] = ink[ink_idx]
        ink_idx = (ink_idx+1) % I
        ink_charge = 0
for f in field:
    print(''.join(f))
