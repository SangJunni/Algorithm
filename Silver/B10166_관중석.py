from math import gcd
d1, d2 = map(int, input().split())
dp = [[0]*d2 for _ in range(d2)]
count = 0
for i in range(d1,d2+1):
    for j in range(1, i+1):
        divider = gcd(i, j)
        denum, num = i//divider-1, j//divider-1
        if dp[denum][num] == 0:
            dp[denum][num] = 1
            count += 1
print(count)