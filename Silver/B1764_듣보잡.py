n, m = map(int, input().split())
d1 = set()
d2 = set()
for _ in range(n):
    d1.add(str(input()))
for _ in range(m):
    d2.add(str(input()))
d3 = list(d1 & d2)
d3.sort()
print(len(d3))
for i in range(len(d3)):
    print(d3[i])
