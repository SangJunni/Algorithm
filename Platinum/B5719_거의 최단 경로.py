import sys
import heapq
from collections import deque
INF = sys.maxsize
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    start, end = map(int, input().split())
    edges = [[0 for _ in range(n)] for _ in range(n)]
    graph = [[] for _ in range(n)]
    inverse_graph = [[] for _ in range(n)]
    # 도로 정보 입력 받기
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        inverse_graph[b].append((a, cost))
    distance = [INF]*n
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0, start))
    while queue:
        c_cost, c_node = heapq.heappop(queue)
        if distance[c_node] < c_cost:
            continue
        for n_node, n_cost in graph[c_node]:
            if edges[c_node][n_node]:
                continue
            new_cost = n_cost + c_cost
            if distance[n_node] > new_cost:
                distance[n_node] = new_cost
                heapq.heappush(queue, (new_cost, n_node))
    queue = deque()
    queue.append(end)
    while queue:
        c_node = queue.popleft()
        if c_node == start:
            continue
        for p_node, p_cost in inverse_graph[c_node]:
            if distance[p_node] + p_cost == distance[c_node] and not edges[p_node][c_node]:
                edges[p_node][c_node] = True
                queue.append(p_node)
    distance = [INF] * n
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        c_cost, c_node = heapq.heappop(queue)
        if distance[c_node] < c_cost:
            continue
        for n_node, n_cost in graph[c_node]:
            if edges[c_node][n_node]:
                continue
            new_cost = n_cost + c_cost
            if distance[n_node] > new_cost:
                distance[n_node] = new_cost
                heapq.heappush(queue, (new_cost, n_node))
    if distance[end] == INF:
        print(-1)
    else:
        print(distance[end])