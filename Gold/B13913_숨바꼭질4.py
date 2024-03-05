#13913
from collections import deque
n, k = map(int, input().split())
q = deque()
q.append(n)
count = [0] * (10**5 + 1)
visited = [0] * (10**5 + 1)
while q:
    tmp = q.popleft()
    if tmp == k:
        print(count[k])
        break
    for new in (tmp-1, tmp+1, tmp*2):
        if 0 <= new <= 10**5:
            if count[new] == 0:
                count[new] = count[tmp] + 1
                visited[new] = tmp
                #print(visited[:19])
                q.append(new)
course = [k]
temp = k
for _ in range(count[k]):
    temp = visited[temp]
    #print(temp)
    course.append(temp)

print(' '.join(map(str, course[::-1])))