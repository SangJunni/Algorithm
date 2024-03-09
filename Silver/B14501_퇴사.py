n = int(input())
t = []
p = []
dp = [0]*(n+1)
for i in range(n):
    x,y = map(int, input().split())
    t.append(x)
    p.append(y)
pay = 0
#print(day_list)
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time<=n:
        dp[i]= max(p[i] + dp[time], pay)
        pay = dp[i]
    else:
        dp[i] = pay
print(pay)