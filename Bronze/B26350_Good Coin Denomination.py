n = int(input())
for _ in range(n):
    line = list(map(int, input().split()))
    flag = 0
    for i in range(1, line[0]):
        if line[i]*2 > line[i+1]:
            flag = 1
            break
    print('Denominations:', end=' ')
    print(*line[1:])
    if flag:
        print('Bad coin denominations!')
    else:
        print('Good coin denominations!')
    print()
