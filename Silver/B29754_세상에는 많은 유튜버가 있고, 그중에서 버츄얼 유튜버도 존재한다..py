n,m = map(int, input().split())
streams = {}
times = {}
result = []
for _ in range(n):
    name, day, stime, etime = input().split()
    day = int(day)
    if name not in streams:
        streams[name] = [0]*52
        times[name] = [0]*52
    sh, sm = map(int, stime.split(":"))
    eh, em = map(int, etime.split(":"))
    streams[name][(day-1)//7] += 1
    times[name][(day-1)//7] += eh*60 + em - (sh*60 + sm)
for name in streams:
    broadcast_every5times = sum([1 for x in streams[name] if x >= 5])
    broadcast_every60hours = sum([1 for x in times[name] if x >= 60*60])
    if broadcast_every5times == m//7 and broadcast_every60hours == m//7:
        result.append(name)
result.sort()
if result:
    for r in result:
        print(r)
else:
    print(-1)