from collections import defaultdict
t = int(input())
for _ in range(1,t+1):
    counter = defaultdict(int)
    n = int(input())
    line = list(map(int, input().split()))
    for l in line:
        counter[l] += 1
    for c in counter:
        if counter[c] == 1:
            print(f"Case #{_}: {c}")