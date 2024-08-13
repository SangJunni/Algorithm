n, m = map(int, input().split())
college_type = [''] + list(input().split())
edges = []
for _ in range(m):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x: x[2])
parent = [x for x in range(n+1)]

def find_parents(x):
    if parent[x] == x:
        return x
    parent[x] = find_parents(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer,count = 0, 0
for a, b, cost in edges:
    if college_type[a] != college_type[b] and find_parents(a) != find_parents(b):
        union_parent(a,b)
        answer += cost
        count += 1
print(answer if count == n-1 else -1)