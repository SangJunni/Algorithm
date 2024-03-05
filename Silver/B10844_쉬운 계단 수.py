n = int(input())
prev = [0] + [1]*9
for i in range(n-1):
    temp = [0]*10
    temp[1] += prev[0]
    temp[8] += prev[9]
    for j in range(1, 9):
        temp[j-1] += prev[j]
        temp[j+1] += prev[j]
    prev = temp[:]
print(sum(prev) % 1000000000)
