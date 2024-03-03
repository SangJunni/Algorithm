data = list(map(int, input()))
length = int(len(data)/2)
sum1 = sum(data[:length])
sum2 = sum(data[length:])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')