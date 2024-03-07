from collections import defaultdict
data = list(input())
result = defaultdict(int)
for i in range(ord('a'),ord('z')+1):
    result[chr(i)] = 0
for d in data:
    result[d] += 1
print(*result.values())