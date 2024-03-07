from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
data = list(map(int, input().split()))
result = bisect_right(data, x) - bisect_left(data, x)
print(result if result > 0 else -1)