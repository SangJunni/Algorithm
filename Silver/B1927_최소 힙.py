import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    op = int(input())
    if op == 0:
        if len(q)==0:
            print(0)
        else:
            print(q[0])
            heapq.heappop(q)
    else:
        heapq.heappush(q, op)