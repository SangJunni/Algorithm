n,a = map(int, input().split())
receipt = list(map(int, input().split()))
result = 0
for r in receipt:
    result += r//a
print(result)