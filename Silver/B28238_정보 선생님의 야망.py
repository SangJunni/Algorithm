from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
cases = defaultdict(int)
for _ in range(n):
    available = list(map(int, input().split()))
    if sum(available) < 2:
        continue
    case = [x for x in range(5) if available[x] == 1]
    for c in combinations(case, 2):
        cases[c] += 1
if cases:
    s_cases = sorted(cases, key=lambda x: cases[x])
    result = [1 if x in s_cases[-1] else 0 for x in range(5)]
    print(cases[s_cases[-1]])
    print(*result)
else:
    print(0)
    print(*[1, 1, 0, 0, 0])
