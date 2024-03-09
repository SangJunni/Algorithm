n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
first = num_list[n-1]
second = num_list[n-2]
sum = 0
while True:
    for i in range(k):
        if m == 0:
            break
        sum = sum + first
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1

print(sum)
