n, x = map(int, input().split())
data = list(map(int, input().split()))
result = [a for a in data if a < x]
for r in result:
    print(r, end=' ')
print()