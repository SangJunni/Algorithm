data = list(map(int, input().split()))
result = sum([x**2 for x in data])%10
print(result)