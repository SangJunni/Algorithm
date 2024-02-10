from datetime import datetime
today = datetime(*list(map(int, input().split('-'))))
n = int(input())
result = 0
for _ in range(n):
    date = datetime(*list(map(int, input().split('-'))))
    if date >= today:
        result += 1
print(result)
