n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
op = int(input())
for _ in range(op):
    command = list(map(int,  input().split()))
    if command[0] == 1:
        field[command[1]-1] = [field[command[1]-1][-1]] + field[command[1]-1][:-1]
    else:
        new_field = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_field[j][n-1-i] = field[i][j]
        field= [x[:] for x in new_field]
for i in range(n):
    print(*field[i])