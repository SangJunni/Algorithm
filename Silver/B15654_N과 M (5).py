#1148 S1
from itertools import permutations
n, m = map(int, input().split())
data = list(map(int, input().split()))
case = list(permutations(data, m))
case.sort()
#print(case)
for a in case:
    for b in a:
        print(b, end=' ')
    print()