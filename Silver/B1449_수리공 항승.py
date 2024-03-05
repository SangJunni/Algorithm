n, l = map(int, input().split())
pos = sorted(list(map(int, input().split())))
count = 0
start = pos[0]
for p in pos[1:]:
    if p - start + 1 > l:
        start = p
        count += 1
print(count + 1)
