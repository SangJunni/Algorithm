from math import floor
x, n = map(int, input().split())
for _ in range(n):
    if x % 2 == 0:
        x = floor(x / 2) ^ 6
    else:
        x = (2 * x) ^ 6
print(x)