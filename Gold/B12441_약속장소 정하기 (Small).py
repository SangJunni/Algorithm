import heapq
import sys

def dijkstra(graph, start, N):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def solve(test_cases):
    results = []

    for case_index, case in enumerate(test_cases):
        N, P, M, friends, roads = case
        graph = [[] for _ in range(N + 1)]

        for road in roads:
            D, L, cities = road
            for i in range(L - 1):
                u, v = cities[i], cities[i + 1]
                graph[u].append((v, D))
                graph[v].append((u, D))

        friend_times = []
        for X, V in friends:
            distances = dijkstra(graph, X, N)
            friend_times.append([distances[i] * V for i in range(1, N + 1)])

        min_time = float('inf')
        for city in range(1, N + 1):
            max_time = max(friend_times[f][city - 1] for f in range(P))
            min_time = min(min_time, max_time)

        if min_time == float('inf'):
            results.append(f'Case #{case_index + 1}: -1')
        else:
            results.append(f'Case #{case_index + 1}: {min_time}')

    return results

T = int(input())
test_cases = []

for _ in range(T):
    N, P, M = map(int, input().split())

    friends = []
    for _ in range(P):
        X, V = map(int, input().split())
        friends.append((X, V))
    roads = []
    for _ in range(M):
        temp = list(map(int,input().split()))
        D, L, cities = temp[0], temp[1], temp[2:]
        roads.append((D, L, cities))

    test_cases.append((N, P, M, friends, roads))

results = solve(test_cases)
for result in results:
    print(result)