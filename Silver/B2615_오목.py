#팔각이동:
directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
field = [list(map(int, input().split())) for _ in range(19)]
visited = [[0]*19 for _ in range(19)]
for i in range(19):
    for j in range(19):
        # 0 이 아닌 경우
        if field[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = 1
            for k in range(4):
                combo, total, l = [(i+1,j+1)], 1, 1
                # print(f'Start combo: {i,j}')
                while True:
                    next_x, next_y = i+l*directions[k][0], j + l*directions[k][1]
                    if (0 <= next_x < 19 and 0 <= next_y < 19) and field[next_x][next_y] == field[i][j]:

                        combo.append((next_x+1, next_y+1))
                        total += 1
                    else:
                        break
                    l += 1
                # print(total)
                if total == 5:
                    combo.sort(key=lambda x: (x[1], x[0]))
                    print(field[i][j])
                    print(*combo[0])
                    exit()
                elif total > 5:

                    for tx, ty in combo:
                        visited[tx-1][ty-1] = 1
print(0)