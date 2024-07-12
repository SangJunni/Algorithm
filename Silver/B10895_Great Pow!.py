a, k = map(int, input().split())
if a == 1:
    print(1)
elif k == 0:
    print(a)
elif k != 0 and a % 2 == 0:
    print(1)
else:
    print(a)