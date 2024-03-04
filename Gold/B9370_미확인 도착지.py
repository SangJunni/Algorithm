import heapq
import sys
INF = sys.maxsize
t = int(input())
# 테스트 케이스
def dijkstra(start):
    queue = [[0,start]]
    dist = [INF]*(n+1)
    dist[start] = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if dist[node] < cost:
            continue
        for distance, next_node in graph[node]:
            if dist[next_node] > distance + cost:
                dist[next_node] = distance + cost
                heapq.heappush(queue,(distance + cost, next_node))
    return dist
for _ in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    destination = []
    for _ in range(t):
        destination.append(int(input()))
    dist_s = dijkstra(s)
    if dist_s[g] < dist_s[h]:
        via = h
    else:
        via = g
    dist_v = dijkstra(via)
    result  = []
    for dest in destination:
        if dist_s[via] + dist_v[dest] == dist_s[dest]:
            result.append(dest)
    print(*sorted(result))