import heapq
t = int(input())
for _ in range(t):
    total = 0
    k = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    while len(files) != 1:
        f1 = heapq.heappop(files)
        f2 = heapq.heappop(files)
        total += f1 + f2
        heapq.heappush(files, f1 + f2)
    print(total)