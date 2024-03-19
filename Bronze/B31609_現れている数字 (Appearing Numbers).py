n = int(input())
result = list(set(map(int,input().split())))
result.sort()
for r in result:
    print(r)