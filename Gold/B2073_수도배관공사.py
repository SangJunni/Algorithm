import sys
INF = sys.maxsize
d, p = map(int, input().split())
dp = [sys.maxsize]+[0]*d
for _ in range(p):
    l, c = map(int, input().split())
    temp = dp[:]
    for i in range(l, d+1):
        if temp[i-l]:
            dp[i] = max(dp[i], min(temp[i-l], c))
print(dp[d])