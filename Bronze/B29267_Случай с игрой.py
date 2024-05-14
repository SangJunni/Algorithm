current, save = 0,0
n, k = map(int, input().split())
for _ in range(n):
    temp = input()
    if temp == 'ammo':
        current += k
    elif temp == 'load':
        current = save
    elif temp == 'shoot':
        current = max(current-1, 0)
    else:
        save = current
    print(current)