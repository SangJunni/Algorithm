import math
PI = 3.14159265
N = int(input())
for _ in range(N):
    T, X = map(float, input().split())
    X = int(X)
    dist = 0
    left = T * 100 - (16.0 / math.sin(PI * X / 180.0))
    right = T * 100 + (16.0 / math.sin(PI * X / 180.0))
    step = 85.0 / math.tan(PI * X / 180.0)
    while dist < right:
        if left < dist < right:
            print("yes")
            break
        dist += step
    else:
        print("no")