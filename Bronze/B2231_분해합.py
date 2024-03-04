n = int(input())
for i in range(n):
    data = list(str(i))
    temp = i
    for d in data:
        temp += int(d)
    if temp == n:
        print(i)
        exit()
print(0)
