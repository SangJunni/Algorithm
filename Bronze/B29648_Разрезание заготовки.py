a, b, s = map(int, input().split())
current, i = 0, max(a, b) + 1
while current < s:
    current = (i - a) * (i - b)
    i += 1
if current == s:
    print(i - 1)
else:
    print(-1)
