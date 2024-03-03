n,h= map(int, input().split())
rides = list(map(int, input().split()))
result = [1 if h >= x else 0 for x in rides]
print(sum(result))