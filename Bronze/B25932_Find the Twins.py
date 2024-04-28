n = int(input())
for _ in range(n):
    zack, mack = 0, 0
    game = list(map(int, input().split()))
    if 17 in game:
        zack = 1
    if 18 in game:
        mack = 1
    print(*game)
    if zack == 0 and mack == 0:
        print('none')
    elif zack == 1 and mack == 0:
        print('zack')
    elif zack == 0 and mack == 1:
        print('mack')
    else:
        print('both')
    print()