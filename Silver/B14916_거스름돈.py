n = int(input())
count = [-1]*(n+1)
count[0] = 0
for i in range(2, n+1):
    if i < 5:
        if count[i-2] != -1:
            count[i] = count[i-2] + 1
    else:
        temp = 100_000
        if count[i-2] != -1:
            temp = min(temp, count[i-2] + 1)
        if count[i-5] != -1:
            temp = min(temp, count[i-5] + 1)
        count[i] = temp
print(count[-1])