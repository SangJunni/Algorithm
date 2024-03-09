from collections import deque
line = list(input())
queue = deque(line)
while queue:
    if queue[-1] != queue[0]:
        print(0)
        break
    if len(queue) == 1:
        queue.pop()
        continue
    queue.popleft()
    queue.pop()
else:
    print(1)