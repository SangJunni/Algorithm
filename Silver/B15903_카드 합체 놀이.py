import heapq
n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))
for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    for i in range(2):
        heapq.heappush(cards, x+y)
print(sum(cards))