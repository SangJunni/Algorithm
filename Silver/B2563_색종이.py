t = int(input())
field = [[0]*100 for _ in range(100)]
area = 0
for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            if field[i][j] == 0:
                area += 1
            field[i][j] = 1
print(area)