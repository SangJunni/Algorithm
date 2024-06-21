x1, x2 = input().split('|')
y1, y2 = input().split('|')
if x1 in [y1, y2] or x2 in [y1, y2]:
    print('Yes')
else:
    print('No')