n = int(input())
data = list(input())
r = 31
m = 1234567891
total = 0
for i in range(n):
    total += (ord(data[i])- ord('a') + 1)*r**i
print(total % m)