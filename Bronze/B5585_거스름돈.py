money = 1000 - int(input())
coin_num = 0
coin_types = [500, 100, 50, 10, 5, 1]
for coin in coin_types:
    coin_num += money // coin
    money %= coin
print(coin_num)