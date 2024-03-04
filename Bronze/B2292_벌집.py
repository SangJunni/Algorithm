n = int(input())
total = 1
count = 1
if n == 1:
    print(1)
    exit()
while True:
    if total >= n:
        print(count - 1)
        break
    total += 6*(count-1)
    count += 1