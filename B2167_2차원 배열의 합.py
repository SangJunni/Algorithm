n, m = map(int, input().split())
array = [[0]*(m+1)]
for _ in range(n):
    array.append([0]+list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(1, m+1):
        array[i][j] += array[i-1][j] + array[i][j-1] -array[i-1][j-1]
cases = int(input())
for _ in range(cases):
    x1, y1, x2, y2 = map(int, input().split())
    print(array[x2][y2] - array[x2][y1-1] - array[x1-1][y2] + array[x1-1][y1-1])