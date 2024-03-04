n, m = map(int, input().split())
set1 = [input() for _ in range(n)]
total = 0
for _ in range(m):
    temp = input()
    if temp in set1:
        total += 1
print(total)
        