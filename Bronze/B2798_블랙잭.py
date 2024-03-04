from itertools import combinations
n, m = map(int, input().split())
data = list(map(int, input().split()))
choices = combinations(data, 3)
max_num = 0
for choice in choices:
    current = sum(choice)
    if current <= m and current > max_num:
        max_num = sum(choice)
print(max_num)
