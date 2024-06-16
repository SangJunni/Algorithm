d, c, r = map(int, input().split())
fatigue = [int(input()) for _ in range(c)]
current = d
for _ in range(r):
    current += int(input())
answer = r
for f in fatigue:
    if f > current:
        break
    current -= f
    answer += 1
print(answer)