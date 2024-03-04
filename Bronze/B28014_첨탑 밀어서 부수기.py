n = int(input())
towers = list(map(int, input().split()))
count = 1
start = towers[0]
for tower in towers[1:]:
    if tower >= start:
        count += 1
        start = tower
    else:
        start = tower
print(count)