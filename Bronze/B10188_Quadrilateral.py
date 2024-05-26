n = int(input())
for _ in range(n):
    r, c = map(int, input().split())
    for __ in range(c):
        print('X'*r)
    print()