import heapq
n = int(input())
queue = []
for _ in range(n):
    val = float(input())
    heapq.heappush(queue, val)
for _ in range(7):
    print("{:.3f}".format(heapq.heappop(queue)))