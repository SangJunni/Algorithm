sudoku = [list(map(int, input().split())) for _ in range(9)]
find = []


def row(x, val):
    for i in range(9):
        if val == sudoku[x][i]:
            return 0
    return 1


def col(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return 0
    return 1


def box(x, y, val):
    sx = x // 3 * 3
    sy = y // 3 * 3
    for i in range(sx, sx + 3):
        for j in range(sy, sy + 3):
            if val == sudoku[i][j]:
                return 0
    return 1


def dfs(num):
    if num == to_find:
        for i in range(9):
            print(*sudoku[i])
        exit(0)
    for j in range(1, 10):
        x = find[num][0]
        y = find[num][1]
        if row(x, j) and col(y, j) and box(x, y, j):
            sudoku[x][y] = j
            dfs(num + 1)
            sudoku[x][y] = 0


for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            find.append([i, j])
to_find = len(find)
dfs(0)
