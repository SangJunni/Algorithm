dp = [0 for _ in range(5002)]
dp[0], dp[1] = 1, 1
for i in range(2,5002):
    c = 0
    for j in range(i):
        c += (dp[j] * dp[i-j-1]) % 1_000_000_007
    c %= 1_000_000_007
    dp[i] = c
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n+1])