coins = [25,10,5,1]
t = int(input())
for _ in range(t):
    balance = int(input())
    count = [0, 0, 0, 0]
    for i in range(4):
        count[i] += balance//coins[i]
        balance %= coins[i]
    print(*count)