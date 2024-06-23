a,b = 100,100
t = int(input())
for _ in range(t):
    r1, r2 = map(int, input().split())
    if r1 > r2:
        b -= r1
    elif r1 < r2:
        a -= r2
print(a)
print(b)