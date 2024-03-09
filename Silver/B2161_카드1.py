from collections import deque
n = int(input())
cards = deque([x for x in range(1, n+1)])
result = []
while cards:
    result.append(cards.popleft())
    if not cards:
        break
    temp = cards.popleft()
    cards.append(temp)
print(*result)