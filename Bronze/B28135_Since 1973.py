n = int(input())
count = 0
for i in range(1,n+1):
    if '50' in str(i) and i == n:
        count += 1
        break
    if '50' in str(i):
        count += 1
    count += 1
print(count)