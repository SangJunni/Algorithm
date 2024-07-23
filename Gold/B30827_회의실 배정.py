n, k = map(int,input().split())
meetings = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1])
rooms=[]
ans = 0
while meetings:
    start,end = meetings.pop()
    rooms.sort(reverse=True)
    for i in range(len(rooms)):
        if rooms[i] < start:
            rooms[i] = end
            ans += 1
            break
    else:
        if len(rooms) < k:
            ans += 1
            rooms += [end]
print(ans)