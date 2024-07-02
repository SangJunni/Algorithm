from math import gcd
from collections import defaultdict
n = int(input())
result = defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    z = gcd(x,y)
    x //= z
    y //= z
    result[(x,y)] += 1

print(max(result.values()))