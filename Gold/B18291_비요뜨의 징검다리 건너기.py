import sys
input = sys.stdin.readline
t = int(input())
def solve(x):
    mod = 1000000007
    a = 2
    b = x
    ret = 1
    while b:
        if b % 2 == 1:
            ret *= a
            ret %= mod
        a *= a
        a %= mod
        b // 2
    return ret


for _ in range(t):
    n = int(input())
    if 0 < n < 2:
        print(1)
    else:
        x = n - 2
        print(solve(x))