import math
k = int(input())
c = list(map(int, input().split()))
d = c[:]
m = c[:]
a, b, n = map(int, input().split())
if a == b:
    print(-1)
    exit()

for i in range(k + 1):
    multiplier = k - i
    if c[i] != 0:
        c[i] /= (multiplier + 1)  # 적분계수
        m[i] *= multiplier  # 미분계수

realValue = 0

for i in range(k + 1):
    tmp = 1
    multiplier = (k + 1) - i
    for _ in range(multiplier):
        tmp *= b
    realValue += (c[i] * tmp)

for i in range(k + 1):
    tmp = 1
    multiplier = (k + 1) - i
    for _ in range(multiplier):
        tmp *= a
    realValue -= (c[i] * tmp)

deltaX = (b - a) / n
realValue /= deltaX

e = deltaX  # 초기값 가정
for _ in range(5):
    gunction = 0
    dgunction = 0

    for sigma in range(n):
        v = a + sigma * deltaX + e
        for i in range(k + 1):
            tmp = 1
            multiplier = k - i
            for _ in range(multiplier):
                tmp *= v
            gunction += (d[i] * tmp)
            dgunction += (m[i] * (tmp / v))

    gunction -= realValue

    # Newton
    e = e - gunction / dgunction

print(f'{e:.6f}')

