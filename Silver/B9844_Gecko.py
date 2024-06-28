h, w = map(int, input().split())
field = [[0]+list(map(int, input().split())) + [0] for _ in range(h)]

for i in range(1, h):
    for j in range(1,w+1):
        field[i][j] += max(field[i - 1][j], field[i - 1][j + 1], field[i-1][j-1])

print(max(field[-1]))