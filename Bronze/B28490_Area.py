n = int(input())
result = 0
for _ in range(n):
    w,h = map(int,input().split())
    result = max(result,w*h)
print(result)