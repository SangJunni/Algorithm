result = list(map(int, input().split()))
answer = 0
standard = max(result)
for r in result:
    if standard-1000 <= r < standard:
        answer += 1
print(answer)