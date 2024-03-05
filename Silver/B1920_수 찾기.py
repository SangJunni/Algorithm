n = int(input())
data1 = list(map(int, input().split()))
data1.sort()
m = int(input())
data2 = list(map(int, input().split()))
for i in data2:
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) //2
        if data1[mid] == i:
            print(1)
            break
        elif i > data1[mid]:
            start = mid+ 1
            continue
        else:
            end = mid -1
            continue
    if start > end:
        print(0)