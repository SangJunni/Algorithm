x1, x2, n = map(int, input().split())
gap = x1 - x2
if gap < 0:
    print('NO')
elif gap == 0 and n != 0:
    print('NO')
elif gap/2 < n:
    print('NO')
elif gap % 2 != 0:
    print('NO')
else:
    print('YES')