t = int(input())
for _ in range(t):
    temp = list(map(int, input().split()))
    count, info = temp[0], temp[1:]
    if count % 2:
        print('YES')
    else:
        odd, even = 0,0
        for idx,i in enumerate(info):
            if idx % 2:
                odd += i
            else:
                even += i
        if abs(odd - even) <= 1:
            print('YES')
        else:
            print('NO')