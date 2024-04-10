n = int(input())
for _ in range(n):
    m = int(input())
    total = 0
    for _ in range(m):
        _, count, price = input().split()
        total += int(count)*float(price)
    print(f'${total:.2f}')