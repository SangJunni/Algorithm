import math
t = int(input())
for _ in range(t):
    icecream = input()
    n3 = math.ceil(len(icecream)/3)
    s = icecream[:n3]
    condition = [s + s[::-1] + s, s+s[::-1][1:] + s, s+s[::-1] + s[1:], s + s[::-1][1:] + s[1:]]
    if icecream in condition:
        print(1)
    else:
        print(0)
