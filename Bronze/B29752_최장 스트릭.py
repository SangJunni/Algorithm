n = int(input())
streak = 0
solved = list(map(int, input().split()))
temp = 0
for sol in solved:
    if sol == 0:
        streak = max(streak, temp)
        temp = 0
    else:
        temp += 1
streak = max(streak, temp)
print(streak)