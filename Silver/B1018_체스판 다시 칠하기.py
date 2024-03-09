n, m = map(int, input().split())
case1 = list('WB'*(m//2) + 'W'*(m % 2))
case2 = list('BW'*(m//2) + 'B'*(m % 2))
min_change =64
data = []
for i in range(n):
    data.append(list(str(input())))
#print(data)
for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        count2 = 0
        for col in range(8):
            for row in range(8):
                if col % 2 == 0:
                    if data[i+col][j+row] != case1[row]:
                        count1 +=1
                    else:
                        count2 +=1
                else:
                    if data[i+col][j+row] != case1[row]:
                        count2 +=1
                    else:
                        count1 +=1
        min_change = min(count1, count2, min_change)
        #print(count1, end=' ')
        #print(count2, end=' ')
        #print(min_change)
print(min_change)