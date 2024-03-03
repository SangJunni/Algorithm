n = int(input())
x = []
y = []
for _ in range(n):
    ix, iy = map(int, input().split())
    x.append(ix)
    y.append(iy)
x.append(x[0])
y.append(y[0])
xr = 0
yr = 0
for i in range(n):
    xr += x[i]*y[i+1]
    yr += y[i]*x[i+1]
print(round(abs(xr-yr)/2, 1))