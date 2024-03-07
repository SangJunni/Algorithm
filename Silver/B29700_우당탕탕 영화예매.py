n, m, k = map(int, input().split())
field = [input() for _ in range(n)]
to_find = '0'*k
count = 0
for i in range(n):
    for j in range(m):
        if field[i][j:j+k] == to_find:
            count += 1
print(count)