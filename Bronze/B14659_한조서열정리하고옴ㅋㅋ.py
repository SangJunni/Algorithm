n = int(input())
peaks = list(map(int, input().split()))
idx = 0
answer, streak = 0, 0
for i in range(1,n):
    if peaks[i] < peaks[idx]:
        streak += 1
    else:
        idx = i
        answer = max(answer, streak)
        streak = 0
answer = max(answer, streak)
print(answer)