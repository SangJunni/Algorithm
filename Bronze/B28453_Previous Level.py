n = int(input())
result = []
players = list(map(int, input().split()))
for player in players:
    if player == 300:
        result.append(1)
    elif 275 <= player < 300:
        result.append(2)
    elif 250 <= player < 275:
        result.append(3)
    else:
        result.append(4)
print(*result)