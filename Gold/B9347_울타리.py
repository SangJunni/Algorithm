from collections import deque, defaultdict as dd
import heapq as hq

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = float('inf')

for _ in range(int(input())):

    height, width = map(int, input().split())
    grid = [tuple(map(int, input().split())) for _ in range(height)]
    visit = [[INF] * width for _ in range(height)]
    is_inside = lambda x, y: 0 <= x < width and 0 <= y < height
    min_heap = []

    # Initialize the heap with the boundary cells
    for y in (0, height - 1):
        for x in range(width):
            cost = grid[y][x]
            hq.heappush(min_heap, (cost, x, y))
            visit[y][x] = cost

    for x in (0, width - 1):
        for y in range(height):
            cost = grid[y][x]
            hq.heappush(min_heap, (cost, x, y))
            visit[y][x] = cost

    # Process the grid using Dijkstra's algorithm
    while min_heap:
        current_cost, x, y = hq.heappop(min_heap)

        if current_cost > visit[y][x]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            next_cost = current_cost + 1

            if is_inside(nx, ny):
                if grid[ny][nx] and next_cost < visit[ny][nx]:
                    visit[ny][nx] = next_cost
                    hq.heappush(min_heap, (next_cost, nx, ny))
                elif not grid[ny][nx] and current_cost < visit[ny][nx]:
                    visit[ny][nx] = current_cost
                    hq.heappush(min_heap, (current_cost, nx, ny))

    dist = dd(int)
    for y in range(height):
        for x in range(width):
            if not grid[y][x]:
                dist[visit[y][x]] += 1

    answer = sorted(dist.items())
    print(*answer[-1])
