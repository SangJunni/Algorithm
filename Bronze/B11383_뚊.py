n, m = map(int, input().split())
shorts = [input() for _ in range(n)]
longs = [input() for _ in range(n)]
for i in range(n):
    temp = ''.join([2*s for s in shorts[i]])
    if temp != longs[i]:
        print('Not Eyfa')
        break
else:
    print('Eyfa')