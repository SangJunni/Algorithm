num = list(map(int, input()))
total = num[0]
for i in range(1, len(num)):
    if num[i] <= 1 or total <= 1:
        total += num[i]
    else:
        total = total * num[i]
print(total)
