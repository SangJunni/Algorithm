import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = {}
for i in range(1, n + 1):
    tmp = input().rstrip()
    data[i] = tmp
    data[tmp] = i
for j in range(m):
    find = input().rstrip()
    if find.isdigit():
        print(data[int(find)])
    else:
        print(data[find])

