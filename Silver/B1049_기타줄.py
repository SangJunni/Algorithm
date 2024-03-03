n, m = map(int, input().split())
separate = []
sets = []
for i in range(m):
    a,b = map(int, input().split())
    separate.append(b)
    sets.append(a)
separate.sort()
sets.sort()
costs = 0
while n > 0:
    if n >=6:
        costs += min(sets[0],separate[0]*6)
        n -= 6
    else:
        costs += min(sets[0], separate[0] * n)
        n = 0
print(costs)