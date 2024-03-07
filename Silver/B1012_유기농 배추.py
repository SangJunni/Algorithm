import sys
sys.setrecursionlimit(10**6)
#꼭 필요!!
def dfs(x, y, field):
    if x <= -1 or x >= len(field) or y <= -1 or y >= len(field[0]):
        return False
    if field[x][y] == 1:
        field[x][y] = 0
        dfs(x-1, y, field)
        dfs(x, y-1, field)
        dfs(x + 1, y, field)
        dfs(x, y+1, field)
        return True
    return False

case = int(input())
for _ in range(case):
    row, col, num = list(map(int, input().split()))
    field = [[0]*row for _ in range(col)]
    for _ in range(0, num):
        x, y = map(int, input().split())
        field[y][x] = 1
    result = 0
    for i in range(col):
        for j in range(row):
            if dfs(i, j, field) == True:
                result += 1
    print(result)
