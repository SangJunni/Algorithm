n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
hide = int(input())
dp = [field[x][:] for x in range(n)]
for i in range(1,m):
    dp[0][i] += dp[0][i-1]
for i in range(1,n):
    dp[i][0] += dp[i-1][0]
for i in range(1,n):
    for j in range(1,m):
        dp[i][j] += min(dp[i-1][j], dp[i][j-1])
if dp[-1][-1] <= hide:
    print('YES')
    print(dp[-1][-1])
else:
    print('NO')