n = int(input())
info = list(map(int, input().split()))
max_val = max(info)
if max_val >= n:
    print(0)
else:
    another = n - max_val - 1
    for i in range(max_val+1):
        if another != 0:
            if i <= another - 1:
                if info.count(i) != 2:
                    print(0)
                    exit()
            else:
                if info.count(i) != 1:
                    print(0)
                    exit()
        else:
            if info.count(i) != 1:
                print(0)
                exit()
    if max_val+1 != another:
        print((2**another)*2)
    else:
        print(2**another)