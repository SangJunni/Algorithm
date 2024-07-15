n, x = map(int, input().split())
dp = [0]*(x+1)
dp[0] = 1
for _ in range(n):
    l, c = map(int, input().split())
    for y in range(x, -1, -1):
        for i in range(1, c+1):
            if y-i*l < 0:
                break
            dp[y] += dp[y-i*l]
print(dp[x])