#1932
n = int(input())
data = [[0]*n for _ in range(n)]
data[0][0] = int(input())
for i in range(1,n):
    temp = list(map(int, input().split()))
    data[i][0:len(temp)] = temp
for i in range(1,n):
    for j in range(n):
        if j == 0 or i < j:
            left_side = 0
        elif i >= j:
            left_side = data[i-1][j-1]
        if i == j or i < j:
            right_side = 0
        elif i >= j:
            right_side = data[i-1][j]
        data[i][j] += max(left_side, right_side)
print(max(data[n-1]))
