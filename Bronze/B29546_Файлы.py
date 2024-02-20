n = int(input())
pic = [input() for _ in range(n)]
m = int(input())
for _ in range(m):
    s,e = map(int, input().split())
    for i in range(s-1,e):
        print(pic[i])