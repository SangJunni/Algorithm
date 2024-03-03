n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse = True)
total = 0
for coin in coins:
    value = k // coin
    total += value
    k -= value*coin
print(total)