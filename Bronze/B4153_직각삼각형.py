data = list(map(int, input().split()))
data.sort()
while data.count(0)!=3:
    print('right' if (data[0]**2 + data[1]**2) == data[2]**2 else 'wrong')
    data = list(map(int, input().split()))
    data.sort()