t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    arr = []
    for i in range(n+2):
        temp = []
        for j in range(m):
            if i == 0 or i==n+1:
                temp.append(0)
            else:
                temp.append(data[0])
                data.pop(0)
        arr.append(temp)
    #print(arr)
