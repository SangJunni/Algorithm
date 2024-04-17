n = int(input())
for _ in range(n):
    num, price = map(int, input().split())
    print(num,price)
    print(price + (price - 2)*(num-1))