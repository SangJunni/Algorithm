from collections import deque, defaultdict as dd
import heapq as hq
import sys

input = lambda: sys.stdin.readline().rstrip()

dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
inf = 1e9

for _ in range(int(input())):

    Y, X = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(Y)]

    visit = [[inf] * X for _ in range(Y)]
    inside = lambda x, y: 0 <= x < X and 0 <= y < Y

    heap = []
    for y in (0, Y - 1):
        for x in range(X):
            crash = arr[y][x]
            hq.heappush(heap, (crash, x, y))
            visit[y][x] = crash
    for x in (0, X - 1):
        for y in range(Y):
            crash = arr[y][x]
            hq.heappush(heap, (crash, x, y))
            visit[y][x] = crash

    while heap:
        t, x, y = hq.heappop(heap)

        if t > visit[y][x]:
            continue

        for dx, dy in dire:
            nt, nx, ny = t + 1, x + dx, y + dy
            if inside(nx, ny):
                if arr[ny][nx] and nt < visit[ny][nx]:
                    visit[ny][nx] = nt
                    hq.heappush(heap, (nt, nx, ny))
                elif not arr[ny][nx] and t < visit[ny][nx]:
                    visit[ny][nx] = t
                    hq.heappush(heap, (t, nx, ny))

    dist = dd(int)
    for y in range(Y):
        for x in range(X):
            if not arr[y][x]:
                dist[visit[y][x]] += 1
    answer = list(sorted(dist.items()))
    print(*answer[-1])
