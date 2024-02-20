n = int(input())
for _ in range(n):
    data = input()
    score = 0
    streak = 0
    for i in data:
        if i =='O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)