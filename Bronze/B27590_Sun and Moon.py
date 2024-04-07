ds, ys = map(int,input().split())
dm, ym = map(int,input().split())
i = 1
while True:
    if (ds+i)%ys == 0 and (dm+i)%ym == 0:
        print(i)
        break
    i += 1