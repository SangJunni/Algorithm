n, x = map(int, input().split())
stamp = []
for _ in range(n):
    stamp.append(tuple(map(int, input().split())))
stamp.sort(key=lambda x: (-x[0], x[1]))
for s, t in stamp:
    if s + t <= x:
        print(s)
        break
else:
    print(-1)