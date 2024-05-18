k = int(input())
for _ in range(k):
    n,s,d = map(int, input().split())
    total = 0
    for __ in range(n):
        di,vi = map(int, input().split())
        if di/s <= d:
            total += vi
    print(f'Data Set {_+1}:')
    print(total)
    if _ != k-1:
        print()