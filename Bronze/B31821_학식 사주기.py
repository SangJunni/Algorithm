n = int(input())
prices =[0]
for _ in range(n):
    prices.append(int(input()))
m = int(input())
counts = [0]*(n+1)
for _ in range(m):
    counts[int(input())] += 1
total = 0
for _ in range(1,n+1):
    total += counts[_]*prices[_]
print(total)