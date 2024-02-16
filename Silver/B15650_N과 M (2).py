from itertools import combinations
n, m = map(int, input().split())
data = [x for x in range(1, n+1)]
case = list(combinations(data, m))
#print(case)
for a in case:
    for b in a:
        print(b, end=' ')
    print()