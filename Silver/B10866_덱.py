import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
data = []
q= deque(data)
for i in range(n):
    op = list(map(str, input().split()))
    #print(op)
    #print(q)
    if op[0] =='push_front':
        q.appendleft(int(op[1]))
    elif op[0] == 'push_back':
        q.append(int(op[1]))
    elif op[0] == 'pop_front':
        if len(q)!=0:
            print(q[0])
            q.popleft()
        else:
            print(-1)
    elif op[0] == 'pop_back':
        if len(q)!=0:
            print(q[-1])
            q.pop()
        else:
            print(-1)
    elif op[0] == 'size':
        print(len(q))
    elif op[0] == 'empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif op[0] == 'back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])

