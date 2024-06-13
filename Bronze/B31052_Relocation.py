n,q = map(int, input().split())
pos = [0]+list(map(int, input().split()))
for _ in range(q):
    query, a, b = map(int, input().split())
    if query == 1:
        pos[a] = b
    else:
        print(abs(pos[a]-pos[b]))