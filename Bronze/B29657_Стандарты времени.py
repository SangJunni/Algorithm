a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g, h, i = map(int, input().split())
result = [0,0,0]
seconds = g*b*c + h * c + i
result[0] = seconds // (e*f)
seconds %= e*f
result[1] = seconds // f
result[2] = seconds % f
print(*result)