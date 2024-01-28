n = int(input())
total = [0, 1, 2, 3, 5]
for i in range(len(total), n+1):
    total.append(total[i-2]+total[i-1])
print(total[n] %10007)