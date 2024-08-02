t = int(input())
for _ in range(t):
    n = int(input())
    count, i = 0, 5
    while i <= n:
        count += n //i
        i *= 5
    print(count)