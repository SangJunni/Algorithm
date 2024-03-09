#백준에서 시간초과 발생 -> pypy3 혹은 sys 라이브러리 사용하기
from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
road_list = [[] for _ in range(n)]
for i in range(m):
    start, end = map(int, input().split())
    road_list[start-1].append(end -1)
distance = [-1] * n

def bfs(graph, start_point, distance):
    queue = deque([start_point])
    distance[start_point] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[v] + 1
    return distance


distance = bfs(road_list, x - 1, distance)
check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i + 1)
        check = True
if check == False:
    print(-1)
#result = [x for x, value in enumerate(distance) if value == k]
#if len(result) == 0:
#    print(-1)
#else:
#    for i in range(len(result)):
#        print(result[i] + 1)
#print(result)
#print(distance)

